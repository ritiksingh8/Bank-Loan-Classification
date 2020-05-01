from django.apps import AppConfig
from keras.models import load_model
from sklearn.externals import joblib
from tensorflow import Graph, Session



def graphandsession():

	model_graph = Graph()
	with model_graph.as_default():
		tf_session = Session()
		with tf_session.as_default():
			mdl=load_model("C:/Users/Ritik/Desktop/Machine Learning Practice/Bank Loan Classification/DjangoAPI/MyAPI/models/model.h5")

	return (model_graph,tf_session,mdl)


class MyapiConfig(AppConfig):
    name = 'MyAPI'
    scalers=joblib.load("C:/Users/Ritik/Desktop/Machine Learning Practice/Bank Loan Classification/DjangoAPI/MyAPI/models/scalers.pkl")
    model_graph,tf_session,mdl = graphandsession()