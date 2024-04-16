import sqlite3 as sq

#
# async def db_start():
#     cur.execute("CREATE TABLE IF NOT EXISTS user("
#                 "user_id TEXT PRIMARY KEY,"
#                 "tg_id INTEGER,username TEXT)")
#     db.commit()
#
#
# async def cmd_start_db(user_id):
#     user = cur.execute("SELECT * FROM users WHERE tg_id == '{key}'".format(key=user_id)).fetchone()
#     if not user:
#         cur.execute("INSERT tg_id INTO users VALUES {key}".format(key=user_id))
#         db.commit()
