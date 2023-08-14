
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
entity_id IN ("sensor.living_room_humidity","sensor.living_room_temperature") 
AND last_updated BETWEEN '2022-10-17 12:30:00' AND '2022-10-17 14:40:0'
""")
#print(cur.fetchall())

a=(cur.fetchmany(1))
print(a)
b=a[0]
c=b[0]

print('c=',c)
print('-----------')
print('ctype=',type(c))


con.commit()

con.close()