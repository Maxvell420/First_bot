class Date:
    def __init__(self, time: str):
        [year, month, days] = self._parse_date(time)
        self._validation(year, month, days)

        self.current_point = 0

        self._days_passed_from_point(
            self.current_point, year=year, month=month, days=days
        )

        self.days = 0
        self.month = 0
        self.year = 0

    def _parse_date(self, time: str) -> list[int]:
        try:
            year = int(time.split("-")[0])
            month = int(time.split("-")[1])
            days = int(time.split("-")[2])
        except:
            raise TypeError("Не верный формат даты!")

        return [year, month, days]

    def getCurrentDate(self, days: int):
        # Из принятых дней возвращает 01-02-2025
        # month , year, days
        return [self.year, self.month, self.days]
        pass

    def _days_passed_from_point(
        self, point: int, year: int, month: int, days: int
    ) -> int:
        for i in range(point, self.year):
            self.year += 1
            all_days += self._num_all_days_year(i)

        self.current_point += self._num_days_from_the_new_year(days, month, year)

        return all_days

    def _validation(self, year: int, month: int, days: int):
        if 0 > year > 9999:
            raise ValueError("Дата не входит в допустимые границы")
        if 1 > month > 12:
            raise ValueError("Дата не входит в допустимые границы")
        if days > self._num_days_in_a_month(month, year) < 1:
            raise ValueError("Дата не входит в допустимые границы")

    def _verification_of_high_year(self, year):  # проверка на високосный год
        if year // 400 == 0:
            return True
        elif year / 4 * 10 % 10 == 0:
            return True
        else:
            return False

    def _num_days_in_a_month(
        self, month, year
    ):  # высчитывает кол. дней в месяце и прибавляет если високосный
        list_days_in_a_month = {
            1: 31,
            2: 28,
            3: 31,
            4: 30,
            5: 31,
            6: 30,
            7: 31,
            8: 31,
            9: 30,
            10: 31,
            11: 30,
            12: 31,
        }
        days = list_days_in_a_month[month]
        if self._verification_of_high_year(year) and month == 2:
            return days + 1
        else:
            return days

    def _num_all_days_year(self, year) -> int:  # кол. дней в году
        if self._verification_of_high_year(year):
            return 366
        else:
            return 365

    def _num_days_from_the_new_year(
        self, days: int, month: int, year: int
    ) -> int:  # рассчитывает кол. дней от нового года
        all_days = 0

        for i in range(1, month):
            self.month += 1
            all_days += self._num_days_in_a_month(i, year)
        all_days += days

        return all_days

    def out_days_from_the_new_year(self) -> str:  # для вывода кол. дней от нового года
        return f"Дней с нового года = {self._num_days_from_the_new_year(days= self.days, month= self.month, year= self.year)}"

    def add_days(self, days: int):
        current_point = self.current_point + days

        sum_days = self.days + days
        if sum_days > self._num_days_in_a_month(self.month, self.year):
            while sum_days > self._num_days_in_a_month(self.month, self.year):
                sum_days -= self._num_days_in_a_month(self.month, self.year)
                self.month += 1
                if self.month > 12:
                    self.year += 1
                    self.month = 1
            self.days = sum_days
        else:
            self.days = sum_days

    def add_month(self, month: int):
        sum_month = self.month + month
        if sum_month > 12:
            while sum_month > 12:
                self.year += 1
                sum_month -= 12

            self.month = sum_month
        else:
            self.month = sum_month

    def add_years(self, year: int) -> int:
        self.year += year
