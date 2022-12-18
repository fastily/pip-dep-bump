# pip-dep-bump
[![Python 3.9+](https://upload.wikimedia.org/wikipedia/commons/4/4f/Blue_Python_3.9%2B_Shield_Badge.svg)](https://www.python.org)
[![License: GPL v3](https://upload.wikimedia.org/wikipedia/commons/8/86/GPL_v3_Blue_Badge.svg)](https://www.gnu.org/licenses/gpl-3.0.en.html)

Bumps requirements.txt deps and updates them in the current virtualenv

```
usage: __main__.py [-h] [-r requirements.txt] [-d]

pip-dep-bump CLI

optional arguments:
  -h, --help           show this help message and exit
  -r requirements.txt  The requirements.txt file to work off of. Default is ./requirements.json
  -d                   Dry run, print contents of new requriements.txt
```