from flask import Flask, request, render_template
# from flask_cors import cross_origin
import sklearn
import joblib
import pandas as pd
import Preprocess
import numpy as np

app = Flask(__name__)
model = joblib.load("model/model.h5")
scaler = joblib.load("model/scaler.h5")


@app.route("/")
# @cross_origin()
def home():
    return render_template("index.html")




@app.route("/predict", methods = ["GET", "POST"])
# @cross_origin()
def predict():
    if request.method == "POST":

        # Date 
        date_dep = request.form["Dep_Time"]
        Journey_day = int(pd.to_datetime(date_dep, format="%Y-%m-%dT%H:%M").day)
        Journey_month = int(pd.to_datetime(date_dep, format ="%Y-%m-%dT%H:%M").month)

        # Departure Time
        Dep_hour = int(pd.to_datetime(date_dep, format ="%Y-%m-%dT%H:%M").hour)
        Dep_min = int(pd.to_datetime(date_dep, format ="%Y-%m-%dT%H:%M").minute)


        # Arrival Time
        date_arr = request.form["Arrival_Time"]
        Arrival_hour = int(pd.to_datetime(date_arr, format ="%Y-%m-%dT%H:%M").hour)
        Arrival_min = int(pd.to_datetime(date_arr, format ="%Y-%m-%dT%H:%M").minute)
    

        # Duration
        dur_hour = abs(Arrival_hour - Dep_hour)
        dur_min = abs(Arrival_min - Dep_min)
        
        Feature1 = request.form["Airline"]
        Feature2 = request.form["Additional_Info"]
        Feature3 = request.form["Destination"]
        Feature4 = request.form["Source"]
        Feature5 = request.form["Total_Stops"]
        
        
            
    data = {'Airline' : Feature1, 'Source' : Feature4, 'Destination' : Feature3 , 'Total_Stops': Feature5, 'Additional_Info' : Feature2}
    final_data = Preprocess.get_data(data)
    
    #pred = scaler.transform([final_data])
        
    data = [Journey_day, Journey_month, Dep_hour, Dep_min, Arrival_hour, Arrival_min, dur_hour, dur_min] + final_data    
    
    prediction=model.predict(np.array(data).reshape(1,-1))
        
    #return str(final_data)
    return render_template('index.html',prediction_text="Your Flight Price is EGP. {}".format(prediction))


    #return render_template("index.html")
if __name__ == "__main__":
    app.run(debug=True)