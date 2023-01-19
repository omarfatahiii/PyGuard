from django.shortcuts import render, get_object_or_404
from django.core.paginator import PageNotAnInteger, Paginator, EmptyPage
from .models import Course, Property, Comment
from .forms import CommentForm
from .models import User
import datetime
from django.utils import timezone
from django.http import HttpResponseRedirect


def list(request):
    list_course = Course.objects.all().filter(active=True).order_by(
        '-updated', '-completed', '-published')
    page = request.GET.get('p', 1)
    paginator = Paginator(list_course, 8)

    try:
        course = paginator.page(page)
    except PageNotAnInteger:
        course = paginator.page(1)
    except EmptyPage:
        course = paginator.page(paginator.num_pages)

    context = {'course': course}
    return render(request, 'course/list.html', context)


def detail(request, pk, slug):
    course = Course.objects.get(id=pk)
    detail_course = get_object_or_404(Course, pk=pk, slug=slug, active=True)
    property = Property.objects.filter(pk=pk)
    comment = Comment.objects.filter(
        course=course).order_by('-published')
    user = request.user
    if user.is_authenticated:
        if user.special < timezone.now():
            user.special = datetime.datetime.now()
            user.is_special = False
            user.save()
    form = CommentForm()
    if request.method == 'POST':
        form = CommentForm(request.POST)
        if form.is_valid():
            add_comment = form.save(commit=False)
            add_comment.course = course
            add_comment.user = User.objects.get(id=request.user.id)
            add_comment.save()
            next = request.POST.get('next', '/')
            return HttpResponseRedirect(next)
    context = {'detail_course': detail_course, 'property_course': property,
               'comment': comment, 'form': form}
    return render(request, 'course/detail.html', context)
