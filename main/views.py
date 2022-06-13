from django.http import HttpResponse
from django.shortcuts import render


def index (request):
    return render (request,'main/index.html')
def payment(request):
    return render(request,'main/payment.html')
def cucumbers(request):
    return render(request,'main/cucumbers.html')
def tomatoes(request):
    return render(request,'main/tomatoes.html')
def cabbage(request):
    return render(request,'main/cabbage.html')
def peppers(request):
    return render(request,'main/peppers.html')
def eggplant(request):
    return render(request,'main/eggplant.html')
def flowers(request):
    return render(request,'main/flowers.html')
def green(request):
    return render(request,'main/green.html')
