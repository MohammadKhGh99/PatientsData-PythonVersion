# started at 22.08.2021 at 17:17
import tkinter.messagebox

import GUI
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


class Patients:
    def add_patient(self, patient: Patient, after_search):
        with sqlite3.connect("Patient.db") as connection:
            cursor = connection.cursor()
            # If we want to save the changes on the patient
            if after_search:
                first, middle, last = patient.fullname.split(" ")
                try:
                    cursor.execute(f"update Patient "
                                   f"set fullname = '{patient.fullname}',"
                                   f"firstname = '{first}', middlename = '{middle}', lastname = '{last}', "
                                   f"id_number = '{patient.id_number}', gender = '{patient.gender}', "
                                   f"social = '{patient.social}', age = '{patient.age}', "
                                   f"children = '{patient.children}', prayer = '{patient.prayer}', "
                                   f"health = '{patient.health}', work = '{patient.work}', "
                                   f"companion = '{patient.companion}', city = '{patient.city}', "
                                   f"phone = '{patient.phone}', description = '{patient.description}', "
                                   f"diagnosis = '{patient.diagnosis}', therapy = '{patient.therapy}' "
                                   f"where fullname = '{patient.fullname}'")
                    connection.commit()
                    tkinter.messagebox.showinfo("! تم الحفظ", "! تم الحفظ")
                except Exception as e:
                    connection.rollback()
                    tkinter.messagebox.showerror("خطأ!", "خطأ!\n" + str(e))
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
                    tkinter.messagebox.showinfo("! تم الحفظ", "! تم الحفظ")
                except Exception as e:
                    connection.rollback()
                    tkinter.messagebox.showerror("خطأ!", "خطأ!\n" + str(e))
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
            with sqlite3.connect("Patient.db") as connection:
                cursor = connection.cursor()

                wanted_cols = 'fullname, id_number, gender, social, age, children,' \
                              ' prayer, health, work, companion, city, phone, description, diagnosis, therapy'

                try:
                    # taking all the patients
                    if (name is None or name.strip() == "") and (id_number is None or id_number.strip() == ""):
                        cursor.execute(f"select {wanted_cols} from Patient")
                        data = cursor.fetchall()
                        # print(data)
                        connection.commit()
                        for j in range(len(data)):
                            row = {ALL_DATA[i]: data[j][i] for i in range(len(ALL_DATA))}
                            to_return.append(row)
                    else:
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
                        # print(data)
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
            tkinter.messagebox.showerror("خطأ!", "خطأ!\n" + str(e))
            raise e

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

