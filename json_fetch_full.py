#!flask/bin/python

import sys

from flask import Flask, render_template, request, redirect, Response
import random, json
from flask_cors import CORS
import pandas as pd
import numpy as np
from xgboost import XGBClassifier,XGBRegressor
from sklearn.model_selection import train_test_split
from sklearn.metrics import accuracy_score
from sklearn.metrics import explained_variance_score
from sklearn.model_selection import GridSearchCV

from sklearn.model_selection import StratifiedKFold, RepeatedKFold
from sklearn.model_selection import cross_val_score
from numpy import mean
from numpy import std

print("starting")


app = Flask(__name__)
CORS(app)

@app.route('/')
def output():
	# serve index template
	return render_template('index.html', name='pyml')

@app.route('/receiver', methods = ['POST'])
def worker():
	# read json + reply
	data = request.get_json(force=True)
	# print(request.status_code)
	result = '77.8'
	print(data)
	# for item in data:
	# 	# loop over every row
	# 	result = item['blood_pressure']
	# print(result)	

	# # start
	# obs_data = pd.read_excel('fhir_Observation_data.xlsx')
	# obs_transform = obs_data.pivot_table(values = 'obs_value', index = 'patient_name', columns='obs_name',aggfunc='mean',)
	# obs_transform.columns = obs_transform.columns.str.replace('.','_').str.replace("/","_")
	# select_col = obs_transform.notnull().sum().sort_values(ascending=False)[0:11].index
	#
	# select_obs = obs_transform[select_col]
	# model = XGBRegressor(booster='gbtree',objective='reg:squarederror',larning_rate = 0.0001, \
	# 					 max_depth = 2, min_child_weight = 1, n_estimators = 50, subsample = 0.4)
	# X = select_obs.drop(['Body Weight','Body Mass Index'], axis=1)
	# y = select_obs['Body Weight']
	# y.replace(np.NaN,y.mean(),inplace=True)
	# model.fit(X, y)
	# # end
	print(model)
	prod_ds = pd.DataFrame(data)
	prod_col = prod_ds.columns
	for col in prod_col:
   	    prod_ds[col] = prod_ds[col].astype(float)
	y_pred = model.predict(prod_ds)
	print(y_pred[0])
	print(str(round(y_pred[0],2)), str(zip(prod_ds.columns, model.feature_importances_)))
	return (str(round(y_pred[0],2)) + ' Feature Importances: ' + \
			str('\n' * 2) + str(list(zip(prod_ds.columns, model.feature_importances_))))



if __name__ == '__main__':
	# run!
	print('In Main fuction')
	# start
	obs_data = pd.read_excel('fhir_Observation_data.xlsx')
	obs_transform = obs_data.pivot_table(values = 'obs_value', index = 'patient_name', columns='obs_name',aggfunc='mean',)
	obs_transform.columns = obs_transform.columns.str.replace('.','_').str.replace("/","_")
	select_col = obs_transform.notnull().sum().sort_values(ascending=False)[0:11].index

	select_obs = obs_transform[select_col]
	model = XGBRegressor(booster='gbtree',objective='reg:squarederror',learning_rate = 0.1, \
						 max_depth = 2, min_child_weight = 1, n_estimators = 50)
	X = select_obs.drop(['Body Weight','Body Mass Index'], axis=1)
	y = select_obs['Body Weight']
	y.replace(np.NaN,y.mean(),inplace=True)
	model.fit(X, y)
	# end
	app.run()