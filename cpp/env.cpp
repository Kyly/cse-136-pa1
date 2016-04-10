#include <iostream>
#include <stdlib.h>     /* getenv */

using namespace std;
int main ()
{

  cout << "Content-type: text/html" << endl << endl;
   cout << "<html>" << endl;
   cout << "<head> <meta charset='UTF-8'><title>We code in our underpants</title> <head>" << endl;
   cout << "<body>" << endl;

   cout << "<h1>Environment Variables</h1><br><br>" << endl;

   cout << "<h2> Browser Variables </h2>" << endl;
   cout << "<table>" << endl;
   cout << "<tr>" << endl;
   cout << "<th>ENVIRONMENT VARIABLE NAME</th>" << endl;
   cout << "<th>VALUE</th>" << endl;
   cout << "</tr>" << endl;
   cout << "<tr><td>HTTP_ACCEPT</td><td>" <<  getenv("HTTP_ACCEPT")  << "</td></tr>" << endl;
cout << "<tr><td>HTTP_ACCEPT_ENCODING</td><td>" <<  getenv("HTTP_ACCEPT_ENCODING")  << "</td></tr>" << endl;
cout << "<tr><td>HTTP_ACCEPT_LANGUAGE</td><td>" <<  getenv("HTTP_ACCEPT_LANGUAGE")  << "</td></tr>" << endl;
if(getenv("HTTP_CACHE_CONTROL")!=0)cout << "<tr><td>HTTP_CACHE_CONTROL</td><td>" <<  getenv("HTTP_CACHE_CONTROL")  << "</td></tr>" << endl;
cout << "<tr><td>HTTP_CONNECTION</td><td>" <<  getenv("HTTP_CONNECTION")  << "</td></tr>" << endl;
cout << "<tr><td>HTTP_COOKIE</td><td>" <<  getenv("HTTP_COOKIE")  << "</td></tr>" << endl;
if(getenv("HTTP_DNT")!=0) cout << "<tr><td>HTTP_DNT</td><td>" <<  getenv ("HTTP_DNT")  << "</td></tr>" << endl;
cout << "<tr><td>HTTP_HOST</td><td>" <<  getenv("HTTP_HOST")  << "</td></tr>" << endl;
if(getenv("HTTP_REFERER") != 0) cout << "<tr><td>HTTP_REFERER</td><td>" <<  getenv ("HTTP_REFERER")  << "</td></tr>" << endl;
cout << "<tr><td>HTTP_UPGRADE_INSECURE_REQUESTS</td><td>" <<  getenv("HTTP_UPGRADE_INSECURE_REQUESTS")  << "</td></tr>" << endl;
cout << "<tr><td>HTTP_USER_AGENT</td><td>" <<  getenv("HTTP_USER_AGENT")  << "</td></tr>" << endl;
    cout << "</table>" << endl;

    cout << "<h2>SERVER VARIABLES</h2>" << endl;
   cout << "<table>" << endl;
   cout << "<tr>" << endl;
   cout << "<th>ENVIRONMENT VARIABLE NAME</th>" << endl;
   cout << "<th>VALUE</th>" << endl;
   cout << "</tr>" << endl;

cout << "<tr><td>CONTEXT_DOCUMENT_ROOT</td><td>" <<  getenv("CONTEXT_DOCUMENT_ROOT")  << "</td></tr>" << endl;
cout << "<tr><td>CONTEXT_PREFIX</td><td>" <<  getenv("CONTEXT_PREFIX")  << "</td></tr>" << endl;
cout << "<tr><td>DOCUMENT_ROOT</td><td>" <<  getenv("DOCUMENT_ROOT")  << "</td></tr>" << endl;
cout << "<tr><td>GATEWAY_INTERFACE</td><td>" <<  getenv("GATEWAY_INTERFACE")  << "</td></tr>" << endl;
if(getenv("HOME") != 0) cout << "<tr><td>HOME</td><td>" <<  getenv("HOME")  << "</td></tr>" << endl;
cout << "<tr><td>PATH</td><td>" <<  getenv("PATH")  << "</td></tr>" << endl;
if(getenv("PATHEXT")!=0) cout << "<tr><td>PATHEXT</td><td>" <<  getenv("PATHEXT")  << "</td></tr>" << endl;
cout << "<tr><td>QUERY_STRING</td><td>" <<  getenv("QUERY_STRING")  << "</td></tr>" << endl;
cout << "<tr><td>REMOTE_ADDR</td><td>" <<  getenv("REMOTE_ADDR")  << "</td></tr>" << endl;
cout << "<tr><td>REMOTE_PORT</td><td>" <<  getenv("REMOTE_PORT")  << "</td></tr>" << endl;
cout << "<tr><td>REQUEST_METHOD</td><td>" <<  getenv("REQUEST_METHOD")  << "</td></tr>" << endl;
cout << "<tr><td>REQUEST_SCHEME</td><td>" <<  getenv("REQUEST_SCHEME")  << "</td></tr>" << endl;
cout << "<tr><td>REQUEST_URI</td><td>" <<  getenv("REQUEST_URI")  << "</td></tr>" << endl;
cout << "<tr><td>SCRIPT_FILENAME</td><td>" <<  getenv("SCRIPT_FILENAME")  << "</td></tr>" << endl;
cout << "<tr><td>SCRIPT_NAME</td><td>" <<  getenv("SCRIPT_NAME")  << "</td></tr>" << endl;
cout << "<tr><td>SERVER_ADDR</td><td>" <<  getenv("SERVER_ADDR")  << "</td></tr>" << endl;
cout << "<tr><td>SERVER_ADMIN</td><td>" <<  getenv("SERVER_ADMIN")  << "</td></tr>" << endl;
cout << "<tr><td>SERVER_NAME</td><td>" <<  getenv("SERVER_NAME")  << "</td></tr>" << endl;
cout << "<tr><td>SERVER_PORT</td><td>" <<  getenv("SERVER_PORT")  << "</td></tr>" << endl;
cout << "<tr><td>SERVER_PROTOCOL</td><td>" <<  getenv("SERVER_PROTOCOL")  << "</td></tr>" << endl;
cout << "<tr><td>SERVER_SIGNATURE</td><td>" <<  getenv("SERVER_SIGNATURE")  << "</td></tr>" << endl;
cout << "<tr><td>SERVER_SOFTWARE</td><td>" <<  getenv("SERVER_SOFTWARE")  << "</td></tr>" << endl;
if(getenv("TERM") != 0) cout << "<tr><td>TERM</td><td>" <<  getenv("TERM")  << "</td></tr>" << endl;

   cout << "</table>" << endl;
   cout << "</body>" << endl;
   cout << "</html>" << endl;

  return 0;
}