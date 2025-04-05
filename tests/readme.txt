Запуск:
    1 Создать виртульное окружение из корня проекта: python3 -m venv .venv
    2 Активировать его: source .venv/bin/activate
    3 Установить нужные пакеты: pip install -r requirements.txt
    4 Добавить в git ignore содержимое .venv: echo "*" > .venv/.gitignore
    5 Запуск тестов где $PATH это путь к файлу (можно указать всю папку с тестами): python3 -m pytest $PATH

Если делать команду: pip freeze > requirements.txt
Она перетрет локальный импорт пакета time_interval и остальных на git ссылку,
пока не разобрался как этого  исбежать (Отдельный файл с локальными пакетами?)


Команда запуска тестов где $PATH это путь к файлу (можно указать всю папку с тестами):
$ python -m pytest $PATH