import numpy as np
import pandas as pd
import os,sys
from src.logger import logging
from src.exception import CustomException
from dataclasses import dataclass
from sklearn.model_selection import train_test_split

## Data ingestion COnfig:
@dataclass
class DataIngestionConfig:
    train_data_path=os.path.join('artifacts','train.csv')
    test_data_path=os.path.join('artifacts','test.csv')
    raw_data_path=os.path.join('artifacts','raw.csv')
    
    
## Create a data ingestion class:
class DataIngestion:
    def __init__(self):
        self.ingestion_config=DataIngestionConfig()
        
    def initiate_data_ingestion(self):
        logging.info('Data Ingestion mwthod is started')
        
        try:
            df=pd.read_csv(os.path.join('notebook/data','final_model_data.csv'))
            logging.info('Datasets read as pandas DataFrame')
            
            os.makedirs(os.path.dirname(self.ingestion_config.raw_data_path),exist_ok=True)
            df.to_csv(self.ingestion_config.raw_data_path,index=False)
            logging.info('Dataset save as raw.csv file')
            
            logging.info('Train test Split starte')
            
            train_set,test_set=train_test_split(df,test_size=0.20,random_state=42)
            train_set.to_csv(self.ingestion_config.train_data_path,index=False)
            test_set.to_csv(self.ingestion_config.test_data_path,index=False)
            
            logging.info('ingestion of Data is completed')
            
            return(
                self.ingestion_config.train_data_path,
                self.ingestion_config.test_data_path
            )       

        except Exception as e:
            logging.info('Some Error Occured into data ingestion class')
            raise CustomException(e,sys)