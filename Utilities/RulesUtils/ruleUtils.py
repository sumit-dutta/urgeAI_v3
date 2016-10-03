import RuleRepository.skinToneRules as sk


def getColorList(userPrefs, skintone, skinToneRules=sk.scores):
    if skintone != "":
        print userPrefs+skinToneRules[skintone].keys()
        return userPrefs+skinToneRules[skintone].keys()
    else:
        return userPrefs
