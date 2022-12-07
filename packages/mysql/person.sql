

drop table if exists persons;

create table persons 
(
    id int auto_increment PRIMARY KEY,
    first_name varchar(255),
    last_name varchar(255),
    address varchar(255),
    city varchar(255)
)

