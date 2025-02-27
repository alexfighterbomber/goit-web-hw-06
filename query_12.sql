--Оцінки студентів у певній групі з певного предмета на останньому занятті.
SELECT students.name, grades.grade, grades.date_received
FROM grades
JOIN subjects ON grades.subject_id = subjects.id
JOIN students ON grades.student_id = students.id
JOIN groups ON students.group_id = groups.id
WHERE subjects.name = 'Математика' 
  AND groups.name = 'SE-2021-1' 
  AND grades.date_received = (
      SELECT MAX(grades.date_received) 
      FROM grades
      JOIN subjects ON grades.subject_id = subjects.id
      JOIN students ON grades.student_id = students.id
      JOIN groups ON students.group_id = groups.id
      WHERE subjects.name = 'Математика' 
        AND groups.name = 'SE-2021-1'
  )
ORDER BY students.name;
