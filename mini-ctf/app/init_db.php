<?php
// app/init_db.php
$dbFile = __DIR__ . '/data.sqlite';
try {
    $db = new PDO('sqlite:' . $dbFile);
    $db->setAttribute(PDO::ATTR_ERRMODE, PDO::ERRMODE_EXCEPTION);
    $db->exec('CREATE TABLE IF NOT EXISTS users (
        id INTEGER PRIMARY KEY AUTOINCREMENT,
        username TEXT UNIQUE,
        password TEXT
    )');

    // Inserisci utenti se la tabella è vuota
    $count = $db->query('SELECT COUNT(*) FROM users')->fetchColumn();
    if ($count == 0) {
        $stmt = $db->prepare('INSERT OR IGNORE INTO users (username, password) VALUES (?, ?)');
        $stmt->execute(['peter', 'peter123!']);  // peter è anche utente di sistema con sudo
        $stmt->execute(['alice', 'wonderland']);
        $stmt->execute(['bob',   'builder']);
    }

    echo "DB init done\n";
} catch (Exception $e) {
    echo "DB init error: " . $e->getMessage() . "\n";
    exit(1);
}
