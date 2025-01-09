-- insert select
-- insere valores em uma tabela usando outra

INSERT INTO profiles (bio, description, user_id) 
select concat('Bio de ', first_name), 
concat('Description de ', first_name), 
id from users;


DELETE FROM profiles;