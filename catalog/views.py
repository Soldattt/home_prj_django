from django.http import HttpResponse
from  django.urls import reverse_lazy

from django.views.generic import ListView, DetailView, FormView, CreateView, UpdateView, DeleteView

from catalog.forms import ContactForm, ProductForm
from catalog.models import Product


class ProductListView(ListView):
    model = Product
    template_name = "products/products_list.html"
    context_object_name = "products"


class ProductCreate(CreateView):
    model = Product
    form_class = ProductForm
    template_name = "products/product_form.html"
    success_url = reverse_lazy('catalog:products_list')


class ProductUpdate(UpdateView):
    model = Product
    form_class = ProductForm
    template_name = "products/product_form.html"
    success_url = reverse_lazy('catalog:products_list')


class ProductDetailView(DetailView):
    model = Product
    template_name = "products/product_detail.html"
    context_object_name = "product"


class ProductDeleteView(DeleteView):
    model = Product
    template_name = "products/product_confirm_delete.html"
    success_url = reverse_lazy('catalog:products_list')


class ContactsFormView(FormView):
    template_name = 'products/contacts.html'
    form_class = ContactForm
    def form_valid(self, form):
        name = form.cleaned_data['name']
        return HttpResponse(f'Спасибо, {name}! Мы с вами свяжемся в ближайшее время.')





