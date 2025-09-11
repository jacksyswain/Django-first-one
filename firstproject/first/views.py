from django.shortcuts import render
from .models import products

# Create your views here.
def all_learning(request):
    product= products.objects.all()
    return render(request,'first/all_learning.html',{'product':product})