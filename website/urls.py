from website.views import *
from django.urls import path

urlpatterns = [
    path("",home_view),
    path("about",about_view),
    path("contact",contact_view),
    path("http-test",http_test),
    path("json-test",json_test)
    
    
]
