from django.urls import path

from apps.auto_salons.views import AutoSalonAddCarView, AutoSalonListCreateView

urlpatterns = [
    path('', AutoSalonListCreateView.as_view()),
    path('/<int:pk>/cars', AutoSalonAddCarView.as_view()),
]