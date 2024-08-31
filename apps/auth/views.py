from rest_framework.generics import GenericAPIView
from rest_framework.permissions import AllowAny


class ActiveUserView(GenericAPIView):
    permission_classes = [AllowAny,]

    # def post(self, *args, **kwargs):
    #     token = kwargs.get('token')
    #     try:
    #         user =J
