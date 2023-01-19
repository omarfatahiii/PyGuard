from django.shortcuts import render
from .models import Referenc
import datetime
from django.utils import timezone
from post.models import Post
from course.models import Course


def home(request):
    post = Post.objects.filter(active=True).order_by('-published')[:3]
    course = Course.objects.filter(active=True).order_by('-published')[:3]
    referenc = Referenc.objects.all()[:10]
    user = request.user
    if user.is_authenticated:
        if user.special < timezone.now():
            user.special = datetime.datetime.now()
            user.is_special = False
            user.save()
    context = {'post': post, 'course': course, 'referenc': referenc}
    template_name = 'base/home.html'
    return render(request, template_name, context)


def referenc(request):
    references = Referenc.objects.all()
    context = {'references': references}
    template_name = 'base/referenc.html'
    return render(request, template_name, context)
