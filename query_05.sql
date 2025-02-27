--Знайти які курси читає певний викладач
SELECT t.name, subj.name as subject_name
FROM teachers AS t
JOIN subjects AS subj ON t.id = subj.teacher_id
WHERE t.name = 'Heather Powers'; 