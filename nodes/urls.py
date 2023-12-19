from nodes.apps import NodesConfig
from rest_framework.routers import DefaultRouter

from nodes.views import NetworkNodeViewSet, ContactViewSet, ProductViewSet

app_name = NodesConfig.name


router = DefaultRouter()
router.register(r'nodes', NetworkNodeViewSet, basename='nodes')
router.register(r'contacts', ContactViewSet, basename='contacts')
router.register(r'products', ProductViewSet, basename='products')

urlpatterns = router.urls
