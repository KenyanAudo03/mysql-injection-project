# 🛡️ MySQL Injection Demo Project

This is a basic Flask-based web app built to **demonstrate SQL injection vulnerabilities** in login forms. It’s meant for educational use only — **do not deploy this to production.**

---

## ⚙️ 1. Prerequisites

- Python 3.x
- MySQL or MariaDB
- Flask
- `pip` (Python package manager)

---

## 🗃️ 2. Setting Up the Database

Start and access your MySQL server:

```bash
sudo systemctl start mysql
sudo mysql
```

CREATE DATABASE `sql-injection`;
USE `sql-injection`;

## 3. Creating a table on the database

CREATE TABLE user (
  ID INT AUTO_INCREMENT PRIMARY KEY,
  USERNAME VARCHAR(20) NOT NULL,
  PASSWORD VARCHAR(255) NOT NULL
);

INSERT INTO user VALUES 
(1, "admin", "admin123"), 
(2, "guest", "guest123");

## 👤 3. Creating a MySQL Use

CREATE USER 'username'@'localhost' IDENTIFIED BY 'userpass';
GRANT ALL PRIVILEGES ON `sql-injection`.* TO 'username'@'localhost';
FLUSH PRIVILEGES;
EXIT;

## 🚀 4. Running the App

``` bash
git clone
https://github.com/KenyanAudo03/mysql-injection-project.git
cd mysql-injection-project
pip install -r requirements.txt
```

- Run the Flask app:
  - ``` bash
	python app.py
	```

- Then open your browser and go to:
    - http://127.0.0.1:5000

## 🔐 5. SQL Injection Demo
To simulate an SQL injection:
- In the username field, enter a valid username followed by '#.
Example:
```bash
admin'#
```

- Enter any random value as password.
The injected '# breaks the SQL query and bypasses password validation.


---
💡 Why This Matters
This project shows how poor input handling can be exploited. Use this as a teaching tool to:

Demonstrate real-world vulnerabilities

Understand how to secure login forms using prepared statements

---

⚠️ Disclaimer
This is for educational use only. Do not use this code in any live project or attempt unauthorized access on real systems. Stay ethical.

---

✨ Credits
Made with 💻 by [Victor Owino]
Inspired by common security flaws in beginner backend apps.

---