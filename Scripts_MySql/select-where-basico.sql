-- Where filtra registros

SELECT * FROM users
where created_at < '2025-01-03 14:45:59' or first_name = 'Maria' and password_hash = 'a_hash';