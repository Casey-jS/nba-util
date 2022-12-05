import sqlite3

def create_users_db():
    db = sqlite3.connect("databases/users.db")

    with open("databases/users.sql") as f:
        db.executescript(f.read())

    populate_users(db)

    db.commit()
    db.close()

def dict_from_row(row):
    return dict(zip(row.keys(), row))

def populate_users(db):
    db.row_factory = sqlite3.Row

    usernames = [
        "admin",
        "bucksfan",
        "lebron",
        "casey"
    ]
    passwords = [
        "password",
        "giannis",
        "king",
        "sytsema"
    ]

    ids = [
        23,
        24, 
        25, 
        26
    ]    

    insert_string = "INSERT INTO Users (id, userName, password) VALUES (?, ?, ?)"
    for i in range(4):
        db.execute(insert_string, (ids[i], usernames[i], passwords[i]))

    cursor = db.cursor()
    for i in range(4):
        
        row = cursor.execute("SELECT * FROM Users WHERE id = ?", (ids[i],)).fetchone()
        d = dict_from_row(row)


        print("New User Added\n-------------------------")
        print("Username: ", d['userName'])
        print("Password: ", d['password'])
        print("ID: ", d['id'])


def get_count():
    db = sqlite3.connect('databases/users.db')
    db.row_factory = sqlite3.Row
    cursor = db.cursor()
    count = cursor.execute("SELECT COUNT(*) id FROM Users").fetchone()[0]
    print(count)

#create_users_db()

#get_count()
"""populate_users() """

