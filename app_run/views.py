from rest_framework.decorators import api_view
from rest_framework.response import Response
from django.conf import settings

from rest_framework import viewsets
from .models import Run
from django.contrib.auth.models import User
from .serializers import RunSerializer, UserSerializer


@api_view(['GET'])
def company_details(request):
    details = {'company_name': settings.COMPANY_NAME,
               'slogan': settings.SLOGAN,
               'contacts': settings.CONTACTS}
    return Response(details)


class RunViewSet(viewsets.ModelViewSet):
    queryset = Run.objects.all()
    serializer_class = RunSerializer
    
    
class UserViewSet(viewsets.ReadOnlyModelViewSet):
    queryset = User.objects.all()
    serializer_class = UserSerializer    

    def get_queryset(self):
        queryset = User.objects.filter(is_superuser=False)
        
        type_param = self.request.query_params.get('type')
        
        if type_param == 'coach':
            return queryset.filter(is_staff=True)
        
        elif type_param == "athlete":
            return queryset.filter(is_staff=False)
        
        return queryset
        
        


