# Script for predicting transaction category
# Use: python predict.py <path to .csv file>
# Requirements: .csv file has to have 'Description', 'Amount' and 'Currency' columns
# Results: creates data/results/predictio .csv file

import sys
import pandas as pd
from utils.my_prep import CategoricalEncoder
import pickle
from sklearn.ensemble import RandomForestClassifier

# retrieve path to file
path_to_file = sys.argv[1]
# load data
df = pd.read_csv(path_to_file)

cols_to_check = {'Description', 'Amount', 'Currency'}
assert cols_to_check & set(df) == cols_to_check

# load prep models
with open('models/enc.pickle', 'rb') as file:  
    enc = pickle.load(file) 
    
with open('models/fillna.pickle', 'rb') as file:  
    fillna = pickle.load(file) 
    
with open('models/tf_idf.pickle', 'rb') as file:  
    tf_idf = pickle.load(file) 
    
with open('models/rf.pickle', 'rb') as file:  
    rf = pickle.load(file) 

# apply data prep
# fillna
for col in fillna.keys():
    df.loc[df[col].isna(), col] = fillna[col]
# encode categories
for c in enc.columns:
    enc.encode(df, c)
# get features from Description
tf_idf_matr = tf_idf.transform(df['Description'])

df_tf_idf = pd.DataFrame(tf_idf_matr.toarray(), columns=tf_idf.get_feature_names_out())

df_concat = pd.concat([df, df_tf_idf], axis=1)
df_concat.drop(columns=['Description'], inplace=True)
# predict
y_pred = rf.predict(df_concat.drop(columns='Category'))
df['Predicted Categoory'] = y_pred
# save
df.to_csv('data/results/prediction.csv')




