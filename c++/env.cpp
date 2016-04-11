#include <iostream>
#include <stdlib.h>     /* getenv */
#include <algorithm>
#include <string.h>

using namespace std;

int get_environ_length(char ** env){
	int i = 0;
	while(env[i] != NULL){i++;}
	return i;
}

bool compare(char* i, char * j){ return strcmp(i,j) < 0; }

int main ()
{

extern char **environ;

int count = 0;

  cout << "Content-type: text/html" << endl << endl;
   cout << "<html>" << endl;
   cout << "<head> <meta charset='UTF-8'><title>We code in our underpants</title> <head>" << endl;
   cout << "<body>" << endl;

int envsize = get_environ_length(environ);
char *envvars [envsize];

while(environ[count] != NULL)
{
	envvars[count] = environ[count];
	//cout << environ[count] << "<br>" << endl;
	count++;
}

sort(envvars, envvars + envsize, compare);
count = 0;
while(envvars[count] != NULL){
cout << envvars[count] <<"<br>" <<endl;
count++;
}
   cout << "   </body>" << endl;
   cout << "</html>" << endl;

  return 0;
}