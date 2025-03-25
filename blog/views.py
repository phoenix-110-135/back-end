from django.shortcuts import render

# Create your views here.
def blog_view(requests):
    return render(requests,'blog/blog-home.html')

def blog_single(requests):
    context= {"title":"title_1","content":"lorem ipsum a difalt image lorem ipsum a difalt image lorem ipsum a difalt image lorem ipsum a difalt image lorem ipsum a difalt image","author":"ALI MOHAMMDI NIA"}
    return render(requests,'blog/blog-single.html',context)