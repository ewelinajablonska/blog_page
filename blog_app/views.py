from django.shortcuts import get_object_or_404, render, redirect
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
            post = form.save(commit=False)
            form.save()
            return redirect('blog_app:index', pk=post.pk)
    
    context = {'form' : form}
    return render(request, 'blog_app/new_post.html', context)

def edit_post(request, pk):
    """Form for edit post."""
    post= get_object_or_404(BlogPost, pk=pk)
    if request.method != 'POST':
        form = PostForm(instance=post)
    else:
        form = PostForm(data = request.POST, instance=post)
        if form.is_valid():
            post = form.save(commit=False)
            form.save()
            return redirect('blog_app:index')
    
    context = {'form' : form}
    return render(request, 'blog_app/new_post.html', context)