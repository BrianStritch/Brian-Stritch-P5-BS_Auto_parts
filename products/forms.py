""" products forms.py """
from django import forms
from .models import Product, Category, Manufacturer
from .widgets import CustomClearableFileInput


class ProductForm(forms.ModelForm):
    """ product model form """
    class Meta:
        """ sets form fields """
        model = Product
        fields = '__all__'

    image = forms.ImageField(label='image',
                             required=False,
                             widget=CustomClearableFileInput)

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        categories = Category.objects.all()
        friendly_names = [(c.id, c.get_friendly_name()) for c in categories]

        self.fields['category'].choices = friendly_names
        for field_name, field in self.fields.items():
            field.widget.attrs['class'] = 'border-black rounded-0'


class ManufacturerForm(forms.ModelForm):
    """ manufacturer model form """

    class Meta:
        """ sets form fields """
        model = Manufacturer
        fields = '__all__'


class CategoryForm(forms.ModelForm):
    """ category model form """

    class Meta:
        """ sets form fields """
        model = Category
        fields = '__all__'
