This script displays contributor statistics for a Git repository.


## Requirements

Git and Python 3.x. For Python, only the standard library is required, there's
no need to install additional packages.


## Installation

Download the `git_stats.py` file or clone the repository.


## Usage

    usage: git_stats.py [-h] [--sort {count,start,duration}] path

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

    Angela Sáenz 644 2010/03 7y2m
    Jaume Soriano 9 2010/03 1m
    Salvador Jiménez 2 2010/03 5m
    Cecilia Blázquez 3 2012/02 1m
    Noah Sanhueza 4984 2012/03 4y5m
    Noemi Ávila 15 2012/03 3y9m
    Marcos Tejero 120 2012/03 2y
    Africa Bilbao 1 2014/04 1m
    Eneko Valverde 11 2014/05 1m
    Carmen Maria Bermúdez 3 2020/05 1y1m
