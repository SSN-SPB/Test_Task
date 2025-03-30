import pymongo


def getFromMongo():

    myclient = pymongo.MongoClient("mongodb://localhost:27017/")
    mydb = myclient["mydatabase"]
    mycol = mydb["customers"]

    myquery = {"address": "Park Lane 38"}

    mydoc = mycol.find(myquery)
    return mydoc


def main():
    print(getFromMongo())
    for x in getFromMongo():
        print(x)


if __name__ == "__main__":
    main()
