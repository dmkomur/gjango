from django.views.generic import ListView, DetailView
from .models import Post


class PostListView(ListView):
    model = Post
    ordering = ["-published"]  # эквивалент .order_by("-published")
    template_name = "blog/index.html"  # иначе искал бы blog/post_list.html
    context_object_name = "posts"  # по умолчанию object_list


class PostDetailView(DetailView):
    model = Post
    template_name = "blog/detail.html"  # иначе blog/post_detail.html
    context_object_name = "post"
