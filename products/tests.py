from datetime import datetime, timedelta

import pytest

from products.models import Category, Product


# Generic Fixtures
@pytest.fixture
def create_category() -> Category:
    return Category.objects.create(
        name="Category 1",
        description="Description 1",
    )


@pytest.fixture
def create_product(create_category: Category) -> Product:
    related_category = create_category
    product = Product.objects.create(
        name="Product 1",
        description="Description 1",
        price=100.00,
        cost=50.00,
        stock=10,
        expiration_days=30,
        last_restocked_at=datetime.strptime("2021-01-01", "%Y-%m-%d"),
    )
    product.related_categories.add(related_category)
    return product


# Models Tests
@pytest.mark.django_db
def test_product_model_str(create_product: Product):
    product = create_product
    assert str(product) == "Product 1"


@pytest.mark.django_db
def test_category_model_str(create_category: Category):
    category = create_category
    assert str(category) == "Category 1"


# Methods Tests
@pytest.mark.django_db
def test_product_model_get_gain(create_product: Product):
    product = create_product
    assert product.get_gain() == 50.00


@pytest.mark.django_db
def test_category_related_products(create_category: Category, create_product: Product):
    category = create_category
    product = create_product
    assert category.products.first() == product
    assert product.related_categories.first() == category


@pytest.mark.django_db
def test_product_model_get_expiration_date(create_product: Product):
    product = create_product
    assert product.get_expiration_date() == product.last_restocked_at + timedelta(days=30)


@pytest.mark.django_db
def test_product_model_is_in_stock(create_product: Product):
    product = create_product
    assert product.is_in_stock() is True


@pytest.mark.django_db
def test_product_model_is_in_stock_false(create_product: Product):
    product = create_product
    product.stock = 0
    assert product.is_in_stock() is False


@pytest.mark.django_db
def test_product_model_is_expired(create_product: Product):
    product = create_product
    assert product.is_expired() is True


@pytest.mark.django_db
def test_product_count_by_category(create_category: Category, create_product: Product):
    """Check if the product_count method can count 2 products in the same category."""
    category = create_category
    product = create_product
    product2 = Product.objects.create(
        name="Product 2",
        description="Description 2",
        price=100.00,
        cost=50.00,
        stock=10,
        expiration_days=30,
        last_restocked_at=datetime.strptime("2021-01-01", "%Y-%m-%d"),
    )
    product2.related_categories.add(category)
    assert category.product_count() == 2


@pytest.mark.django_db
def test_category_average_price(create_category: Category, create_product: Product):
    """Check if the average_price method can calculate the average price of 2 products in the
    same category."""
    category = create_category
    product = create_product
    product2 = Product.objects.create(
        name="Product 2",
        description="Description 2",
        price=100.00,
        cost=50.00,
        stock=10,
        expiration_days=30,
        last_restocked_at=datetime.strptime("2021-01-01", "%Y-%m-%d"),
    )
    product2.related_categories.add(category)
    assert category.average_product_price() == 100.00
