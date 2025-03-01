from django.shortcuts import render, redirect, get_object_or_404
from django.contrib.auth.decorators import login_required
from .models import Blog


# READ: Show all blogs
def blog_list(request):
    blogs = Blog.objects.all().order_by('-created_at')  # Newest first
    return render(request, 'blogs/blog_list.html', {'blogs': blogs})


# CREATE: Post a new blog
@login_required  # Only logged-in users
def blog_create(request):
    if request.method == 'POST':
        title = request.POST['title']
        content = request.POST['content']
        Blog.objects.create(title=title, content=content, author=request.user)
        return redirect('blog_list')
    return render(request, 'blogs/blog_form.html')


# UPDATE: Edit your own blog
@login_required
def blog_edit(request, id):
    blog = get_object_or_404(Blog, id=id)
    if blog.author != request.user:  # Check ownership
        return redirect('blog_list')  # Redirect if not your blog
    if request.method == 'POST':
        blog.title = request.POST['title']
        blog.content = request.POST['content']
        blog.save()
        return redirect('blog_list')
    return render(request, 'blogs/blog_form.html', {'blog': blog})


# DELETE: Delete your own blog
@login_required
def blog_delete(request, id):
    blog = get_object_or_404(Blog, id=id)
    if blog.author != request.user:  # Check ownership
        return redirect('blog_list')
    if request.method == 'POST':
        blog.delete()
        return redirect('blog_list')
    return render(request, 'blogs/blog_confirm_delete.html', {'blog': blog})
