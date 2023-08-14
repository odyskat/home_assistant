import sqlite3
con = sqlite3.connect("home-assistant_v2.db")
cur = con.cursor()
# cur.execute("""CREATE TABLE movie(title, year, score)""")

# cur.execute("INSERT INTO movie VALUES ('odysseus',1994,9000)")

cur.execute("""SELECT 
state
FROM 
states
WHERE
entity_id IN ("sensor.living_room_humidity")""")
d=cur.fetchmany(3)
print(d)

# a=cur.fetchmany(1)
# b=a[0]
# c=float(b[0])
# print(c)
# #print(type(c))

con.commit()

con.close()