from django.shortcuts import render, get_object_or_404
from .models import Product
from .forms import ProductForm, RawProductForm
from django.http import Http404
# Create your views here.

def product_create_view(request):
    form = ProductForm(request.POST or None)
    if form.is_valid():
        form.save()
        form = ProductForm()

    context = {
        'form': form,
    }
    return render(request, "products/product_create.html", context)

def redener_intial_data(request):
    initial_data = {
        'title': 'Awesome title',
        'description': 'stupid desc',
        'price': 0.00,
    }
    obj = Product.objects.get(id=1)
    form = ProductForm(request.POST or None, instance=obj)
    if form.is_valid():
        form.save()

    context = {
        'form': form,
    }
    return render(request, "products/product_create.html", context)


def product_lookup(request, id):

    # obj = Product.objects.get(id=id)
    # obj = get_object_or_404(Product, id=id)
    try:
        obj = Product.objects.get(id=id)
    except Product.DoesNotExist:
        raise Http404
    form = ProductForm(request.POST or None, instance=obj)

    context = {
        'form': form,
    }
    return render(request, "products/product_view.html", context)


# def product_create_view(request):

#     if request.method == 'POST':
#         new_title = request.POST.get('title')
#         print(new_title)
#     context = {
#     }
#     return render(request, "products/product_create.html", context)


# def product_create_view(request):
#     my_form = RawProductForm()
#     if request.method == 'POST':
#         my_form = RawProductForm(request.POST)
#         if my_form.is_valid():
#             print(my_form.cleaned_data)
#             Product.objects.create(**my_form.cleaned_data)
#         else:
#             print(my_form.errors)
#
#
#
#     context = {
#         "form": my_form
#     }
#     return render(request, "products/product_create.html", context)


def product_detail_view(request):
    obj = Product.objects.get(id=1)
    # context = {
    #     'title': obj.title,
    #     'description': obj.description,
    # }
    context = {
        'object': obj,
    }
    return render(request, "products/detail.html", context)
