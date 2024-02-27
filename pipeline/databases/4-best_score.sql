-- LIST ALL RECORDS WITH A SCORE
SELECT name, score FROM second_table 
WHERE score >= 10 ORDER BY score DESC;