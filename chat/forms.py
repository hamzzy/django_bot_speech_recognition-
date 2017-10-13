from django import forms
from .models import  chat
class ChatForm(forms.Form):
    chat=forms.CharField()

