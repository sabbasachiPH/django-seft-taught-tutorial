from django.urls import path
from . import views

urlpatterns = [
    path('',views.home, name='home'),
    path('about/',views.about, name='about'),
    path('menu/',views.menu, name='menu'),
    path('menu_card/',views.menu_by_id, name='menu_card'),
    # path('input/',views.input_form),
    # path('tst/',views.test_form)
    
]