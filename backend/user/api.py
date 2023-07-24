from rest_framework.decorators import APIView
from rest_framework.renderers import JSONRenderer
from rest_framework.response import Response
from rest_framework.exceptions import AuthenticationFailed
from .models import User
# install PyJWT
import jwt
import datetime

# 회원가입
from .serializers import UserSerializer


class GetToken(APIView):
    def post(self, request):
        user = User.objects.get_or_create(user_number=request['user_number'])

        payload = {
            'user_number': user.user_number,
            'exp': datetime.datetime.now() + datetime.timedelta(minutes=60),
            'iat': datetime.datetime.now()
        }

        token = jwt.encode(payload, "secretJWTkey", algorithm="HS256").decode('utf-8')

        response = Response()
        response.set_cookie(key='jwt', value=token, httponly=True)
        response.data = {
            'jwt': token
        }

        return response


class DeleteToken(APIView):
    def post(self):
        response = Response()
        response.delete_cookie('jwt')
        response.data = {
            "message": 'success'
        }
        return response


class UserView(APIView):
    def get(self, request):
        token = request.COOKIES.get('jwt')

        if not token:
            raise AuthenticationFailed('UnAuthenticated!')

        try:
            payload = jwt.decode(token, 'secretJWTkey', algorithms=['HS256'])

        except jwt.ExpiredSignatureError:
            raise AuthenticationFailed('UnAuthenticated!')

        user = User.objects.get(user_number=payload['user_number'])
        serializer = UserSerializer(user)

        return Response(serializer.data)

