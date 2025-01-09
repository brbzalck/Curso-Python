-- limit - limita a qntd de valores
-- offset - começa a partir do valor de determinado resultado

SELECT id, first_name as fn, email FROM users 
-- WHERE id BETWEEN 50 AND 100 ORDER BY fn asc LIMIT 5 offset 5;
WHERE id BETWEEN 50 AND 100 ORDER BY fn asc LIMIT 9,3;