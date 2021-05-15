from flask import Flask, render_template, request

import argparse
import prediction
#custom files
from errorClass import NoModelPath
from preProcessing import clean_reviews


###cli arg parser
parser = argparse.ArgumentParser()
parser.add_argument("-p", "--modelpath", \
                help="Path for Model.pkl file, has to include the model.pkl in the file path", \
                type=str)
args = parser.parse_args()
### Parsing complete

#Setting -p path as model location to the variable
modelLocation = args.modelpath

#checking for necessary path
# can be regex for pkl file
if(modelLocation == None):
    raise NoModelPath('please insert flag -p and path for model.pkl file, including the model.pkl')
    #pass
else: 
    print ("\n\n\nmodelLocation ->", modelLocation, type(modelLocation), "\n\n\n")

#Setup
#Setting flask app 
app = Flask(__name__, static_url_path='',
            static_folder='',)
print("prev static path",app._static_folder)

#Setting home
@app.route("/home")
@app.route("/")
def home():
    return render_template('home.html')





