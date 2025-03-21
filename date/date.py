
class Date:
    def __init__(self, time: str):
        self.time: str = time
        if 0 >= len(time):
            time = "00-00-00"

        self.year =  int(time.split("-")[0])
        self.mounth =  int(time.split("-")[1])
        self.days = int(time.split("-")[2])

    def verification_of_high_year(self):
        year = self.year
        last_num_year = year % 10
        if year // 400 == 0:
            return True
        elif (last_num_year * 10 / 4) % 10 == 0:
            return True
        else:
            return False 

    def days_in_a_mounth(self, mounth):
        list_days_in_a_mounth = {1: 31, 2: 28, 3: 31, 4: 30, 5: 31, 
                                 6: 30, 7: 31, 8: 31, 9: 30, 10: 31,
                                 11: 30, 12: 31}
        days = list_days_in_a_mounth[mounth]
        if self.verification_of_high_year() == True and mounth == 2:
            days = days + 1
            return days
        else:
            return days
        
    
    def days_passed_NY(self):
        all_days = 0

        for i in range(1, self.mounth + 1):
            all_days += self.days_in_a_mounth(i)

        return f"Дней с нового года = {all_days}"



date = Date(str(input("Введите дату в формате гггг-мм-дд: ")))

print(date.days_passed_NY())