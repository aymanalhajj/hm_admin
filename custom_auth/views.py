from rest_framework.response import Response
from rest_framework.decorators import api_view
from .serializer import UserAccountSerializer
from .models import UserAccount



@api_view(['POST'])
def user_login(request):
    serializer = UserAccountSerializer(data = request.data)
    data = {}
    if serializer.is_valid():
        request_data = serializer.data
        user_count = UserAccount.objects.filter(username=request_data.get('username'),password = request_data.get('password')).count()
        #user_count = Client.objects.filter(username='ayman',password = 'ayman').count
        if user_count > 0:
            # return token
            data['status'] = 'login.succeed'
            data['token'] = 'token53453gdgfdgf'
            data['user_count'] = user_count
            return Response(data, status = 200)
        else:
            data['status'] = 'login.failed'
            data['message'] = 'imvalid.credintials'
            return Response(data, status = 401)
    else:
        data['status'] = 'login.failed'
        data['message'] = serializer.errors
        return Response(data, status = 400)

@api_view(['POST'])
def user_register(request):
    serializer = UserAccountSerializer(data=request.data)
    if serializer.is_valid():
        serializer.save()
        return Response(serializer.data)
    
    return Response(serializer.error_messages)