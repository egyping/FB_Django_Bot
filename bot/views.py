from django.shortcuts import render
from django.views import generic
from django.views.decorators.csrf import csrf_exempt
from django.utils.decorators import method_decorator
from django.http import HttpResponse









@method_decorator(csrf_exempt, name='dispatch')
class BotAPI(generic.View):

    def get(self, request, *args, **kwargs):
        if self.request.GET['hub.verify_token'] == "123456":
            return HttpResponse(self.request.GET["hub.challenge"])
        else:
            return HttpResponse(" pass code not correct!!")


