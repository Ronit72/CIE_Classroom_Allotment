from django import forms  
from invigilator.models import Invigilator


class InvigilatorForm(forms.ModelForm):
    
    class Meta:  
        model = Invigilator 
        fields = {'id','name','email','invigilation_count'}