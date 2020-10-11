from django import forms
from .models import Product

class ProductForm(forms.ModelForm):
    title = forms.CharField(
        label='',
        widget=forms.TextInput(
            attrs={"placeholder": "Your Title"}
        ))
    # email = forms.EmailField()
    price = forms.DecimalField(initial=199.99)
    description = forms.CharField(
        required=False,
        widget=forms.Textarea(attrs={
            "class": "new-class-name two",
            "rows": 20,
            "cols": 50,
            "id": "my-id-for-text-area",
            "placeholder": "Your Description"
        })
    )
    class Meta:
        model = Product
        fields = [
            'title',
            'description',
            'price'
        ]
    def clean_title(self, *args, **kwargs):
        title = self.cleaned_data.get("title")
        if not "news" in title:
            raise forms.ValidationError('This is not valid title')
        else:
            return title

    def clean_email(self, *args, **kwargs):
        email = self.cleaned_data.get("email")
        if not email.endswith('edu'):
            raise forms.ValidationError('This is not valid email')
        else:
            return email

class RawProductForm(forms.Form):
    # https://docs.djangoproject.com/en/3.1/ref/forms/fields/
    title = forms.CharField(label='', widget=forms.TextInput(attrs={"placeholder": "Your Title"}))
    price = forms.DecimalField(initial=199.99)
    description = forms.CharField(
        required=False,
        widget=forms.Textarea(attrs={
            "class": "new-class-name two",
            "rows": 20,
            "cols": 50,
            "id": "my-id-for-text-area",
            "placeholder": "Your Description"
        })
    )
