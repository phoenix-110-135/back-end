from blog.views import *
from django.urls import path

app_name = 'blog'

urlpatterns = [
    path("",blog_view,name="blog"),
    path("<int:pid>",blog_single,name="single"),
    # path("post-<int:pid>",test,name="test"),
    
    
    
]
