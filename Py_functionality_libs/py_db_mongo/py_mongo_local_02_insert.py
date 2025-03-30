# https://www.mongodb.com/languages/python
# https://www.w3schools.com/python/python_mongodb_create_db.asp
# https://www.w3schools.com/python/showpython.asp?filename=demo_mongodb_query
import pymongo


def main():
    myclient = pymongo.MongoClient("mongodb://localhost:27017/")
    mydb = myclient["db_test230330"]
    mycol = mydb["db_test230330_connect"]
    mydict = {"name": "John", "address": "Highway 37"}
    x = mycol.insert_one(mydict)


if __name__ == "__main__":
    main()
