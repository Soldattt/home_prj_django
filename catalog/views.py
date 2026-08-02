from django.http import HttpResponse
from django.shortcuts import render

from catalog.models import Product

def product_list(request):
    products = Product.objects.all()
    context = {"products": products}
    return render(request, "products_list.html", context)

def contacts(request):
    if request.method == "POST":
        name = request.POST.get("name")
        message = request.POST.get("message")
        return HttpResponse(
            f"{name}, Ваше сообщение получено, вскоре с Вами свяжется специалист."
        )
    return render(request, "contacts.html")




