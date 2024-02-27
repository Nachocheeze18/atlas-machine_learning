SELECT city, AVG(temperature * 9/5 + 32) AS avg_temp
FROM your_table_name
GROUP BY city
ORDER BY avg_temp DESC;
