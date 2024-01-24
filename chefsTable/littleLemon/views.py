from django.http import HttpResponse, HttpResponseRedirect,request
from django.shortcuts import render

from littleLemon.models import Menu

# Create your views here.

def home(request):
    return render(request, "index.html")

def about(request):
    return render(request, "about.html")

def menu(request):
    newmenu = {'mains':[
        {'name': 'falafei', 'price':"12"},
        {'name': 'Sharma', 'price':"22"},
        {'name': 'Dosa', 'price':"32"},
        {'name': 'Gryo', 'price':"42"},
    ]}
    return render(request, "menu.html",newmenu)

def menu_by_id(request):
    newmenu = Menu.objects.all()
    newmenu_dict = {"menu": newmenu}
    return render(request, "menu_card.html", newmenu_dict)