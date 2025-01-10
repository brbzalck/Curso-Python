-- Apaga registros com join

SELECT u.first_name, p.bio FROM users u
LEFT JOIN profiles p ON p.user_id = u.id 
WHERE u.first_name = 'Katelyn';


DELETE p, u FROM users u
LEFT JOIN profiles p ON p.user_id = u.id 
WHERE u.first_name = 'Katelyn';