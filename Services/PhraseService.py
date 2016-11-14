import IntelligenceLayer.PhraseParser.phraseParser as pp
import DatabaseLayer.converseWithDB as cdb
import json

def getPhraseProducts(phrase):
    mappedAttrs = pp.extractPrefsFromPhrase(phrase)

    colors = []
    types = []
    subCats = []
    occasions = []

    if "Colors" in mappedAttrs.keys():
        colors = mappedAttrs["Colors"]

    if "Type" in mappedAttrs.keys():
        types = mappedAttrs["Type"]

    if "Sub_category" in mappedAttrs.keys():
        subCats = mappedAttrs["Sub_category"]

    if "Occasion" in mappedAttrs.keys():
        occasions = mappedAttrs["Occasion"]

    feed = cdb.phraseQuery("looksmash_db", ["ShoppersStop"], colors, types, subCats, occasions)

    images = {}
    i=0
    for product in feed:
        images[i]={"image" :product["Image"],
                   # "msg" : product["msg"],
                   "url" : product["Url"],
                   "domain": product["Domain"],
                   # "score": product["score"],
                   "Color": product["Color"],
                   "Sub_category": product["Sub_category"],
                   "Product Name": product["Product Name"],
                   "Cost": product["Cost"],
                   "Brand": product["Brand"],
                   "Category": product["Category"],
                   }

        if "Neck" in product.keys():
            images[i]["Neck"] = product["Neck"],

        if "Sleeves" in product.keys():
            images[i]["Sleeves"] = product["Sleeves"]

        i = i+1

    return {"result": json.dumps(images)}



