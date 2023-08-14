import sqlite3
import datetime

date=datetime.date.today()
datestr=str(date)
# print(datestr)
con = sqlite3.connect("C:/Users/odysseus Katopodis/OneDrive/Vscode/html_table/home-assistant_v2.db")


###### datetime query######################################################################################################
cur = con.cursor()


cur.execute("""SELECT 
last_updated
FROM 
states
WHERE
entity_id IN ("sensor.living_room_temperature")
ORDER BY last_updated DESC 
""")

a0=cur.fetchmany(1)
b0=a0[0]
c0=b0[0]

# print(c0)
# print(type(c0))

datetime=c0
print('datetime=',datetime)
print('-----------------------')
#remove last  subsecond digits 
datetime=datetime[:19]
print('datetime removed characters=',datetime)
print('-----------------------')

datepart= datetime[:11]
print('datepart=',datepart)

timepart=datetime[11:]
print('timepart=',timepart)

hour=timepart[:2]
print('hour=',hour)
hour=int(hour)
hour=hour+2
print('hour=',hour)
hour=str(hour)
print('hour=',hour,'type=',type(hour))

timepart=timepart[2:]
print('timepart cut=',timepart)

timepart=hour+timepart
print('timepart new=',timepart)

datetimeEET=datepart+timepart
print('converted to EET datetimeEET=', datetimeEET)

con.commit()

###### datetime query#########################################################################################################

###### temp 7am query#########################################################################################################
cur = con.cursor()

cur.execute("""SELECT 
state
FROM 
states
WHERE
entity_id IN ("sensor.living_room_temperature") 
AND last_updated BETWEEN ? AND ?
""", (datestr+' 04:57:00',datestr+' 05:10:00')) ### database uses UTC time and user uses EET time. EET= UTC+2

a1=cur.fetchall()
print('a1=',a1,'type=', type(a1))
print('---------------------------')
b1=a1[1]
print('b1=',b1,'type=', type(b1))
print('---------------------------')

#########check if a1 empty###########
if not a1:
    # print("Variable is empty")
    c1='no value in database'
else: 
# print('Variable has value')
    b1=a1[0]
    c1=b1[0]
    ##check if c1 is "unknown" or "unavailable" text string or any float number that can't be transformed to float()
    if (c1>="un"): 
        
        pass
    else:
        c1=float(c1)
##end check

# print(c1)
# print(type(c1))

val7am=c1
print('val7am=',val7am)
print('-----------------------------------------')

con.commit()
###### temp 7am query#########################################################################################################


###### temp 10am query#########################################################################################################
cur = con.cursor()

cur.execute("""SELECT 
state
FROM 
states
WHERE
entity_id IN ("sensor.living_room_temperature") 
AND last_updated BETWEEN ? AND ?
""", (datestr+' 07:57:00',datestr+' 08:10:00'))  ### database uses UTC time and user uses EET time. EET= UTC+2

a1=cur.fetchmany(1)
# print('a1=',a1)
# print('---------------------------')

#########check if a1 empty###########
if not a1:
    # print("Variable is empty")
    c1='no value in database'
else: 
# print('Variable has value')
    b1=a1[0]
    c1=b1[0]
    ##check if c1 is "unknown" or "unavailable" text string or any float number that can't be transformed to float()
    if (c1>="un"): 
        pass
    else:
        c1=float(c1)
##end check

# print(c1)
# print(type(c1))

val10am=c1
print('val10am=',val10am)
print('-----------------------------------------')

con.commit()
###### temp 10am query#########################################################################################################

###### temp 1pm query#########################################################################################################
cur = con.cursor()

cur.execute("""SELECT 
state
FROM 
states
WHERE
entity_id IN ("sensor.living_room_temperature") 
AND last_updated BETWEEN ? AND ?
""", (datestr+' 10:57:00',datestr+' 11:10:00')) ### database uses UTC time and user uses EET time. EET= UTC+2

a1=cur.fetchmany(1)
# print('a1=',a1)
# print('---------------------------')

#########check if a1 empty###########
if not a1:
    # print("Variable is empty")
    c1='no value in database'
else: 
# print('Variable has value')
    b1=a1[0]
    c1=b1[0]
    ##check if c1 is "unknown" or "unavailable" text string or any float number that can't be transformed to float()
    if (c1>="un"): 
        pass
    else: 
        c1=float(c1)
##end check

# print(c1)
# print(type(c1))


val1pm=c1
print('val1pm=',val1pm)
print('-----------------------------------------')
con.commit()
###### temp 1apm query#########################################################################################################

con.close()




import jinja2
sensor_name = 'sensor1'
datetime=datetime
val7am=val7am
val10am=val10am
val1pm=val1pm
outputfile = 'C:/Users/odysseus Katopodis/OneDrive/Vscode/html_table/tablenew.html'
subs = jinja2.Environment( 
              loader=jinja2.FileSystemLoader('C:/Users/odysseus Katopodis/OneDrive/Vscode/html_table')      
              ).get_template('table.html').render(datetime=datetimeEET,sensor_name=sensor_name,val7am=val7am,val10am=val10am,val1pm=val1pm)
# lets write the substitution to a file
with open(outputfile,'w') as f: f.write(subs)