from django.shortcuts import render, HttpResponse
from django.http import JsonResponse
from django.core.serializers import serialize
from .models import User

# Create your views here.
def home(request):
    return HttpResponse("welcome")

def users(request):
    users = User.objects.all()
    users_json = serialize('json', users)
    return JsonResponse(users_json, safe=False)