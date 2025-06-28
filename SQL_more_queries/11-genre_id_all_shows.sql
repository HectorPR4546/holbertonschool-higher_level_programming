-- This script lists all shows contained in the database hbtn_0d_tvshows, including those without a genre.
-- As a Holberton student, I'm learning to use LEFT JOIN to include all records from one table even if there's no match in the other.
SELECT tv_shows.title, tv_show_genres.genre_id
FROM tv_shows
LEFT JOIN tv_show_genres ON tv_shows.id = tv_show_genres.show_id
ORDER BY tv_shows.title ASC, tv_show_genres.genre_id ASC;
