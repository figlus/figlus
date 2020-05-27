<?php
	$servername="localhost";
	$mysql_user="root";
	$mysql_pass="cisco";
	$dbname="JPWP";


	if($_SERVER['REQUEST_METHOD'] == 'POST'){
		$conn=mysqli_connect($servername, $mysql_user, $mysql_pass, $dbname);
		$email=$_POST['email'];
		$password=$_POST['password'];
		$query="SELECT 'name' FROM registration WHERE (email=? AND password=?";
		$stmt=mysqli_prepare($conn, $query);
		mysqli_stmt_bind_param($stmt, 'ss', $email, $password);
		mysqli_stmt_execute($stmt);
  		mysqli_stmt_bind_result($stmt, $name);

  		if(mysqli_stmt_fetch($stmt)){
		    echo 'Hello ' . $name;
		    }else{
		    echo("Error");
		    }
		    
		} else {
		    echo("Error");
		}
					