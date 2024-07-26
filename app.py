from flask import Flask, render_template, request, redirect, url_for
from flask_sqlalchemy import SQLAlchemy # type: ignore

app = Flask(__name__)
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///users.db'
db = SQLAlchemy(app)

class User(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    username = db.Column(db.String(150), nullable=False)
    email = db.Column(db.String(150), unique=True, nullable=False)

@app.route('/')
def home():
    return "Welcome to Home Page!</h>"

@app.route('/admin', methods=['GET', 'POST'])
def admin():
    if request.method == 'POST':
        username = request.form['username']
        email = request.form['email']
        
        print(f"Adding user: {username}, Email: {email}")
        return redirect(url_for('admin'))
    return render_template('admin.html')

if __name__ == '__main__':
    app.run(debug=True) 