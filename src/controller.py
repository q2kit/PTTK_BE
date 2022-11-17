import jwt
import hashlib
import datetime

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


def create_customer(request):
    try:
        username = request.POST['username']
        password = request.POST['password']
        password = hashlib.sha256(password.encode()).hexdigest()
        first_name = request.POST['first_name']
        last_name = request.POST['last_name']
        phone_number = request.POST['phone_number']
        email = request.POST['email']
        city = request.POST['city']
        district = request.POST['district']
        ward = request.POST['ward']
        street = request.POST['street']
    except Exception as e:
        name_param = str(e).split("'")[1]
        raise Exception(f"Missing parameter: {name_param}")

    try:
        Account.objects.get(username=username)
        raise Exception("Username already exists")
    except:
        pass

    try:
        city = City.objects.get(id=city)
        district = District.objects.get(id=district)
        ward = Ward.objects.get(id=ward)
        if ward.district != district or district.city != city:
            raise Exception("Invalid address")
    except:
        raise Exception("Invalid address")

    account = Account.objects.create(username=username, password=password)
    Customer.objects.create(
        account=account,
        first_name=first_name,
        last_name=last_name,
        phone_number=phone_number,
        email=email,
        city=city,
        district=district,
        ward=ward,
        street=street
    )

    return jwt.encode({
        "uid": account.uuid,
        "iat": datetime.datetime.now(),
        "exp": datetime.datetime.now() + datetime.timedelta(days=7)})


def create_seller(request):
    try:
        token = request.headers['Authorization']
        uid = jwt.decode(token, verify=False)['uid']
    except KeyError:
        raise Exception("Missing token")
    except:
        raise Exception("Invalid token")

    try:
        shop_name = request.POST['shop_name']
        shop_description = request.POST['shop_description']
        phone_number = request.POST['phone_number']
    except Exception as e:
        name_param = str(e).split("'")[1]
        raise Exception(f"Missing parameter: {name_param}")

    account = Account.objects.get(uuid=uid)
    if account.seller:
        raise Exception("Just one shop per account")

    Seller.objects.create(
        account=account,
        shop_name=shop_name,
        shop_description=shop_description,
        phone_number=phone_number
    )


def login(request):
    try:
        username = request.POST['username']
        password = request.POST['password']
        password = hashlib.sha256(password.encode()).hexdigest()
    except Exception as e:
        name_param = str(e).split("'")[1]
        raise Exception(f"Missing parameter: {name_param}")

    try:
        account = Account.objects.get(username=username)
    except:
        raise Exception("Account not found")

    if account.password != password:
        raise Exception("Wrong password")

    return jwt.encode({
        "uid": account.uuid,
        "iat": datetime.datetime.now(),
        "exp": datetime.datetime.now() + datetime.timedelta(days=7)})
