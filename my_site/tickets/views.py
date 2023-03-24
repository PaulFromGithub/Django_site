from django.shortcuts import render

def index(request):
    return render(request, 'tickets/index.html')

def about(request):
    return render(request, 'tickets/about.html')