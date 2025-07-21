from django.db import models

# Abstract base class for Dish
class Dish(models.Model):
    name = models.CharField(max_length=100)
    calories = models.IntegerField()
    vegan = models.BooleanField(default=False)
    gluten_free = models.BooleanField(default=False)
    purchase_price = models.DecimalField(max_digits=8, decimal_places=2, default=0)
    retail_price = models.DecimalField(max_digits=8, decimal_places=2, default=0)
    picture = models.ImageField(upload_to='dish_pictures/', null=True, blank=True) #The field is optional (null=True, blank=True). Images will be uploaded to MEDIA_ROOT/platos/ (MEDIA_ROOT is set to /media/ in project's settings, is the directory on your server where uploaded files will be stored.).Django’s ImageField requires the Pillow library

    class Meta:
        abstract = True

# Concrete classes inheriting from Dish

class SecondCourse(Dish):
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
    
    second_course = models.ForeignKey(SecondCourse, on_delete=models.CASCADE)
    dessert = models.ForeignKey('app_dessert.Dessert', on_delete=models.CASCADE)
    drink = models.ForeignKey(Drink, on_delete=models.CASCADE)
    bread = models.ForeignKey(Bread, on_delete=models.CASCADE)

    @property #These are not stored in the database, but are calculated on the fly whenever you access them. This ensures the values are always up-to-date, reflecting any changes to the related dishes or menus
    def purchase_price(self):
        return sum([
            self.first_course.purchase_price,
            self.second_course.purchase_price,
            self.dessert.purchase_price,
            self.drink.purchase_price,
            self.bread.purchase_price
        ])

    @property
    def retail_price(self):
        return sum([
            self.first_course.retail_price,
            self.second_course.retail_price,
            self.dessert.retail_price,
            self.drink.retail_price,
            self.bread.retail_price
        ])

class Order(models.Model):
    menus = models.ManyToManyField(Menu)
    customer = models.ForeignKey(Customer, on_delete=models.CASCADE)
    due_date = models.DateTimeField(null=True, blank=True) # menus must be delivered to client on this date
    gotten_date = models.DateTimeField(null=True, blank=True) # order was communicated by client on this date

    @property
    def purchase_price(self):
        return sum(menu.purchase_price for menu in self.menus.all())

    @property
    def retail_price(self):
        return sum(menu.retail_price for menu in self.menus.all())
