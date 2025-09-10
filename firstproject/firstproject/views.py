from django.http import HttpResponse
from django.shortcuts import render


def home(request):
    # return HttpResponse("Hello world i am learning django")
    return render(request,'index.html')
def about(request):
    # return HttpResponse("Hello world we are in about page")
    return render(request,'about.html')
def contact(request):
    # return HttpResponse("Hello world we are in contact page ")
    return render(request,'contact.html')
def learnmore(request):
    # return HttpResponse("Hello world we are in learn more page")
    return render(request,'learnmore.html')