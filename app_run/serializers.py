from rest_framework import serializers
from .models import Run
from django.contrib.auth.models import User


class RunSerializer(serializers.ModelSerializer):
    athlete_data = serializers.SerializerMethodField() 
    class Meta:
        model = Run
        fields = '__all__'
        
    def get_athlete_data(self, obj):
        user = obj.athlete
        return {
            'id' : user.id,
            'username' : user.username,
            'last_name' : user.last_name,
            'first_name' : user.first_name
        }
        
        
        
        
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
        
                