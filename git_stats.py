#!/usr/bin/env python3

from __future__ import annotations
from dataclasses import dataclass
from operator import attrgetter
from enum import Enum
from itertools import chain
import datetime as dt
import subprocess
import argparse
from typing import Mapping, MutableMapping, Sequence, Iterable


@dataclass(frozen=True)
class LogEntry:
    name: str
    date: dt.datetime


def read_log(repo_path: str) -> Iterable[str]:
    git_command = (
        "git",
        "log",
        "--format=tformat:%aI %aN",
    )
    env: Mapping[str, str] = {}
    process = subprocess.run(git_command, capture_output=True, check=True, cwd=repo_path, env=env)
    return (input_line.decode("utf-8") for input_line in process.stdout.splitlines())


def parse_log(log_lines: Iterable[str]) -> Iterable[LogEntry]:
    for log_line in log_lines:
        yield parse_line(log_line)


def parse_line(line: str) -> LogEntry:
    parts = line.split(maxsplit=1)
    if len(parts) != 2:
        raise ValueError
    return LogEntry(
        name=parts[1].strip(),
        date=dt.datetime.fromisoformat(parts[0]),
    )


@dataclass(frozen=True)
class ContributorStats:
    name: str
    first_commit_date: dt.datetime
    last_commit_date: dt.datetime
    commit_count: int

    @property
    def activity_period(self) -> str:
        return format_period(self.last_commit_date - self.first_commit_date)

    @property
    def start_of_activity(self) -> str:
        return self.first_commit_date.strftime("%Y/%m")


def format_period(period: dt.timedelta) -> str:
    year = dt.timedelta(days=365)
    month = dt.timedelta(days=30)
    years, years_remainder = divmod(period, year)
    months = round(years_remainder / month)
    if months == 0 and years == 0:
        months = 1
    ret_years = str(years) + "y" if years > 0 else ""
    ret_months = str(months) + "m" if months > 0 else ""
    return ret_years + ret_months


def gather_stats(log_entries: Iterable[LogEntry]) -> Sequence[ContributorStats]:
    contributor_stats: MutableMapping[str, ContributorStats] = {}
    for log_entry in log_entries:
        name = log_entry.name
        if name not in contributor_stats:
            contributor_stats[name] = ContributorStats(
                name=name,
                first_commit_date=log_entry.date,
                last_commit_date=log_entry.date,
                commit_count=1,
            )
        else:
            previous_stats = contributor_stats[name]
            contributor_stats[name] = ContributorStats(
                name=name,
                first_commit_date=min(previous_stats.first_commit_date, log_entry.date),
                last_commit_date=max(previous_stats.last_commit_date, log_entry.date),
                commit_count=previous_stats.commit_count + 1,
            )
    return tuple(contributor_stats.values())


class SortType(Enum):
    COUNT = "count"
    START = "start"
    DURATION = "duration"


def sort_stats(
        stats: Iterable[ContributorStats],
        sort_type: SortType,
    ) -> Iterable[ContributorStats]:
    if sort_type == SortType.COUNT:
        return sorted(stats, key=attrgetter("commit_count"), reverse=True)
    if sort_type == SortType.START:
        return sorted(stats, key=attrgetter("first_commit_date"))
    if sort_type == SortType.DURATION:
        return sorted(
            stats,
            key=lambda entry: entry.last_commit_date - entry.first_commit_date,
            reverse=True,
        )
    raise ValueError


def format_stats(stats: Iterable[ContributorStats]) -> Iterable[str]:
    stats = tuple(stats)
    name_column_width = max_name_length(stats) + 4
    return (format_stat_line(stat, name_column_width) for stat in stats)


def max_name_length(stats: Iterable[ContributorStats]) -> int:
    return max(map(lambda stat: len(stat.name), stats))


def format_stat_line(stat: ContributorStats, name_column_width: int) -> str:
    return (
        f"{stat.name} {'_' * (name_column_width - len(stat.name) - 1)}"
        f" {stat.commit_count:5} {stat.start_of_activity} {stat.activity_period: >6}"
    )


def main() -> None:
    parser = argparse.ArgumentParser(
        description="Show author commit statistics for a Git repository.",
        epilog="""
            Output includes author's name, commit count, date of first commit and activity period.
        """,
    )
    parser.add_argument("path", nargs="+", help="path to Git repository")
    parser.add_argument(
        "--sort",
        choices=("count", "start", "duration",),
        default="start",
        help="display order",
    )
    args = parser.parse_args()
    log_lines = chain.from_iterable(map(read_log, args.path))
    stats = gather_stats(parse_log(log_lines))
    for line in format_stats(sort_stats(stats, SortType(args.sort))):
        print(line)


if __name__ == "__main__":
    main()
