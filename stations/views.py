from django.http import HttpResponse
from django.shortcuts import render

def index(request):
    # Your code here
    
    # Return an HttpResponse object
    return render(request, "index.html", {})