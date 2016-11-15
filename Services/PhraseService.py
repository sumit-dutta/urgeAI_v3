import IntelligenceLayer.PhraseParser.phraseParser as pp
import DatabaseLayer.converseWithDB as cdb
import json
import IntelligenceLayer.RuleEngine.ruleEngine as re
from operator import itemgetter

def getPhraseProducts(userprefs):

    bodyPrefs = {
        "accentuate": {
            "arms": False,
            "bust": False,
            "waist": False,
            "legs" : False
        },

        "bodyType": {
            "Oval": False,
            "Trapezoid": False,
            "Rectangle": False
        },

        "hide": {
            "arms": False,
            "bust": False,
            "stomach": False,
            "hips and thighs": False
        }
    }


    phrase = userprefs["phrase"]
    mappedAttrs = pp.extractPrefsFromPhrase(phrase)

    colors = []
    types = []
    subCats = []
    occasions = []
    scores = cdb.getFullData("looksmash_rules", "accentuate_women")[0]
    scores_men = cdb.getFullData("looksmash_rules", "accentuate_men")[0]
    hideScores = cdb.getFullData("looksmash_rules", "hide")[0]

    if "Colors" in mappedAttrs.keys():
        colors = mappedAttrs["Colors"]

    if "Type" in mappedAttrs.keys():
        types = mappedAttrs["Type"]

    if "Sub_category" in mappedAttrs.keys():
        subCats = mappedAttrs["Sub_category"]

    if "Occasion" in mappedAttrs.keys():
        occasions = mappedAttrs["Occasion"]

    products = cdb.phraseQuery("looksmash_db", ["ShoppersStop"], colors, types, subCats, occasions)

    if userprefs["gender"] == "Female":

        for bodyPart in userprefs["accentuate"]:
            bodyPrefs["accentuate"][bodyPart] = True

        for bodyPart in userprefs["hide"]:
            bodyPrefs["hide"][bodyPart] = True


    elif userprefs["gender"] == "Male":
        for bodyType in userprefs["bodyType"]:
            bodyPrefs["bodyType"][bodyType] = True


    for doc in products:
        accentuateScore, accentuateMsg = re.computeAccentuateScores(doc, bodyPrefs, scores) if userprefs["gender"] == "Female" else re.computeAccentuateScoresForMen(doc, bodyPrefs, scores_men)
        hideScore =  re.computeHideScores(doc, bodyPrefs, hideScores) if userprefs["gender"] == "Female" else 0
        doc["score"] = accentuateScore + hideScore

    feed = sorted(products, key=itemgetter('score'))


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



