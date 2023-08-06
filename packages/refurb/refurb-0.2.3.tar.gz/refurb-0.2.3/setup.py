# -*- coding: utf-8 -*-
from setuptools import setup

packages = \
['refurb',
 'refurb.checks',
 'refurb.checks.builtin',
 'refurb.checks.contextlib',
 'refurb.checks.flow',
 'refurb.checks.function',
 'refurb.checks.iterable',
 'refurb.checks.logical',
 'refurb.checks.pathlib',
 'refurb.checks.readability',
 'refurb.checks.string']

package_data = \
{'': ['*']}

install_requires = \
['mypy>=0.971,<0.972']

entry_points = \
{'console_scripts': ['refurb = refurb.__main__:main']}

setup_kwargs = {
    'name': 'refurb',
    'version': '0.2.3',
    'description': 'A tool for refurbish and modernize Python codebases',
    'long_description': '# Refurb\n\nA tool for refurbishing and modernizing Python codebases.\n\n## Example\n\n```python\n# main.py\n\nwith open("file.txt") as f:\n    contents = f.read()\n```\n\nRunning:\n\n```\n$ refurb main.py\ntmp.py:3:1 [FURB101]: Use `y = Path(x).read_text()` instead of `with open(x, ...) as f: y = f.read()`\n```\n\n## Installing\n\nBefore installing, it is recommended that you setup a [virtual environment](https://docs.python.org/3/tutorial/venv.html).\n\n```\n$ pip3 install refurb\n$ refurb file.py\n```\n\n## Installing (For Development)\n\n```\n$ git clone https://github.com/dosisod/refurb\n$ cd refurb\n$ make install\n$ make install-local\n```\n\nTests can be ran all at once with `make`, or you can run each tool on its own using\n`make black`, `make flake8`, and so on.\n\nUnit tests can be ran with `pytest` or `make test`.\n\n> Since the end-to-end (e2e) tests are slow, they are not ran when running `make test`.\n> You will need to run `make test-e2e` to run them.\n\n## Explainations For Checks\n\nYou can use `refurb --explain FURB123`, where `FURB123` is the error code you are trying to look up.\nFor example:\n\n````\n$ refurb --explain FURB123\nDon\'t cast a variable or literal if it is already of that type. For\nexample:\n\nBad:\n\n```\nname = str("bob")\nnum = int(123)\n```\n\nGood:\n\n```\nname = "bob"\nnum = 123\n````\n\n## Ignoring Certain Checks\n\nUse `--ignore 123` to ignore check 123. The error code can be in the form `FURB123` or `123`.\n\n## Configuring Refurb\n\nIn addition to the command line arguments, you can also add your settings in the `pyproject.toml` file.\nFor example, the following command line arguments:\n\n```\nrefurb file.py --ignore 100 --load some_dir\n```\n\nCorresponds to the following in your `pyproject.toml` file:\n\n```\n[tool.refurb]\nignore = [100]\nload = ["some_dir"]\n```\n\nAnd all you need to run is `refurb file.py`!\n\n> Note that `ignore` and `load` are the only supported options in the config file, since\n> all other command line options are one-offs, and don\'t make sense to be in the config file.\n\n## Writing Your Own Check\n\nIf you want to extend Refurb with your own custom checks, you can easily do so with\nthe `refurb gen` command. Note that this command uses the `fzf` fuzzy-finder for the\ngetting user input, so you will need to [install it](https://github.com/junegunn/fzf#installation)\nbefore continuing.\n\nThis is the basic overview of creating a new check using the `refurb gen` command:\n\n1. First select the node type you want to accept\n2. Then type in the path of where you want to put your check file\n3. Add your code to the generated file\n\n> To get an idea of what you need to do to get your check working the way you want it,\n> use the `--debug` flag to see the AST representation of a given file.\n\nTo run, use `refurb file.py --load your.path.here`\n\n> Note that when using `--load`, you need to use dots in your argument, just like\n> importing a normal python module.\n\n## Plugins (Coming Soon)\n\nWork is underway to make Refurb plugin-extensible.\n\n## Why Does This Exist?\n\nI love doing code reviews: I like taking something and making it better, faster, more\nelegant, and so on. Lots of static analysis tools already exist, but none of them seem\nto be focused on making code more elegant, more readable, more modern. That is what\nRefurb tries to do.\n\n## What Refurb Is Not\n\nRefurb is not a linter or a type checker. It is not meant as a first-line of defense for\nfinding bugs, it is meant for making nice code look even better.\n',
    'author': 'dosisod',
    'author_email': 'None',
    'maintainer': 'None',
    'maintainer_email': 'None',
    'url': 'https://github.com/dosisod/refurb',
    'packages': packages,
    'package_data': package_data,
    'install_requires': install_requires,
    'entry_points': entry_points,
    'python_requires': '>=3.10,<4.0',
}


setup(**setup_kwargs)
