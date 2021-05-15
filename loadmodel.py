import pickle

from app import modelLocation

#Loading model
model = pickle.load(open(modelLocation, 'rb'))
vectorizer = pickle.load(open('vect.pkl','rb'))