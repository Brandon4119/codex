
from django.views.generic import (
    CreateView,
    DetailView,
    UpdateView,
    DeleteView,
    ListView
)
from django.urls import reverse_lazy
from .models import Issue

class IssueCreateView(CreateView):
    template_name = "issues/new.html"
    model = Issue
    fields = ["summary", "description", "assignee", "status"]

    def form_valid(self, form):
        form.instance.reporter = self.request.user
        return super().form_valid(form)

class IssueDetailView(DetailView):
    template_name = "issues/detail.html"
    model = Issue 

    class IssueUpdateView(UpdateView):
        template_name = "issues/edit.html"
        model = Issue
        fields = ["summary", "description", "assignee", "status"]

class IssueDeleteView(DeleteView):
        template_name = "issues/delete.html"
        model = Issue
        success_url = reverse_lazy("list")

class IssueListView(ListView):
        template_name = "issues/list.html"
        model = Issue