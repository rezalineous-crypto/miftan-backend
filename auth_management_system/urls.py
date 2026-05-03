# user_management_system/urls.py
from django.urls import path

from auth_management_system.controller.login_service_api import LoginServiceAPIView
from auth_management_system.controller.logout_service_api import LogoutServiceAPIView
from auth_management_system.controller.refresh_token_service_api import RefreshTokenServiceAPIView
from auth_management_system.controller.user_entity_access_service_api import UserEntityAccessServiceAPIView
from auth_management_system.controller.users_service_api import UsersServiceAPIView
urlpatterns = [
      
    path('login-service/', LoginServiceAPIView.as_view(), name='login-service'),
    path('users-service/', UsersServiceAPIView.as_view(), name='users-service'),
    path('logout-service/', LogoutServiceAPIView.as_view(), name='logout-service'),
    path('refresh-token-service/', RefreshTokenServiceAPIView.as_view(), name='refresh-token-service'),
    path('user-entity-access-service/', UserEntityAccessServiceAPIView.as_view(), name='user-entity-access-service'),
]
