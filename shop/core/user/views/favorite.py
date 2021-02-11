from django.shortcuts import render
from django.utils.translation import ugettext_lazy as _

def favorite(request):
    context = {
        'title':_('Избранные товары'),
        'view':'Favorite'
    }
    return render(request,'user/%s/favorite.html' % request.folder,context)