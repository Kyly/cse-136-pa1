#include <iostream>
#include <stdio.h>      /* printf */
#include <stdlib.h>     /* getenv */

using namespace std;
int main ()
{

extern char **environ;

int count = 0;

  cout << "Content-type: text/html" << endl << endl;
   cout << "<html>" << endl;
   cout << "<head> <meta charset='UTF-8'><title>We code in our underpants</title> <head>" << endl;
   cout << "<body bgcolor=\"white\">" << endl;
   cout << "   <body>" << endl;


while(environ[count] != NULL)
{
	cout << environ[count] << "<br>" << endl;
	count++;
}

   cout << "   </body>" << endl;
   cout << "</html>" << endl;

  return 0;
}