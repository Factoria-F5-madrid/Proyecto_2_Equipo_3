from django.db import models
from Food5_app.models import Dish

# Create your models here.
class SecondCourse(Dish):

    class Meta:
        db_table = 'second_course'
        managed = False  # Set to False if you want to manage the table manually