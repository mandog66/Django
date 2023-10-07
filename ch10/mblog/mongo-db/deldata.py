import pymongo
import list

def main():
    client, collections = list.list_mongodb_data("ch08", "posts")

    name = input("Please enter the name that you want to delete : ")
    while name != "":
        collections.delete_one({"name":name})
        name = input("Please enter the name that you want to delete : ")

    records = collections.find()
    for rec in records:
        print(rec)
    return None

if __name__ == '__main__':
    main()
