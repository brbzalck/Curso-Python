SELECT max(salary) as max_salary,
min(salary) as min_salary,
AVG(salary) as avg_salary,
sum(salary) as sum_salary,
COUNT(salary) as count_salary 
FROM users u
WHERE first_name = 'Lucas';

SELECT u.first_name, 
max(salary) as max_salary,
min(salary) as min_salary,
AVG(salary) as avg_salary,
sum(salary) as sum_salary,
COUNT(u.id) as total 
from users u LEFT JOIN profiles p 
ON p.user_id = u.id 
GROUP BY u.first_name 
ORDER BY total DESC;