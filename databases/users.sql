DROP TABLE IF EXISTS Users;
CREATE TABLE Users(
    id int primary key,
    userName text not null,
    password text not null
);