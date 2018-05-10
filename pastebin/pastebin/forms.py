from django.forms import ModelForm 
from .models import Paste

class PastebinForms(ModelForm):
    class Meta:
        model = Paste
        fields=["title","language","code"]