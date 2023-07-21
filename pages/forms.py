from django import forms
from .models import GetInTouch

class FormGet (forms.ModelForm):
    class Meta:
        model = GetInTouch
        fields = [
            'full_name',
            'email_address',
            'phone_number',
            'message',
        ]

        widgets = {
            'full_name':forms.TextInput(attrs={'class':'form-control'}),
            'email_address':forms.TextInput(attrs={'class':'form-control'}),
            'phone_number':forms.TextInput(attrs={'class':'form-control'}),
            'message':forms.Textarea(attrs={'class':'form-control'}),
            

        }

        