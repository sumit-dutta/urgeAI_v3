
import RuleRepository.looksmashStandards as ls
import IntelligenceLayer.RuleEngine.ruleEngine as re
import DatabaseLayer.converseWithDB as cdb
import random

high = ["Wow! This will look great on you.",
    "The perfect product to complement your style.",
    "Put your most stylish foot forward with this product.",
    "You have a good eye for style.",
    "Nice! You know how to pick em'.",
    "Looks like you have your personal style all figured out.",
    "You're going to make all the right moves in this product."
    "We love this product for you!",
    "Oh! You're going to look smooth in this." ]

medium = ["Good choice, you sure have style.",
    "The perfect product to complement your style.",
    "Put your most stylish foot forward with this product.",
    "A good piece to add to your wardrobe.",
    "This choice has great fashion potential",
    "You can mix and match this with ease.",
    "You're going to look great in this.",
    "You have the perfect product now to find an occasion."]

low = ["Find something that will match your style.",
    "Try a different product, maybe?",
    "A different product might be better suited for you.",
    "Try something in a different colour.",
    "Perfect clothes are hard to find sometimes.",
    "Hmm.. looks like this isn't the one.",
    "This might not be the best choice for you.",
    "Oh no! Try another product, it might be a better match to your style."   ]


def getMessage(list):
    index = random.randint(0,len(list) - 1)
    return list[index]



def getRatingMessage(score):
    message = ""
    if score >= .65:
        message = getMessage(high)

    if score >= .4 and score < .65:
        message = getMessage(medium)

    if score < .4:
        message = getMessage(low)

    return message





def getRatings(record, userPrefs):
    ratings = {
        "overall": 0,
        "body type": 0,
        "skin tone": 0,
        "message": ""
    }
    skinTone, smsg = re.computeSkinToneScores(record, userPrefs["skinTone"], [])
    print type(skinTone)

    if record[ls.Attributes.Sex.value] == "Women":
        accentuate, amsg = re.computeAccentuateScores(record, userPrefs, cdb.getFullData("looksmash_rules", "accentuate_women")[0])
        hide = re.computeHideScores(record, userPrefs, cdb.getFullData("looksmash_rules", "hide")[0])
        print "A", accentuate
        print "H", hide
        bodyType = 0.6 *accentuate + 0.4*hide
        overall =  max(.3,float(bodyType + skinTone)/2)
        message = getRatingMessage(overall)

        ratings["overall"] = overall
        ratings["body type"] = bodyType
        ratings["skin tone"] = skinTone
        ratings["message"] = message

        return ratings

    elif record[ls.Attributes.Sex.value] == "Men":
        bodyType, msg = re.computeAccentuateScoresForMen(record, userPrefs, cdb.getFullData("looksmash_rules", "accentuate_men")[0])
        print type(bodyType)
        overall = max(.3,float(bodyType + skinTone)/2)
        message = getRatingMessage(overall)

        ratings["overall"] = overall
        ratings["body type"] = bodyType
        ratings["skin tone"] = skinTone
        ratings["message"] = message

        return ratings
