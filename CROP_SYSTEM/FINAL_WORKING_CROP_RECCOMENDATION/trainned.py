import pandas as pd                                                       
from sklearn import preprocessing                                 
from sklearn.ensemble import RandomForestClassifier
import numpy as np      
import joblib

excel = pd.read_excel('Crop.xlsx', header = 0)                           
le = preprocessing.LabelEncoder()                                 
crop = le.fit_transform(list(excel["CROP"]))                                                                                
NITROGEN = list(excel["NITROGEN"])                                         
PHOSPHORUS = list(excel["PHOSPHORUS"])                                    
POTASSIUM = list(excel["POTASSIUM"])                                   
TEMPERATURE = list(excel["TEMPERATURE"])                                 
HUMIDITY = list(excel["HUMIDITY"])
PH = list(excel["PH"])                                                  
RAINFALL = list(excel["RAINFALL"])                                      
features = list(zip(NITROGEN, PHOSPHORUS, POTASSIUM, TEMPERATURE, HUMIDITY, PH, RAINFALL))                    
features = np.array([NITROGEN, PHOSPHORUS, POTASSIUM, TEMPERATURE, HUMIDITY, PH, RAINFALL],dtype=float)                    
features = features.transpose()                                                                              
model=RandomForestClassifier(n_estimators=10)
model.fit(features, crop)     
joblib.dump(model, 'mod.joblib')
loaded_model = joblib.load('mod.joblib')