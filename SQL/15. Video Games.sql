SELECT title, MAX(metascore) FROM games;
SELECT language, COUNT(language) FROM games GROUP BY language;
SELECT genre, AVG(metascore) FROM games GROUP BY genre;