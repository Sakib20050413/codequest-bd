-- CodeQuest BD: CSE 324 Web Technologies Sessional
-- Evaluation iv: Standalone PHP & MySQLi CRUD Module
-- Student: Md Najmus Sakib Rahatul (ID: 1119003)
-- Department of CSE, BAIUST, Cumilla

CREATE DATABASE IF NOT EXISTS codequest_php_db CHARACTER SET utf8mb4 COLLATE utf8mb4_unicode_ci;
USE codequest_php_db;

-- 1. Challenges Table
CREATE TABLE IF NOT EXISTS challenges (
    id INT AUTO_INCREMENT PRIMARY KEY,
    title VARCHAR(150) NOT NULL,
    track VARCHAR(50) NOT NULL,
    difficulty ENUM('Beginner', 'Intermediate', 'Advanced') DEFAULT 'Beginner',
    engine ENUM('ROVER_MAZE', 'DOM_BUILDER', 'CODE_JUDGE') DEFAULT 'CODE_JUDGE',
    xp_reward INT DEFAULT 100,
    starter_code TEXT,
    expected_output TEXT,
    created_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP
);

-- 2. Student Scores Table
CREATE TABLE IF NOT EXISTS student_scores (
    id INT AUTO_INCREMENT PRIMARY KEY,
    student_id VARCHAR(20) NOT NULL,
    student_name VARCHAR(100) NOT NULL,
    challenge_id INT,
    language_used VARCHAR(30) NOT NULL,
    score INT DEFAULT 100,
    evaluated_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP,
    FOREIGN KEY (challenge_id) REFERENCES challenges(id) ON DELETE SET NULL
);

-- Seed Initial Challenges
INSERT INTO challenges (title, track, difficulty, engine, xp_reward, starter_code, expected_output) VALUES
('Grid Rover 101: Loop Straight', 'C Programming', 'Beginner', 'ROVER_MAZE', 100, '#include <stdio.h>\nint main() {\n  for(int i=0; i<3; i++) printf("MOVE_FORWARD\\n");\n  return 0;\n}', 'REACHED_PORTAL'),
('DOM Shield Activator', 'JavaScript & DOM', 'Intermediate', 'DOM_BUILDER', 150, 'document.getElementById("shield").classList.add("active");', 'SHIELD_ACTIVE'),
('Student Record Inserter', 'PHP & MySQL', 'Intermediate', 'CODE_JUDGE', 200, '<?php\n// Write mysqli_query INSERT query\n$sql = "INSERT INTO students (id, name) VALUES (1119003, '\''Sakib'\'')";\necho "RECORD_INSERTED";\n?>', 'RECORD_INSERTED');

-- Seed Initial Scores
INSERT INTO student_scores (student_id, student_name, challenge_id, language_used, score) VALUES
('1119003', 'Md Najmus Sakib Rahatul', 1, 'C', 100),
('1119003', 'Md Najmus Sakib Rahatul', 2, 'JavaScript', 150),
('1119001', 'Tanvir Ahmed', 1, 'C', 100);
