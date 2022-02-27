from django.urls import path
from rest_framework.routers import SimpleRouter
from accounts.views import RegisterView
from rest_framework_simplejwt.views import (
    TokenObtainPairView,
    TokenRefreshView,
    TokenVerifyView
)
app_name = 'accounts'

#routers = SimpleRouter()
#routers.register('users', UserAPIView, basename='users')
#urlpatterns = routers.urls

urlpatterns = [
    path('create/', RegisterView.as_view(), name='register'),
    path('api/token/', TokenObtainPairView.as_view(), name='token_obtain_pair'),
    path('api/token/refresh/', TokenRefreshView.as_view(), name='token_refresh'),
    path('api/token/verify/', TokenVerifyView.as_view(), name='token_verify'),
]
