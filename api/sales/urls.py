from rest_framework.routers import DefaultRouter

from api.sales.views import CartView, SaleView

app_name = "sales-api"
router = DefaultRouter()

router.register("products", SaleView)
router.register("categories", CartView)

urlpatterns = router.urls
