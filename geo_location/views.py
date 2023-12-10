from django.shortcuts import render
from rest_framework.response import Response
from res_framework.decorators import api_view
from .serializer import GeoLocationSerializer
from .models import GeoLocation


@api_view(['POST'])
def add_location(request):
    serializer = GeoLocationSerializer(data = request.data)
    if serializer.is_valid():
        serializer.save()
        return Response({'status':'succeed', 'message': 'organization_location_created_successfully'})
    else:
        print(serializer.errors)
        return Response({'status':'failed','errors': serializer.errors})


