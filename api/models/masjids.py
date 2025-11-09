from uuid import uuid4
from datetime import datetime

# app utils imports
from ..cores.extensions import db


class Masjid(db.Model):
    __tablename__ = 'masjids'

    masjid_id = db.Column(db.String(), primary_key=True, default=lambda: str(uuid4()), unique=True, nullable=False)
    name = db.Column(db.String(255), nullable=False)
    category = db.Column(db.String(100), nullable=True)
    country = db.Column(db.String(100), nullable=False)
    city = db.Column(db.String(100), nullable=True)
    latitude = db.Column(db.Float, nullable=False)
    longitude = db.Column(db.Float, nullable=False)
    image_url = db.Column(db.String(500), nullable=True)
    date_of_creation = db.Column(db.DateTime, nullable=True)
    

    # date states
    created_at = db.Column(db.DateTime, default=datetime.now)
    updated_at = db.Column(db.DateTime, default=datetime.now, onupdate=datetime.now)

    def __repr__(self):
        return f'<Masjid {self.name}>'

    # class methods
    @classmethod
    def get_by_id(masjid_model, masjid_id):
        return masjid_model.query.get(masjid_id)

    @classmethod
    def get_by_name(masjid_model, name):
        return masjid_model.query.filter_by(name=name).first()

    @classmethod
    def get_by_country(masjid_model, country):
        return masjid_model.query.filter_by(country=country).all()

    @classmethod
    def get_by_city(masjid_model, city):
        return masjid_model.query.filter_by(city=city).all()

    @classmethod
    def get_by_country_and_city(masjid_model, country, city):
        return masjid_model.query.filter_by(country=country, city=city).all()

    def to_dict(self):
        return {
            'masjid_id': self.masjid_id,
            'name': self.name,
            'category': self.category,
            'country': self.country,
            'city': self.city,
            'image_url': self.image_url,
            'date_of_creation': self.date_of_creation.isoformat() if self.date_of_creation else None,
            'latitude': self.latitude,
            'longitude': self.longitude,
            'created_at': self.created_at.isoformat() if self.created_at else None,
            'updated_at': self.updated_at.isoformat() if self.updated_at else None,
        }

    @classmethod
    def to_collection_dict(cls, masjid_collection=None):
        if not masjid_collection:
            masjid_collection = cls.query.all()
        return [masjid.to_dict() for masjid in masjid_collection]

    # instance methods
    def save(self):
        db.session.add(self)
        db.session.commit()

    def delete(self):
        db.session.delete(self)
        db.session.commit()

    def ping(self):
        self.updated_at = datetime.now()
        db.session.commit()

