from rest_framework.routers import DefaultRouter

from api.products.views import CategoryView, DiscountView, ProductView

app_name = "products-api"
router = DefaultRouter()

router.register("products", ProductView)
router.register("categories", CategoryView)
router.register("discounts", DiscountView)

urlpatterns = router.urls
