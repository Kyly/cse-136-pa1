<?php

function startsWith($haystack, $needle) {
    // search backwards starting from haystack length characters from the end
    return $needle === "" || strrpos($haystack, $needle, -strlen($haystack)) !== false;
}

$server = array();
$browser = array();

$bo = $_SERVER;
ksort($bo);
foreach($bo as $key_name => $key_value) {
    if (startsWith($key_name, "HTTP_"))
        $browser[$key_name] = $key_value;
    else
        $server[$key_name] = $key_value;

}


Print ("<!DOCTYPE html><html>");
Print ("<head>");
//Print ("<style>");
//Print ("table, th, td { border: 1px solid black; border-collapse: collapse; }");
//Print ("</style>");
Print ("<title>We Code In Our Underpants</title>");
Print ("<meta charset='UTF-8'");
Print ("</head>");
Print("<body style='background-color: white;'>");



Print ("<h1>Server</h1>");
Print ("<table><tr><th>Name</th><th>Value</th></tr>");

foreach($server as $key_name => $key_value) {
    Print ("<tr><td>" . $key_name . "</td><td>" . $key_value . "</td></tr>");
}

Print ("</table>");
Print ("<br></br>");

Print ("<h1>Browser</h1>");
Print ("<table><tr><th>Name</th><th>Value</th></tr>");

foreach($browser as $key_name => $key_value) {
    Print ("<tr><td>" . $key_name . "</td><td>" . $key_value . "</td></tr>");
}

Print ("</table>");
Print ("<br></br>");



Print ("</body></html>");