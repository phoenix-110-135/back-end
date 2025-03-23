from website.views import *
from django.urls import path


app_name = 'web'

urlpatterns = [
    path("",home_view,name="index"),
    path("elements",elements_view),
    path("about",about_view,name="about"),
    path("contact",contact_view,name="contact"),
    path("blog-home",blog_home_view,name="blog_home"),
    path("blog-single",contact_view,name="blog_single"),
    path("http-test",http_test),
    path("json-test",json_test)
    
    
]
