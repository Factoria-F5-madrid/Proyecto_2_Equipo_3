from django.db import models
from app_first_course.models import FirstCourse
from app_second_course.models import SecondCourse
from app_dessert.models import Dessert
from app_drink.models import Drink
from app_Bread.models import Bread  # cuidado con las mayúsculas en el nombre de la app

class Menu(models.Model):
    first_course = models.ForeignKey(FirstCourse, on_delete=models.CASCADE)
    second_course = models.ForeignKey(SecondCourse, on_delete=models.CASCADE)
    dessert = models.ForeignKey(Dessert, on_delete=models.CASCADE)
    drink = models.ForeignKey(Drink, on_delete=models.CASCADE)
    bread = models.ForeignKey(Bread, on_delete=models.CASCADE)

    @property
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