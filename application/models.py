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
    Parcel_Change_Check = db.Column(db.String(4), nullable=False)
    Parcels_Combined_Acres = db.Column(db.Float, nullable=False)
    Commodity_Acres = db.Column(db.Float)
    Hay_Acres = db.Column(db.Float)
    Perm_Pasture_Acres = db.Column(db.Float)
    Noncommercial_Wood_Acres = db.Column(db.Float)
    Commerical_Wood_Acres = db.Column(db.Float)
    Other_Crop_Acres = db.Column(db.Float)
    Homesite_Acres = db.Column(db.Float)
    Road_Waste_Pond_Acres = db.Column(db.Float)
    CRP_Acres = db.Column(db.Float)
    Con25_Acres = db.Column(db.Float)
    Other_Use_Acres = db.Column(db.Float)
    Stated_Total_Acres = db.Column(db.Float, nullable=False)
    Farmed_Acres_1 = db.Column(db.Float)
    Farmed_Acres_2 = db.Column(db.Float)
    Farmed_Acres_3 = db.Column(db.Float)
    Use_of_Land_1 = db.Column(db.Float)
    Use_of_Land_2 = db.Column(db.Float)
    Use_of_Land_3 = db.Column(db.Float)
    Units_Acre_1 = db.Column(db.Float)
    Units_Acre_2 = db.Column(db.Float)
    Units_Acre_3 = db.Column(db.Float)
    Price_Unit_1 = db.Column(db.Float)
    Price_Unit_2 = db.Column(db.Float)
    Price_Unit_3 = db.Column(db.Float)
    Gross_Income_1 = db.Column(db.Float)
    Gross_Income_2 = db.Column(db.Float)
    Gross_Income_3 = db.Column(db.Float)
    date_added = db.Column(db.DateTime, default=datetime.utcnow)

    def __repr__(self):
        return '<Ag App Number %r>' % self.AG_APP

class PreviousCAUVApp(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    user = db.Column(db.String(30), nullable=False)
    AG_APP = db.Column(db.String(30))
    Parcel_Change_Check = db.Column(db.String(30))
    Parcels_Combined_Acres = db.Column(db.String(30))
    Commodity_Acres = db.Column(db.String(30))
    Hay_Acres = db.Column(db.String(30))
    Perm_Pasture_Acres = db.Column(db.String(30))
    Noncommercial_Wood_Acres = db.Column(db.String(30))
    Commerical_Wood_Acres = db.Column(db.String(30))
    Other_Crop_Acres = db.Column(db.String(30))
    Homesite_Acres = db.Column(db.String(30))
    Road_Waste_Pond_Acres = db.Column(db.String(30))
    CRP_Acres = db.Column(db.String(30))
    Con25_Acres = db.Column(db.String(30))
    Other_Use_Acres = db.Column(db.String(30))
    Stated_Total_Acres = db.Column(db.String(30))
    Farmed_Acres_1 = db.Column(db.String(30))
    Farmed_Acres_2 = db.Column(db.String(30))
    Farmed_Acres_3 = db.Column(db.String(30))
    Use_of_Land_1 = db.Column(db.String(30))
    Use_of_Land_2 = db.Column(db.String(30))
    Use_of_Land_3 = db.Column(db.String(30))
    Units_Acre_1 = db.Column(db.String(30))
    Units_Acre_2 = db.Column(db.String(30))
    Units_Acre_3 = db.Column(db.String(30))
    Price_Unit_1 = db.Column(db.String(30))
    Price_Unit_2 = db.Column(db.String(30))
    Price_Unit_3 = db.Column(db.String(30))
    Gross_Income_1 = db.Column(db.String(30))
    Gross_Income_2 = db.Column(db.String(30))
    Gross_Income_3 = db.Column(db.String(30))
    date_added = db.Column(db.DateTime, default=datetime.utcnow)

    def __repr__(self):
        return '<Ag App Number %r>' % self.AG_APP
