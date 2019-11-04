from application import routes

def acreage_check(form, field):
    if field.data !=  routes.land_dict[field]:
        raise ValidationError("Field does not match previous year")
