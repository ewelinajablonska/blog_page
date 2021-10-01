from django.shortcuts import render

from blog_app.models import BlogPost

# Create your views here.
def index(request):
    """The home page for blog application."""
    posts = BlogPost.objects.order_by('date_added')
    context = { 'posts' : posts}
    return render(request, 'blog_app/index.html', context)