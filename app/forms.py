from app.models import CustomUser
from django import forms
from django.contrib.auth.forms import UserCreationForm

class SignUpForm(UserCreationForm):
    Address_line_1 = forms.CharField(widget=forms.TextInput, required=False)
    profile_picture = forms.ImageField(widget=forms.FileInput(attrs={'accept': 'images/*'}), required=False)
    class Meta:
        model = CustomUser
        fields = ['first_name', 'last_name', 'profile_picture', 'username', 'email', 'password1', 'password2', 'Address_line_1', 'city', 'state', 'pincode']