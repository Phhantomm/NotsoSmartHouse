from flask import Flask, jsonify, redirect, url_for, render_template, request, session, flash
import requests
import json

from flask_sqlalchemy import SQLAlchemy

app = Flask(__name__)
app.config['SECRET_KEY'] = 'pythonwork'
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///UserInfo.sqlite'
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False  
db = SQLAlchemy(app)

with app.app_context():
    db.create_all()

class UserInfo(db.Model):
    id = db.Column(db.Integer, primary_key=True, autoincrement=True)
    name = db.Column(db.String(80), nullable=False)
    surname = db.Column(db.String(80), nullable=False)
    telephone = db.Column(db.Float, nullable=False)

    def __init__(self, name, surname, telephone):
        self.name = name
        self.surname = surname
        self.telephone = telephone

@app.route('/', methods=['GET','POST'])
def home():
    return render_template('index.html')

@app.route('/product', methods=['GET', 'POST'])
def product():
    if request.method == 'POST':
        name = request.form['name']
        surname = request.form['surname']
        telephone = request.form['telephone']
        
        # Create a new UserInfo object and store it in the database
        user = UserInfo(name=name, surname=surname, telephone=telephone)
        with app.app_context():
            db.create_all()
            db.session.add(user)
            db.session.commit()
        
        # return jsonify({'message': 'Order placed successfully'})
        return redirect(url_for('delivery'))

    # Render the product.html template for GET requests
    return render_template('product.html')


@app.route('/profile')
def user():
    return render_template('user.html')


@app.route('/youshallnotpass')
def youshouldnthavedonethat():
    return render_template('youshouldnthavedonethat.html')

@app.route('/delivery', methods=['GET', 'POST'])
def delivery():
    
    return render_template('delivery.html')

@app.route('/search', methods=['GET'])
def search():
    query = request.args.get('query')

    if query == 'windows':
        return redirect(url_for('windows'))
    elif query == 'secret2':
        return redirect(url_for('secret'))
    else:
        flash('YOU SHANT PASS')
        return render_template('index.html')
    
@app.route('/windows')
def windows():
    return render_template('windows.html')

@app.route('/secret')
def secret():
    return render_template('secret.html')

@app.route('/confession')
def confession():
    return render_template('confession.html')



if __name__ == "__main__":
    app.run(debug=True)


#http://nsshouse.pythonanywhere.com
