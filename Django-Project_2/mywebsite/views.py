from django.shortcuts import render

def index(request):
    context = {
        "judul": "Riceufood",
        "subjudul": "Selamat Datang di Riceufood",
        "banner": "img/banner_riceufood_home.png",

    }
    return render(request,"index.html",context)

