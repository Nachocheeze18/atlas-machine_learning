-- lists shows by rating
SELECT title, SUM(rating) AS rating_sum
FROM tv_shows
GROUP BY title
ORDER BY rating_sum DESC;