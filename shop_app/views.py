from django.shortcuts import render, get_object_or_404
from .models import *
from django.db.models import Q
from django.core.paginator import Paginator, EmptyPage, InvalidPage


# Create your views here.


def fun(request, c_slug=None):
    c_page = None
    prodt = None
    if c_slug != None:
        c_page = get_object_or_404(Categ, slug=c_slug)
        prodt = Product.objects.filter(category=c_page, available=True)
    else:
        prodt = Product.objects.all().filter(available=True)
    cat = Categ.objects.all()
    paginator = Paginator(prodt, 4)
    try:
        page = int(request.GET.get('page', '1'))
    except:
        page = 1
    try:
        pro = paginator.page(page)
    except(EmptyPage, InvalidPage):
        pro = Paginator.page(Paginator.num_pages)
    return render(request, 'home.html', {'pr': prodt, 'ct': cat, 'pg': pro})


def ProductDetails(request, c_slug, product_slug):
    try:
        prod = Product.objects.get(category__slug=c_slug, slug=product_slug)
    except Exception as e:
        raise e
    return render(request, 'product.html', {'pr': prod})


def searching(request):
    prod = None
    query = None
    if 'q' in request.GET:
        query = request.GET.get('q')
        prod = Product.objects.all().filter(Q(name__contains=query) | Q(desc__contains=query))
    return render(request, 'search.html', {'qr': query, 'pr': prod})
