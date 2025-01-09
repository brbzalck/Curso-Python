-- Seleciona users.id, profiles.id, profiles.bio
-- profiles.description, users.first_name
-- da tabela users
-- unindo com a tabela profiles
-- quando a condição u.id = p.user_id for satisfeita
-- onde users.first_name terminar com "a"
-- ordena por users.first_name decrescente
-- limita 5 registros

SELECT u.id as uid, p.id as pid, p.bio, u.first_name
from users as u, profiles as p 
WHERE u.id = p.user_id;

SELECT u.id as uid, u.first_name, p.id as pid, p.bio
from users as u INNER JOIN profiles p ON u.id = p.user_id
WHERE u.first_name LIKE '%a' ORDER BY u.first_name ASC 
LIMIT 5; 