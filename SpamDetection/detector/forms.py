from django import forms

class MessageForm(forms.Form):
    Enter_your_mail = forms.CharField(widget=forms.Textarea(attrs={'class': 'form-control','placeholder':'Enter Your Email Messages here.. '}))