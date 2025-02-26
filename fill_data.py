from datetime import datetime
import faker
from random import randint, choice
import sqlite3

NUMBER_STUDENTS = 50
NUMBER_SUBJECTS = 8
NUMBER_GROUPS = 3
NUMBER_TEACHERS = 5
NUMBER_GRADES = 20

def generate_fake_data(students, subjects, groups, teachers, grades) -> tuple:
    fake_students = []  # тут зберігатимемо студентів
    fake_subjects = []  # тут зберігатимемо предмети
    fake_groups = []  # тут зберігатимемо групи
    fake_teachers = []  # тут зберігатимемо викладачів
    fake_grades = []  # тут зберігатимемо оцінки
    
    fake_data = faker.Faker()
    
    '''Створимо набір груп у кількості number_groups'''
    for _ in range(groups):
        fake_groups.append(fake_data.company())

    '''Створимо набір студентів у кількості number_students'''
    for _ in range(students):
        fake_students.append(fake_data.name())
        
    '''Створимо набір предметів у кількості number_subjects'''
    for _ in range(subjects):
        fake_subjects.append(fake_data.job())
    
    '''Створимо набір викладачів у кількості number_teachers'''
    for _ in range(teachers):
        fake_teachers.append(fake_data.name())
        
    return fake_students, fake_subjects, fake_groups, fake_teachers

def prepare_data(students, subjects, groups, teachers) -> tuple:
 
    for_groups = []
    # Готуємо список кортежів із назвами груп
    for group in groups:
        for_groups.append((group, ))
 
    for_students = []
    # Готуємо список кортежів із іменами студентів
    for student in students:
        for_students.append((student, randint(1, NUMBER_GROUPS)))  
    
    for_subjects = []
    # Готуємо список кортежів із назвами предметів  
    for subject in subjects:    
        for_subjects.append((subject, randint(1, NUMBER_TEACHERS)))        
    
    for_teachers = []
    # Готуємо список кортежів із іменами викладачів
    for teacher in teachers:
        for_teachers.append((teacher, ))
    
    for_grades = []
    # Готуємо список кортежів із оцінками
    for stud in range(1, NUMBER_STUDENTS):
        for _ in range(NUMBER_GRADES):
            grade_date = datetime(2025, randint(1, 5), randint(1, 28)).date()
            for_grades.append((stud, randint(1, NUMBER_SUBJECTS), randint(60, 100), grade_date))
    
    return for_students, for_subjects, for_groups, for_teachers, for_grades

 
# def insert_data_to_db(companies, employees, payments) -> None:
#     # Створимо з'єднання з нашою БД та отримаємо об'єкт курсору для маніпуляцій з даними

#     with sqlite3.connect('salary.db') as con:

#         cur = con.cursor()

#         '''Заповнюємо таблицю компаній. І створюємо скрипт для вставлення, де змінні, які вставлятимемо, відзначимо
#         знаком заповнювача (?) '''

#         sql_to_companies = """INSERT INTO companies(company_name)
#                                VALUES (?)"""

#         '''Для вставлення відразу всіх даних скористаємося методом executemany курсора. Першим параметром буде текст
#         скрипта, а другим - дані (список кортежів).'''

#         cur.executemany(sql_to_companies, companies)

#         # Далі вставляємо дані про співробітників. Напишемо для нього скрипт і вкажемо змінні

#         sql_to_employees = """INSERT INTO employees(employee, post, company_id)
#                                VALUES (?, ?, ?)"""

#         # Дані були підготовлені заздалегідь, тому просто передаємо їх у функцію

#         cur.executemany(sql_to_employees, employees)

#         # Останньою заповнюємо таблицю із зарплатами

#         sql_to_payments = """INSERT INTO payments(employee_id, date_of, total)
#                               VALUES (?, ?, ?)"""

#         # Вставляємо дані про зарплати

#         cur.executemany(sql_to_payments, payments)

#         # Фіксуємо наші зміни в БД

#         con.commit()


if __name__ == "__main__":
    print(prepare_data(*generate_fake_data(NUMBER_STUDENTS, NUMBER_SUBJECTS, NUMBER_GROUPS, NUMBER_TEACHERS, NUMBER_GRADES)))
#     companies, employees, posts = prepare_data(*generate_fake_data(NUMBER_COMPANIES, NUMBER_EMPLOYESS, NUMBER_POST))
#     insert_data_to_db(companies, employees, posts)