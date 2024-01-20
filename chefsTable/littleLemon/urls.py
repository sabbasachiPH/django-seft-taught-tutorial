from django.urls import path
from . import views

urlpatterns = [
    path('form/',views.form_view),
    # path('input/',views.input_form),
    # path('tst/',views.test_form)
    
]