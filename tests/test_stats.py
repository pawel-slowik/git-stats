import datetime as dt
from git_stats import LogEntry, ContributorStats, gather_stats


def test_stats() -> None:
    log_entries = (
        LogEntry(name="foo", date=dt.datetime(year=2002, month=5, day=6, hour=7, minute=8)),
        LogEntry(name="bar", date=dt.datetime(year=2000, month=3, day=4, hour=5, minute=6)),
        LogEntry(name="foo", date=dt.datetime(year=2001, month=4, day=5, hour=6, minute=7)),
        LogEntry(name="foo", date=dt.datetime(year=2000, month=3, day=4, hour=5, minute=6)),
    )
    expected_stat_entries = (
        ContributorStats(
            name="foo",
            first_commit_date=dt.datetime(year=2000, month=3, day=4, hour=5, minute=6),
            last_commit_date=dt.datetime(year=2002, month=5, day=6, hour=7, minute=8),
            commit_count=3,
        ),
        ContributorStats(
            name="bar",
            first_commit_date=dt.datetime(year=2000, month=3, day=4, hour=5, minute=6),
            last_commit_date=dt.datetime(year=2000, month=3, day=4, hour=5, minute=6),
            commit_count=1,
        ),
    )
    stats = gather_stats(log_entries)

    assert len(stats) == len(expected_stat_entries)
    assert all(expected_stat_entry in stats for expected_stat_entry in expected_stat_entries)
