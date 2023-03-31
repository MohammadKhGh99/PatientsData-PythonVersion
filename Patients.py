# started at 22.08.2021 at 17:17
from Constants import *
# import tkinter.messagebox
# import pymssql
# import pyodbc
import os.path
import csv
import pandas as pd


class Patient:
    def __init__(self, name: str, id_number: str, gender: str, social: str, age: str, children: str, prayer: str,
                 health: str, work: str, companion: str, city: str, phone: str, description: str, diagnosis: str,
                 therapy_text: str, therapy_num: str, therapy_date: str):
        self.name = name
        self.fname, self.mname, self.lname = name.split(" ")
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
        self.therapy_text = therapy_text
        self.therapy_date = therapy_date
        self.therapy_num = therapy_num
        # self.therapys[therapy_num] = (therapy_date, therapy_text)


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
    def __init__(self):

        if not os.path.exists(folder_name):
            os.mkdir(folder_name)

        self.patients = list()

        if not os.path.exists(os.path.join(this_dir, csv_file)):
            with open(os.path.join(this_dir, csv_file), 'w', encoding="utf-8-sig", newline='\n') as f:
                csv.writer(f).writerow(ALL_DATA)

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
        # mydb = mysql.connector.connect(
        #     host="MOHAMMADGH-PC",
        #     instance="SQL EXPRESS",
        #     user="m7md",
        #     password="12345",
        #     port="1433"
        # )

        # pyodbc.connect(
            # "DRIVER={SQL Server Native Client 11.0};SERVER=MOHAMMADGH-PC;DATABASE=Patients;UID=m7md;PWD=12345") as connection
        # with pymssql.connect(r"MOHAMMADGH-PC\SQLEXPRESS", "m7md", "12345", "Patients") as connection:
        # with pyodbc.connect(driver="{SQL Server Native Client 11.0}", host="MOHAMMADGH-PC", database="Patients",
        #                     user="m7md", password="12345") as connection:
        #     with connection.cursor() as cursor:
        #         # If we want to save the changes on the patient
        #         if after_search:
        #             first, middle, last = patient.fullname.split(" ")
        #             cursor.execute(f"update Patient "
        #                            f"set firstname = N'{first}', "
        #                            f"middlename = N'{middle}', "
        #                            f"lastname = N'{last}', "
        #                            f"id_number = N'{patient.id_number}', "
        #                            f"gender = N'{patient.gender}', "
        #                            f"social = N'{patient.social}', "
        #                            f"age = N'{patient.age}', "
        #                            f"children = N'{patient.children}', "
        #                            f"prayer = N'{patient.prayer}', "
        #                            f"health = N'{patient.health}', "
        #                            f"work = N'{patient.work}', "
        #                            f"companion = N'{patient.companion}', "
        #                            f"city = N'{patient.city}', "
        #                            f"phone = N'{patient.phone}', "
        #                            f"description = N'{patient.description}', "
        #                            f"diagnosis = N'{patient.diagnosis}', "
        #                            f"therapy = N'{patient.therapy}' "
        #                            f"where fullname = N'{patient.fullname}'")
        #             connection.commit()
        #         # If we want to save a new patient
        #         else:
        #             first, middle, last = patient.fullname.split(" ")
        #             cursor.execute(
        #                 "INSERT INTO Patient "
        #                 "VALUES(%s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s)",
        #                 (patient.fullname, first, middle, last, patient.id_number, patient.gender, patient.social,
        #                  patient.age, patient.children, patient.prayer, patient.health, patient.work, patient.companion,
        #                  patient.city, patient.phone, patient.description, patient.diagnosis, patient.therapy))
        #             connection.commit()

        # todo - csv file version
        with open(os.path.join(this_dir, csv_file), 'a', encoding="utf-8-sig", newline='') as f:
            new_row = [patient.name, patient.id_number, patient.gender, patient.social, patient.age, patient.children,
                       patient.prayer, patient.health, patient.work, patient.companion, patient.city, patient.phone,
                       patient.description, patient.diagnosis]#, patient.therapy_text]


            if after_search:
                df = pd.read_csv(os.path.join(this_dir, csv_file))
                idx = df[df[ALL_NAME] == patient.name].index[0]
                df.loc[idx, ALL_DATA] = new_row
                df.to_csv(os.path.join(this_dir, csv_file), encoding="utf-8-sig", index=False)
            else:
                new_row_dict = {ALL_DATA[i]:new_row[i] for i in range(len(new_row))}
                new_row_dict[ALL_DATA[14 + THERAPYS_NUMS.index(patient.therapy_num)]] = patient.therapy_date + ',' + patient.therapy_text

                writer = csv.DictWriter(f, fieldnames=ALL_DATA)
                # writer = csv.writer(f)
                # self.patients.append(patient)
                writer.writerow(new_row_dict)

            # if patient.therapy_text != "":
            #     therapy_dict = {ALL_DATA[14 + THERAPYS_NUMS.index(patient.therapy_num)]:patient.therapy_date + ',' + patient.therapy_text}


    def remove_patient(self, patient: Patient):
        pass

    def search_patient(self, option: str = NAME_SEARCH, name: str = None, id_number: str = None):
        # to_return = []
        # try:
        #     # with pymssql.connect(r"MOHAMMADGH-PC\SQLEXPRESS", "m7md", "12345", "Patients") as connection:
        #     with pyodbc.connect(driver="{SQL Server Native Client 11.0}", host="MOHAMMADGH-PC", database="Patients",
        #                         user="m7md", password="12345") as connection:
        #         with connection.cursor() as cursor:
        #
        #             wanted_cols = 'fullname, id_number, gender, social, age, children, prayer, health, work, ' \
        #                           'companion, city, phone, description, diagnosis, therapy'
        #
        #             if option == ID_SEARCH:
        #                 cursor.execute(f"select {wanted_cols} from Patient where cast(id_number as varchar(9)) = '{id_number}'")
        #             else:
        #                 if option == ALL_NAME:
        #                     cursor.execute(f"select {wanted_cols} from Patient where fullname = N'{name}'")
        #                 elif option == FLNAME:
        #                     cur = name.split(" ")
        #                     cursor.execute(
        #                         f"select {wanted_cols} from Patient where firstname = N'{cur[0]}' and lastname = N'{cur[1]}'")
        #                 elif option == FMNAME:
        #                     cur = name.split(" ")
        #                     fmname = "firstname + ' ' + middlename"
        #                     cursor.execute(f"select {wanted_cols} from Patient where {fmname} = N'{cur[0]} {cur[1]}'")
        #                     # cursor.execute(
        #                 elif option == FNAME:
        #                     cursor.execute(f"select {wanted_cols} from Patient where firstname = N'{name}'")
        #                 elif option == LNAME:
        #                     cursor.execute(f"select {wanted_cols} from Patient where lastname = N'{name}'")
        #
        #             data = cursor.fetchall()
        #             connection.commit()
        #             for j in range(len(data)):
        #                 row = {ALL_DATA[i]: data[j][i] for i in range(len(ALL_DATA))}
        #                 to_return.append(row)
        #
        #     if len(to_return) == 0:
        #         if option == ID_SEARCH:
        #             return -1, ID_NOT_EXISTS
        #         else:
        #             return -1, NAME_NOT_EXISTS
        #
        #     return to_return
        # except Exception as e:
        #     raise e
            # tkinter.messagebox.showerror("Error", str(e))

        # todo - csv file version
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
