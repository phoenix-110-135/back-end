from blog.views import *
from django.urls import path

app_name = 'blog'

urlpatterns = [
    path("",blog_view,name="blog"),
    path("<int:pid>",blog_single,name="single"),
    path("category/<str:cat_name>",blog_view,name="category"),
    path("author/<str:author_username>",blog_view,name="author"),
    path("search/",blog_search,name="search"),
    # path("post-<int:pid>",test,name="test"),
    
    
    
]
