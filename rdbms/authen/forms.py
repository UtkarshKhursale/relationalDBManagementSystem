from django import forms
from django.contrib.auth.forms import UserCreationForm, UserChangeForm, AuthenticationForm
from django.forms.widgets import PasswordInput, TextInput, NumberInput
from .models import CustomUser


class SignUpForm(UserCreationForm):
    mobile_no = forms.CharField(max_length=10, help_text='Enter Mobile number without code')
    branch = forms.CharField(max_length=100, help_text='Enter your branch')
    email = forms.EmailField(max_length=150, help_text='Email')
    first_name = forms.CharField(max_length=100, help_text='Enter your first name')
    last_name = forms.CharField(max_length=100, help_text='Enter your last name')
    class Meta:
        model = CustomUser
        fields =('username', 'email', 'first_name', 'last_name', 'mobile_no', 'branch', 'batch', 'password1', 'password2',)# UserCreationForm.Meta.fields + ('full_name', 'age',)
    def __init__(self, *args, **kwargs):
        super(SignUpForm, self).__init__(*args, **kwargs)
        self.fields['username'].widget = forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'Username'})
        self.fields['username'].label = False
        self.fields['email'].widget = forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'Email-Id'})
        self.fields['first_name'].widget = forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'First Name'})
        self.fields['last_name'].widget = forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'Last Name'})
        self.fields['mobile_no'].widget = forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'Mobile Number'})
        self.fields['branch'].widget = forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'Branch'})
        self.fields['batch'].widget = forms.NumberInput(attrs={'class': 'form-control', 'placeholder': 'Batch'})
        self.fields['password1'].widget = forms.PasswordInput(attrs={'class': 'form-control', 'placeholder': 'Password'})
        self.fields['password1'].label = False
        self.fields['password2'].widget = forms.PasswordInput(attrs={'class': 'form-control', 'placeholder': 'Confirm Password'})

class MyAuthForm(AuthenticationForm):
    class Meta:
        fields = ['username', 'password']
    def __init__(self, *args, **kwargs):
        super(MyAuthForm, self).__init__(*args, **kwargs)
        self.fields['username'].widget = forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'Username'})
        self.fields['username'].label = False
        self.fields['password'].widget = forms.PasswordInput(attrs={'class': 'form-control', 'placeholder': 'Password'})
        self.fields['password'].label = False
