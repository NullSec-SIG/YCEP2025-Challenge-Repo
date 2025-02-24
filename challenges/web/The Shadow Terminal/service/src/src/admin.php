<?php
session_start();
require 'vendor/autoload.php';

use Firebase\JWT\JWT;
use Firebase\JWT\Key;

error_reporting(0);

$secret = "secret123";
$FLAG = "YCEP25{W3AK_JWT_PA55W0RD}";

if (!isset($_COOKIE['jwt_token'])) {
    header("Location: signin.php");
    exit;
}

try {
    $decoded = JWT::decode($_COOKIE['jwt_token'], new Key($secret, 'HS256'));
} catch (Exception $e) {
    header("Location: signin.php");
    exit;
}

$userRole = isset($decoded->role) ? $decoded->role : "guest";
?>
<!DOCTYPE html>
<html lang="en">
<head>
  <meta charset="UTF-8" />
  <meta name="viewport" content="width=device-width, initial-scale=1.0" />
  <title>Admin Panel - The Shadow Terminal</title>
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
      max-width: 1000px;
      margin: auto;
      padding: 2rem;
    }
  </style>
</head>
<body>
  <div class="container mt-10">
    <?php if ($userRole !== "admin"): ?>
      <h1 class="text-3xl font-bold mb-4">ACCESS DENIED</h1>
      <p class="mb-4">
        You are signed in as <strong><?php echo htmlspecialchars($decoded->username); ?></strong> with role <strong><?php echo htmlspecialchars($userRole); ?></strong>.<br>
        Only users with <strong>admin</strong> privileges can access this section.
      </p>
      <a href="logout.php" class="underline">Sign out and try again</a>
    <?php else: ?>
      <h1 class="text-3xl font-bold mb-4">Welcome, Admin!</h1>
      <p class="mb-4">Access granted. Here is your secret flag:</p>
      <div class="bg-gray-800 p-4 border border-green-500 rounded">
        <code><?php echo $FLAG; ?></code>
      </div>
      <a href="logout.php" class="underline mt-4 inline-block">Sign out</a>
    <?php endif; ?>
  </div>
</body>
</html>
