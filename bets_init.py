import sqlite3


def create_bets_db():
    db = sqlite3.connect("databases/bets.db")

    with open("databases/bets.sql") as f:
        db.executescript(f.read())

    db.row_factory = sqlite3.Row

    names = ["LeBron James", "Russell Westbrook", "Anthony Davis", "Joel Embiid", "Jayson Tatum"]
    stats = ["pts", "ast", "reb", "blk", "3pt"]
    opps = ["GSW", "ATL", "NOP", "IND", "DET"]
    amount = [27.5, 8.5, 9.5, 1.5, 5.5]
    user = "admin"
    ids = [2544, 201566, 203076, 203954, 1628369]

    for i in range(5):
        insert_string = "INSERT INTO Bets (user, playerID, playerName, stat, amount, opp) VALUES (?, ?, ?, ?, ?, ?)"
        db.execute(insert_string, ("admin", ids[i], names[i], stats[i], amount[i], opps[i]))
    
    db.commit()
    db.close()

create_bets_db()