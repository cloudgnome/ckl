from django.contrib.auth.signals import user_logged_out
from django.shortcuts import redirect
from django.http import JsonResponse
# from django.utils.translation import LANGUAGE_SESSION_KEY
from user.models import AnonymousUser

def logout(request,lang = 'ru'):
    """
    Removes the authenticated user's ID from the request and flushes their
    session data.
    """
    # Dispatch the signal before the user is logged out so the receivers have a
    # chance to find out *who* logged out.
    user = getattr(request, 'user', None)
    if hasattr(user, 'is_authenticated') and not user.is_authenticated:
        user = None
    user_logged_out.send(sender=user.__class__, request=request, user=user)

    if hasattr(request, 'user'):
        request.user = AnonymousUser()

    # orders = Order.objects.filter(user=user)
    # if orders:
    #   from django.contrib.sessions.backends.db import SessionStore
    #   session = SessionStore()
    #   session.save()
    #   request.session = session
    # else:
    request.session.flush()

    if request.is_ajax():
        return JsonResponse({'result':1})
    else:
        return redirect(request.META['HTTP_REFERER'])