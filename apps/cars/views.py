from rest_framework import status
from rest_framework.generics import GenericAPIView, ListCreateAPIView, RetrieveUpdateDestroyAPIView, UpdateAPIView
from rest_framework.mixins import (
    CreateModelMixin,
    DestroyModelMixin,
    ListModelMixin,
    RetrieveModelMixin,
    UpdateModelMixin,
)
from rest_framework.pagination import PageNumberPagination
from rest_framework.permissions import AllowAny, IsAuthenticated
from rest_framework.response import Response

from core.paginations import PagePagination

from apps.auto_salons.models import AutoSalonModel
from apps.cars.filter import CarFilter
from apps.cars.models import CarModel
from apps.cars.serializers import CarFotoSerializer, CarSerializer


class CarListCreateView(GenericAPIView, CreateModelMixin, ListModelMixin):
    serializer_class = CarSerializer
    queryset = CarModel.objects.all()
    filterset_class = CarFilter
    permission_classes = (AllowAny,)

    # def get_queryset(self):
    #     return car_filter(self.request.query_params)

    def post(self, request, *args, **kwargs):
        permission_classes = (IsAuthenticated,)
        auto_salon_id = request.data.get('auto_salon_id')
        auto_salon = None
        if auto_salon_id:
            auto_salon = AutoSalonModel.objects.get(id=auto_salon_id)

        serializer = self.get_serializer(data=request.data)
        serializer.is_valid(raise_exception=True)
        serializer.save(auto_salon=auto_salon)
        return Response(serializer.data, status=status.HTTP_201_CREATED)

    def get(self, request, *args, **kwargs):
        permission_classes = (AllowAny,)
        return super().list(request, *args, **kwargs)


class CarRetrieveUpdateDestroyView(RetrieveUpdateDestroyAPIView):
    serializer_class = CarSerializer
    queryset = CarModel.objects.all()

    def get_permissions(self):
        if self.request.method == 'DELETE':
            return (IsAuthenticated(),)
        return (AllowAny,)


class CarAddPhotoView(UpdateAPIView):
    # permission_classes = (IsAuthenticated,)
    permission_classes = (AllowAny,)
    serializer_class = CarFotoSerializer
    queryset = CarModel.objects.all()

    def perform_update(self, serializer):
        car = self.get_object()
        car.photo.delete()
        super().perform_update(serializer)














