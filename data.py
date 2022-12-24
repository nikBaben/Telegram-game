import sqlite3



async def create_db(): 
    global cur,db
    db = sqlite3.connect("data.db")
    cur = db.cursor()
    cur.execute("CREATE TABLE IF NOT EXISTS data_game(user_id PRIMARY KEY, level int, upgrade int)")
    db.commit()


async def create_profile(user_id): 
    cur.execute("""INSERT INTO data_game """)