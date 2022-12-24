import sqlite3



async def create_db(): 
    global cur,db
    db = sqlite3.connect("data.db")
    cur = db.cursor()
    cur.execute("CREATE TABLE IF NOT EXISTS data_game (login STR, name str, level int default 1, updrade int default 1, balance  int default 1)")
    db.commit()


async def create_profile(user_id): 
    cur.execute("INSERT INTO data_game (login) VALUES (?)",(user_id,))
    db.commit()



#async def update_db(): 
   # cur.execute(

   # )


async def get_user(): 
    a =cur.execute("SELECT * FROM data_game ").fetchall()
    return a
    
