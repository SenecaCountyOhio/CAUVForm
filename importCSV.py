from application import db, login_manager, create_app
from application.models import PreviousCAUVApp
import csv

app = create_app()
app.app_context().push()
db.session.query(PreviousCAUVApp).delete()
db.session.commit()
cauv_dict = {
    'AG_APP': None,
    'Parcel_Change_Check': None,
    'Parcels_Combined_Acres': None,
    'Commodity_Acres': None,
    'Hay_Acres': None,
    'Perm_Pasture_Acres': None,
    'Noncommercial_Wood_Acres': None,
    'Commerical_Wood_Acres': None,
    'Other_Crop_Acres': None,
    'Homesite_Acres': None,
    'Road_Waste_Pond_Acres': None,
    'CRP_Acres': None,
    'Con25_Acres': None,
    'Other_Use_Acres': None,
    'Stated_Total_Acres': None,
    'Farmed_Acres_1': None,
    'Farmed_Acres_2': None,
    'Farmed_Acres_3': None,
    'Use_of_Land_1': None,
    'Use_of_Land_2': None,
    'Use_of_Land_3': None,
    'Units_Acre_1': None,
    'Units_Acre_2': None,
    'Units_Acre_3': None,
    'Price_Unit_1': None,
    'Price_Unit_2': None,
    'Price_Unit_3': None,
    'Gross_Income_1': None,
    'Gross_Income_2': None,
    #'Gross_Income_3': None,
}

for row in open('2019RENEWAL_CAUV_APPS_DATABASE.csv'):
    line = row.split(',')
    cauv_dict['AG_APP'] = line[0]
    cauv_dict['Parcels_Combined_Acres'] = line[1]
    cauv_dict['Parcel_Change_Check'] = line[2]
    cauv_dict['Commodity_Acres'] = line[3]
    cauv_dict['Hay_Acres'] = line[4]
    cauv_dict['Perm_Pasture_Acres'] = line[5]
    cauv_dict['Noncommercial_Wood_Acres'] = line[6]
    cauv_dict['Commerical_Wood_Acres'] = line[7]
    cauv_dict['Other_Crop_Acres'] = line[8]
    cauv_dict['Homesite_Acres'] = line[9]
    cauv_dict['Road_Waste_Pond_Acres'] = line[10]
    cauv_dict['CRP_Acres'] = line[11]
    cauv_dict['Con25_Acres'] = line[12]
    cauv_dict['Other_Use_Acres'] = line[13]
    cauv_dict['Stated_Total_Acres'] = line[14]
    cauv_dict['Farmed_Acres_1'] = line[15]
    cauv_dict['Use_of_Land_1'] = line[16]
    cauv_dict['Units_Acre_1'] = line[17]
    cauv_dict['Price_Unit_1'] = line[18]
    cauv_dict['Gross_Income_1'] = line[19]
    cauv_dict['Farmed_Acres_2'] = line[20]
    cauv_dict['Use_of_Land_2'] = line[21]
    cauv_dict['Units_Acre_2'] = line[22]
    cauv_dict['Price_Unit_2'] = line[23]
    cauv_dict['Gross_Income_2'] = line[24]
    cauv_dict['Farmed_Acres_3'] = line[25]
    cauv_dict['Use_of_Land_3'] = line[26]
    cauv_dict['Units_Acre_3'] = line[27]
    cauv_dict['Price_Unit_3'] = line[28]
    # cauv_dict['Gross_Income_3'] = line[29]
    for each in cauv_dict:
        app = PreviousCAUVApp(
            user="BC",
            AG_APP=cauv_dict['AG_APP'],
            Parcel_Change_Check=cauv_dict['Parcel_Change_Check'],
            Parcels_Combined_Acres=cauv_dict['Parcels_Combined_Acres'],
            Commodity_Acres=cauv_dict['Commodity_Acres'],
            Hay_Acres=cauv_dict['Hay_Acres'],
            Perm_Pasture_Acres=cauv_dict['Perm_Pasture_Acres'],
            Noncommercial_Wood_Acres=cauv_dict['Noncommercial_Wood_Acres'],
            Commerical_Wood_Acres=cauv_dict['Commerical_Wood_Acres'],
            Other_Crop_Acres=cauv_dict['Other_Crop_Acres'],
            Homesite_Acres=cauv_dict['Homesite_Acres'],
            Road_Waste_Pond_Acres=cauv_dict['Road_Waste_Pond_Acres'],
            CRP_Acres=cauv_dict['CRP_Acres'],
            Con25_Acres=cauv_dict['Con25_Acres'],
            Other_Use_Acres=cauv_dict['Other_Use_Acres'],
            Stated_Total_Acres=cauv_dict['Stated_Total_Acres'],
            Farmed_Acres_1=cauv_dict['Farmed_Acres_1'],
            Farmed_Acres_2=cauv_dict['Farmed_Acres_2'],
            Farmed_Acres_3=cauv_dict['Farmed_Acres_3'],
            Use_of_Land_1=cauv_dict['Use_of_Land_1'],
            Use_of_Land_2=cauv_dict['Use_of_Land_2'],
            Use_of_Land_3=cauv_dict['Use_of_Land_3'],
            Units_Acre_1=cauv_dict['Units_Acre_1'],
            Units_Acre_2=cauv_dict['Units_Acre_2'],
            Units_Acre_3=cauv_dict['Units_Acre_3'],
            Price_Unit_1=cauv_dict['Price_Unit_1'],
            Price_Unit_2=cauv_dict['Price_Unit_2'],
            Price_Unit_3=cauv_dict['Price_Unit_3'],
            Gross_Income_1=cauv_dict['Gross_Income_1'],
            Gross_Income_2=cauv_dict['Gross_Income_2'],
            # Gross_Income_3=cauv_dict['Gross_Income_3'],
        )
        db.session.add(app)
db.session.commit()
