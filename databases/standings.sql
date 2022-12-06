DROP TABLE IF EXISTS Standings;
CREATE TABLE Standings(
    teamID int primary key,
    teamName text not null,
    conf text not null,
    lrank int not null,
    record text not null,
    home text not null,
    away text not null,
    last10 text not null
);