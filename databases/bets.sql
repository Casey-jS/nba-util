DROP TABLE IF EXISTS Bets;
CREATE TABLE Bets(
    user text not null, 
    playerID int not null, 
    playerName text not null,
    stat text not null,
    amount decimal not null,
    opp text not null
);