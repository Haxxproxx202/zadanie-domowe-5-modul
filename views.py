from django.shortcuts import render, get_object_or_404, redirect
from django.template.defaulttags import register
from django.views import View
from django.views.generic import TemplateView

from .models import Category, Product
from django.views.generic.edit import FormView, UpdateView
from .forms import AddCategoryForm, EditCategoryForm, AddProductsForm
from django.urls import reverse

# Create your views here.
class ListCategories(View):
    def get(self, request):
        list_categories = Category.objects.order_by('category_name')
        ctx = {'list_cat': list_categories}
        return render(request, 'homework_app/list_categories.html', ctx)

@register.filter
def get_value(dictionary, key):
    return dictionary.get(key)

class OneCategory(View):
    def get(self, request, slug):
        item = Category.objects.get(slug=slug)
        gross_price = item.product_set.all().order_by('name')
        list = {}
        for i in gross_price:
            list[i.name] = (float(i.price) * (1 + float(i.vat)))
        ctx = {'item': item, 'gross_price': gross_price, 'list': list}
        return render(request, 'homework_app/category.html', ctx)


class OneProduct(View):
    def get(self, request, id):
        product = Product.objects.get(id=id)
        ctx = {'product': product}
        return render(request, 'homework_app/oneproduct.html', ctx)

class AddCategoryView(FormView):
    # pass
    template_name = "homework_app/add_category.html"
    form_class = AddCategoryForm
    success_url = "/categories/"
    def form_valid(self, form):
        form.save()
        return super().form_valid(form)

class EditCategoryView(UpdateView):
    model = Category
    # form_class = EditCategoryForm
    template_name = "homework_app/category_update_form.html"
    fields = "__all__"

    success_url = "/categories/"

    def get_object(self, queryset=None):
        return get_object_or_404(Category, slug=self.kwargs.get("slug"))

class ProductList(View):
    def get(self, request):
        list = Product.objects.all()
        return render(request, 'homework_app/list_products.html', {'list': list})

class EditProductView(UpdateView):
    template_name = "homework_app/product_update_form.html"
    model = Product
    fields = "__all__"
    success_url = "/products/"

    def get_object(self, queryset=None):
        return get_object_or_404(Product, pk=self.kwargs.get("product_id"))

class AddProductView(FormView):
    template_name = "homework_app/add_product.html"
    form_class = AddProductsForm
    success_url = "/products/"


    def form_valid(self, form):
        form.save()
        return super().form_valid(form)

class MainView(View):
    def get(self, request):
        return render(request, 'homework_app/main.html')

class SearchResult(View):
    def get(self, request):
        return render(request, 'homework_app/search.html')
    def post(self, request):
        result = request.POST.get('result')
        error = []

        try:
            categories = Category.objects.filter(category_name__icontains=result)
        except:
            error.append("Nie znaleziono żadnej kategorii")
        try:
            products = Product.objects.filter(name__icontains=result)
        except:
            error.append("Nie znaleziono żadnego produktu")

        print(error)

        if error:
            return render(request, 'homework_app/search.html', context={'error': error})
        return render(request, 'homework_app/search.html', {'categories': categories, 'products': products})







        # students = Student.objects.filter(last_name__icontains=form.cleaned_data['name'])







