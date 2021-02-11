from django.views.generic import View
from django.shortcuts import render,get_object_or_404
from checkout.forms import CallbackForm
from checkout.models import Order
from catalog.models import Product
from cart.views import Buyer
from json import loads
from django.contrib.auth import login
from django.core.exceptions import PermissionDenied
from user.models import User

class CallbackView(View):
    def get(self,request,*args,**kwargs):
        if request.user.is_anonymous or not request.user.phone:
            form = CallbackForm()
            return render(request,'checkout/%s/callback.html' % request.folder,{'form':form})
        else:
            item = get_object_or_404(Product,id=kwargs['id'],is_available=True)
            cart = Buyer(request).quick_order(item,kwargs.get('qty') or 1)
            Order.objects.create(name=request.user.name or "Перезвонить",phone=request.user.phone,cart=cart)
            form = False
            return render(request,'checkout/%s/callback.html' % request.folder,{'form':form})

    def post(self,request,*args,**kwargs):
        form = CallbackForm(loads(request.body.decode('utf-8')))
        if form.is_valid():
            item = get_object_or_404(Product,id=kwargs['id'],is_available=True)
            cart = Buyer(request).quick_order(item,kwargs.get('qty') or 1)
            Order.objects.create(name=request.user.name or "Перезвонить",phone=form.cleaned_data['phone'],cart=cart)

            if request.user.is_authenticated and not request.user.phone:
                request.user.phone = form.cleaned_data['phone']
                request.user.save()
            elif request.user.is_anonymous:
                try:
                    User.objects.get(phone=form.cleaned_data['phone'])
                except User.DoesNotExist:
                    user = User.objects.create(phone=form.cleaned_data['phone'])

                    user.backend = 'django.contrib.auth.backends.ModelBackend'
                    login(request,user)
                except:
                    pass

            form = False
        return render(request,'checkout/%s/callback.html' % request.folder,{'form':form})