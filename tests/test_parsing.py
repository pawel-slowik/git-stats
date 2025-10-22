import datetime as dt
from git_stats import LogEntry, parse_log, parse_line


def test_parse_log() -> None:
    log = (
        "2025-10-08T15:36:15+01:00 Test",
        "2025-10-08T15:36:16+01:00 Foo Bar Baz",
        "2025-10-08T15:36:14+01:00 !",
    )
    entries = tuple(parse_log(log))

    assert len(entries) == 3
    assert all(isinstance(e, LogEntry) for e in entries)


def test_parse_line() -> None:
    entry = parse_line("2025-10-08T15:36:16+01:00 Foo Bar Baz")

    assert entry.name == "Foo Bar Baz"
    assert entry.date == dt.datetime(
        year=2025,
        month=10,
        day=8,
        hour=15,
        minute=36,
        second=16,
        tzinfo=dt.timezone(dt.timedelta(hours=1)),
    )
