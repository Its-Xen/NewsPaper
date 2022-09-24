from django.contrib.auth.forms import UserChangeForm, UserCreationForm
from .models import CustomUser

class CUCREATIONFORM(UserCreationForm):
    class Meta(UserCreationForm):
        model = CustomUser
        fields = (
            'username',
            'age',
            'email',
        )

class CUCHANGEFORM(UserChangeForm):
    class Meta:
        model = CustomUser
        fields = (
            'username',
            'age',
            'email',
        )