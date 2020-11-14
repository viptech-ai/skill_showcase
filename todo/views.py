from django.shortcuts import render

# Create your views here.
from django.http import HttpResponse


def todo(request):
    return render(request, "todo.html")