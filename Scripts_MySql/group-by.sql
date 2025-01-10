-- Group by - Agrupa valores & Count conta quantos valores 
-- agrupados por id

SELECT first_name, COUNT(id) as total FROM users u
GROUP BY first_name
ORDER BY total DESC;