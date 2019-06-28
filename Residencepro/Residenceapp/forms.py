from django import forms
class ResidenceForm(forms.Form):
    username = forms.CharField(label='Username',widget=forms.TextInput(attrs={'class': 'form-control','placeholder': 'Username'}))

    email = forms.EmailField(label='Email',widget=forms.EmailInput(attrs={'class': 'form-control','placeholder': 'ex@gmail.com'}))

    password = forms.IntegerField(label='Password',widget=forms.PasswordInput(attrs={'class': 'form-control','placeholder':'Password'}))
    confirm_password = forms.IntegerField(label='Confirm Password',widget=forms.PasswordInput(attrs={'class': 'form-control','placeholder':'Confirmpassword'}))
class Loginform(forms.Form):
    username = forms.CharField(label='Username',widget=forms.TextInput(attrs={'class':'form-control'}))
    password = forms.IntegerField(label='Password',widget=forms.PasswordInput(attrs={'class':'form-control'}))