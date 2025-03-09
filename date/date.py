start_date = "2025-12-31"


class Date:
    def __init__(self, time: str = "0"):
        self.time: int = time
        self.dateTime: bool = self._is_date(time)

    




# По ходу решения задачи ты будешь делать ветку с помощью команды git checkout -b изменять этот класс
# И я буду ревьювить код

date = Date()
print(date)
