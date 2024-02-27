-- LIST ALL RECORDS WITH A SCORE
SELECT score, name FROM second_table 
WHERE score >= 10 ORDER BY score DESC;