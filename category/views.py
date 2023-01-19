from django.shortcuts import render, get_object_or_404
from .models import Parent, Child


def list_parent(request):
    list = Parent.objects.all()
    context = {'list_parent': list}
    return render(request, 'category/list_parent.html', context)


def list_child(request, slug):
    list = get_object_or_404(Child, slug=slug)
    context = {'list_child': list}
    return render(request, 'category/list_child.html', context)
