from django.forms import model_to_dict
from rest_framework import status
from rest_framework.response import Response
from rest_framework.views import APIView


from rest_framework.generics import GenericAPIView, ListCreateAPIView, RetrieveUpdateDestroyAPIView


from rest_framework.mixins import ListModelMixin, RetrieveModelMixin, UpdateModelMixin, DestroyModelMixin, \
    CreateModelMixin

from apps.cars.filter import car_filter
from apps.cars.models import CarModel
from apps.cars.serializers import CarSerializer


class CarListCreateView(GenericAPIView, CreateModelMixin, ListModelMixin):
    serializer_class = CarSerializer
    queryset = CarModel.objects.all()

    def get_queryset(self):
        return car_filter(self.request.query_params)

    def post(self, request, *args, **kwargs):
        return super().create(request, *args, **kwargs)

    def get(self, request, *args, **kwargs):
        return super().list(request, *args, **kwargs)


class CarRetrieveUpdateDestroyView(GenericAPIView, RetrieveModelMixin, UpdateModelMixin, DestroyModelMixin):
    serializer_class = CarSerializer

    def get(self, request, *args, **kwargs):
        return super().retrieve(request, *args, **kwargs)

    def put(self, request, *args, **kwargs):
        return super().update(request, *args, **kwargs)

    def patch(self, request, *args, **kwargs):
        return super().partial_update(request, *args, **kwargs)

    def delete(self, request, *args, **kwargs):
        return super().destroy(request, *args, **kwargs)









