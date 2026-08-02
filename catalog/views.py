from django.http import HttpResponse
from django.shortcuts import render, get_object_or_404

from catalog.models import Product

def product_list(request):
    products = Product.objects.all()
    context = {"products": products}
    return render(request, "products_list.html", context)

def product_detail(request, id):
    product = get_object_or_404(Product, id=id)
    context = {"product": product}
    return render(request, "product_detail.html", context)

def contacts(request):
    if request.method == "POST":
        name = request.POST.get("name")
        message = request.POST.get("message")
        return HttpResponse(
            f"{name}, Ваше сообщение получено, вскоре с Вами свяжется специалист."
        )
    return render(request, "contacts.html")





