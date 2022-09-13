from multiprocessing import context
from django.shortcuts import render
from katalog.models import CatalogItem

# TODO: Create your views here.
def show_catalog(request):
    context = {
        'listobject': CatalogItem.objects.all(), 
        'nama': 'Khansa Jovita', 'npm': '2106651686' 
    }
    return render(request, "katalog.html", context)