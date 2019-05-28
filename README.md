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
4) After signin, option to select chatroom is provided 26 May
5) Added password protection to chatrooms 27 May 19:55
        *root /chat url is open for all. Password is empty string.


TO DO:
1) Fix database of the project ( Can't add data to models ) -> Working fine for other projects.
2) Show sender's email id with the message in the chat room.
3) Generalise the directory of static files using pathlib. Currently pointing to my pc's directory.
4) Add CSS to chat room page.

<html>
  <body>
    Login/Landing Page:
    <img src="https://i.imgur.com/R8CoVaG.png" alt="Login">

    SignUp Page:
        <img src="https://i.imgur.com/R8CoVaG.png" alt="Login">

    Password Reset Page:
        <img src="https://i.imgur.com/ZYF99SJ.png" alt="Login">

    Select Chatroom Page:
        <img src="https://i.imgur.com/hTcIRCk.png " alt="Login">

    Chatroom Password Prompt:
        <img src="https://i.imgur.com/8UpIMn7.png" alt="Login">

    Chatroom:
        <img src="https://i.imgur.com/oaPrr3i.png" alt="Login">

  </body>
  </html>
