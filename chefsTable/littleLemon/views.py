from django.http import HttpResponse, HttpResponseRedirect,request
from django.shortcuts import render

from littleLemon.forms import LogForm
# Create your views here.

def form_view(request):
    form = LogForm
    if request.method == 'POST':
        form = LogForm(request.POST)
        if form.is_valid:
            form.save()            
    context = {"form": form}
    return render(request, "form.html", context)

def about(request):
    content = {'about': 'Lorem ipsum dolor sit amet consectetur adipisicing elit. Id odio corporis nihil, ducimus magni laudantium assumenda voluptatum itaque alias veniam non ad rem beatae commodi, doloribus modi explicabo fuga perspiciatis.'}
    return render(request, "about.html",content)

# def menu(request):
#     menuitem = {'name': 'Greek Salad'}
#     return render(request, "menu.html",menuitem)

def menu(request):
    newmenu = {'mains':[
        {'name': 'falafei', 'price':"12"},
        {'name': 'Sharma', 'price':"22"},
        {'name': 'Dosa', 'price':"32"},
        {'name': 'Gryo', 'price':"42"},
    ]}
    return render(request, "menu.html",newmenu)

