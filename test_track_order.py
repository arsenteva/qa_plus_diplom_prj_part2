# Анна Арсентьева, 11 когорта, Инженер по тестированию плюс, финальный проект, часть 2

import sender_send_request
import data

def test_get_order_by_track():
    order_track = int(sender_send_request.get_track())
    response = sender_send_request.get_order(order_track)
    assert response.status_code == 200

