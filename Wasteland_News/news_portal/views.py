from datetime import datetime

from django.shortcuts import render
from django.views.generic import ListView, DetailView
from .models import *


# Create your views here.
class PostsList(ListView):
    model = Post
    ordering = '-date_time'
    template_name = 'news.html'
    context_object_name = 'news'

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['time_now'] = datetime.utcnow()
        context['next_post'] = None
        context['length'] = f"Count of news : '{Post.objects.count()}'"
        return context


class PostDetail(DetailView):
    model = Post
    ordering = '-date_time'
    template_name = 'post_detail.html'
    context_object_name = 'post_detail'

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['time_now'] = datetime.utcnow()
        context['next_post'] = None
        context['length'] = f"Count of news : '{Post.objects.count()}'"
        return context
