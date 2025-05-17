from django.shortcuts import render , get_object_or_404
from blog.models import Post 
# Create your views here.
def blog_view(requests):
    post = Post.objects.filter(status=1)
    context = {'posts':post}
    return render(requests,'blog/blog-home.html',context)

def blog_single(requests,pid):
    post = get_object_or_404(Post,pk=pid,status=1)
    # posts = Post.objects.filter(status=1)
    # post get_object_or_404(Post,pk=pid,status=1)
    context = {'posts' : post}
    # context= {"title":"title_1","content":"lorem ipsum a difalt image lorem ipsum a difalt image lorem ipsum a difalt image lorem ipsum a difalt image lorem ipsum a difalt image","author":"ALI MOHAMMDI NIA"}
    return render(requests,'blog/blog-single.html',context)

def test(requests,pid):
    # posts = Post.objects.get(id=pid)
    post = get_object_or_404(Post,pk=pid)
    context = {'posts' : post}
    # context = {'name' : name}
    return render(requests,'test.html',context)
