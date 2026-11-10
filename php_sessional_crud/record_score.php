<?php
require_once 'db.php';

$errors = [];
$challenges = [];

if ($db_connected) {
    $res = mysqli_query($conn, "SELECT id, title FROM challenges ORDER BY title ASC");
    if ($res) {
        while ($row = mysqli_fetch_assoc($res)) {
            $challenges[] = $row;
        }
    }
}

if ($_SERVER['REQUEST_METHOD'] === 'POST') {
    $student_id    = sanitize_input($conn, $_POST['student_id'] ?? '');
    $student_name  = sanitize_input($conn, $_POST['student_name'] ?? '');
    $challenge_id  = (int)($_POST['challenge_id'] ?? 0);
    $language_used = sanitize_input($conn, $_POST['language_used'] ?? 'C');
    $score         = (int)($_POST['score'] ?? 100);

    if (empty($student_id) || empty($student_name)) {
        $errors[] = "Student ID and Name are required.";
    }

    if (empty($errors)) {
        if ($db_connected) {
            $stmt = mysqli_prepare($conn, "INSERT INTO student_scores (student_id, student_name, challenge_id, language_used, score) VALUES (?, ?, ?, ?, ?)");
            if ($stmt) {
                mysqli_stmt_bind_param($stmt, "ssisi", $student_id, $student_name, $challenge_id, $language_used, $score);
                if (mysqli_stmt_execute($stmt)) {
                    mysqli_stmt_close($stmt);
                    header("Location: index.php?msg=score_recorded");
                    exit;
                } else {
                    $errors[] = "MySQL insert error: " . mysqli_error($conn);
                }
            }
        } else {
            header("Location: index.php?msg=score_recorded");
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
    <title>Record Student Score — PHP MySQLi CRUD</title>
    <script src="https://cdn.tailwindcss.com"></script>
    <link href="https://cdnjs.cloudflare.com/ajax/libs/font-awesome/6.4.0/css/all.min.css" rel="stylesheet">
</head>
<body class="bg-slate-950 text-slate-100 min-h-screen p-6">
    <div class="max-w-xl mx-auto bg-slate-900 border border-slate-800 rounded-2xl p-8 shadow-2xl">
        <div class="flex justify-between items-center pb-6 border-b border-slate-800 mb-6">
            <div>
                <h1 class="text-xl font-bold text-white flex items-center gap-2">
                    <i class="fa-solid fa-trophy text-amber-400"></i> Record Sessional Lab Score
                </h1>
                <p class="text-xs text-slate-400 mt-1">Inserts a verified score row into `student_scores`</p>
            </div>
            <a href="index.php" class="text-slate-400 hover:text-white text-sm bg-slate-800 px-3 py-1.5 rounded-lg border border-slate-700">
                Cancel
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

        <form method="POST" class="space-y-5">
            <div>
                <label class="block text-xs uppercase font-semibold text-slate-300 mb-2">Student ID *</label>
                <input type="text" name="student_id" required value="1119003" class="w-full bg-slate-950 border border-slate-700 rounded-xl px-4 py-2.5 text-white focus:outline-none focus:border-amber-500">
            </div>

            <div>
                <label class="block text-xs uppercase font-semibold text-slate-300 mb-2">Student Full Name *</label>
                <input type="text" name="student_name" required value="Md Najmus Sakib Rahatul" class="w-full bg-slate-950 border border-slate-700 rounded-xl px-4 py-2.5 text-white focus:outline-none focus:border-amber-500">
            </div>

            <div>
                <label class="block text-xs uppercase font-semibold text-slate-300 mb-2">Coding Challenge</label>
                <select name="challenge_id" class="w-full bg-slate-950 border border-slate-700 rounded-xl px-4 py-2.5 text-white focus:outline-none focus:border-amber-500">
                    <?php if (empty($challenges)): ?>
                        <option value="1">Challenge 1: Grid Rover Loop</option>
                        <option value="2">Challenge 2: DOM Shield</option>
                    <?php else: ?>
                        <?php foreach ($challenges as $c): ?>
                            <option value="<?php echo $c['id']; ?>"><?php echo htmlspecialchars($c['title']); ?></option>
                        <?php endforeach; ?>
                    <?php endif; ?>
                </select>
            </div>

            <div class="grid grid-cols-2 gap-4">
                <div>
                    <label class="block text-xs uppercase font-semibold text-slate-300 mb-2">Language Used</label>
                    <select name="language_used" class="w-full bg-slate-950 border border-slate-700 rounded-xl px-4 py-2.5 text-white focus:outline-none focus:border-amber-500">
                        <option value="C">C</option>
                        <option value="C++">C++</option>
                        <option value="Python">Python</option>
                        <option value="JavaScript">JavaScript</option>
                        <option value="PHP">PHP</option>
                    </select>
                </div>
                <div>
                    <label class="block text-xs uppercase font-semibold text-slate-300 mb-2">Score Awarded</label>
                    <input type="number" name="score" value="100" min="10" max="500" class="w-full bg-slate-950 border border-slate-700 rounded-xl px-4 py-2.5 text-white focus:outline-none focus:border-amber-500">
                </div>
            </div>

            <div class="flex justify-end gap-3 pt-4 border-t border-slate-800">
                <a href="index.php" class="px-5 py-2.5 rounded-xl border border-slate-700 text-slate-400 hover:text-white text-sm">Cancel</a>
                <button type="submit" class="bg-amber-500 hover:bg-amber-400 text-slate-950 font-bold px-6 py-2.5 rounded-xl text-sm flex items-center gap-2 transition shadow-lg shadow-amber-500/20">
                    <i class="fa-solid fa-trophy"></i> Save Score
                </button>
            </div>
        </form>
    </div>
</body>
</html>
