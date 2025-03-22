from django.shortcuts import render
from django.http import HttpResponse,JsonResponse


def home_view(requests):
    return HttpResponse("<h1>HOME</h1>")

def about_view(requests):
    return HttpResponse("<h1>ABOUT</h1>")
def contact_view(requests):
    return HttpResponse("<h1>CONTACT</h1>")
def http_test(requests):
    return HttpResponse("<h1>good</h1>")

def json_test(requests):
    return JsonResponse({"response" : 200})

