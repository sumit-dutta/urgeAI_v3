import IntelligenceLayer.RuleEngine.pairingEngine as pe
import RuleRepository.looksmashStandards as ls
import DatabaseLayer.converseWithDB as cdb

def getPairingRules():
    rules = cdb.getFullData("looksmash_rules", "pairing")[0]
    return rules


def pairProduct(record, gender):

    rules = getPairingRules()

    if ls.Attributes.Style.value in record.keys():
        pattern = record[ls.Attributes.Style.value]
    else:
        pattern = ""

    if record["Category"] == "Topwear":
        return pe.pairProductTopwear(gender, record[ls.Attributes.Color.value], pattern, record[ls.Attributes.Sub_Category.value], rules)

    if record["Category"] == ls.Category.Bottomwear.value:
        return pe.pairProductBottomwear(gender, record[ls.Attributes.Color.value], pattern, record[ls.Attributes.Sub_Category.value], rules)

    if record["Category"] == ls.Category.Footwear.value:
        return pe.pairProductFootwear(gender, record[ls.Attributes.Color.value], pattern, record[ls.Attributes.Sub_Category.value], rules)