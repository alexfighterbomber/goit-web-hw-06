--Знайти список студентів у певній групі
SELECT s.name as student, g.name as group_name
FROM students as s
JOIN groups as g ON s.group_id = g.id
WHERE g.name = 'SE-2021-1';