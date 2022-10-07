from.models import contact_us
from django import forms
class contact_form(forms.ModelForm):
    class Meta:
        model = contact_us
        fields = '__all__'