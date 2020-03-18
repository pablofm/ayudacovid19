from peticiones import views
from rest_framework import routers


router = routers.SimpleRouter()
router.register('peticiones', views.PeticionesAPIView)


urlpatterns = router.urls
