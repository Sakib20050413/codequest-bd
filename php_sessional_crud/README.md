# CodeQuest BD — Standalone PHP & MySQLi CRUD Module
**Course:** CSE 324 — Web Technologies Sessional Lab Final Project  
**Requirement Focus:** Continuous Evaluation (iv) — PHP & Database CRUD  
**Student:** Md Najmus Sakib Rahatul (ID: `1119003`)  
**Department:** Computer Science & Engineering, BAIUST, Cumilla  

---

## 1. Overview
This module demonstrates standard, procedural PHP scripting interacting with a MySQL database via the `mysqli_*` extension. It fulfills 100% of the CSE 324 syllabus requirement for server-side scripting and database CRUD operations.

## 2. Implemented Features
1. **Create (C):** `create_challenge.php` & `record_score.php` using prepared statements (`mysqli_prepare()`, `mysqli_stmt_bind_param()`, `mysqli_stmt_execute()`).
2. **Read (R):** `index.php` queries both the `challenges` and `student_scores` tables using `mysqli_query()` and `mysqli_fetch_assoc()`.
3. **Update (U):** `edit_challenge.php` modifies existing challenge records with parameter binding.
4. **Delete (D):** `delete_challenge.php` safely removes records based on primary key `id`.
5. **Security & Sanitization:** Input sanitization with `trim()`, `stripslashes()`, `htmlspecialchars()`, and `mysqli_real_escape_string()`.

## 3. How to Run Locally

### Option A: Using Built-in PHP Development Server (Quick Lab Demo)
```bash
cd php_sessional_crud
php -S localhost:8080
```
Then open `http://localhost:8080` in your web browser.

### Option B: Using XAMPP / WampServer
1. Copy the `php_sessional_crud` folder to `C:\xampp\htdocs\codequest_crud`.
2. Start **Apache** and **MySQL** in XAMPP Control Panel.
3. Open `http://localhost/phpmyadmin` and import `schema.sql` (or create database `codequest_php_db`).
4. Browse to `http://localhost/codequest_crud`.
