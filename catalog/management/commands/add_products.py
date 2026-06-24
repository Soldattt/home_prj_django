from django.core.management.base import BaseCommand
from catalog.models import Category, Product


class Command(BaseCommand):
    help = 'Add test products'

    def handle(self, *args, **kwargs):
        Category.objects.all().delete()

        category, _ = Category.objects.get_or_create(name='Фрукты и овощи', description='Свежие фрукты и овощи')

        products = [
            {'name': 'Помидоры', 'price': '230.0', 'category': category},
            {'name': 'Бананы', 'price': '310.0', 'category': category},
        ]

        for product_obj in products:
            product, created = Product.objects.get_or_create(**product_obj)
            if created:
                self.stdout.write(self.style.SUCCESS(f'Продукт: {product.name} добавлен, цена {product.price}'))
            else:
                self.stdout.write(self.style.WARNING(f'Продукт: {product.name} по цене {product.price} уже существует'))