<?php
require_once 'db.php';

$errors = [];

if ($_SERVER['REQUEST_METHOD'] === 'POST') {
    $title           = sanitize_input($conn, $_POST['title'] ?? '');
    $track           = sanitize_input($conn, $_POST['track'] ?? '');
    $difficulty      = sanitize_input($conn, $_POST['difficulty'] ?? 'Beginner');
    $engine          = sanitize_input($conn, $_POST['engine'] ?? 'CODE_JUDGE');
    $xp_reward       = (int)($_POST['xp_reward'] ?? 100);
    $starter_code    = $_POST['starter_code'] ?? '';
    $expected_output = $_POST['expected_output'] ?? '';

    if (empty($title)) {
        $errors[] = "Challenge Title is required.";
    }
    if (empty($track)) {
        $errors[] = "Language Track is required.";
    }

    if (empty($errors)) {
        if ($db_connected) {
            $stmt = mysqli_prepare($conn, "INSERT INTO challenges (title, track, difficulty, engine, xp_reward, starter_code, expected_output) VALUES (?, ?, ?, ?, ?, ?, ?)");
            if ($stmt) {
                mysqli_stmt_bind_param($stmt, "ssssiss", $title, $track, $difficulty, $engine, $xp_reward, $starter_code, $expected_output);
                if (mysqli_stmt_execute($stmt)) {
                    mysqli_stmt_close($stmt);
                    header("Location: index.php?msg=created");
                    exit;
                } else {
                    $errors[] = "MySQL execution error: " . mysqli_error($conn);
                }
            } else {
                $errors[] = "Prepare statement error: " . mysqli_error($conn);
            }
        } else {
            // Simulated success if testing without local MySQL
            header("Location: index.php?msg=created");
            exit;
        }
    }
}
?>
<!DOCTYPE html>
<html lang="en">
<head>
    <meta charset="UTF-8">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <title>Add Challenge — PHP MySQLi CRUD</title>
    <script src="https://cdn.tailwindcss.com"></script>
    <link href="https://cdnjs.cloudflare.com/ajax/libs/font-awesome/6.4.0/css/all.min.css" rel="stylesheet">
</head>
<body class="bg-slate-950 text-slate-100 min-h-screen p-6">
    <div class="max-w-3xl mx-auto bg-slate-900 border border-slate-800 rounded-2xl p-8 shadow-2xl">
        <div class="flex justify-between items-center pb-6 border-b border-slate-800 mb-6">
            <div>
                <h1 class="text-2xl font-bold text-white flex items-center gap-2">
                    <i class="fa-solid fa-square-plus text-emerald-400"></i> Insert New Coding Challenge
                </h1>
                <p class="text-xs text-slate-400 mt-1">Executes prepared `INSERT INTO challenges` via MySQLi</p>
            </div>
            <a href="index.php" class="text-slate-400 hover:text-white text-sm bg-slate-800 px-3 py-1.5 rounded-lg border border-slate-700">
                Cancel / Back
            </a>
        </div>

        <?php if (!empty($errors)): ?>
            <div class="bg-rose-950/40 border border-rose-500/30 text-rose-300 rounded-xl p-4 mb-6 text-sm">
                <ul class="list-disc list-inside space-y-1">
                    <?php foreach ($errors as $e): ?>
                        <li><?php echo htmlspecialchars($e); ?></li>
                    <?php endforeach; ?>
                </ul>
            </div>
        <?php endif; ?>

        <form method="POST" class="space-y-6">
            <div>
                <label class="block text-xs uppercase font-semibold text-slate-300 mb-2">Challenge Title *</label>
                <input type="text" name="title" required placeholder="e.g., Matrix Inversion in C" class="w-full bg-slate-950 border border-slate-700 rounded-xl px-4 py-2.5 text-white focus:outline-none focus:border-emerald-500">
            </div>

            <div class="grid grid-cols-1 md:grid-cols-3 gap-4">
                <div>
                    <label class="block text-xs uppercase font-semibold text-slate-300 mb-2">Track *</label>
                    <select name="track" class="w-full bg-slate-950 border border-slate-700 rounded-xl px-4 py-2.5 text-white focus:outline-none focus:border-emerald-500">
                        <option value="C Programming">C Programming</option>
                        <option value="C++ OOP & STL">C++ OOP & STL</option>
                        <option value="Python Automation">Python Automation</option>
                        <option value="JavaScript & DOM">JavaScript & DOM</option>
                        <option value="PHP & MySQL">PHP & MySQL</option>
                        <option value="HTML5 & CSS3">HTML5 & CSS3</option>
                    </select>
                </div>
                <div>
                    <label class="block text-xs uppercase font-semibold text-slate-300 mb-2">Difficulty</label>
                    <select name="difficulty" class="w-full bg-slate-950 border border-slate-700 rounded-xl px-4 py-2.5 text-white focus:outline-none focus:border-emerald-500">
                        <option value="Beginner">Beginner</option>
                        <option value="Intermediate">Intermediate</option>
                        <option value="Advanced">Advanced</option>
                    </select>
                </div>
                <div>
                    <label class="block text-xs uppercase font-semibold text-slate-300 mb-2">Game Engine</label>
                    <select name="engine" class="w-full bg-slate-950 border border-slate-700 rounded-xl px-4 py-2.5 text-white focus:outline-none focus:border-emerald-500">
                        <option value="CODE_JUDGE">Mode 3: Code Judge</option>
                        <option value="ROVER_MAZE">Mode 1: Rover Maze</option>
                        <option value="DOM_BUILDER">Mode 2: DOM Builder</option>
                    </select>
                </div>
            </div>

            <div>
                <label class="block text-xs uppercase font-semibold text-slate-300 mb-2">XP Reward (50 - 500)</label>
                <input type="number" name="xp_reward" value="100" min="50" max="500" class="w-full bg-slate-950 border border-slate-700 rounded-xl px-4 py-2.5 text-white focus:outline-none focus:border-emerald-500">
            </div>

            <div>
                <label class="block text-xs uppercase font-semibold text-slate-300 mb-2">Starter Code Template</label>
                <textarea name="starter_code" rows="4" class="w-full bg-slate-950 border border-slate-700 rounded-xl p-3 font-mono text-sm text-emerald-400 focus:outline-none focus:border-emerald-500" placeholder="#include <stdio.h>&#10;int main() { ... }"></textarea>
            </div>

            <div>
                <label class="block text-xs uppercase font-semibold text-slate-300 mb-2">Expected Standard Output</label>
                <textarea name="expected_output" rows="2" class="w-full bg-slate-950 border border-slate-700 rounded-xl p-3 font-mono text-sm text-amber-300 focus:outline-none focus:border-emerald-500" placeholder="e.g., SUCCESS or 120"></textarea>
            </div>

            <div class="flex justify-end gap-3 pt-4 border-t border-slate-800">
                <a href="index.php" class="px-5 py-2.5 rounded-xl border border-slate-700 text-slate-400 hover:text-white text-sm">Cancel</a>
                <button type="submit" class="bg-emerald-500 hover:bg-emerald-400 text-slate-950 font-bold px-6 py-2.5 rounded-xl text-sm flex items-center gap-2 transition shadow-lg shadow-emerald-500/20">
                    <i class="fa-solid fa-check"></i> Save Challenge (INSERT)
                </button>
            </div>
        </form>
    </div>
</body>
</html>
