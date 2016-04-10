import java.util.*;
import java.text.SimpleDateFormat;

public class HelloWorld {

    public static void main(String[] args) {
    	// Header portion of the code
	System.out.println("Content-type: text/html\n\n");
	System.out.println("<html>\n<head>\n<title>Hello CGI World</title>\n</head>\n");
	
	// set the body background color
	Random rn = new Random();
	int colorNum = rn.nextInt(16) + 1;
	String color = "";
	switch(colorNum){
		case 1: color = "aqua";
		break;
                case 2: color = "black";
                break;
                case 3: color = "blue";
                break;
                case 4: color = "fuchsia";
                break;
                case 5: color = "gray";
                break;
                case 6: color = "green";
                break;
                case 7: color = "lime";
                break;
                case 8: color = "maroon";
                break;
                case 9: color = "navy";
                break;
                case 10: color = "olive";
                break;
                case 11: color = "purple";
                break;
                case 12: color = "red";
                break;
                case 13: color = "silver";
                break;
                case 14: color = "teal";
                break;
                case 15: color = "white";
                break;
                case 16: color = "yellow";
                break;
	}
	System.out.println("<body bgcolor = '" + color + "'>\n");

	// set time and print Hello World message
	String timeStamp = new SimpleDateFormat("MM/dd/yyyy_HH:mm:ss").format(Calendar.getInstance().getTime());
    	System.out.println("<h1>Hello World from Java @ " + timeStamp + "</h1>\n");
	// html bottom
	System.out.println("</body>\n</html>");         
    }

}
