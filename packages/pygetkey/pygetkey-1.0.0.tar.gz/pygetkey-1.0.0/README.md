# getkey

A Python module to get the pressed key

## Installation

### From PyPI

```sh
pip3 install pygetkey
```

### From GitHub

```sh
pip3 install git+https://github.com/donno2048/getkey
```

## Usage

```py
import getkey
getkey.get_key() # Wait for a key to be pressed and return it
getkey.get_last_key() # Don't wait for a key to be pressed and return the last pressed key (mainly for "async" loops)
```
