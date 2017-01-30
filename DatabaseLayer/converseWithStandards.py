
from pymongo import MongoClient


client = MongoClient('35.154.113.253', 27017)



def getStandardValues(dbName, collectionName, standardName):
    print dbName, collectionName
    db = client[dbName]
    collection = db[collectionName]
    result =  collection.find({}, {standardName:1,  "_id":0})
    return list(result)[0]