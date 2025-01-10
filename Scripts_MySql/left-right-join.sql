-- Seleciona users.id, profiles.id, profiles.bio
-- profiles.description, users.first_name
-- da tabela users (todos os registros da tabela da esquerda)
-- unindo com a tabela profiles (tabela da direita é opcional)

-- SELECT u.id as uid, u.first_name, p.id as pid, p.bio
-- from users as u RIGHT JOIN profiles p ON u.id = p.user_id;

SELECT u.id as uid, u.first_name, p.id as pid, p.bio
from users as u LEFT JOIN profiles p ON u.id = p.user_id;