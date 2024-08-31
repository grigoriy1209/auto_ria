from rest_framework import status
from rest_framework.generics import GenericAPIView, ListCreateAPIView
from rest_framework.permissions import IsAuthenticated
from rest_framework.response import Response

from apps.auto_salons.models import AutoSalonModel
from apps.auto_salons.serializers import AutoSalonSerializer
from apps.cars.serializers import CarSerializer


class AutoSalonListCreateView(ListCreateAPIView):
    serializer_class = AutoSalonSerializer
    queryset = AutoSalonModel.objects.all()
    permission_classes = (IsAuthenticated,)


class AutoSalonAddCarView(GenericAPIView):
    queryset = AutoSalonModel.objects.all()
    permission_classes = (IsAuthenticated,)

    def post(self, *args, **kwargs):
        auto_salon = self.get_object()
        data = self.request.data
        serializer = CarSerializer(data=data)
        serializer.is_valid(raise_exception=True)
        serializer.save(auto_salon=auto_salon)
        as_serializer = AutoSalonSerializer(auto_salon)
        return Response(as_serializer.data, status.HTTP_201_CREATED)
