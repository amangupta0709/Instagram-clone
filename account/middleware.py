from django.contrib.auth.hashers import make_password, check_password


class passwordencryption:
    def __init__(self, get_response):
        self.get_response = get_response
        # One-time configuration and initialization.

    def __call__(self, request):
        # Code to be executed for each request before
        # the view (and later middleware) are called.
        if request.method == 'POST':
            request.POST = request.POST.copy()
            encrypted = make_password(request.POST['password'])
            request.POST['password'] = encrypted
            print(request.POST['password'])


        response = self.get_response(request)

        # Code to be executed for each request/response after
        # the view is called.

        return response