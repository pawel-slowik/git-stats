import datetime as dt
import pytest
from git_stats import format_period


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
