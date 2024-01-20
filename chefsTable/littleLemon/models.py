from django.db import models

# Create your models here.
class MenuCategory(models.Model):
    menu_category_name = models.CharField(max_length = 200)

class Menu(models.Model):
    menu_item = models.CharField(max_length = 200)
    price = models.IntegerField()
    category_id = models.ForeignKey(MenuCategory, on_delete=models.PROTECT, default=None)



class Customer(models.Model):
    name = models.CharField(max_length = 200)
    reservation_day = models.CharField(max_length=20)
    seats = models.IntegerField()

    def __str__(self):
        return self.name +" : On " + self.reservation_day + "requested for" + self.seats + "seats"

# class Menu(models.Model):
#     name = models.CharField(max_length = 100)
#     cuisine = models.CharField(max_length=100)
#     price = models.IntegerField()

#     def __str__(self):
#         return self.name +" : " + self.cuisine

class Menuitems(models.Model):
    itemname = models.CharField(max_length = 200)
    category = models.CharField(max_length=300)
    year = models.IntegerField()

    def __str__(self):
        return self.itemname +" : " + self.category + " : " + self.year


