<?php
session_start();
?>
<!DOCTYPE html>
<html lang="en">
<head>
  <meta charset="UTF-8" />
  <meta name="viewport" content="width=device-width, initial-scale=1.0" />
  <title>The Shadow Terminal - Hacker Forum</title>
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
      max-width: 800px;
      margin: auto;
      padding: 2rem;
    }
  </style>
</head>
<body>
  <nav class="p-4 border-b border-green-500">
    <div class="container flex justify-between">
      <h1 class="text-3xl font-bold">The Shadow Terminal</h1>
      <div>
        <a href="signin.php" class="mr-4">Sign In</a>
        <a href="signin.php">Login</a>
      </div>
    </div>
  </nav>

  <div class="container mt-10">
    <h2 class="text-2xl font-bold mb-4">Welcome to the Underground Hacker Forum</h2>
    <p>
      Learn hacking today, exchange knowledge, and explore the digital underworld. Dive deep into discussions about exploits, vulnerabilities, and bypassing security measures. Our community is full of rebels who are not afraid to challenge the status quo.
    </p>
    
    <div class="mt-8">
      <h3 class="text-xl font-semibold mb-2">Latest Threads:</h3>
      <ul class="list-disc ml-5">
        <li>Exploiting JWT Vulnerabilities</li>
        <li>Privilege Escalation Techniques</li>
        <li>Secrets of the Dark Web</li>
      </ul>
    </div>
  </div>
</body>
</html>
