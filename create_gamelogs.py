import sqlite3

db: sqlite3.Connection = sqlite3.connect('/databases/game_logs.db')
db.row_factory = sqlite3.Row
cursor = db.cursor()

values_to_insert = (
    2544, 
    ""
)