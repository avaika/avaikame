#!/bin/bash

ssh avaika '
cd /home/avaika/www/avaika.me;
source .env/bin/activate
./manage.py dumpdata --natural-foreign --exclude auth.permission --exclude contenttypes > db.json;
./manage.py dumpdata thumbnail >> db_t.json;
zip db.zip db.json;
'
scp avaika:/home/avaika/www/avaika_me/db.zip .
unzip db.zip
./manage.py loaddata db.json
./manage.py loaddata db_t.json
rm db.zip db.json db_t.json
ssh avaika 'cd /home/avaika/www/avaika.me; rm db.zip db.json db_t.json'
