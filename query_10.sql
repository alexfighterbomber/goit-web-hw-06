--Список курсів, які певному студенту читає певний викладач
SELECT subjects.name
FROM grades
JOIN subjects ON grades.subject_id = subjects.id
JOIN students ON grades.student_id = students.id
JOIN teachers ON subjects.teacher_id = teachers.id
WHERE students.name = 'David Smith' AND teachers.name = 'Stephanie Nelson'
GROUP BY subjects.name;
