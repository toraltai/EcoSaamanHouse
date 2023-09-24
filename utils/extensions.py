from flask_sqlalchemy import SQLAlchemy
from flask_admin import Admin

admin = Admin()
db = SQLAlchemy()

ALLOWED_EXTENSIONS = {'pdf', 'png', 'jpg', 'jpeg', 'gif'}

def allowed_file(filename):
    return '.' in filename and \
           filename.rsplit('.', 1)[1].lower() in ALLOWED_EXTENSIONS