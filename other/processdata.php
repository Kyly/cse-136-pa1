<?php
/**
 * Created by IntelliJ IDEA.
 * User: abbas
 * Date: 4/10/16
 * Time: 7:15 PM
 */

if ($_REQUEST["name"]) {
    $name = $_REQUEST["name"];
    $password = $_REQUEST["password"];
    $magicnumber = $_REQUEST["magicnumber"];
}

//else if ($_POST["name"]) {
//    $name = $_GET["name"];
//    $password = $_GET["password"];
//    $magicnumber = $_GET["magicnumber"];
//}

Print ("<!DOCTYPE html> <html> <head> <meta charset='UTF-8'><title>We code in our underpants</title>");
Print ("<body style='background-color: white'>");

for ($i = 0; $i < $magicnumber; $i++) {
    Print ("<h1>Hello " . $name . " with a password of " . $password . " </h1>");
}

Print ("</body></html>");
