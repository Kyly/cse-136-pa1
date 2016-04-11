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

   cout << "<h1>Environment Variables</h1><br><br>" << endl;

   cout << "<h2> Browser Variables </h2>" << endl;
   cout << "<table>" << endl;
   cout << "<tr>" << endl;
   cout << "<th>NAME</th>" << endl;
   cout << "<th>VALUE</th>" << endl;
   cout << "</tr>" << endl;
    int envsize = get_environ_length(environ);

    char *browvars [envsize];
    char *servvars [envsize];
    int browcount = 0;
    int servcount = 0;


    while(environ[count] != NULL)
    {
    	if(strstr(environ[count],"HTTP") != 0){
		browvars[browcount] = environ[count];
		browcount++;
	}
	else{
		servvars[servcount] = environ[count];
		servcount++;
	}
    	//cout << environ[count] << "<br>" << endl;
    	count++;
    }


    sort(browvars, browvars + browcount, compare);
    sort(servvars, servvars + servcount, compare);
    count = 0;


    while(browvars[count] != NULL){
	const char * separator = strchr(browvars[count], '=');
	if(separator == NULL) break;
	int index = separator - browvars[count];
	string pre(browvars[count], index);
	string post(browvars[count]+index+1);
        cout << "<tr><td>" << pre <<"</td><td>" << post << "</td></tr>" <<endl;
        count++;
    }


   cout << "</table>" << endl;

   cout << "<h2>SERVER VARIABLES</h2>" << endl;
   cout << "<table>" << endl;
   cout << "<tr>" << endl;
   cout << "<th>NAME</th>" << endl;
   cout << "<th>VALUE</th>" << endl;
   cout << "</tr>" << endl;

   count = 0;
   while(servvars[count] != NULL){
	const char * separator = strchr(servvars[count], '=');
	if(separator == NULL) break;
	int index = separator - servvars[count];
	string pre(servvars[count], index);
	string post(servvars[count]+index+1);
        cout << "<tr><td>" << pre <<"</td><td>" << post << "</td></tr>" <<endl;
        count++;
   }

   cout << "</table>" << endl;
    cout << "</body>" << endl;
    cout << "</html>" << endl;

   return 0;
}