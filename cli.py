#!/usr/bin/env python3

import csv

import tabulate

import config_cli as config
import footcode as fc


def is_polish_sounding(name):
    return ((name.endswith('ski') or name.endswith('cki')) and
            not ('v' in name or 'x' in name))


def sum_up_polish_players():
    players_header = ['Name', 'Team goals (total)',
                      'Team goals (home)', 'Team goals (away)']
    players = list()
    bundes = fc.get_current_league_table(config.league_id)
    for team in bundes['standing']:
        goals_total = team['goals']
        goals_home = team['home']['goals']
        goals_away = team['away']['goals']
        team_players = fc.get_team_players(team['_links']['team']['href'])
        for player in team_players['players']:
            name = player['name']
            if is_polish_sounding(name):
                players.append([name, goals_total, goals_home, goals_away])

    print(tabulate.tabulate(players, headers=players_header))


def sum_up_season():
    bundes = fc.get_current_league_table(config.league_id)

    teams = list()
    for team in bundes['standing']:
        market_value = fc.team_to_market_value(team)
        teams.append([team['teamName'], team['goals'], market_value])

    teams.sort(key=lambda t: t[1], reverse=True)

    with open(config.csv_file, 'w') as f:
        writer = csv.writer(f)
        teams_header = [['Name', 'Goals', 'Market value']]
        writer.writerows(teams_header)
        writer.writerows(teams)


def main():
    sum_up_polish_players()
    sum_up_season()


if __name__ == '__main__':
    main()
