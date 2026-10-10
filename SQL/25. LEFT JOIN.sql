SELECT author_id
FROM books
LEFT JOIN authors
ON books.author_id = authors.id;