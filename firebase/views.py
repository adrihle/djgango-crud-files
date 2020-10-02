from os import name
from django.http.response import HttpResponse
from django.shortcuts import render, redirect
from django.http import HttpResponse

from .models import Product
from .forms import ProductForm, ProductForm2


def index(request):
    print('ok, just for now we enter into a view')
    message = 'upload here a product'
    
    if request.method == 'POST':
        form = ProductForm2(request.POST, request.FILES)
        if form.is_valid():
            newproduct = Product(name=request.POST['name'], 
                                description=request.POST['description'],
                                image=request.FILES['image'])

            newproduct.save()

            return redirect('index')

        else:
            message = 'The form is not valid homie'
    else:
        form = ProductForm2()

    products = Product.objects.all()
    context = {
        'products': products,
        'form': form,
        'message': message
        }

    return render(request, 'list.html', context)

def delete(request, id=None):
    to_delete = Product.objects.get(id=id)
    to_delete.delete()
    return redirect('index')