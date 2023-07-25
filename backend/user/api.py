from rest_framework import status
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


# 쿠키로 관리하려면?
# token = request.COOKIES.get('jwt')
# response.delete_cookie('jwt')

class GetToken(APIView):
    def post(self, request):
        user, _ = User.objects.get_or_create(user_number=request.data.get("user_number"), user_number_repeat=request.data.get("user_number", ""))

        payload = {
            'user_number': user.user_number,
            'exp': datetime.datetime.now() + datetime.timedelta(minutes=60),
            'iat': datetime.datetime.now()
        }

        token = jwt.encode(payload, "secretJWTkey", algorithm="HS256").decode('utf-8')

        response = Response()
        response.set_cookie(key='jwt', value=token, httponly=True)
        response.data = {
            'token': token
        }
        response.status = status.HTTP_201_CREATED
        return response
