from django.http import HttpResponse
from django.shortcuts import render


def home(request):
    return render(request, "home.html")


def contacts(request):
    if request.method == "POST":
        name = request.POST.get("name")
        message = request.POST.get("message")
        return HttpResponse(
            f"{name}, Ваше сообщение получено, вскоре с Вами свяжется специалист."
        )
    return render(request, "contacts.html")
