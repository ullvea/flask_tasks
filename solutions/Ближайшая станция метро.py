import requests

server_address = 'http://geocode-maps.yandex.ru/1.x/?'
api_key = 'f86828c6-788e-41e3-bdfe-9f45d8f7ca92'
geocode = input('Введите адрес: ')
# Готовим запрос.
geocoder_request = f'{server_address}apikey={api_key}&geocode={geocode}&kind=metro&format=json'

# Выполняем запрос.
response = requests.get(geocoder_request)
if response:
    # Преобразуем ответ в json-объект
    json_response = response.json()
    toponym = json_response["response"]["GeoObjectCollection"]["featureMember"][0]["GeoObject"]
    print(toponym)
    # Полный адрес топонима:
    toponym_address = toponym["metaDataProperty"]["GeocoderMetaData"]["text"]
    # Координаты центра топонима:
    toponym_coodrinates = toponym["Point"]["pos"]
    # Печатаем извлечённые из ответа поля:
    print(toponym_address, "имеет координаты:", toponym_coodrinates)
else:
    print("Ошибка выполнения запроса:")
    print(geocoder_request)
    print("Http статус:", response.status_code, "(", response.reason, ")")