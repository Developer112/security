import socket
import time
print("Created by Security Researcher")
time.sleep(1)
print("This program is meant to protect people from phishing.")
time.sleep(1)
x = socket.gethostbyname(raw_input(" eg: google.com \n Enter real site url: "))
y = socket.gethostbyname(raw_input(" eg: google.com \n Enter suspicious site ur$
print("Now it will compare the site IPs.")
len1 = len(x)
len2 = len(y)
match1 = x[::len1 - 3]
match2 = y[::len2 - 3]
if x != y :
        if match1 != match2 :
                print("Phishing site detected: " + y)
else:
        print("The site is safe!")
