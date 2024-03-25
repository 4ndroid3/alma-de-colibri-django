from rest_framework.routers import DefaultRouter

from api.core.views import CityView, UserView

app_name = "core-api"
router = DefaultRouter()

router.register("cities", CityView)
router.register("users", UserView)

urlpatterns = router.urls
