DROP TABLE IF EXISTS GameLogs;
CREATE TABLE GameLogs(
    playerID int not null,
    opp text not null,
    wl text not null,
    pts int not null,
    fg text not null,
    threes text not null,
    reb int not null,
    ast int not null,
    stl int not null,
    blk int not null
);