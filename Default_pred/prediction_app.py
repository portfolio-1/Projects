import numpy as np
from flask import Flask, request, jsonify, render_template
import pickle
import joblib

app=Flask(__name__,template_folder='templates')
model = pickle.load(open('model.pkl','rb'))

cols = ["Target", "Predicted_probability"]

@app.route('/')
def home():
    return render_template("home.html")

@app.route('/predict', method=['POST'])
def predict():
    int_feature = [X for X in request.form.values()]
    final = np.array(int_features)
    data_unseen = predict_model(model, data=data_unseen, round=0)
    prediction = int(prediction.label[0])
    
    return render_template('home.html',pred='Expected Bill will be{}'.format(prediction))