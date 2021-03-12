import sqlalchemy
from sqlalchemy.ext.automap import automap_base
from sqlalchemy.orm import Session
from sqlalchemy import create_engine, func
import datetime as dt

# import Flask
from flask import Flask, jsonify

#Database Setup
engine = create_engine("sqlite:///Resources/hawaii.sqlite")

#reflect an existing database into a new model
Base = automap_base()
# reflect the tables
Base.prepare(engine, reflect = True)

# Save references to each table
Measurement = Base.classes.measurement
Station = Base.classes.station

#Create an app
app = Flask(__name__)

#Define what to do when a user hits the index route
@app.route("/")
def home():
    return (
        f"Available Routes:<br/>"
        f"/api/v1.0/precipitation<br/>"
        f"/api/v1.0/stations<br/>"
        f"/api/v1.0/tobs<br/>"
        f"/api/v1.0/enter start date in YYYY-MM-DD format<br/>"
        f"/api/v1.0/enter start date in YYYY-MM-DD format/enter end date in YYYY-MM-DD format<br/>"
    )

@app.route("/api/v1.0/precipitation")
def precipitation():
    # Create our session (link) from Python to the Database
    session = Session(engine)

    #Query all precipitation data
    results = session.query(Measurement.date, Measurement.prcp).all()

    session.close()

    #Create a dictionary from the precipitation data
    precp_data = []
    for date, prcp in results:
        precp_dict = {}
        precp_dict[date] = prcp
        precp_data.append(precp_dict)
        
    return jsonify(precp_data)

@app.route("/api/v1.0/stations")
def stations():
    # Create our session (link) from Python to the Database
    session = Session(engine)

    #Query list of stations
    results = session.query(Station.id, Station.name).all()

    session.close()

    #Create a dictionary from the data
    station_info = []
    for id, name in results:
        station_dict = {}
        station_dict["Station ID"] = id
        station_dict["Station Name"] = name
        station_info.append(station_dict)
    return jsonify(station_info)

@app.route("/api/v1.0/tobs")
def tobs():
    # Create our session (link) from Python to the Database
    session = Session(engine)

    #Find most active station
    active_station = session.query(Station.station,func.count(Measurement.station)).\
        filter(Measurement.station == Station.station).group_by(Measurement.station).\
            order_by(func.count(Measurement.station).desc()).first()
    
    #Calculate date 12 months from last record
    year_ago_date = dt.date(2017,8,23)- dt.timedelta(days = 365)

    #Query temperature observations and corresponding dates
    active_station_data = session.query(Measurement.tobs, Measurement.date).\
        filter(Measurement.station == active_station[0]).filter(Measurement.date>=year_ago_date).all()

    session.close()

    temperature_data =[]
    for tobs, date in active_station_data:
        temp_dict ={}
        temp_dict["Date"] = date
        temp_dict["Temperature"] = tobs
        temperature_data.append(temp_dict)
    return jsonify(temperature_data)

@app.route("/api/v1.0/<start>")
def startdate(start):
    # Create our session (link) from Python to the Database
    session = Session(engine)

    #Find most active station
    results = session.query(func.min(Measurement.tobs), func.max(Measurement.tobs), func.avg(Measurement.tobs)).\
        filter(Measurement.date>=start).all()
        
    session.close()

    startdate = []
    for min, max, avg in results:
        temp_stats = {}
        temp_stats["Average Temperature"] = avg
        temp_stats["Min Temperature"] = min
        temp_stats["Max Temperature"] = max
        temp_stats["Observations Since"] = start
        startdate.append(temp_stats)

    return jsonify(startdate)

@app.route("/api/v1.0/<start>/<end>")
def start_end(start, end):
    # Create our session (link) from Python to the Database
    session = Session(engine)

    #Find most active station
    results = session.query(func.min(Measurement.tobs), func.max(Measurement.tobs), func.avg(Measurement.tobs)).\
        filter(Measurement.date>=start).filter(Measurement.date<=end).all()
    session.close()

    startend = []
    for min, max, avg in results:
        temp_start_end = {}
        temp_start_end["Average Temperature"] = avg
        temp_start_end["Min Temperature"] = min
        temp_start_end["Max Temperature"] = max
        temp_start_end["Observations Start Date"] = start
        temp_start_end["Observations End Date"] = end
        startend.append(temp_start_end)
    return jsonify(startend)

if __name__ == "__main__":
    app.run(debug=True)