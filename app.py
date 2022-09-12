from flask import Flask, request, redirect
from flask.templating import render_template
from flask_sqlalchemy import SQLAlchemy

app = Flask(__name__)
app.debug = True

app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///site.db'
db= SQLAlchemy(app)

class currentlocation(db.Model):
    #vehicleno which is unique to each
    #driver_name driver of particular vehicle
    #latitude and longitude which gives the present location of the vehicle
    #timestamp which gives current time
    #acceleration gives acceleration at a particular instant
    vehicle_no = db.Column(db.String(11) , primary_key=True)
    driver_name = db.Column(db.String(50),unique=False,nullable=False)
    latitude = db.Column(db.String(10),unique=False,nullable=False)
    longitude = db.Column(db.String(10),unique=False,nullable=False)
    timestamp = db.Column(db.DateTime,nullable=False) 
    acceleration = db.Column(db.Float)
    
    def __repr__(self):
        return f"currentlocation:{self.vehicle_no}, Driver:{self.driver_name}"
@app.route("/")
def index():
    vehicles = currentlocation.query.all()
    return render_template('index.html',vehicles=vehicles)

@app.route('/add_data')
def add_data():
    return render_template('add_vehicle.html')

@app.route('/add', methods=["POST"])
def vehicle():
    vehicle_no = request.form.get("vehicle_no")
    driver_name = request.form.get("driver_name")
    latitude = request.form.get("latitude")
    longitude = request.form.get("longitude")
    timestamp = request.form.get("timestamp")
    acceleration = request.form.get("acceleration")
    if vehicle_no!='' and driver_name!='' and latitude!='' and longitude!='' and timestamp!='' and acceleration is not None:
        p=currentlocation(vehicle_no=vehicle_no,driver_name=driver_name,latitude=latitude,longitude=longitude,timestamp=timestamp,acceleration=acceleration)
        db.session.add(p)
        db.session.commit()
        return redirect('/')
    else:
        return redirect('/')

@app.route('/delete/<int:vehicle_no>')
def erase(vehicle_no):
    data=currentlocation.query.get(vehicle_no)
    db.session.delete(data)
    db.session.commit()
    return redirect('/')
       
if __name__ =='__main__':
    app.run()

from flask_migrate import Migrate, migrate
migrate=Migrate(app,db)
