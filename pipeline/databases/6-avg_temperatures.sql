-- import in hbtn_0c_0 database this table dump
SELECT city, AVG(temp) AS avg_temp
FROM temperature
GROUP BY city
ORDER BY avg_temp DESC;
