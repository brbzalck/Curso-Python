-- Update - Atualiza registros

-- SEMPRE utilize o UPDATE com WHERE especificando aonde atualizar
UPDATE users SET first_name = 'Elijaah', last_name = 'Espinosa' 
WHERE id = 50;

SELECT * FROM users WHERE id = 50;