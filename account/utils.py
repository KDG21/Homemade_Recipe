import jwt
import json

from django.http import HttpResponse

from homemade_recipe.settings import SECRET_KEY, ALGORITHM
from account.models import Account

def login_check(func):
    def wrapper(self, request, *args, **kwargs):
        try:
            token = request.headers.get('Authorization', None)
            payload = jwt.decode(token, SECRET_KEY, algorithms=ALGORITHM)
            if Account.objects.filter(id=payload['id']):
                user = Account.objects.get(id=payload['id'])
                request.user = user
        except jwt.exceptions.DecodeError:
            return HttpResponse(status=401)
        except Account.DoesNotExist:
            return HttpResponse(status=400)
        return func(self, request, *args, **kwargs)
    return wrapper