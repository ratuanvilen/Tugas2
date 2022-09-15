from multiprocessing import context
from django.shortcuts import render
from katalog.models import CatalogItem 

# TODO: Create your views here.
def show_katalog(request):
    data_katalog = CatalogItem.objects.all()
    context = {
        'list_barang_katalog' : data_katalog,
        'nama' : 'Ratu Almas Naurah Anvilen',
        'NPM' : '2106752035',
    }
    return render(request, "katalog.html", context)