from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework.authtoken.models import Token

from .models import User


class SignupView(APIView):
    def post(self, request):
        user = User.objects.create_user(user_number=request.data['hello'])

        user.save()

        token = Token.objects.create(user=user)
        print(token)
        return Response({"Token": token.key})
