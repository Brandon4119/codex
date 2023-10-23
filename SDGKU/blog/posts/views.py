from typing import Any
from django.forms.models import BaseModelForm
from django.http import HttpResponse
from django.views.generic import (
    ListView,
    DetailView,
    CreateView,
    UpdateView,
    DeleteView
)

from django.urls import reverse_lazy
from .models import Post, Status
from django.contrib.auth.mixins import (
    LoginRequiredMixin,
    UserPassesTestMixin)

from django.core.exceptions import PermissionDenied

class PostListView(ListView):
    template_name = "posts/list.html"
    model = Post

class PostDetailView(DetailView):
    template_name = "posts/detail.html"
    model = Post

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        draft = Status.objects.get(name="draft")
        if (context["post"].status == draft
            and context["post"].author != self.request.user):
            context["post"] = None
        if context("post"):
            return context
        raise PermissionDenied()

class PostCreateView(LoginRequiredMixin, CreateView):
    template_name = "posts/new.html"
    model = Post
    fields = ["title", "subtitle", "body", "status"]

    def form_valid(self, form):
        form.instance.author = self.request.user
        return super().form_valid(form)

class PostDeleteView(DeleteView):
    template_name = "posts/delete.html"
    model = Post
    success_url = reverse_lazy("list")

    def test_func(self):
        # This must be true or false
        post = self.get_object()
        post = self.request.user == post.author

class PostUpdateView(
        LoginRequiredMixin,
        UserPassesTestMixin, 
        UpdateView):
    template_name = "posts/update.html"
    model = Post
    fields = ["title", "subtitle", "body", "status"]

    def test_func(self):
        post = self.get_object()
        return self.request.user == post.author


class PostListView(ListView):
    template_name = "posts/list.html"
    model = Post

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        published = Status.objects.get(name="published")
        context["post_list"] = Post.objects.filter(
            status=published
        ).order_by("created_on").reverse()
        return context

class DraftPostListView(LoginRequiredMixin, ListView):
    template_name = "posts/list.html"
    model = Post

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        draft = Status.objects.get(name="draft")
        context["post_list"] = Post.objects.filter(
            status=draft
        ).filter(
            author=self.request.user
        ).order_by("created_on").reverse()
        return context
    
class ArchivedPostListView(LoginRequiredMixin, ListView):
    template_name = "post/list.html"
    model = Post

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        archived = Status.objects.get(name="archived")
        context["post_list"] = Post.objects.filter(
            status=archived
        ).filter(
            author=self.request.user
        ).order_by("created_on").reverse()
        return context


# Create archived page or feature
# Should filter by "archived" status
# Only logged in users can see the archive


# The update view class requires, at a minimum:
# 1. template_name
# 2. model
# 3. A list of fields that should be present on the generated form

# the update view will require a very specific url pattern which should
# include the primarykey of instante of our model that we wish to modify.

# The delete view will also require a primary key to be provided throught a url pattern.

# The delete view will need, at a minimum:
# 1. template_name
# 2. model
# 3. success_url (this should redirect our users after a successful delete)