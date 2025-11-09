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

    @prayer_ns.doc(
        'Get All Prayers',
        responses={
            200: "Success.",
            400: "Bad request.",
            401: "Unauthorized.",
            403: "Forbidden."
        },
    )
    def get(self):
        """
            Get all prayers
        """
        return make_response(jsonify(
            {
                'message': 'Prayers fetched successfully.', 
                'payload': Prayer.to_collection_dict()
            }), 
            200
        )