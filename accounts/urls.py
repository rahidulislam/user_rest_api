from django.urls import path
from rest_framework.routers import SimpleRouter
from accounts.views import UserAPIView
app_name = 'accounts'

routers = SimpleRouter()
routers.register('users', UserAPIView, basename='users')

urlpatterns = routers.urls