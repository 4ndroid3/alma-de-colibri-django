from rest_framework.routers import DefaultRouter

from api.products.views import CategoryView, ProductView

app_name = "products-api"
router = DefaultRouter()

router.register("list", ProductView)
router.register("categories", CategoryView)

urlpatterns = router.urls
