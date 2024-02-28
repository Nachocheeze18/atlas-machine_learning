-- lists all shows
SELECT title, genre_id
FROM tv_shows
LEFT JOIN tv_show_genres ON tv_show_id
WHERE genre_id IS NULL
ORDER BY title ASC, genre_id ASC;