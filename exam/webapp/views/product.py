from django.views.generic import View, TemplateView, RedirectView, FormView, ListView, CreateView, DetailView, UpdateView, DeleteView
from django.shortcuts import render, get_object_or_404, redirect
from django.urls import reverse, reverse_lazy
from webapp.forms import ProductForm, SearchForm
from webapp.models import Product, Feedback
from django.db.models import Q
from django.utils.http import urlencode
from django.contrib.auth.mixins import PermissionRequiredMixin, LoginRequiredMixin
from django.contrib.auth.models import User
from django.contrib.auth import get_user_model

class ProductCreate(PermissionRequiredMixin, CreateView):
    template_name = 'product/create.html'
    form_class = ProductForm
    model = Product
    permission_required = 'webapp.add_product'

    def get_success_url(self):
        return reverse('webapp:home')



class ProductList(ListView):
    template_name = 'product/list.html'
    model = Product
    context_object_name = 'products'
    ordering = ('name',)
    paginate_by = 10
    paginate_orphans = 2

    def get(self, request, **kwargs):
        self.form = SearchForm(request.GET)
        self.search_data = self.get_search_data()
        return super(ProductList, self).get(request, **kwargs)

    def get_queryset(self):
        queryset = super().get_queryset()

        if self.search_data:
            queryset = queryset.filter(
                Q(name__icontains=self.search_data) |
                Q(description__icontains=self.search_data)
            )
        return queryset

    def get_search_data(self):
        if self.form.is_valid():
            return self.form.cleaned_data['search_value']
        return None

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['search_form'] = self.form

        if self.search_data:
            context['query'] = urlencode({'search_value': self.search_data})

        return context



class ProductEdit(PermissionRequiredMixin, UpdateView):
    model = Product
    template_name = 'product/edit.html'
    form_class = ProductForm
    context_object_name = 'product'
    permission_required = 'webapp.change_product'

    def get_success_url(self):
        return reverse('webapp:view', kwargs={'pk': self.object.pk})


class ProductView(DetailView):
    model = Product
    template_name = 'product/view.html'

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['feedbacks'] = self.get_object().product.filter(moder_check=True)
        return context

    # def dispatch(self, request, *args, **kwargs):
    #     if not request.user.is_authenticated:
    #         return redirect('accounts:login')
    #     return super().dispatch(request, *args, **kwargs)


class ProductDelete(PermissionRequiredMixin, DeleteView):
    template_name = 'product/delete.html'
    model = Product
    context_object_name = 'product'
    success_url = reverse_lazy('webapp:home')
    permission_required = 'webapp.delete_product'

