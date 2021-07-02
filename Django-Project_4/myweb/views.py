from django.shortcuts import render

def index(request):
    context = {
        "judul":"Riceufood",
        "heading":"Selamat Datang",
        "subheading":"Riceufood",
    }
    return render(request,"index.html",context)