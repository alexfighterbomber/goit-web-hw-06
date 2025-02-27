--Знайти список курсів, які відвідує студент.
SELECT subjects.name
FROM grades
JOIN subjects ON grades.subject_id = subjects.id
JOIN students ON grades.student_id = students.id
WHERE students.name = 'David Smith'
GROUP BY subjects.name;