from django.http import HttpResponse
import csv
from app_Bread.models import Bread
from app_dessert.models import Dessert
from app_drink.models import Drink
from app_first_course.models import FirstCourse
from app_second_course.models import SecondCourse
from app_customer.models import Customer
from app_order.models import Order
from app_menu.models import Menu

def exportAllToCsv(request):
    # Creamos la respuesta HTTP con tipo CSV
    response = HttpResponse(content_type='text/csv')
    response['Content-Disposition'] = 'attachment; filename="all_data.csv"'
    writer = csv.writer(response)

    # Exportar modelos que heredan de Dish (platos con los mismos campos)
    dish_models = [
        (Bread, 'Bread'),
        (Dessert, 'Dessert'),
        (Drink, 'Drink'),
        (FirstCourse, 'First Course'),
        (SecondCourse, 'Second Course')
    ]

    # Encabezados para los platos
    writer.writerow(['Model', 'ID', 'Name', 'Calories', 'Vegan', 'Gluten Free', 'Purchase Price', 'Retail Price'])
    
    # Escribimos los datos de cada modelo de plato
    for model, name in dish_models:
        for obj in model.objects.all():
            writer.writerow([
                name,
                obj.id,
                obj.name,
                obj.calories,
                obj.vegan,
                obj.gluten_free,
                obj.purchase_price,
                obj.retail_price
            ])
    #=========================================================
    writer.writerow([])

    # Exportar datos de los clientes
    writer.writerow(['Customer', 'ID', 'Name', 'Address', 'Email'])
    for c in Customer.objects.all():
        writer.writerow(['Customer', c.id, c.name, c.address, c.email])
    writer.writerow([])

    # Exportar datos de los menús
    writer.writerow(['Menu', 'ID', 'FirstCourse', 'SecondCourse', 'Dessert', 'Drink', 'Bread'])
    for m in Menu.objects.all():
        writer.writerow([
            'Menu',
            m.id,
            str(m.first_course),
            str(m.second_course),
            str(m.dessert),
            str(m.drink),
            str(m.bread)
        ])
    #=========================================================
    writer.writerow([])

    # Exportar datos de los pedidos
    writer.writerow(['Order', 'ID', 'Customer', 'Due Date', 'Gotten Date', 'Menus'])
    for o in Order.objects.all():
        writer.writerow([
            'Order',
            o.id,
            str(o.customer),
            o.due_date,
            o.gotten_date,
            '; '.join(str(m) for m in o.menus.all())  # Lista de menús separados por ;
        ])

    return response
