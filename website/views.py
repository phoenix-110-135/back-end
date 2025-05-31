from django.shortcuts import render
from django.http import HttpResponse,JsonResponse , FileResponse,HttpResponseNotFound
import os 

def download_ip_file(request):
    file_path = os.path.join(os.path.dirname(__file__), '../data/ip_logs.txt')
    if os.path.exists(file_path):
        return FileResponse(open(file_path, 'rb'), as_attachment=True, filename='ip_logs.txt')
    else:
        return HttpResponseNotFound("فایل پیدا نشد.")


def home_view(requests):
    return render(requests,'website\index.html')

def about_view(requests):
    return render(requests,'website/about.html')

def contact_view(requests):
    return render(requests,'website\contact.html')

def elements_view(requests):
    return render(requests,'website\elements.html')

def blog_home_view(requests):
    return render(requests,'blog/blog-home.html')

def blog_single_view(requests):
    return render(requests,'blog/blog-single.html')

def http_test(requests):
    return HttpResponse("<h1>good</h1>")

def json_test(requests):
    return JsonResponse({"response" : 200})

def test(requests):
    return render(requests,"test.html")