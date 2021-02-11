# -*- coding=utf-8 -*-
from blog.models import Article
from shop.forms import ReviewForm
from django.views.generic import View
from catalog.models import Product,Offer,City
from catalog.models.special import Special
from shop.models import Slider,Review,Robots
from django.template.response import TemplateResponse
from django.shortcuts import render,get_object_or_404,Http404
from django.core.paginator import Paginator, EmptyPage, PageNotAnInteger
from django.http import HttpResponseNotFound,HttpResponseServerError,JsonResponse,HttpResponse
from shop.context import meta
from json import loads

__all__ = ['categories','ConfirmView','maintenance','PageView','GuestbookView','MainView','HomeView','error500','error404','RobotsView']

def maintenance(request):
    return render(request,'shop/%s/maintenance.html' % request.folder)

def categories(request):
    return render(request,'shop/%s/nav.html' % request.folder)

class HomeView(View):
    def get(self,request,*args,city=None,**kwargs):
        latest = Product.objects.filter(slug__isnull=False,is_available=True).order_by('-id')
        special = Product.objects.filter(special__gt=0,is_available=True)

        if request.user.is_opt:
            latest = latest.filter(storage=1)
            special = special.filter(storage=1)

        itemSlice = 6 if request.folder is 'desktop' else 4

        context = {
            'offers':Offer.objects.filter(product__is_available=True)[:itemSlice],
            'latest':latest[:itemSlice],
            'special':special[:itemSlice],
            'sliders':Slider.objects.all()
        }
        return render(request,'shop/%s/home.html' % request.folder,context)

class MainView(HomeView):
    pass

class PageView(View):
    def get(self,request,*args,**kwargs):
        context = {}
        if request.path == 'igrushki-optom':
            context['products'] = Offer.objects.filter(product__is_available=True)[:17]
        return render(request, 'shop/%s/page.html' % request.folder, context)

class GuestbookView(View):
    def get(self,request,*args,**kwargs):
        context = {}
        reviews = Review.objects.filter(active=True).order_by('-id')
        paginator = Paginator(list(reviews), 9)
        try:
            context['reviews'] = paginator.page(request.GET.get('page') or 1)
        except EmptyPage:
            context['reviews'] = []
        return render(request, 'shop/%s/guestbook.html' % request.folder, context)

    def post(self,request,*args,**kwargs):
        if request.user.is_authenticated:
            form = ReviewForm(loads(request.body.decode('utf-8')))
            if form.is_valid():
                review = form.save()
                review.author = request.user.name
                review.save()
                return JsonResponse({'result':True})
            else:
                return JsonResponse({'result':False,'errors':form.errors})
        else:
            return JsonResponse({'result':False,'authenticate':True})

class RobotsView(View):
    def get(self,request,*args,**kwargs):
        if 'm' in request.get_host().split('.'):
            robots = Robots.objects.get(mobile=True)
        else:
            robots = Robots.objects.first()
        return HttpResponse(robots.body, content_type='text/plain')

class ConfirmView(View):
    def get(self,request,*args,**kwargs):
        f = open('/home/core/shop/ckl.com.ua/static/0B0127C60937ADEB32D6551305975E48.txt')
        return HttpResponse(f.read(), content_type='text/plain')

def error404(request, exception):
    return HttpResponseNotFound(render(request, 'shop/%s/404.html' % request.folder))

def error500(request):
    return HttpResponseServerError(render(request, 'shop/%s/500.html' % request.folder))