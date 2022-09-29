# started at 22.08.2021 at 17:17
import csv
import os
from Constants import *


class Patient:
    def __init__(self, name: str, id_number: str, gender: str, social: str, age: str, children: str, prayer: str,
                 health: str, work: str, companion: str, city: str, phone: str, description: str, diagnosis: str,
                 therapy: str):
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


folder_name = "المعالجة"
csv_file = "patients.csv"
this_dir = os.path.join(os.path.abspath(os.curdir), folder_name)


class Patients:
    def __init__(self):

        if not os.path.exists(folder_name):
            os.mkdir(folder_name)

        self.patients = list()

        if not os.path.exists(os.path.join(this_dir, csv_file)):
            with open(os.path.join(this_dir, csv_file), 'w', encoding="utf-8-sig", newline='\n') as f:
                writer = csv.writer(f)
                first_row = [NAME[1:], ID[1:], GENDER[1:], SOCIAL_SIT[1:], AGE[1:], CHILDREN[1:],
                             PRAYER[1:], HEALTH[1:], WORK[1:], COMPANION[1:], CITY[1:], PHONE[1:], DESCRIPTION[1:],
                             DIAGNOSIS[1:], THERAPY[1:]]
                writer.writerow(first_row)

    def add_patient(self, patient: Patient):
        with open(os.path.join(this_dir, csv_file), 'a', encoding="utf-8-sig", newline='\n') as f:
            writer = csv.writer(f)
            self.patients.append(patient)
            new_row = [patient.name, patient.id_number, patient.gender, patient.social, patient.age, patient.children,
                       patient.prayer, patient.health, patient.work, patient.companion, patient.city, patient.phone,
                       patient.description, patient.diagnosis, patient.therapy]

            writer.writerow(new_row)

    def remove_patient(self, patient: Patient):
        self.patients.remove(patient)

    def search_patient(self, id_or_name: str = NAME_SEARCH, name: str = None, id_number: str = None):
        with open(os.path.join(this_dir, csv_file), 'r', encoding="utf-8-sig", newline='\n') as f:
            reader = csv.DictReader(f, ALL_DATA)
            to_return = []
            for row in reader:
                if row[NAME[1:]] == NAME[1:]:
                    continue
                if id_or_name == NAME_SEARCH:
                    if name is None:
                        return -1, NAME_SEARCH_ERR
                    elif row[NAME[1:]].startswith(name):
                        print(row[NAME[1:]])
                        to_return.append(row)
                elif id_or_name == ID_SEARCH:
                    if id_number is None:
                        return -1, ID_SEARCH_ERR
                    elif row[ID[1:]].startswith(id_number):
                        to_return.append(row)
        return (-1, SEARCH_NOT_EXISTS) if len(to_return) == 0 else to_return
