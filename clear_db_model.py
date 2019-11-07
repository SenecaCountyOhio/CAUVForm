from application import db, login_manager, create_app
from application.models import User, CAUVApp, PreviousCAUVApp, TempCAUVApp
import sys


def delete_model(dict, argument):
    return db.session.query(dict[argument]).delete()


app = create_app()
app.app_context().push()
model_dict = {
    'User': User,
    'CAUVApp': CAUVApp,
    'PreviousCAUVApp': PreviousCAUVApp,
    'TempCAUVApp': TempCAUVApp
}
delete_model(
    dict=model_dict,
    argument=str(sys.argv[1])
)
db.session.commit()
