from django.shortcuts import render

# Create your views here.
import pandas as pd
from sklearn.feature_extraction.text import CountVectorizer
from sklearn.model_selection import train_test_split
from sklearn.naive_bayes import MultinomialNB
from sklearn.metrics import accuracy_score
from .forms import MessageForm


data = pd.read_csv("../SpamDetection/emails.csv") 
# print(data.header())


vectorizer = CountVectorizer()
X = vectorizer.fit_transform(data['text'])


X_train, X_test, y_train, y_test = train_test_split(X, data['spam'], test_size=0.2)


model = MultinomialNB()
model.fit(X_train, y_train)


def predictMessage(message):
    test_data = vectorizer.transform([message])
    prediction = model.predict(test_data)
    return "Spam" if prediction[0] == 1 else "Ham"
    # return prediction
   

def Home(request):
    result = None
    if request.method == 'POST':
        form = MessageForm(request.POST)
        if form.is_valid():
            message = form.cleaned_data['Enter_your_mail']
            result = predictMessage(message)
    else:
        form = MessageForm()
    return render(request, 'index.html', {'form': form, 'result': result})