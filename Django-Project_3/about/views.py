from django.shortcuts import render

# Create your views here.
def index(request):
    context = {
    "judul": "Riceufood | About",
    "heading":"About",
    "subheading":"Tentang Riceufood"
    }
    return render(request,"about/index.html",context)