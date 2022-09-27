# started at 22.08.2021 at 17:17
import csv
import os


class Patient:
    def __init__(self, name, id_number, gender, social, age, children, prayer, health, work, companion, city, phone,
                 description, diagnosis, therapy):
        self.name = name
        self.id_number = id_number
        self.gender = gender
        self.social = social
        self.age = age
        self.children = children
        self.prayer = prayer
        self.health = health
        self.work = work
        self.companion = companion
        self.city = city
        self.phone = phone
        self.description = description
        self.diagnosis = diagnosis
        self.therapy = therapy
        # self.come_dates = come_dates
        # self.explanation = explanation


folder_name = "المعالجة"
csv_file = "patients.csv"
NAME = "Name"
PID = "id"
AGE = "Age"
COME = "Come_Cause"
ABSENT = "Absent_Cause"
FINISH = "Finish_Cause"
DATES = "Dates"
SYMPTOMS = "Symptoms"


class Patients:
    def __init__(self):
        this_dir = os.path.join(os.path.abspath(os.curdir), folder_name)
        if not os.path.exists(folder_name):
            os.mkdir(folder_name)
        if not os.path.exists(csv_file):
            self.csv_file = open(os.path.join(this_dir, csv_file), 'w')
        else:
            self.csv_file = open(csv_file, 'r+')

        self.patients = list()

    def add_patient(self, patient: Patient):
        self.patients.append(patient)

    def remove_patient(self, patient: Patient):
        self.patients.remove(patient)

    def search_patient(self, name: str):
        reader = csv.DictReader(self.csv_file)
        for line in reader:
            # name = line[NAME] == patient.get_name()
            # pid = line[PID] == patient.get_pid()
            # age = line[AGE] == patient.get_age()
            # come_cause = line[COME] == patient.get_come_cause()
            # absent_cause = line[ABSENT] == patient.get_absent_cause()
            # finish_cause = line[FINISH] == patient.get_finish_cause()
            # dates = line[DATES] == patient.get_dates()
            # symptoms = line[SYMPTOMS] == patient.get_symptoms()
            # if name and pid and age and come_cause and absent_cause and finish_cause and dates and symptoms:
            #     return
            if line[NAME] == name:
                return Patient(name, line[PID], line[AGE], line[COME], line[ABSENT], line[FINISH], line[DATES], line[SYMPTOMS])
        return None

