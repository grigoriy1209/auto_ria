from django.contrib.auth import get_user_model
from django.db.transaction import atomic

from rest_framework import permissions, serializers
from rest_framework.generics import ListCreateAPIView
from rest_framework.permissions import IsAuthenticated

from core.services.email_service import EmailService

from apps.users.models import ProfileModel

UserModel = get_user_model()


class RoleSerializer(serializers.Serializer):
    role = serializers.ChoiceField(choices=UserModel.ROLE_CHOICES)


class RoleListCreateView(ListCreateAPIView):
    serializer_class = RoleSerializer
    permission_classes = [IsAuthenticated]


class ProfileSerializer(serializers.ModelSerializer):
    class Meta:
        model = ProfileModel
        fields = ('id', 'name', 'surname', 'age', 'created_at', 'updated_at')


class UserSerializer(serializers.ModelSerializer):
    profile = ProfileSerializer()

    class Meta:
        model = UserModel
        fields = (
            'id',
            'email',
            'password',
            'is_active',
            'is_staff',
            'is_superuser',
            'last_login',
            'created_at',
            'updated_at',
            'profile',
        )

        read_only_fields = ('id', 'is_active', 'is_staff', 'is_superuser', 'last_login', 'created_at', 'updated_at')
        extra_kwargs = {
            'password': {
                'write_only': True,
            },
        }

    @atomic
    def create(self, validated_data):
        profile = validated_data.pop('profile')
        user = UserModel.objects.create_user(**validated_data)
        ProfileModel.objects.create(**profile, user=user)
        EmailService.register_email(user)
        return user
