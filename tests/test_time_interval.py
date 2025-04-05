from time_interval.date import Date
from time_interval.interval import Interval


def test_exact_100_days():
    date_1 = Date("2000-01-01")
    date_2 = Date("2000-01-02")
    interval = Interval(date_1, date_2)
    assert interval.interval() == 1
