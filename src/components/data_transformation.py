import numpy as np
import pandas as pd
import os
import sys
from src.logger import logging
from src.exception import CustomException
from sklearn.impute import SimpleImputer
from sklearn.preprocessing import StandardScaler
from sklearn.preprocessing import OneHotEncoder
from sklearn.compose import ColumnTransformer
from sklearn.pipeline import Pipeline
from dataclasses import dataclass
from src.utils import save_object


## Data Transformation Config:
@dataclass
class DataTransformationConfig:
    preprocessor_obj_file_path=os.path.join('artifacts','preprocessor.pkl')


## Data Transformation class:
@dataclass
class DataTransformation:
    def __init__(self):
        self.data_transformation_config=DataTransformationConfig()
    
    def get_data_transformation_object(self):
        try:
            numerical_column=['Blood_Pressure_systolic',
                'Blood_Pressure_diastolic',
                'Heart_Rate',
                'Respiratory_Rate',
                'Temperature_Celsius',
                'Glucose_Level',
                'Cholesterol_Level',
                'Diagnosis_Code',
                'Age',
                'Oxygen_Saturation']
            categorical_column=['Gender']
            
            ## Numerical pipeline:
            num_pipeline=Pipeline(
        steps=[
        ('Imputer',SimpleImputer(strategy='median')),
        ('Scaler',StandardScaler())
        ])
        
            ## Categorical Pipeline:    
            cat_pipeline = Pipeline(
        steps=[
        ('Imputer', SimpleImputer(strategy='most_frequent')),
        ('Encoder', OneHotEncoder(handle_unknown='ignore')),
        ('Scaler', StandardScaler(with_mean=False))  # with_mean=False because one-hot encoded data is sparse
            ])
            
            logging.info('Preprocessor Pipeline Creation started')
            preprocessor=ColumnTransformer([
            ('numerical_pipeline',num_pipeline,numerical_column),
            ('categorical_pipeline',cat_pipeline,categorical_column)
            ])
            
            return preprocessor     
    
        except Exception as e:
            logging.info('Some Error occured into Data Transformation class')
            raise CustomException(e,sys)
        
    def initiate_data_transformation(self,train_data_path,test_data_path):
        try:
            train_df=pd.read_csv(train_data_path)
            test_df=pd.read_csv(test_data_path)
            logging.info('Read train and test data completed')
            logging.info(f"Train DataFrame Head :\n {train_df.head().to_string()}")
            logging.info(f"Test DataFrame Head :\n {test_df.head().to_string()}")
            
            logging.info('Obtaining preprocessing object')
            
            preprocessing_obj=self.get_data_transformation_object()
            
            target_column_name='Diagnosis'
            drop_columns=[target_column_name,'Unnamed: 0','Patient_ID','Date_of_Birth']
            
            # Feature devide  into independet and depedent features
            input_feature_train_df=train_df.drop(columns=drop_columns,axis=1)
            target_feature_train_df=train_df[target_column_name] 


            input_feature_test_df=train_df.drop(columns=drop_columns,axis=1)
            target_feature_test_df=train_df[target_column_name] 
            
            ## apply the transformation
            input_feature_train_arr=preprocessing_obj.fit_transform(input_feature_train_df)
            input_feature_test_arr=preprocessing_obj.fit_transform(input_feature_test_df)
            
            logging.info("Applying preprocessing object on training and testing datsets.")
            
            
            train_arr=np.c_[input_feature_train_arr,np.array(target_feature_train_df)]
            test_arr=np.c_[input_feature_test_arr,np.array(target_feature_test_df)]
            
            save_object(
                file_path=self.data_transformation_config.preprocessor_obj_file_path,
                obj=preprocessing_obj
                )
            
            logging.info("Preprocessor pickle in create and saved")
            
            return (
                train_arr,
                test_arr,
                self.data_transformation_config.preprocessor_obj_file_path
            )

        except Exception as e:
            logging.info('Some Error occured into initiate_data_transformation method')
            raise CustomException(e,sys)