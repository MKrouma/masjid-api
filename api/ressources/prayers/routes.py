import os
from datetime import datetime, timedelta, date
from flask import jsonify, request, make_response, url_for, redirect, current_app
from flask_restx import Resource
from sqlalchemy import or_
from dotenv import load_dotenv

# api imports
from api.models.prayers import Prayer
from api.cores.errors import bad_request, unauthorized
from api.cores.extensions import limiter, db

# players modules
from . import PrayerRessource


# load env
load_dotenv(override=True)

# init namespace
prayer_ns = PrayerRessource.prayer_ns


@prayer_ns.route('')
class GetPrayers(Resource):

    def get(self):
        """
            Get all prayers
        """
        payload = {
            "prayers" : Prayer.to_collection_dict()
        }

        # add next prayer
        next_prayer = Prayer.get_next_prayer()
        payload["next_prayer"] = next_prayer.to_dict()

        return make_response(jsonify(
            {
                'message': 'Prayers fetched successfully.', 
                'payload': payload
            }), 
            200
        )