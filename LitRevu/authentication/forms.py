from django import forms
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth import login, get_user_model


class SignupForm(UserCreationForm):
    class Meta(UserCreationForm.Meta):
        model = get_user_model()
        fields = ('username', 'email', 'first_name', 'last_name', 'role')


"""class LoginForm(forms.Form):
    class Meta:
        username = forms.CharField(max_length=60, label="User name")
        password = forms.CharField(
            max_length=60, widget=forms.PasswordInput, label="Password"
        )"""




