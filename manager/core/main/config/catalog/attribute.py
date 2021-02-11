from main.list.model import ModelAdmin
from catalog.models import Attribute
from django.db.models import Q
from main.forms import AttributeForm

class AttributeAdmin(ModelAdmin):
    model = Attribute
    form = AttributeForm
    head = (('id','id'),('Название','name'))
    head_search = (('по id','id'),('по названию','name__icontains'))
    list_display = ('id','name')
    editTemplate = 'main/edit.html'

    def get_filters(self,value):
        return Q(name__icontains=value) | Q(values__value__icontains=value)

    def saveExtras(self,json,attribute):
        attribute.values.all().delete()
        if json.get('value'):
            for value in json.get('value'):
                attribute.values.create(value=value)