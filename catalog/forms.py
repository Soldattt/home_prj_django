from django import forms

from django.core.validators import MinValueValidator


from catalog.models import Product

import re
from django import forms
from django.core.exceptions import ValidationError
from .models import Product

FORBIDDEN_WORDS = [
    'казино', 'криптовалюта', 'крипта', 'биржа', 'дешево', 'бесплатно', 'обман', 'полиция', 'радар'
]


class ProductForm(forms.ModelForm):
    class Meta:
        model = Product
        fields = ['name', 'description', 'price', 'image']
        widgets = {
            'image': forms.ClearableFileInput(attrs={'class': 'form-control-file'}),
        }

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)

        # Стилизация лейблов и полей
        for field_name, field in self.fields.items():
            # Добавляем базовые классы Bootstrap ко всем виджетам
            if 'class' in field.widget.attrs:
                field.widget.attrs['class'] += ' form-control'
            else:
                field.widget.attrs['class'] = 'form-control'

            # Специфичные настройки для разных типов полей
            if isinstance(field.widget, forms.Textarea):
                field.widget.attrs.update({'rows': 4})
            elif isinstance(field.widget, forms.NumberInput):
                field.widget.attrs.update({'step': '0.01'})
            elif isinstance(field.widget, forms.ClearableFileInput):
                # Для файловых инпутов класс может отличаться в зависимости от версии Bootstrap
                field.widget.attrs['class'] = 'form-control-file'

            # Добавляем плейсхолдеры для лучшего UX
            placeholders = {
                'name': 'Например: Беспроводные наушники',
                'description': 'Краткое описание характеристик и преимуществ',
                'price': '0.00'
            }
            if field_name in placeholders:
                field.widget.attrs['placeholder'] = placeholders[field_name]

    def clean_price(self):
        price = self.cleaned_data.get('price')
        if price is not None and price < 0:
            raise ValidationError('Цена не может быть отрицательной.')
        return price



    def clean(self):
        cleaned_data = super().clean()
        name = cleaned_data.get('name', '')
        description = cleaned_data.get('description', '')

        # Объединяем текст для проверки
        text_to_check = f"{name} {description}".lower()

        found_words = []
        for word in FORBIDDEN_WORDS:
            pattern = r'\b' + re.escape(word) + r'\b'
            if re.search(pattern, text_to_check):
                found_words.append(word)

        if found_words:
            raise ValidationError(
                f'Поля содержат запрещенные слова: {", ".join(found_words)}. Пожалуйста, измените название или описание.'
            )
        return cleaned_data

class ContactForm(forms.Form):
    name = forms.CharField(max_length=100)
    phone = forms.CharField(max_length=15)
    message = forms.CharField(widget=forms.Textarea)



