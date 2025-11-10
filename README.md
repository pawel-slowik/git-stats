This script displays contributor statistics for a Git repository.


## Requirements

Git and Python 3.x. For Python, only the standard library is required, there's
no need to install additional packages.

The script relies on authors' names being consistent throughout the entire
history of a repository. Inconsistencies can be worked around with a
[gitmailmap](https://git-scm.com/docs/gitmailmap).


## Installation

Download the `git_stats.py` file or clone the repository.


## Usage

    usage: git_stats.py [-h] [--sort {count,start,duration}] path [path ...]

    Show author commit statistics for a Git repository.

    positional arguments:
      path                  path to Git repository

    options:
      -h, --help            show this help message and exit
      --sort {count,start,duration}
                            display order

    Output includes author's name, commit count, date of first commit and activity
    period.


## Example output

    Angela Sáenz ____________   644 2010/03   7y2m
    Jaume Soriano ___________     9 2010/03     1m
    Salvador Jiménez ________     2 2010/03     5m
    Cecilia Blázquez ________     3 2012/02     1m
    Noah Sanhueza ___________  4984 2012/03   4y5m
    Noemi Ávila _____________    15 2012/03   3y9m
    Marcos Tejero ___________   120 2012/03     2y
    Africa Bilbao ___________     1 2014/04     1m
    Eneko Valverde __________    11 2014/05     1m
    Carmen Maria Bermúdez ___     3 2020/05   1y1m
