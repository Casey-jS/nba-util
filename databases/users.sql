DROP TABLE IF EXISTS Users;
CREATE TABLE Users(
    id int,
    userName text primary key,
    password text not null
);