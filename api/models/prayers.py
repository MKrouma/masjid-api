from uuid import uuid4
from datetime import datetime, time

# app utils imports
from ..cores.extensions import db


class Prayer(db.Model):
    __tablename__ = 'prayers'

    prayer_id = db.Column(db.String(), primary_key=True, default=lambda: str(uuid4()), unique=True, nullable=False)
    name = db.Column(db.String(255), nullable=False, unique=True)
    description = db.Column(db.String(255), nullable=False)
    order = db.Column(db.Integer, nullable=False, unique=True)
    start_hour = db.Column(db.Time, nullable=True)
    end_hour = db.Column(db.Time, nullable=True)

    # date states
    created_at = db.Column(db.DateTime, default=datetime.now)
    updated_at = db.Column(db.DateTime, default=datetime.now, onupdate=datetime.now)

    def __repr__(self):
        return f'<Prayer {self.name}>'

    # class methods
    @classmethod
    def get_by_id(prayer_model, prayer_id):
        return prayer_model.query.get(prayer_id)

    @classmethod
    def get_by_name(prayer_model, name):
        return prayer_model.query.filter_by(name=name).first()

    def to_dict(self):
        return {
            'prayer_id': self.prayer_id,
            'name': self.name,
            'description': self.description,
            'order': self.order,
            'start_hour': self.start_hour.isoformat() if self.start_hour else None,
            'end_hour': self.end_hour.isoformat() if self.end_hour else None,
            # 'created_at': self.created_at.isoformat() if self.created_at else None,
            # 'updated_at': self.updated_at.isoformat() if self.updated_at else None,
        }

    @classmethod
    def to_collection_dict(cls, prayer_collection=None):
        if not prayer_collection:
            prayer_collection = cls.query.all()
        return [prayer.to_dict() for prayer in prayer_collection]

    # instance methods
    def save(self):
        db.session.add(self)
        db.session.commit()

    def delete(self):
        db.session.delete(self)
        db.session.commit()