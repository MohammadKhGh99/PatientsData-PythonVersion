# started at 22.08.2021 at 17:17
from Constants import *
import os
import csv
# import pandas as pd
import sqlite3


class Patient:
    def __init__(self, fullname: str, id_number: str, gender: str, social: str, age: str, children: str, prayer: str,
                 health: str, work: str, companion: str, city: str, phone: str, description: str, diagnosis: str,
                 therapy: str):
        self.fullname = fullname
        self.fname, self.mname, self.lname = fullname.split(" ")
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
folder_name = "علاج"
csv_file = "patients.csv"
this_dir = os.path.join(os.path.abspath(os.curdir), folder_name)

# DRIVER = "SQL Server"
# SERVER_NAME = "MOHAMMADGH-PC\\SQLEXPRESS"
# DATABASE_NAME = "Patients"
# CONNECTION = f'DRIVER={DRIVER};' \
#              f'SERVER={SERVER_NAME};' \
#              f'DATABASE={DATABASE_NAME};' \
#              f'Trusted_Connection=yes;'


class Patients:
    # def __init__(self):
        # self.__sql_create_table = """
        # create table Patient(
        #     fullname nvarchar(45) unique,
        #     firstname nvarchar(15),
        #     middlename nvarchar(15),
        #     lastname nvarchar(15),
        #     id_number nvarchar(9) primary key,
        #     gender nvarchar(7),
        #     social nvarchar(15),
        #     age nvarchar(3),
        #     children nvarchar(3),
        #     prayer nvarchar(5),
        #     health nvarchar(30),
        #     work nvarchar(30),
        #     companion nvarchar(30),
        #     city nvarchar(20),
        #     phone nvarchar(12),
        #     description nvarchar(200),
        #     diagnosis nvarchar(100),
        #     therapy nvarchar(400)
        # )
        # """

        # if not os.path.exists(folder_name):
        #     os.mkdir(folder_name)
        #
        # self.patients = list()
        #
        # if not os.path.exists(os.path.join(this_dir, csv_file)):
        #     with open(os.path.join(this_dir, csv_file), 'w', encoding="utf-8-sig", newline='\n') as f:
        #         csv.writer(f).writerow(ALL_DATA)

        # self.connection_settings = 'driver={SQL Server};server=MOHAMMADGH-PC\\SQLEXPRESS;port=1433;uid=m7md;pwd=12345;'
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

        # pyodbc.connect(
        #     "DRIVER={SQL Server Native Client 11.0};SERVER=MOHAMMADGH-PC;DATABASE=Patients;UID=m7md;PWD=12345") as connection
        # with pymssql.connect(r"MOHAMMADGH-PC\SQLEXPRESS", "m7md", "12345", "Patients") as connection:
        # with pyodbc.connect(driver="{SQL Server Native Client 11.0}", host="MOHAMMADGH-PC", database="Patients",
        #                     user="m7md", password="12345") as connection:
        with sqlite3.connect("Patient.db") as connection:
            cursor = connection.cursor()
            # If we want to save the changes on the patient
            if after_search:
                first, middle, last = patient.fullname.split(" ")
                try:
                    cursor.execute(f"update Patient "
                                   f"set fullname = '{patient.fullname}',"
                                   f"firstname = '{first}', "
                                   f"middlename = '{middle}', "
                                   f"lastname = '{last}', "
                                   f"id_number = '{patient.id_number}', "
                                   f"gender = '{patient.gender}', "
                                   f"social = '{patient.social}', "
                                   f"age = '{patient.age}', "
                                   f"children = '{patient.children}', "
                                   f"prayer = '{patient.prayer}', "
                                   f"health = '{patient.health}', "
                                   f"work = '{patient.work}', "
                                   f"companion = '{patient.companion}', "
                                   f"city = '{patient.city}', "
                                   f"phone = '{patient.phone}', "
                                   f"description = '{patient.description}', "
                                   f"diagnosis = '{patient.diagnosis}', "
                                   f"therapy = '{patient.therapy}' "
                                   f"where fullname = '{patient.fullname}'")
                    connection.commit()
                except Exception as e:
                    connection.rollback()
                    raise e
            # If we want to save a new patient
            else:
                first, middle, last = patient.fullname.split(" ")
                try:
                    cursor.execute(
                        "INSERT INTO Patient "
                        "VALUES(?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?)",
                        (patient.fullname, first, middle, last, patient.id_number, patient.gender, patient.social,
                         patient.age, patient.children, patient.prayer, patient.health, patient.work, patient.companion,
                         patient.city, patient.phone, patient.description, patient.diagnosis, patient.therapy))
                    connection.commit()
                except Exception as e:
                    connection.rollback()
                    raise e

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
        try:
            # with pymssql.connect(r"MOHAMMADGH-PC\SQLEXPRESS", "m7md", "12345", "Patients") as connection:
            # with pyodbc.connect(driver="{SQL Server Native Client 11.0}", host="MOHAMMADGH-PC", database="Patients",
            #                     user="m7md", password="12345") as connection:
            with sqlite3.connect("Patient.db") as connection:
                cursor = connection.cursor()

                wanted_cols = 'fullname, id_number, gender, social, age, children,' \
                              ' prayer, health, work, companion, city, phone, description, diagnosis, therapy'

                try:
                    if option == ID_SEARCH:
                        cursor.execute(f"select {wanted_cols} from Patient where cast(id_number as varchar(9)) = '{id_number}'")
                    else:
                        if option == ALL_NAME:
                            cursor.execute(f"select {wanted_cols} from Patient where fullname = '{name}'")
                        elif option == FLNAME:
                            cur = name.split(" ")
                            cursor.execute(
                                f"select {wanted_cols} from Patient where firstname = '{cur[0]}' and lastname = '{cur[1]}'")
                        elif option == FMNAME:
                            cur = name.split(" ")
                            fmname = "firstname + ' ' + middlename"
                            cursor.execute(f"select {wanted_cols} from Patient where {fmname} = '{cur[0]} {cur[1]}'")
                        elif option == FNAME:
                            cursor.execute(f"select {wanted_cols} from Patient where firstname = '{name}'")
                        elif option == LNAME:
                            cursor.execute(f"select {wanted_cols} from Patient where lastname = '{name}'")
                    data = cursor.fetchall()

                    connection.commit()
                    for j in range(len(data)):
                        row = {ALL_DATA[i]: data[j][i] for i in range(len(ALL_DATA))}
                        to_return.append(row)
                except Exception as e:
                    connection.rollback()
                    raise e

            if len(to_return) == 0:
                if option == ID_SEARCH:
                    return -1, ID_NOT_EXISTS
                else:
                    return -1, NAME_NOT_EXISTS

            return to_return
        except Exception as e:
            raise e
            # tkinter.messagebox.showerror("Error", str(e))

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
        #                 wanted_name_split = name.split(" ")
        #                 if cur_name_split[0] == wanted_name_split[0] and cur_name_split[-1] == wanted_name_split[-1]:
        #                     to_return.append(row)
        #             # first middle name search
        #             elif option == FMNAME:
        #                 wanted_name_split = name.split(" ")
        #                 if cur_name_split[0] == wanted_name_split[0] and cur_name_split[1] == wanted_name_split[1]:
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

