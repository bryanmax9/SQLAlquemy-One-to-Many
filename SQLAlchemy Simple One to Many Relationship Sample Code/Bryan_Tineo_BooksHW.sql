-- Created by Vertabelo (http://vertabelo.com)
-- Last modification date: 2023-02-22 20:14:16.24

-- tables
-- Table: book
CREATE TABLE book (
    ISBN varchar(20)  NOT NULL,
    publicationYear int  NOT NULL,
    genre_name varchar(20)  NOT NULL,
    publisher_name varchar(50)  NOT NULL,
    year int  NOT NULL,
    title varchar(150)  NOT NULL,
    CONSTRAINT book_pk PRIMARY KEY (ISBN)
);

CREATE INDEX books_unique_01 on book (title ASC,year ASC);

-- Table: genre
CREATE TABLE genre (
    name varchar(50)  NOT NULL,
    CONSTRAINT genre_pk PRIMARY KEY (name)
);

-- Table: publisher
CREATE TABLE publisher (
    name varchar(50)  NOT NULL,
    address varchar(100)  NOT NULL,
    CONSTRAINT publisher_pk PRIMARY KEY (name)
);

-- foreign keys
-- Reference: books_genres_fk_01 (table: book)
ALTER TABLE book ADD CONSTRAINT books_genres_fk_01
    FOREIGN KEY (genre_name)
    REFERENCES genre (name)  
    NOT DEFERRABLE 
    INITIALLY IMMEDIATE
;

-- Reference: books_publisher_fk_01 (table: book)
ALTER TABLE book ADD CONSTRAINT books_publisher_fk_01
    FOREIGN KEY (publisher_name)
    REFERENCES publisher (name)  
    NOT DEFERRABLE 
    INITIALLY IMMEDIATE
;

-- End of file.

