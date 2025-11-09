from flask_restx import Namespace, fields


class PrayerRessource:
    prayer_ns = Namespace("prayer", description="Prayers related operations.")