import pandas as pd
import matplotlib.pyplot as plt

data = pd.read_csv('train.tsv' , sep='\t')

Sentiment_count=data.groupby('Sentiment').count()


#######################################################
#Vectorizing the data using filtered Reg expression to count only english words without symbols and numbers
from sklearn.feature_extraction.text import CountVectorizer
from nltk.tokenize import RegexpTokenizer
#tokenizer to remove unwanted elements from out data like symbols and numbers
token = RegexpTokenizer(r'[a-zA-Z0-9]+')
cv = CountVectorizer(lowercase=True,stop_words='english',ngram_range = (1,1),tokenizer = token.tokenize)
text_counts= cv.fit_transform(data['Phrase'])


##########################Split test and train data from each other
from sklearn.model_selection import train_test_split
X_train, X_test, y_train, y_test = train_test_split(
    text_counts, data['Sentiment'], test_size=0.3, random_state=1)

################Text classification using Naive Bayes classifier
from sklearn.naive_bayes import MultinomialNB
#Import scikit-learn metrics module for accuracy calculation
from sklearn import metrics
# Model Generation Using Multinomial Naive Bayes
clf = MultinomialNB().fit(X_train, y_train)
predicted= clf.predict(X_test)
print("MultinomialNB Accuracy (Naive Bayes):",metrics.accuracy_score(y_test, predicted))


#####################Vectorizing using TD-IDF classifier
from sklearn.feature_extraction.text import TfidfVectorizer
tf=TfidfVectorizer()
text_tf= tf.fit_transform(data['Phrase'])

from sklearn.model_selection import train_test_split
X2_train, X2_test, y2_train, y2_test = train_test_split(
    text_tf, data['Sentiment'], test_size=0.3, random_state=123)

from sklearn.naive_bayes import MultinomialNB
from sklearn import metrics
# Model Generation Using Multinomial Naive Bayes
clf = MultinomialNB().fit(X2_train, y2_train)
predicted= clf.predict(X2_test)
print("MultinomialNB Accuracy (TF-IDF):",metrics.accuracy_score(y2_test, predicted))    