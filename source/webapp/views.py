from django.contrib.auth.mixins import LoginRequiredMixin
from django.urls import reverse, reverse_lazy
from django.views.generic import ListView, CreateView, DetailView, UpdateView, DeleteView

from webapp.forms import ProductForm, ReviewForm
from webapp.models import Product, Review


class IndexView(ListView):
    template_name = 'index.html'
    context_object_name = 'products'
    model = Product
    paginate_by = 4
    paginate_orphans = 1


class ProductCreateView(CreateView):
    template_name = 'product/create.html'
    model = Product
    form_class = ProductForm

    def get_success_url(self):
        return reverse('webapp:index')


class ProductView(DetailView):
    model = Product
    template_name = 'product/detail.html'


class ProductUpdateView(LoginRequiredMixin, UpdateView):
    model = Product
    template_name = 'product/update.html'
    fields = ('name', 'category', 'description', 'photo')
    context_object_name = 'product'

    def get_success_url(self):
        return reverse('webapp:product_detail', kwargs={'pk': self.object.pk})


class ProductDeleteView(LoginRequiredMixin, DeleteView):
    model = Product
    template_name = 'product/delete.html'
    success_url = reverse_lazy('webapp:index')
    context_object_name = 'product'


class ReviewCreateView(CreateView):
    template_name = 'product/create.html'
    model = Review
    form_class = ReviewForm

    def get_success_url(self):
        return reverse('webapp:index.html')