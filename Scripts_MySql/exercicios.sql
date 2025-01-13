-- 1) Insira 5 usuários OK
-- 2) Insira 5 perfís para os usuários inseridos
-- 3) Insira permissões (roles) para os usuários inseridos
-- 4) Selecione os últimos 5 usuários por ordem decrescente
-- 5) Atualize o último usuário inserido
-- 6) Remova uma permissão de algum usuário
-- 7) Remova um usuário que tem a permissão "PUT"
-- 8) Selecione usuários com perfís e permissões (obrigatório)
-- 9) Selecione usuários com perfís e permissões (opcional)
-- 10) Selecione usuários com perfís e permissões ordenando por salário

-- DELETE FROM users WHERE id BETWEEN 111 AND 114;

-- 1) Insira 5 usuários
INSERT INTO users (first_name, last_name, email, salary, password_hash) 
VALUES ('José', 'Alfredo', 'ja@gmail.com', 2500, 'a52'),  ('Antonio', 'Rodrigues', 'ar@gmail.com', 3600, 'b93'), 
('Letícia', 'Gomes', 'lo@gmail.com', 2800, 't92'), ('Julia', 'Paes', 'jp@gmail.com', 2300, 'h89'), ('Jorge', 'Alecrim', 'jam@gmail.com', 1800, 'k98');

-- 2) Insira 5 perfís para os usuários inseridos
INSERT INTO profiles (bio, description, user_id) select	CONCAT('Bio de ', first_name), 
CONCAT('Description de ', first_name), id from users WHERE id BETWEEN 120 and 124; 

-- 3) Insira permissões (roles) para os usuários inseridos
INSERT INTO users_roles (user_id, role_id) select id, (SELECT id from roles order by rand() limit 1) from users u WHERE id BETWEEN 120 and 124;

-- 4) Selecione os últimos 5 usuários por ordem decrescente
SELECT * FROM users u order by id desc limit 5;

-- 5) Atualize o último usuário inserido
UPDATE users SET salary = 7000 where id = 124;

-- 6) Remova uma permissão de algum usuário
DELETE FROM users_roles WHERE user_id = 33 AND role_id = 5;

-- 7) Remova um usuário que tem a permissão "PUT"
SELECT u.id, u.first_name, r.name FROM users u INNER JOIN users_roles ur ON u.id = ur.user_id INNER JOIN roles r ON ur.role_id = r.id;
DELETE FROM users_roles WHERE user_id = 90 and role_id = 3;

-- 8) Selecione usuários com perfís e permissões (obrigatório)
SELECT u.id, u.first_name, p.bio, p.description, r.name FROM users u 
INNER JOIN profiles p ON u.id = p.user_id 
INNER JOIN users_roles ur ON u.id = ur.user_id
INNER JOIN roles r ON ur.role_id = r.id;


-- 10) Selecione usuários com perfís e permissões ordenando por salário
SELECT u.id, u.first_name, p.bio, p.description, r.name, u.salary FROM users u 
INNER JOIN profiles p ON u.id = p.user_id 
INNER JOIN users_roles ur ON u.id = ur.user_id
INNER JOIN roles r ON ur.role_id = r.id ORDER BY u.salary desc;


