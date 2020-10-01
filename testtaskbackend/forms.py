from django import forms
from .models import Equipment, Equipment_type
import re
from django.core.exceptions import ValidationError

class EquipmentForm(forms.Form):
    serial_number = forms.CharField(max_length=10)
    code_of_type = forms.ModelChoiceField(queryset=Equipment_type.objects.all())
    class Meta:
        model = Equipment

        widgets = {
            'class': 'form-control'
        }
