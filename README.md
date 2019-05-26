# Collabgator

<html>
  <body>
    <h1> Collabgator - Group Chat </h1>
  </body>
  </html>

Collabgator is a Django based web application that will be used for collaboration among teams in an organisation.
Currently, the Group Chat functionality is being developed which is a subset of the overall web application.

Program flow -
1) Root url, /signin and all undefined urls will point to the signin page
2) Firebase is used to authenticate users
3) Sign up and Forgot Password functionality is also employed thorugh Firebase
4) After signin, option to select chatroom is provided


TO DO:
1) Add password protection to chatrooms
2) Fixed database of the project ( Can't add data to models )
3) Show sender's email id with the message in the chat room.
