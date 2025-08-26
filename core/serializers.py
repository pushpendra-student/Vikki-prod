
from djoser.serializers import UserCreateSerializer as MainUserCreateSerializer, UserSerializer as BaseUserSerializer


class UserCreateSerializer(MainUserCreateSerializer):
    class Meta(MainUserCreateSerializer.Meta):
        fields = ['id', 'username', 'password',
                  'email', 'first_name', 'last_name']


class UserSerializer(BaseUserSerializer):
    class Meta(BaseUserSerializer.Meta):
        fields = ['id', 'username', 'email', 'first_name', 'last_name']
