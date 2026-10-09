SELECT artist, AVG(plays) 
FROM playlist 
GROUP BY artist;