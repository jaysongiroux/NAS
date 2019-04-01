# NAS
<h3><b> To Run: </b> </h3>
MAC: in terminal run the "run.sh" script. then enter NAS Login and Password. once this is entered everytime you run the program it will pull from the login.txt file created by the login.py script. <br>

WINDOWS: modify the python code where it says "USERNAME" and "PASSWORD" to your login credentials. then run from cmd. it will mount the drives and close its self.
  
  
<h3><b>Purpose: </b></h3>
-	To run on both OSX and windows <br>

-	Mounts a desired NAS drive through VPN and LAN assuming DNS is configured correctly. <br>

-	Be easily expandable in the event more servers are added<br>

-	Open Plex server in chrome<br>

-	Have a one time use login feature that stores login credentials in a separate document<br>


<h3><b>To be finished: </b> </h3>
-	Username and encryption algorithm to protect login credentials instead of being stored in plain text. 
-	GUI for windows
-	Server monitoring to determine if server is online before trying to mount to it. This would prevent time-out errors which take approx. 30 seconds for machines on OSX. 

