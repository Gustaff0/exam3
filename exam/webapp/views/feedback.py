from django.views.generic import View, TemplateView, RedirectView, FormView, ListView, CreateView, DetailView, UpdateView, DeleteView
from django.shortcuts import render, get_object_or_404, redirect
from django.urls import reverse, reverse_lazy
from webapp.forms import ProductForm, SearchForm, FeedbackForm, FeedbackModerForm
from webapp.models import Product, Feedback
from django.db.models import Q
from django.utils.http import urlencode
from django.contrib.auth.mixins import PermissionRequiredMixin, LoginRequiredMixin
from django.contrib.auth.models import User
from django.contrib.auth import get_user_model

class FeedbackCreate(LoginRequiredMixin, CreateView):
    model = Feedback
    template_name = 'feedback/create.html'
    form_class = FeedbackForm

    def form_valid(self, form):
        product = get_object_or_404(Product, pk=self.kwargs.get('pk'))
        feedback = form.save(commit=False)
        feedback.product = product
        feedback.author = self.request.user
        feedback.save()
        return redirect('webapp:view', pk=product.pk)


class FeedbackEdit(UpdateView):
    model = Feedback
    template_name = 'feedback/edit.html'
    form_class = FeedbackForm
    context_object_name = 'feedback'

    def get_success_url(self):
        return reverse('webapp:view', kwargs={'pk': self.object.product.pk})



class FeedbackDelete(DeleteView):
    model = Feedback

    def get(self, request, *args, **kwargs):
        return self.delete(request, *args, **kwargs)

    def get_success_url(self):
        return reverse('webapp:view', kwargs={'pk': self.object.product.pk})



class FeedbackList(ListView):
    template_name = 'feedback/list.html'
    model = Feedback
    context_object_name = 'feedback'

    def get_queryset(self):
        filter_val = self.request.GET.get('moder_check', 'True')
        new_context = Feedback.objects.filter(
            moder_check=filter_val,
        )
        return new_context

    def get_context_data(self, **kwargs):
        context = super(FeedbackList, self).get_context_data(**kwargs)
        context['filter'] = self.request.GET.get('moder_check', 'True')
        return context


class FeedBackChekModer(PermissionRequiredMixin, UpdateView):
    model = Feedback
    template_name = 'feedback/edit_check_moder.html'
    form_class = FeedbackModerForm
    context_object_name = 'feedback'
    permission_required = 'webapp.user_add_or_del'

    def get_success_url(self):
        return reverse('webapp:list_check_moder')


class FeedbackModerList(ListView):
    template_name = 'feedback/moder_check.html'
    model = Feedback
    context_object_name = 'feedback'