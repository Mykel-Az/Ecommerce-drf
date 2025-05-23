import pytest

pytestmark = pytest.mark.django_db

class TestCategoryModel:
    def test_str_method(self, category_factory):
        # Arrange
        obj = category_factory(name="test_cat")
        # Act        
        # Assert
        assert obj.__str__() == "test_cat"

class TestBrandModel:
    def test_str_method(self, brand_factory):
        # Arrange
        obj = brand_factory(name="test_brand")
        # Act        
        # Assert
        assert obj.__str__() == "test_brand"

class TestProductModel:
    def test_str_method(self, product_factory, brand_factory, category_factory):
        # Arrange
        obj = product_factory(name="test_product")
        # Act        
        # Assert
        assert obj.__str__() == "test_product"