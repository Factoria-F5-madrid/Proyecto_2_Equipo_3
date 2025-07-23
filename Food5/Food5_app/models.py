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




class Customer(models.Model):
    name = models.CharField(max_length=100)
    address = models.CharField(max_length=255)
    email = models.EmailField(unique=True)



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
