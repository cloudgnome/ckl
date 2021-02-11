from main.models import Task
from settings import BASE_DIR,DOMAIN,CACHE_URL,STATIC_ROOT,COMPANY_NAME
from bs4 import BeautifulSoup
from catalog.models import Product,Currency,Category,Special
from math import ceil
import shutil
from impexp import load,dump
from django.utils import timezone
import datetime
import pathlib
from django.template.loader import render_to_string

try:
    from settings import PARENT_DATABASE
except:
    PARENT_DATABASE = None

try:
    from settings import HOST,PROTOCOL
except:
    HOST = PROTOCOL = None

text = '{model}\t{title}\t{description}\t{link}\t{image_link}\t{availability}\t{price}\t{brand}\t{category}'
text_facebook = '{model}\t{title}\t{description}\t{link}\t{image_link}\t{availability}\t{price}\t{brand}\t{category}\t{condition}'

def merchant_task(min_price,categories=[],facebook=False):
    domain = 'https://%s/' % DOMAIN
    domain_image = 'https://%s' % DOMAIN

    try:
        float(min_price)
    except:
        min_price = 0

    if not facebook:
        with open('{BASE_DIR}/{DOMAIN}/static/google_feed.txt'.format(BASE_DIR=BASE_DIR,DOMAIN=DOMAIN),'w') as f:
            f.write('id\ttitle\tdescription\tlink\timage_link\tavailability\tprice\tbrand\tgoogle product category')
            f.write('\n')
            if categories:
                categories = Category.objects.filter(id__in=categories).get_descendants()
                products = Product.objects.filter(is_available=True,retail_price__gte=min_price,category__in=categories)
            else:
                products = Product.objects.filter(is_available=True,retail_price__gte=min_price)

            for product in products:
                description = product.description.filter(language__code='ru').first() or ''
                if description:
                    try:
                        description = BeautifulSoup(description.text, "html.parser").text.replace('\n','').replace('\t','')[:5000]
                    except:
                        description = ''
                f.write(text.format(model=product.model,title=product.names(lang='ru'),description=description,link=domain + product.slug,image_link=domain_image + product.image.list_thumb,availability=product.google_availability,price=str(product.price) + ' UAH',brand=product.brand_name,category=product.google_category_name()))
                f.write('\n')

        Task.objects.filter(task_type=1).update(task_status=2)

    else:
        with open('{BASE_DIR}/{DOMAIN}/static/facebook_feed.txt'.format(BASE_DIR=BASE_DIR,DOMAIN=DOMAIN),'w') as f:
            f.write('id\ttitle\tdescription\tlink\timage_link\tavailability\tprice\tbrand\tgoogle product category\tcondition')
            f.write('\n')
            for product in Product.objects.filter(is_available=True,retail_price__gte=min_price):
                description = product.description.filter(language__code='ru').first() or ''
                if description:
                    try:
                        description = BeautifulSoup(description.text, "html.parser").text.replace('\n','').replace('\t','')[:5000]
                    except:
                        description = ''
                f.write(text_facebook.format(model=product.model,title=product.names(lang='ru'),description=description,link=domain + product.slug,image_link=domain_image + product.image.list_thumb,availability=product.google_availability,price=str(product.price) + ' UAH',brand=product.brand_name,category=product.google_category_name(),condition='new'))
                f.write('\n')

        Task.objects.filter(task_type=3).update(task_status=2)

def currency_prices():
    try:
        task = Task.objects.get(task_type=4)
        task.task_status = 1
        task.save()
    except Task.DoesNotExist:
        Task.objects.create(task_type=4,task_status=1)

    for p in Product.objects.filter(currency=0):
        p.retail_price = ceil(p.retail_price)

        p.update()

    for p in Product.objects.exclude(currency=0):
        cur = Currency.objects.get(type=p.currency)
        p.retail_price = ceil(p.purchase_price * cur.value)

        p.update()

    shutil.rmtree(CACHE_URL + 'cache/html')

    Task.objects.filter(task_type=4).update(task_status=2)

def prices(verbose=False,brands=[]):
    output = {}
    not_found = {}

    for product in Product.objects.using('igroteka').filter(brand_id__in=brands):
        try:
            p = Product.objects.using('default').get(model=product.model)
            output[p.model] = p.name
        except Product.DoesNotExist:
            not_found[product.model] = product.name
            continue

        p.retail_price = product.retail_price
        p.big_opt_price = product.big_opt_price
        p.is_available = product.is_available

        if hasattr(product,'special'):
            try:
                Special.objects.create(product=p,price=product.special.price)
            except:
                p.special.price=product.special.price
                p.special.save()
        elif hasattr(p,'special'):
            p.special.delete()

        if verbose:
            p.update()
        else:
            p.save()

    Task.objects.filter(task_type=2).update(task_status=2)

    if verbose:
        return {'output':output,'not_found':not_found}

def sync(verbose=False,brands=[]):
    if not PARENT_DATABASE:
        return

    output = {}

    items = Product.objects.using(PARENT_DATABASE).filter(brand__id__in=brands)

    related,data = dump(items)

    if related and data:
        load(related,data)

    Task.objects.filter(task_type=5).update(task_status=2)

def stock(verbose=False):
    items = Product.objects.values('model').all()

    if verbose:
        print(items)

    for item in items:
        try:
            result = Product.objects.using(PARENT_DATABASE).values('is_available').get(model=item.get('model'))
            Product.objects.filter(model=item.get('model')).update(
                is_available=result.get('is_available'),
            )

        except Product.DoesNotExist:
            if verbose:
                print('not_found:' + item.get('model'))
            continue

    Task.objects.filter(task_type=5).update(task_status=2)

def sync_prices(verbose=False):
    items = Product.objects.values('model').all()

    if verbose:
        print(items)

    for item in items:
        try:
            result = Product.objects.using(PARENT_DATABASE).values('id','special__price','big_opt_price','retail_price').get(model=item.get('model'))
            Product.objects.filter(model=item.get('model')).update(
                retail_price=result.get('retail_price'),
                big_opt_price=result.get('big_opt_price')
            )

            p = Product.objects.get(model=item.get('model'))
            if result.get('special__price'):
                try:
                    Special.objects.create(product=p,price=result.get('special__price'))
                except:
                    p.special.price = result.get('special__price')
                    p.special.save()

            elif hasattr(p,'special'):
                p.special.delete()

        except Product.DoesNotExist:
            if verbose:
                print('not_found:' + item.get('model'))
            continue

    Task.objects.filter(task_type=6).update(task_status=2)

def rozetka(verbose=False,products=None):
    if HOST and PROTOCOL:
        context = {
            'categories':Category.objects.filter(active=True),
            'products':products or Product.objects.filter(is_available=True,slug__isnull=False,qty__gt=0),
            'HOST':HOST,
            'PROTOCOL':PROTOCOL,
            'COMPANY_NAME':COMPANY_NAME
        }

        content = render_to_string('main/export.xml', context).replace('\n','').replace('\t','').replace('    ','')
        with open(STATIC_ROOT + 'export.xml','w') as f:
            f.write(content)

    Task.objects.filter(task_type=7).update(task_status=2)

def hotline(verbose=False):
    if HOST and PROTOCOL:
        context = {
            'categories':Category.objects.filter(active=True),
            'products':Product.objects.filter(is_available=True,slug__isnull=False,qty__gt=0,retail_price__gte=250),
            'HOST':HOST,
            'PROTOCOL':PROTOCOL,
            'COMPANY_NAME':COMPANY_NAME
        }

        content = render_to_string('main/export1.xml', context).replace('\n','').replace('\t','').replace('    ','')
        with open(STATIC_ROOT + 'export1.xml','w') as f:
            f.write(content)

    Task.objects.filter(task_type=8).update(task_status=2)