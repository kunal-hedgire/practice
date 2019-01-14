from django import forms
from studApp.models import studInfo
'''
GENDER_CHOICES = (
    ('Male',  'Male'),
    ('Female','Female'),
    ('Other', 'Other')
)
'''

class StudentForm(forms.ModelForm):
    class Meta:
        model = studInfo
        fields = "__all__"