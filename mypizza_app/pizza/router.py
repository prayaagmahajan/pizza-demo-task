from rest_framework.routers import DefaultRouter
from .views import PizzaViewset,PizzaSizeViewset,PizzaToppingsViewset
router = DefaultRouter()
router.register(r'pizza', PizzaViewset)
router.register(r'pizzasize', PizzaSizeViewset)
router.register(r'pizzatopping', PizzaToppingsViewset)
