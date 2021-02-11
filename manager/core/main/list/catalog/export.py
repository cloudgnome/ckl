from main.list.model import ModelAdmin
from catalog.models import Export
from main.forms import ExportForm

class ExportAdmin(ModelAdmin):
    listView = 'List'
    model = Export
    form = ExportForm
    head = (('id','id'),('Товар','product'))
    head_search = (('по id','id'),('',''))
    list_display = ('id','product__name')