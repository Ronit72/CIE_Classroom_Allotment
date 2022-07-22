from django import forms  
from room.models import Room  
from django.core.exceptions import ValidationError


class RoomForm(forms.ModelForm):
    def validate_capacity(capacity):
        if capacity>999 or capacity<1:
            raise ValidationError("Capacity should be between 0 and 999")
        return capacity
    capacity = forms.IntegerField(validators=[validate_capacity])

    class Meta:  
        model = Room  
        fields = {'room_no','capacity'}