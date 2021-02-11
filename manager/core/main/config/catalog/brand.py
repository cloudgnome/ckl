from main.list.model import ModelAdmin
from catalog.models import Brand
from main.forms import BrandForm

class BrandAdmin(ModelAdmin):
    model = Brand
    form = BrandForm
    order_by = 'name'
    head = (('id','id'),('Название','name'),('Страна','country'))
    head_search = (('по id','id'),('по названию','name__icontains'),('по стране','country__icontains'))
    list_display = ('id','name','country')