import pytest # type: ignore

from product.models import Product

@pytest.mark.django_db
def test_create_product():
    product = Product.objects.create(
        title="Carrinho",
        description="Carrinho vermelho",
        price=123
    )

    assert product.title == "Carrinho"
    assert product.description == "Carrinho vermelho"
    assert product.price == 123
