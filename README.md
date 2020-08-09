# tttproj (using Django,html5,css)
This is a web-application in which it fetches data from given server link using packages(bs4,requests) and helps to count the frequency of each word in the text/sentence provided.
In this "tttassign" is the project-name and "tttmain" is the app-name.
So at first if we open the url/website , from "tttassign" urls.py  it will move to "tttmain" urls.py ,initially page created in html5 can be seen with a number to enter.
Navbar.html of the page is stored in tttmain/templates/include/navbar.html. So this navbar.html page is extended in home.html as to reduce inconsistency in code.
If a number entered in the starting page and submitting it leads to definition "inte" in views.py which computes the frequency and returns to frontend in form of dict.
Finally in the frontend using table both keys and values are fetched in two different columns and result is displayed.
