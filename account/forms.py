from django.contrib.auth.forms import UserCreationForm
from account.models import User


class UserCreationCustomForm(UserCreationForm):
    class Meta:
        model = User
        fields = ['first_name', 'last_name', 'username',
                  'email', 'password1', 'password2']
