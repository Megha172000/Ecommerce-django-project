from math import ceil

from django.shortcuts import render,HttpResponse
from . models import product

def shopindex(request):
    products = product.objects.all()
    print(products)
    n=len(products)
    nSlides = n // 4 + ceil((n / 4) + (n // 4))
    params = {'no_of_slides': nSlides, 'range': range(1, nSlides), 'product': products}
    return render(request,'shop/index.html',params)

def about(request):
    return render(request, 'shop/about.html')

def contact(request):
    return HttpResponse('contact us')

def tracker(request):
    return HttpResponse('its about tracker')

def search(request):
    return HttpResponse('search about us')




def productView(request):
    return HttpResponse('its about product')

def checkout(request):
    return HttpResponse('checkout')
