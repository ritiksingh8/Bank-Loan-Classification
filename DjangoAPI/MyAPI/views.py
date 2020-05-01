from django.shortcuts import render
from . models import approvals
import pickle
from sklearn.externals import joblib
import json
import numpy as np
from sklearn import preprocessing
import pandas as pd
from .forms import ApprovalForm
from keras import backend as K
from keras.models import load_model
from django.contrib import messages
from .apps import MyapiConfig
# Create your views here.

def ohevalue(df):
	ohe_col = ['Dependents', 'ApplicantIncome', 'CoapplicantIncome', 'LoanAmount',
       'Loan_Amount_Term', 'Credit_History', 'Gender_Female', 'Gender_Male',
       'Married_No', 'Married_Yes', 'Education_Graduate',
       'Education_Not Graduate', 'Self_Employed_No', 'Self_Employed_Yes',
       'Property_Area_Rural', 'Property_Area_Semiurban',
       'Property_Area_Urban']

	cat_columns = ['Gender','Married','Education','Self_Employed','Property_Area']

	df_processed = pd.get_dummies(df, columns=cat_columns)

	newdict = {}

	for i in ohe_col:
		if i in df_processed.columns:
			newdict[i] = df_processed[i].values
		else:
			newdict[i] = 0
	newdf = pd.DataFrame(newdict)
	return newdf

# @api_view(["POST"])
def approvereject(unit):
	try:
		mdl = load_model("C:/Users/Ritik/Desktop/Machine Learning Practice/Bank Loan Classification/DjangoAPI/MyAPI/models/model.h5")
		scalers = joblib.load("C:/Users/Ritik/Desktop/Machine Learning Practice/Bank Loan Classification/DjangoAPI/MyAPI/models/scalers.pkl")
		X = scalers.transform(unit)
		y_pred = mdl.predict(X)
		y_pred = (y_pred>0.58)
		newdf = pd.DataFrame(y_pred, columns=['Status'])
		newdf = newdf.replace({True:'Approved', False:'Rejected'})
		K.clear_session()
		return (newdf.values[0][0],X[0])
	except ValueError as e:
		return (e.args[0])


def cxcontact(request):
	if request.method == 'POST':
		form=ApprovalForm(request.POST)
		if form.is_valid():
				myDict = (request.POST).dict()
				df = pd.DataFrame(myDict, index=[0])
				answer = approvereject(ohevalue(df))[0]
				Xscalers = approvereject(ohevalue(df))[1]
				print(Xscalers)
				messages.success(request,'Application Status: {}'.format(answer))
	
	form=ApprovalForm()
				
	return render(request, 'MyAPI/cxform.html', {'form':form})