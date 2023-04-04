from pydrive.drive import GoogleDrive
from pydrive.auth import GoogleAuth
import os

gauth = GoogleAuth()
gauth.LoadCredentialsFile("client_secrets_new.json")

if gauth.credentials is None:
    gauth.LocalWebserverAuth()
elif gauth.access_token_expired:
    gauth.Refresh()
else:
    gauth.Authorize()

gauth.SaveCredentialsFile("client_secrets_new.json")
drive = GoogleDrive(gauth)
path = r"./علاج"

def upload_file_to_drive():
    for x in os.listdir(path):
        file_list = drive.ListFile(
            {'q': "'1Jis1dontLnCDRjCYRy5isMPZZlHLG62J' in parents and trashed = False"}).GetList()
        try:
            for file1 in file_list:
                if file1['title'] == os.path.join(path, x):
                    file1.Delete()
        except:
            pass
        f = drive.CreateFile({'parents': [{'id': '1Jis1dontLnCDRjCYRy5isMPZZlHLG62J'}]})
        f.SetContentFile(os.path.join(path, x))
        f.Upload()
        f = None

def save_func():
    upload_file_to_drive()

def download_from_drive():
    file_list = drive.ListFile({'q': "1Jis1dontLnCDRjCYRy5isMPZZlHLG62J in parents and trashed = false”"})
    print(file_list)
    for file in file_list:
        print('title: % s, id: %s' %(file['title'], file['id']))

def load_func():
    download_from_drive()

#
# def save_func():
#     from pydrive.drive import GoogleDrive
#     from pydrive.auth import GoogleAuth
#     import os
#     gauth = GoogleAuth()
#     gauth.LoadCredentialsFile("mycreds.txt")
#     if gauth.credentials is None:
#         gauth.LocalWebserverAuth()
#     elif gauth.access_token_expired:
#         gauth.Refresh()
#     else:
#         gauth.Authorize()
#     gauth.SaveCredentialsFile("mycreds.txt")
#     drive = GoogleDrive(gauth)
#
#
#
#
#
#
#     import json
#     import requests
#
#     headers = {
#         "Authorization": "Bearer ya29.a0Ael9sCO03erMHH9Dz4ozOTnIA2ZbVrlFc4thEmjnMvd-efnh8wcwTEA6GpQJv5do96AHVDcMRusU_LQebcH52fVJgwvOEp-neZA1U68Qp6euiB1vBLQo_N2fLfx-8lqxAF3_YKjsb7QJ0T03i-LWcc-75Dv4aCgYKAYgSARESFQF4udJhyknNG7RBXqotuKs3nUTC2A0163"
#     }
#
#     para = {
#         "name": "patients.csv",
#         "parents": ["1Jis1dontLnCDRjCYRy5isMPZZlHLG62J"]
#     }
#
#     files = {
#         'data': ('metadata', json.dumps(para), 'application/json;charset=UTF-8'),
#         'file': open('./علاج/patients.csv', 'rb')
#     }
#
#     r = requests.post("https://www.googleapis.com/upload/drive/v3/files?uploadType=multipart",
#                       headers=headers,
#                       files=files
#                       )