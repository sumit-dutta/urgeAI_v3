import nltk
from nltk.corpus import stopwords
from RuleRepository import looksmashStandards as ls
from stemming.porter2 import stem




def addStems(valueList):
    stems = []
    for value in valueList:
        stems.append(stem(value))


    return valueList + stems


def createMapper(valueList):

    mapperDict = {}
    for value in valueList:
        mappedTo = []
        mappedTo.append(value.lower())
        mappedTo.append(stem(value.lower()))
        mapperDict.update(dict.fromkeys(mappedTo,value))

    return mapperDict



colors = [e.value for e in ls.Colors]
lcolors = createMapper(colors)
types = [e.value for e in ls.Type]
ltypes = createMapper(types)
accentuate = ["arms", "bust", "legs", "waist"]
hide = ["arms", "bust", "stomach", "hips and thighs"]

def tokenizeImpWords(phrase):
    stop = set(stopwords.words('english'))
    words = [i for i in phrase.lower().split() if i not in stop]
    return words


def wordEntityMapping(word, map):

    if word.lower() in lcolors.keys():
        map["colors"].append(lcolors[word.lower()])


    if word.lower() in ltypes.keys():
        map["types"].append(ltypes[word.lower()])


    return map





def exractPrefsFromPhrase(phrase):
    mapper = {
        "colors": [],
        "types": [],
        "accentuate": [],
        "hide": [],
        "skinTone": ""

    }

    words = tokenizeImpWords(phrase)

    for word in words:
        wordEntityMapping(word, mapper)

    return mapper




