from flask import Flask,render_template,request,jsonify
from src.logger import logging
from src.exception import CustomException
import os
import sys
from src.pipelines.prediction_pipeline import CustomData,PredictionPipeline
import json
app=Flask(__name__)

@app.route('/',methods=['GET','POST'])
def index():
    return render_template('index.html')

@app.route('/predict',methods=['GET','POST'])
def prediction():
    if request.method=='POST':
        data=CustomData(
            Gender=(request.form.get('Gender')),
            Blood_Pressure_systolic=int(request.form.get('Blood_Pressure_systolic')),
            Blood_Pressure_diastolic=int(request.form.get('Blood_Pressure_diastolic')),
            Heart_Rate=int(request.form.get('Heart_Rate')),
            Respiratory_Rate=int(request.form.get('Respiratory_Rate')),
            Temperature_Celsius=float(request.form.get('Temperature_Celsius')),
            Glucose_Level=float(request.form.get('Glucose_Level')),
            Cholesterol_Level=int(request.form.get('Cholesterol_Level')),
            Diagnosis_Code=float(request.form.get('Diagnosis_Code')),
            Age=int(request.form.get('Age')),
            Oxygen_Saturation=int(request.form.get('Oxygen_Saturation'))
        )
        logging.info(data)
        final_new_data=data.get_data_as_daraframe()
        
        logging.info(final_new_data)
        predict_pipeline=PredictionPipeline()
        logging.info('prediction pipeline is loaded')
        result= predict_pipeline.predict(final_new_data)
        
        logging.info(f'prediction is Done {result}')
        return render_template('result.html',predicted_disease=result)
        # return render_template('form.html')
    
    else:
        return render_template('index.html')
        # return render_template('form.html')
if __name__=='__main__':
    app.run(debug=True,host='0.0.0.0')