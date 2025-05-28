# https://www.mongodb.com/languages/python
from pymongo import MongoClient


def get_database():

    # Provide the mongodb atlas url to
    # connect python to mongodb using pymongo
    # CONNECTION_STRING = "mongodb://localhost/db_test230330"
    # CONNECTION_STRING =
    # "mongodb+srv://user:pass@cluster.mongodb.net/myFirstDatabase"
    CONNECTION_STRING = "mongodb+srv://actrealtyint:XpfXi8aOOWFu40Ev@cluster0.1rzubih.mongodb.net/ActualRealty_2022-09-22"

    # Create a connection using MongoClient.
    # You can import MongoClient or use pymongo.MongoClient
    client = MongoClient(CONNECTION_STRING)

    # Create the database for our example
    print(client["channels"])
    return client


def main():
    dbname = get_database()
    mycol = dbname["channels"]
    print("mycol")
    print(mycol)
    # myquery = {"name": {"$regex": "3$"}}

    mydoc = mycol.get_collection("channels")
    print(mydoc)
    # print(mydoc)
    for y in mydoc.find():
        print(y)


# This is added so that many files can reuse the function get_database()
if __name__ == "__main__":
    main()
