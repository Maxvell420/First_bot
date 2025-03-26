
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
                if days <= self.days_in_a_month(self.month, self.year):
                    self.days = days

                    return True
                else:
                    raise AttributeError("Дата не входит в допустимые границы")
            else:
             raise AttributeError("Дата не входит в допустимые границы")

        else:
          raise AttributeError("Дата не входит в допустимые границы")

    def verification_of_high_year(self, year): # проверка на високосный год
        last_num_year = year % 10
        if self.year // 400 == 0:
            return True
        elif (last_num_year * 10 / 4) % 10 == 0:
            return True
        else:
            return False 

    def days_in_a_month(self, month, year): # высчитывает кол. дней в месяце и прибавляет если високосный
        list_days_in_a_month = {1: 31, 2: 28, 3: 31, 4: 30, 5: 31, 
                                 6: 30, 7: 31, 8: 31, 9: 30, 10: 31,
                                 11: 30, 12: 31}
        days = list_days_in_a_month[month]
        if self.verification_of_high_year(year) and self.month == 2:
            return days + 1
        else:
            return days
    
    def days_passed_NY(self): # рассчитывает кол. дней от нового года
        all_days = 0

        for i in range(1, self.month):
            all_days += self.days_in_a_month(i)

        all_days += self.days
 
        if self.year != 0:
            return f"Дней с нового года = {all_days}"
        else:
            return f"Данные введены не верно"

class Date_to_date(Date):
    def __init__(self, time_1: str, time_2: str):
        if self._validation(time_1) and self._validation(time_2):
            self.year_1 = int(time_1.split("-")[0])
            self.month_1 = int(time_1.split("-")[1])
            self.days_1 = int(time_1.split("-")[2])
            self.year_2 = int(time_2.split("-")[0])
            self.month_2 = int(time_2.split("-")[1])
            self.days_2 = int(time_2.split("-")[2])
            
            return 
        raise TimeoutError("Не верно введены данные!")
    
    def _Initial_date(self): # сравнивает числа
        if self.year_1 <= self.year_2:
            if self.month_1 == self.month_2:
                if self.days_1 < self.days_2:
                    return True
            elif self.month_1 < self.month_2:
                return True
        return False
    
    def _days_left_NY(self, days_passed, month, year): # считает количество дней оставшихся до нового года
        all_days = 0
        for i in range(month, 13):
            days = self.days_in_a_month(year)
            all_days += days
        all_days = all_days - days_passed
        return all_days
    
    def date_to_date(self):


        


date_2 = Date_to_date("2024-02-24","2025-03-02")
print(date_2._Initial_date())
