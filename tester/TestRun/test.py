import json

import DatabaseLayer.converseWithDB as cdb
import DatabaseLayer.dataNormalization as dn
import IntelligenceLayer.Messaging.messagingEngine as me
import IntelligenceLayer.RuleEngine.ruleEngine as re
import RuleRepository.looksmashStandards as ls
import Utilities.RulesUtils.ruleUtils as ru
import random
import IntelligenceLayer.PhraseParser.phraseParser as pp


#print re.computeAccentuateScores(data, userPrefs)




# with open('../DataFiles/jabong_data.json', 'rb') as f:
#     data = f.readlines()
#
# data = map(lambda x: x.rstrip(), data)
# data_json_str = "[" + ','.join(data) + "]"
#
# data = json.loads(data_json_str)





# for doc in data:
#
#     score =  re.computeAccentuateScores(dn.normalize_data(doc), userPrefs)
#     if score>0:
#         print doc
#         print score

def getCategoryValueIndex(value, grouped_data, category):
    ind = -1
    if len(grouped_data[value][category])>0 and float(value) > 0:
        ind = random.randint(0,len(grouped_data[value][category])-1)
    return ind


def fromPhrase(phrase, gender):
    userPrefs = pp.exractPrefsFromPhrase(phrase, gender)
    return testFeed(userPrefs)


def createFeed(sorted_scores, grouped_data):
    topwears = []
    bottmwear = []
    footwear = []

    feed = []

    bmIndex = 0
    fwIndex = 0

    for score in sorted_scores:
        curTopwears = grouped_data[score][ls.Category.Topwear.value]
        curBottomwears = grouped_data[score][ls.Category.Bottomwear.value]
        curFootwears = grouped_data[score][ls.Category.Footwear.value]

        random.shuffle(curTopwears)
        random.shuffle(curBottomwears)
        random.shuffle(curFootwears)

        topwears.extend(curTopwears)
        bottmwear.extend(curBottomwears)
        footwear.extend(curFootwears)


    for i in range(0,(len(topwears))):
        feed.append(topwears[i])
        if i%2 == 0 and bmIndex < len(bottmwear):
            feed.append(bottmwear[bmIndex])
            bmIndex = bmIndex + 1

        if i%3 == 0 and fwIndex < len(footwear):
            feed.append(footwear[fwIndex])
            fwIndex = fwIndex + 1


    while (bmIndex < len(bottmwear)):
        feed.append(bottmwear[bmIndex])
        bmIndex = bmIndex + 1

        if bmIndex%3 == 0 and fwIndex < len(footwear):
            feed.append(footwear[fwIndex])
            fwIndex = fwIndex + 1


    if fwIndex < len(footwear):
        feed.extend(footwear[fwIndex:])

    return feed




def testFeed(userprefs):
    print userprefs

    accentuateWeight = .7
    colorWeight = .5
    skinToneWeight = .1
    scores = cdb.getFullData("looksmash_rules", "accentuate_women")[0]
    scores_men = cdb.getFullData("looksmash_rules", "accentuate_men")[0]
    hideScores = cdb.getFullData("looksmash_rules", "hide")[0]
    normalization = cdb.getFullData("looksmash_normalization", "normalization")[0]





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

    colors = userprefs['colors']
    types = userprefs['types']
    skinTone = userprefs['skinTone']
    domains = ["ShoppersStop"]

    if userprefs["gender"] == "Female":

        for bodyPart in userprefs["accentuate"]:
            bodyPrefs["accentuate"][bodyPart] = True

        for bodyPart in userprefs["hide"]:
            bodyPrefs["hide"][bodyPart] = True

        jabong_data =  cdb.getFullDataWithColorsAndTypesFromDomain("looksmash_db", "looksmash_women", domains, ru.getColorList(colors,skinTone), types)


    elif userprefs["gender"] == "Male":
         for bodyType in userprefs["bodyType"]:
            bodyPrefs["bodyType"][bodyType] = True

         jabong_data =  cdb.getFullDataWithColorsAndTypesFromDomain("looksmash_db", "looksmash_men", domains, ru.getColorList(colors,skinTone), types)





    scored_data = []
    grouped_data = {}
    for doc in jabong_data:
        #doc = dn.normalize_data(doc, normalization)
        accentuateScore, accentuateMsg = re.computeAccentuateScores(doc, bodyPrefs, scores) if userprefs["gender"] == "Female" else re.computeAccentuateScoresForMen(doc, bodyPrefs, scores_men)
        hideScore =  re.computeHideScores(doc, bodyPrefs, hideScores) if userprefs["gender"] == "Female" else 0
        colorScore, colorMsg = re.computeColorScores(doc, colors)
        skinToneScore, skinToneMsg = re.computeSkinToneScores(doc,skinTone,colors)

        print accentuateScore, hideScore, colorScore, skinToneScore

        doc['score'] = accentuateWeight*(accentuateScore + hideScore) + colorWeight*colorScore + skinToneWeight*skinToneScore
        doc['msg'] = me.getMsg(accentuateMsg + colorMsg + skinToneMsg)
        #print doc
        if doc['score'] not in grouped_data.keys():
            grouped_data[doc['score']] = {
                ls.Category.Topwear.value : [],
                ls.Category.Bottomwear.value : [],
                ls.Category.Footwear.value : []
            }

        del doc['_id']
        grouped_data[doc['score']][doc['Category']].append(doc)
        scored_data.append(doc)




    #json.dump(grouped_data, open("grouped.txt",'w'))
    sorted_keys = grouped_data.keys()
    sorted_keys.sort(reverse=True)

    feed = createFeed(sorted_keys, grouped_data)
    print feed

    images = {}
    i=0
    for product in feed:
        images[i]={"image" :product["Image"],
                   "msg" : product["msg"],
                   "url" : product["Url"],
                   "domain": product["Domain"],
                   "score": product["score"],
                   "Color": product["Color"],
                   "Sub_category": product["Sub_category"],
                   "Product Name": product["Product Name"],
                   "Cost": product["Cost"],
                   "Brand": product["Brand"],
                   "Category": product["Category"],
                   "Test": ""
                   }

        if "Neck" in product.keys():
            images[i]["Neck"] = product["Neck"],

        if "Sleeves" in product.keys():
            images[i]["Sleeves"] = product["Sleeves"]

        if "Pattern" in product.keys():
            images[i]["Pattern"] = product["Pattern"]


        i = i+1


    return {"result": json.dumps(images)}




def normalizeDB():
    women_data =  cdb.getFullData("looksmash_db", "looksmash_women")

    for doc in women_data:
        dn.normalize_data(doc)


    men_data =  cdb.getFullData("looksmash_db", "looksmash_men")
    for doc in men_data:
        dn.normalize_data(doc)

    return "done"


    #cdb.printColVals("Sub_category")

#
#
# with open('../DataFiles/snapdeal_data.json', 'rb') as f:
#     data = f.readlines()
#
# data = map(lambda x: x.rstrip(), data)
# data_json_str = "[" + ','.join(data) + "]"
#
# data = json.loads(data_json_str)
#
#
#
#
#
# scored_data = []
# for curDoc in data:
#
#         if curDoc['Sex'] != "Men":
#             doc = dn.normalize_data(curDoc)
#
#             doc['score'] = re.computeAccentuateScores(doc, userPrefs) + re.computeSkinToneScores(doc, "fair") + re.computeColorScores(doc, colors)
#             #print doc
#             scored_data.append(doc)
#
# sorted_data = sorted(scored_data, key=itemgetter('score'), reverse=True)
#
#
# top10 = itertools.islice(sorted_data, 10)
#
# print "Result"
#
# for doc in top10:
#     print doc
#     file = cStringIO.StringIO(urllib.urlopen(doc["Image"]).read())
#     img = Image.open(file)
#     img.show()