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


from django.contrib.auth import get_user_model
from rest_framework import views, permissions, status
from rest_framework.permissions import IsAuthenticated
from rest_framework.response import Response

from .serializer import ObtainTokenSerializer
from .models import JWTAuthentication

@api_view(['POST'])
def obtain_token(request):
    # permission_classes = [permissions.AllowAny]
    serializer_class = ObtainTokenSerializer
    serializer = serializer_class(data=request.data)
    if(serializer.is_valid()):
        username_or_phone_number = serializer.validated_data.get('username')
        password = serializer.validated_data.get('password')
        user = UserAccount.objects.filter(username=username_or_phone_number).first()
        if user is None:
            user = UserAccount.objects.filter(mobile=username_or_phone_number).first()
        if user is None or not user.check_password(password):
            return Response({'message': 'Invalid credentials'}, status=status.HTTP_400_BAD_REQUEST)
        jwt_token = JWTAuthentication.create_jwt(user)
        response_data =  {'status':'succeed', 'message': 'login_successfully','jwt':jwt_token,"is_engineer":"0","is_supervisor":"0"}
        if(user.type.id==2):
            response_data["is_engineer"] = 1

        if(user.type.id==3):
            response_data["is_supervisor"] = 1
        
        print(response_data)
        print(user.type.id)
        return Response(response_data, status=status.HTTP_200_OK)
    else:
        return Response({'status':'failed', 'message': 'token validation failed',})

@api_view(['GET'])
def validate_token(request):
    auth_status = JWTAuthentication.authenticate(request)
    auth_status['user'] = None
    return Response(auth_status,200)