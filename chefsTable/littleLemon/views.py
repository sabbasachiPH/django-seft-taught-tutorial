from django.http import HttpResponse, HttpResponseRedirect,request
from django.shortcuts import render


from datetime import datetime
from .forms import InputForm
# Create your views here.

def form_view(request):
    form = InputForm
    context = {"form": form}
    return render(request, "form.html", context)


def input_form(request): 
    context ={} 
    context['form']= InputForm() 
    return render(request, "home.html", context) 

# def test_form(request): 
#     context ={} 
#     context['form']= demoForm() 
#     return render(request, "nameForm.html", context) 



def home(request):
    path = request.path
    scheme = request.scheme
    method = request.method
    path_info = request.path_info
    address = request.META['REMOTE_ADDR']
    user_agent = request.META['HTTP_USER_AGENT']
    msg = f"""
        <br>Path :{path }
        <br>Scheme :{scheme }
        <br>Method :{method }
        <br>Path Info :{path_info }
        <br>Address :{address }
        <br>User Agent :{user_agent }
    """
    return HttpResponse(msg, content_type='text/html', charset='utf-8')


def menuitems(request, dish):
    items = {
        'pasta': 'Pasta is a type of noodle made from combination of wheat , water or eggs.',
        'falafel': 'falafel are deep fried patties or balls made....',
        'cheesecake': 'Cheese Cake is a type of dessert made with cream, soft cheese on top of cookie, pastry crust or graham cracker and fruit sauce topping.'
    }
    description = items[dish]
    return HttpResponse(f"<h2>{dish}</h2>"+description)


def display_date(request):
    date_joined = datetime.today().year
    return HttpResponse(date_joined)

def menu(request):
    formContent = """<h1 style="color:#f4CE14;" >This is Little Lemon Again!</h1>
    
    """
    return HttpResponse(formContent)

# def hi(request):
#     return HttpResponse(f'Hi form Little Lemon')

# def menu_by_id(request, menu_id):
#     menu = Menu.objects.get(pk=menu_id)
#     return HttpResponse(f"{menu.menu_item}: Type of {menu.cuisine} cuisine")
