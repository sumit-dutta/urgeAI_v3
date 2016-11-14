import nltk
from nltk.corpus import stopwords
from RuleRepository import looksmashStandards as ls
from stemming.porter2 import stem
from fuzzywuzzy import fuzz
from DatabaseLayer import converseWithDB as cdb
from RuleRepository import normalizationRules as nr
from DatabaseLayer import dataNormalization as dn




def addStems(valueList):
    stems = []
    for value in valueList:
        stems.append(stem(value))


    return valueList + stems


def getBivariates(tokens):
    bivariateTokens = []
    for i in range(0,len(tokens)-1):
        bivariateTokens.append(tokens[i] + " " + tokens[i+1])

    return bivariateTokens


def getTrivariates(tokens):
    trivariateTokens = []
    for i in range(0,len(tokens)-2):
        trivariateTokens.append(tokens[i] + " " + tokens[i+1] + " " + tokens[i+2])

    return trivariateTokens


def intersect(a, b):
    return list(set(a) & set(b))


def getDependentIndices(phrase, phrases):
    indices = []
    for i in range(0, len(phrases)):
        score = fuzz.partial_ratio(phrase.lower(), phrases[i].lower())
        #print phrase, phrases[i], score
        if score >= 90:
            indices.append(i)

    return indices


def thresholdPartialMatches(phrases, standards):
    print phrases
    print standards
    partialMatches = []
    for i in range(0, len(phrases)):
        for j in range(0, len(standards)):
            #print phrases
            score = fuzz.partial_ratio(phrases[i], standards[j].lower())
            if score >= 80:
                partialMatches.append(standards[j])


                curPhrase = phrases[i].split()
                if len(curPhrase) > 1:
                    indices = getDependentIndices(standards[j], phrases)
                    print "Found ", phrases[i]
                    for index in indices:
                        print "Removing->",index, phrases[index] , " by ", standards[j]
                        phrases[index] = ""


                standards[j] = ""


    return partialMatches


def createMapper(valueList):

    mapperDict = {}
    for value in valueList:
        mappedTo = []
        mappedTo.append(value.lower())
        mappedTo.append(stem(value.lower()))
        mapperDict.update(dict.fromkeys(mappedTo,value))

    return mapperDict

def mapAttributes(attributes, attributeName, mappedAttributes):
    for i in range(0, len(attributes)-1):
        mappedAttributes[attributes[i]] = attributeName

    return mappedAttributes


def getMappedAttributes(attributes, mapper):
    mapped = {}
    for attribute in attributes:
        print attribute
        key = mapper[attribute]
        if key not in mapped.keys():
            mapped[key] = []

        mapped[key].append(attribute)

    return mapped



mappedAttributes = {}
standards = []
colors = [e.value for e in ls.Colors]
mappedAttributes = mapAttributes(colors, "Colors", mappedAttributes)
types = [e.value for e in ls.Type]

subCategories = [e.value for e in ls.Sub_Category]
mappedAttributes = mapAttributes(subCategories, "Sub_Category", mappedAttributes)
mappedAttributes = mapAttributes(types, "Type", mappedAttributes)

typeNormalization = cdb.getFullData("looksmash_normalization", "normalization")[0]

typeMappings = dn.unionDict(nr.types_dict, dn.formatDict(typeNormalization["Type"]))

standards.extend(colors)
standards.extend(types)
standards.extend(subCategories)


ltypes = createMapper(types)
accentuate = ["arms", "bust", "legs", "waist"]
hide = ["arms", "bust", "stomach", "hips and thighs"]

def tokenizeImpWords(phrase):
    stop = set(stopwords.words('english'))
    words = [i for i in phrase.lower().split() if i not in stop]
    return words



# def wordEntityMapping(word, map):
#
#     if word.lower() in lcolors.keys():
#         map["colors"].append(lcolors[word.lower()])
#
#
#     if word.lower() in ltypes.keys():
#         map["types"].append(ltypes[word.lower()])
#
#
#     print ltypes
#     return map



def removeTypeDependency(mappedAttributes, typeMappings):
    if "Sub_Category" in mappedAttributes.keys() and "Type" in mappedAttributes.keys():
        for category in mappedAttributes["Sub_Category"]:
                if typeMappings[category] in mappedAttributes["Type"]:
                    mappedAttributes["Type"] = [x for x in mappedAttributes["Type"] if x != typeMappings[category]]


    return mappedAttributes


def extractPrefsFromPhrase(phrase):
    mapper = {
        "colors": [],
        "types": [],
        "accentuate": [],
        "hide": [],
        "skinTone": "",
        "bodyType": []

    }

    words = tokenizeImpWords(phrase)
    phrases = []

    phrases.extend(getTrivariates(words))
    phrases.extend(getBivariates(words))
    phrases.extend(words)


    thresholdMatches = thresholdPartialMatches(phrases, standards)
    print thresholdMatches

    result = removeTypeDependency(getMappedAttributes(thresholdMatches, mappedAttributes), typeMappings)
    print result
    return result




#extractPrefsFromPhrase("looking for red maxi dress and black sport shoes")




