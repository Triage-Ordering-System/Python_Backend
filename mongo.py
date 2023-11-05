from pymongo import MongoClient
from patients import Patients


import datetime
from bson.objectid import ObjectId


def add_patient(patient):
    cluster = "mongodb+srv://DNSNate:2003@cluster0.gn4y1m0.mongodb.net/Patient_report?retryWrites=true&w=majority"

    client = MongoClient(cluster)
    db = client.Patient_report
    symptoms = []
    durations = []
    for s in patient.get_list_of_symptoms_durations():
        symptoms.append(s[0])
        durations.append(s[1])
    
    todo1 = {"name" : patient.get_name(), "age": patient.get_age(), "symptoms":symptoms, "durations": durations, "severity": patient.get_severity, "Past History": patient.past_history}
    todos = db.Patient
    result = todos.insert_one(tdo1)
    
    return


