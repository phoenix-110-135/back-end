from website.views import *
from django.urls import path


app_name = 'web'

urlpatterns = [
    path("",home_view,name="index"),
    path('get-all-ip/', download_ip_file, name='download-ip'),
    path("elements",elements_view,name="elements"),
    path("about",about_view,name="about"),
    path("contact",contact_view,name="contact"),
    path("blog-home",blog_home_view,name="blog_home"),
    path("blog-single",blog_single_view,name="blog_single"),
    path("http-test",http_test),
    path("json-test",json_test),
    path("test",test,name="test")

    
    
]
