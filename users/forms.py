from tkinter.messagebox import NO
from django.contrib.auth import authenticate
from django import forms
from django.contrib.auth.forms import AuthenticationForm

from .models import *


class RegistrationForm(forms.ModelForm):

    email = forms.EmailField(max_length=100, help_text='Required', error_messages={'required': 'Sorry, you will need an email'})
    password = forms.CharField(label='Password', widget=forms.PasswordInput)
    password2 = forms.CharField(label='Repeat password', widget=forms.PasswordInput)

    class Meta:
        model = UserBase
        fields = ('email', )


    def clean_password2(self):
        cd = self.cleaned_data
        if cd['password'] != cd['password2']:
            raise forms.ValidationError('Password do not match!')
        return cd['password2']

    def clean_eamil(self):
        email = self.cleaned_data['email']
        if UserBase.objects.filter(email=email).exists():
            raise forms.ValidationError(
                'Please use another Email, that is already taken')
        return email

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.fields['email'].widget.attrs.update(
            {"class": "form-control mb-3", "placeholder": "E-mail", "name": "email"})
        self.fields['password'].widget.attrs.update(
            {"class": "form-control mb-3", "placeholder": "Password"})
        self.fields['password2'].widget.attrs.update(
            {"class": "form-control", "placeholder": "Repeat password"}
        )





class UserLoginForm(AuthenticationForm):
    class Meta:
        model = UserBase
        fields = ['username', 'password']

    username = forms.CharField(label='Email', widget=forms.TextInput(attrs={
        "class": "form-control mb-3",
        "placeholder": "Email kiriting",
        'id': 'login-username'}))

    password = forms.CharField(label='Parol', widget=forms.PasswordInput(attrs={
        "class": "form-control mb-3",
        "placeholder": "Parolni kiriting",
        'id': 'login-pwd'}))


    def clean(self):
        username = self.cleaned_data['username']
        password = self.cleaned_data['password']
        user = authenticate(username=username, password=password)
        if not user:
            raise forms.ValidationError('Email yoki parol xato!')

        return self.cleaned_data