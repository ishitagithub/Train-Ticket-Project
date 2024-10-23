<?php

if ($_SERVER["REQUEST_METHOD"] == "POST") {
    $fname = $_POST['fname'];
    $lname = $_POST['lname'];
    $tname = $_POST['tname'];
    $tno = $_POST['tno'];
    $email = $_POST['email'];
    $tel = $_POST['tel'];
    $date = $_POST['date'];

    $servername = "localhost";
    $username = "root";
    $password = "Mysql";
    $dbname = "trainProject";

    $conn = new mysqli($servername, $username, $password, $dbname);
    if ($conn->connect_error) {
        die("Connection failed: " . $conn->connect_error);
    }

    $stmt = $conn->prepare("INSERT INTO ticket_book (fname, lname, tname, tno, email, tel, date) VALUES (?, ?, ?, ?, ?, ?, ?)");
    $stmt->bind_param("sssisss", $fname, $lname, $tname, $tno, $email, $tel, $date);

    if ($stmt->execute() === TRUE) {
        // Redirect to pass.html with URL parameters
        header("Location: passBooking.html?fname=$fname&lname=$lname&tname=$tname&tno=$tno&email=$email&tel=$tel&date=$date");
        exit();
    } else {
        echo "Error: " . $stmt->error;
    }
    

    $stmt->close();
    $conn->close();
}

?>
