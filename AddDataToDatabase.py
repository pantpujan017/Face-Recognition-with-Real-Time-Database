import firebase_admin
from firebase_admin import credentials
from firebase_admin import db
import os



cred = credentials.Certificate("serviceAccountKey.json")
firebase_admin.initialize_app(cred,{'databaseURL':"https://faceattendancerealtime-9fe36-default-rtdb.firebaseio.com/"
})


ref=db.reference('Students')

data={
    "2257":
        {
        "name":"Elon Musk",
        "major":"Computer Science",
        "starting_year":2022,
        "total_attendance":15,
        "standing":"G",
        "year":3,
        "last_attendance_time":"2024-7-3 00:54:34"
},
"3245":
        {
        "name":"Steve Jobs",
        "major":"Management",
        "starting_year":2022,
        "total_attendance":22,
        "standing":"VG",
        "year":2,
        "last_attendance_time":"2024-6-22 00:12:34"
},
"6752":
        {
        "name":"Bill Gates",
        "major":"Management",
        "starting_year":2022,
        "total_attendance":3,
        "standing":"NG",
        "year":2,
        "last_attendance_time":"2023-7-3 02:34:34"
}


}

for key,value in data.items():
    ref.child(key).set(value)