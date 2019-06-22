import random

from django.shortcuts import render
from django.http.response import JsonResponse


def index(request):
    return render(request, "index.html")


def stats(request):
    return JsonResponse({"hello": random.randint(0, 314)})

