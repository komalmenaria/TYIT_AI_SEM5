# bayesian network
# Step 1 import packages 6
import numpy as np
import pandas as pd
import csv
from pgmpy.estimators import MaximumLikelihoodEstimator
from pgmpy.models import BayesianNetwork
from pgmpy.inference import VariableElimination
# Step 2 get dataset 
heartdisease = pd.read_csv('heart.csv')
heartdisease = heartdisease.replace('?',np.nan)
# Step 3 print data and data attribute
print("Sample instance of data is given below")
print(heartdisease.head())

print("\n Data and Attributes")
print(heartdisease.dtypes)

# Step 4 initalizing model and tell them which data have to use 

model = BayesianNetwork([('age','heartdisease'),('sex','heartdisease'),('exang','heartdisease'),
                         ('cp','heartdisease'),('restecg','heartdisease'),('chol','heartdisease')])
model.fit(heartdisease, estimator=MaximumLikelihoodEstimator)
# Step 5 Inferencing the bayesian network 
print("\n Inferencing the bayesian network ")
heartdiseasetest_infer = VariableElimination(model)

# Step 6 print probability of evidence 1 and 2 

print('\n 1.Probability of HeartDisease given evidence=restecg:1')
q1=heartdiseasetest_infer.query(variables=['heartdisease'],evidence={'restecg':1})
print(q1)

  
print('\n 2.Probability of HeartDisease given evidence= cp:2 ')  
q2=heartdiseasetest_infer.query(variables=['heartdisease'],evidence={'cp':2})
print(q2)