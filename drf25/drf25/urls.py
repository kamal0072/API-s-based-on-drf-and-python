
from django.contrib import admin
from django.urls import path,include
from api import views
from rest_framework.routers import DefaultRouter
from rest_framework.authtoken.views import obtain_auth_token


router=DefaultRouter()
router.register('studentapi',views.StudentViewSet,basename='stuent') 

urlpatterns = [
    path('admin/', admin.site.urls),
    path('',include(router.urls)),
    path('stu-auth/',include('rest_framework.urls')),
    path('obtailtoken/',obtain_auth_token),
]
