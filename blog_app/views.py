from django.shortcuts import render, redirect
from .models import BlogPost
from .forms import PostForm

# Create your views here.
def index(request):
    """The home page for blog application."""
    posts = BlogPost.objects.order_by('date_added')
    context = { 'posts' : posts}
    return render(request, 'blog_app/index.html', context)

def new_post(request):
    """Form for add new post."""
    if request.method != 'POST':
        form = PostForm()
    else:
        form = PostForm(data = request.POST)
        if form.is_valid():
            form.save()
            return redirect('blog_app:index')
    
    context = {'form' : form}
    return render(request, 'blog_app/new_post.html', context)