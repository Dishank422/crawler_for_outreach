# crawler_for_outreach

Prerequisites:
1. [Pipenv](https://pypi.org/project/pipenv/)

To install Pipenv, run:
```shell
$ pip3 install pipenv
```
Clone this repo using
```shell
$ git clone https://github.com/Dishank422/crawler_for_outreach.git
```

To setup virtual environment:
```shell
$ cd crawler_for_outreach
$ pipenv install
```

To run the program, run:
```shell
$ pipenv shell
$ python crawler.py
```

To remove virtual environment
```shell
$ pipenv --rm
```

## How to use
Run the python script, enter the year. The program may take a few minutes to run, the papers which are not present in archive will be added to `pubs.csv`, please note that this script overwrites `pubs.csv`, the new list of papers is also appended to `archive.csv`.
