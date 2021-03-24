from django.urls import path,include
from rest_framework.routers import DefaultRouter
from enroll.api import views

router=DefaultRouter()
router.register('user',views.UserViewSet,basename='user')

urlpatterns = [
    path('',include(router.urls)),
    path('auth/',include('rest_framework.urls')),
]
