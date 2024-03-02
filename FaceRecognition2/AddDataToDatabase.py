import firebase_admin
from firebase_admin import credentials
from firebase_admin import db
cred = credentials.Certificate("ServiceAccountKey.json")
firebase_admin.initialize_app(cred,{
    "databaseURL":"https://facerecognition-6917b-default-rtdb.firebaseio.com/"
})

ref = db.reference('Students')

data = {
    "1":{
        "name": "Silvia Flores Maus",
        "Curso": "Administração",
        "ano-comeco": 2020,
        "Cadeiras": 3,
        "Matriculado":"Sim",
        "Ano": 2,
        "latest_attendence_time": "2023-12-09 17:00:00"
    },
    "2":{
        "name": "Felipe Flores Maus",
        "Curso": "Técnico em Informática",
        "ano-comeco": 2019,
        "Cadeiras": 5,
        "Matriculado":"Sim",
        "Ano": 2,
        "latest_attendence_time": "2023-12-09 17:00:00"
    },
    "3":{
        "name": "Leonardo Flores Maus",
        "Curso": "Análise e Desenvolvimento de Sistemas",
        "ano-comeco": 2019,
        "Cadeiras": 3,
        "Matriculado":"Sim",
        "Ano": 3,
        "latest_attendence_time": "2023-12-09 17:00:00"
    }
}

for key, value in data.items():
    ref.child(key).set(value)

