create database login;
use login;
create table logininfo(
id varchar (10),
name varchar(30),
phone varchar (13),
email varchar(100)
);
select * from logininfo;

DROP database login;
