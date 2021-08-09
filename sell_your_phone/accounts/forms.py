from django import forms
from django.contrib.auth import get_user_model
from django.contrib.auth.forms import UserCreationForm, AuthenticationForm
from sell_your_phone.accounts.models import Profile
from sell_your_phone.core.forms import BootstrapFormMixin

UserModel = get_user_model()


class LoginForm(BootstrapFormMixin, AuthenticationForm):
    pass


class RegisterForm(BootstrapFormMixin, UserCreationForm):
    class Meta:
        model = UserModel
        fields = ('email',)


class ProfileForm(BootstrapFormMixin, forms.ModelForm):
    class Meta:
        model = Profile
        fields = ('profile_image',)
