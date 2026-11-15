from django.urls import path

from catalog.apps import CatalogConfig

from .views import ProductListView, ProductDetailView, ContactsFormView, ProductCreate, ProductUpdate, ProductDeleteView

app_name = CatalogConfig.name
urlpatterns = [
    path("", ProductListView.as_view(), name="products_list"),
    path("products/<int:pk>/", ProductDetailView.as_view(), name="product_detail"),
    path("contacts/", ContactsFormView.as_view(), name="contacts"),
    path("products/create/", ProductCreate.as_view(), name="product_create"),
    path("products/<int:pk>/update/", ProductUpdate.as_view(), name="product_update"),
    path("products/<int:pk>/delete/", ProductDeleteView.as_view(), name="product_delete"),

]
