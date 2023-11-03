from django.contrib import admin
from django.urls import path
from turn.views import *
from rest_framework_simplejwt.views import(
    TokenObtainPairView,
    TokenRefreshView
)

urlpatterns = [
    path('admin/', admin.site.urls),
    path('home', home, name='home'),
    path('post-todo', post_todo, name='post-todo'),
    path('get-todo' , get_todo, name='get-todo'),
    path('delete', delete_todo, name='delete'),
    path('update_patch', update_patch, name='update_patch'),
    path('class', TodoClass.as_view(), name='class'),
    path('with/<str:city_name>/', weather_view, name='with')
] 
