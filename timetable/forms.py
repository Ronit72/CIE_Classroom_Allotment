from django import forms  
from timetable.models import Timetable  


class TimetableForm(forms.ModelForm):
    on_date = forms.fields.DateField(widget=forms.widgets.DateInput(attrs={'type': 'date'}))
    free_time = forms.fields.TimeField(widget=forms.widgets.TimeInput(attrs={'type': 'time'}))
    class Meta:  
        model = Timetable 
        fields = '__all__'

class TimetableUpdateForm(forms.ModelForm):
    class Meta:
        model = Timetable
        fields =['free_time', 'on_date']
        widgets = {
           'on_date': forms.fields.DateInput(attrs={'type': 'date', 'class': 'form-control'}),
            'free_time': forms.fields.TimeInput(attrs={'type': 'time', 'class': 'form-control'}),
        }