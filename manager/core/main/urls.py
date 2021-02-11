from django.conf.urls import url
from .views import *

urlpatterns = [
    url(r'^autocomplete/(?P<Model>[a-zA-Z]+)/(?P<value>.*)$',autocomplete),
    url(r'^order_autocomplete/(?P<value>.*)$',order_autocomplete),
    url(r'^delivery/city/(?P<type>[0-9])/(?P<value>.*)$',city),
    url(r'^delivery/departament/(?P<type>[0-9])/(?P<city_id>[0-9]+)/$',departaments),
    url(r'^delivery/departament/(?P<type>[0-9])/(?P<city_id>[0-9]+)/(?P<value>.*)$',departaments),
    url(r'^prices$', PricesView.as_view(), name='prices'),
    url(r'^stock$', StockView.as_view(), name='stock'),
    url(r'^search/(?P<Model>[a-zA-Z]+)$',search),
    url(r'^gallery/(?P<Model>[a-zA-Z]+)/(?P<id>[0-9]+)/ordering$',ordering),
    url(r'^(?P<Model>[a-zA-Z]+)/list$',items),
    url(r'^add/(?P<Model>[a-zA-Z]+)$',AddView.as_view()),
    url(r'^edit/(?P<Model>[a-zA-Z]+)/(?P<id>[0-9]+)$',EditView.as_view()),
    url(r'^edit/(?P<Model>[a-zA-Z]+)$',EditView.as_view()),
    url(r'^delete/(?P<Model>[_a-zA-Z]+)/(?P<id>[0-9]+)$',delete),
    url(r'^delete/(?P<Model>[_a-zA-Z]+)$',delete),
    url(r'^change_database',change_database),
    url(r'^merchant/create/(?P<facebook>facebook)$',merchant_create),
    url(r'^merchant/create$',merchant_create),
    url(r'^sync/prices$',task),
    url(r'^sync/stock$',task),
    url(r'^sync/rozetka$',task),
    url(r'^sync/hotline$',task),
    url(r'^prices/sync',prices_sync),
    url(r'^drop_cache',drop_cache),
    url(r'^',index)
]