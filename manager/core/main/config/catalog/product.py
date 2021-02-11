from main.list.model import ModelAdmin
from catalog.models import Product,Add_Model
from main.forms import ProductForm,GalleryForm,Gallery
from django.db.models import Q
from base64 import b64decode
from django.core.files.base import ContentFile

class ProductAdmin(ModelAdmin):
    listView = 'ListProduct'
    model = Product
    form = ProductForm
    head = (('id','id'),('Название','name'),('',''),('Артикул','model'),('Розничная','retail_price'),('Нал','is_available'),('Произ-тель','brand__name'),('Склад','storage'))
    list_display = ('id','__str__','admin_image','model','price','available','brand_name','get_storage_display')
    head_search = (('по id','id'),('по названию','description__name__icontains'),(),('по артикулу','model__icontains'),('цена','retail_price'),(),('произв.','brand__description__name__icontains'),())

    def get_filters(self,value):
        try:
            int(value)
            return Q(id=value) | Q(model__icontains=value) | Q(description__name__icontains=value)
        except:
            return Q(model__icontains=value) | Q(description__name__icontains=value)

    def saveExtras(self,json,product):
        if json.get('images'):
            for image in json.get('images'):
                try:
                    image = ContentFile(b64decode(image.replace('data:image/jpeg;base64,','')), name='{}.{}'.format(image[27:42],'jpg'))
                    image = Gallery(image=image,product = product)
                    image.save()
                except:
                    continue

        product.add_model.all().delete()
        if json.get('add_model'):
            for model in json.get('add_model'):
                product.add_model.create(model=model)

class Add_ModelAdmin(ModelAdmin):
    model = Add_Model