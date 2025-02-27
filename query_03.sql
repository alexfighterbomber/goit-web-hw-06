--Знайти середній бал у групах з певного предмета.
SELECT subj.name, g.name AS group_name, ROUND(AVG(gr.grade), 2) AS avg_grade
FROM grades AS gr
JOIN students AS s ON gr.student_id = s.id
JOIN groups AS g ON s.group_id = g.id
JOIN subjects AS subj ON gr.subject_id = subj.id
WHERE subj.name = 'Экономіка'  -- Укажите нужный предмет
GROUP BY g.id
ORDER BY avg_grade DESC;
