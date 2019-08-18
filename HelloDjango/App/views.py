from django.http import HttpResponse
from django.shortcuts import render
from django.views import View
from django.views.generic import TemplateView


def index(request):
    return HttpResponse("Index")


class OrderView(View):

    msg = "哈哈哈"

    def get(self, request):
        return HttpResponse("Order Get%s" % self.msg)

    def post(self, request):
        return HttpResponse("Order Post")

    def put(self, request):
        return HttpResponse("Order Put")

    def delete(self, request):
        return HttpResponse("Order Delete")


class HelloTemplateView(TemplateView):

    template_name = 'Hello.html'