create table Patient(
	name varchar(30) primary key,
	id_number varchar(9),
	gender varchar(7),
	social varchar(15),
	age int,
	children int,
	prayer bit,
	health varchar(20),
	work varchar(20),
	companion varchar(30),
	city varchar(20),
	phone varchar(12),
	description varchar(200),
	diagnosis varchar(100),
	therapy varchar(400)
)