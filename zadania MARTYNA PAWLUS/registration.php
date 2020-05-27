<?php

// upewnij się, czy dane się zgadzają z tymi, które znajdziesz w zakładce Konta użytkowników na localhost/phpmyadmin
$servername="localhost";
$mysql_user="root";
$mysql_pass="cisco";
$dbname="JPWP";
$conn=mysqli_connect($servername, $mysql_user, $mysql_pass, $dbname);

if($_SERVER['REQUEST_METHOD']=='POST'){
    $name=$_POST["name"];
    $surname=$_POST["surname"];
    $email=$_POST["email"];
    $password1=$_POST["password1"];
    $password2=$_POST["password2"];
    //TODO
    $name_regexp="/^[a-żA-Ż]+[a-żA-Ż\ ]{3,}$/";
    $name_check = preg_match($name_regexp, $name);
    //TODO
    $surname_regexp="/^[a-żA-Ż]+[a-żA-Ż\-]*$/";
    $surname_check = preg_match($surname_regexp, $surname);
    //TODO
    $email_regexp='/^[a-zA-Z0-9\-\_\.]+\@[a-zA-Z0-9\-\_\.]+\.[a-zA-Z]{2,5}$/D';
    $email_check = preg_match($email_regexp, $email);
    
    //TODO odpowiednio sprawdź czy hasła się zgadzają
    if($password1 == $password2){
        if(($name_check == true) && ($surname_check == true) && ($email_check == true)){
            $query="INSERT INTO `registration`(`name`, `surname`, `email`, `password`) VALUES (?,?,?,?)";
            $stmt = mysqli_prepare($conn, $query);
            mysqli_stmt_bind_param($stmt, 'ssss', $name, $surname, $email, $password1);
            mysqli_stmt_execute($stmt);

            if(mysqli_stmt_affected_rows($stmt) == 1) {
                echo("registered successfully");
            }else{
                echo("error in registration");
            }
        } else {
            echo("Error in expression");
        }
    } else {
        echo("Wrong password");
    }
}else{
echo("error in request method");
}
?>