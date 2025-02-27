--Середній бал, який певний викладач ставить певному студенту
SELECT ROUND(AVG(grades.grade), 2) AS avg_grade
FROM grades
JOIN subjects ON grades.subject_id = subjects.id
JOIN students ON grades.student_id = students.id
JOIN teachers ON subjects.teacher_id = teachers.id
WHERE students.name = 'David Smith' AND teachers.name = 'Stephanie Nelson'
GROUP BY students.name, teachers.name;
