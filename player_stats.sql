DROP TABLE IF EXISTS PlayerStats;
CREATE TABLE PlayerStats(
    id int primary key,
    fullName text not null,
    ppg decimal not null,
    apg decimal not null,
    rpg decimal not null,
    spg decimal not null,
    bpg decimal not null
);