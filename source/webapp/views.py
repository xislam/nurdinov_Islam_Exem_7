from django.urls import reverse
from django.views.generic import ListView, CreateView, UpdateView, DeleteView, DetailView
from webapp.models import Poll
from webapp.forms import *


class IndexView(ListView):
    template_name = 'poll/index.html'
    context_object_name = 'poll'
    model = Poll
    context_key = 'polls'

    def get_objects(self):
        return super().get_objects().order_by('-created_at')

    ordering = ['-created_at']
    paginate_by = 5
    paginate_orphans = 1


class PollView(ListView):
    template_name = 'poll/poll_view.html'
    context_object_name = 'polls'
    model = Poll


class PollDetailView(DetailView):
    template_name = 'poll/polls.html'
    context_object_name = 'poll'
    model = Poll


class PollCreateView(CreateView):
    template_name = 'poll/create_poll.html'

    model = Poll

    form_class = PollForm

    def get_success_url(self):
        return reverse('poll_view', kwargs={'pk': self.object.pk})


class PollUpdateView(UpdateView):
    model = Poll
    template_name = 'poll/update_poll.html'
    form_class = PollForm
    context_object_name = 'poll'

    def get_success_url(self):
        return reverse('poll_view', kwargs={'pk': self.object.pk})


class PollDeleteView(DeleteView):
    model = Poll
    template_name = 'poll/delete.html'
    form_class = PollForm
    context_object_name = 'poll'
    page = 'error.html'

    def get_success_url(self):
        return reverse('poll_view', kwargs={'pk': self.object.pk})


class ChoiceDetailView(DetailView):
    template_name = 'choice/choices.html'
    context_object_name = 'choice'
    model = Choice


class ChoiceCreateView(CreateView):
    template_name = 'choice/create.html'

    model = Choice

    form_class = ChoiceForm

    def get_success_url(self):
        return reverse('view_choice')


class ChoiceUpdateView(UpdateView):
    model = Choice
    template_name = 'choice/update.html'
    form_class = ChoiceForm
    context_object_name = 'choice'

    def get_success_url(self):
        return reverse('view_choice')


class ChoiceDeleteView(DeleteView):
    model = Choice
    template_name = 'choice/delete.html'
    form_class = ChoiceForm
    context_object_name = 'choice'
    page = 'error.html'

    def get_success_url(self):
        return reverse('view_choice')
