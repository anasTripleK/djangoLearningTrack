from django.shortcuts import render

# Create your views here.

def starting_page(request):
    return render(request, "blog/index.html")
def all_posts(requests):
    pass
def each_post_detail(request):
    pass