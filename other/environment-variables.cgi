#!/bin/bash

echo "Content-Type: text/html"
echo ""
echo '<html>'
echo '<head>'
echo '<meta http-equiv="Content-Type" content="text/html; charset=UTF-8">'
echo '<title>Environment Variables</title>'
echo "<style>"
echo "table, th, td { border: 1px solid black; border-collapse: collapse; }"
echo "th, td { padding: 5px; }"
echo "</style>"

echo '</head>'
echo '<body>'

echo '<h1>ENVIRONMENT VARIABLES</h1> <br><br>'

#Browser Settings
echo '<h2>BROWSER VARIABLES</h2>'
echo '<table>'
echo '<tr>'
echo '<th>ENVIRONMENT VARIABLE NAME</th>'
echo '<th>VALUE</th>'
echo '</tr>'
echo "<tr><td>HTTP_ACCEPT</td><td>${HTTP_ACCEPT}</td></tr>"
echo "<tr><td>HTTP_ACCEPT_ENCODING</td><td>${HTTP_ACCEPT_ENCODING}</td></tr>"
echo "<tr><td>HTTP_ACCEPT_LANGUAGE</td><td>${HTTP_ACCEPT_LANGUAGE}</td></tr>"
echo "<tr><td>HTTP_CACHE_CONTROL</td><td>${HTTP_CACHE_CONTROL}</td></tr>"
echo "<tr><td>HTTP_CONNECTION</td><td>${HTTP_CONNECTION}</td></tr>"
echo "<tr><td>HTTP_DNT</td><td>${HTTP_DNT}</td></tr>"
echo "<tr><td>HTTP_HOST</td><td>${HTTP_HOST}</td></tr>"
echo "<tr><td>HTTP_UPGRADE_INSECURE_REQUESTS</td><td>${HTTP_UPGRADE_INSECURE_REQUESTS}</td></tr>"
echo "<tr><td>HTTP_USER_AGENT</td><td>${HTTP_USER_AGENT}</td></tr>"
echo '</table>'

echo '<h2>SERVER VARIABLES</h2>'
echo '<table>'
echo '<tr>'
echo '<th>ENVIRONMENT VARIABLE NAME</th>'
echo '<th>VALUE</th>'
echo '</tr>'
echo "<tr><td>CONTEXT_DOCUMENT_ROOT</td><td>${CONTEXT_DOCUMENT_ROOT}</td></tr>"
echo "<tr><td>CONTEXT_PREFIX</td><td>${CONTEXT_PREFIX}</td></tr>"
echo "<tr><td>DOCUMENT_ROOT</td><td>${DOCUMENT_ROOT}</td></tr>"
echo "<tr><td>GATEWAY_INTERFACE</td><td>${GATEWAY_INTERFACE}</td></tr>"
echo "<tr><td>PATH</td><td>${PATH}</td></tr>"
echo "<tr><td>QUERY_STRING</td><td>${QUERY_STRING}</td></tr>"
echo "<tr><td>REMOTE_ADDR</td><td>${REMOTE_ADDR}</td></tr>"
echo "<tr><td>REMOTE_PORT</td><td>${REMOTE_PORT}</td></tr>"
echo "<tr><td>REQUEST_METHOD</td><td>${REQUEST_METHOD}</td></tr>"
echo "<tr><td>REQUEST_SCHEME</td><td>${REQUEST_SCHEME}</td></tr>"
echo "<tr><td>REQUEST_URI</td><td>${REQUEST_URI}</td></tr>"
echo "<tr><td>SCRIPT_FILENAME</td><td>${SCRIPT_FILENAME}</td></tr>"
echo "<tr><td>SCRIPT_NAME</td><td>${SCRIPT_NAME}</td></tr>"
echo "<tr><td>SERVER_ADDR</td><td>${SERVER_ADDR}</td></tr>"
echo "<tr><td>SERVER_ADMIN</td><td>${SERVER_ADMIN}</td></tr>"
echo "<tr><td>SERVER_NAME</td><td>${SERVER_NAME}</td></tr>"
echo "<tr><td>SERVER_PORT</td><td>${SERVER_PORT}</td></tr>"
echo "<tr><td>SERVER_PROTOCOL</td><td>${SERVER_PROTOCOL}</td></tr>"
echo "<tr><td>SERVER_SIGNATURE</td><td>${SERVER_SIGNATURE}</td></tr>"
echo "<tr><td>SERVER_SOFTWARE</td><td>${SERVER_SOFTWARE}</td></tr>"
echo '</table>'
echo '</body>'
echo '</html>'

