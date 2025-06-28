-- This script lists all shows contained in the database hbtn_0d_tvshows that do not have a genre linked.
-- As a Holberton student, I'm learning to find records that lack related data using LEFT JOIN and WHERE NULL.
SELECT tv_shows.title, tv_show_genres.genre_id
FROM tv_shows
LEFT JOIN tv_show_genres ON tv_shows.id = tv_show_genres.show_id
WHERE tv_show_genres.genre_id IS NULL
ORDER BY tv_shows.title ASC, tv_show_genres.genre_id ASC;
