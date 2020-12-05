from firebase import Firebase

apiKey = "AIzaSyBathSfk_1F36efi-zc5DlwKlHvrHG_ors"
authDomain = "nsgt-5ed5a.firebaseapp.com"
databaseURL =  "https://nsgt-5ed5a-default-rtdb.firebaseio.com"
projectId = "nsgt-5ed5a"
storageBucket = "nsgt-5ed5a.appspot.com"
messagingSenderId = "436519156337"
appId = "1:436519156337:web:e4f44e253153cc80bdb9d0"
measurementId = "G-CHDNNE6FVT"

config = {
  "apiKey": apiKey,
  "authDomain": "{}.firebaseapp.com".format(projectId),
  "databaseURL": databaseURL,
  "storageBucket": storageBucket,
  "serviceAccount": "path/to/serviceAccountCredentials.json"
}

firebase = Firebase(config)
db = firebase.database()


q1 = {"question": "What are the Target Sectors of APT 10?", "type": "reconnaissance", "ID": "q001"}
q2 = {"question": "Why target the U.S. Govt?", "type": "reconnaissance", "ID": "q002"}
q3 = {"question": "Attack Pattern", "type": "reconnaissance", "ID":"q003"}
q4 = {"question": "Known Malware", "type": "reconnaissance", "ID":"q004"}

db.child("questions").push(q1)
db.child("questions").push(q2)
db.child("questions").push(q3)
db.child("questions").push(q4)

a1 = {"answer": "construction and engineering firms", "ID":"a001", "parent":["q001"]}
a2 = {"answer": "aerospace firms", "ID":"a002", "parent":["q001"]}
a3 = {"answer": "United States Government agencies", "ID":"a003", "parent":["q001"], "DR":["q002"]}
a4 = {"answer": "telecom firms", "ID":"a004", "parent":["q001"]}

a5 = {"answer": "support Chinese national secuirty goals by acquiring military intelligence info", "ID":"a005", "parent":["q002"]}

a6 = {"answer": "Bugjuice - a backdoor that launches benign files that loads malicious DLL", "ID":"a006", "parent":["q004"]}
a7 = {"answer": "Snugride - backdoor that communicates with C2 server via HTTPS requests", "ID":"a007", "parent":["q004"]}

a8 = {"answer": "Spear phising attacks sent to target emails with malicious files attached to the email", "ID":"a008", "parent":["q003"], "DR" ["a006", "a007"]}
a9 = {"answer": "Register C2 domains that closely resemble legitimate Japanese organisations", "ID":"a009", "parent":["q003"]}

db.child("answers").push(a1)
db.child("answers").push(a2)
db.child("answers").push(a3)
db.child("answers").push(a4)
db.child("answers").push(a5)
db.child("answers").push(a6)
db.child("answers").push(a7)
db.child("answers").push(a8)
db.child("answers").push(a9)



'''
firebase = firebase.FirebaseApplication("https://nsgt-5ed5a-default-rtdb.firebaseio.com/", None)

data = {
    'name': "Test_User",
    'username': "test_user",
    'password': "testingtesting123",
    'email': "testing123@gmail.com",

}

result = firebase.post('/nsgt-5ed5a-default-rtdb/Users', data)
<<<<<<< HEAD

=======
'''
>>>>>>> a1e133dfff187896705a4e2a5215883fdcb6756d
