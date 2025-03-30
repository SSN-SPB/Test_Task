# https://www.mongodb.com/languages/python
# https://www.w3schools.com/python/python_mongodb_create_db.asp
import pymongo


def main():
    myclient = pymongo.MongoClient("mongodb://localhost:27017/")
    mydb = myclient["mydatabase"]
    mycol = mydb["customers"]


if __name__ == "__main__":
    main()
