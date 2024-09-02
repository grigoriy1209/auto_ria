from django.urls import path

from apps.auth.views import ActiveUserView

from rest_framework_simplejwt.views import TokenObtainPairView, TokenRefreshView

urlpatterns = [
    path('', TokenObtainPairView.as_view(), name='token_obtain_pair'),
    path('/refresh', TokenRefreshView.as_view(), name='token_refresh'),
    path('/activate/<str:token>', ActiveUserView.as_view(), name='token_activate'),


]