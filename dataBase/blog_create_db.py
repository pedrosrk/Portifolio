import sqlite3 as sql

#connect to SQLite
con = sql.connect('db_web.db')

#Create a Connection
cur = con.cursor()

#Drop msgs table if already exsist.
cur.execute("DROP TABLE IF EXISTS msgs")

#Create msgs table  in db_web database
sql ='''CREATE TABLE "msgs" (
	"UID"	INTEGER PRIMARY KEY AUTOINCREMENT,
	"UNAME"	TEXT,
	"CONTACT"	TEXT
)'''
cur.execute(sql)

#commit changes
con.commit()

#close the connection
con.close()