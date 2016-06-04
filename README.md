# footcode

A tool for extracting specific information from football-data.org.

(The code is not production-ready. Consider it a toy.)

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

## Security note

API provided by football-data.org uses HTTP. Your API key may leak due to the man-in-the-middle attack. You have been warned.
