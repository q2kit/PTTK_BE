from .models import *


def create_address():
    f = open('address.csv', 'r', encoding='utf-8')
    for line in f:
        _, city, _, district, _, ward = line.split(',')
        city = city.strip()
        district = district.strip()
        ward = ward.strip()
        try:
            city = City.objects.get(name=city)
        except:
            city = City.objects.create(name=city)
        try:
            district = District.objects.get(name=district)
        except:
            district = District.objects.create(name=district, city=city)
        try:
            ward = Ward.objects.get(name=ward)
        except:
            ward = Ward.objects.create(name=ward, district=district)
    f.close()


def get_cities(request=None):
    return [{
        "id": city.id,
        "name": city.name
    } for city in City.objects.all()]


def get_districts(request):
    city = request.GET.get('city')
    return [{
        "id": district.id,
        "name": district.name
    } for district in District.objects.filter(city_id=city)]


def get_wards(request):
    district = request.GET.get('district')
    return [{
        "id": ward.id,
        "name": ward.name
    } for ward in Ward.objects.filter(district_id=district)]
