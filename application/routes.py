from flask import redirect, render_template, flash, request, session, url_for
from flask_login import login_required, logout_user, current_user, login_user
from flask import current_app as app
from werkzeug.security import generate_password_hash, check_password_hash
from .forms import SigninForm, SignupForm, AppSearch, CAUVForm
from .models import db, User, CAUVApp, PreviousCAUVApp
from . import login_manager


@login_manager.user_loader
def load_user(user_id):
    """Check if user is logged-in on every page load."""
    if user_id is not None:
        return User.query.get(user_id)
    return None


@app.route('/')
def base():
    return redirect('/signin')


@app.route('/signup', methods=['GET', 'POST'])
@login_required
def signup():
    """Signup Form."""
    signup_form = SignupForm()
    if request.method == 'POST':
        new_user = User(
            username=request.form['email'],
            password=request.form['password']
        )
        db.session.add(new_user)
        db.session.commit()
        return redirect('/signin')
    return render_template('signup.html', form=signup_form)


@app.route('/signin', methods=['GET', 'POST'])
def signin():
    """Login Form."""
    login_form = SigninForm()
    if request.method == 'POST':
        user = User.query.filter(
            User.username == request.form['email']).first()
        if user.password == request.form['password']:
            login_user(user)
            return redirect('/app_search')
    return render_template('signin.html', form=login_form)


@app.route('/logout')
@login_required
def logout():
    logout_user()
    return redirect('/signin')


@app.route('/app_search', methods=['POST', 'GET'])
@login_required
def app_search():
    search_form = AppSearch()
    error = []
    if request.method == 'POST':
        search = request.form['search']
        app = PreviousCAUVApp.query.filter(
            PreviousCAUVApp.AG_APP == search).first()
        if app is None:
            error = ['No Applications Found using ' + search]
        else:
            return redirect(url_for('fillform', id=search))
    return render_template('search.html', error=error, form=search_form)


@app.route('/fillform/<id>', methods=['POST', 'GET'])
@login_required
def fillform(id):
    form = CAUVForm()
    message = ''
    app = PreviousCAUVApp.query.filter(PreviousCAUVApp.AG_APP == id).first()
    land_dict = {
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

    if request.method == 'POST':
        errors = []
        temp_dict = {}
        for each in land_dict:
            if land_dict[each][0] != request.form[each]:
                errors.append(each)
            temp_dict[each] = request.form[each]
        if len(errors) == 0:
            message = "No Errors"
        else:
            message = "The following fields do not match the previous year: " + str(errors)

    return render_template(
        'index.html',
        app=app,
        form=form,
        land_dict=land_dict,
    )


@app.route('/user')
@login_required
def home():
    return 'The Current User is ' + current_user.username
