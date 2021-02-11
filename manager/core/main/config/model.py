from django.db.models import Q
from django.template.loader import get_template
from json import loads
from main.forms import PageDescriptionForm,CategoryDescriptionForm, \
BrandDescriptionForm,TagDescriptionForm,CityDescriptionForm,ArticleDescriptionForm

class ModelAdmin:
    exclude = {}
    listView = 'List'
    editTemplate = 'main/slug.html'
    # meta = DescriptionForm
    searchHtml = 'main/items.html'
    listHtml = 'main/list.html'
    database = 'default'

    @property
    def meta(self):
        return eval('%sDescriptionForm' % self.__str__())

    def __init__(self,database):
        self.database = database

    def context(self,item):
        return {}

    def extraContext(self,context):
        return context

    def saveExtras(self,request,item):
        return

    @property
    def panel(self):
        try:
            panel = 'main/panel/%s.html' % self.__str__().lower()
            get_template(panel)
        except:
            panel = 'main/panel/default.html'

        return panel

    @property
    def ordering(self):
        return self.order_by or '-id'

    def __str__(self):
        return self.model.__name__

    def __len__(self):
        return len(self.list_display)

    def __iter__(self):
        for field in self.list_display:
            yield field

    def __getattr__(self,name):
        if hasattr(self.model,name):
            # if name == 'objects':
            #     return getattr(self.model,name).using(self.database)
            return getattr(self.model,name)

        return None

    def filters(self,request):
        filters = {}

        if request.body:
            filters = loads(request.body.decode('utf8'))
            return Q(**filters)

        if request.GET:
            for field in request.GET:
                if field in ['block','page','limit','o','all']:
                    continue
                try:
                    value = eval(request.GET[field])
                    if value is None:
                        raise Exception()
                except:
                    value = request.GET[field]
                filters[field] = value

            return Q(**filters)

        return Q()

    def search(self,value):
        if not value:
            return Q()

        return Q(name__icontains=value)

    def get_filters(self,value):
        return Q(name__icontains=value)