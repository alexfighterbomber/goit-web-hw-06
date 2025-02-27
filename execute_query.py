import sqlite3

def execute_query(file: str):
    # читаємо файл зі скриптом для створення БД
    with open(file, 'r') as f:
        sql = f.read()

    # створюємо з'єднання з БД (якщо файлу з БД немає, він буде створений)
    with sqlite3.connect('university.db') as con:
        cur = con.cursor()
        # виконуємо скрипт із файлу, який створить таблиці в БД
        cur.execute(sql)
        return cur.fetchall()

if __name__ == "__main__":
    print(execute_query('query_01.sql'))
