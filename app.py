from flask import Flask, render_template, request
import pickle


import argparse

#custom files
from errorClass import NoModelPath
from prediction import predict
###cli arg parser
parser = argparse.ArgumentParser()
parser.add_argument("-p", "--modelpath", \
                help="Path for Model.pkl file, has to include the model.pkl in the file path", \
                type=str)
args = parser.parse_args()

modelLocation = args.modelpath

if(modelLocation == None):
    raise NoModelPath('please insert flag -p and path for model.pkl file, including the model.pkl')
    #pass
else: 
    print ("\n\n\nmodelLocation ->", modelLocation, type(modelLocation), "\n\n\n")



app = Flask(__name__, static_url_path='',
            static_folder='',)
print("prev static path",app._static_folder)

model = pickle.load(open(modelLocation, 'rb'))
vectorizer = pickle.load(open('vect.pkl','rb'))


@app.route("/home")
@app.route("/")
def home():
    return render_template('home.html')

@app.route('/predict', methods=['POST'])
def predict1():
    return predict(model, vectorizer)

if __name__ == '__main__':
    app.run()





