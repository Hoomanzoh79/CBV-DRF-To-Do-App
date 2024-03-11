from .views import TaskViewSet
from rest_framework.routers import DefaultRouter

app_name = "api-v1"

router = DefaultRouter()
router.register("task", TaskViewSet, basename="task")

urlpatterns = router.urls
