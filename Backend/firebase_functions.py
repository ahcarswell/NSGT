from firebase import firebase

firebase = firebase.FirebaseApplication("https://nsgt-5ed5a-default-rtdb.firebaseio.com/", None)

data = {
    'name': "Test_User",
    'username': "test_user",
    'password': "testingtesting123",
    'email': "testing123@gmail.com",

}

result = firebase.post('/nsgt-5ed5a-default-rtdb/Users', data)
