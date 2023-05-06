import sqlite3
import tkinter.messagebox
import pandas as pd


def do_backup_xlsx(msg=False):
    try:
        with sqlite3.connect("Patient.db") as connection:
            df = pd.read_sql("SELECT * from Patient", connection)
            df.to_excel("BackUp.xlsx")

        if msg:
            tkinter.messagebox.showinfo("نجاح", "تم التحويل بنجاح!")

    except Exception as e:
        tkinter.messagebox.showerror("فشل", "فشل\n" + str(e))
