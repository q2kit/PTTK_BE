from django.http import JsonResponse
from controllers import accountController


def auth(request, func):
    if request.method == "POST":
        try:
            return JsonResponse({
                "status": "OK",
                "token": func(request)
            })
        except Exception as e:
            return JsonResponse({
                "status": "ER",
                "error": str(e)
            })
    else:
        return JsonResponse({
            "status": "ER",
            "error": "Invalid request method"
        })


def register(request):
    return auth(request, accountController.register)


def login(request):
    return auth(request, accountController.login)

    