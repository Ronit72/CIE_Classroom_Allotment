
from django import forms
from django.core.exceptions import ValidationError
from django.db.models import fields

from .models import Excel, Schedule

class ExcelForm(forms.ModelForm):
    def validate_file(xls):
        # print(xls.name.endswith('.xlsx'))
        if not (xls.name.endswith('.xlsx') or xls.name.endswith('.csv')):
            raise ValidationError("Only csv and xls file format supported!")
        return xls
    xls = forms.FileField(validators=[validate_file], widget=forms.FileInput(attrs={"class": ""}))
    class Meta:
        model = Excel
        fields = {'title','xls'}

class ScheduleForm(forms.ModelForm):
    
    def validate_file(pdf):
        if not pdf.name.endswith('.pdf'):
            raise ValidationError("Only pdf file format supported!")
        return pdf
    pdf = forms.FileField(validators=[validate_file], widget=forms.FileInput(attrs={"class": ""}))
    class Meta:
        model = Schedule
        fields = {'title','pdf'}
