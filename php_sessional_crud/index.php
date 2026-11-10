<?php
require_once "db.php";

// 1. CREATE (INSERT)
if (isset($_POST['create_task'])) {
    $title = mysqli_real_escape_string($conn, $_POST['title']);
    $lang  = mysqli_real_escape_string($conn, $_POST['language']);
    $diff  = mysqli_real_escape_string($conn, $_POST['difficulty']);
    $xp    = (int)$_POST['xp_reward'];
    mysqli_query($conn, "INSERT INTO practice_tasks (title, language, difficulty, xp_reward) VALUES ('$title', '$lang', '$diff', $xp)");
    header("Location: index.php");
    exit;
}

// 2. UPDATE
if (isset($_POST['update_task'])) {
    $id    = (int)$_POST['id'];
    $title = mysqli_real_escape_string($conn, $_POST['title']);
    $lang  = mysqli_real_escape_string($conn, $_POST['language']);
    $diff  = mysqli_real_escape_string($conn, $_POST['difficulty']);
    $xp    = (int)$_POST['xp_reward'];
    mysqli_query($conn, "UPDATE practice_tasks SET title='$title', language='$lang', difficulty='$diff', xp_reward=$xp WHERE id=$id");
    header("Location: index.php");
    exit;
}

// 3. DELETE
if (isset($_GET['delete'])) {
    $id = (int)$_GET['delete'];
    mysqli_query($conn, "DELETE FROM practice_tasks WHERE id=$id");
    header("Location: index.php");
    exit;
}

// 4. FETCH FOR EDIT
$edit = ['id' => '', 'title' => '', 'language' => 'Python 3', 'difficulty' => 'Easy', 'xp_reward' => 100];
if (isset($_GET['edit'])) {
    $id = (int)$_GET['edit'];
    $res = mysqli_query($conn, "SELECT * FROM practice_tasks WHERE id=$id");
    if ($res && mysqli_num_rows($res) > 0) {
        $edit = mysqli_fetch_assoc($res);
    }
}
?>
<!DOCTYPE html>
<html lang="en">
<head>
  <meta charset="UTF-8">
  <title>CodeQuest LMS — PHP & MySQLi CRUD Manager (CSE 324)</title>
  <style>
    body { font-family: Arial, sans-serif; background: #f8fafc; color: #0f172a; padding: 28px; }
    .wrap { max-width: 920px; margin: 0 auto; background: #fff; border: 1px solid #cbd5e1; border-radius: 10px; padding: 24px; }
    table { width: 100%; border-collapse: collapse; margin-top: 18px; }
    th, td { border: 1px solid #cbd5e1; padding: 10px 12px; text-align: left; font-size: 14px; }
    th { background: #0f172a; color: #fff; }
    input, select { padding: 8px 10px; border: 1px solid #94a3b8; border-radius: 6px; margin-right: 8px; }
    button { padding: 8px 16px; background: #1d4ed8; color: #fff; border: none; border-radius: 6px; cursor: pointer; }
  </style>
</head>
<body>
  <div class="wrap">
    <h2>CodeQuest LMS — PHP & MySQLi Task CRUD (CSE 324 Evaluation iv)</h2>
    <form method="POST" action="index.php">
      <input type="hidden" name="id" value="<?= htmlspecialchars($edit['id']) ?>">
      <input type="text" name="title" placeholder="Task Title" value="<?= htmlspecialchars($edit['title']) ?>" required>
      <select name="language">
        <option value="HTML5 & CSS3">HTML5 & CSS3</option>
        <option value="JavaScript DOM">JavaScript DOM</option>
        <option value="Python 3">Python 3</option>
        <option value="PHP & SQL">PHP & SQL</option>
      </select>
      <select name="difficulty">
        <option value="Easy">Easy</option>
        <option value="Medium">Medium</option>
        <option value="Hard">Hard</option>
      </select>
      <input type="number" name="xp_reward" value="<?= (int)$edit['xp_reward'] ?>" style="width:90px;">
      <?php if ($edit['id']): ?>
        <button type="submit" name="update_task">Update Task</button>
      <?php else: ?>
        <button type="submit" name="create_task">Save New Task</button>
      <?php endif; ?>
    </form>

    <table>
      <thead>
        <tr><th>ID</th><th>Title</th><th>Language</th><th>Difficulty</th><th>XP</th><th>Actions</th></tr>
      </thead>
      <tbody>
        <?php
        $rows = mysqli_query($conn, "SELECT * FROM practice_tasks ORDER BY id DESC");
        if ($rows):
          while ($r = mysqli_fetch_assoc($rows)): ?>
            <tr>
              <td><?= (int)$r['id'] ?></td>
              <td><?= htmlspecialchars($r['title']) ?></td>
              <td><?= htmlspecialchars($r['language']) ?></td>
              <td><?= htmlspecialchars($r['difficulty']) ?></td>
              <td><?= (int)$r['xp_reward'] ?> XP</td>
              <td>
                <a href="index.php?edit=<?= (int)$r['id'] ?>">Edit</a> |
                <a href="index.php?delete=<?= (int)$r['id'] ?>" onclick="return confirm('Delete this task?')">Delete</a>
              </td>
            </tr>
        <?php endwhile; endif; ?>
      </tbody>
    </table>
  </div>
</body>
</html>
