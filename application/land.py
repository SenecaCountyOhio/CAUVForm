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
                    temp_list.append('No previous submission')
                else:
                    temp_list.append(getattr(obj, each))
        land_dict[each] = temp_list
    return land_dict
