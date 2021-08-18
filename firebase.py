import pyrebase
from gabung import gabung

firebaseConfig = {
    "apiKey": "AIzaSyAeLzgjzy_LV_bpDck064AEUZ2vRf91ka4",
    "authDomain": "final-project-9e2cc.firebaseapp.com",
    "databaseURL": "https://final-project-9e2cc-default-rtdb.asia-southeast1.firebasedatabase.app",
    "projectId": "final-project-9e2cc",
    "storageBucket": "final-project-9e2cc.appspot.com",
    "messagingSenderId": "816416542969",
    "appId": "1:816416542969:web:6275bacdd4d2aa5e54d228",
    "measurementId": "G-EC494EPBMD"
}

firebase = pyrebase.initialize_app(firebaseConfig)
db = firebase.database()

def stream_handler(message):
    print(message["event"]) # put
    print(message["path"]) # /-K7yGTTEp7O549EzTYtI
    print(message["data"]) # {'title': 'Pyrebase', "body": "etc..."}
    print("====")
    if message["data"] != None :
        a =  gabung(message["data"]["berita"])
        a["link"] = message["data"]["berita"]
        db.child("berita").push(a)
        db.child("link").remove()

my_stream = db.child("link").stream(stream_handler)
