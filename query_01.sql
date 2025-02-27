--Знайти 5 студентів із найбільшим середнім балом з усіх предметів.
SELECT  s.name, ROUND(AVG(g.grade), 2) as avg_grade
FROM grades as g
LEFT JOIN students as s ON g.student_id = s.id
GROUP BY s.id
ORDER BY avg_grade DESC
LIMIT 5;