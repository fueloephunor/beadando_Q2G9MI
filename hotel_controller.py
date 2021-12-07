""" Import """
from flask import Blueprint, request, Response
import hotel_service as service

hotel_api = Blueprint('hotel_controller', __name__)


@hotel_api.route('/add_data', methods=['POST'])
def receive_data():
    """ receive data """
    data = request.get_json()

    if "hotel_name" not in data or "hotel_room_temperature" not in data:
        return Response("Bad arguments", 400)

    print(data)
    service.push_to_database(data)
    return Response(f"Data received successfully", 200)


@hotel_api.route('/get_data', methods=["GET"])
def return_data():
    """ return data """
    last_element = service.query_last_element()
    print(last_element)
    return Response(f"Data received successfully", 200)


@hotel_api.route('/delete_data', methods=["DELETE"])
def delete_data():
    service.mongo_collection.delete_many({})
    return Response(f"Data delete successfully", 200)