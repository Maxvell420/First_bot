
class Date:
    def __init__(self, time: str):
        self._validation(time)

    def _validation(self, time): 
        try:
            year =  int(time.split("-")[0])
            month =  int(time.split("-")[1])
            days = int(time.split("-")[2])
        except:
            raise TypeError("Не верный формат даты!")
        
        if 0 <= year <= 9999:
            self.year = year
            if 1 <= month <= 12:
                self.month = month
                if days <= self._days_in_a_month(self.month, self.year):
                    self.days = days

                    return True
                else:
                    raise AttributeError("Дата не входит в допустимые границы")
            else:
             raise AttributeError("Дата не входит в допустимые границы")

        else:
          raise AttributeError("Дата не входит в допустимые границы")

    def _verification_of_high_year(self, year): # проверка на високосный год
        last_num_year = year % 10
        if year // 400 == 0:
            return True
        elif (last_num_year * 10 / 4) % 10 == 0:
            return True
        else:
            return False 

    def _days_in_a_month(self, month, year): # высчитывает кол. дней в месяце и прибавляет если високосный
        list_days_in_a_month = {1: 31, 2: 28, 3: 31, 4: 30, 5: 31, 
                                 6: 30, 7: 31, 8: 31, 9: 30, 10: 31,
                                 11: 30, 12: 31}
        days = list_days_in_a_month[month]
        if self._verification_of_high_year(year) and month == 2:
            return days + 1
        else:
            return days
    
    def _days_passed_NY(self, days, month, year): # рассчитывает кол. дней от нового года
        all_days = 0

        for i in range(1, month):
            all_days += self._days_in_a_month(i, year)
        all_days += days
 
        return all_days
        
    def date(self): # для вывода кол. дней от нового года
        return f"Дней с нового года = {self._days_passed_NY(days= self.days, month= self.month, year= self.year)}"

class Date_to_date(Date):
    def __init__(self, time_1: str, time_2: str):
        if self._validation(time_1) and self._validation(time_2):
            self.time_1 = time_1
            self.time_2 = time_2
            self.year_1 = int(time_1.split("-")[0])
            self.month_1 = int(time_1.split("-")[1])
            self.days_1 = int(time_1.split("-")[2])
            self.year_2 = int(time_2.split("-")[0])
            self.month_2 = int(time_2.split("-")[1])
            self.days_2 = int(time_2.split("-")[2])
            
            return 
        raise TimeoutError("Не верно введены данные!")
        
    def _initial_date(self): # сравнивает числа
        if self.year_1 < self.year_2:
            return True
        elif self.year_1 == self.year_2:
            if self.month_1 <= self.month_2:
                if self.days_1 < self.days_2:
                    return True
                elif self.days_1 == self.days_2:
                    raise ValueError("Введено одно и тоже число!")
        return False
    
    def _change_num(self): # меняет числа местами 1<2
        if self._initial_date():
            year_1 = self.year_1
            month_1 = self.month_1
            days_1 = self.days_1
            year_2 = self.year_2
            month_2 = self.month_2
            days_2 = self.days_2
        else:
            year_1 = self.year_2
            month_1 = self.month_2
            days_1 = self.days_2
            year_2 = self.year_1
            month_2 = self.month_1
            days_2 = self.days_1
        
        return (year_1, month_1, days_1,
                year_2, month_2, days_2)

    def _days_left_NY(self, days_passed, month, year): # считает количество дней оставшихся до нового года
        all_days = 0
        for i in range(month, 13):
            days = self._days_in_a_month(i, year)
            all_days += days
        all_days = all_days - days_passed
        return all_days
    
    def _all_days_year(self, year): # кол. дней в году
        if self._verification_of_high_year(year):
            return 366
        else:
            return 365
        
    def date_to_date(self): # кол. дней от даты до даты
        dates = self._change_num()
        years = dates[3] - dates[0]
        all_days = 0
        all_days += self._days_left_NY(days_passed= dates[2],month= dates[1],year= dates[0])
        all_days += self._days_passed_NY(days= dates[5], month= dates[4], year= dates[3])

        for i in range(1 + dates[0], years + dates[0]):
            all_days += self._all_days_year(i)

        return f" С {self.time_1} по {self.time_2} прошло {all_days}"


date_2 = Date_to_date("1996-06-11","2010-02-17")


print(date_2.date_to_date())
