from django.shortcuts import render
from django.utils.translation import ugettext_lazy as _

def compare(request):
    context = {
        'title':_('Сравнение товаров'),
        'view':'Compare'
    }

    return render(request,'user/%s/compare.html' % request.folder,context)