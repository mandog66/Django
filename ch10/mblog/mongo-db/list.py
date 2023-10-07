import pymongo

def list_mongodb():
    client = pymongo.MongoClient('mongodb://root:example@mongo:27017/')
    alldb = client.list_database_names()
    return print(alldb)

def list_mongodb_data(dbName: str, doc: str):
    client = pymongo.MongoClient('mongodb://root:example@mongo:27017/')
    collections = client[dbName][doc]
    records = collections.find()
    for rec in records:
        print(rec)
    return client, collections

if __name__ == '__main__':
    list_mongodb()

    list_mongodb_data("ch08", "bodyinfo")