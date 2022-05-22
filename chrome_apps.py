# -*- coding: utf-8 -*-
"""
Created on Sun May 22 09:41:19 2022

@author: Rajesh
"""


import pandas as pd

df = pd.read_csv("C:/Users/HP/Desktop/chrome_reviews.csv")

import numpy as np
df_NA = df.dropna(how = 'all')
#df[df['Star'] != 3]
#df_NA.keys()
df_NA['Positivity'] = np.where(df_NA['Star'] > 3, 1, 0)
cols = ['ID', 'Star', 'Review URL', 'Thumbs Up', 'User Name', 'Developer Reply', 'Version','Review Date', 'App ID']
df_NA.drop(cols, axis=1, inplace=True)

import re
import nltk
nltk.download('stopwords')
from nltk.corpus import stopwords
from nltk.stem.porter import PorterStemmer



# Initialize empty array
# to append clean text
corpus = []
num = len(df_NA)

df_NA['Text'] = df_NA['Text'].astype(str)
# (reviews) rows to clean
for i in range(0, num):
	
	# column : "Text", row ith
	review = re.sub('[^a-zA-Z]', ' ', df_NA['Text'][i])
	
	# convert all cases to lower cases
	review = review.lower()
	
	# split to array(default delimiter is " ")
	review = review.split()
	
	# creating PorterStemmer object to
	# take main stem of each word
	ps = PorterStemmer()
	
	# loop for stemming each word
	# in string array at ith row
	review = [ps.stem(word) for word in review
				if not word in set(stopwords.words('english'))]
				
	# rejoin all string array elements
	# to create back into a string
	review = ' '.join(review)
	
	# append each string to create
	# array of clean text
	corpus.append(review)

from sklearn.feature_extraction.text import CountVectorizer
cv = CountVectorizer(max_features = 1000)
X = cv.fit_transform(corpus).toarray()
y = df_NA.iloc[:, 1].values

# train a random forest model to perform classification as positive or negative review
from sklearn.model_selection import train_test_split
x_train, x_cv, y_train, y_cv = train_test_split(X, y, test_size = 0.20)
from sklearn.ensemble import RandomForestClassifier
model = RandomForestClassifier(n_estimators = 350,criterion = 'entropy')
                             
model.fit(x_train, y_train)

from sklearn.metrics import accuracy_score
pred_cv = model.predict(x_cv)
accuracy_score(y_cv,pred_cv)

pred_train = model.predict(x_train)
accuracy_score(y_train,pred_train)

import pickle 
pickle_out = open("classifier.pkl", mode = "wb") 
pickle.dump(model, pickle_out) 
pickle_out.close()


import pandas as pd
import numpy as np
import pickle
import streamlit as st
from PIL import Image
  
# loading in the model to predict on the data
pickle_in = open('classifier.pkl', 'rb')
classifier = pickle.load(pickle_in)


def prediction(Text,Positivity):  
   
    prediction = classifier.predict(
        [[Text,Positivity]])
    print(prediction)
    return prediction


# this is the main function in which we define our webpage 
def main():
      # giving the webpage a title
    st.title("chrome reviews")
      
   
    html_temp = """
    <div style ="background-color:yellow;padding:13px">
    <h1 style ="color:black;text-align:center;">Streamlit chrome reviews ML App </h1>
    </div>
    """
      
   
    st.markdown(html_temp, unsafe_allow_html = True)
      
   
    Text_ = st.text_input("Text", "Type Here")
    Positivity_ = st.text_input("Positivity", "Type Here")
    result =""
      
    
    if st.button("Predict"):
        result = prediction(Text_,Positivity_)
    st.success('The output is {}'.format(result))
     
if __name__=='__main__':
    main()
  




















