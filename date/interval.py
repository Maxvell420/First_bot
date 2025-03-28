from date_all_funk import Date

date_ = Date

class Interval:
    def __init__(self, time_1: str, time_2: str):
        self.time_1: str = time_1
        self.time_2: str = time_2
    
    def _calculation_interval(self, time_1: str, time_2: str):
        all_days = 0
        date_1 = date_(time_1)
        date_2 = date_(time_2)
        date_1_time = date_1.out_time()
        date_2_time = date_2.out_time()
        from_N_Y = date_1._num_days_from_the_new_year(date_1_time[2], date_1_time[1], date_1_time[0])
        all_days += from_N_Y
        before_N_Y = date_2._num_days_before_the_new_year(date_2_time[2], date_2_time[1], date_2_time[0])
        all_days += before_N_Y
        years = date_2_time[0] - date_1_time[0]
        for i in range(1 + date_1_time[0], years + date_1_time[0]):
            funkcia = date_(time_1)._num_all_days_year(i)              # вот этот момент работает, но time_1 там не учитывается
            all_days += funkcia   

        return all_days
        
    def out_num_interval(self):
        return f" С {self.time_1} по {self.time_2} прошло {self._calculation_interval(self.time_1, self.time_2)}"

