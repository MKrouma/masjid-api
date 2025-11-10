from flask_restx import Namespace, fields


class PrayerRessource:
    prayer_ns = Namespace("prayers", description="Prayers related operations.")