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

select * from Patient
select cast(Patient.firstname as varchar(15)) from Patient where Patient.fullname = N'معمر خالد غنايم'
delete from Patient where Patient.fullname = N'معمر خالد غنايم'

select fullname, id_number, gender, social, age, children, prayer, health, work, companion, city, phone, description, diagnosis, therapy 
from Patient where cast(firstname as varchar(15)) = N'محمد'

drop table Patient


select @@SERVERNAME





update Patient set Patient.health = N'حرقة' where Patient.fullname = N'محمد خالد غنايم'