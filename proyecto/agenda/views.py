from django.views.generic import TemplateView
from django.http import HttpResponse, JsonResponse
from django.views import View
from django.views.generic.list import ListView
from django.views.decorators.csrf import csrf_exempt
from django.utils.decorators import method_decorator
from .models import create_list
import json

class laprincipal(ListView):
    template_name = "agenda.html"
    model = create_list
    ordering = ['-id']

class agendaApi(View):
    def get(self, request):
        data = create_list.objects.all()
        print(data)
        cnt = create_list(namel = data['nm'], userl = data['us'], datecl = data['dtc'], dateml = data['dtm'])
        cnt.save()
        return JsonResponse(data, safe=False)
    def post(self, request):
        data = list(create_list.objects.values())
        print(data)
        cnt = create_list(namel = data['nm'], userl = data['us'], datecl = data['dtc'], dateml = data['dtm'])
        cnt.save()
        return JsonResponse(data, safe=False)