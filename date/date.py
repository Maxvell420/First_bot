start_date = "20-25-2025"


class Date:
    def __init__(self, time: str = "0"):
        self.time: int = time
        self.dateTime: bool = self._is_date(time)

    def _is_date(self, time: str):
        return str.isdecimal(time)

    def setTime(self, time: int):
        self.time = time

    def getTime(self):
        return self.time

    # def validateStart_date(self, start_date):
    #     if start_date == "not_valid":
    # Exception

    def getPassedDays(self):
        # some cool code
        return "Прошло 150 дней с начала года"


date = Date()
print(date)
