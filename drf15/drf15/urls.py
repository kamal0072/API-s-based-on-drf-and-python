from django.contrib import admin
from django.urls import path
from api import views

urlpatterns = [
    path('admin/', admin.site.urls),
    path('stulistapi/',views.StudentListApi.as_view()),
    path('stucreateapi/',views.StudentCreateApi.as_view()),
    path('sturetreiveapi/<int:pk>',views.StudentRetreiveApi.as_view()),
    path('studestrsyapi/<int:pk>',views.StudentDestroyApi.as_view()),
    path('studestrsyapi/<int:pk>',views.StudentDestroyApi.as_view()),
    path('stulistcreateapi/',views.StudentListCreateApi.as_view()),
    path('sturetreiveupdateapi/<int:pk>',views.StudentRetreiveUpdateApi.as_view()),
    path('sturetreivedestroyapi/<int:pk>',views.StudentRetreiveDestroyApi.as_view()),
    path('sturetreiveupdatedestroyapi/<int:pk>',views.StudentRetreiveUpdateDestroyApi.as_view()),
]
