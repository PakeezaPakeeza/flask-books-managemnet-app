CREATE DATABASE IF NOT EXISTS flask_books;
CREATE TABLE books (
    id INT AUTO_INCREMENT PRIMARY KEY,
    title VARCHAR(100),
    author VARCHAR(100),
    pages INT,
    genre VARCHAR(50),
    summary TEXT
);
