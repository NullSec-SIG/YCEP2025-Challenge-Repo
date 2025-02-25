<?php
session_start();
setcookie("jwt_token", "", time() - 3600, "/");
header("Location: signin.php");
exit;
