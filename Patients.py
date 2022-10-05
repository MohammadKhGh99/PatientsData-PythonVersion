# started at 22.08.2021 at 17:17
import csv
import os
import sys

import pyodbc
from Constants import *

try:
    import pandas as pd
except ImportError:
    import subprocess

    command_line = "pip install pandas"
    sub = subprocess.Popen(command_line, stderr=open(os.devnull, 'w'))
    sub.wait()


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

        self.connection_settings = (
                'DRIVER={SQL Server};' +
                r'SERVER=MOHAMMADGH-PC\SQLEXPRESS;'
                'DATABASE=Patients;'
                'UID=mkhgh;'
                'PWD=1234;'
                'Trusted_Connection=yes;')

    def add_patient(self, patient: Patient, after_search):
        connection = pyodbc.connect(self.connection_settings)
        cursor = connection.cursor()

        if after_search:
            cursor.execute("update Patient "
                           "set Patient.name = ?, Patient.id_number = ?, Patient.gender = ?, Patient.social = ?, "
                           "Patient.age = ?, Patient.children = ?, Patient.prayer = ?, Patient.health = ?, "
                           "Patient.work = ?, Patient.companion = ?, Patient.city = ?, Patient.phone = ?, "
                           "Patient.description = ?, Patient.diagnosis = ?, Patient.therapy = ? where Patient.name = ?",
                           patient.name, patient.id_number, patient.gender, patient.social, patient.age,
                           patient.children, patient.prayer, patient.health, patient.work, patient.companion,
                           patient.city, patient.prayer, patient.description, patient.diagnosis, patient.therapy,
                           patient.name)
            connection.commit()
        else:
            cursor.execute("INSERT INTO Patient VALUES(?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?);",
                           (patient.name, patient.id_number, patient.gender, patient.social, patient.age,
                            patient.children,
                            patient.prayer, patient.health, patient.work, patient.companion, patient.city,
                            patient.phone,
                            patient.description, patient.diagnosis, patient.therapy))
            connection.commit()
        cursor.close()
        connection.close()
        # todo - csv file version
        # with open(os.path.join(this_dir, csv_file), 'a', encoding="utf-8-sig", newline='\n') as f:
        #     new_row = [patient.name, patient.id_number, patient.gender, patient.social, patient.age, patient.children,
        #                patient.prayer, patient.health, patient.work, patient.companion, patient.city, patient.phone,
        #                patient.description, patient.diagnosis, patient.therapy]
        #
        #     if after_search:
        #         df = pd.read_csv(os.path.join(this_dir, csv_file))
        #         idx = df[df[ALL_NAME] == patient.name].index[0]
        #         df.loc[idx, ALL_DATA] = new_row
        #         df.to_csv(os.path.join(this_dir, csv_file), index=False)
        #     else:
        #         writer = csv.writer(f)
        #         # self.patients.append(patient)
        #         writer.writerow(new_row)

    def remove_patient(self, patient: Patient):
        pass

    def search_patient(self, option: str = NAME_SEARCH, name: str = None, id_number: str = None):
        to_return = []
        connection = pyodbc.connect(self.connection_settings)
        cursor = connection.cursor()
        # try:
        if option == ID_SEARCH:
            cursor.execute("select * from Patient where Patient.id_number = ?", id_number)
        else:
            if option == ALL_NAME:
                cursor.execute("select * from Patient where Patient.name = ?", name)
            elif option == FLNAME:
                cur = name.split(" ")
                cursor.execute("select * from Patient where Patient.name like ?", f"{cur[0]} %{cur[1]}")
            elif option == FMNAME:
                cur = name.split(" ")
                cursor.execute("select * from Patient where Patient.name like ?", f"{cur[0]} {cur[1]}%")
            elif option == FNAME:
                cursor.execute("select * from Patient where Patient.name like ?", f"{name}%")
            elif option == LNAME:
                cursor.execute("select * from Patient where Patient.name like ?", f"%{name}")

        data = cursor.fetchall()
        for j in range(len(data)):
            row = {ALL_DATA[i]: data[j][i] for i in range(len(ALL_DATA))}
            to_return.append(row)

        connection.commit()
        cursor.close()
        connection.close()

        if len(to_return) == 0:
            if option == ID_SEARCH:
                return -1, ID_NOT_EXISTS
            else:
                return -1, NAME_NOT_EXISTS

        return to_return

        # todo - csv file version
        # with open(os.path.join(this_dir, csv_file), 'r', encoding="utf-8-sig", newline='\n') as f:
        #     reader = csv.DictReader(f, ALL_DATA)
        #     to_return = []
        #     for row in reader:
        #         # id number search
        #         if option == ID_SEARCH:
        #             if row[ID[1:]] == id_number:
        #                 to_return.append(row)
        #         else:
        #             cur_name = row[ALL_NAME]
        #             cur_name_split = cur_name.split(" ")
        #
        #             # first row (header)
        #             if cur_name == ALL_NAME:
        #                 continue
        #             # first middle last name search
        #             if option == ALL_NAME:
        #                 if cur_name == name:
        #                     to_return.append(row)
        #             # first last name search
        #             elif option == FLNAME:
        #                 if cur_name_split[0] == name[0] and cur_name_split[-1] == name[-1]:
        #                     to_return.append(row)
        #             # first middle name search
        #             elif option == FMNAME:
        #                 if cur_name_split[0] == name[0] and cur_name_split[1] == name[1]:
        #                     to_return.append(row)
        #             # first name search
        #             elif option == FNAME:
        #                 if cur_name_split[0] == name:
        #                     to_return.append(row)
        #             elif option == LNAME:
        #                 if cur_name_split[-1] == name:
        #                     to_return.append(row)
        #
        # if len(to_return) == 0:
        #     if option == ID_SEARCH:
        #         return -1, ID_NOT_EXISTS
        #     else:
        #         return -1, NAME_NOT_EXISTS
        #
        # return to_return
