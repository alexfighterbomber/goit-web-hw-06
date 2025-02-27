from datetime import datetime
import faker
from faker.providers import BaseProvider
from random import randint, choice
import sqlite3

 
NUMBER_STUDENTS = 50
NUMBER_TEACHERS = 5
NUMBER_GRADES = 20

def generate_fake_data(students, teachers) -> tuple:
    fake_students = []  # тут зберігатимемо студентів
    fake_subjects = [
            "Математика", "Програмування", "Бази даних", "Экономіка",
            "Менеджмент", "Психологія", "Соціология", "Англійська мова"
        ]
    fake_groups = ['SE-2021-1', 'ME-2022-4', 'LAW-2024-3']  # тут зберігатимемо групи
    fake_teachers = []  # тут зберігатимемо викладачів

    
    fake_data = faker.Faker()

    '''Створимо набір студентів у кількості students'''
    for _ in range(students):
        fake_students.append(fake_data.name())
    
    '''Створимо набір викладачів у кількості teachers'''
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
        for_students.append((student, randint(1, len(groups))))  
    
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
    for stud in range(1, NUMBER_STUDENTS+1):
        for _ in range(NUMBER_GRADES):
            grade_date = datetime(2025, randint(1, 5), randint(1, 28)).date()
            for_grades.append((stud, randint(1, len(subjects)), randint(60, 100), grade_date))
    
    return for_students, for_subjects, for_groups, for_teachers, for_grades

 
def insert_data_to_db(students, subjects, groups, teachers, grades):
    # Створимо з'єднання з нашою БД та отримаємо об'єкт курсору для маніпуляцій з даними

    with sqlite3.connect('university.db') as con:

        cur = con.cursor()

        sql_to_students = """INSERT INTO students(name, group_id)
                             VALUES (?, ?)"""
 
        cur.executemany(sql_to_students, students)

        sql_to_subjects = """INSERT INTO subjects(name, teacher_id)
                             VALUES (?, ?)"""
                             
        cur.executemany(sql_to_subjects, subjects)
        
        sql_to_groups = """INSERT INTO groups(name)
                           VALUES (?)"""
        
        cur.executemany(sql_to_groups, groups)
        
        sql_to_teachers = """INSERT INTO teachers(name)
                             VALUES (?)"""
                             
        cur.executemany(sql_to_teachers, teachers) 

        sql_to_grades = """INSERT INTO grades(student_id, subject_id, grade, date_received)
                            VALUES (?, ?, ?, ?)"""
        
        cur.executemany(sql_to_grades, grades)
       
        # Фіксуємо наші зміни в БД

        con.commit()


if __name__ == "__main__":

    insert_data_to_db(*prepare_data(*generate_fake_data(NUMBER_STUDENTS, NUMBER_TEACHERS)))
    print('Data has been successfully added to the database!')