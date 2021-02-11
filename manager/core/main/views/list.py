from django.shortcuts import render
from django.http import JsonResponse,Http404
from django.core.paginator import Paginator, EmptyPage, PageNotAnInteger

def items(request,Model):
    page = request.GET.get('page')
    block = request.GET.get('block')
    limit = request.session.get('limit')

    ordering = request.GET.get('o') or Model.ordering
    filters = request.GET.copy()
    all = request.GET.get('all')

    if request.is_ajax() and block:
        template = 'main/items.html'
    else:
        template = 'main/list.html'

    query = Model.filters(request)

    if query:
        items = Model.objects.filter(query).order_by(ordering).distinct()
    else:
        items = Model.objects.filter(query).exclude(**Model.exclude).order_by(ordering).distinct()

    count = items.count()

    if not all:
        item = items[:20]

        paginator = Paginator(items, limit)
        try:
            items = paginator.page(page or 1)
        except EmptyPage:
            items = paginator.page(1)

    context = {
        'items':items,
        'model':Model,
        'page':page,
        'view':Model.listView,
        'filters':filters,
        'panel':Model.panel,
        'count':count
    }


    return render(request,template,context)