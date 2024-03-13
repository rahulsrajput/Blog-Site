from django.contrib.auth.forms import UserCreationForm, AuthenticationForm, UserChangeForm
from django.contrib.auth.models import User


class signup_form(UserCreationForm):
    class Meta:
        model = User
        fields = ['username', 'email']

class login_form(AuthenticationForm):
    pass

class profile_edit(UserChangeForm):
    password = None
    class Meta:
        model = User
        fields = ['username', 'email', 'first_name', 'last_name']