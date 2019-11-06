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
    AG_APP = db.Column(db.String(30), nullable=False)
    Parcel_Change_Check = db.Column(db.String(4), nullable=False)
    Parcel_Change_Note = db.Column(db.String(150))
    Parcels_Combined_Acres = db.Column(db.String(30), nullable=False)
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
    Stated_Total_Acres = db.Column(db.String(30), nullable=False)
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

class TempCAUVApp(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    user = db.Column(db.String(30), nullable=False)
    AG_APP = db.Column(db.String(30))
    Parcel_Change_Check = db.Column(db.String(30))
    Parcel_Change_Note = db.Column(db.String(150))
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
