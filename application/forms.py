from wtforms import (
    Form,
    StringField,
    PasswordField,
    SubmitField,
    SelectField,
    BooleanField,
    IntegerField,
    DecimalField,
    TextAreaField,
    RadioField
)
from wtforms.validators import (
    ValidationError,
    required,
    InputRequired,
    DataRequired,
    Email,
    EqualTo,
    Length
)

class SignupForm(Form):
    """User Sign Up Form."""
    username = StringField(
        'Email',
        validators=[
            DataRequired(message=('That\'s not a valid email address.'))
        ]
    )
    password = PasswordField(
        'Password',
        validators=[DataRequired(message="Please enter a password.")]
    )
    confirm = PasswordField(
        'Confirm Password',
        validators=[
            InputRequired(),
            EqualTo(
                password,
                message='Passwords must match.'
            )
        ]
    )
    submit = SubmitField(
        'Register'
    )

    def validate_email(self, email):
        """Email validation."""
        user = User.query.filter_by(email=email.data).first()
        if user is not None:
            raise ValidationError('Please use a different email address.')


class SigninForm(Form):
    """User Sign In Form."""
    username = StringField(
        'Email',
        validators=[
            DataRequired(message=('That\'s not a valid email address.'))
        ]
    )
    password = PasswordField('Password',
                             validators=[DataRequired(message="Please enter a password."), ])
    submit = SubmitField('Register')


class AppSearch(Form):
    search = IntegerField('Search App Number')
    submit = SubmitField('Search')

class CAUVForm(Form):
    Commodity_Acres = DecimalField(
        'Commodity Crops -- Corn/Soybeans/Wheat/Oats'
    )
    Hay_Acres = DecimalField(
        'Hay -- Baled at least twice a year'
    )
    Perm_Pasture_Acres = DecimalField(
        'Permanent Pasture -- Used for commercial animal husbandry'
    )
    Noncommercial_Wood_Acres = DecimalField(
        'Noncommercial Woodland -- Contiguous to 10(ten) acres of farmed land'
    )
    Commerical_Wood_Acres = DecimalField(
        'Commercial Timber'
    )
    Other_Crop_Acres = DecimalField(
        'Other Crops -- Nursery Stock/Vegetables/Flowers'
    )
    Homesite_Acres = DecimalField(
        'Homesite(s) -- Minimum 1(one) acre per house'
    )
    Road_Waste_Pond_Acres = DecimalField(
        'Road/Waste/Pond'
    )
    CRP_Acres = DecimalField(
        'Conservation Program -- CRP/CREP/etc. (provide the contract and map)'
    )
    Con25_Acres = DecimalField(
        'Conservation Practices limited to 25% or less of the total acreage(provide map)'
    )
    Other_Use_Acres = DecimalField(
        'Other Use -- Agritourism, Biofuel Production, etc.'
    )
    Stated_Total_Acres = DecimalField(
        label='Total Acres -- Must match acres above',
        validators=[DataRequired()]
    )
    Farmed_Acres_1 = DecimalField()
    Farmed_Acres_2 = DecimalField()
    Farmed_Acres_3 = DecimalField()
    Use_of_Land_1 = StringField()
    Use_of_Land_2 = StringField()
    Use_of_Land_3 = StringField()
    Units_Acre_1 = StringField()
    Units_Acre_2 = StringField()
    Units_Acre_3 = StringField()
    Price_Unit_1 = StringField()
    Price_Unit_2 = StringField()
    Price_Unit_3 = StringField()
    Gross_Income_1 = StringField()
    Gross_Income_2 = StringField()
    Gross_Income_3 = StringField()
    Parcel_Change_Check = RadioField(
        label='Will the general farming operations on any of these parcels change this year?',
        validators=[InputRequired()],
        choices=[
            ('Yes', 'Yes'),
            ('No', 'No')
        ],
    )
    Parcel_Change_Note = TextAreaField(
        'If yes, provide an explanation below;',
        # validators=[Parcel_Check(Parcel_Change_Check)]
    )
    submit = SubmitField('Submit')
