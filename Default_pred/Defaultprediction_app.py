
#Import libraries
import numpy as np
from flask import Flask, request, jsonify, render_template
#import pickle
import joblib

app=Flask(__name__,template_folder='templates')

# Load the model
model = joblib.load(open('model.pkl','rb'))

@app.route('/')
def home():
    return render_template('home.html')


@app.route('/api',methods=['POST'])
def predict():
    # Get the data from the POST request.
    datas = request.get_json(force=True)

    # Make prediction using model loaded from disk
    pred=[]
    for data in datas:
        prediction = model.predict([np.array([data['Probability'], data['Predicted_probability']])])

        # Take the first value of prediction
        output = int(prediction[0])
        out = "Defaulter" if output == 1 else "Repayer"
        pred.append(out)
        
    return jsonify(pred)