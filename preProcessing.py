#This file contains code for preprocessing
from bs4 import BeautifulSoup
import re

import nltk
from nltk.corpus import stopwords

nltk.download('stopwords')

def clean_reviews(review):

    review = BeautifulSoup(review, features="html.parser").text

    emotions = re.findall('(?::|;|=)(?:-)?(?:\)|\(|D|P)', review)

    review = re.sub("[^a-zA-Z]", " ", review)

    review = review.lower().split()

    eng_stopwords = set(stopwords.words("english"))
    review = [w for w in review if not w in eng_stopwords]

    review = ' '.join(review + emotions)

    return review