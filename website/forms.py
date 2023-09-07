from django import forms
from django.contrib.auth.forms import UserCreationForm, UserModel
from django.contrib.auth.models import User

class SignUpForm(UserCreationForm):
    email = forms.EmailField(label='', widget=forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'Email Address'}))
    first_name = forms.CharField(label='', max_length=20, widget=forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'First Name'}))
    last_name = forms.CharField(label='', max_length=20, widget=forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'Last Name'}))
    address = forms.CharField(label='', max_length=50, widget=forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'Street Address'}))
    city = forms.CharField(label='', max_length=30, widget=forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'City Name'}))
    zip_code = forms.IntegerField(label='', max_length=10, widget=forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'Zip Code'}))


    class Meta:
        model: User
        fields = ('username', 'first_name', 'last_name', 'email', 'password', 'password1')

    def __init__(self, *args, **kwargs):
        super(SignUpForm, self).__init__(*args, **kwargs)

        self.fields['username'].widget.attrs['placeholder'] = 'User Name'
        self.fields['username'].label =  ''
        self.fields['username'].help_text = '<span class=”form-text text-muted”><small>Required. 150 characters or fewer. Letters, digits and @/./+/-/ only.</small></span>'


        self.fields['password']. widget.attrs['class'] = 'form-control'
        self.fields['password']. widget.attrs['placeholder'] = 'Password'
        self.fields['password'].label =  ''
        self.fields['password'].help_text = '<ul class= “form-text text-muted small”><li>Your password can\'t be too similar to your other personal information.</li><li>Your password must contain at least 8 characters.</li><li>Your password can\'t be a commonly used password.</li><li>Your password can\'t be entirely numeric.</li><ul>'

        self.fields['password1']. widget.attrs['class'] = 'form-control'
        self.fields['password1']. widget.attrs['placeholder'] = 'Confirm Password'
        self.fields['password1'].label =  ''
        self.fields['password1'].help_text = '<span class=”form-text text-muted”><small>Enter the same password as before, for verification.</small></span>'

                    
                    
 