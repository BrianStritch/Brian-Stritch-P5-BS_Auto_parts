# imports
# 3rd party imports from django
from django import forms

# internal imports from BS_Auto_parts
from .models import SiteUsersContactDetails, ExistingUsersContactDetails



class CreateSiteUsersContactDetailsForm(forms.ModelForm):
    """
        Class based form to set the fields in
        the SiteUsersContactDetails model form for
        creating a new user contact details form
    """
    class Meta:
        """
        Class to indicate which model to use and to
        set the fields in the create review model form
        """
        model = SiteUsersContactDetails
        fields = (
            'name',
            'surname',
            'email',            
            'phone_number',
            'street_address1',
            'street_address2',
            'town_or_city',
            'county',
            'country',
            'postcode',
            'message',
            )


class CreateSimpleUsersContactForm(forms.ModelForm):
    """
        Class based form to set the fields in
        the SiteUsersContactDetails model form for
        creating a new user contact details form
    """
    class Meta:
        """
        Class to indicate which model to use and to
        set the fields in the create review model form
        """
        model = SiteUsersContactDetails
        fields = (
            'name',
            'surname',
            'email',
            'message',
            )


class CreateExistingUsersContactForm(forms.ModelForm):
    """
        Class based form to set the fields in
        the ExistingUsersContactDetails model form for
        creating a new contact us form
    """
    class Meta:
        """
        Class to indicate which model to use and to
        set the fields in the create review model form
        """
        model = ExistingUsersContactDetails
        fields = (
            'message',
            )
