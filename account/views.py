import json
import bcrypt
import jwt
# import requests

from django.http import HttpResponse, JsonResponse
from django.core.validators import validate_email, RegexValidator
from django.core.exceptions import ValidationError
from django.views import View

from homemade_recipe.settings import SECRET_KEY, ALGORITHM

from account.models import Account

# 회원가입
class SignUpView(View):
    def post(self, request):
        data = json.loads(request.body)
        id_validator = RegexValidator(
            regex = "^(?=.*[A-Za-z])(?=.*\d)([A-Za-z\d]){4,8}")
        password_validator = RegexValidator(
            regex = "^(?=.*[A-Za-z])(?=.*\d)([A-Za-z\d]){6,20}")
        try:
            id_validator(data['user_id'])
            user_id = data['user_id']

            if not Account.objects.filter(user_id=user_id).exists():
                password_validator(data['password'])
                account_pw = bcrypt.hashpw(data['password'].encode('utf-8'), bcrypt.gensalt()).decode('utf-8')
                if not Account.objects.filter(nickname=data['nickname']).exists():
                    Account.objects.create(
                        user_id      = data['user_id'],
                        password     = account_pw,
                        name         = data['name'],
                        nickname     = data['nickname'],
                        email        = validate_email(data['email']),
                        phone_number = data['phone_number'],
                        birthday     = data['birthday']
                    )
                    return HttpResponse(status = 200)
                return HttpResponse(status = 400)
            return HttpResponse(status = 400)
        except ValidationError:
            return HttpResponse(status = 400)
        except KeyError:
            return JsonResponse({'message':'INVALID KEY'}, status = 400)

# 로그인
class SignInView(View):
    def post(self, request):
        data = json.loads(request.body)
        user_id = data['user_id']
        try:
            if Account.objects.filter(user_id=user_id).exists():
                user = Account.objects.get(user_id=user_id)
                if user.del_yn == False:
                    if bcrypt.checkpw(data['password'].encode('utf-8'), user.password.encode('utf-8')):
                        token = jwt.encode({'id':user.id}, SECRET_KEY, algorithm = ALGORITHM).decode('utf-8')
                        return JsonResponse({'token':token}, status = 200)
                    return HttpResponse(status = 400)
                return HttpResponse(status = 401)
            return HttpResponse(status = 400)
        except KeyError:
            return JsonResponse({'message':'INVALID KEY'}, status = 400)

# 로그아웃

# 회원정보수정

# 마이페이지