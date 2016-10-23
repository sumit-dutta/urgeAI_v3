
import RuleRepository.looksmashStandards as ls
import IntelligenceLayer.RuleEngine.ruleEngine as re
import DatabaseLayer.converseWithDB as cdb

def getRatings(record, userPrefs):
    ratings = {
        "overall": 0,
        "body type": 0,
        "skin tone": 0
    }
    skinTone, smsg = re.computeSkinToneScores(record, userPrefs["skinTone"], [])
    print type(skinTone)

    if record[ls.Attributes.Sex.value] == "Women":
        accentuate, amsg = re.computeAccentuateScores(record, userPrefs, cdb.getFullData("looksmash_rules", "accentuate_women")[0])
        hide = re.computeHideScores(record, userPrefs, cdb.getFullData("looksmash_rules", "hide")[0])
        bodyType = ( accentuate + hide )/2
        overall = (bodyType + skinTone)/2

        ratings["overall"] = overall
        ratings["body type"] = bodyType
        ratings["skin tone"] = skinTone

        return ratings

    elif record[ls.Attributes.Sex.value] == "Men":
        bodyType, msg = re.computeAccentuateScoresForMen(record, userPrefs, cdb.getFullData("looksmash_rules", "accentuate_men")[0])
        print type(bodyType)
        overall = (bodyType + skinTone)/2

        ratings["overall"] = overall
        ratings["body type"] = bodyType
        ratings["skin tone"] = skinTone

        return ratings
