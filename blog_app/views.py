from django.shortcuts import render

# Create your views here.
def index(request):
    """The home page for blog application."""
    return render(request, 'blog_app/index.html')