--Знайти середній бал, який ставить певний викладач зі своїх предметів.
SELECT ROUND(AVG(gr.grade), 2) AS avg_grade, t.name
FROM grades as gr
JOIN subjects as s ON gr.subject_id = s.id
JOIN teachers as t ON s.teacher_id = t.id
WHERE t.name = 'Michael Smith'
GROUP BY t.name
ORDER BY avg_grade DESC;

