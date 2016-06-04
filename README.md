# footcode

A tool for extracting specific information from football-data.org.

## Dependencies

`footcode` uses Python 3 and libraries `tabulate` and `requests`. You can install them using `pip3 install requests tabulate`.

## Setting it up

Basically, all you need to start, is providing your API key in `config.py`.

```bash
cp config.py.sample config.py
editor config.py
```

## Running

Just execute `./cli.py`. **Warning**: it will overwrite file pointed by `csv_file` variable (see `config_cli.py`).
