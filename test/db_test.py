import sqlite3

def get_db():
    db = sqlite3.connect("databases/team_logs.db")
    db.row_factory = sqlite3.Row
    return db


db = get_db()

cursor = db.cursor()

def dict_from_row(row):
    return dict(zip(row.keys(), row))

games = cursor.execute("SELECT * FROM TeamLogs WHERE teamID = ?", (1610612753,)).fetchall()

for row in games:
    d = dict(row)
    print(d['opp'])
    print(d['pts'])
    print(d['ast'])










