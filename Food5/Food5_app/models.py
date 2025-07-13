from django.db import models

# Abstract base class for Dish
class Dish(models.Model):
    name = models.CharField(max_length=100)
    calories = models.IntegerField()
    vegan = models.BooleanField(default=False)
    gluten_free = models.BooleanField(default=False)
    purchase_price = models.DecimalField(max_digits=8, decimal_places=2)
    sale_price = models.DecimalField(max_digits=8, decimal_places=2)
    picture = models.ImageField(upload_to='dish_pictures/', null=True, blank=True) #The field is optional (null=True, blank=True). Images will be uploaded to MEDIA_ROOT/platos/ (MEDIA_ROOT is set to /media/ in project's settings, is the directory on your server where uploaded files will be stored.).Django’s ImageField requires the Pillow library

    class Meta:
        abstract = True

# Concrete classes inheriting from Dish
class FirstCourse(Dish):
    pass

class SecondCourse(Dish):
    pass

class Dessert(Dish):
    pass

class Drink(Dish):
    pass

class Bread(Dish):
    pass

class Customer(models.Model):
    name = models.CharField(max_length=100)
    address = models.CharField(max_length=255)
    email = models.EmailField(unique=True)

class Menu(models.Model):
    first_course = models.ForeignKey(FirstCourse, on_delete=models.CASCADE)
    second_course = models.ForeignKey(SecondCourse, on_delete=models.CASCADE)
    dessert = models.ForeignKey(Dessert, on_delete=models.CASCADE)
    drink = models.ForeignKey(Drink, on_delete=models.CASCADE)
    bread = models.ForeignKey(Bread, on_delete=models.CASCADE)

class Order(models.Model):
    menus = models.ManyToManyField(Menu)
    customer = models.ForeignKey(Customer, on_delete=models.CASCADE)
