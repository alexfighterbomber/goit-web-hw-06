--Знайти середній бал на потоці (по всій таблиці оцінок)
SELECT ROUND(AVG(grade),  2) as avg_grade
FROM grades;
