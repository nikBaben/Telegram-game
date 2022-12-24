import sqlite3



async def create_db(): 
    global cur,db
    db = sqlite3.connect("data.db")
    cur = db.cursor()
    cur.execute("CREATE TABLE IF NOT EXISTS data_game (login str)")
    db.commit()


async def create_profile(lol:str): 
    cur.execute("INSERT INTO data_game (login) VALUES (?)",(lol,))
    db.commit()

