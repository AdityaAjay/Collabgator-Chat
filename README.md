# Collabgator

<html>
  <body>
    <h1> Collabgator - Group Chat </h1>
  </body>
  </html>

Collabgator is a Django based web application that will be used for collaboration among teams in an organisation.
Currently, the Group Chat functionality is being developed which is a subset of the overall web application.

Program flow -
1) Root url, /signin and all undefined urls will point to the sign-in page
2) Firebase is used to authenticate users
3) Sign up and Forgot Password functionality is also employed through Firebase
4) After signin, option to select chatroom is provided (26 May)
5) Added password protection to chatrooms (27 May 19:55)
         /chat url is open for all. Password is empty string.
6) Generalised the directory of static files using os.getcwd() 


TO DO:
1) Fix database of the project ( Can't add data to models ) -> Working fine for other projects.
2) Show sender's email id with the message in the chat room.
3) Fix upper and lower case URLs
