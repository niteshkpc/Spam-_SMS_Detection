import streamlit as st
import pickle

import string
import nltk
from nltk.corpus import stopwords
from nltk.stem import PorterStemmer

# Initialize the stemmer outside the function for better performance
ps = PorterStemmer()


def transform_text(text):
    # 1. Lowercase the text
    text = text.lower()

    # 2. Tokenize into words
    words = nltk.word_tokenize(text)

    # 3. Remove non-alphanumeric characters
    alphanumeric_words = []
    for i in words:
        if i.isalnum():
            alphanumeric_words.append(i)

    # 4. Remove stopwords and punctuation
    filtered_words = []
    stop_words = set(stopwords.words("english"))
    for i in alphanumeric_words:
        if i not in stop_words and i not in string.punctuation:
            filtered_words.append(i)

    # 5. Apply stemming
    stemmed_words = []
    for i in filtered_words:
        stemmed_words.append(ps.stem(i))

    # 6. Join back into a single string
    return " ".join(stemmed_words)


tfidf = pickle.load(open('vectorizer.pkl', 'rb'))
model = pickle.load(open('model.pkl', 'rb'))

st.title('Email/SMS Classifier')
input_sms = st.text_area('Enter your message', '')

if st.button('Predict'):


    # 1. Preprocess
    transform_sms = transform_text(input_sms)
    # 2. vectorize
    vector_input = tfidf.transform([transform_sms])
    # 3. predict
    result = model.predict(vector_input)[0]
    # 4. Display
    if result == 1:
        st.header('Spam')
    else:
        st.header('Not Spam')
