# SQLAlchemy-Challenge

## Climate Analysis and Exploration
Explore the climate database to conduct basic analysis on historical climate data. All of the analysis should be completed using SQLAlchemy ORM queries, Pandas, and Matplotlib.
* Use the hawaii.sqlite and climate_starter.ipynb files to conduct the analysis
* Create an engine to connect to your sqlite database using SQLAlchemy 'create_engine'
* Reflect the tables into classes ('Station' and 'Measurement') using SQLAlchemy 'automap_base()'
* Link Python to the database by creating an SQLAlchemy session (close the session at the end of the analysis)

### Precipitation Analysis
* Find the most recent date in the data set
* Retrieve the last 12 months of precipitation data (based on the previously calculated date)
* Select the 'date' and 'prcp' values
* Load the query results into a Pandas DataFrame and set the index to the date column
* Sort the values by 'date'
* Plot the results using the DataFrame 'plot' method
* Print the summary statistics for the precipitation data

### Station Analysis
* Calculate the total number of stations in the dataset
* Find the most ctive stations - the stations with the most number of recorded observations
   * List the stations and obversation counts in descending order
   * Identify which station id has the highest number of observations
   * Using the most active station id, calculate the min, max, and average temperature
* Retrieve the last 12 months of temperature observation data (note: use the date variables created in the precipitation analysis)
   * Filter by the station with the highest number of observations
   * Find the last 12 months of temperature observations for this station
   * Plot the results in a histogram with 12 bins

## Climate App
Design a Flask API based on the previous analysis
* Use Flask to create the following routes:
   * '/'
      * Home Page
      * List all available routes

   * '/api/v1.0/precipitation'
      * Query 'date' and 'prcp' data and create a dictionary using 'date' as a key and 'prcp' as the value
      * Return the JSON presentation of your dictionary

   * '/api/v1.0/stations'
      * Return a JSON list of stations from the dataset
      
   * '/api/v1.0/tobs'
      * Query the dates and temperature observations of the most active station for the last year of data
      * Return a JSON list of temperature observations for the previous year

   * '/api/v1.0/<start>'
      * Return a JSON list of minimum temperature, the average temperature, and the max temperature for a given start date

   * '/api/v1.0/<start>/<end>'
      * Return a JSON list of minimum temperature, the average temperature, and the max temperature for a records between the start date and end date inclusive


