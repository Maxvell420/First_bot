from time_interval.date import Date
from time_interval.interval import Interval


def test_exact_1_days():
    date_1 = Date("2000-01-01")
    date_2 = Date("2000-01-02")
    interval = Interval(date_1, date_2)
    assert interval.interval() == 1


def test_exact_5000_days():
    date_1 = Date("2011-07-28")
    date_2 = Date("2025-04-05")
    interval = Interval(date_1, date_2)
    assert interval.interval() == 5000


def test_not_1_days():
    date_1 = Date("2011-07-28")
    date_2 = Date("2025-04-05")
    interval = Interval(date_1, date_2)
    assert interval.interval() != 1
