-- lists all shows
SELECT title, genre_id
FROM tv_shows
LEFT JOIN tv_show_genres ON tv_shows.id = tv_show_genres.tv_show_id
WHERE tv_show_genres IS NULL
ORDER BY title ASC, genre_id ASC;