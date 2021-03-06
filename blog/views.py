import csv

from django.shortcuts import render, get_object_or_404
from django.core import serializers
from django.contrib.auth.mixins import LoginRequiredMixin, UserPassesTestMixin
from django.contrib.auth.decorators import login_required
from django.contrib.auth.models import User
from django.views.generic import (
    ListView,
    DetailView,
    CreateView,
    UpdateView,
    DeleteView,
    View
)
from django.http import HttpResponse
from .models import Post


def home(request):
    context = {
        'posts': Post.objects.all()
    }
    return render(request, 'blog/home.html', context)


class PostListView(ListView):
    model = Post
    template_name = 'blog/home.html'  # <app>/<model>_<viewtype>.html
    context_object_name = 'posts'
    ordering = ['-date_posted']  # newest to oldest
    paginate_by = 8


class UserPostListView(ListView):  # displaying all posts of a user
    model = Post
    template_name = 'blog/user_posts.html'  # <app>/<model>_<viewtype>.html
    context_object_name = 'posts'
    ordering = ['-date_posted']  # newest to oldest
    paginate_by = 8

    def get_queryset(self):
        user = get_object_or_404(User, username=self.kwargs.get('username'))
        return Post.objects.filter(author=user).order_by('-date_posted')


class PostDetailView(DetailView):
    model = Post


def userProfileView(request, username):
    user = get_object_or_404(User, username=username)
    return render(request, 'blog/user_profile.html', {'user_data': user})


class PostCreateView(LoginRequiredMixin, CreateView):
    model = Post
    fields = ['title', 'content']

    def form_valid(self, form):
        form.instance.author = self.request.user
        return super().form_valid(form)


class PostUpdateView(LoginRequiredMixin, UserPassesTestMixin, UpdateView):
    model = Post
    fields = ['title', 'content']

    def form_valid(self, form):
        form.instance.author = self.request.user
        return super().form_valid(form)

    def test_func(self):  # check if user is OP before editing post
        post = self.get_object()
        if self.request.user == post.author:
            return True
        return False


class PostDeleteView(LoginRequiredMixin, UserPassesTestMixin, DeleteView):
    model = Post
    success_url = '/'

    def test_func(self):  # check if user is OP before editing post
        post = self.get_object()
        if self.request.user == post.author:
            return True
        return False


def about(request):
    return render(request, 'blog/about.html', {'title': 'About'})


def export(request):
    return render(request, 'blog/export.html', {'title': 'Export'})


def export_csv(request):
    response = HttpResponse(content_type='text/csv')

    writer = csv.writer(response)
    writer.writerow(['Title', 'Content', 'Date Posted', 'Author'])

    for post in Post.objects.all().values_list('title', 'content', 'date_posted', 'author'):
        writer.writerow(post)

    response['Content-Disposition'] = 'attachment; filename="posts.csv"'

    return response


def export_json(request):
    data = Post.objects.filter(date_posted__isnull=False).order_by('-date_posted')
    post_list = serializers.serialize('json', data)
    return HttpResponse(post_list, content_type="text/json-comment-filtered")
