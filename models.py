from utils.extensions import db

class File(db.Model):
    __tablename__ = 'file'
    
    id = db.Column(db.Integer, primary_key=True)
    filename = db.Column(db.String(100))
    url = db.Column(db.String(250))
    object_id = db.Column(db.Integer, db.ForeignKey('my_object.id'), nullable=True)
    my_object = db.relationship('MyObject', backref=db.backref('files', lazy=True))

class MyObject(db.Model):
    __tablename__ = 'my_object'

    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(50))
    desc = db.Column(db.String(250))

    def __init__(self, name, desc):
        self.name = name
        self.desc = desc
