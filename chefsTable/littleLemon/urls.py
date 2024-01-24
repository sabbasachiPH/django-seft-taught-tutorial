from django.urls import path
from . import views

urlpatterns = [
    path('menu/',views.menu),
    path('menu_card/',views.menu_by_id),
    # path('input/',views.input_form),
    # path('tst/',views.test_form)
    
]