from django.http import Http404
from django.shortcuts import render
from django.http import HttpResponseServerError, HttpResponseNotAllowed

class Handle404Middleware:
    def __init__(self, get_response):
        self.get_response = get_response

    def __call__(self, request):
        response = self.get_response(request)
        if response.status_code == 404:
            # Handle 404 error here
            return handle_404_error(request)
        return response

def handle_404_error(request):
    # You can implement your custom logic here, like logging or redirecting
    # For simplicity, let's just render a template
    return render(request,'error/404.html',status=500)




class HandleErrorsMiddleware:
    def __init__(self, get_response):
        self.get_response = get_response

    def __call__(self, request):
        response = self.get_response(request)
        if response.status_code == 500:
            # Handle 500 Internal Server Error
            return self.handle_500_error(request)
        elif response.status_code == 505:
            # Handle 505 HTTP Version Not Supported
            return self.handle_505_error(request)
        return response

    def handle_500_error(self, request):
        # Custom handling for 500 Internal Server Error
        return render(request,'error/505.html',status=500)

    def handle_505_error(self, request):
        # Custom handling for 505 HTTP Version Not Supported
        return render(request,'error/505.html',status=505)
