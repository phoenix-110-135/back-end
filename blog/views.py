from django.shortcuts import render
from blog.models import Post 
# Create your views here.
def blog_view(requests):
    return render(requests,'blog/blog-home.html')

def blog_single(requests):
    context= {"title":"title_1","content":"lorem ipsum a difalt image lorem ipsum a difalt image lorem ipsum a difalt image lorem ipsum a difalt image lorem ipsum a difalt image","author":"ALI MOHAMMDI NIA"}
    return render(requests,'blog/blog-single.html',context)

def test(requests):
    posts = Post.objects.all()
    context = {'posts':posts}
    return render(requests,'test.html',context)