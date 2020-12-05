from firebase import Firebase

apiKey: "AIzaSyBathSfk_1F36efi-zc5DlwKlHvrHG_ors",
    authDomain: "nsgt-5ed5a.firebaseapp.com",
    databaseURL: "https://nsgt-5ed5a-default-rtdb.firebaseio.com",
    projectId: "nsgt-5ed5a",
    storageBucket: "nsgt-5ed5a.appspot.com",
    messagingSenderId: "436519156337",
    appId: "1:436519156337:web:e4f44e253153cc80bdb9d0",
    measurementId: "G-CHDNNE6FVT" 

config = {
  "apiKey": "apiKey",
  "authDomain": "projectId.firebaseapp.com",
  "databaseURL": "https://databaseName.firebaseio.com",
  "storageBucket": "projectId.appspot.com",
  "serviceAccount": "path/to/serviceAccountCredentials.json"
}

firebase = Firebase(config)
db = firebase.database()


q1 = {"question": "What are the Target Sectors of APT 10?", "type": "reconnaissance"}
q2 = {"question": "Why target the U.S. Govt?", "type": "reconnaissance"}
q3 = {"question": "Attack Pattern", "type": "reconnaissance"}
q4 = {"question": "Software Deployment Tools"}

db.child("questions").push(q1)
db.child("questions").push(q2)
db.child("questions").push(q3)
db.child("questions").push(q4)


'''
firebase = firebase.FirebaseApplication("https://nsgt-5ed5a-default-rtdb.firebaseio.com/", None)

data = {
    'name': "Test_User",
    'username': "test_user",
    'password': "testingtesting123",
    'email': "testing123@gmail.com",

}

result = firebase.post('/nsgt-5ed5a-default-rtdb/Users', data)
'''
