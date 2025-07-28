from django.db import models
from app_customer.models import Customer
from app_menu.models import Menu


# Create your models here.

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