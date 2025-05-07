import factory

from main.models import *

class CategoryFactory(factory.django.DjangoModelFactory):
    class Meta:
        model = Category

    name = factory.Sequence(lambda n: f'Category_{n}')

class BrandFactory(factory.django.DjangoModelFactory):
    class Meta:
        model = Brand

    name = factory.Sequence(lambda n: f'brand_{n}')


class ProductFactory(factory.django.DjangoModelFactory):
    class Meta:
        model = Product

    # name = 'test_product'
    # description = 'test_description'
    # is_digital = True
    price = 100.00
    brand = factory.SubFactory(BrandFactory)
    category = factory.SubFactory(CategoryFactory)