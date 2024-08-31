from django.urls import path

from apps.cars.views import CarAddPhotoView, CarListCreateView, CarRetrieveUpdateDestroyView

urlpatterns = [
    path('', CarListCreateView.as_view(), ),
    path('/<int:pk>', CarRetrieveUpdateDestroyView.as_view(), ),
    path('/<int:pk>/photo', CarAddPhotoView.as_view(), ),

]

