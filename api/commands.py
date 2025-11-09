import os
import json
import click
import pandas as pd
from flask.cli import with_appcontext
from sqlalchemy import exists, and_
from dotenv import load_dotenv
from datetime import datetime, time
from api import db
from api.models.masjids import Masjid
from api.models.prayers import Prayer

# load env
load_dotenv(override=True)
mode = os.getenv('FLASK_ENV')
data_dir = 'data/temp'


@click.command(name="restart_db")
@with_appcontext
def restart_db():
    """Restart the database by dropping and creating all tables."""

    db.drop_all()
    db.create_all()
    # Role.insert_roles()
    print("Database restarted successfully.")


@click.command(name="add_prayers")
@with_appcontext
def add_prayers():
    """Add prayers to the database from a JSON file."""

    # read json data
    file_name = os.path.join(data_dir, 'prayers.json')
    prayer_df = pd.read_json(file_name)

    count_exists = 0
    count_added = 0
    for index, row in prayer_df.iterrows():
        prayer_data = row.to_dict()

        # check if prayer already exists
        if Prayer.get_by_name(prayer_data['name']):
            print(f"Prayer {prayer_data['name']} already exists.")
            count_exists += 1
        
        else:
            # Parse time strings to time objects
            if prayer_data.get('start_hour'):
                prayer_data['start_hour'] = datetime.strptime(prayer_data['start_hour'], '%H:%M:%S').time()
            if prayer_data.get('end_hour'):
                prayer_data['end_hour'] = datetime.strptime(prayer_data['end_hour'], '%H:%M:%S').time()
            
            new_prayer = Prayer(**prayer_data)
            new_prayer.save()
            count_added += 1

    print(f"Successfully added {count_added} prayers to db.")
    print(f"Prayers already exists: {count_exists}")


@click.command(name="add_masjids")
@with_appcontext
def add_masjids():
    """Add masjids to the database from a CSV file."""

    # read csv data
    file_name = os.path.join(data_dir, 'osm_masjid-clean-20251109.csv')
    masjid_df = pd.read_csv(file_name)
    
    count_exists = 0
    count_added = 0
    for index, row in masjid_df.iterrows():
        masjid_data = row.to_dict()

        new_masjid = Masjid(**masjid_data)
        new_masjid.save()
    
        count_added += 1

    
    print(f"Successfully added {count_added} prayers to db.")
    print(f"Prayers already exists: {count_exists}")
    
        

    