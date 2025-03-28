class Date:
    def __init__(self, time: str):
        self._validation(time)
        self.year =  int(time.split("-")[0])
        self.month =  int(time.split("-")[1])
        self.days = int(time.split("-")[2])

    def _validation(self, time): 
        try:
            year =  int(time.split("-")[0])
            month =  int(time.split("-")[1])
            days = int(time.split("-")[2])
        except:
            raise TypeError("Не верный формат даты!")
        
        if 0 > year > 9999:
            self.year = year
            raise ValueError("Дата не входит в допустимые границы")
        if 1 > month > 12:
            self.month = month
            raise ValueError("Дата не входит в допустимые границы")
        if days > self._num_days_in_a_month(month, year):
            self.days = days
            raise ValueError("Дата не входит в допустимые границы")

    def _verification_of_high_year(self, year): # проверка на високосный год
        last_num_year = year % 10
        if year // 400 == 0:
            return True
        elif (last_num_year * 10 / 4) % 10 == 0:
            return True
        else:
            return False 

    def _num_days_in_a_month(self, month, year): # высчитывает кол. дней в месяце и прибавляет если високосный
        list_days_in_a_month = {1: 31, 2: 28, 3: 31, 4: 30, 5: 31, 
                                 6: 30, 7: 31, 8: 31, 9: 30, 10: 31,
                                 11: 30, 12: 31}
        days = list_days_in_a_month[month]
        if self._verification_of_high_year(year) and month == 2:
            return days + 1
        else:
            return days

    def _num_all_days_year(self, year): # кол. дней в году
        if self._verification_of_high_year(year):
            return 366
        else:
            return 365

    def _num_days_from_the_new_year(self, days:int, month:int, year:int): # рассчитывает кол. дней от нового года
        all_days = 0

        for i in range(1, month):
            all_days += self._num_days_in_a_month(i, year)
        all_days += days
 
        return all_days

    def _num_days_before_the_new_year(self, days_passed:int, month:int, year:int): # считает количество дней оставшихся до нового года
        all_days = 0
        for i in range(month, 13):
            days = self._num_days_in_a_month(i, year)
            all_days += days
        all_days = all_days - days_passed
        return all_days
    
    def out_days_from_the_new_year(self): # для вывода кол. дней от нового года
        return f"Дней с нового года = {self._num_days_from_the_new_year(days= self.days, month= self.month, year= self.year)}"

    def out_time(self):
        return (self.year, self.month, self.days)

