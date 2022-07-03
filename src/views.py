from flask import Blueprint, render_template, request, redirect, url_for
from . import db
from .models import Comment
from datetime import datetime

main = Blueprint('main', __name__)


@main.route('/', methods=['POST', 'GET'])
def index():
    if request.method == 'POST':

        try:
            new_time = datetime.utcnow()
            new_id = request.form['id']
            new_data = Comment.query.filter_by(id=new_id).first()
            new_data.time_out = new_time
            db.session.commit()
            return redirect(url_for('main.sign_out'))
        except:
            return 'There was an issue adding your task'

    else:
        comments = Comment.query.order_by(Comment.date_in).all()
        return render_template('index.html', comments=comments)


@main.route('/sign')
def sign():
    return render_template('sign.html')


@main.route('/sign_out', methods=['POST', 'GET'])
def sign_out():

    return render_template('sign_out.html')


@main.route('/admin', methods=['POST', 'GET'])
def admin():
    comments = Comment.query.all()
    return render_template('admin.html', comments=comments)


@main.route('/sign', methods=['POST'])
def sign_post():
    name = request.form.get('name')
    floor = request.form.get('floor')
    company = request.form.get('company')
    whom_to_see = request.form.get('whom_to_see')
    comment = request.form.get('comment')
    phone_no = request.form.get('phone_no')

    new_comment = Comment(name=name, comment=comment,
                          floor=floor, company=company, whom_to_see=whom_to_see, phone_no=phone_no)

    db.session.add(new_comment)
    db.session.commit()

    return redirect(url_for('main.index'))


@main.route('/delete/<int:id>')
def delete(id):
    task_to_delete = Comment.query.get_or_404(id)

    try:
        db.session.delete(task_to_delete)
        db.session.commit()
        return redirect('/admin')
    except:
        return 'There was a problem deleting that task'
