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
    # serializer.is_valid(raise_exception=True)
    serializer.is_valid()

    username_or_phone_number = serializer.validated_data.get('username')
    password = serializer.validated_data.get('password')
    print("password")
    print(serializer.validated_data.get('password'))
    user = UserAccount.objects.filter(username=username_or_phone_number).first()
    if user is None:
        user = UserAccount.objects.filter(mobile=username_or_phone_number).first()
    if user is None or not user.check_password(password):
    # if user is None:
        return Response({'message': 'Invalid credentials'}, status=status.HTTP_400_BAD_REQUEST)

    # Generate the JWT token
    jwt_token = JWTAuthentication.create_jwt(user)

    return Response({'status':'succeed', 'message': 'login_successfully','data':jwt_token})