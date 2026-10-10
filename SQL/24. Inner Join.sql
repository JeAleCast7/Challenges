SELECT id 
FROM authors
INNER JOIN books
ON authors.id = books.author_id;