from django.shortcuts import render, get_object_or_404
from django.core.paginator import Paginator, EmptyPage, PageNotAnInteger
from .models import Post, Comment
from .forms import CommentForm
from .models import User
from django.http import HttpResponseRedirect


def list(request):
    list_post = Post.objects.filter(
        active=True).order_by('-updated', '-published')
    page = request.GET.get('p', 1)
    paginator = Paginator(list_post, 8)

    try:
        post = paginator.page(page)
    except PageNotAnInteger:
        post = paginator.page(1)
    except EmptyPage:
        post = paginator.page(paginator.num_pages)

    context = {'post': post}
    template_name = 'post/list.html'
    return render(request, template_name, context)


def detail(request, slug, pk):
    post = Post.objects.get(id=pk)
    detail_post = get_object_or_404(Post, pk=pk, slug=slug, active=True)
    comment = Comment.objects.filter(
        post=post).order_by('-published')

    form = CommentForm()
    if request.method == 'POST':
        form = CommentForm(request.POST)
        if form.is_valid():
            add_comment = form.save(commit=False)
            add_comment.post = post
            add_comment.user = User.objects.get(id=request.user.id)
            add_comment.save()
            next = request.POST.get('next', '/')
            return HttpResponseRedirect(next)
    context = {'detail_post': detail_post,
               'comment': comment, 'form': form}
    template_name = 'post/detail.html'
    return render(request, template_name, context)
