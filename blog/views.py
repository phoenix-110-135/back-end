from django.shortcuts import render , get_object_or_404
from blog.models import Post , Category
from django.core.paginator import Paginator , PageNotAnInteger,EmptyPage
# Create your views here.
def blog_view(requests,**kwargs):
    posts = Post.objects.filter(status=1)
    if kwargs.get('cat_name') != None:
        posts = Post.objects.filter(category__name=kwargs['cat_name'])
    if kwargs.get('author_username') != None:
        posts = Post.objects.filter(author__username=kwargs['author_username'])
    posts = Paginator(posts,3)
    try:
        page_number = requests.GET.get('page')
        posts = posts.get_page(page_number)
    except PageNotAnInteger:
        posts = posts.get_page(1)
    except EmptyPage:
        posts = posts.get_page(1)
    context = {'posts':posts}
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

def blog_category(requests,cat_name):
    category = get_object_or_404(Category, name=cat_name)
    posts = Post.objects.filter(category=category)
    context = {'posts': posts}
    return render(requests, 'blog/blog-home.html', context)

def blog_search(requests):
    if requests.method == "GET":
        if s := requests.GET.get("s"):
            post = Post.objects.filter(content__contains=s)
    context = {'posts':post}
    return render(requests,'blog/blog-home.html',context)