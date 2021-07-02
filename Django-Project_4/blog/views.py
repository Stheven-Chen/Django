from django.shortcuts import render

# Create your views here.
from .models import post

def index(request):

    postingan = post.objects.all()
    print(postingan)

    context = {
        "judul":"Riceufood | Blog",
        "heading":"Blog",
        "subheading":"Jurnal",
        "post":postingan,
    }
    return render(request,"blog/index.html",context)