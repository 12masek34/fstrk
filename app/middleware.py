
from django.utils.deprecation import MiddlewareMixin
from django.http import HttpResponse


class AlwaysReturn200Middleware(MiddlewareMixin):

    def __call__(self, request):
        response = self.get_response(request)

        if response.status_code != 200:
            response.status_code = 200

        return response

    def process_exception(self, request, exception):
        return HttpResponse(b"", status=200)
