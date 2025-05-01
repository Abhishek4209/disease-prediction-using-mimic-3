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
    if request.method=='GET':
        return render_template('form.html')
    
    else:
        data=CustomData(
            Gender=(request.form.get('gender')),
            Blood_Pressure_systolic=float(request.form.get('blood_Pressure_systolic')),
            Blood_Pressure_diastolic=float(request.form.get("blood_Pressure_diastolic")),
            Heart_Rate=float(request.form.get('heart_Rate')),
            Respiratory_Rate=float(request.form.get('respiratory_Rate')),
            Temperature_Celsius=float(request.form.get('temperature_Celsius')),
            Glucose_Level=float(request.form.get('glucose_Level')),
            Cholesterol_Level=float(request.form.get('cholesterol_Level')),
            Diagnosis_Code=float(request.form.get('diagnosis_Code')),
            Age=float(request.form.get('age')),
            Oxygen_Saturation=float(request.form.get('oxygen_Saturation'))
        )

        logging.info(data)
        final_new_data=data.get_data_as_daraframe()
        
        logging.info(final_new_data)
        predict_pipeline=PredictionPipeline()
        logging.info('prediction pipeline is loaded')
        result= predict_pipeline.predict(final_new_data)
        
        logging.info(f'prediction is Done {result}')
        return render_template('form.html',predicted_disease=result)
    
    
if __name__=='__main__':
    app.run(debug=True,host='0.0.0.0')