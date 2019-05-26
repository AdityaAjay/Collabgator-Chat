from django.shortcuts import render
from django.http import HttpResponse
import pyrebase, time
from django.contrib import auth

signedIn = False
# api for firebase
config = {
    'apiKey': "AIzaSyAyDYH4GiqlzRqEVObqaLinTHW3IbX4Q3o",
    'authDomain': "collabgator.firebaseapp.com",
    'databaseURL': "https://collabgator.firebaseio.com",
    'projectId': "collabgator",
    'storageBucket': "collabgator.appspot.com",
    'messagingSenderId': "610129888834",
    'appId': "1:610129888834:web:64bfa75232a66633"
}
firebase = pyrebase.initialize_app(config)
authe = firebase.auth()
database = firebase.database()


def signIn(request):
    return render(request, "login.html")


def postsign(request):
    global signedIn
    email = request.POST.get('email')
    passw = request.POST.get("pass")
    try:
        user = authe.sign_in_with_email_and_password(email, passw)
        context = {
            'email': email
        }
    except:
        message = "Invalid Credentials. Please check your email ID and password."
        # return render(request, "login.html", {"msg": message})
        return HttpResponse("""
        <script type="text/javascript">
        alert('Invalid Credentials. Please try again.')
        window.location.href = "/signin"    
        </script>""")
        # return HttpResponse('<dialog open><a href="/signin/">Invalid Credentials. Please try again.</a></dialog>')
    # print(user)
    # print(user['idToken'])
    # session_id = user['idToken']
    # request.session['uid'] = str(session_id)
    signedIn = True
    return render(request, "selectroom.html", context)


def signUp(request):
    return render(request, "newaccount.html")


def postsignup(request):
    name = request.POST.get('name')
    email = request.POST.get('email')
    passw = request.POST.get('pass')
    try:
        user = authe.create_user_with_email_and_password(email, passw)
        uid = user['localId']
        data = {"name": name, "status": "1"}
        database.child("users").child(uid).child("details").set(data)
    except:
        message = "Unable to create account try again"
        return render(request, "signup.html", {"messg": message})

    return render(request, "login.html")


def roomselected(request):
    roomid = request.POST.get('roomid')
    responseURL = f"""<script type="text/javascript">
        window.location.href = "/chat/{roomid}"    
        </script>"""
    return HttpResponse(responseURL)


def forgotpassword(request):
    return render(request, "forgotpassword.html")


def logout(request):
    global signedIn
    signedIn = False
    auth.logout(request)
    return render(request, 'login.html')
