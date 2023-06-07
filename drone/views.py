from django.shortcuts import render
from django.http import HttpResponse


def my_view(request):
    return render(request, 'drone/home.html')


def another_view(request):
    return HttpResponse("This is another view.")
