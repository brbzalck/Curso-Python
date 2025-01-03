-- Seleciona base de dados
use base_de_dados;
-- para comentar
# outro jeito de comentar
/* mais um jeito de comentar*/

-- crtl + enter para executar

-- Mostra as tabelas da base de Dados.
show tables;
-- Descreve as colunas da tabela.
describe users;
-- Inserir registros na base de dados
INSERT INTO users (first_name, last_name, email, password_hash) VALUES 
('Pedro', 'Santos', 'pedro@gmail.com', 'b_hash'), 
('Esther', 'Montovani', 'esther@gmail.com', 'c_hash'), 
('Eduarda', 'Oliveira', 'duda@gmail.com', 'd_hash');
