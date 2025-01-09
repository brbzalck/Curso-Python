-- between seleciona um range
SELECT * FROM users
-- where created_at <= '2021-07-10 21:33:24' and created_at >= '2021-05-27 20:27:02';
where created_at BETWEEN '2021-05-27 20:27:02' AND '2021-07-10 21:33:24'
and id BETWEEN 20 AND 50;