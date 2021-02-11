from django.shortcuts import render
from subprocess import Popen, PIPE
from settings import MEDIA_ROOT,BASE_DIR,CACHE_URL
from main.models import Task
from django.http import JsonResponse
from tasks import merchant_task,prices,stock

try:
    from tasks import sync,sync_prices
except:
    pass

try:
    from tasks import rozetka
except:
    pass

try:
    from tasks import hotline
except:
    pass

import shutil
from os.path import isfile
from json import loads
from ast import literal_eval

try:
    from tasks import currency_prices
except:
    pass

__all__ = ['index','merchant_create','prices_sync','drop_cache','task']

def drop_cache(request):
    try:
        shutil.rmtree(CACHE_URL + 'cache/html')
        proc = Popen(['/home/ckl/shop/ffs.sh'], stdin=PIPE, stdout=PIPE, stderr=PIPE)
        output, error = proc.communicate()
        with open('process.log','wb') as f:
            f.write(output + error)

        return JsonResponse({'result':True})
    except:
        return JsonResponse({'result':False})

def calculate_prices(request):
    try:
        task = Task.objects.get(task_type=4)
        task.task_status = 1
        task.save()
    except Task.DoesNotExist:
        Task.objects.create(task_type=4,task_status=1)

    currency_prices.apply_async()

def merchant_create(request,facebook=False):
    try:
        task = Task.objects.get(task_type=1 if not facebook else 3)
        task.task_status = 1
        task.save()
    except Task.DoesNotExist:
        Task.objects.create(task_type=1 if not facebook else 3,task_status=1)

    merchant_task.apply_async((request.GET.get('min_price'),facebook))

    return JsonResponse({'result':True})

def task(request):
    # data = loads(request.body)
    # brands = data.get('brands')
    # task_type = data.get('task_type')

    if 'stock' in request.path:
        try:
            task = Task.objects.get(task_type=5)
            task.task_status = 1
            task.save()
        except Task.DoesNotExist:
            Task.objects.create(task_type=5,task_status=1)

        stock.apply_async()

    elif 'prices' in request.path:
        try:
            task = Task.objects.get(task_type=6)
            task.task_status = 1
            task.save()
        except Task.DoesNotExist:
            Task.objects.create(task_type=6,task_status=1)

        sync_prices.apply_async()

    elif 'rozetka' in request.path:
        try:
            task = Task.objects.get(task_type=7)
            task.task_status = 1
            task.save()
        except Task.DoesNotExist:
            Task.objects.create(task_type=7,task_status=1)

        rozetka.apply_async()

    elif 'hotline' in request.path:
        try:
            task = Task.objects.get(task_type=8)
            task.task_status = 1
            task.save()
        except Task.DoesNotExist:
            Task.objects.create(task_type=8,task_status=1)

        hotline.apply_async()

    return JsonResponse({'result':True})

def prices_sync(request):
    try:
        task = Task.objects.get(task_type=2)
        task.task_status = 1
        task.save()
    except Task.DoesNotExist:
        Task.objects.create(task_type=2,task_status=1)

    prices.apply_async()

    return JsonResponse({'result':True})

def index(request):
    # media_total = system('du -h %s' % MEDIA_ROOT)
    # media = system('du -h --max-depth=1 %s' % MEDIA_ROOT)
    # total = system('df -h /')

    proc = Popen([BASE_DIR + '/manager/core/monitor.sh'], stdin=PIPE, stdout=PIPE, stderr=PIPE)
    output, err = proc.communicate()
    data = output.decode('utf8').replace('\n','').split(' ')

    root = '{CACHE_URL}cache/html/desktop/ru/static/'.format(CACHE_URL=CACHE_URL)
    if not isfile(root + 'categories.html'):
        from catalog.views import StaticView
        StaticView(request,root)

    context = {
        # 'memory_total':data[0],
        # 'memory_used':data[1],
        # 'memory_left':data[2],
        'view':'Home',
        'model':'Home',
        'merchant':Task.objects.filter(task_type=1).first(),
        'facebook_merchant':Task.objects.filter(task_type=3).first(),
        'prices':Task.objects.filter(task_type=2).first(),
        'calculate_prices':Task.objects.filter(task_type=4).first(),
        'stock':Task.objects.filter(task_type=5).first(),
        'nav':root + 'categories.html',
        'sync_stock':Task.objects.filter(task_type=6).first(),
        'rozetka':Task.objects.filter(task_type=7).first(),
        'hotline':Task.objects.filter(task_type=8).first()
    }

    return render(request,'main/base.html',context)