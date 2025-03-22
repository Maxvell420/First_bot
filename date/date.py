
class Date:
    def __init__(self, time: str):
        self.time: str = time
        self.__verification(time)
        
    def __verification(self, time): # проверка заполненных данных, если проверка не пройтена,
                                    # то в функции days_passed_NY выведется сообщение(работает от значения года)
        try:
            self.year =  int(time.split("-")[0])
            self.month =  int(time.split("-")[1])
            self.days = int(time.split("-")[2])
        except:
            self.days = 0
            self.month = 0
            self.year = 0      
        
        if 1000 <= self.year <= 9999 and 1 <= self.month <= 12 and 1 <= self.days <= 31:
            return True
        else:
            self.days = 0
            self.month = 0
            self.year = 0
            return False

    def verification_of_high_year(self): # проверка на високосный год
        year = self.year
        last_num_year = year % 10
        if year // 400 == 0:
            return True
        elif (last_num_year * 10 / 4) % 10 == 0:
            return True
        else:
            return False 

    def days_in_a_month(self, month): # высчитывает кол. дней в месяце и прибавляет если високосный
        list_days_in_a_month = {1: 31, 2: 28, 3: 31, 4: 30, 5: 31, 
                                 6: 30, 7: 31, 8: 31, 9: 30, 10: 31,
                                 11: 30, 12: 31}
        days = list_days_in_a_month[month]
        if self.verification_of_high_year() and month == 2:
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
    def prov(self):
        return f"вот: {self.days}"

#date = Date(str(input("Введите дату в формате гггг-мм-дд: ")))
#print(date.days_passed_NY())

date_2 = Date_to_date("2025-03-01")
print(date_2.days_passed_NY())