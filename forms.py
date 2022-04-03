from django import forms
from .models import Category, Product

class AddCategoryForm(forms.ModelForm):
    class Meta:
        model = Category
        fields = "__all__"

class EditCategoryForm(forms.ModelForm):
    class Meta:
        model = Category
        fields = "__all__"

class AddProductsForm(forms.ModelForm):
    class Meta:
        model = Product
        fields = "__all__"

# class SearchForm(forms.ModelForm):
#
#
