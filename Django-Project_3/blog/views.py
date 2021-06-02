from django.shortcuts import render

def index(request):

    context = {

        "judul": "Riceufood | Blog",
        "heading":"Blog",
        "subheading":"Ini adalah jurnal"

    }    
    return render(request, "blog/index.html",context)
