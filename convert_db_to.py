# (A) INIT
# (A1) LOAD MODULES
import sqlite3, os, openpyxl
import tkinter.messagebox
from sqlite3 import Error
from Constants import ALL_DATA

# (A2) SETTINGS
DBFILE = "Patient.db"

# (B) OPEN DATABASE & CREATE EXCEL
conn = sqlite3.connect(DBFILE)
cursor = conn.cursor()
book = openpyxl.Workbook()
sheet = book.active

# (C) EXPORT DATA TO EXCEL
cursor.execute("SELECT * FROM Patient")
results = cursor.fetchall()

def do_backup_xlsx():
    try:
        j = 1
        for c in ALL_DATA:
            cell = sheet.cell(row=1, column=j)
            cell.value = c
            j += 1

        i = 1
        for row in results:
            i += 1
            j = 1
            for ind, col in enumerate(row):
                if ind in [1, 2 ,3]:
                    continue
                cell = sheet.cell(row=i, column=j)
                cell.value = col
                j += 1

        # (D) SAVE EXCEL FILE & CLOSE DB
        book.save("BackUp.xlsx")
        conn.close()
    except Exception as e:
        tkinter.messagebox.showerror("فشل", "فشل\n" + str(e))