import math
import requests

apikey = "40d1649f-0493-4b70-98ba-98533de7710b"


def get_coordinates(city_name):
    try:
        url = "https://geocode-maps.yandex.ru/1.x/"
        params = {
            'apikey': apikey,
            'geocode': city_name,
            'format': 'json'

        }
        response = requests.get(url, params)
        json = response.json()
        coords_string = json['response']['GeoObjectCollection'][
            'featureMember'][0]['GeoObject']['Point']['pos']
        coord_l, crd = map(float, coords_string.split())
        return coord_l, crd
    except Exception as exep:
        return exep


def get_country(city_name):
    import requests
    try:
        url = "https://geocode-maps.yandex.ru/1.x/"
        params = {
            'apikey': apikey,
            'geocode': city_name,
            'format': 'json'
        }
        data = requests.get(url, params).json()
        return data['response']['GeoObjectCollection']['featureMember'][0][
            'GeoObject']['metaDataProperty']['GeocoderMetaData'][
            'AddressDetails']['Country']['CountryName']
    except Exception as excep:
        return 'Возникла ошибка! Её нужно устранить'


def get_distance(p1, p2):
    rad = 6373.0

    coord_l1 = math.radians(p1[0])
    crd1 = math.radians(p1[1])
    coord_l2 = math.radians(p2[0])
    crd2 = math.radians(p2[1])

    d_coord = coord_l2 - coord_l1
    d_crd = crd2 - crd1

    a = math.sin(d_crd / 2)
    2 + math.cos(crd1) * \
    math.cos(crd2) * math.sin(d_coord / 2) * 2
    length = 2 * math.atan2(a * 0.5, (1 - a) * 0.5)

    distance = rad * length
    return distance
