
from django.contrib import admin
from django.urls import path
from api import views
urlpatterns = [
    path('admin/', admin.site.urls),
    path('stulistapi/',views.StudentApiView.as_view()),
    path('stucreateapi/',views.StudentCreate.as_view()),
    path('sturetreiveapi/<int:pk>',views.StudentRetrieve.as_view()),
    path('stuupdateapi/<int:pk>',views.StudentUpdate.as_view()),
    path('studeleteapi/<int:pk>',views.StudentDestry.as_view()),
]
