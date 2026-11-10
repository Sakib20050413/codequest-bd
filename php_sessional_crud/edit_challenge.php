<?php
require_once 'db.php';

$id = isset($_GET['id']) ? (int)$_GET['id'] : 0;
$errors = [];
$challenge = null;

if ($db_connected && $id > 0) {
    $stmt = mysqli_prepare($conn, "SELECT * FROM challenges WHERE id = ?");
    mysqli_stmt_bind_param($stmt, "i", $id);
    mysqli_stmt_execute($stmt);
    $res = mysqli_stmt_get_result($stmt);
    $challenge = mysqli_fetch_assoc($res);
    mysqli_stmt_close($stmt);
}

if (!$challenge) {
    $challenge = [
        'id' => $id,
        'title' => 'Sample Challenge',
        'track' => 'C Programming',
        'difficulty' => 'Beginner',
        'engine' => 'CODE_JUDGE',
        'xp_reward' => 100,
        'starter_code' => '',
        'expected_output' => ''
    ];
}

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

    if (empty($errors)) {
        if ($db_connected) {
            $stmt = mysqli_prepare($conn, "UPDATE challenges SET title = ?, track = ?, difficulty = ?, engine = ?, xp_reward = ?, starter_code = ?, expected_output = ? WHERE id = ?");
            if ($stmt) {
                mysqli_stmt_bind_param($stmt, "ssssissi", $title, $track, $difficulty, $engine, $xp_reward, $starter_code, $expected_output, $id);
                if (mysqli_stmt_execute($stmt)) {
                    mysqli_stmt_close($stmt);
                    header("Location: index.php?msg=updated");
                    exit;
                } else {
                    $errors[] = "MySQL update error: " . mysqli_error($conn);
                }
            }
        } else {
            header("Location: index.php?msg=updated");
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
    <title>Edit Challenge — PHP MySQLi CRUD</title>
    <script src="https://cdn.tailwindcss.com"></script>
    <link href="https://cdnjs.cloudflare.com/ajax/libs/font-awesome/6.4.0/css/all.min.css" rel="stylesheet">
</head>
<body class="bg-slate-950 text-slate-100 min-h-screen p-6">
    <div class="max-w-3xl mx-auto bg-slate-900 border border-slate-800 rounded-2xl p-8 shadow-2xl">
        <div class="flex justify-between items-center pb-6 border-b border-slate-800 mb-6">
            <div>
                <h1 class="text-2xl font-bold text-white flex items-center gap-2">
                    <i class="fa-solid fa-pen-to-square text-indigo-400"></i> Edit Challenge #<?php echo $id; ?>
                </h1>
                <p class="text-xs text-slate-400 mt-1">Executes prepared `UPDATE challenges WHERE id = ?` via MySQLi</p>
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

        <form method="POST" class="space-y-6">
            <div>
                <label class="block text-xs uppercase font-semibold text-slate-300 mb-2">Challenge Title *</label>
                <input type="text" name="title" required value="<?php echo htmlspecialchars($challenge['title']); ?>" class="w-full bg-slate-950 border border-slate-700 rounded-xl px-4 py-2.5 text-white focus:outline-none focus:border-indigo-500">
            </div>

            <div class="grid grid-cols-1 md:grid-cols-3 gap-4">
                <div>
                    <label class="block text-xs uppercase font-semibold text-slate-300 mb-2">Track *</label>
                    <select name="track" class="w-full bg-slate-950 border border-slate-700 rounded-xl px-4 py-2.5 text-white focus:outline-none focus:border-indigo-500">
                        <?php 
                        $tracks = ["C Programming", "C++ OOP & STL", "Python Automation", "JavaScript & DOM", "PHP & MySQL", "HTML5 & CSS3"];
                        foreach ($tracks as $t) {
                            $sel = ($challenge['track'] == $t) ? 'selected' : '';
                            echo "<option value='$t' $sel>$t</option>";
                        }
                        ?>
                    </select>
                </div>
                <div>
                    <label class="block text-xs uppercase font-semibold text-slate-300 mb-2">Difficulty</label>
                    <select name="difficulty" class="w-full bg-slate-950 border border-slate-700 rounded-xl px-4 py-2.5 text-white focus:outline-none focus:border-indigo-500">
                        <?php 
                        $diffs = ["Beginner", "Intermediate", "Advanced"];
                        foreach ($diffs as $d) {
                            $sel = ($challenge['difficulty'] == $d) ? 'selected' : '';
                            echo "<option value='$d' $sel>$d</option>";
                        }
                        ?>
                    </select>
                </div>
                <div>
                    <label class="block text-xs uppercase font-semibold text-slate-300 mb-2">Game Engine</label>
                    <select name="engine" class="w-full bg-slate-950 border border-slate-700 rounded-xl px-4 py-2.5 text-white focus:outline-none focus:border-indigo-500">
                        <?php 
                        $engines = ["CODE_JUDGE" => "Mode 3: Code Judge", "ROVER_MAZE" => "Mode 1: Rover Maze", "DOM_BUILDER" => "Mode 2: DOM Builder"];
                        foreach ($engines as $k => $v) {
                            $sel = ($challenge['engine'] == $k) ? 'selected' : '';
                            echo "<option value='$k' $sel>$v</option>";
                        }
                        ?>
                    </select>
                </div>
            </div>

            <div>
                <label class="block text-xs uppercase font-semibold text-slate-300 mb-2">XP Reward</label>
                <input type="number" name="xp_reward" value="<?php echo $challenge['xp_reward']; ?>" min="50" max="500" class="w-full bg-slate-950 border border-slate-700 rounded-xl px-4 py-2.5 text-white focus:outline-none focus:border-indigo-500">
            </div>

            <div>
                <label class="block text-xs uppercase font-semibold text-slate-300 mb-2">Starter Code Template</label>
                <textarea name="starter_code" rows="4" class="w-full bg-slate-950 border border-slate-700 rounded-xl p-3 font-mono text-sm text-emerald-400 focus:outline-none focus:border-indigo-500"><?php echo htmlspecialchars($challenge['starter_code'] ?? ''); ?></textarea>
            </div>

            <div>
                <label class="block text-xs uppercase font-semibold text-slate-300 mb-2">Expected Standard Output</label>
                <textarea name="expected_output" rows="2" class="w-full bg-slate-950 border border-slate-700 rounded-xl p-3 font-mono text-sm text-amber-300 focus:outline-none focus:border-indigo-500"><?php echo htmlspecialchars($challenge['expected_output'] ?? ''); ?></textarea>
            </div>

            <div class="flex justify-end gap-3 pt-4 border-t border-slate-800">
                <a href="index.php" class="px-5 py-2.5 rounded-xl border border-slate-700 text-slate-400 hover:text-white text-sm">Cancel</a>
                <button type="submit" class="bg-indigo-600 hover:bg-indigo-500 text-white font-bold px-6 py-2.5 rounded-xl text-sm flex items-center gap-2 transition shadow-lg shadow-indigo-600/20">
                    <i class="fa-solid fa-check"></i> Update Challenge (UPDATE)
                </button>
            </div>
        </form>
    </div>
</body>
</html>
