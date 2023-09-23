from django.views.generic import (
    ListView,
    DetailView,
    CreateView,
    UpdateView,
    DeleteView
)

from django.urls import reverse_lazy
from .models import Post

class PostListView(ListView):
    template_name = "posts/list.html"
    model = Post

class PostDetailView(DetailView):
    template_name = "posts/detail.html"
    model = Post

class PostCreateView(CreateView):
    template_name = "posts/new.html"
    model = Post
    fields = ["title","author", "subtitle", "body"]

class PostDeleteView(DeleteView):
    template_name = "posts/delete.html"
    model = Post
    success_url = reverse_lazy("list")

class PostUpdateView(UpdateView):
    template_name = "posts/update.html"
    model = Post
    fields = ["title","author", "subtitle", "body"]



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