import os 
import sys 
import dill
import pickle
import numpy as np 
import pandas as pd 
from src.exception import CustomException 
from sklearn.metrics import r2_score
from sklearn.model_selection import GridSearchCV




def save_object(file_path, obj): 
    try: 
        dir_path = os.path.dirname(file_path)

        os.makedirs(dir_path, exist_ok=True)

        with open(file_path, "wb") as file_obj: 
            dill.dump(obj, file_obj)
    
    except Exception as e: 
        raise CustomException(e)
    

    
def evaluate_model(X_train, y_train, X_test, y_test, models, param):
    try:
        report = {}
        trained_models = {}

        for model_name, model in models.items():
            param_grid = param.get(model_name, {})

            if param_grid:
                gs = GridSearchCV(estimator=model, param_grid=param_grid, cv=3, n_jobs=-1)
                gs.fit(X_train, y_train)
                best_model = gs.best_estimator_
            else:
                best_model = model
                best_model.fit(X_train, y_train)

            # Store trained model
            trained_models[model_name] = best_model

            # Score
            y_test_pred = best_model.predict(X_test)
            report[model_name] = r2_score(y_test, y_test_pred)

        return report, trained_models

    except Exception as e:
        raise CustomException(e)
    
def load_object(file_path): 
    try: 
        with open(file_path,"rb") as file_obj: 
            return dill.load(file_obj)

    except Exception as e: 
        raise CustomException(e)