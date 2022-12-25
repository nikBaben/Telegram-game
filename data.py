import sqlite3



async def create_db(): 
    global cur,db
    db = sqlite3.connect("data.db")
    cur = db.cursor()
    cur.execute("CREATE TABLE IF NOT EXISTS data_game (login STR, name STR, level int default 1, updrade int default 1, balance  int default 0)")
    db.commit()


async def create_profile(user_id,user_name): 
    user = (user_id,user_name)
    cur.execute("INSERT INTO data_game (login,name) VALUES (?,?)", user )
    db.commit()



async def get_balance(user_id):
    user = user_id
    a = cur.execute("SELECT balance FROM data_game WHERE login=?", (user,)).fetchone()
    return a



async def up_balance(money,user_id):
    user = (money,user_id)
    a = cur.execute("UPDATE data_game set balance = ? WHERE login = ? ", user)
    return a

async def get_user(user_id): 
    a =cur.execute("SELECT name FROM data_game WHERE login = ? ",(user_id,)).fetchone()
    return a
    
