
from rest_framework.routers import SimpleRouter

from core.api.v1.views.human import HumanViewSet

router = SimpleRouter()

router.register('v1/people', HumanViewSet, basename='people')

urlpatterns = router.urls
app_name = 'core'