from flask import Flask,redirect,url_for,render_template,request
from flask_sqlalchemy import SQLAlchemy


app=Flask(__name__)
app.config['SECRET_KEY']= 'ADKADKFJ'
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///test.db'


db = SQLAlchemy(app)


class Booking():
        id = db.Column(db.Integer, primary_key=True)
        name = db.Column(db.String())
        phonenumber = db.Column(db.String())
        course = db.Column(db.String())
        level = db.Column(db.String())
        singlebooking = db.Column(db.String())
        numberofbooking = db.Column(db.String())
        date = db.Column(db.String())
        room = db.Column(db.String())
        bed = db.Column(db.String())
        def __repr__(self):
            return f"Course('{self.id}', {self.name}', {self.phonenumber}')"






@app.route('/',methods=['GET','POST'])
def home():
    if request.method=='POST':
        # Handle POST Request here
        return render_template('index.html')
    return render_template('index.html')





if __name__ == '__main__':
    #DEBUG is SET to TRUE. CHANGE FOR PROD
    app.run(host="0.0.0.0", port=5000,debug=True)