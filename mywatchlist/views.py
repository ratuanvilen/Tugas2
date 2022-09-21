from django.shortcuts import render

# Create your views here.
from django.shortcuts import render
from django.http import HttpResponse
from django.core import serializers
from mywatchlist.models import MyWatchlist


def show_mywatchlist(request):
    data_film = MyWatchlist.objects.all()
    
    belum_nonton = MyWatchlist.objects.filter(watched="Not yet").count()
    sudah_nonton = MyWatchlist.objects.filter(watched="Yes").count()
    
    if sudah_nonton > belum_nonton:
        pesan = "Selamat, kamu sudah banyak menonton!"
    else:
        pesan = "Wah, kamu masih sedikit menonton!"

    
    context = {
        'watchlist' : data_film,
        'nama' : "Ratu Almas Naurah Anvilen",
        'npm' : "2106752035",
        'message' : pesan,
    }
    return render(request, "watchlist.html", context)

def show_xml (request):
    data = MyWatchlist.objects.all()
    return HttpResponse(serializers.serialize("xml", data), content_type="application/xml")

def show_xml_by_id(request, id):
    data = MyWatchlist.objects.filter(pk=id)
    return HttpResponse(serializers.serialize("xml", data), content_type="application/xml")
    
def show_json (request):
    data = MyWatchlist.objects.all()
    return HttpResponse(serializers.serialize("json", data), content_type="application/json")

def show_json_by_id(request, id):
    data = MyWatchlist.objects.filter(pk=id)
    return HttpResponse(serializers.serialize("json", data), content_type="application/json")