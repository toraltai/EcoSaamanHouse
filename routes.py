from flask import Blueprint, render_template, request, redirect,flash
from utils.boto import *
from utils.extensions import db, allowed_file
import os
from models import File


main = Blueprint('main', __name__)


@main.route('/', methods=['GET','POST']) 
def upload():
    image_files = [file.url for file in File.query.with_entities(File.url).all()]
    if request.method == 'POST':
        if not request.files['file']:
            flash("error")
            return redirect(request.url)
        
    uploaded_files = request.files.getlist('file')
    bucket = config('BUCKET')
    
    for file in uploaded_files:
        if file and allowed_file(file.filename):
            s3.upload_fileobj(file, config('BUCKET'), file.filename)
            file = File(filename = file.filename,
                        url = f'https://{bucket}.s3.eu-north-1.amazonaws.com/{file.filename}')
            db.session.add(file)
            db.session.commit()
        return redirect(request.url)

    return render_template('index.html', image_files=image_files)


@main.route('/after')
def after():
    image_files = os.listdir('static/media')
    return render_template('after.html', image_files=image_files)


@main.route('/test')
def ping():
    return get_bucket()