from django.http import JsonResponse
from django.views.decorators.csrf import csrf_exempt
from . import controller


def create_address(request):
    controller.create_address()
    return JsonResponse({
        "status": "OK",
        "message": "Address created"
    }, status=200)


def get_cities(request):
    return JsonResponse({
        "status": "OK",
        "cities": controller.get_cities()
    }, status=200)


def get_districts(request):
    return JsonResponse({
        "status": "OK",
        "districts": controller.get_districts(request)
    }, status=200)


def get_wards(request):
    return JsonResponse({
        "status": "OK",
        "wards": controller.get_wards(request)
    }, status=200)


def auth(request, func):
    if request.method == "POST":
        try:
            return JsonResponse({
                "status": "OK",
                "token": func(request)
            }, status=200)
        except Exception as e:
            return JsonResponse({
                "status": "ER",
                "message": str(e)
            }, status=400)
    else:
        return JsonResponse({
            "status": "ER",
            "message": "Method not allowed"
        }, status=405)


@csrf_exempt
def create_customer(request):
    return auth(request, controller.create_customer)


@csrf_exempt
def create_seller(request):
    return auth(request, controller.create_seller)


@csrf_exempt
def login(request):
    return auth(request, controller.login)
