# Little Flask App for KMD interview

from flask import Flask, render_template, request

# ML Model
import sklearn
import pandas as pd
import numpy as np
import joblib

app = Flask(__name__)
model = joblib.load("./bestmodel.joblib")
data = pd.read_csv("testDataForModel.csv")

@app.route('/', methods=['GET'])

def startScreen():
    return render_template('index.html')

@app.route('/', methods=['POST', 'GET'])

def predict():
    # ML Algo Prediction
    index = request.form.get("idx", type=int)
    
    prediction = model.predict(data[index:index+1])
    pred_price = '%s %.2f' % ("Bulldozer Sales Price is predicted to ", prediction)

    salesID = data.SalesID[index:index+1]
    #salesIDformatted = int(salesID)
    salesIDformatted = '%s %d' % ("for Sales ID is ", salesID)
    

    return render_template('index.html', prediction=pred_price, salesID=salesIDformatted)


if __name__ == '__main__':
    app.run(port=3000, debug=True)