SELECT u.first_name, p.bio FROM users u
-- UPDATE users u
JOIN profiles p ON p.user_id = u.id
-- SET p.bio = 'Bio de Katelyn atualizado' 
WHERE u.first_name = 'Katelyn';

UPDATE users u
JOIN profiles p ON p.user_id = u.id
SET p.bio = 'Bio de Katelyn refatorado' 
WHERE u.first_name = 'Katelyn';