<?php
include('koneksi.php');
if($_GET['aksi']=='tambah'){
	$name=$_POST['name'];
	$cat=$_POST['id_category'];
	$cashier=$_POST['id_cashier'];
	$price=$_POST['price'];
	$results=mysqli_query($mysqli,"insert into product(name,id_category,id_cashier,price) values('$name','$cat','$cashier','$price')");
	if($results){
		header("location:index.php");
	}else{
		echo "ERROR, data gagal ditambahkan".mysqli_error($mysqli);
	}
}
else if($_GET['aksi']=='edit'){
    $id_cashier = $_POST['id_cashier'];
    $id_category = $_POST['id_category'];
    $name = $_POST['name'];
    $price = $_POST['price'];
	$id = $_GET['id'];
    //query update
    $query = mysqli_query($mysqli, "UPDATE product SET name='$name' , id_cashier='$id_cashier' , id_category='$id_category', price='$price' WHERE id='$id'");

    if ($query) {
        header("location:index.php");    
    }
    else{
        echo "ERROR, data gagal diupdate". mysqli_error($mysqli);
    }
}else if($_GET['aksi'] == 'delete'){
	$id=$_GET['id'];
	$querydelete=mysqli_query($mysqli, "delete from product where id='$id'");
	if($querydelete){
		header("Location:index.php");
	}
	mysqli_close($mysqli);
}
?>