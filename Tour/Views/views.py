from django.shortcuts import render



def index(request):
    return render(request, 'index.html')


def Customer_Home(request):
    return render(request, 'Customer_Home.html')



