import sqlite3

# Создание и подключение к базе данных
conn = sqlite3.connect('students.db')
cursor = conn.cursor()

# Создание таблицы студент
cursor.execute('''
CREATE TABLE IF NOT EXISTS student (
    id INTEGER PRIMARY KEY,
    hobby TEXT,
    first_name TEXT,
    last_name TEXT,
    birth_year INTEGER,
    homework_score INTEGER
)
''')

# Добавление 10 студентов
students = [
    ('Reading', 'John', 'Smith', 1995, 9),
    ('Gaming', 'Alice', 'Johnson', 1996, 11),
    ('Swimming', 'Robert', 'Brown', 1994, 7),
    ('Painting', 'Michael', 'Williams', 1997, 13),
    ('Hiking', 'Mary', 'Jones', 1993, 15),
    ('Writing', 'Patricia', 'Garcia', 1998, 5),
    ('Cycling', 'Jennifer', 'Miller', 1999, 17),
    ('Dancing', 'James', 'Martinez', 1992, 8),
    ('Running', 'Linda', 'Hernandez', 1991, 12),
    ('Singing', 'David', 'Lopez', 1990, 10)
]

cursor.executemany('''
INSERT INTO student (hobby, first_name, last_name, birth_year, homework_score)
VALUES (?, ?, ?, ?, ?)
''', students)

# Достать всех студентов, у которых фамилия больше 10 символов
cursor.execute('''
SELECT * FROM student WHERE LENGTH(last_name) > 10
''')
long_last_names = cursor.fetchall()
print("Студенты с фамилией более 10 символов:")
for student in long_last_names:
    print(student)

# Изменить имена всех студентов, у которых балл больше 10 на 'Genius'
cursor.execute('''
UPDATE student SET first_name = 'Genius' WHERE homework_score > 10
''')
conn.commit()

# Вывести всех студентов с именем 'Genius'
cursor.execute('''
SELECT * FROM student WHERE first_name = 'Genius'
''')
genius_students = cursor.fetchall()
print("Студенты с именем 'Genius':")
for student in genius_students:
    print(student)

# Закрытие соединения с базой данных
conn.close()
