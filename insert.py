from models import generate_device
from mongoengine import connect
from elasticsearch import Elasticsearch


def insert_mongodb():
    connect('backoffice')
    for i in range(10**7):
        device = generate_device()
        device.save()


def insert_elasticsearch():
    es = Elasticsearch()
    for i in range(10**7):
        device = generate_device().to_json()
        es.index(index="backoffice", doc_type="device", id=i, body=device)


insert_elasticsearch()
