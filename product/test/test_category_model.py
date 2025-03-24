import pytest # type: ignore

from product.models import Category

@pytest.mark.django_db
def test_create_category():
    category = Category.objects.create(
        title="Titulo teste da categoria",
        slug="Slug test",
        description="Desc Test"
    )

    assert category.title == "Titulo teste da categoria"
    assert category.slug == "Slug test"
    assert category.description == "Desc Test"
