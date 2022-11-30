DROP TABLE IF EXISTS FavoritePlayer;
CREATE TABLE FavoritePlayer(
    favID int primary key,
    userID int not null,
    playerID int not null
);