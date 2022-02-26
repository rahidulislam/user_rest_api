from django.urls import path
from rest_framework.routers import SimpleRouter
from accounts.views import UserAPIView,RegisterAPIView
app_name = 'accounts'

routers = SimpleRouter()
routers.register('users', UserAPIView, basename='users')

#urlpatterns = routers.urls
urlpatterns = [
    path('list/', RegisterAPIView.as_view(), name='register')
]
