import datetime as dt
from git_stats import ContributorStats, SortType, sort_stats


def test_sort_count() -> None:
    stats = (
        ContributorStats(
            name="foo",
            first_commit_date=dt.datetime(year=2000, month=1, day=2),
            last_commit_date=dt.datetime(year=2020, month=1, day=2),
            commit_count=6,
        ),
        ContributorStats(
            name="bar",
            first_commit_date=dt.datetime(year=2000, month=1, day=2),
            last_commit_date=dt.datetime(year=2010, month=1, day=2),
            commit_count=5,
        ),
        ContributorStats(
            name="baz",
            first_commit_date=dt.datetime(year=2000, month=1, day=2),
            last_commit_date=dt.datetime(year=2005, month=1, day=2),
            commit_count=7,
        ),
    )
    sorted_stats = tuple(sort_stats(stats, SortType.COUNT))

    assert sorted_stats[0].commit_count == 7
    assert sorted_stats[1].commit_count == 6
    assert sorted_stats[2].commit_count == 5


def test_sort_start() -> None:
    stats = (
        ContributorStats(
            name="foo",
            first_commit_date=dt.datetime(year=2010, month=1, day=2),
            last_commit_date=dt.datetime(year=2030, month=1, day=2),
            commit_count=3,
        ),
        ContributorStats(
            name="bar",
            first_commit_date=dt.datetime(year=2005, month=1, day=2),
            last_commit_date=dt.datetime(year=2030, month=1, day=2),
            commit_count=2,
        ),
        ContributorStats(
            name="baz",
            first_commit_date=dt.datetime(year=2020, month=1, day=2),
            last_commit_date=dt.datetime(year=2030, month=1, day=2),
            commit_count=1,
        ),
    )
    sorted_stats = tuple(sort_stats(stats, SortType.START))

    assert sorted_stats[0].first_commit_date == dt.datetime(year=2005, month=1, day=2)
    assert sorted_stats[1].first_commit_date == dt.datetime(year=2010, month=1, day=2)
    assert sorted_stats[2].first_commit_date == dt.datetime(year=2020, month=1, day=2)


def test_sort_duration() -> None:
    stats = (
        ContributorStats(
            name="one day",
            first_commit_date=dt.datetime(year=2000, month=1, day=2),
            last_commit_date=dt.datetime(year=2000, month=1, day=2),
            commit_count=3,
        ),
        ContributorStats(
            name="one year",
            first_commit_date=dt.datetime(year=2001, month=1, day=2),
            last_commit_date=dt.datetime(year=2002, month=1, day=2),
            commit_count=2,
        ),
        ContributorStats(
            name="ten years",
            first_commit_date=dt.datetime(year=2020, month=1, day=2),
            last_commit_date=dt.datetime(year=2030, month=1, day=2),
            commit_count=1,
        ),
    )
    sorted_stats = tuple(sort_stats(stats, SortType.DURATION))

    assert sorted_stats[0].name == "ten years"
    assert sorted_stats[1].name == "one year"
    assert sorted_stats[2].name == "one day"
