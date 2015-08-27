from mongoengine import *
from faker import Faker

fake = Faker()

class OS(EmbeddedDocument):
    name = StringField()
    version = StringField()

class Hardware(EmbeddedDocument):
    manufacturer = StringField()
    model = StringField()
    texture_format = StringField()
    gpu_extension = StringField()

class Cor3(EmbeddedDocument):
    files_versions = ListField(StringField())

class Device(Document):
    merchant = IntField()
    identifier = StringField()
    uid = StringField()
    version = StringField()
    locale = StringField()
    os = EmbeddedDocumentField(OS)
    hardware = EmbeddedDocumentField(Hardware)
    cor3 = EmbeddedDocumentField(Cor3)
    account_id = IntField()
    app_id = IntField()

    meta = {'indexes': [
        {'fields': ['$identifier']
        }
    ]}

def generate_device():
    os = OS(name=fake.word(), version=fake.word())
    hardware = Hardware(
        manufacturer=fake.word(),
        model=fake.word(),
        texture_format=fake.word(),
        gpu_extension=fake.word()
    )
    cor3 = Cor3(files_versions=[fake.word(), fake.word()])
    device = Device(
        merchant=fake.random_int(),
        identifier=fake.sha256(),
        uid=fake.sha256(),
        version=fake.word(),
        locale=fake.word(),
        os=os,
        hardware=hardware,
        cor3=cor3,
        account_id=fake.random_int(),
        app_id=fake.random_int()
    )
    return device
