from django.urls import path
from . import views

urlpatterns = [
    path('',views.home),
    path('dishes/<str:dish>',views.menuitems),
    path('display_date/',views.display_date),
    path('menu/',views.menu),
    path('form/',views.form_view),
    # path('input/',views.input_form),
    # path('tst/',views.test_form)
    
]