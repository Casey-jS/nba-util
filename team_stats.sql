DROP TABLE IF EXISTS TeamStats;
CREATE TABLE TeamStats(
    id int primary key,
    teamName text not null,
    wins int not null,
    losses int not null,
    wpct decimal not null,
    ppg decimal not null,
    fg3pct decimal not null,
    plusminus int not null,
    wrank int not null
);