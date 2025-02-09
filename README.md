<h1>Car Dekho Price Prediction</h1>

<h3>Objective</h3><a id="1"></a>
<p>In this project, the objective is to predict Car Selling Price on various features like Car's Present_Price, Kms_Driven, Owner, Fuel_Type, Seller_Type, Transmission. We will use the CAR DEKHO dataset from Kaggle. This dataset contains information about used cars listed on <a href='www.cardekho.com'><u>website</u></a></p>

<h3>Quick Demo</h3><a id="2"></a>

![demo_gif](https://github.com/Prasad14-hub/Car_Price_Prediction/blob/main/demo_gif.gif)

<br><p>We can predict Car Selling Price by filling the data over UI and after that prediction will be displayed over UI.</p>

<h3>Dataset Prview</h3><a id="3"></a>
A preview of top ten rows of the Car Dekho dataset.


| | Car_Name | Year | Selling_Price | Present_Price | Kms_Driven | Fuel_Type | Seller_Type | Transmission | Owner |
|-| -------- | ---- | ------------- | ------------- | ---------- | --------- | ----------- | ------------ | ----- |
|0| Maruti Alto Std | 2012 | 1.2 Lakh* | null | 120000 | Petrol | Individual | Manual | First Owner |
|1| Hyundai Grand i10 Asta | 2016 | 5.5 Lakh* | 7.11-7.48 Lakh* | 20000 | Petrol | Individual | Manual | First Owner |
|2| Hyundai i20 Asta | 2010 | 2.15 Lakh* | null | 60000 | Petrol | Individual | Manual | First Owner |
|3| Maruti Alto K10 VXI | 2012 | 2.26 Lakh* | null | 37000 | Petrol | Individual | Manual | First Owner |
|4| Ford Ecosport 1.5 TDCi Titanium BSIV | 2015 | 5.7 Lakh* | 10.14-13.79 Lakh* | 30000 | Diesel | Dealer | Manual | First Owner |
|5| Maruti Wagon R VXI BS IV | 2013 | 3.5 Lakh* | 5.16-6.94 Lakh* | 35000 | Petrol | Individual | Manual | First Owner |
|6| Hyundai i10 Sportz 1.2 | 2013 | 3.15 Lakh* | 6.54-6.63 Lakh* | 40000 | Petrol | Dealer | Manual | First Owner |
|7| Maruti Wagon R VXI | 2018 | 4.1 Lakh* | 5.26-7.01 Lakh* | 17512 | Petrol | Dealer | Manual | First Owner |
|8| Hyundai Venue SX Plus Turbo DCT BSIV | 2019 | 10.5 Lakh* | 7.70-13.02 Lakh* | 20000 | Petrol | Individual | Automatic | First Owner |
|9| Mahindra TUV 300 T6 | 2017 | 5.75 Lakh* | null | 70000 | Diesel | Dealer | Manual | First Owner |

<h3>Description of variables in the dataset</h3><a id="4"></a>
Above dataset contains information about used cars listed on <a href='https://www.cardekho.com/'><u>website</u></a>. This data can be used for a lot of purposes such as car price prediction using Machine Learning algorithms.
The columns in the given dataset are as follows:

```Car_Name:``` Name of Car sold

```Year:``` Year in which car was bought

```Selling_Price:``` Price at which car sold

```Present_Price:``` Price of same car model in current year 

```Kms_Driven:``` Number of Kilometers Car driven before it is sold

```Fuel_Type:``` Type of fuel Car uses

```Seller_Type:``` Type of seller 

```Transmission:``` Gear transmission of the car (Automatic / Manual)

```Owner:``` Number of previous owners 
 
<h3>Car Price Prediction directory tree</h3><a id="5"></a>

```
├─ Templates
│  └─ index.html
│
├─ app.py
│
├─ demo_gif.gif
│
├─ rf_Model.pkl
│  
├─ Car_Price_Prediction.ipynb
│  
├─ car_data.csv
│
├─ Procfile
│
├─ README.md 
│
└─ requirements.txt
    
```
    
```Templates``` : contains templates for UI

```app.py``` : Front and back end portion of the web application

```Car_Price_Prediction.ipynb``` : conatains ipynb file (Jypiter Notebook file)

```rf_Model.pkl```  : contains model for prediction

```requirements.txt``` : required libraries 

```car_data.csv```  : conatins raw data as csv file

<h3>Installation</h3><a id=""></a>

* Clone this repository and unzip it.

* create new env with python 3 and activate it .

* Install the required packages using pip install -r requirements.txt

* Execute the command: python app.py

* Open ```http://127.0.0.1:5000/``` in your browser.
