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

