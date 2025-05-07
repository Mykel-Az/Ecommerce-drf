import json
import pytest
import factory

pytestmark = pytest.mark.django_db

class TestCategoryEndpoint:
    
    endpoint = '/api/categories/'

    def test_category_get(self, category_factory, api_client):
        # Arrange
        category = category_factory.create_batch(4)
        # Act
        response = api_client().get(self.endpoint)
        # Assert
        assert response.status_code == 200
        print(json.loads(response.content))
        assert len(json.loads(response.content)) == 4


class TestBrandEndpoint:
    
    endpoint = '/api/brands/'

    def test_brand_get(self, brand_factory, api_client):
        # Arrange
        brand = brand_factory.create_batch(4)
        # Act
        response = api_client().get(self.endpoint)
        # Assert
        assert response.status_code == 200
        print(json.loads(response.content))
        assert len(json.loads(response.content)) == 4