import sys
import time

import requests

import config


def quit(msg):
    print(msg, file=sys.stderr)
    sys.exit(1)


def debug(msg):
    if config.verbose:
        print(msg, file=sys.stderr)


def get_request_header():
    return {'X-Auth-Token': config.api_key}


def call_api(resource_url):
    ''' Call API. Retry on failure. '''
    url = requests.compat.urljoin(config.url_base, resource_url)

    success = False
    tries = 0
    while not success and tries < config.max_tries:
        tries += 1
        try:
            r = requests.get(url, headers=get_request_header())
        except requests.exceptions.ConnectionError:
            quit('Connectior error.')
        if r.ok:
            success = True
        else:
            seconds = config.sleep_seconds
            if r.status_code == 429:
                # too many requests
                try:
                    seconds = int(r.headers['X-RequestCounter-Reset'])
                    seconds = max(1, seconds)  # sleep at least 1 second
                except KeyError:
                    pass
            debug('Connection problem. Retry in {} seconds.'.format(seconds))
            time.sleep(seconds)
    if success:
        try:
            return r.json()
        except:
            quit('Invalid response.')
    quit('Failed to fetch data from API.')


def get_current_league_table(season_id):
    return call_api('soccerseasons/{}/leagueTable'.format(season_id))


def team_to_market_value(team):
    try:
        team_info = call_api(team['_links']['team']['href'])
        return team_info['squadMarketValue']
    except KeyError:
        quit('Unknown data structure. API changed?')


def get_team_players(team_url):
    team_info = call_api(team_url)
    try:
        return call_api(team_info['_links']['players']['href'])
    except KeyError:
        quit('Unknown data structure. API changed?')
