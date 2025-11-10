# Masjid-API
An API for masjid in Ivory Coast.


## Migration
```
DEV MIGRATE
flask --app=main.py db init --directory mig_dev
flask --app=main.py db migrate -m "lat, lon in masjid model" --directory mig_dev
flask --app=main.py db upgrade --directory mig_dev
flask --app=main.py db stamp head --directory mig_dev

STAGE MIGRATE
flask --app=main.py db init --directory mig_stage
flask --app=main.py db migrate -m "init stage mig" --directory mig_stage
flask --app=main.py db upgrade --directory mig_stage
flask --app=main.py db stamp head --directory mig_stage
```


## Commands
```
flask --app=main.py restart_db
flask --app=main.py add_prayers
flask --app=main.py add_masjids
```