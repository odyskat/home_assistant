from datetime import datetime
import sqlite3
con = sqlite3.connect("home-assistant_v2.db")
cur = con.cursor()
# cur.execute("""CREATE TABLE movie(title, year, score)""")

# cur.execute("INSERT INTO movie VALUES ('odysseus',1994,9000)")

cur.execute("""SELECT 
last_updated
FROM 
states
WHERE
entity_id IN ("sensor.living_room_humidity","sensor.living_room_temperature")""")


a=(cur.fetchmany(2))
print('a=',a)

b=a[0]
print('b=',b)

b1=a[1]
print('b1=',b1)

c=b[0]
c1=b1[0]
print('c1=',c1)

print('c=',c)
print('-----------')
print('ctype=',type(c))


d=datetime.fromisoformat(c)
print('d=',d)
print('-----------')
print('dtype=',type(d))

d1=datetime.fromisoformat(c1)
print('d1=',d1)
print('-----------')
print('d1type=',type(d1))

if d1>d:
    print('d1>d=','true')
else:
    print('d1>d=','false')

con.commit()

con.close()