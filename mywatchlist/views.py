from django.shortcuts import render
from mywatchlist.models import MywatchlistItem
from django.http import HttpResponse
from django.core import serializers

# Create your views here.
def show_html(request):
    listfilm = MywatchlistItem.objects.all()
    context = {
        'listfilm': listfilm,
        'nama': 'Khansa Jovita', 'npm': '2106651686',
    }
    return render(request, "mywatchlist.html", context)

def show_xml(request):
    listfilm = MywatchlistItem.objects.all()
    return HttpResponse(serializers.serialize("xml", listfilm), content_type="application/xml")

def show_json(request):
    listfilm = MywatchlistItem.objects.all()
    return HttpResponse(serializers.serialize("json", listfilm), content_type="application/json")
