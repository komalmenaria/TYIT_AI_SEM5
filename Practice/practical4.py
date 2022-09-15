# Step 1 import modules 6
import numpy as np
import pandas as pd
import csv
from pgmpy.models import BayesianNetwork
from pgmpy.estimators import MaximumLikelihoodEstimator
from pgmpy.inference import VariableElimination 
# Step 2 get data 

heartdisease = pd.read_csv('heart.csv')
heartdisease = heartdisease.replace('?',np.nan)


# Step 3 print data and datatype 

# Step 4 Creating model and tell them which data have to use 
# Step 5 Inferencing the basiyan network 
# Step 6 print probability on evidence 1 and 2 
 