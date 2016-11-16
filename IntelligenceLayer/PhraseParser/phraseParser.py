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
            print phrases[i], standards[j].lower(), score
            if score >= 90:

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
    for i in range(0, len(attributes)):
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


synonyms = {
    "polos": ls.Sub_Category.Polo_T_shirts.value,
    "polo tee": ls.Sub_Category.Polo_T_shirts.value,
    "polo shirt": ls.Sub_Category.Polo_T_shirts.value,
    "polo collar tee": ls.Sub_Category.Polo_T_shirts.value,
    "polo collar shirt": ls.Sub_Category.Polo_T_shirts.value,
    "fitting dress": ls.Sub_Category.Bodycon_Dresses.value,
    "form fitting dress": ls.Sub_Category.Bodycon_Dresses.value,
    "figure hugging dress": ls.Sub_Category.Bodycon_Dresses.value,
    "tight dress": ls.Sub_Category.Bodycon_Dresses.value,
    "long dress": ls.Sub_Category.Maxis.value,
    "floor length dress": ls.Sub_Category.Maxis.value,
    "flowy dress": ls.Sub_Category.Maxis.value,
    "ankle length dress": ls.Sub_Category.Maxis.value,
    "beach dress": ls.Sub_Category.Maxis.value,
    "informal dress": ls.Sub_Category.Maxis.value,
    "tshirt": ls.Type.Tees.value,
    "tee-shirt": ls.Type.Tees.value,
    "tee shirt": ls.Type.Tees.value,
    "casual tee": ls.Type.Tees.value,
    "casual t": ls.Type.Tees.value,
    "sport shirt": ls.Type.Tees.value,
    "indigo": ls.Colors.Blue.value,
    "navy": ls.Colors.Blue.value,
    "cyan": ls.Colors.Blue.value,
    "bluish": ls.Colors.Blue.value,
    "fuchsia": ls.Colors.Pink.value,
    "pinkish" : ls.Colors.Pink.value,
    "mauve": ls.Colors.Purple.value,
    "violet": ls.Colors.Purple.value,
    "purplish": ls.Colors.Purple.value,
    "emerald": ls.Colors.Green.value,
    "pista": ls.Colors.Green.value,
    "lime": ls.Colors.Green.value,
    "pastel": ls.Colors.Green.value

}

def removeDependentPhrases(phrase, phrases):
    for i in range(0, len(phrases)):
        if fuzz.partial_ratio(phrase, phrases[i]) > 90:
            phrases[i] = ""

    return phrases


def replaceSynonyms(phrases):
    for i in range(0, len(phrases)):
        if phrases[i] in synonyms.keys():
            curPhrase = phrases[i]
            phrases = removeDependentPhrases(phrases[i], phrases)
            phrases[i] = synonyms[curPhrase].lower()

    return phrases




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
    print mappedAttributes.keys()
    if "Sub_category" in mappedAttributes.keys() and "Type" in mappedAttributes.keys():
        print "True"
        for category in mappedAttributes["Sub_category"]:
                print typeMappings[category]
                if typeMappings[category] in mappedAttributes["Type"]:
                    mappedAttributes["Type"] = [x for x in mappedAttributes["Type"] if x != typeMappings[category]]


    return mappedAttributes


def extractPrefsFromPhrase(phrase):

    mappedAttributes = {}
    standards = []
    colors = [e.value for e in ls.Colors]
    mappedAttributes = mapAttributes(colors, "Colors", mappedAttributes)
    types = [e.value for e in ls.Type]
    occasions = ["Everyday wear", "Regular wear", "Party"]

    subCategories = [e.value for e in ls.Sub_Category]
    mappedAttributes = mapAttributes(subCategories, "Sub_category", mappedAttributes)
    mappedAttributes = mapAttributes(types, "Type", mappedAttributes)
    mappedAttributes = mapAttributes(occasions, "Occasions", mappedAttributes)
    print "here",mappedAttributes

    typeNormalization = cdb.getFullData("looksmash_normalization", "normalization")[0]

    typeMappings = dn.unionDict(nr.types_dict, dn.formatDict(typeNormalization["Type"]))

    standards.extend(occasions)
    standards.extend(colors)
    standards.extend(types)
    standards.extend(subCategories)

    standards = sorted(standards, key=len, reverse=True)



    ltypes = createMapper(types)
    accentuate = ["arms", "bust", "legs", "waist"]
    hide = ["arms", "bust", "stomach", "hips and thighs"]

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


    thresholdMatches = thresholdPartialMatches(replaceSynonyms(phrases), standards)
    print thresholdMatches

    result = removeTypeDependency(getMappedAttributes(thresholdMatches, mappedAttributes), typeMappings)
    print "here",result
    return result




#extractPrefsFromPhrase("looking for red maxi dress and black sport shoes")




