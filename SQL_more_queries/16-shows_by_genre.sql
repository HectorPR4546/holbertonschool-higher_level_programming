-- This script lists all shows and all genres linked to that show from the database hbtn_0d_tvshows.
-- As a Holberton student, I'm learning to display all shows, even those without genres, and sort them.
SELECT tv_shows.title, tv_genres.name
FROM tv_shows
LEFT JOIN tv_show_genres ON tv_shows.id = tv_show_genres.show_id
LEFT JOIN tv_genres ON tv_show_genres.genre_id = tv_genres.id
ORDER BY tv_shows.title ASC, tv_genres.name ASC;
