from pydrive.drive import GoogleDrive
from pydrive.auth import GoogleAuth
import tkinter.messagebox

# For using listdir()
import os

# Below code does the authentication
# part of the code
gauth = GoogleAuth()

# Creates local webserver and auto
# handles authentication.
gauth.LocalWebserverAuth()
drive = GoogleDrive(gauth)

# replace the value of this variable
# with the absolute path of the directory
db_path = r"Patient.db"
xlsx_path = r"BackUp.xlsx"

def save_func():
    try:
        file_list = drive.ListFile(
            {'q': "'{}' in parents and trashed=false".format('1Jis1dontLnCDRjCYRy5isMPZZlHLG62J')}).GetList()
        for file in file_list:
            if file['title'] == xlsx_path:
                file.Delete()
            if file['title'] == db_path:
                file.Delete()
        # iterating thought all the files/folder
        # of the desired directory
        for x in [db_path, xlsx_path]:
            f = drive.CreateFile({'parents': [{'id': '1Jis1dontLnCDRjCYRy5isMPZZlHLG62J'}]})
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

def load_func():
    try:
        file_list = drive.ListFile(
            {'q': "'{}' in parents and trashed=false".format('1Jis1dontLnCDRjCYRy5isMPZZlHLG62J')}).GetList()
        for file in file_list:
            # print(file)
            file.GetContentFile(fr"BackUp\{file['title']}")
        tkinter.messagebox.showinfo("نجاح", "تم إستعادة الملفات بنجاح!")
    except Exception as e:
        tkinter.messagebox.showerror("فشل", "فشلت الإستعادة!")


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