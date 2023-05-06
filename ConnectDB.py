import sqlite3

# create a database
connection = sqlite3.connect("Patient.db")

# create a table
sql_create_table = """
create table Patient(
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

cursor = connection.cursor()
try:
    cursor.execute(sql_create_table)
    connection.commit()
except Exception as e:
    connection.rollback()

