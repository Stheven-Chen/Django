from django.shortcuts import render
from django.http import HttpResponse

def index(request):
    context = {

        "judul": "Riceufood",
        "heading":"Selamat Datang",
        "subheading":"di Riceufood"

    }
    return render(request,"index.html",context)