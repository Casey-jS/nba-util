DROP TABLE IF EXISTS TeamLogs;
CREATE TABLE TeamLogs(
    teamID int not null,
    opp text not null,
    res text not null,
    pts int not null,
    ast int not null,
    reb int not null,
    fg text not null,
    fg3 text not null,
    ft text not null,
    tov int not null,
    stl int not null,
    blk int not null
);