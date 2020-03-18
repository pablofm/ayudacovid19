from colaboradores import views
from rest_framework import routers


router = routers.SimpleRouter()
router.register('colaboradores', views.ColaboradoresAPIView)


urlpatterns = router.urls
