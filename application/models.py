from . import db
from flask_login import UserMixin
from datetime import datetime

class User(UserMixin, db.Model):
    id = db.Column(db.Integer, primary_key=True)
    username = db.Column(db.String(30), nullable=False, unique=True)
    password = db.Column(db.String(15), nullable=False)
    date_created = db.Column(db.DateTime, default=datetime.utcnow)

    def __repr__(self):
        return '<User %r>' % self.username

class CAUVApp(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    user = db.Column(db.String(30), nullable=False)
    AG_APP = db.Column(db.Integer, nullable=False, unique=True)
    Parcel_Change_Check = db.Column(db.Boolean, default=False, nullable=False)
    Parcels_Combined_Acres = db.Column(db.Float, nullable=False)
    Commodity_Acres = db.Column(db.Float, default=0, nullable=False)
    Hay_Acres = db.Column(db.Float, default=0, nullable=False)
    Perm_Pasture_Acres = db.Column(db.Float, default=0, nullable=False)
    Noncommercial_Wood_Acres = db.Column(db.Float, default=0, nullable=False)
    Commerical_Wood_Acres = db.Column(db.Float, default=0, nullable=False)
    Other_Crop_Acres = db.Column(db.Float, default=0, nullable=False)
    Homesite_Acres = db.Column(db.Float, default=0, nullable=False)
    Road_Waste_Pond_Acres = db.Column(db.Float, default=0, nullable=False)
    CRP_Acres = db.Column(db.Float, default=0, nullable=False)
    Con25_Acres = db.Column(db.Float, default=0, nullable=False)
    Other_Use_Acres = db.Column(db.Float, default=0, nullable=False)
    Stated_Total_Acres = db.Column(db.Float, nullable=False)
    date_added = db.Column(db.DateTime, default=datetime.utcnow)

    def __repr__(self):
        return '<Ag App Number %r>' % self.AG_APP
