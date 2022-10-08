# started at 22.08.2021 at 17:17
from tkinter import messagebox

import pymssql as pymssql

from Constants import *

try:
    import pyodbc
except Exception:
    import subprocess
    import os

    command_line = "pip install pyodbc"
    sub = subprocess.Popen(command_line, stderr=open(os.devnull, 'w'))
    sub.wait()


# import pyodbc


class Patient:
    def __init__(self, name: str, id_number: str, gender: str, social: str, age: str, children: str, prayer: str,
                 health: str, work: str, companion: str, city: str, phone: str, description: str, diagnosis: str,
                 therapy: str):
        self.fullname = name
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


# todo - csv file version
# folder_name = "therapy"
# csv_file = "patients.csv"
# this_dir = os.path.join(os.path.abspath(os.curdir), folder_name)

# DRIVER = "SQL Server"
# SERVER_NAME = "MOHAMMADGH-PC\\SQLEXPRESS"
# DATABASE_NAME = "Patients"
# CONNECTION = f'DRIVER={DRIVER};' \
#              f'SERVER={SERVER_NAME};' \
#              f'DATABASE={DATABASE_NAME};' \
#              f'Trusted_Connection=yes;'


class Patients:
    def __init__(self):

        # if not os.path.exists(folder_name):
        #     os.mkdir(folder_name)
        #
        # self.patients = list()
        #
        # if not os.path.exists(os.path.join(this_dir, csv_file)):
        #     with open(os.path.join(this_dir, csv_file), 'w', encoding="utf-8-sig", newline='\n') as f:
        #         csv.writer(f).writerow(ALL_DATA)

        self.connection_settings = 'driver={SQL Server};server=MOHAMMADGH-PC\\SQLEXPRESS;port=1433;uid=m7md;pwd=12345;'
        # 'DRIVER={SQL Server};' +
        # r'SERVER=MOHAMMADGH-PC\SQLEXPRESS;'
        # 'DATABASE=Patients;'
        # 'UID=mkhgh;'
        # 'PWD=1234;'
        # 'Trusted_Connection=yes;')
        # 'DRIVER={ODBC Driver 17 for SQL Server};' +
        # r'SERVER=.\MOHAMMADGH-PC\SQLEXPRESS;'
        # 'DATABASE=Patients;'
        # # 'Port=1433'
        # 'UID=mkhgh;'
        # 'PWD=1234;'
        # 'Trusted_Connection=yes;')

    def add_patient(self, patient: Patient, after_search):
        with pymssql.connect(r"MOHAMMADGH-PC\SQLEXPRESS", "m7md", "12345", "Patients") as connection:
            with connection.cursor() as cursor:
                # If we want to save the changes on the patient
                if after_search:
                    # Patient.fullname = '{patient.fullname}', "
                    #                                    f"
                    first, middle, last = patient.fullname.split(" ")
                    cursor.execute(f"update Patient "
                                   f"set Patient.firstname = '{first}', "
                                   f"Patient.middlename = '{middle}', "
                                   f"Patient.lastname = '{last}', "
                                   f"Patient.id_number = '{patient.id_number}', "
                                   f"Patient.gender = '{patient.gender}', "
                                   f"Patient.social = '{patient.social}', "
                                   f"Patient.age = '{patient.age}', "
                                   f"Patient.children = '{patient.children}', "
                                   f"Patient.prayer = '{patient.prayer}', "
                                   f"Patient.health = '{patient.health}', "
                                   f"Patient.work = '{patient.work}', "
                                   f"Patient.companion = '{patient.companion}', "
                                   f"Patient.city = '{patient.city}', "
                                   f"Patient.phone = '{patient.phone}', "
                                   f"Patient.description = '{patient.description}', "
                                   f"Patient.diagnosis = '{patient.diagnosis}', "
                                   f"Patient.therapy = '{patient.therapy}' "
                                   f"where cast(Patient.fullname as varchar(45)) = '{patient.fullname}'")
                    connection.commit()
                # If we want to save a new patient
                else:
                    print(patient.fullname)
                    first, middle, last = patient.fullname.split(" ")
                    cursor.execute(
                        "INSERT INTO Patient VALUES(%s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s)",
                        (patient.fullname, first, middle, last, patient.id_number, patient.gender,
                         patient.social, patient.age, patient.children, patient.prayer, patient.health,
                         patient.work, patient.companion, patient.city, patient.phone, patient.description,
                         patient.diagnosis, patient.therapy))
                    connection.commit()

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
        with pymssql.connect(r"MOHAMMADGH-PC\SQLEXPRESS", "m7md", "12345", "Patients") as connection:
            with connection.cursor() as cursor:

                wanted_cols = 'Patient.fullname, Patient.id_number, Patient.gender, Patient.social, Patient.age, ' \
                              'Patient.children, Patient.prayer, Patient.health, Patient.work, Patient.companion, ' \
                              'Patient.city, Patient.phone, Patient.description, Patient.diagnosis, Patient.therapy'

                if option == ID_SEARCH:
                    cursor.execute(f"select {wanted_cols} from Patient where cast(Patient.id_number as varchar(9)) = '{id_number}'")
                else:
                    if option == ALL_NAME:
                        cursor.execute(f"select {wanted_cols} from Patient where cast(Patient.fullname as varchar(45)) = '{name}'")
                    elif option == FLNAME:
                        cur = name.split(" ")
                        cursor.execute(
                            f"select {wanted_cols} from Patient where cast(Patient.firstname as varchar(15)) = '{cur[0]}' and cast(Patient.lastname as varchar(15)) = '{cur[1]}'")
                        # cursor.execute(
                        #     f"select * from Patient where cast(Patient.name as varchar(30)) like '{cur[0]} _% {cur[1]}'")
                    elif option == FMNAME:
                        cur = name.split(" ")
                        cursor.execute(
                            f"select {wanted_cols} from Patient where cast(Patient.firstname as varchar(15)) = '{cur[0]}' and cast(Patient.middlename as varchar(15)) = '{cur[1]}'")
                        # cursor.execute(
                        #     f"select * from Patient where cast(Patient.name as varchar(30)) like '{cur[0]} {cur[1]} _%'")
                    elif option == FNAME:
                        print(name)
                        cursor.execute(f"select {wanted_cols} from Patient where cast(Patient.firstname as varchar(15)) = '{name}'")
                        # cursor.execute(f"select * from Patient where cast(Patient.name as varchar(30)) like '^{name} _% _%'")
                    elif option == LNAME:
                        cursor.execute(f"select {wanted_cols} from Patient where cast(Patient.lastname as varchar(15)) = '{name}'")
                        # cursor.execute(f"select * from Patient where cast(Patient.name as varchar(30)) like '_% _% {name}'")

                data = cursor.fetchall()
                connection.commit()
                print(data)
                for j in range(len(data)):
                    # row = dict()
                    # for i in range(len(ALL_DATA)):
                    #     if i == 1 or i == 2 or i == 3:
                    #         continue

                    row = {ALL_DATA[i]: data[j][i] for i in range(len(ALL_DATA))}
                    to_return.append(row)

                # cursor.close()
                # connection.close()

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
