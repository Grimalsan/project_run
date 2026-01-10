from rest_framework import serializers
from .models import Run
from django.contrib.auth.models import User


class RunSerializer(serializers.ModelSerializer):
    class Meta:
        model = Run
        fields = '__all__'
        
        
class UserSerializer(serializers.ModelSerializer):
    type = serializers.SerializerMethodField() # Так мы задаем вычисляемое поле

    class Meta:
        model = User
        fields = ['id', 'date_joined', 'username', 'last_name', 'first_name', 'type'] # Здесь добавлено поле type, которого нет в модели

    # Определяем метод, который вычисляет значение поля
    def get_type(self, obj):
        if obj.is_staff:
            return 'coach'
        return 'athlete'
        
                