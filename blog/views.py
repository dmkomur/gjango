from django.views.generic import (
    ListView,
    DetailView,
    CreateView,
    UpdateView,
    DeleteView,
)
from django.urls import reverse_lazy
from .models import Post
from .forms import PostForm


class PostListView(ListView):
    model = Post
    ordering = ["-published"]  # эквивалент .order_by("-published")
    template_name = "blog/index.html"  # иначе искал бы blog/post_list.html
    context_object_name = "posts"  # по умолчанию object_list


class PostDetailView(DetailView):
    model = Post
    template_name = "blog/detail.html"  # иначе blog/post_detail.html
    context_object_name = "post"


class PostCreateView(CreateView):
    model = Post
    form_class = PostForm
    success_url = reverse_lazy("blog:index")


class PostUpdateView(UpdateView):
    model = Post
    form_class = PostForm
    success_url = reverse_lazy("blog:index")


class PostDeleteView(DeleteView):
    model = Post
    template_name = "blog/post_confirm_delete.html"
    success_url = reverse_lazy("blog:index")
