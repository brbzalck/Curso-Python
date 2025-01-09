-- Order ordena valores
-- order by id asc(idcrescende)
-- order by id desc(decrescente)

SELECT id, first_name as fn, email FROM users 
WHERE id BETWEEN 50 and 100 ORDER BY fn ASC;