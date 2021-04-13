from django.contrib.auth import get_user_model
from django.contrib.auth.forms import UserCreationForm, UserChangeForm
from phone_field import PhoneField
from django import forms 
from accounts.models import Profile , User


class ProfileCreateForm(UserCreationForm):
    class Meta:
        fields = ('first_name', 'last_name', "username", "email")
        # more fields: 'phone', 'title',

        model = get_user_model()

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.fields["username"].label = "Display Name"
        self.fields["email"].label = "Email address"
        self.fields['first_name'].label = "First Name"
        self.fields['last_name'].label = "Last Name"

# class PasswordChangerForm(PasswordChangeForm):


class ProfileChangeFrom(UserChangeForm):
    class Meta:
        fields = ('first_name', 'last_name', "email")
        exclude = ("username",)
        model = get_user_model()
        # widgets = {
        #     'username': forms.TextInput(attrs={'readonly': 'readonly'}),
        #     'email': forms.TextInput(attrs={'readonly': 'readonly'})
        # }

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.fields["username"].label = "Display name"
        self.fields["email"].label = "Email address"
        self.fields['first_name'].label = "First Name"
        self.fields['last_name'].label = "Last Name"

class UserForm(forms.ModelForm):
    class Meta:
        model = User
        fields = ('first_name', 'last_name', 'email')

class ProfileForm(forms.ModelForm):
    class Meta:
        model = Profile
        fields = ('phone', 'title', 'system_name')