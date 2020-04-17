from django.shortcuts import render
from django.http import JsonResponse
from blog_test.models import *
from blog_test.forms import CommentForm
from django.http import Http404
import random


def get_blogs(request):
    blogs = Blog.objects.all().order_by('-created')
    return render(request, 'blog-list.html', {'blogs': blogs})


def get_details(request, blog_id):
    try:
        blog = Blog.objects.get(id=blog_id)
    except Blog.DoesNotExist:
        raise Http404
    if request.method == 'GET':
        form = CommentForm()
    else:
        form = CommentForm(request.POST)
        if form.is_valid():
            cleaned_data = form.cleaned_data
            cleaned_data['blog'] = blog
            Comment.objects.create(**cleaned_data)
    ctx = {
        'blog': blog,
        'comments': blog.comment_set.all().order_by('-created'),
        'form': form
    }
    return render(request, 'blog_details.html', ctx)


def chat(request):

    return render(request, 'chat.html')


def ask_deal(request):
    show_word = '最' * random.randint(0, 6)
    return JsonResponse({'data': '你{}帅'.format(show_word)})
