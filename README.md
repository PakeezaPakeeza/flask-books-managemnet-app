
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

3. Set up the database manually: (Optional)
   ```bash
   mysql -u flask_user -p 
   ```
5. Run the application:
   ```bash
   python app.py
   ```
6. Open your browser and visit `http://127.0.0.1:5000` to use the app.

## Installation with Docker Run
Step 1: Start the Flask App
bash
Copy code
docker run -d -p 5000:5000 --network booknet --name flask-cont flaskbook-img:latest
Step 2: Start the MySQL Database
bash
Copy code
docker run -d --name mysql-container \
  -e MYSQL_ROOT_PASSWORD=root_password \
  -e MYSQL_DATABASE=flask_books \
  -e MYSQL_USER=flask_user \
  -e MYSQL_PASSWORD=admin \
  --network booknet mysql:latest

## Installation using docker compose
docker-compose up -d
http://127.0.0.1:5000
docker-compose down

## Usage

- **Homepage**: Displays a list of all books in the collection.
- **Add Book**: Use the "Add Book" button to add a new book.
- **Edit Book**: Click the "Edit" button next to a book to update its details.
- **Delete Book**: Click the "Delete" button next to a book to remove it from the collection.


## License

This project is licensed under the [MIT License](LICENSE).

---

Happy coding! 🚀
