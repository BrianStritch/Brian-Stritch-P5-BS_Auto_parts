# imports
# 3rd party imports from django
from django import forms
from django.contrib.auth.models import User
from .models import UserProfile
from django.contrib.auth.forms import UserCreationForm, UserChangeForm


class UserAccountDetailsForm(UserCreationForm):
    """
    Class based form to create new user with additional fields for
    first name and last name inheriting from the built in django
    usercreation form
    """
    email = forms.EmailField(required=True)

    class Meta:
        """
        Class to indicate which model to use and to
        set the fields in the create user model form
        """
        model = User
        fields = (
            'username',
            'first_name',
            'last_name',
            'email',
            'password1',
            'password2',
        )

    def update(self, commit=True):
        """
        Class to update the users details and save to the database
        """
        user = super(UserAccountDetails, self).save(commit=False)
        user.first_name = self.cleaned_data['first_name']
        user.last_name = self.cleaned_data['last_name']
        user.email = self.cleaned_data['email']

        if commit:
            user.save()

        return user


class UserProfileForm(forms.ModelForm):

    class Meta:
        model = UserProfile
        exclude = ('user', )

    def __init__(self, *args, **kwargs):
        """
        Add placeholders and classes, remove auto-generated
        labels and set autofocus on first field
        """
        super().__init__(*args, **kwargs)
        placeholders = {
            'default_phone_number': 'Phone Number',
            'default_postcode': 'Postal Code or Eircode',
            'default_town_or_city': 'Town or City',
            'default_street_address1': 'Street Address 1',
            'default_street_address2': 'Street Address 2',
            'default_county': 'County, State or Locality',
        }

        self.fields['default_phone_number'].widget.attrs['autofocus'] = True
        for field in self.fields:
            if field != 'default_country':
                if self.fields[field].required:
                    placeholder = f'{placeholders[field]}'
                else:
                    placeholder = placeholders[field]
                self.fields[field].widget.attrs['placeholder'] = placeholder
            self.fields[field].widget.attrs[
                'class'] = 'border-black rounded-0 profile-form-input'
            self.fields[field].label = False


class EditProfileForm(UserChangeForm):
    """
        Class based form inheriting from the built in django built
        in userchangeform the Create Review model form for
        creating a new review
    """
    email = forms.EmailField(required=True)

    class Meta:
        """
        Class to indicate which model to use and to
        set the fields in the user change form
        """
        model = User
        fields = (
            'email',
            'first_name',
            'last_name',
        )
