#!/usr/bin/env php

<?php

$randInt = rand(1, 16);
$timezone = date_default_timezone_set("Y-m-d H:i:s");

$colors = array("aqua", "black", "blue", "fuchsia", "gray", "green", "lime", "maroon", "navy",
    "olive", "purple", "red", "silver", "teal", "white", "yellow");

$text="black";
if ($randInt == 2)
    $text="white";


Print ("Content-Type: text/html");
Print ("");
Print ("<!DOCTYPE html><html>");
Print ("<html>");
Print ("<head>");
Print ("<title>We Code In Our Underpants</title>");
Print ("<meta charset='UTF-8'");
Print ("</head>");
Print ("<body style='background-color: " . $colors[$randInt-1] . "; color: " . $text . ";' ><h1>Hello World from PHP @" . $timezone . '</h1>');
Print ("</body></html>");