from django.urls import path

from catalog.apps import CatalogConfig

from . import views

app_name = CatalogConfig.name
urlpatterns = [
    path("", views.product_list, name="products_list"),
    path("catalog/<int:id>/", views.product_detail, name="product_detail"),
    path("contacts/", views.contacts, name="contacts"),

]
