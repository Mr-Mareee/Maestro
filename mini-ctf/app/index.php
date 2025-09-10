<?php
// app/index.php
$db = new PDO('sqlite:' . __DIR__ . '/data.sqlite');
$db->setAttribute(PDO::ATTR_ERRMODE, PDO::ERRMODE_EXCEPTION);

echo "<h2>Test sempre per il mio progetto di Web Applications (il primo non sembra piaciuto molto al prof) – Login</h2>";
echo '<form method="GET">
  <label>User: <input name="user"></label><br>
  <label>Pass: <input name="pass" type="password"></label><br>
  <button type="submit">Login</button>
</form>
<hr>';

if (isset($_GET['user']) && isset($_GET['pass'])) {
    $u = $_GET['user'];
    $p = $_GET['pass'];

    // VULNERABILE: concatenazione diretta in SQL
    $sql = "SELECT id, username FROM users WHERE username = '$u' AND password = '$p'";
    //echo "<p><b>Query (in chiaro):</b> <code>$sql</code></p>";

    try {
        $rows = $db->query($sql)->fetchAll(PDO::FETCH_ASSOC);
        if ($rows && count($rows) > 0) {
            echo "<p style='color:green'>Login OK! Benvenuto, " . htmlspecialchars($rows[0]['username']) . ".</p>";
        } else {
            echo "<p style='color:red'>Credenziali errate.</p>";
        }
    } catch (Exception $e) {
        echo "<p style='color:red'>Errore DB: " . htmlspecialchars($e->getMessage()) . "</p>";
    }
}

//echo "<hr><p>Tip: prova injection tipo <code>' OR '1'='1</code> 😉</p>";
