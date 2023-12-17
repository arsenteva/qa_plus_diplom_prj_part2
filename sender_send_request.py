# Анна Арсентьева, 11 когорта, Инженер по тестированию плюс, финальный проект, часть 2

import configuration
import requests
import data

# Создаем заказ
def post_new_order():
    return requests.post(configuration.URL_SERVICE + configuration.CREATE_ORDER_PATH,
                         json=data.order_body)

# Сохраняем номер заказа
def get_track():
    track_id = post_new_order().json()["track"]
    return track_id

# Получаем заказ по его номеру
def get_order(track_id):
    return requests.get(configuration.URL_SERVICE + configuration.GET_ORDER_INFO_PATH + f"?t={track_id}")


