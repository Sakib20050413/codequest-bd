<?php
/**
 * CodeQuest BD - Database Connection (MySQLi Procedural)
 * CSE 324 Web Technologies Sessional (Evaluation iv: PHP CRUD)
 * Student: Md Najmus Sakib Rahatul (ID: 1119003), CSE, BAIUST
 */

$host     = getenv('MYSQL_HOST') ?: '127.0.0.1';
$username = getenv('MYSQL_USER') ?: 'root';
$password = getenv('MYSQL_PASSWORD') ?: '';
$database = getenv('MYSQL_DATABASE') ?: 'codequest_php_db';
$port     = getenv('MYSQL_PORT') ? (int)getenv('MYSQL_PORT') : 3306;

// Create MySQLi connection
$conn = @mysqli_connect($host, $username, $password, $database, $port);

// If connection fails, provide clear pedagogical error message or fallback notice
$db_connected = true;
$db_error_msg = "";

if (!$conn) {
    $db_connected = false;
    $db_error_msg = mysqli_connect_error();
} else {
    mysqli_set_charset($conn, "utf8mb4");
}

/**
 * Helper to sanitize user inputs against SQL Injection and XSS
 */
function sanitize_input($conn, $data) {
    $data = trim($data);
    $data = stripslashes($data);
    $data = htmlspecialchars($data, ENT_QUOTES, 'UTF-8');
    if ($conn) {
        $data = mysqli_real_escape_string($conn, $data);
    }
    return $data;
}
?>
