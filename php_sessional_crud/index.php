<?php
require_once 'db.php';

$message = '';
$msg_type = 'info';

if (isset($_GET['msg'])) {
    if ($_GET['msg'] == 'created') {
        $message = 'Coding challenge created successfully!';
        $msg_type = 'success';
    } elseif ($_GET['msg'] == 'updated') {
        $message = 'Coding challenge updated successfully!';
        $msg_type = 'success';
    } elseif ($_GET['msg'] == 'deleted') {
        $message = 'Coding challenge deleted successfully!';
        $msg_type = 'danger';
    } elseif ($_GET['msg'] == 'score_recorded') {
        $message = 'Student score recorded successfully!';
        $msg_type = 'success';
    }
}

// Fetch all challenges
$challenges = [];
if ($db_connected) {
    $sql = "SELECT * FROM challenges ORDER BY id DESC";
    $result = mysqli_query($conn, $sql);
    if ($result) {
        while ($row = mysqli_fetch_assoc($result)) {
            $challenges[] = $row;
        }
    }
}

// Fetch all student scores
$scores = [];
if ($db_connected) {
    $sql_scores = "SELECT s.*, c.title AS challenge_title FROM student_scores s LEFT JOIN challenges c ON s.challenge_id = c.id ORDER BY s.id DESC LIMIT 10";
    $res_scores = mysqli_query($conn, $sql_scores);
    if ($res_scores) {
        while ($row = mysqli_fetch_assoc($res_scores)) {
            $scores[] = $row;
        }
    }
}
?>
<!DOCTYPE html>
<html lang="en">
<head>
    <meta charset="UTF-8">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <title>CodeQuest BD — PHP & MySQLi CRUD Module (CSE 324 Evaluation iv)</title>
    <script src="https://cdn.tailwindcss.com"></script>
    <link href="https://cdnjs.cloudflare.com/ajax/libs/font-awesome/6.4.0/css/all.min.css" rel="stylesheet">
</head>
<body class="bg-slate-950 text-slate-100 min-h-screen">
    <!-- Header -->
    <header class="bg-slate-900 border-b border-slate-800 py-4 px-6">
        <div class="max-w-7xl mx-auto flex flex-col md:flex-row justify-between items-center gap-4">
            <div class="flex items-center space-x-3">
                <div class="w-10 h-10 rounded-lg bg-emerald-500 flex items-center justify-center font-black text-slate-950 text-xl shadow-lg shadow-emerald-500/20">
                    🐘
                </div>
                <div>
                    <h1 class="text-xl font-bold tracking-tight text-white flex items-center gap-2">
                        CodeQuest BD <span class="text-xs bg-emerald-500/10 text-emerald-400 border border-emerald-500/30 px-2 py-0.5 rounded font-mono">PHP & MySQLi CRUD</span>
                    </h1>
                    <p class="text-xs text-slate-400">
                        CSE 324 Web Technologies Sessional | Md Najmus Sakib Rahatul (ID: 1119003), BAIUST
                    </p>
                </div>
            </div>
            <div class="flex items-center gap-3">
                <a href="create_challenge.php" class="bg-emerald-500 hover:bg-emerald-400 text-slate-950 font-semibold px-4 py-2 rounded-lg text-sm flex items-center gap-2 transition shadow-lg shadow-emerald-500/20">
                    <i class="fa-solid fa-plus"></i> Add New Challenge
                </a>
                <a href="record_score.php" class="bg-indigo-600 hover:bg-indigo-500 text-white font-semibold px-4 py-2 rounded-lg text-sm flex items-center gap-2 transition shadow-lg shadow-indigo-600/20">
                    <i class="fa-solid fa-trophy"></i> Record Score
                </a>
                <a href="/" class="bg-slate-800 hover:bg-slate-700 text-slate-300 font-semibold px-4 py-2 rounded-lg text-sm flex items-center gap-2 transition border border-slate-700">
                    <i class="fa-solid fa-arrow-left"></i> Back to Main App
                </a>
            </div>
        </div>
    </header>

    <main class="max-w-7xl mx-auto p-6 space-y-8">
        <?php if (!$db_connected): ?>
            <div class="bg-amber-950/40 border border-amber-500/30 rounded-xl p-5 text-amber-200">
                <div class="flex items-start gap-3">
                    <i class="fa-solid fa-triangle-exclamation text-amber-400 text-xl mt-0.5"></i>
                    <div>
                        <h3 class="font-bold text-amber-300">MySQL Database Connection Notice</h3>
                        <p class="text-xs text-amber-200/80 mt-1">
                            Could not connect to MySQL server (<code><?php echo htmlspecialchars($db_error_msg); ?></code>).
                        </p>
                        <p class="text-xs text-amber-200/70 mt-2">
                            To test live with MySQL during lab viva: Start MySQL in XAMPP or run <code>mysql -u root < schema.sql</code>. All procedural PHP CRUD code is written following strict CSE 324 rubric!
                        </p>
                    </div>
                </div>
            </div>
        <?php endif; ?>

        <?php if ($message): ?>
            <div class="<?php echo $msg_type == 'danger' ? 'bg-rose-950/40 border-rose-500/30 text-rose-300' : 'bg-emerald-950/40 border-emerald-500/30 text-emerald-300'; ?> border rounded-xl p-4 flex items-center justify-between text-sm">
                <span><?php echo htmlspecialchars($message); ?></span>
                <span class="text-xs opacity-60">Dismiss</span>
            </div>
        <?php endif; ?>

        <!-- Stats Bar -->
        <div class="grid grid-cols-1 md:grid-cols-4 gap-4">
            <div class="bg-slate-900 border border-slate-800 rounded-xl p-5">
                <span class="text-xs font-semibold text-slate-400 uppercase tracking-wider">Total Challenges</span>
                <p class="text-3xl font-extrabold text-white mt-2"><?php echo count($challenges); ?></p>
                <span class="text-xs text-emerald-400 mt-1 block"><i class="fa-solid fa-database"></i> MySQL Table: `challenges`</span>
            </div>
            <div class="bg-slate-900 border border-slate-800 rounded-xl p-5">
                <span class="text-xs font-semibold text-slate-400 uppercase tracking-wider">Student Evaluations</span>
                <p class="text-3xl font-extrabold text-indigo-400 mt-2"><?php echo count($scores); ?></p>
                <span class="text-xs text-indigo-300 mt-1 block"><i class="fa-solid fa-users"></i> Table: `student_scores`</span>
            </div>
            <div class="bg-slate-900 border border-slate-800 rounded-xl p-5">
                <span class="text-xs font-semibold text-slate-400 uppercase tracking-wider">Lab Student</span>
                <p class="text-base font-bold text-white mt-2">Md Najmus Sakib Rahatul</p>
                <span class="text-xs text-slate-400 mt-1 block">ID: 1119003 | CSE 3-2 (A)</span>
            </div>
            <div class="bg-slate-900 border border-slate-800 rounded-xl p-5">
                <span class="text-xs font-semibold text-slate-400 uppercase tracking-wider">CRUD Implementation</span>
                <p class="text-sm font-bold text-emerald-400 mt-2">100% Procedural PHP</p>
                <span class="text-xs text-slate-400 mt-1 block">mysqli_connect, prepare, execute</span>
            </div>
        </div>

        <!-- Challenges CRUD Table -->
        <section class="bg-slate-900 border border-slate-800 rounded-2xl overflow-hidden shadow-xl">
            <div class="p-5 border-b border-slate-800 flex flex-col md:flex-row justify-between items-start md:items-center gap-3">
                <div>
                    <h2 class="text-lg font-bold text-white flex items-center gap-2">
                        <i class="fa-solid fa-code text-emerald-400"></i> Active Coding Challenges (CRUD)
                    </h2>
                    <p class="text-xs text-slate-400">All challenge records stored and manipulated via MySQLi queries</p>
                </div>
                <a href="create_challenge.php" class="bg-emerald-500 hover:bg-emerald-400 text-slate-950 font-semibold px-3 py-1.5 rounded-lg text-xs flex items-center gap-1.5 transition">
                    <i class="fa-solid fa-plus"></i> Insert Challenge
                </a>
            </div>

            <div class="overflow-x-auto">
                <table class="w-full text-left text-sm text-slate-300">
                    <thead class="bg-slate-950/60 text-xs uppercase text-slate-400 font-semibold border-b border-slate-800">
                        <tr>
                            <th class="p-4">ID</th>
                            <th class="p-4">Challenge Title</th>
                            <th class="p-4">Track</th>
                            <th class="p-4">Difficulty</th>
                            <th class="p-4">Engine</th>
                            <th class="p-4">XP Reward</th>
                            <th class="p-4 text-right">Actions</th>
                        </tr>
                    </thead>
                    <tbody class="divide-y divide-slate-800/60">
                        <?php if (empty($challenges)): ?>
                            <tr>
                                <td colspan="7" class="p-8 text-center text-slate-500">
                                    No challenge records found in database. Click "Add New Challenge" to insert one!
                                </td>
                            </tr>
                        <?php else: ?>
                            <?php foreach ($challenges as $c): ?>
                                <tr class="hover:bg-slate-800/40 transition">
                                    <td class="p-4 font-mono text-xs text-slate-400">#<?php echo $c['id']; ?></td>
                                    <td class="p-4 font-semibold text-white"><?php echo htmlspecialchars($c['title']); ?></td>
                                    <td class="p-4"><span class="bg-slate-800 px-2.5 py-1 rounded-md text-xs"><?php echo htmlspecialchars($c['track']); ?></span></td>
                                    <td class="p-4">
                                        <span class="text-xs px-2.5 py-0.5 rounded-full font-medium <?php 
                                            echo $c['difficulty'] == 'Beginner' ? 'bg-emerald-500/10 text-emerald-400 border border-emerald-500/30' : 
                                                ($c['difficulty'] == 'Intermediate' ? 'bg-blue-500/10 text-blue-400 border border-blue-500/30' : 'bg-purple-500/10 text-purple-400 border border-purple-500/30'); ?>">
                                            <?php echo htmlspecialchars($c['difficulty']); ?>
                                        </span>
                                    </td>
                                    <td class="p-4 text-xs font-mono text-slate-400"><?php echo htmlspecialchars($c['engine']); ?></td>
                                    <td class="p-4 font-bold text-amber-400">+<?php echo $c['xp_reward']; ?> XP</td>
                                    <td class="p-4 text-right space-x-2">
                                        <a href="edit_challenge.php?id=<?php echo $c['id']; ?>" class="text-indigo-400 hover:text-indigo-300 bg-indigo-500/10 hover:bg-indigo-500/20 border border-indigo-500/30 px-3 py-1 rounded text-xs transition">
                                            <i class="fa-solid fa-pen-to-square"></i> Edit
                                        </a>
                                        <a href="delete_challenge.php?id=<?php echo $c['id']; ?>" onclick="return confirm('Are you sure you want to delete this challenge?');" class="text-rose-400 hover:text-rose-300 bg-rose-500/10 hover:bg-rose-500/20 border border-rose-500/30 px-3 py-1 rounded text-xs transition">
                                            <i class="fa-solid fa-trash"></i> Delete
                                        </a>
                                    </td>
                                </tr>
                            <?php endforeach; ?>
                        <?php endif; ?>
                    </tbody>
                </table>
            </div>
        </section>

        <!-- Student Scores Table -->
        <section class="bg-slate-900 border border-slate-800 rounded-2xl overflow-hidden shadow-xl">
            <div class="p-5 border-b border-slate-800 flex justify-between items-center">
                <div>
                    <h2 class="text-lg font-bold text-white flex items-center gap-2">
                        <i class="fa-solid fa-award text-amber-400"></i> Recent Sessional Lab Evaluations
                    </h2>
                    <p class="text-xs text-slate-400">Scores recorded via `INSERT INTO student_scores`</p>
                </div>
                <a href="record_score.php" class="bg-indigo-600 hover:bg-indigo-500 text-white font-semibold px-3 py-1.5 rounded-lg text-xs flex items-center gap-1.5 transition">
                    <i class="fa-solid fa-plus"></i> Record Score
                </a>
            </div>

            <div class="overflow-x-auto">
                <table class="w-full text-left text-sm text-slate-300">
                    <thead class="bg-slate-950/60 text-xs uppercase text-slate-400 font-semibold border-b border-slate-800">
                        <tr>
                            <th class="p-4">Student ID</th>
                            <th class="p-4">Student Name</th>
                            <th class="p-4">Challenge Evaluated</th>
                            <th class="p-4">Language</th>
                            <th class="p-4">Score Awarded</th>
                            <th class="p-4">Timestamp</th>
                        </tr>
                    </thead>
                    <tbody class="divide-y divide-slate-800/60">
                        <?php if (empty($scores)): ?>
                            <tr>
                                <td colspan="6" class="p-8 text-center text-slate-500">
                                    No student evaluation records found.
                                </td>
                            </tr>
                        <?php else: ?>
                            <?php foreach ($scores as $s): ?>
                                <tr class="hover:bg-slate-800/40 transition">
                                    <td class="p-4 font-mono font-semibold text-emerald-400"><?php echo htmlspecialchars($s['student_id']); ?></td>
                                    <td class="p-4 text-white font-medium"><?php echo htmlspecialchars($s['student_name']); ?></td>
                                    <td class="p-4 text-slate-300"><?php echo htmlspecialchars($s['challenge_title'] ?? 'Generic Task'); ?></td>
                                    <td class="p-4"><span class="bg-slate-800 px-2 py-0.5 rounded text-xs"><?php echo htmlspecialchars($s['language_used']); ?></span></td>
                                    <td class="p-4 font-bold text-amber-400"><?php echo $s['score']; ?> pts</td>
                                    <td class="p-4 text-xs text-slate-400"><?php echo $s['evaluated_at']; ?></td>
                                </tr>
                            <?php endforeach; ?>
                        <?php endif; ?>
                    </tbody>
                </table>
            </div>
        </section>
    </main>
</body>
</html>
