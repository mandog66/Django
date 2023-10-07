import pymongo
import list

def main():
    client, collections = list.list_mongodb_data("ch08", "posts")

    name = input("Name : ")
    while name != "":
        age = input("Age(kg) : ")
        height = input("Height(cm) : ")
        collections.insert_one({"name":name, "age":age, "height":height})
        name = input("Name : ")

    records = collections.find()
    for rec in records:
        print(rec)
    return None

if __name__ == '__main__':
    main()
