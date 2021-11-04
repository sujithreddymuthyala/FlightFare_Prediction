from flask import Flask, jsonify, render_template, request
import os
import numpy
import pickle
from sklearn.ensemble import RandomForestRegressor

app = Flask(__name__)

@app.route("/")
def index():
    return render_template("index.html")

@app.route("/predict",methods=['POST'])

def predict():
    if request.method == 'POST':


        Source = request.form['Source']
        Destination = request.form['Destination']
        Date = request.form['Date']
        Airline = request.form['Airline']
        Stops = int(request.form['Stops'])

        Source = int(Source)

        data=[['Source', 'Destination', 'Date', 'Airline', 'Stops']]

        mdl = pickle.load(open('Flightfare_predict.pkl', 'rb'))

        prediction = mdl.predict(data)
    return render_template('index.html', prediction=prediction)




if __name__ == "__main__":
    app.run(debug=True, port=9457)
