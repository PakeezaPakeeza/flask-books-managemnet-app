
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
├── 📜 books.sql              # SQL script for database setup
├── 📜 README.md              # Project documentation
```
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

## 🎨 **Screenshots**
### **Homepage**
![Homepage](https://via.placeholder.com/800x400?text=Homepage+Screenshot)

### **Add a Book**
![Add Book](https://via.placeholder.com/800x400?text=Add+Book+Form)

## 🛡️ **License**
This project is licensed under the MIT License. See the [LICENSE](LICENSE) file for details.

---

## 💡 **Acknowledgments**
- Flask documentation: [Flask Official Docs](https://flask.palletsprojects.com/)
- MySQL documentation: [MySQL Docs](https://dev.mysql.com/doc/)

