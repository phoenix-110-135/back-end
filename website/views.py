from django.shortcuts import render
from django.http import HttpResponse,JsonResponse


def home_view(requests):
    return render(requests,'website\index.html')

def about_view(requests):
    return render(requests,'about.html')

def contact_view(requests):
    return render(requests,'contact.html')

def http_test(requests):
    return HttpResponse("<h1>good</h1>")

def json_test(requests):
    return JsonResponse({"response" : 200})

