#!/bin/bash

docker exec -it homeassistant bash

apk get sqlite3

sqlite3 home-assistant_v2.db <<'END_SQL'

.headers on 

.mode html 

.once /config/test10.html

SELECT  entity_id,   state,last_updated FROM states WHERE entity_id IN ("sensor.living_room_humidity")
END_SQL