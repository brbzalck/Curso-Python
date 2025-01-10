INSERT INTO users_roles (user_id, role_id) VALUES (33, 3);

SELECT id, 
(SELECT id from roles order by RAND() limit 1) from users u;

INSERT INTO users_roles (user_id, role_id) SELECT id, 
(SELECT id from roles order by RAND() limit 1) from users u;