import sqlite3
import tkinter.messagebox

# create a database
connection = sqlite3.connect("Patient.db")

# create a table
sql_create_table = """
create table if not exists Patient(
    serial_year nvarchar(4),
    serial_num nvarchar(20),
    fullname nvarchar(45) primary key,
    firstname nvarchar(15),
    middlename nvarchar(15),
    lastname nvarchar(15),
    id_number nvarchar(9),
    gender nvarchar(7),
    social nvarchar(15),
    age nvarchar(3),
    children nvarchar(3),
    prayer nvarchar(5),
    health nvarchar(30),
    work nvarchar(30),
    companion nvarchar(30),
    city nvarchar(20),
    phone nvarchar(12),
    description nvarchar(200),
    diagnosis nvarchar(100),
    therapy nvarchar(400)
)
"""

arabic_sql_create_table = """
create table if not exists Patient(
    سنة_الرقم_التسلسلي nvarchar(4),
    الرقم_التسلسلي nvarchar(20),
    الإسم_الثلاثي nvarchar(45) primary key,
    الإسم_الشخصي nvarchar(15),
    إسم_الأب nvarchar(15),
    إسم_العائلة nvarchar(15),
    رقم_الهوية nvarchar(9),
    الجنس nvarchar(7),
    الحالة_الإجتماعية nvarchar(15),
    العمر nvarchar(3),
    أولاد nvarchar(3),
    صلاة nvarchar(5),
    صحة nvarchar(30),
    العمل nvarchar(30),
    المرافق nvarchar(30),
    البلد nvarchar(20),
    الهاتف nvarchar(12),
    وصف_الحالة nvarchar(200),
    التشخيص nvarchar(100),
    العلاج nvarchar(400)
)
"""




def create_table():
    cursor = connection.cursor()
    try:
        cursor.execute(arabic_sql_create_table)
        connection.commit()
    except Exception as e:
        print(str(e))
        tkinter.messagebox.showerror("خطأ", "خطأ في بناء الجدول!\n" + str(e))
        connection.rollback()

# if __name__ == "__main__":
#     create_table()
