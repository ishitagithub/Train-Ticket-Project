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

    $stmt = $conn->prepare("SELECT * FROM ticket_book");
    $stmt->execute();
    $result = $stmt->get_result();

    while ($row = $result->fetch_assoc()) {
        if ($row['tno'] == $tno && $row['date'] == $date) {
            $stmt = $conn->prepare("DELETE FROM ticket_book WHERE tno = ? LIMIT 1");
            $stmt->bind_param("i", $tno);
            $stmt->execute();
            $stmt->close();
            $conn->close();

            include('passCancelling.html');
            exit();
        }
    }

    $conn->close();
    include('pass2Cancelling.html');
}

?>
