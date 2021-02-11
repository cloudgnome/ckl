from django.http import JsonResponse
from django.shortcuts import render
from catalog.models import Product
from django.db.models import Q

def autocomplete(request,Model,value):
    if Model == Product:
        items = Model.objects.filter(Q(description__name__icontains=value) | Q(model__icontains=value)).distinct()[:16]
    else:
        items = Model.objects.filter(description__name__icontains=value).distinct()[:16]

    return JsonResponse({'items':[item.autocomplete_dict() for item in items]})

def order_autocomplete(request,value):
    items = Product.objects.filter(Q(description__name__icontains=value) | Q(model__icontains=value)).distinct()[:16]
    return render(request,'main/autocomplete.html',{'items':items})