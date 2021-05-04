from rest_framework.routers import DefaultRouter
from .views import PizzaViewset
router = DefaultRouter()
router.register(r'pizza', PizzaViewset)