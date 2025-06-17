from django import template
from blog.models import Post
from blog.models import Category

register = template.Library()


@register.simple_tag(name="totalpost")
def func():
    posts = Post.objects.filter(status=1).count()
    return posts 

@register.simple_tag(name="posts")
def func():
    posts = Post.objects.filter(status=1)
    return posts 


@register.filter
def snippet(value,args=20):
    return value[:args] + "...."

@register.inclusion_tag("blog/blog-popular-post.html")
def latestsposts(arg=3):
    posts = Post.objects.filter(status=1).order_by('published_date')[:arg]
    return {"posts": posts}

@register.inclusion_tag("blog/blog-category.html")
def postcategory():
    posts = Post.objects.filter(status=1).order_by('published_date')
    cat_dict = {}
    categories = Category.objects.all()
    for name in categories: 
        cat_dict[name]=posts.filter(categories=name).count()
    return {'categories' : cat_dict}