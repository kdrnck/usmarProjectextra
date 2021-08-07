from typing import ChainMap
from django import forms as forms
from django.forms import fields
from .models import UserBase 
from django.contrib.auth.forms import (AuthenticationForm, PasswordResetForm,
                                       SetPasswordForm)

class UserLoginForm(AuthenticationForm):
    username = forms.CharField(widget=forms.TextInput(
        attrs={'class': 'form-control mb-3', 'placeholder': 'Kullanıcı Adı', 'id': 'login-username'}))
    password = forms.CharField(widget=forms.PasswordInput(
        attrs={
            'class': 'form-control',
            'placeholder': 'Şifre',
            'id': 'login-pwd',
        }
    ))


class RegistrationForm(forms.ModelForm):
    
    user_name = forms.CharField(label='Kullanıcı Adı', min_length=4, max_length=50, help_text='Zorunlu')
    email = forms.EmailField(max_length=100, help_text="zorunlu", error_messages={'required':'Eposta girmeniz gerekmektedir'})
    password = forms.CharField(label='Şifre', widget=forms.PasswordInput)

    class Meta:
        model = UserBase
        fields = ('user_name',)

    def clean_email(self):
        email = self.cleaned_data['email']
        if UserBase.objects.filter(email=email).exists():
            raise forms.ValidationError(
                'Bu e-posta adresi zaten kullanımda.')
        return email

    def clean_username(self):
        user_name = self.cleaned_data['user_name'].lower()
        r = UserBase.objects.filter(user_name=user_name)
        if r.count():
            raise forms.ValidationError(
                'Bu  kullanıcı adı zaten alınmış.')
        return user_name

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.fields['user_name'].widget.attrs.update(
            {'class': 'form-control mb-3', 'placeholder': 'Kullanıcı Adı'})
        self.fields['email'].widget.attrs.update(
            {'class': 'form-control mb-3', 'placeholder': 'E-posta', 'name': 'email', 'id': 'id_email'})
        self.fields['password'].widget.attrs.update(
            {'class': 'form-control mb-3', 'placeholder': 'Şifre'})


class UserEditForm(forms.ModelForm):

    email = forms.EmailField(
        label='E-posta hesabı (değiştirilemiyor)', max_length=200, widget=forms.TextInput(
            attrs={'class': 'form-control mb-3', 'placeholder': 'email', 'id': 'form-email', 'readonly': 'readonly'}))

    first_name = forms.CharField(
        label='İsminiz', max_length=150, widget=forms.TextInput(
            attrs={'class': 'form-control mb-3', 'placeholder': 'Ahmet', 'id': 'form-firstname'}))

    phone_number = forms.CharField(
        label='Telefon Numaranız', max_length=15, widget=forms.TextInput(
            attrs={'class': 'form-control mb-3', 'placeholder': '053* *** ****', 'id': 'form-phone'}))
    address = forms.CharField(
        label='Adresiniz', max_length=500, widget=forms.TextInput(
            attrs={'class': 'form-control mb-2', 'placeholder': 'Bahçeköy Yeni Mahalle...', 'id': 'form-adress'}))

    class Meta:
        model = UserBase
        fields = ('email', 'first_name', 'phone_number', 'address')

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.fields['first_name'].required = True
        self.fields['email'].required = True

class PwdResetForm(PasswordResetForm):


    email = forms.EmailField(max_length=254, widget=forms.TextInput(
        attrs={'class': 'form-control mb-3', 'placeholder': 'Email', 'id': 'form-email'}))


    def clean_email(self):
        email = self.cleaned_data['email']
        u = UserBase.objects.filter(email=email)
        if not u:
            raise forms.ValidationError(
                'Böyle bir e-posta adresi sisteme kayıtlı değil')
        return email

class PwdResetConfirmForm(SetPasswordForm):
    new_password1 = forms.CharField(
        label='Şifreyi gir', widget=forms.PasswordInput(
            attrs={'class': 'form-control mb-3', 'placeholder': 'Yeni şifren', 'id': 'form-newpass'}))
    new_password2 = forms.CharField(
        label='Tekrar gir', widget=forms.PasswordInput(
            attrs={'class': 'form-control mb-3', 'placeholder': 'Yeni şifren', 'id': 'form-new-pass2'}))