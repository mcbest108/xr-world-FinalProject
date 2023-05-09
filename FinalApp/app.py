from flask import Flask, render_template, url_for, request
from flask_sqlalchemy import SQLAlchemy
from model import app, User, db


@app.route('/')
def index():
    users = User.query.all()
    return render_template('index.html', users=users)





@app.route('/submit', methods=['GET', 'POST'])
def submit():
    name = request.form['name']
    email = request.form['email']
    message = request.form['message']
    print(request.form['name'])
    print(request.form['email'])
    print(request.form['message'])

    user = User(name=name, email=email, message=message)
    db.session.add(user)
    db.session.commit()

    return 'Information submitted successfully! <br> <h3>Go back to last page, scroll to the bottom of the page to the USER section, AND REFRESH PAGE to see your submission'



if __name__ == '__main__':
    with app.app_context():
        db.create_all()
    app.run(debug=True)