from django.core.management.base import BaseCommand, CommandError
import os
from django.utils import timezone
from settings import BASE_DIR, DOMAIN, JS_BUILD, CSS_BUILD

try:
    from settings import SPRITE_CATEGORIES
except:
    SPRITE_CATEGORIES = None

class Command(BaseCommand):
    help = 'Create Static'
    css = ['font-awesome-5.0/css/all.min','select','main','login','categories','category','edit',
            'list','order','menu','home']

    js = ['core/jquery.min','core/jquery.ui.min','core/vanilla','core/http','core/select',
            'main','menu','templates',
            'category/category',
            'views/base','views/login','views/edit/autocomplete',
            'views/edit/base','views/edit/brand','views/edit/cart','views/edit/category',
            'views/edit/default','views/edit/fgk','views/edit/gallery','views/edit/home',
            'views/edit/order','views/edit/product','views/edit/tag',
            'views/list/base','views/list/category','views/list/googlefeed',
            'views/list/order','views/list/product',
            'core/router']

    buildPath = '{baseDir}/manager/static/min{build}.{type}'
    base_path = '{baseDir}/manager/core/static/{type}/{name}.{type}'
    domain_path = '{baseDir}/manager/static/{type}/{name}.{type}'

    dirname = os.path.dirname('{BASE_DIR}'.format(BASE_DIR=BASE_DIR))
    category_sprite = '{dirname}/ckl/shop/static/css/desktop/categorySprite.css'.format(dirname=dirname,DOMAIN=DOMAIN)

    def cache(self,type,buildType):
        buildPath = self.buildPath.format(baseDir=BASE_DIR,DOMAIN=DOMAIN,type=type,build=buildType)
        category_sprite = self.category_sprite.format(DOMAIN=DOMAIN)
        with open(buildPath,'w',encoding='utf-8') as build:
            for name in getattr(self,"%s" % type):
                try:
                    file = self.domain_path.format(baseDir=BASE_DIR,type=type,name=name)
                    file = open(file)
                except:
                    file = self.base_path.format(baseDir=BASE_DIR,type=type,name=name)
                    file = open(file)

                print(file)

                text = file.read().replace('\n','').replace('\t','')
                build.write(text)

            if SPRITE_CATEGORIES and type == 'css':
                with open(category_sprite,'r') as f:
                    build.write(f.read())

            print('\nResult:')
            print(buildPath)
            print('\n\n')

    def add_arguments(self, parser):
        parser.add_argument('--type', nargs='+', type=str)

    def handle(self, *args, **options):
        time = timezone.now()
        if options['type']:
            self.cache(options['type'][0],buildType=eval(options['type'][0].upper() + '_BUILD'))
        else:
            for t in ['css','js']:
                self.cache(t,buildType=eval(t.upper() + '_BUILD'))

        print('Time: %s' % (timezone.now() - time))
        print('Complete.')