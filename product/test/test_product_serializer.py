import pytest # type: ignore

from product.serializers.product_serializer import ProductSerializer

@pytest.mark.django_db
def test_product_serializer():
    
    data = {
        "title": "Teste serializer",
        "description": "Testando o serializer",
        "price": 999
    }

    serializer = ProductSerializer(data=data)

    assert serializer.is_valid(), f"Erros: {serializer.errors}"

    product = serializer.save()

    assert product.title == data["title"]
    assert product.description == data["description"]
    assert product.price == data["price"]

    serializer = ProductSerializer(product)
    serialized_data = serializer.data

    assert serialized_data["title"] == data["title"]
    assert serialized_data["description"] == data["description"]
    assert serialized_data["price"] == data["price"]
