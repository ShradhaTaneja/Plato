create table restaurant (
    rid int auto_increment primary key,
    rname varchar(50) not null,
    raddress varchar(200) not null, 
    rcity varchar(20) not null,
    rstate varchar(20) not null,
    rating int default 0,
    rcontact varchar(20) not null,
    rwebsite varchar(30),
    remail varchar(30)
);
