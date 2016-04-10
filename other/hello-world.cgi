#!/bin/bash

echo "Content-Type: text/html"
echo ""
echo "<html>"
echo "<head>"
echo '<meta http-equiv="Content-Type" content="text/html" charset="UTF-8">'
echo "<title>Hello World</title>"
case $(( RANDOM % (16 - 1 + 1 ) + 1 )) in
    1) echo "<style>body {background-color: aqua}</style>"
       ;;
    2) echo "<style>body {background-color: black; color: white;}</style>"
       ;;
    3) echo "<style>body {background-color: blue; color: white;}</style>"
       ;;
    4) echo "<style>body {background-color: fuchsia}</style>"
       ;;
    5) echo "<style>body {background-color: gray}</style>"
       ;;
    6) echo "<style>body {background-color: green}</style>"
       ;;
    7) echo "<style>body {background-color: lime}</style>"
       ;;
    8) echo "<style>body {background-color: maroon}</style>"
       ;;
    9) echo "<style>body {background-color: navy; color: white;}</style>"
       ;;
    10) echo "<style>body {background-color: olive}</style>"
        ;;
    11) echo "<style>body {background-color: purple; color: white;}</style>"
        ;;
    12) echo "<style>body {background-color: red}</style>"
        ;;
    13) echo "<style>body {background-color: silver}</style>"
        ;;
    14) echo "<style>body {background-color: teal}</style>"
        ;;
    15) echo "<style>body {background-color: white}</style>"
        ;;
    16) echo "<style>body {background-color: yellow}</style>"
        ;;
esac

echo "</head>"
echo "<body>Hello World from BASH @ $(date)</body>"
echo "</html>"

