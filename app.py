from flask import Flask
from flask_cors import CORS
from utils.extensions import db,admin
from flask_admin.contrib.sqla import ModelView
from models import MyObject, File
from routes import main


app = Flask(__name__)
CORS(app)
app.config["SQLALCHEMY_DATABASE_URI"] = "sqlite:///db.sqlite3"
app.config["SECRET_KEY"] = "mysecret"
db.init_app(app)


admin.init_app(app)
admin.add_view(ModelView(MyObject, db.session))
admin.add_view(ModelView(File, db.session))

app.register_blueprint(main)


def create_database_tables(app):
    with app.app_context():
        db.create_all() 

create_database_tables(app)

if __name__ == '__main__':
    app.run(debug=True)