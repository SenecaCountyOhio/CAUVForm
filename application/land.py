from application.models import CAUVApp, PreviousCAUVApp, TempCAUVApp


def land(form, app_num):
    model_dict = {
        'CAUVApp': CAUVApp.query.filter(
            CAUVApp.AG_APP == app_num).first(),
        'PreviousCAUVApp': PreviousCAUVApp.query.filter(
            PreviousCAUVApp.AG_APP == app_num).first(),
        'TempCAUVApp': TempCAUVApp.query.filter(
            TempCAUVApp.AG_APP == app_num).first(),
        'CAUVForm': form,
    }
    land_dict = {
        'Commodity_Acres': [],
        'Hay_Acres': [],
        'Perm_Pasture_Acres': [],
        'Noncommercial_Wood_Acres': [],
        'Commerical_Wood_Acres': [],
        'Other_Crop_Acres': [],
        'Homesite_Acres': [],
        'Road_Waste_Pond_Acres': [],
        'CRP_Acres': [],
        'Con25_Acres': [],
        'Other_Use_Acres': [],
        'Stated_Total_Acres': [],
    }
    for each in land_dict:
        temp_list = []
        for models in model_dict:
            obj = model_dict[models]
            if models == 'CAUVForm':
                x = getattr(obj, each)
                label = getattr(x, 'label')
                temp_list.append(x)
                temp_list.append(label)
            else:
                if obj is None:
                    temp_list.append('')
                else:
                    temp_list.append(getattr(obj, each))
        land_dict[each] = temp_list
    return land_dict

def income(form, app_num):
    model_dict = {
        'CAUVApp': CAUVApp.query.filter(
            CAUVApp.AG_APP == app_num).first(),
        'PreviousCAUVApp': PreviousCAUVApp.query.filter(
            PreviousCAUVApp.AG_APP == app_num).first(),
        'TempCAUVApp': TempCAUVApp.query.filter(
            TempCAUVApp.AG_APP == app_num).first(),
        'CAUVForm': form,
    }

    row_dict = {
        'income_row_1': {
            'Farmed_Acres_1': [],
            'Use_of_Land_1': [],
            'Units_Acre_1': [],
            'Price_Unit_1': [],
            'Gross_Income_1': [],
        },
        'income_row_2': {
            'Farmed_Acres_2': [],
            'Use_of_Land_2': [],
            'Units_Acre_2': [],
            'Price_Unit_2': [],
            'Gross_Income_2': [],
        },
        'income_row_3': {
            'Farmed_Acres_3': [],
            'Use_of_Land_3': [],
            'Units_Acre_3': [],
            'Price_Unit_3': [],
            'Gross_Income_3': [],
        },
    }

    for row in row_dict:
        for each in row_dict[row]:
            temp_list = []
            for model in model_dict:
                obj = model_dict[model]
                if obj is None:
                    temp_list.append('')
                else:
                    temp_list.append(getattr(obj, each))
            row_dict[row][each] = temp_list
    return row_dict


def item5(form, app_num):
    model_dict = {
        'CAUVApp': CAUVApp.query.filter(
            CAUVApp.AG_APP == app_num).first(),
        'PreviousCAUVApp': PreviousCAUVApp.query.filter(
            PreviousCAUVApp.AG_APP == app_num).first(),
        'TempCAUVApp': TempCAUVApp.query.filter(
            TempCAUVApp.AG_APP == app_num).first(),
        'CAUVForm': form,
    }
    item5_dict = {
        'Parcel_Change_Check': [],
        'Parcel_Change_Note': [],
    }

    for each in item5_dict:
        temp_list = []
        for model in model_dict:
            obj = model_dict[model]
            if model == 'CAUVForm':
                x = getattr(obj, each)
                label = getattr(x, 'label')
                temp_list.append(x)
                temp_list.append(label)
            else:
                if obj is None:
                    temp_list.append('')
                else:
                    temp_list.append(getattr(obj, each))
        item5_dict[each] = temp_list
    return item5_dict
