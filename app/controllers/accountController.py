from models.account import Account
import hashlib
import datetime
import jwt

from django.conf import settings

SECRET_KEY = settings.SECRET_KEY


def login(request):
    try:
        username = request.POST.get("username")
        password = request.POST.get("password")
        account = Account.objects.get(username=username)
        if account.password == hashlib.sha256(password.encode()).hexdigest():
            return jwt.encode({
                "uid": str(account.uuid),
                "iat": datetime.datetime.utcnow(),
                "exp": datetime.datetime.utcnow() + datetime.timedelta(days=30)
            }, SECRET_KEY)
        else:
            raise Exception("Invalid password")
    except Account.DoesNotExist:
        raise Exception("Account does not exist")
    except KeyError:
        raise Exception("Invalid request body [username, password]")