from flask import redirect, render_template, flash, request, session, url_for
from flask_login import login_required, logout_user, current_user, login_user
from flask import current_app as app
from werkzeug.security import generate_password_hash, check_password_hash
from .forms import SigninForm, SignupForm, AppSearch, CAUVForm
from .models import db, User, CAUVApp, PreviousCAUVApp, TempCAUVApp
from . import login_manager
from .land import land


@login_manager.user_loader
def load_user(user_id):
    """Check if user is logged-in on every page load."""
    if user_id is not None:
        return User.query.get(user_id)
    return None


@app.route('/')
def base():
    return redirect('/signin')


@app.route('/signin', methods=['GET', 'POST'])
def signin():
    """Login Form."""
    login_form = SigninForm()
    error = ''
    if request.method == 'POST':
        try:
            user = User.query.filter(
                User.username == request.form['username']
            ).first()
            if user.password == request.form['password']:
                login_user(user)
                return redirect('/app_search')
            else:
                error = "Password does not match"
        except:
            error = 'User not registered, contact admin'
    return render_template(
        'signin.html',
        form=login_form,
        error=error
    )


@app.route('/signup', methods=['GET', 'POST'])
@login_required
def signup():
    """Signup Form."""
    if current_user.username != 'admin':
        return redirect('/app_search')
    else:
        signup_form = SignupForm()
        error = ""
        if request.method == 'POST':
            try:
                if request.form['confirm'] == request.form['password']:
                    new_user = User(
                        username=request.form['username'],
                        password=request.form['password']
                    )
                    db.session.add(new_user)
                    db.session.commit()
                    return render_template(
                        'success.html'
                    )
                else:
                    error = 'Passwords do not match'
            except:
                error = 'User already in system'
        return render_template(
            'signup.html',
            form=signup_form,
            error=error
        )


@app.route('/logout')
@login_required
def logout():
    logout_user()
    return redirect('/signin')


@app.route('/app_search', methods=['POST', 'GET'])
@login_required
def app_search():
    if current_user.username == 'admin':
        admin = 1
    else:
        admin = 0
    search_form = AppSearch()
    error = []
    if request.method == 'POST':
        search = request.form['search']
        app = PreviousCAUVApp.query.filter(
            PreviousCAUVApp.AG_APP == search
        ).first()
        if app is None:
            error = ['No Applications Found using ' + search]
        else:
            return redirect('/fillform/' + str(search))

    return render_template(
        'search.html',
        error=error,
        form=search_form,
        admin=admin,
    )


@app.route('/fillform/<int:id>', methods=['POST', 'GET'])
@login_required
def fillform(id):
    app_num = id
    form = CAUVForm()
    message = ''
    app = PreviousCAUVApp.query.filter(PreviousCAUVApp.AG_APP == id).first()
    land_dict1 = land(
        form=CAUVForm(),
        app_num=app_num
    )
    land_dict2 = {
        'Commodity_Acres': [
            app.Commodity_Acres,
            form.Commodity_Acres,
            form.Commodity_Acres.label
        ],
        'Hay_Acres': [
            app.Hay_Acres,
            form.Hay_Acres,
            form.Hay_Acres.label
        ],
        'Perm_Pasture_Acres': [
            app.Perm_Pasture_Acres,
            form.Perm_Pasture_Acres,
            form.Perm_Pasture_Acres.label
        ],
        'Noncommercial_Wood_Acres': [
            app.Noncommercial_Wood_Acres,
            form.Noncommercial_Wood_Acres,
            form.Noncommercial_Wood_Acres.label
        ],
        'Commerical_Wood_Acres': [
            app.Commerical_Wood_Acres,
            form.Commerical_Wood_Acres,
            form.Commerical_Wood_Acres.label
        ],
        'Other_Crop_Acres': [
            app.Other_Crop_Acres,
            form.Other_Crop_Acres,
            form.Other_Crop_Acres.label
        ],
        'Homesite_Acres': [
            app.Homesite_Acres,
            form.Homesite_Acres,
            form.Homesite_Acres.label
        ],
        'Road_Waste_Pond_Acres': [
            app.Road_Waste_Pond_Acres,
            form.Road_Waste_Pond_Acres,
            form.Road_Waste_Pond_Acres.label
            ],
        'CRP_Acres': [
            app.CRP_Acres,
            form.CRP_Acres,
            form.CRP_Acres.label
        ],
        'Con25_Acres': [
            app.Con25_Acres,
            form.Con25_Acres,
            form.Con25_Acres.label
        ],
        'Other_Use_Acres': [
            app.Other_Use_Acres,
            form.Other_Use_Acres,
            form.Other_Use_Acres.label
        ],
        'Stated_Total_Acres': [
            app.Stated_Total_Acres,
            form.Stated_Total_Acres,
            form.Stated_Total_Acres.label
        ],
    }
    income_dict = {
        'Income_Row_1': [
            [
                form.Farmed_Acres_1,
                app.Farmed_Acres_1,
            ],
            [
                form.Use_of_Land_1,
                app.Use_of_Land_1,
            ],
            [
                form.Units_Acre_1,
                app.Units_Acre_1,
            ],
            [
                form.Price_Unit_1,
                app.Price_Unit_1,
            ],
            [
                form.Gross_Income_1,
                app.Gross_Income_1,
            ],
        ],
        'Income_Row_2': [
            [
                form.Farmed_Acres_2,
                app.Farmed_Acres_2,
            ],
            [
                form.Use_of_Land_2,
                app.Use_of_Land_2,
            ],
            [
                form.Units_Acre_2,
                app.Units_Acre_2,
            ],
            [
                form.Price_Unit_2,
                app.Price_Unit_2,
            ],
            [
                form.Gross_Income_2,
                app.Gross_Income_2,
            ]
        ],
        'Income_Row_3': [
            [
                form.Farmed_Acres_3,
                app.Farmed_Acres_3
            ],
            [
                form.Use_of_Land_3,
                app.Use_of_Land_3
            ],
            [
                form.Units_Acre_3,
                app.Units_Acre_3
            ],
            [
                form.Price_Unit_3,
                app.Price_Unit_3
            ],
            [
                form.Gross_Income_3,
                app.Gross_Income_3
            ]
        ]
    }
    if request.method == 'POST':
        db.session.query(TempCAUVApp).delete()
        db.session.commit()
        new_temp_app = TempCAUVApp(
            user=current_user.username,
            AG_APP=app.AG_APP,
            Parcel_Change_Check=request.form['Parcel_Change_Check'],
            Parcel_Change_Note=request.form['Parcel_Change_Note'],
            Parcels_Combined_Acres=app.Parcels_Combined_Acres,
            Commodity_Acres=request.form['Commodity_Acres'],
            Hay_Acres=request.form['Hay_Acres'],
            Perm_Pasture_Acres=request.form['Perm_Pasture_Acres'],
            Noncommercial_Wood_Acres=request.form['Noncommercial_Wood_Acres'],
            Commerical_Wood_Acres=request.form['Commerical_Wood_Acres'],
            Other_Crop_Acres=request.form['Other_Crop_Acres'],
            Homesite_Acres=request.form['Homesite_Acres'],
            Road_Waste_Pond_Acres=request.form['Road_Waste_Pond_Acres'],
            CRP_Acres=request.form['CRP_Acres'],
            Con25_Acres=request.form['Con25_Acres'],
            Other_Use_Acres=request.form['Other_Use_Acres'],
            Stated_Total_Acres=request.form['Stated_Total_Acres'],
            Farmed_Acres_1=request.form['Farmed_Acres_1'],
            Farmed_Acres_2=request.form['Farmed_Acres_2'],
            Farmed_Acres_3=request.form['Farmed_Acres_3'],
            Use_of_Land_1=request.form['Use_of_Land_1'],
            Use_of_Land_2=request.form['Use_of_Land_2'],
            Use_of_Land_3=request.form['Use_of_Land_3'],
            Units_Acre_1=request.form['Units_Acre_1'],
            Units_Acre_2=request.form['Units_Acre_2'],
            Units_Acre_3=request.form['Units_Acre_3'],
            Price_Unit_1=request.form['Price_Unit_1'],
            Price_Unit_2=request.form['Price_Unit_2'],
            Price_Unit_3=request.form['Price_Unit_3'],
            Gross_Income_1=request.form['Gross_Income_1'],
            Gross_Income_2=request.form['Gross_Income_2'],
            Gross_Income_3=request.form['Gross_Income_3'],
        )
        db.session.add(new_temp_app)
        db.session.commit()
        return redirect('/submit/' + str(id))

    return render_template(
        'index.html',
        app=app,
        form=form,
        land_dict=land_dict1,
        income_dict=income_dict
    )


@app.route('/submit/<int:id>', methods=['POST', 'GET'])
@login_required
def submit(id):
    app_num = id
    form = CAUVForm()
    temp_app = TempCAUVApp.query.filter(
        TempCAUVApp.AG_APP == id
    ).first()
    old_app = PreviousCAUVApp.query.filter(
        PreviousCAUVApp.AG_APP == id
    ).first()
    land_dict = land(
        form=CAUVForm(),
        app_num=app_num,
    )
    income_dict = {
        'Income_Row_1': [
            [
                old_app.Farmed_Acres_1,
                temp_app.Farmed_Acres_1,
            ],
            [
                old_app.Use_of_Land_1,
                temp_app.Use_of_Land_1,
            ],
            [
                old_app.Units_Acre_1,
                temp_app.Units_Acre_1,
            ],
            [
                old_app.Price_Unit_1,
                temp_app.Price_Unit_1,
            ],
            [
                old_app.Gross_Income_1,
                temp_app.Gross_Income_1,
            ],
        ],
        'Income_Row_2': [
            [
                old_app.Farmed_Acres_2,
                temp_app.Farmed_Acres_2,
            ],
            [
                old_app.Use_of_Land_2,
                temp_app.Use_of_Land_2,
            ],
            [
                old_app.Units_Acre_2,
                temp_app.Units_Acre_2,
            ],
            [
                old_app.Price_Unit_2,
                temp_app.Price_Unit_2,
            ],
            [
                old_app.Gross_Income_2,
                temp_app.Gross_Income_2,
            ]
        ],
        'Income_Row_3': [
            [
                old_app.Farmed_Acres_3,
                temp_app.Farmed_Acres_3
            ],
            [
                old_app.Use_of_Land_3,
                temp_app.Use_of_Land_3
            ],
            [
                old_app.Units_Acre_3,
                temp_app.Units_Acre_3
            ],
            [
                old_app.Price_Unit_3,
                temp_app.Price_Unit_3
            ],
            [
                old_app.Gross_Income_3,
                temp_app.Gross_Income_3
            ]
        ]
    }
    if request.method == "POST":
        app = CAUVApp.query.filter(CAUVApp.AG_APP == app_num).first()
        if app is None:
            completed_app = CAUVApp(
                user=current_user.username,
                AG_APP=temp_app.AG_APP,
                Parcel_Change_Check=temp_app.Parcel_Change_Check,
                Parcels_Combined_Acres=temp_app.Parcels_Combined_Acres,
                Commodity_Acres=temp_app.Commodity_Acres,
                Hay_Acres=temp_app.Hay_Acres,
                Perm_Pasture_Acres=temp_app.Perm_Pasture_Acres,
                Noncommercial_Wood_Acres=temp_app.Noncommercial_Wood_Acres,
                Commerical_Wood_Acres=temp_app.Commerical_Wood_Acres,
                Other_Crop_Acres=temp_app.Other_Crop_Acres,
                Homesite_Acres=temp_app.Homesite_Acres,
                Road_Waste_Pond_Acres=temp_app.Road_Waste_Pond_Acres,
                CRP_Acres=temp_app.CRP_Acres,
                Con25_Acres=temp_app.Con25_Acres,
                Other_Use_Acres=temp_app.Other_Use_Acres,
                Stated_Total_Acres=temp_app.Stated_Total_Acres,
                Farmed_Acres_1=temp_app.Farmed_Acres_1,
                Farmed_Acres_2=temp_app.Farmed_Acres_2,
                Farmed_Acres_3=temp_app.Farmed_Acres_3,
                Use_of_Land_1=temp_app.Use_of_Land_1,
                Use_of_Land_2=temp_app.Use_of_Land_2,
                Use_of_Land_3=temp_app.Use_of_Land_3,
                Units_Acre_1=temp_app.Units_Acre_1,
                Units_Acre_2=temp_app.Units_Acre_2,
                Units_Acre_3=temp_app.Units_Acre_3,
                Price_Unit_1=temp_app.Price_Unit_1,
                Price_Unit_2=temp_app.Price_Unit_2,
                Price_Unit_3=temp_app.Price_Unit_3,
                Gross_Income_1=temp_app.Gross_Income_1,
                Gross_Income_2=temp_app.Gross_Income_2,
                Gross_Income_3=temp_app.Gross_Income_3,
            )
            db.session.add(completed_app)
            db.session.commit()
            return render_template('success.html')
        else:
            app.user = current_user.username
            app.AG_APP = temp_app.AG_APP
            app.Parcel_Change_Check = temp_app.Parcel_Change_Check
            app.Parcels_Combined_Acres = temp_app.Parcels_Combined_Acres
            app.Commodity_Acres = temp_app.Commodity_Acres
            app.Hay_Acres = temp_app.Hay_Acres
            app.Perm_Pasture_Acres = temp_app.Perm_Pasture_Acres
            app.Noncommercial_Wood_Acres = temp_app.Noncommercial_Wood_Acres
            app.Commerical_Wood_Acres = temp_app.Commerical_Wood_Acres
            app.Other_Crop_Acres = temp_app.Other_Crop_Acres
            app.Homesite_Acres = temp_app.Homesite_Acres
            app.Road_Waste_Pond_Acres = temp_app.Road_Waste_Pond_Acres
            app.CRP_Acres = temp_app.CRP_Acres
            app.Con25_Acres = temp_app.Con25_Acres
            app.Other_Use_Acres = temp_app.Other_Use_Acres
            app.Stated_Total_Acres = temp_app.Stated_Total_Acres
            app.Farmed_Acres_1 = temp_app.Farmed_Acres_1
            app.Farmed_Acres_2 = temp_app.Farmed_Acres_2
            app.Farmed_Acres_3 = temp_app.Farmed_Acres_3
            app.Use_of_Land_1 = temp_app.Use_of_Land_1
            app.Use_of_Land_2 = temp_app.Use_of_Land_2
            app.Use_of_Land_3 = temp_app.Use_of_Land_3
            app.Units_Acre_1 = temp_app.Units_Acre_1
            app.Units_Acre_2 = temp_app.Units_Acre_2
            app.Units_Acre_3 = temp_app.Units_Acre_3
            app.Price_Unit_1 = temp_app.Price_Unit_1
            app.Price_Unit_2 = temp_app.Price_Unit_2
            app.Price_Unit_3 = temp_app.Price_Unit_3
            app.Gross_Income_1 = temp_app.Gross_Income_1
            app.Gross_Income_2 = temp_app.Gross_Income_2
            app.Gross_Income_3 = temp_app.Gross_Income_3
            db.session.commit()
            return render_template('success.html')

    return render_template(
        'submit.html',
        land_dict=land_dict,
        income_dict=income_dict,
        app=temp_app,
        old_app=old_app,
        form=form
    )


@app.route('/view/<model>')
@login_required
def view(model):
    if current_user.username == "admin":
        model_dict = {
            "CAUVApp": CAUVApp.query.all(),
            "User": User.query.all()
        }
        rows = model_dict[model]
        return render_template(
            'view.html',
            model=model,
            rows=rows,
        )
    else:
        return redirect('/app_search')

@app.route('/user')
@login_required
def home():
    return 'The Current User is ' + current_user.username
