--Знайти студента із найвищим середнім балом з певного предмета.
SELECT subj.name, s.name, ROUND(AVG(g.grade), 2) AS avg_grade
FROM grades AS g
JOIN students AS s ON g.student_id = s.id
JOIN subjects AS subj ON g.subject_id = subj.id
WHERE subj.name = 'Экономіка'
GROUP BY s.name, subj.name
ORDER BY avg_grade DESC
LIMIT 1;