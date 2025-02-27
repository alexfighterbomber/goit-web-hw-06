--Знайти оцінки студентів у окремій групі з певного предмета.
SELECT gr.grade
FROM grades AS gr
JOIN students AS s ON gr.student_id = s.id
JOIN groups AS g ON s.group_id = g.id
JOIN subjects AS subj ON gr.subject_id = subj.id
WHERE subj.name = 'Менеджмент' AND g.name = 'LAW-2024-3';
