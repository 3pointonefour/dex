from flask import request, render_template
#import all necessary model variables from app
from loadmodel import model, vectorizer

import numpy as np

from preProcessing import clean_reviews
from app import app #This line exists for the server routing 

@app.route('/predict', methods=['POST'])
def predict():
    if request.method == 'POST':
        rev = request.form['rev']


        print("\n\n\ninput ->", rev, type(rev))
        clean_review = clean_reviews(str(rev))
        print("clean_review->", clean_review)

        vectorised_review = vectorizer.transform(np.array([clean_review]))
        print("vector->\n", vectorised_review)

        print('model input shape', vectorised_review.shape)
        prediction = model.predict(vectorised_review)

        pred = ['Negative','Postive'][prediction[0]]

        return render_template("pred.html", value=pred)