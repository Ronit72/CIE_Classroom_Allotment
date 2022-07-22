from django import forms
from exam.models import Exam  
from django import forms

class ExamForm(forms.ModelForm):
    exam_date = forms.fields.DateField(widget=forms.widgets.DateInput(attrs={'type': 'date'}))
    time_slot = forms.fields.TimeField(widget=forms.widgets.TimeInput(attrs={'type': 'time'}))

    class Meta:  
        model = Exam  
        fields = '__all__'

class ExamUpdateForm(forms.ModelForm):
    class Meta:
        model = Exam
        fields = '__all__'
        widgets = {
            'course_no': forms.TextInput(attrs={'class': 'form-control'}),
           'exam_date': forms.fields.DateInput(attrs={'type': 'date', 'class': 'form-control'}),
            'time_slot': forms.fields.TimeInput(attrs={'type': 'time', 'class': 'form-control'}),
        }