from rest_framework.decorators import APIView
from rest_framework.renderers import JSONRenderer
from rest_framework.response import Response
from rest_framework.exceptions import AuthenticationFailed
from .models import User
# install PyJWT
import jwt, datetime

# 회원가입
from .serializers import UserSerializer


class RegisterView(APIView):
    def post(self, request):
        serializer = UserSerializer(data=request.data)
        serializer.is_valid(raise_exception=True)
        serializer.save()
        return Response(serializer.data)


class LoginView(APIView):
    def post(self, request):
        user_number = request.data['user_number']

        user = User.objects.get(user_number=user_number)
        serialize_user = UserSerializer(user)
        json_user = JSONRenderer().render(serialize_user.data)

        if user is None:
            raise AuthenticationFailed('User does not found!')

        ## JWT 구현 부분
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


class LogoutView(APIView):
    def post(self, req):
        res = Response()
        res.delete_cookie('jwt')
        res.data = {
            "message": 'success'
        }

        return res
