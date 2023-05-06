# import sys
# import subprocess
#
# # implement pip as a subprocess:
# subprocess.check_call([sys.executable, '-m', 'pip', 'install', 'pydrive'])
#
from pydrive.drive import GoogleDrive
from pydrive.auth import GoogleAuth
import tkinter.messagebox
from convert_db_to import do_backup_xlsx

# For using listdir()
import os
import csv
import pandas as pd
import sqlite3
gauth = None
root_folder = None
drive = None

def authentication_func():
    # Below code does the authentication
    # part of the code
    global gauth, root_folder, drive
    gauth = GoogleAuth()

    # Creates local webserver and auto
    # handles authentication.
    gauth.LocalWebserverAuth()
    drive = GoogleDrive(gauth)

    # searching for the root folder to save to
    file_name = "المعالجة بالرقية الشرعية"
    query = f"title = '{file_name}'"
    root_list_check = drive.ListFile({'q': query}).GetList()

    # Check if the file exists
    if root_list_check:
        root_folder = root_list_check[0]
    else:
        body = {'title': "المعالجة بالرقية الشرعية", 'mimeType': "application/vnd.google-apps.folder"}
        root_folder = drive.CreateFile(body)
        root_folder.Upload()

# replace the value of this variable
# with the absolute path of the directory
db_path = r"Patient.db"
xlsx_path = r"BackUp.xlsx"

def save_func():
    do_backup_xlsx()
    try:
        if gauth is None:
            authentication_func()

        root_list = drive.ListFile({'q': f"'{root_folder['id']}' in parents and trashed=false"}).GetList()
        for file in root_list:
            if file['title'] == xlsx_path:
                file.Delete()
            if file['title'] == db_path:
                file.Delete()
        # iterating thought all the files/folder
        # of the desired directory

        for x in [db_path, xlsx_path]:
            f = drive.CreateFile({'parents': [{'id': f"{root_folder['id']}"}]})
            f.SetContentFile(x)
            f.Upload()

            # Due to a known bug in pydrive if we
            # don't empty the variable used to
            # upload the files to Google Drive the
            # file stays open in memory and causes a
            # memory leak, therefore preventing its
            # deletion
            f = None
        tkinter.messagebox.showinfo("نجاح", "تم الحفظ في جوجل درايف!")
    except Exception as e:
        tkinter.messagebox.showerror("فشل", "فشل الحفظ إلى جوجل درايف!")


# def _csv_to_db():
#     with open('csvfile.csv', 'r') as csvfile:
#         # create the object of csv.reader()
#         csv_file_reader = csv.reader(csvfile, delimiter=',')
#         # skip the header
#         next(csv_file_reader, None)
#
#         # 2. create database
#         with sqlite3.connect("Patient.db") as connection:
#             cursor = connection.cursor()
#
#             for row in csv_file_reader:
#                 # skip the first row
#
#                 row_str = ""
#                 fullname, (firstname, middlename, lastname) = row[0], row[0].split(" ")
#                 id_number, gender, social, age, children = row[1], row[2], row[3], row[4], row[5]
#                 prayer, health, work, companion, city = row[6], row[7], row[8], row[9], row[10]
#                 phone, description, diagnosis, therapy = row[11], row[12], row[13], row[14]
#
#                 # 5. create insert query
#                 insert_query = f"INSERT INTO Patient VALUES ('{fullname}','{firstname}','{middlename}','{lastname}'," \
#                               f"'{id_number}','{gender}','{social}','{age}','{children}','{prayer}','{health}'," \
#                               f"'{work}','{companion}','{city}','{description}','{diagnosis}','{therapy}')"
#                 # 6. Execute query
#                 cursor.execute(insert_query)
#             # # 7. commit changes
#             connection.commit()
#             # # 8. close connection
#             # connection.close()

def load_func():
    try:
        if gauth is None:
            authentication_func()

        root_list = drive.ListFile({'q': f"'{root_folder['id']}' in parents and trashed=false"}).GetList()
        for file in root_list:
            file.GetContentFile(fr"BackUp\{file['title']}")

        # with sqlite3.connect("Patient.db") as connection:
        #     cursor = connection.cursor()
        #     cursor.execute('DELETE FROM Patient')
        #     connection.commit()

            # wb = pd.read_excel('BackUp.xlsx', sheet_name='Sheet')
            # wb.to_sql(name='Patient', con=connection, if_exists='replace', index=True)
            # connection.commit()

        tkinter.messagebox.showinfo("نجاح", "تم إستعادة الملفات بنجاح!")
    except Exception as e:
        tkinter.messagebox.showerror("فشل", "فشلت الإستعادة!" + " " + str(e))


# from pydrive.drive import GoogleDrive
# from pydrive.auth import GoogleAuth
# import os
#
# gauth = GoogleAuth()
# gauth.LoadCredentialsFile("client_secrets_new.json")
#
# if gauth.credentials is None:
#     gauth.LocalWebserverAuth()
# elif gauth.access_token_expired:
#     gauth.Refresh()
# else:
#     gauth.Authorize()
#
# gauth.SaveCredentialsFile("client_secrets_new.json")
# drive = GoogleDrive(gauth)
# path = r"./علاج"
#
# def upload_file_to_drive():
#     for x in os.listdir(path):
#         file_list = drive.ListFile(
#             {'q': "'1Jis1dontLnCDRjCYRy5isMPZZlHLG62J' in parents and trashed = False"}).GetList()
#         try:
#             for file1 in file_list:
#                 if file1['title'] == os.path.join(path, x):
#                     file1.Delete()
#         except:
#             pass
#         f = drive.CreateFile({'parents': [{'id': '1Jis1dontLnCDRjCYRy5isMPZZlHLG62J'}]})
#         f.SetContentFile(os.path.join(path, x))
#         f.Upload()
#         f = None
#
# def save_func():
#     upload_file_to_drive()
#
# def download_from_drive():
#     file_list = drive.ListFile({'q': "1Jis1dontLnCDRjCYRy5isMPZZlHLG62J in parents and trashed = false”"})
#     print(file_list)
#     for file in file_list:
#         print('title: % s, id: %s' %(file['title'], file['id']))
#
# def load_func():
#     download_from_drive()
#
# #
# # def save_func():
# #     from pydrive.drive import GoogleDrive
# #     from pydrive.auth import GoogleAuth
# #     import os
# #     gauth = GoogleAuth()
# #     gauth.LoadCredentialsFile("mycreds.txt")
# #     if gauth.credentials is None:
# #         gauth.LocalWebserverAuth()
# #     elif gauth.access_token_expired:
# #         gauth.Refresh()
# #     else:
# #         gauth.Authorize()
# #     gauth.SaveCredentialsFile("mycreds.txt")
# #     drive = GoogleDrive(gauth)
# #
# #
# #
# #
# #
# #
# #     import json
# #     import requests
# #
# #     headers = {
# #         "Authorization": "Bearer ya29.a0Ael9sCO03erMHH9Dz4ozOTnIA2ZbVrlFc4thEmjnMvd-efnh8wcwTEA6GpQJv5do96AHVDcMRusU_LQebcH52fVJgwvOEp-neZA1U68Qp6euiB1vBLQo_N2fLfx-8lqxAF3_YKjsb7QJ0T03i-LWcc-75Dv4aCgYKAYgSARESFQF4udJhyknNG7RBXqotuKs3nUTC2A0163"
# #     }
# #
# #     para = {
# #         "name": "patients.csv",
# #         "parents": ["1Jis1dontLnCDRjCYRy5isMPZZlHLG62J"]
# #     }
# #
# #     files = {
# #         'data': ('metadata', json.dumps(para), 'application/json;charset=UTF-8'),
# #         'file': open('./علاج/patients.csv', 'rb')
# #     }
# #
# #     r = requests.post("https://www.googleapis.com/upload/drive/v3/files?uploadType=multipart",
# #                       headers=headers,
# #                       files=files
# #                       )