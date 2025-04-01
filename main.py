from time_interval.date import Date
from time_interval.interval import Interval



date_1, date_2 = Date("2020-03-03"), Date("2025-03-13")
print(date_1.days, date_1.month, date_1.year)

intetrval_ = Interval(date_1, date_2)

print(intetrval_.interval())

date_1.add_days(200)
print(date_1.days, date_1.month, date_1.year)


date_1.add_month(16)
print(date_1.days, date_1.month, date_1.year)

print(intetrval_.interval())

date_2.add_years(5)
print(date_2.days, date_2.month, date_2.year)

print(intetrval_.interval())
