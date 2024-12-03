
# Flask Books Management App

A simple Flask application for managing a collection of books. This application uses MySQL as the database and provides features to add, update, view, and delete books.

## Project Structure

```
.
|-- LICENSE
|-- app.py             # Main Flask application
|-- books.sql          # SQL script to create the database and table
|-- templates          # HTML templates for the frontend
    |-- add_book.html  # Template for adding a new book
    |-- delete.html    # Template for deleting a book
    |-- index.html     # Homepage template displaying the list of books
    |-- update.html    # Template for updating a book
|-- .env               # Environment variables for database configuration
```

## Features

- Add new books to the collection.
- Update details of existing books.
- View a list of all books.
- Delete books from the collection.
- Fully responsive frontend built using Bootstrap.

## Prerequisites

- Python 3.x
- MySQL Server
- `pip` for Python package management

## Installation

1. Clone the repository:
   ```bash
   git clone https://github.com/your-repo/flask-books-management-app.git
   cd flask-books-management-app
   ```

2. Install dependencies:
   ```bash
   pip install -r requirements.txt
   ```

3. Create the database:
   - Log in to your MySQL server and run the `books.sql` script to set up the database and table.
   ```bash
   mysql -u your_user -p < books.sql
   ```

4. Create a `.env` file in the root directory and add the following environment variables:
   ```env
   MYSQL_HOST=localhost
   MYSQL_USER=your_mysql_user
   MYSQL_PASSWORD=your_mysql_password
   MYSQL_DB=flask_books
   ```

5. Run the application:
   ```bash
   python app.py
   ```

6. Open your browser and visit `http://127.0.0.1:5000` to use the app.

## Usage

- **Homepage**: Displays a list of all books in the collection.
- **Add Book**: Use the "Add Book" button to add a new book.
- **Edit Book**: Click the "Edit" button next to a book to update its details.
- **Delete Book**: Click the "Delete" button next to a book to remove it from the collection.

## Database Setup

The `books.sql` file contains the SQL script to create the database and `books` table:
```sql
CREATE DATABASE IF NOT EXISTS flask_books;
USE flask_books;

CREATE TABLE books (
    id INT AUTO_INCREMENT PRIMARY KEY,
    title VARCHAR(100),
    author VARCHAR(100),
    pages INT,
    genre VARCHAR(50),
    summary TEXT
);
```

## Environment Variables

Ensure the `.env` file contains the correct credentials for your MySQL server:
```env
MYSQL_HOST=localhost
MYSQL_USER=your_mysql_user
MYSQL_PASSWORD=your_mysql_password
MYSQL_DB=flask_books
```

## License

This project is licensed under the [MIT License](LICENSE).

---

Happy coding! 🚀
