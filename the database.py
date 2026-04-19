import sqlite3

# Создание и подключение к БД
connection = sqlite3.connect('games.db')
cursor = connection.cursor()

cursor.execute("PRAGMA foreign_keys = ON")

# Удаляем старые таблицы 
cursor.execute("DROP TABLE IF EXISTS games")
cursor.execute("DROP TABLE IF EXISTS platforms")
cursor.execute("DROP TABLE IF EXISTS progress")


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

connection.commit()


