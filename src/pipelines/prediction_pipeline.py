import numpy as np
import pandas as pd
import sys
import os
from src.logger import logging
from src.exception import CustomException
from src.utils import load_object

class PredictionPipeline:
    def __init__(self):
        pass
    
    def predict(self,features):
        try:
            preprocessor_path=os.path.join('artifacts','preprocessor.pkl')
            model_path=os.path.join('artifacts','model.pkl')
            
            
            preprocessor=load_object(preprocessor_path)
            model=load_object(model_path)
            
            data_scaled=preprocessor.transform(features)
            pred=model.predict(data_scaled)
            
            
            return pred
            
        except Exception as e:
            raise CustomException(e,sys)
            logging.info('Some Error Occured into predict function in Prediction pipelin')
    
class CustomData:
    def __init__(self,
            Gender:str,
            Blood_Pressure_systolic:float,
            Blood_Pressure_diastolic:float,
            Heart_Rate:float,
            Respiratory_Rate:float,
            Temperature_Celsius:float,
            Glucose_Level:float,
            Cholesterol_Level:float,
            Diagnosis_Code:float,
            Age:float,
            Oxygen_Saturation:float
            ):
        self.Gender=Gender
        self.Blood_Pressure_systolic=Blood_Pressure_systolic
        self.Blood_Pressure_diastolic=Blood_Pressure_diastolic
        self.Heart_Rate=Heart_Rate
        self.Respiratory_Rate=Respiratory_Rate
        self.Temperature_Celsius=Temperature_Celsius
        self.Glucose_Level=Glucose_Level
        self.Cholesterol_Level=Cholesterol_Level
        self.Diagnosis_Code=Diagnosis_Code
        self.Age=Age
        self.Oxygen_Saturation=Oxygen_Saturation
        
    
    
    def get_data_as_daraframe(self):
        try:
            custom_data_input_dict={
                
                "Gender":[self.Gender],
                "Blood_Pressure_systolic":[self.Blood_Pressure_systolic],
                "Blood_Pressure_diastolic":[self.Blood_Pressure_diastolic],
                "Heart_Rate":[self.Heart_Rate],
                "Respiratory_Rate":[self.Respiratory_Rate],
                "Temperature_Celsius":[self.Temperature_Celsius],
                "Glucose_Level":[self.Glucose_Level],
                "Cholesterol_Level":[self.Cholesterol_Level],
                "Diagnosis_Code":[self.Diagnosis_Code],
                "Age":[self.Age],
                "Oxygen_Saturation":[self.Oxygen_Saturation]
                
            }
            
            df=pd.DataFrame(custom_data_input_dict)
            logging.info('DataFrame Gathered')
            return df
        
        except Exception as e:
            raise CustomException(e,sys)
            logging.info('Some Error occured into get data as dataframe methods')
            