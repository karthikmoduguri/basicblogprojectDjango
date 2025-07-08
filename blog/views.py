from django.shortcuts import render,redirect

from blog.models import Post
from blog.forms import PostForm

# Create your views here.
def blog(request):
    blog_p=Post.objects.all()
    return render(request, 'blog.html',{'blog_p': blog_p})


def create_post(request):
    if request.method == 'POST':
        form = PostForm(request.POST)
        if form.is_valid():
            form.save()  # 🎯 Saves to DB
            return redirect('post_list')  # Redirect after success
    else:
        form = PostForm()

    return render(request, 'create_post.html', {'form': form})

def post_list(request):
    posts = Post.objects.all().order_by('-created_date')
    return render(request, 'post_list.html', {'posts': posts})

