
# 📚 **Flask Books Management Application**

## 🌟 **Overview**
This is a simple and interactive two-tier Flask application for managing books. It provides features like:
- ➕ Add a new book.
- 📜 View all books.
- ✏️ Update an existing book.
- ❌ Delete a book.

All book data is stored in a **MySQL database**. The application uses **Flask** for backend logic and **Bootstrap** for a responsive user interface.

---

## 🛠️ **Technologies Used**
- **Python** 🐍: Backend logic using Flask.
- **Flask-MySQLdb** 🛢️: Connect Flask to MySQL.
- **HTML/CSS** 🎨: For frontend templates.
- **Bootstrap** 💎: For modern, responsive design.
- **MySQL** 🗄️: Database to store book details.

---

## 📁 **Project Structure**
```plaintext
📂 project/
├── 📜 app.py                 # Main application file
├── 📂 templates/             # HTML templates
│   ├── index.html         # Homepage (book list)
│   ├── add_book.html      # Add a new book
│   ├── update.html        # Update an existing book
│   ├── delete.html        # Confirm book deletion
├── 📂 static/                # Static assets (optional CSS/JS)
├── 📜 books.sql              # SQL script for database setup
├── 📜 README.md              # Project documentation
```

---

## 🚀 **Getting Started**

### 📝 **1. Prerequisites**
Ensure you have the following installed:
- Python 3.8+ 🐍
- MySQL Server 🛢️
- `pip` (Python package manager)

### 📥 **2. Clone the Repository**
```bash
git clone https://github.com/your-username/flask-books-management.git
cd flask-books-management
```

### 📦 **3. Install Dependencies**
```bash
pip install flask flask-mysqldb
```

### 🗄️ **4. Set Up the Database**
1. Log in to MySQL:
   ```bash
   mysql -u your_user -p
   ```
2. Run the `books.sql` file to create the database and table:
   ```sql
   source books.sql;
   ```
3. Verify the database and table:
   ```sql
   USE flask_books;
   SHOW TABLES;
   ```

### ⚙️ **5. Configure Environment Variables**
You can use a `.env` file or export variables directly:
```plaintext
MYSQL_HOST=localhost
MYSQL_USER=flask_user
MYSQL_PASSWORD=your_password
MYSQL_DB=flask_books
```

If using a `.env` file, install `python-dotenv`:
```bash
pip install python-dotenv
```

### ▶️ **6. Run the Application**
Start the Flask app:
```bash
python app.py
```

Visit the application in your browser:
```plaintext
http://127.0.0.1:5000
```

---

## 🌟 **Features**

### 🖥️ **1. Homepage**
- Displays a list of books stored in the database.
- Includes "Edit" and "Delete" buttons for each book.

### ➕ **2. Add a Book**
- Navigate to `/add_book` to add new books via a form.

### ✏️ **3. Edit a Book**
- Update existing book details via `/update_book/<id>`.

### ❌ **4. Delete a Book**
- Delete books with confirmation via `/delete_book/<id>`.

### 📊 **5. API Endpoint**
Access all books in JSON format:
```plaintext
GET /api/books
```

---

## 🎨 **Screenshots**
### **Homepage**
![Homepage](https://via.placeholder.com/800x400?text=Homepage+Screenshot)

### **Add a Book**
![Add Book](https://via.placeholder.com/800x400?text=Add+Book+Form)

---

## ⚡ **Environment Variables Example**
Use the following `.env` file format:
```plaintext
MYSQL_HOST=localhost
MYSQL_USER=flask_user
MYSQL_PASSWORD=your_password
MYSQL_DB=flask_books
```

---

## 📜 **SQL Setup**
Here’s the `books.sql` file to set up your database:
```sql
CREATE DATABASE IF NOT EXISTS flask_books;
USE flask_books;

CREATE TABLE IF NOT EXISTS books (
    id INT AUTO_INCREMENT PRIMARY KEY,
    title VARCHAR(100) NOT NULL,
    author VARCHAR(100) NOT NULL,
    pages INT NOT NULL,
    genre VARCHAR(50) NOT NULL,
    summary TEXT
);
```

---

## 🛡️ **License**
This project is licensed under the MIT License. See the [LICENSE](LICENSE) file for details.

---

## 💡 **Acknowledgments**
- Flask documentation: [Flask Official Docs](https://flask.palletsprojects.com/)
- MySQL documentation: [MySQL Docs](https://dev.mysql.com/doc/)

