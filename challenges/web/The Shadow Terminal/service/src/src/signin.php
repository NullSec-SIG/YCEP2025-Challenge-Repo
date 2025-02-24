<?php
session_start();
require 'vendor/autoload.php';

use Firebase\JWT\JWT;
use Firebase\JWT\Key;

error_reporting(0);

$secret = "secret123";
$message = "";

// NOTE: In production, NEVER store passwords in plain text.
$users_db = [
    'NULLSEC' => ['password' => 'sigmadjsalkj2302983209823', 'role' => 'admin'],
    'GUEST_USER' => ['password' => 'GUEST_PASS', 'role' => 'guest']
];

if (isset($_COOKIE['jwt_token'])) {
    header("Location: admin.php");
    exit;
}

if ($_SERVER["REQUEST_METHOD"] === "POST" && isset($_POST["username"]) && isset($_POST["password"])) {
    $username = trim($_POST["username"]);
    $password = trim($_POST["password"]);
    
    // Check credentials against our "database"
    if (isset($users_db[$username]) && $users_db[$username]['password'] === $password) {
        $payload = [
            "username" => $username,
            "role"     => $users_db[$username]['role'],
            "exp"      => time() + 3600
        ];
        $jwt = JWT::encode($payload, $secret, 'HS256');
        
        setcookie("jwt_token", $jwt, time() + 3600, "/");
        header("Location: admin.php");
        exit;
    } else {
        $message = "Invalid username or password!";
    }
}
?>
<!DOCTYPE html>
<html lang="en">
<head>
  <meta charset="UTF-8" />
  <meta name="viewport" content="width=device-width, initial-scale=1.0" />
  <title>Sign In - The Shadow Terminal</title>
  <link href="https://cdn.jsdelivr.net/npm/tailwindcss@2.2.19/dist/tailwind.min.css" rel="stylesheet" />
  <style>
    body {
      background-color: #000;
      color: #39ff14;
    }
    a {
      color: #39ff14;
    }
    .container {
      max-width: 600px;
      margin: auto;
      padding: 2rem;
    }
  </style>
</head>
<body>
  <div class="container mt-10">
    <h1 class="text-3xl font-bold mb-4">Sign In to The Shadow Terminal</h1>
    <?php if ($message): ?>
      <div class="bg-red-500 text-black p-2 mb-4"><?php echo htmlspecialchars($message); ?></div>
    <?php endif; ?>
    <form method="POST" class="bg-gray-800 p-6 rounded">
      <label class="block mb-2">Username:</label>
      <input type="text" name="username" class="w-full p-2 mb-4 bg-gray-900 border border-green-500 text-green-300" placeholder="Enter your username" required>
      
      <label class="block mb-2">Password:</label>
      <input type="password" name="password" class="w-full p-2 mb-4 bg-gray-900 border border-green-500 text-green-300" placeholder="Enter your password" required>
      
      <button type="submit" class="w-full bg-green-600 hover:bg-green-700 p-2 rounded">Sign In</button>
    </form>
  </div>
</body>
</html>
