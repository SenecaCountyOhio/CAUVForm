from flask import redirect, render_template, flash, request, session, url_for
from flask_login import login_required, logout_user, current_user, login_user
from flask import current_app as app
from werkzeug.security import generate_password_hash, check_password_hash
from .forms import SigninForm, SignupForm, AppSearch, CAUVForm
from .models import db, User, CAUVApp
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
            username = request.form['email'],
            password = request.form['password']
        )
        db.session.add(new_user)
        db.session.commit()
        return redirect('/signin')
        #if signup_form.validate():
        #    flash('Logged in successfully.')
        #    return render_template('/index.html')
    return render_template('signup.html', form=signup_form)

@app.route('/signin', methods=['GET', 'POST'])
def signin():
    """Login Form."""
    login_form = SigninForm()
    if request.method == 'POST':
        user = User.query.filter(User.username == request.form['email']).first()
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
        apps = CAUVApp.query.filter(CAUVApp.AG_APP == search).all()
        if len(apps) == 0:
            error = ['No Applications Found using ' + search]
        else:
            redirect = '/form' + str(apps.AG_APP)
            return redirect(redirect)
    return render_template('search.html', error=error, form=search_form)

@app.route('/form<int:id>', methods=['POST','GET'])
@login_required
def form(id):
    app_form = CAUVForm()
    apps = CAUVApp.query.filter(CAUVApp.AG_APP == id).all()
    if request.method == 'POST':
        pass
    return render_template('index.html', apps=apps, form=app_form)



@app.route('/user')
@login_required
def home():
    return 'The Current User is ' + current_user.username
