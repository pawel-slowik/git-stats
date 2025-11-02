import datetime as dt
import pytest
from git_stats import ContributorStats, format_period, format_stat_line, format_stats


@pytest.mark.parametrize(
    "period,expected_output",
    (
        (dt.timedelta(), "1m"),
        (dt.timedelta(days=40), "1m"),
        (dt.timedelta(days=50), "2m"),
        (dt.timedelta(days=365), "1y"),
        (dt.date(year=2025, month=12, day=10) - dt.date(year=2022, month=7, day=5), "3y5m"),
    )
)
def test_format_period(period: dt.timedelta, expected_output: str) -> None:
    assert format_period(period) == expected_output


def test_format_stat_line() -> None:
    stats = ContributorStats(
        name="Test",
        first_commit_date=dt.datetime(year=2025, month=12, day=10),
        last_commit_date=dt.datetime(year=2026, month=12, day=10),
        commit_count=100,
    )

    assert format_stat_line(stats, 8) == "Test ___   100 2025/12     1y"


def test_output() -> None:
    stats = (
        ContributorStats(
            name="Angela Sáenz",
            first_commit_date=dt.datetime(year=2010, month=3, day=1),
            last_commit_date=dt.datetime(year=2017, month=5, day=1),
            commit_count=644,
        ),
        ContributorStats(
            name="Jaume Soriano",
            first_commit_date=dt.datetime(year=2010, month=3, day=1),
            last_commit_date=dt.datetime(year=2010, month=4, day=1),
            commit_count=9,
        ),
        ContributorStats(
            name="Salvador Jiménez",
            first_commit_date=dt.datetime(year=2010, month=3, day=1),
            last_commit_date=dt.datetime(year=2010, month=8, day=1),
            commit_count=2,
        ),
        ContributorStats(
            name="Cecilia Blázquez",
            first_commit_date=dt.datetime(year=2012, month=2, day=1),
            last_commit_date=dt.datetime(year=2012, month=3, day=1),
            commit_count=3,
        ),
        ContributorStats(
            name="Noah Sanhueza",
            first_commit_date=dt.datetime(year=2012, month=3, day=1),
            last_commit_date=dt.datetime(year=2016, month=8, day=1),
            commit_count=4984,
        ),
        ContributorStats(
            name="Noemi Ávila",
            first_commit_date=dt.datetime(year=2012, month=3, day=1),
            last_commit_date=dt.datetime(year=2015, month=12, day=1),
            commit_count=15,
        ),
        ContributorStats(
            name="Marcos Tejero",
            first_commit_date=dt.datetime(year=2012, month=3, day=1),
            last_commit_date=dt.datetime(year=2014, month=3, day=1),
            commit_count=120,
        ),
        ContributorStats(
            name="Africa Bilbao",
            first_commit_date=dt.datetime(year=2014, month=4, day=1),
            last_commit_date=dt.datetime(year=2014, month=5, day=1),
            commit_count=1,
        ),
        ContributorStats(
            name="Eneko Valverde",
            first_commit_date=dt.datetime(year=2014, month=5, day=1),
            last_commit_date=dt.datetime(year=2014, month=6, day=1),
            commit_count=11,
        ),
        ContributorStats(
            name="Carmen Maria Bermúdez",
            first_commit_date=dt.datetime(year=2020, month=5, day=1),
            last_commit_date=dt.datetime(year=2021, month=6, day=1),
            commit_count=3,
        ),
    )

    assert tuple(format_stats(stats)) == (
        "Angela Sáenz ____________   644 2010/03   7y2m",
        "Jaume Soriano ___________     9 2010/03     1m",
        "Salvador Jiménez ________     2 2010/03     5m",
        "Cecilia Blázquez ________     3 2012/02     1m",
        "Noah Sanhueza ___________  4984 2012/03   4y5m",
        "Noemi Ávila _____________    15 2012/03   3y9m",
        "Marcos Tejero ___________   120 2012/03     2y",
        "Africa Bilbao ___________     1 2014/04     1m",
        "Eneko Valverde __________    11 2014/05     1m",
        "Carmen Maria Bermúdez ___     3 2020/05   1y1m",
    )
