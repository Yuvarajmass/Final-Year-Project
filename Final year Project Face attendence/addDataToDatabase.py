import firebase_admin
from firebase_admin import credentials
from firebase_admin import db

cred = credentials.Certificate("ServiceAccountKey.json")
firebase_admin.initialize_app(cred, {

    'databaseURL': "https://faceattendancerealtime-c3cc2-default-rtdb.firebaseio.com/"
})

ref = db.reference('Students')

data = {
    "638133":
        {
            "name": "Yuvaraj",
            "major": "computer science",
            "starting_year": 2024,  # Corrected starting_year value
            "total_attendance": 22,
            "standing": "G",
            "year": 2,
            "last_attendance_time": '2024-02-08 02:02:54',
        },
    "638134":
        {  # Corrected syntax to add a new student
            "name": "John Doe",
            "major": "biology",
            "starting_year": 2023,  # Example starting year
            "total_attendance": 22,  # Example attendance value
            "standing": "G",  # Example standing value
            "year": 1,  # Example year value
            "last_attendance_time": '2024-02-10 10:10:10',  # Example last attendance time
    }
}

for key, value in data.items():
    ref.child(key).set(value)  # Set the value for each child key
