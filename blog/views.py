from django.http import HttpResponse
from django.urls import reverse_lazy, reverse

from django.views.generic import ListView, DetailView, FormView, UpdateView, DeleteView

from django.views.generic.edit import CreateView

from blog.forms import ContactForm
from blog.models import Blog


class BlogListView(ListView):
    model = Blog
    template_name = "blogs/blog_list.html"
    context_object_name = "blogs"

    def get_queryset(self):
        return Blog.objects.filter(status=True)


class BlogDetailView(DetailView):
    model = Blog
    template_name = "blogs/blog_detail.html"
    context_object_name = "blog"

    def get_object(self, queryset=None):
        self.object = super().get_object(queryset)
        self.object.count += 1
        self.object.save()
        return self.object


class BlogCreateView(CreateView):
    model = Blog
    template_name = "blogs/blog_form.html"
    fields = ["title", "content", "image"]
    success_url = reverse_lazy('blog:blog_list')


class BlogUpdateView(UpdateView):
    model = Blog
    template_name = "blogs/blog_form.html"
    fields = ["title", "content", "image"]
    success_url = reverse_lazy('blog:blog_list')

    def get_success_url(self):
        return reverse("blog:blog_detail", args=[self.kwargs.get('pk')])


class BlogDeleteView(DeleteView):
    model = Blog
    template_name = "blogs/blog_confirm_delete.html"
    success_url = reverse_lazy('blog:blog_list')

class ContactsFormView(FormView):
    template_name = 'blogs/contacts.html'
    form_class = ContactForm
    def form_valid(self, form):
        name = form.cleaned_data['name']
        return HttpResponse(f'Спасибо, {name}! Мы с вами свяжемся в ближайшее время.')





