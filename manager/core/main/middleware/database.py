from main.list import *

class DatabaseMiddleware:
    def __init__(self, get_response):
        self.get_response = get_response
        # One-time configuration and initialization.

    def __call__(self, request):
        # Code to be executed for each request before
        # the view (and later middleware) are called.
        limit = request.GET.get('limit')
        session_limit = request.session.get('limit')

        if not session_limit or (limit and session_limit != limit):
            request.session['limit'] = limit or 9

        response = self.get_response(request)

        # Code to be executed for each request/response after
        # the view is called.

        return response

    def process_view(self, request, view_func, view_args, view_kwargs):
        model = view_kwargs.get('Model')

        if model:
            Model = eval(model[0].capitalize() + model[1:] + 'Admin')
            # view_args += (Model(database=request.session.get('database')),)
            view_kwargs['Model'] = Model()

            return view_func(request,*view_args,**view_kwargs)
