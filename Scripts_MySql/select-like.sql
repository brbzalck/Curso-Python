-- like (parecido)
-- usa %(qualquer coisa) ou _()um caractere para completar palavras
-- com começo/final parecido.

SELECT * FROM users WHERE first_name LIKE 'J____'
OR first_name LIKE 'lu%'; 