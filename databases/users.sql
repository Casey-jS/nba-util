DROP TABLE IF EXISTS Users;
CREATE TABLE Users(
    id int not null,
    userName text not null,
    email text not null,
    password text not null
);