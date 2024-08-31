from django.urls import path

from apps.users.views import UserBlockView, UserListCreateView, UserToAdminView, UserUnBlockView

urlpatterns = [
    path('', UserListCreateView.as_view(), name='users'),
    path('/<int:pk>/block', UserBlockView.as_view(), name='block'),
    path('/<int:pk>/un_block', UserUnBlockView.as_view(), name='un_block'),
    path('/<int:pk>/admins', UserToAdminView.as_view(), name='admins'),
]