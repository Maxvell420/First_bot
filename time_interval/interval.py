from time_interval.date import Date


class Interval:
    def __init__(self, date_1=Date, date_2=Date):
        self.date_1 = date_1
        self.date_2 = date_2

    def interval(self) -> int:
        return (
            self.date_2.days_passed_zero_point() - self.date_1.days_passed_zero_point()
        )
