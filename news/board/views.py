from django.http import HttpResponse
from django.views import View
from .tasks import hello
from .tasks import hello, printer

class IndexView(View):
    def get(self, request):
        hello.delay()
        return HttpResponse('Hello!')

    def get(self, request):
        printer.delay(10)
        hello.delay()
        return HttpResponse('Hello!')
