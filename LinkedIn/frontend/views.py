from django.shortcuts import render

def Home(request):
    return render(request,'output/home.html')

def network(request):
    return render(request,'output/network.html')