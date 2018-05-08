from django.conf.urls import url, include
from rest_framework import routers
from . import views
from .views import CustomObtainAuthToken

router = routers.DefaultRouter()
router.register(r'users', views.UserViewSet)
router.register(r'settlements', views.SettlementViewSet)
router.register(r'carriers', views.CarrierViewSet)

urlpatterns = [
    url(r'^', include(router.urls)),
    url(r'^authenticate/', CustomObtainAuthToken.as_view()),
]