# messaging/forms.py

from django import forms

class ComposeMessageForm(forms.Form):
    recipient = forms.CharField(max_length=100, label="Recipient")
    subject = forms.CharField(max_length=200)
    body = forms.CharField(widget=forms.Textarea)

    
