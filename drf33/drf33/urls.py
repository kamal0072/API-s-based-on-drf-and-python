"""drf33 URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/3.1/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import path,include
from api import views
from rest_framework.routers import DefaultRouter

router=DefaultRouter()
router.register('stucrup',views.StudentRetreiveUpdateDestroyApi,basename='stucrup')

urlpatterns = [
    path('admin/', admin.site.urls),
    # path('',include(router.urls)),
    path('stulist/',views.StudentListApi.as_view()),
    path('stucreate/',views.StudentCreateApi.as_view()),
    path('sturetreive/<int:pk>',views.StudentRetreiveApi.as_view()),
    path('stuupdate/<int:pk>',views.StudentUpdateApi.as_view()),
    path('sturetriveupdatedestroy/<int:pk>',views.StudentRetreiveUpdateDestroyApi.as_view()),
    path('stu-auth',include('rest_framework.urls')),
]
