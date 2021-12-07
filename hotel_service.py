""" Import """
import time
import pymongo
import datetime
import numpy as np
import threading
from multiprocessing import Queue

mongo_cluster = pymongo.MongoClient("mongodb+srv://fulophunor:Asdf3210@cluster0.srkbk.mongodb.net/"
                                    "HotelDB?retryWrites=true&w=majority")

mongo_database = mongo_cluster["HotelDB"]
mongo_collection = mongo_database["Hotels"]


service_queue = Queue()
SLEEP_INTERVAL = 10


def push_to_database(data_to_push):
    """" push to database"""
    data_to_push["Time"] = str.replace(str(datetime.datetime.now()), " ", "T")
    service_queue.put(data_to_push)


def query_last_element():
    """ queue last element """
    return mongo_collection.find_one({}, sort=[('_id', pymongo.DESCENDING)])


def queue_process():
    """ queue process """
    print("Queue started!")
    while True:
        time.sleep(SLEEP_INTERVAL)
        print("Queue check!")
        while not service_queue.empty():
            data = service_queue.get()

            hotel_avg = np.average(list(data["hotel_room_temperature"].values()))
            data["hotel_room_temperature"]["Average"] = hotel_avg

            hotel_max = np.max(list(data["hotel_room_temperature"].values()))
            data["hotel_room_temperature"]["Maximum_temperature"] = hotel_max

            hotel_min = np.min(list(data["hotel_room_temperature"].values()))
            data["hotel_room_temperature"]["Minimum_temperature"] = hotel_min

            mongo_collection.insert_one(data)


queue_thread = threading.Thread(target=queue_process)
queue_thread.start()
