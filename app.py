import os
from flask import Flask, render_template, request, redirect, flash, jsonify
from flask_mysqldb import MySQL

app = Flask(__name__)
app.secret_key = 'your_secret_key'

# Configure MySQL from environment variables
app.config['MYSQL_HOST'] = os.environ.get('MYSQL_HOST', 'localhost')
app.config['MYSQL_USER'] = os.environ.get('MYSQL_USER', 'flask_user')
app.config['MYSQL_PASSWORD'] = os.environ.get('MYSQL_PASSWORD', 'password')
app.config['MYSQL_DB'] = os.environ.get('MYSQL_DB', 'flask_books')

# Initialize MySQL
mysql = MySQL(app)

# Initialize the database
def init_db():
    with app.app_context():
        cur = mysql.connection.cursor()
        cur.execute('''
        CREATE TABLE IF NOT EXISTS books (
            id INT AUTO_INCREMENT PRIMARY KEY,
            title VARCHAR(100),
            author VARCHAR(100),
            pages INT,
            genre VARCHAR(50),
            summary TEXT
        );
        ''')
        mysql.connection.commit()
        cur.close()

# Routes
@app.route('/')
def index():
    """
    Render the index page with the list of books from the database.
    """
    cur = mysql.connection.cursor()
    cur.execute('SELECT * FROM books')
    books = cur.fetchall()
    cur.close()
    return render_template('index.html', data=books)

@app.route('/add_book', methods=['GET', 'POST'])
def add_book():
    """
    Add a new book to the database.
    """
    if request.method == 'POST':
        title = request.form.get('title')
        author = request.form.get('author')
        pages = request.form.get('pages')
        genre = request.form.get('genre')
        summary = request.form.get('summary')
        cur = mysql.connection.cursor()
        cur.execute(
            'INSERT INTO books (title, author, pages, genre, summary) VALUES (%s, %s, %s, %s, %s)',
            (title, author, pages, genre, summary)
        )
        mysql.connection.commit()
        cur.close()
        flash('Book added successfully!', 'success')
        return redirect('/')
    return render_template('add_book.html')

@app.route('/update_book/<int:book_id>', methods=['GET', 'POST'])
def update_book(book_id):
    """
    Update an existing book in the database.
    """
    cur = mysql.connection.cursor()
    cur.execute('SELECT * FROM books WHERE id = %s', (book_id,))
    book = cur.fetchone()
    if book:
        if request.method == 'POST':
            title = request.form.get('title')
            author = request.form.get('author')
            pages = request.form.get('pages')
            genre = request.form.get('genre')
            summary = request.form.get('summary')
            cur.execute(
                'UPDATE books SET title = %s, author = %s, pages = %s, genre = %s, summary = %s WHERE id = %s',
                (title, author, pages, genre, summary, book_id)
            )
            mysql.connection.commit()
            cur.close()
            flash('Book updated successfully!', 'success')
            return redirect('/')
        return render_template('update.html', book=book)
    flash(f'Book with id {book_id} not found', 'danger')
    return redirect('/')

@app.route('/delete_book/<int:book_id>', methods=['GET', 'POST'])
def delete_book(book_id):
    """
    Delete an existing book from the database.
    """
    cur = mysql.connection.cursor()
    cur.execute('SELECT * FROM books WHERE id = %s', (book_id,))
    book = cur.fetchone()
    if book:
        if request.method == 'POST':
            cur.execute('DELETE FROM books WHERE id = %s', (book_id,))
            mysql.connection.commit()
            cur.close()
            flash('Book deleted successfully!', 'success')
            return redirect('/')
        return render_template('delete.html', book=book)
    flash(f'Book with id {book_id} not found', 'danger')
    return redirect('/')

# API route (optional)
@app.route('/api/books', methods=['GET'])
def api_books():
    """
    Return all books in JSON format.
    """
    cur = mysql.connection.cursor()
    cur.execute('SELECT * FROM books')
    books = cur.fetchall()
    cur.close()
    return jsonify(books)

if __name__ == '__main__':
    init_db()
    app.run(host='0.0.0.0', port=5000, debug=True)
