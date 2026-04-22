import sqlite3

# Создание и подключение к БД
connection = sqlite3.connect('games.db')
cursor = connection.cursor()

cursor.execute("PRAGMA foreign_keys = ON")

# Таблица 1: Платформы (3 столбца)

cursor.execute("""
CREATE TABLE platforms (
    id INTEGER PRIMARY KEY AUTOINCREMENT,
    name TEXT NOT NULL,
    company TEXT NOT NULL
)
""")

# Таблица 2: Прогресс (4 столбца)
cursor.execute("""
CREATE TABLE progress (
    id INTEGER PRIMARY KEY AUTOINCREMENT,
    status TEXT NOT NULL,
    hours_played INTEGER,
    rating INTEGER
)
""")

# Таблица 3: Игры (6 столбцов)
cursor.execute("""
CREATE TABLE games (
    id INTEGER PRIMARY KEY AUTOINCREMENT,
    title TEXT NOT NULL,
    platform_id INTEGER NOT NULL,
    genre TEXT NOT NULL,
    year INTEGER NOT NULL,
    progress_id INTEGER,
    FOREIGN KEY (platform_id) REFERENCES platforms(id),
    FOREIGN KEY (progress_id) REFERENCES progress(id)
)
""")

# Пользовательский ввод
print(" Введите название игры: ")
title = input()

print("Введите платформу: ")
platform_name = input()

print(" Введите жанр: ")
genre = input()

print(" Введите год выпуска: ")
year = int(input())

print(" Введите статус : ")
status = input()

print("Введите сколько часов наиграно: ")
hours = int(input())

print(" Введите оценку (1-10): ")
rating = int(input())

cursor.execute("""
INSERT INTO platforms (name, company) VALUES (?, ?)
""")

cursor.execute("""
INSERT INTO progress (status, hours_played, rating) VALUES (?, ?, ?)
""")

cursor.execute("""
INSERT INTO games (title, platform_id, genre, year, progress_id) VALUES (?, ?, ?, ?, ?)
""")

# Пользовательский ввод
print(" Введите название игры: ")
title = input()

print("Введите платформу: ")
platform_name = input()

print(" Введите жанр: ")
genre = input()

print(" Введите год выпуска: ")
year = int(input())

print(" Введите статус : ")
status = input()

print("Введите сколько часов наиграно: ")
hours = int(input())

print(" Введите оценку (1-10): ")
rating = int(input())

cursor.execute("""
INSERT INTO platforms (name, company) VALUES (?, ?)
""",(title,platform_name,genre,year))

cursor.execute("""
INSERT INTO progress (status, hours_played, rating) VALUES (?, ?, ?)
""",(status,hours,rating))

#Заполнение таблиц в вручную
cursor.execute("""
INSERT INTO games (title,platform_name,genre,year)
VALUES("Resident Evil 4","экшен","PC", 2026)
""")
cursor.execute("""
INSERT INTO games (title,platform_name,genre,year)
VALUES("The Sims 4","Симулятор"," PlayStation 4", 2014)
""")
cursor.execute("""
INSERT INTO games (title,platform_name,genre,year)
VALUES("The Elder Scrolls 5: Skyrim","фэнтези","PlayStation 3", 2011)
""")
cursor.execute("""
INSERT INTO games (title,platform_name,genre,year)
VALUES("Crimson Desert","ролевая игра","Xbox Series X", 2026)
""")
cursor.execute("""
INSERT INTO games (title,platform_name,genre,year)
VALUES("Perfect Dark","приключение","Xbox Game Studios", 2025)
""")

#Через случайные комбинации
platform_array=[(),(),(),(),(),(),
(),(),(),(),(),(),
(),(),(),(),(),(),
(),(),(),(),(),(),
(),(),(),(),(),()
]
cursor.execute("""
INSERT INTO platforms (name, company) VALUES (?, ?)
""",platform_array)

progress_array=[(),(),(),(),(),(),
(),(),(),(),(),(),
(),(),(),(),(),(),
(),(),(),(),(),(),
(),(),(),(),(),()
]
cursor.execute("""
INSERT INTO progress (status, hours_played, rating) VALUES (?, ?, ?)
""",progress_array)

games_array=[(),(),(),(),(),(),
(),(),(),(),(),(),
(),(),(),(),(),(),
(),(),(),(),(),(),
(),(),(),(),(),() 
]
cursor.execute("""
INSERT INTO games (title,platform_id,genre,year,progress_id ) VALUES (?, ?, ?, ? ,?)
""",games_array)

connection.commit()
connection.close()
