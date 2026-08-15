from django.http import HttpResponse

from django.views.generic import ListView, DetailView, FormView

from catalog.forms import ContactForm
from catalog.models import Product


class ProductListView(ListView):
    model = Product
    template_name = "products/products_list.html"
    context_object_name = "products"

class ProductDetailView(DetailView):
    model = Product
    template_name = "products/product_detail.html"
    context_object_name = "product"

class ContactsFormView(FormView):
    template_name = 'products/contacts.html'
    form_class = ContactForm
    def form_valid(self, form):
        name = form.cleaned_data['name']
        return HttpResponse(f'Спасибо, {name}! Мы с вами свяжемся в ближайшее время.')





