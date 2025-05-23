import numpy as np
import pandas as pd
from src.exception import CustomException
from src.logger import logging
import sys
import os
import pickle
from sklearn.metrics import accuracy_score



def save_object(file_path,obj):
    try:
        dir_path=os.path.dirname(file_path)
        
        os.makedirs(dir_path,exist_ok=True)
        
        with open(file_path,"wb") as file_obj:
            pickle.dump(obj,file_obj)
            
    except Exception as e:
        raise CustomException(e,sys)  
    
def evaluate_model(X_train,y_train,X_test,y_test,models):
    try:
        report = {}
        for i in range(len(models)):
            model = list(models.values())[i]
            logging.info('Fiting our model on given training data')
            model.fit(X_train,y_train)

            ## Predict Testing data
            y_test_pred =model.predict(X_test)

            logging.info('Get accuracy scores for train and test data')
            # train_model_score = accuracy_score(y_train,y_train_pred)
            test_model_score = accuracy_score(y_test,y_test_pred)

            report[list(models.keys())[i]] =  test_model_score

        return report

    except Exception as e:
            logging.info('Exception occured during model training')
            raise CustomException(e,sys)

def load_object(file_path):
    try:
        with open(file_path,'rb') as file_obj:
            return pickle.load(file_obj)
    except Exception as e:
        logging.info('Exception Occured in load_object function utils')
        raise CustomException(e,sys)
    
