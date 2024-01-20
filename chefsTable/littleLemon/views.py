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

