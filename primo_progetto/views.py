from django.shortcuts import render

# Create your views here.

def index_root(request):
    return render(request,"primo_progetto/index_root.html")