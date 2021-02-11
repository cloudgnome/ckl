from django.views.generic import View
from user.forms import SignInForm,ForgetPassForm
from django.forms.utils import ErrorList
from django.contrib.auth.hashers import check_password
from django.contrib.auth import login
from django.shortcuts import render,redirect
from django.http import JsonResponse
from user.models import User

class SigninView(View):
    template = 'main/registration/login.html'

    def get(self,request,*args,**kwargs):
        if request.user.is_anonymous:
            context = {
                'next': request.GET.get('next'),
                'form': SignInForm(),
                'view': 'login'
            }
            return render(request, self.template,context)

        elif 'next' in request.GET:
            return redirect(request.GET['next'])
        else:
            return redirect('/')

    def post(self,request,*args,**kwargs):
        if request.user.is_anonymous:
            base = 'base.html' if request.is_ajax() else 'main/%s/index.html' % request.folder
            form = SignInForm(request.POST)
            if form.is_valid():
                user = authenticate(name=form.cleaned_data['phone'], password=form.cleaned_data['password'])
                if user is not None and request.is_ajax():
                    login(request, user)
                    next = request.POST.get('next') or '/'
                    return JsonResponse({'next':next})
            return render(request, self.template,{'base':base,'form':form})
        else:
            return JsonResponse({'next':request.POST.get('next')})

def authenticate(name=None, password=None):
    try:
        user = User.objects.get(name=name)

        if check_password(password, user.password):
            user.backend = 'main.backends.ModelBackend'
            return user
    except:
        pass

    return None