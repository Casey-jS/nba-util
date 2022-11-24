import sqlite3

def get_db():
    db = sqlite3.connect("player_stats.db")
    db.row_factory = sqlite3.Row
    return db

def get_count():
    db = get_db()
    cursor = db.cursor()
    cursor.execute("Select * from PlayerStats")
    row_count = len(cursor.fetchall())
    print(row_count)
    cursor.close()
    return row_count

def get_player(id):
    db = get_db()
    player = db.execute("SELECT * FROM PlayerStats WHERE id = ?", (id,)).fetchone()
    db.close()
    return player

def get_id(name):
    db = get_db()
    cursor = db.cursor()
    query = "SELECT * FROM PlayerStats WHERE fullName = ?"
    id = cursor.execute(query, (name,)).fetchone()

    cursor.close()
    return id[0]

# maybe add capability to filter by position
# string passed in should be column name
def get_league_leaders(stat):
    db = get_db()
    cursor = db.cursor()

    query = "SELECT * FROM PlayerStats ORDER BY ppg desc LIMIT 10"
    leader_ids = cursor.execute(query).fetchall()
    return leader_ids


ppg_leaders = get_league_leaders("ppg")

for i in range(10):
    player = ppg_leaders[i]

    fullName = player[1]
    ppg = player[2]
    print(fullName, end = "\n\n")
    print("ID: " + str(player[0]))

    print("PPG: " + str(ppg), end = "\n\n")







    



