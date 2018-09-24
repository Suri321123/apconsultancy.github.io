from django import forms
from django.forms import ModelForm
from django.forms import ModelChoiceField
from .models import RegisterUser

class RegisterJob(ModelForm):
    class Meta:
        model = RegisterUser
        widgets = {'dob': forms.DateInput(attrs={'class': 'dobForm'}),}
        fields = '__all__'

    def clean_mobile(self):
        mobile = self.cleaned_data['mobile']
        num_words = len(str(mobile))
        if num_words != 10:
            raise forms.ValidationError("*Enter a valid mobile number")
        return mobile

    def clean_dob(self):
        dob = self.cleaned_data['dob']
        year = str(dob).split('-')
        if int(year[2]) > 1995:
            raise forms.ValidationError("*You are not 18 years old")
        return dob


class ContactForm(forms.Form):
    name = forms.CharField(label='name',
                    widget=forms.TextInput(attrs={'placeholder': 'Your Name'}))
    email = forms.EmailField(label='email',
                    widget=forms.TextInput(attrs={'placeholder': 'Your E-Mail'}))
    message = forms.CharField(widget=forms.Textarea(attrs={'placeholder': 'Write us your query','cols': 50, 'rows': 3}))
