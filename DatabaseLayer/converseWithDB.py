import pymongo

from pymongo import MongoClient
from itertools import chain


client = MongoClient('35.154.113.253', 27017)



def getColumnValues(dbName, collectionName, columnName):
    print dbName, collectionName
    db = client[dbName]
    collection = db[collectionName]
    result =  collection.find({}, {columnName:1, "_id":0})
    values = []
    for doc in result:
        if columnName in doc.keys():
            values.append(doc[columnName])
    return list(set(values))


def getColumnValuesForDomain(dbName, collectionName, columnName, domain):
    print dbName, collectionName
    db = client[dbName]
    collection = db[collectionName]
    result =  collection.find({"Domain":domain}, {columnName:1, "_id":0})
    values = []
    for doc in result:
        if columnName in doc.keys():
            values.append(doc[columnName])
    return list(set(values))


def getSchemaDetails(dbName, collectionName):
    print dbName, collectionName
    db = client[dbName]
    collection = db[collectionName]
    schematodo = collection.find_one()
    for key in schematodo:
        print key,type(key)




def printColVals(columnName):
    print columnName
    print "flipkart",getColumnValues("looksmash_normalized", "flipkart_normalized", columnName)
    print "jabong",getColumnValues("looksmash_normalized", "jabong_normalized", columnName)
    print "snapdeal",getColumnValues("looksmash_normalized", "snapdeal_normalized", columnName)




def getFullData(dbName, collectionName):
    db = client[dbName]
    collection = db[collectionName]
    result = collection.find()
    return result


def getGenderData(dbName, collectionName, gender):
    db = client[dbName]
    collection = db[collectionName]
    result = collection.find({"Sex": gender})
    return result

def getFullDataFromDomain(dbName, collectionName, domain):
    db = client[dbName]
    collection = db[collectionName]
    result = collection.find({"Domain": domain})
    return result


def getGenderDataFromDomain(dbName, collectionName, gender, domain):
    db = client[dbName]
    collection = db[collectionName]
    result = collection.find({"Sex": gender, "Domain": domain})
    return result


def getGenderDataFromDomainWithCategory(dbName, collectionName, gender, domain, category):
    db = client[dbName]
    collection = db[collectionName]
    result = collection.find({"Sex": gender, "Domain": domain, "Category": category})
    return result




def getCategoryData(dbName, collectionName, category):
    db = client[dbName]
    collection = db[collectionName]
    result = collection.find({"Category": category})
    return result

def getCategoryDataFromDomain(dbName, collectionName, domain, *category):
    db = client[dbName]
    collection = db[collectionName]
    conditionList = []
    for cat in category:
        condition = {"Category": cat}
        conditionList.append(condition)

    finalQuery = {"$or": conditionList, "Domain": domain}
    result = collection.find(finalQuery)
    return result

def getSubCategoryDataFromDomain(dbName, collectionName, domain, *subCategory):
    db = client[dbName]
    collection = db[collectionName]
    conditionList = []
    for cat in subCategory:
        condition = {"Sub_category": cat}
        conditionList.append(condition)

    finalQuery = {"$or": conditionList, "Domain": domain}
    result = collection.find(finalQuery)
    return result



def getFullDataWithColors(dbName, collectionName, *colors):
    db = client[dbName]
    collection = db[collectionName]
    conditionList = []
    for color in colors:
        condition = {"Color": color}
        conditionList.append(condition)

    finalQuery = {"$or": conditionList}
    result = collection.find(finalQuery)
    return result


def getFullDataWithColorsAndCategory(dbName, collectionName, colors, *category):
    db = client[dbName]
    collection = db[collectionName]
    conditionListForColor = []
    conditionListForCategory = []
    for color in colors:
        condition = {"Color": color}
        conditionListForColor.append(condition)

    for cat in category:
        condition = {"Category": cat}
        conditionListForCategory.append(condition)

    finalQuery = {"$or": conditionListForColor, "$or": conditionListForCategory}
    result = collection.find(finalQuery)
    return result


def getFullDataWithColorsAndCategoryFromDomain(dbName, collectionName, domain, colors, *category):
    db = client[dbName]
    collection = db[collectionName]
    conditionListForColor = []
    conditionListForCategory = []
    for color in colors:
        condition = {"Color": {"$elemMatch":{"$eq":color}}}
        conditionListForColor.append(condition)

    for cat in category:
        condition = {"Category": cat}
        conditionListForCategory.append(condition)
    print conditionListForColor
    finalQuery = {"$and":[{"$or": conditionListForColor}, {"$or": conditionListForCategory}, {"Domain": domain}]}
    print finalQuery
    result = collection.find(finalQuery)
    return result

def getFullDataWithColorsAndTypesFromDomain(dbName, collectionName, domains, colors, types):
    db = client[dbName]
    collection = db[collectionName]
    conditionListForColor = []
    conditionListForType = []
    conditionListForDomain = []
    for color in colors:
        condition = {"Color": {"$elemMatch":{"$eq":color}}}
        conditionListForColor.append(condition)

    for type in types:
        condition = {"Type": type}
        conditionListForType.append(condition)

    for domain in domains:
        condition = {"Domain": domain}
        conditionListForDomain.append(condition)


    if len(conditionListForColor) > 0 :
        if len(conditionListForType) > 0:
            finalQuery = {"$and":[{"$or": conditionListForColor}, {"$or": conditionListForType}, {"$or": conditionListForDomain}]}

        else:
            finalQuery = {"$and":[{"$or": conditionListForColor}, {"$or": conditionListForDomain}]}

    elif len(conditionListForType) > 0 :
        finalQuery = {"$and":[{"$or": conditionListForType}, {"$or": conditionListForDomain}]}

    else:
        finalQuery = {"$or": conditionListForDomain}





    print finalQuery
    result = collection.find(finalQuery)
    return result


def phraseQuery(dbName, domains, colors, types, subCats, occasions):
    db = client[dbName]
    collection1 = db["looksmash_men"]
    collection2 = db["looksmash_women"]
    conditionListForColor = []
    conditionListForSubCat = []
    conditionListForDomain = []
    conditionListForType = []
    print subCats

    for color in colors:
        condition = {"Color": {"$elemMatch":{"$eq":color}}}
        conditionListForColor.append(condition)

    for subCat in subCats:
        condition = {"Sub_category": subCat}
        conditionListForSubCat.append(condition)

    for domain in domains:
        condition = {"Domain": domain}
        conditionListForDomain.append(condition)

    for type in types:
        condition = {"Type": type}
        conditionListForType.append(condition)

    conjunctionQueryForType = []
    conjunctionQueryForSubCat = []

    print conditionListForSubCat

    if len(conditionListForType) > 0:
        conjunctionQueryForType.append({"$or": conditionListForType})
        if len(conditionListForColor) > 0:
            conjunctionQueryForType.append({"$or": conditionListForColor})

        if len(conditionListForDomain) > 0:
            conjunctionQueryForType.append({"$or": conditionListForDomain})






    if len(conditionListForSubCat) > 0:
        conjunctionQueryForSubCat.append({"$or": conditionListForSubCat})
        if len(conditionListForColor) > 0:
            conjunctionQueryForSubCat.append({"$or": conditionListForColor})

        if len(conditionListForDomain) > 0:
            conjunctionQueryForSubCat.append({"$or": conditionListForDomain})





    finalQuery = {"$or" : []}

    if len(conjunctionQueryForType) > 0:
        finalQuery["$or"].append({"$and":conjunctionQueryForType})


    if len(conjunctionQueryForSubCat) > 0:
        finalQuery["$or"].append({"$and":conjunctionQueryForSubCat})



    print finalQuery
    result1 = collection1.find(finalQuery)
    result2 = collection2.find(finalQuery)
    result = [x for x in chain(result1, result2)]
    return result





def getFullDataWithColorsAndSubCategoryFromDomain(dbName, collectionName, domains, colors, subCats):
    db = client[dbName]
    collection = db[collectionName]
    conditionListForColor = []
    conditionListForSubCat = []
    conditionListForDomain = []
    for color in colors:
        condition = {"Color": {"$elemMatch":{"$eq":color}}}
        conditionListForColor.append(condition)

    for subCat in subCats:
        condition = {"Sub_category": subCat}
        conditionListForSubCat.append(condition)

    for domain in domains:
        condition = {"Domain": domain}
        conditionListForDomain.append(condition)


    finalQuery = {"$and":[{"$or": conditionListForColor}, {"$or": conditionListForSubCat}, {"$or": conditionListForDomain}]}
    print finalQuery
    result = collection.find(finalQuery)
    return result




def updateDocument(dbName, collectionName, id, attribute, value):
    db = client[dbName]
    collection = db[collectionName]
    collection.update({"_id": id},
                      {
                        "$set" : {attribute:value}
                      }
                      )



def renameFieldInDocument(dbName, collectionName, field, newVal):
    db = client[dbName]
    collection = db[collectionName]
    collection.update({}, {"$rename":{field:newVal}}, False, True);





def replaceDocument(dbName, collectionName, document):
    print "Replacing Doc ->", document
    db = client[dbName]
    collection = db[collectionName]
    id = document["_id"]
    collection.replace_one({"_id": id}, document)







