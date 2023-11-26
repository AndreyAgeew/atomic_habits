from rest_framework import serializers
from django.contrib.auth import authenticate, get_user_model

from users.models import User


class UserSerializer(serializers.ModelSerializer):
    """
        Сериализатор для модели пользователя.

        Attributes:
            id (int): Уникальный идентификатор пользователя.
            email (str): Адрес электронной почты пользователя.
            first_name (str): Имя пользователя.
            last_name (str): Фамилия пользователя.
            avatar (str): Путь к изображению профиля пользователя.
            phone (str): Номер телефона пользователя.
            country (str): Страна, в которой проживает пользователь.
    """

    class Meta:
        model = get_user_model()
        fields = ['id', 'email', 'first_name', 'last_name', 'avatar', 'phone', 'country']


class UserLoginSerializer(serializers.Serializer):
    """
        Сериализатор для аутентификации пользователя.

        Attributes:
            email (str): Адрес электронной почты пользователя.
            password (str): Пароль пользователя.

        Methods:
            validate(data): Проверяет переданные данные на наличие
                корректных учетных данных пользователя.

        Raises:
            serializers.ValidationError: Если учетные данные некорректны или отсутствуют.

        Returns:
            dict: Словарь с проверенными данными, включая объект пользователя (если успешно).
    """
    email = serializers.EmailField()
    password = serializers.CharField(style={'input_type': 'password'}, trim_whitespace=False)

    def validate(self, data):
        email = data.get('email')
        password = data.get('password')

        if email and password:
            user = authenticate(request=self.context.get('request'), email=email, password=password)

            if not user:
                msg = 'Unable to log in with provided credentials.'
                raise serializers.ValidationError(msg, code='authorization')
        else:
            msg = 'Must include "email" and "password".'
            raise serializers.ValidationError(msg, code='authorization')

        data['user'] = user
        return data


class UserRegistrationSerializer(serializers.ModelSerializer):
    """
    Сериализатор для регистрации нового пользователя на основе модели User.

    Attributes:
        password (str): Пароль пользователя.

    Methods:
        create(validated_data): Метод для создания нового пользователя на основе валидированных данных.

    Returns:
        User: Объект пользователя.
    """
    password = serializers.CharField(write_only=True)

    class Meta:
        model = User
        fields = ('email', 'password', 'first_name', 'last_name', 'avatar', 'phone', 'country', 'chat_id')

    def create(self, validated_data):
        user = User.objects.create(
            email=validated_data['email'],
            first_name=validated_data.get('first_name', ''),
            last_name=validated_data.get('last_name', ''),
            avatar=validated_data.get('avatar', None),
            phone=validated_data.get('phone', ''),
            country=validated_data.get('country', ''),
            chat_id=validated_data.get('chat_id', '0'),
        )
        user.set_password(validated_data['password'])
        user.save()
        return user
