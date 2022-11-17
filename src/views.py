from django.http import JsonResponse

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
