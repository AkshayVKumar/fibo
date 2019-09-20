from django import forms

class Form_Data(forms.Form):
    data=forms.IntegerField(min_value=1,label="Enter the Number")