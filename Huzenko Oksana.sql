--Creating tables

create table hosts (
	id_host serial primary key,
	name_host varchar(50)
);

create table rooms (
	id_room serial primary key,
	id_host int references hosts(id_host),
	address varchar(50),
	capacity int,
	num_bedroom int,
	price_per_day float
);

create table guests (
	id_guest serial primary key,
	name_guest varchar(50)
);

create table reservations (
	id_visit serial primary key,
	start_date date,
	end_date date,
	id_room int references rooms(id_room),
	id_guest int references guests(id_guest)
);


--Writing rows

insert into hosts(name_host)
values ('John Smith')

insert into hosts(name_host)
values 
('Robert Brown'),
('David Grey')

insert into guests(name_guest)
values 
('Maria Pickwell'),
('Liz Rodriguez'),
('Ann Martinez')

insert into rooms(id_host, address, capacity, num_bedroom, price_per_day)
values 
(1, 'London, 1st street', 2, 2, 100.0),
(2, 'Amsterdam', 2, 1, 150.0),
(1, 'London, 2nd street', 2, 2, 120.0)

insert into reservations(start_date, end_date, id_room, id_guest)
values 
('2023-01-01', '2023-01-03', 1, 2),
('2023-01-04', '2023-01-06', 3, 2),
('2023-01-09', '2023-01-11', 2, 1)
	

--Analytical queries

select name_guest
from guests g 
join reservations r on r.id_guest=g.id_guest 
join rooms on r.id_room=rooms.id_room 
where id_host=2 and start_date>='2023-01-01' and start_date<'2023-02-01'



select name_guest, count(*) as number_reservations
from guests g 
join reservations r on r.id_guest=g.id_guest
group by name_guest 
order by number_reservations desc 
limit 1



select 
	name_host, 
	sum((r.end_date - r.start_date)*rooms.price_per_day) as income
from hosts h 
join rooms on h.id_host=rooms.id_host 
join reservations r on r.id_room=rooms.id_room 
where start_date>='2023-01-01' and start_date<'2023-02-01'
group by name_host
order by income desc 
limit 1

