from django.contrib.auth.mixins import LoginRequiredMixin
from django.views.generic import ListView, DetailView, UpdateView, CreateView, DeleteView
from django.urls import reverse_lazy
from .models import cookie_stand


class cookie_standListView(LoginRequiredMixin, ListView):
    template_name = "cookie_stands/cookie_stand_list.html"
    model = cookie_stand
    context_object_name = "cookie_stands"


class cookie_standDetailView(LoginRequiredMixin, DetailView):
    template_name = "cookie_stands/cookie_stand_detail.html"
    model = cookie_stand


class cookie_standUpdateView(LoginRequiredMixin, UpdateView):
    template_name = "cookie_stands/cookie_stand_update.html"
    model = cookie_stand
    fields = "__all__"


class cookie_standCreateView(LoginRequiredMixin, CreateView):
    template_name = "cookie_stands/cookie_stand_create.html"
    model = cookie_stand
    fields = ["name", "rating", "reviewer"] # "__all__" for all of them


class cookie_standDeleteView(LoginRequiredMixin, DeleteView):
    template_name = "cookie_stands/cookie_stand_delete.html"
    model = cookie_stand
    success_url = reverse_lazy("cookie_stand_list")
