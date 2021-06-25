from flask import Flask, render_template, request
import jsonify
import requests
import pickle
import numpy as np
import sklearn
import joblib
from sklearn.preprocessing import StandardScaler
app = Flask(__name__)
model = joblib.load('Random_Forest_Model.pkl')
@app.route('/',methods=['GET'])
def Home():
    return render_template('index.html')


standard_to = StandardScaler()
@app.route("/predict", methods=['POST'])
def predict():
    if request.method == 'POST':
        Car_Age=int(request.form['Car_Age'])
        Avg_Price=float(request.form['Avg_Price'])
        Kms_Driven=int(request.form['Kms_Driven'])
        Mileage=float(request.form['Mileage'])
        Max_Power=float(request.form['Max_Power'])
        Engine=float(request.form['Engine'])
        Seats=float(request.form['Seats'])
        Fuel_Type=request.form['Fuel_Type']

        if(Fuel_Type=='Petrol'):
                Fuel_Type_Petrol=1
                Fuel_Type_Diesel=0
                Fuel_Type_LPG=0
        elif(Fuel_Type=='Diesel'):
            Fuel_Type_Petrol=0
            Fuel_Type_Diesel=1
            Fuel_Type_LPG=0
        elif(Fuel_Type=='LPG'):
            Fuel_Type_Petrol=0
            Fuel_Type_Diesel=0
            Fuel_Type_LPG=1
        else:
            Fuel_Type_Petrol=0
            Fuel_Type_Diesel=0
            Fuel_Type_LPG=0

        Car_Age=2021-Car_Age

        Seller_Type=request.form['Seller_Type']
        if(Seller_Type=='Individual'):
            Seller_Type_Individual=1
            Seller_Type_Trustmark_Dealer=0
        elif(Seller_Type=='Trustmark_Dealer'):
            Seller_Type_Individual=0
            Seller_Type_Trustmark_Dealer=1
        else:
            Seller_Type_Individual=0
            Seller_Type_Trustmark_Dealer=0   

        Transmission_Type=request.form['Transmission_Type']
        if(Transmission_Type=='Mannual'):
            Transmission_Type_Mannual=1
        else:
            Transmission_Type_Mannual=0    
        prediction=model.predict([[Avg_Price,Car_Age,Fuel_Type_Diesel,Fuel_Type_Petrol,Fuel_Type_LPG,Kms_Driven,Seller_Type_Individual,Seller_Type_Trustmark_Dealer,Mileage,Max_Power,Engine,Seats,Transmission_Type_Manual]])

        output=round(prediction[0],2)
        if output<0:
            return render_template('index.html',prediction_texts="Sorry you cannot sell this car")
        else:
            return render_template('index.html',prediction_text="You Can Sell The Car at {}".format(output))
    else:
        return render_template('index.html')

if __name__=="__main__":
    app.run(debug=True)