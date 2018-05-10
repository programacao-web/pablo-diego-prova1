from django.forms import ModelForm 
from .models import Pastebin

class PastebinForms(ModelForm):
    class Meta:
        model = Pastebin
        fields=["title","language","code"]