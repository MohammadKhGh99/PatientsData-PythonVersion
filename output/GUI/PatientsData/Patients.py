# started at 22.08.2021 at 17:17
import csv
import os
from Constants import *
import subprocess
import sys
import importlib.util
package = "pandas"

is_present = importlib.util.find_spec(package)
if is_present is None:
    print(package + " is not installed")
    subprocess.check_call([sys.executable, '-m', 'pip', 'install', package])
else:
    print("Successfull")
import pandas as pd


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


folder_name = "therapy"
csv_file = "patients.csv"
this_dir = os.path.join(os.path.abspath(os.curdir), folder_name)


class Patients:
    def __init__(self):

        if not os.path.exists(folder_name):
            os.mkdir(folder_name)

        self.patients = list()

        if not os.path.exists(os.path.join(this_dir, csv_file)):
            with open(os.path.join(this_dir, csv_file), 'w', encoding="utf-8-sig", newline='\n') as f:
                csv.writer(f).writerow(ALL_DATA)

    def add_patient(self, patient: Patient, after_search):
        with open(os.path.join(this_dir, csv_file), 'a', encoding="utf-8-sig", newline='\n') as f:
            new_row = [patient.name, patient.id_number, patient.gender, patient.social, patient.age, patient.children,
                       patient.prayer, patient.health, patient.work, patient.companion, patient.city, patient.phone,
                       patient.description, patient.diagnosis, patient.therapy]

            if after_search:
                df = pd.read_csv(os.path.join(this_dir, csv_file))
                idx = df[df[ALL_NAME] == patient.name].index[0]
                df.loc[idx, ALL_DATA] = new_row
                df.to_csv(os.path.join(this_dir, csv_file), index=False)
            else:
                writer = csv.writer(f)
                # self.patients.append(patient)
                writer.writerow(new_row)

    def remove_patient(self, patient: Patient):
        pass
        # self.patients.remove(patient)

    def search_patient(self, option: str = NAME_SEARCH, name: str = None, id_number: str = None):
        with open(os.path.join(this_dir, csv_file), 'r', encoding="utf-8-sig", newline='\n') as f:
            reader = csv.DictReader(f, ALL_DATA)
            to_return = []
            for row in reader:
                # id number search
                if option == ID_SEARCH:
                    if row[ID[1:]] == id_number:
                        to_return.append(row)
                else:
                    cur_name = row[ALL_NAME]
                    cur_name_split = cur_name.split(" ")

                    # first row (header)
                    if cur_name == ALL_NAME:
                        continue
                    # first middle last name search
                    if option == ALL_NAME:
                        if cur_name == name:
                            to_return.append(row)
                    # first last name search
                    elif option == FLNAME:
                        if cur_name_split[0] == name[0] and cur_name_split[-1] == name[-1]:
                            to_return.append(row)
                    # first middle name search
                    elif option == FMNAME:
                        if cur_name_split[0] == name[0] and cur_name_split[1] == name[1]:
                            to_return.append(row)
                    # first name search
                    elif option == FNAME:
                        if cur_name_split[0] == name:
                            to_return.append(row)
                    elif option == LNAME:
                        if cur_name_split[-1] == name:
                            to_return.append(row)

        if len(to_return) == 0:
            if option == ID_SEARCH:
                return -1, ID_NOT_EXISTS
            else:
                return -1, NAME_NOT_EXISTS

        return to_return
