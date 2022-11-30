DROP TABLE IF EXISTS PlayerStats;
CREATE TABLE PlayerStats(
    id int primary key,
    fullName text not null,
    teamID int not null,
    fantasyRank int not null,
    team text not null,
    games int not null,
    age int not null,
    ppg decimal not null,
    apg decimal not null,
    rpg decimal not null,
    spg decimal not null,
    bpg decimal not null,
    fgpct decimal not null,
    fg3pct decimal not null,
    ftpct decimal not null
);