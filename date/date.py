
class Date:
    def __init__(self, time: str = "дата не указана"):
        self.time: str = time
        

    def days_of_the_year(self):
        
        return f"days_of_the_year"




# По ходу решения задачи ты будешь делать ветку с помощью команды git checkout -b изменять этот класс
# И я буду ревьювить код

date = Date("2025-03-09")
print(date.time)
print(date.days_of_the_year())
