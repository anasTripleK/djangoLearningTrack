from django.shortcuts import render

# Create your views here.

def starting_page(request):
    return render(request, "blog/index.html")
def all_posts(request):
    return render(request, "blog/all-posts.html")
def each_post_detail(request, slug):
    return render(request, "blog/post-detail.html")