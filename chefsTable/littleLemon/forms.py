# import the standard Django Forms 
# from built-in library 
from django import forms 
from django.forms.widgets import NumberInput	


# creating a form 
# Tutorial time 3:00:00
SHIFT = [
	("1","Morning"),
	("2","Afternoon"),
	("3","Evening"),
]

class InputForm(forms.Form): 	
	first_name = forms.CharField(max_length = 200) 
	last_name = forms.CharField(max_length = 200) 
	shift = forms.ChoiceField(choices = SHIFT)
	time_log = forms.TimeField(help_text="Enter the exact time")
 
	
# FAVOURITE_DISH = [
# 	('italian','Italian'),
# 	('french','French'),
# 	('mexican', 'Mexican'),
# 	('greek', 'Greek'),
# 	('turkish', 'Turkish'),
# ]

# class demoForm(forms.Form):
# 	test_name = forms.CharField(label = "Test Name",max_length =200)
# 	test_email = forms.EmailField(label = "Your Email Address")
# 	test_reservation_date = forms.DateField(label = "Reservation Date", widget = forms.NumberInput(attrs={'type': 'date'}))
# 	test_favourite_dish = forms.ChoiceField(label = "Choose Favourite Item", choices = FAVOURITE_DISH )
# 	test_radio_dish = forms.ChoiceField(label = "Click on Favourite Item", widget = forms.RadioSelect, choices = FAVOURITE_DISH )
# 	test_address = forms.CharField(label = "Test Address",max_length =200, widget = forms.Textarea(attrs={'rows':2}))
