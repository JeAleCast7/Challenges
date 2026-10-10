CREATE TABLE contact (
  name TEXT,
  birthday DATE,
  location TEXT,
  note TEXT,
  fav_meal TEXT
);

INSERT INTO contact (name, birthday, location, note, fav_meal)
VALUES (
  'Juan', 
  '2002-02-02', 
  'none of your business CA 113323',
  'he loves cats',
  'cheese burgers' );