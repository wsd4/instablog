from django.shortcuts import render
from django.shortcuts import redirect
from django.shortcuts import get_object_or_404
from django.core.urlresolvers import reverse

from .models import Post
from .models import Category
from .models import Tag
from .models import Comment


def list_posts(request):

    try:
        page = int(request.GET['page'])
        if page < 1:
            page = 1
    except Exception:
        page = 1

    per_page = 5

    #posts = Post.objects.order_by('-created_at')[page-1:page*per_page]
    posts = Post.objects.order_by('-created_at')

    return render(request, 'list.html', {
        'posts': posts,
    })


def view_post(request, pk):
    post = get_object_or_404(Post, pk=pk)

    return render(request, 'view.html',{
        'post': post,
    })


def create_post(request):

    if request.method == 'GET':
        categories = Category.objects.all()
        context = {
            'categories': categories,
        }
    elif request.method == 'POST':

        form = request.POST
        category = get_object_or_404(Category, pk=form['category'])
        post = Post(
            title=form['title'],
            content=form['content'],
            category=category,
        )
        post.full_clean()
        post.save()
        url = reverse('blog:view_post', kwargs={'pk': post.pk})

        return redirect(url)

    return render(request, 'edit.html', context)


def edit_post(request, pk):

    if request.method == 'GET':
        post = get_object_or_404(Post, pk=pk)
        categories = Category.objects.all()
    elif request.method == 'POST':

        # 교제처럼 바로 넘기면 수정이 아니라 새로 생기는 버그가 있음
        # return create_post(request)

        form = request.POST
        post = get_object_or_404(Post, pk=pk)
        post.title = form['title']
        post.content = form['content']
        post.category = get_object_or_404(Category, pk=form['category'])
        post.full_clean()
        post.save()
        url = reverse('blog:view_post', kwargs={'pk': post.pk})

        return redirect(url)


    return render(request, 'edit.html', {
        'post': post,
        'categories': categories,
    })


def delete_post(request, pk):

    post = get_object_or_404(Post, pk=pk)

    if request.method == 'POST':
        post.delete()

        return redirect('blog:list_posts')

    elif request.method == 'GET':

        return render(request, 'delete.html', {
            'post': post
        })

