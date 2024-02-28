-- shows all genres and shows liked to one another
SELECT genre AS genre, COUNT(*) AS number_of_shows
FROM hbtn_0d_tvshows
GROUP BY genre
HAVING COUNT(*) > 0
ORDER BY COUNT(*) DESC;
