import numpy as np
import pandas as pd
import sys
import os
from src.logger import logging
from src.exception import CustomException
from src.utils import save_object
from src.utils import evaluate_model
from dataclasses import dataclass
from sklearn.linear_model import LogisticRegression
from sklearn.neighbors import KNeighborsClassifier
from sklearn.tree import DecisionTreeClassifier
from sklearn.ensemble import RandomForestClassifier, GradientBoostingClassifier, AdaBoostClassifier, BaggingClassifier
from sklearn.svm import SVC
from sklearn.naive_bayes import GaussianNB, MultinomialNB
from xgboost import XGBClassifier
from lightgbm import LGBMClassifier
from catboost import CatBoostClassifier
from sklearn.metrics import accuracy_score


@dataclass
class ModelTrainerConfig:
    trained_model_file_path=os.path.join('artifacts','model.pkl')
    
class ModelTrainer:
    def __init__(self):
        self.model_trainer_config=ModelTrainerConfig() 
    
    
    def initate_model_training(self,train_array,test_array):
        try:
            logging.info('Splitting Dependent and Independent variables from train and test data')
            X_train, y_train, X_test, y_test = (
                train_array[:,:-1],
                train_array[:,-1],
                test_array[:,:-1],
                test_array[:,-1]
            )
        
            models = {
    "Logistic Regression": LogisticRegression(),
    # "K-Nearest Neighbors": KNeighborsClassifier(),
    # "Decision Tree": DecisionTreeClassifier(),
    # "Random Forest": RandomForestClassifier(),
    # "Support Vector Classifier": SVC(),
    # "Naive Bayes (Gaussian)": GaussianNB(),
    # "Naive Bayes (Multinomial)": MultinomialNB(),
    # "Gradient Boosting": GradientBoostingClassifier(),
    # "AdaBoost": AdaBoostClassifier(),
    # "Bagging Classifier": BaggingClassifier(),
    # "XGBoost Classifier": XGBClassifier(use_label_encoder=False, eval_metric='logloss'),
    # "LightGBM Classifier": LGBMClassifier(),
    # "CatBoost Classifier": CatBoostClassifier(verbose=0)
}

        
            model_report:dict=evaluate_model(X_train,y_train,X_test,y_test,models)
            print(model_report)
            print('\n====================================================================================\n')
            logging.info(f'Model Report : {model_report}')

            # To get best model score from dictionary 
            best_model_score = max(sorted(model_report.values()))

            best_model_name = list(model_report.keys())[
                list(model_report.values()).index(best_model_score)
            ]
            
            best_model = models[best_model_name]

            print(f'Best Model Found , Model Name : {best_model_name} , accuracy Score : {best_model_score}')
            print('\n====================================================================================\n')
            logging.info(f'Best Model Found , Model Name : {best_model_name} , accuracy Score : {best_model_score}')

            save_object(
                file_path=self.model_trainer_config.trained_model_file_path,
                obj=best_model
            )
        
        
        
        except Exception as e:
            logging.info('Some Error occured into Model trainer class')
            raise CustomException(e,sys)
        