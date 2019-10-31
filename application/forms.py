from wtforms import Form, StringField, PasswordField, validators, SubmitField, SelectField, BooleanField, IntegerField, DecimalField
from wtforms.validators import ValidationError, DataRequired, Email, EqualTo, Length

class SignupForm(Form):
    """User Sign Up Form."""
    email = StringField('Email',[
        Length(min=6, message=('Little short for an email address?')),
        Email(message=('That\'s not a valid email address.')),
        DataRequired(message=('That\'s not a valid email address.'))])
    password = PasswordField('Password',
        validators=[DataRequired(message="Please enter a password."),])
    confirm = PasswordField('Confirm Password',
        validators=[EqualTo(password, message='Passwords must match.')])
    submit = SubmitField('Register')

    def validate_email(self, email):
        """Email validation."""
        user = User.query.filter_by(email=email.data).first()
        if user is not None:
            raise ValidationError('Please use a different email address.')


class SigninForm(Form):
    """User Sign In Form."""
    email = StringField('Email',[
        Email(message=('That\'s not a valid email address.')),
        DataRequired(message=('That\'s not a valid email address.'))])
    password = PasswordField('Password',
        validators=[DataRequired(message="Please enter a password."),])
    submit = SubmitField('Register')

class AppSearch(Form):
    search = IntegerField('Search App Number')
    submit = SubmitField('Search')

class CAUVForm(Form):
    Commodity_Acres = DecimalField('Commodity Crops -- Corn/Soybeans/Wheat/Oats')
    Hay_Acres = DecimalField('Hay -- Baled at least twice a year')
    Perm_Pasture_Acres = DecimalField('Permanent Pasture -- Used for commercial animal husbandry')
    Noncommercial_Wood_Acres = DecimalField('Noncommercial Woodland -- Contiguous to 10(ten) acres of farmed land')
    Commerical_Wood_Acres = DecimalField('Commercial Timber')
    Other_Crop_Acres = DecimalField('Other Crops -- Nursery Stock/Vegetables/Flowers')
    Homesite_Acres = DecimalField('Homesite(s) -- Minimum 1(one) acre per house')
    Road_Waste_Pond_Acres = DecimalField('Road/Waste/Pond')
    CRP_Acres = DecimalField('Conservation Program -- CRP/CREP/etc. (provide the contract and map)')
    Con25_Acres = DecimalField('Conservation Practices limited to 25% or less of the total acreage(provide map)')
    Other_Use_Acres = DecimalField('Other Use -- Agritourism, Biofuel Production, etc.')
    submit = SubmitField('Submit')
