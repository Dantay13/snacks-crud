from django.urls import reverse_lazy
from django.views.generic import ListView, DetailView, CreateView, UpdateView, DeleteView
from .models import Snack


class SnackListView(ListView):
    template_name = 'snacks/snack_list.html'
    model = Snack


class SnackDetailView(DetailView):
    template_name = 'snacks/snack_detail.html'
    model = Snack


class SnackCreateView(CreateView):
    template_name = 'snacks/snack_form.html'
    model = Snack
    fields = ['title', 'purchaser', 'description']

    def get_success_url(self):
        return reverse_lazy('snack_list')


class SnackUpdateView(UpdateView):
    template_name = 'snacks/snack_form.html'
    model = Snack
    fields = ['title', 'purchaser', 'description']


class SnackDeleteView(DeleteView):
    template_name = 'snacks/snack_confirm_delete.html'
    model = Snack
    success_url = reverse_lazy('snack_list')