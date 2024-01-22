from django.urls import path
from . import views

urlpatterns = [
    path('form/',views.form_view),
    path('about/',views.about),
    # path('input/',views.input_form),
    # path('tst/',views.test_form)
    
]