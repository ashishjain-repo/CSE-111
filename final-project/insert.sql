INSERT INTO genre
(genre_name)
VALUES
    ('Science Fiction')
,   ('Fantasy')
,   ('Mystery')
,   ('Thriller')
,   ('Romance')
,   ('Historical Fiction');
INSERT INTO format
(format_type)
VALUES
    ('Hardcover')
,   ('Paperback')
,   ('E-book')
,   ('Audiobook')
,   ('Audio CD');

INSERT INTO author
(
    author_fname
,   author_mname
,   author_lname
,   author_dob
,   author_dod
)
VALUES
    ('Rasipuram','Krishnaswami Iyer','Narayanaswami','1906-10-10','2001-05-13')
,   ('Joanne','','Rowling','1965-07-31',NULL)
,   ('Gabriel','Garcia','Marquez','1927-03-06','2014-04-17')
,   ('Paulo','Coelho','de Souza','1947-08-24',NULL)
,   ('Margaret','Eleanor','Atwood','1939-11-18',NULL)
,   ('Yuval','Noah','Harai','1976-02-24',NULL)
,   ('Haruki','','Murakami','1949-01-12',NULL)
,   ('Herbert','George','Wells','1866-09-21','1946-08-13')
,   ('Jane','','Austen','1775-12-16','1817-07-18')
,   ('Alfred','Joseph','Hitchcock','1899-08-13','1980-04-29');

INSERT INTO book
(
    book_name
,   author_id
)
VALUES
    ('Swami and Friends',(SELECT author_id FROM author WHERE author_fname = 'Rasipuram'));
