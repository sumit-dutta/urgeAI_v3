# import RuleRepository.accentuateRules as rp
# import RuleRepository.skinToneRules as sk
# #import RuleRepository.productPairingRules as pp
#
#
# hideParams = ["Sub_category", "Neck", "Sleeves", "Fit"]
#
# def getNormalizedScore(score):
#     if score > 1:
#         return 1
#     elif score < -1:
#         return -1
#     else:
#         return score
#
# def computeScore(record, rules, scores, preference, bodyPart):
#     score = 0
#     count = 0
#     for attr in rules[preference][bodyPart]:
#         if attr in record.keys() and record[attr] in scores[bodyPart].keys():
#             recordAttr = record[attr]
#             if isinstance(record[attr], list):
#                 recordAttr = record[attr][0]
#             print scores[bodyPart][recordAttr]
#             score = score + float(scores[bodyPart][recordAttr])
#             count = count + 1
#             #print attr, score
#
#     return getNormalizedScore(score)
#
#
#
# def computeAccentuateScoresForMen(record, userPrefs, scores, rules = rp.rules_men):
#
#     score  = 0
#     msg = ''
#     if userPrefs["bodyType"]["Oval"]:
#         curScore =  computeScore(record, rules, scores, "bodyType", "Oval")
#         if curScore > 0:
#             score = score + computeScore(record, rules, scores, "bodyType", "Oval")
#             msg = msg + 'AA'
#     if userPrefs["bodyType"]["Trapezoid"]:
#         curScore =  computeScore(record, rules, scores, "bodyType", "Trapezoid")
#         if curScore > 0:
#             score = score + computeScore(record, rules, scores, "bodyType", "Trapezoid")
#             msg = msg + 'AB'
#     if userPrefs["bodyType"]["Rectangle"]:
#         curScore =  computeScore(record, rules, scores, "bodyType", "Rectangle")
#         if curScore > 0:
#             score = score + computeScore(record, rules, scores, "bodyType", "Rectangle")
#             msg = msg + 'AL'
#
#
#     return score, msg
#
#
#
#
# def computeAccentuateScores(record, userPrefs, scores = rp.scores, rules = rp.rules,):
#
#     score  = 0
#     msg = ''
#     if userPrefs["accentuate"]["arms"]:
#          curScore =  computeScore(record, rules, scores, "accentuate", "arms")
#          if curScore > 0:
#             score = score + computeScore(record, rules, scores, "accentuate", "arms")
#             msg = msg + 'AA'
#
#     if userPrefs["accentuate"]["bust"]:
#          curScore =  computeScore(record, rules, scores, "accentuate", "bust")
#          if curScore > 0:
#             score = score + computeScore(record, rules, scores, "accentuate", "bust")
#             msg = msg + 'AB'
#     if userPrefs["accentuate"]["legs"]:
#          curScore =  computeScore(record, rules, scores, "accentuate", "legs")
#          if curScore > 0:
#             score = score + computeScore(record, rules, scores, "accentuate", "legs")
#             msg = msg + 'AL'
#     if userPrefs["accentuate"]["waist"]:
#          curScore = computeScore(record, rules, scores, "accentuate", "waist")
#          if curScore > 0:
#             score = score + computeScore(record, rules, scores, "accentuate", "waist")
#             msg = msg + 'AW'
#
#     return getNormalizedScore(score), msg
#
#
# def computeHideScores(record, userPrefs, scores = rp.scores):
#     print scores
#     score  = 0
#
#     if userPrefs["hide"]["arms"]:
#         score = score + computeHScore(record, scores, "hide", "arms")
#
#     if userPrefs["hide"]["bust"]:
#         score = score + computeHScore(record, scores, "hide", "bust")
#
#     if userPrefs["hide"]["hips and thighs"]:
#         score = score + computeHScore(record, scores, "hide", "hips and thighs")
#
#     if userPrefs["hide"]["stomach"]:
#         score = score + computeHScore(record, scores, "hide", "stomach")
#
#
#     return getNormalizedScore(score)
#
#
# def computeHScore(record, scores, ruleType, bodyPart):
#     #print record["Category"]
#     score = 0
#     count = 0
#     for attr in hideParams:
#         # print attr
#         # print record
#         # print scores[bodyPart].keys()
#         # print "----"
#         if attr in record.keys() and record[attr] in scores[bodyPart].keys():
#             print scores[bodyPart][record[attr]], record[attr]
#             score = score + float(scores[bodyPart][record[attr]])
#             count = count + 1
#             #print attr, score
#
#     return getNormalizedScore(score)
#
#
#
#
# def computeSkinToneScores(record, skinTone, colors, scores = sk.scores):
#     score = 0
#     count = 0
#     msg = ""
#     if skinTone != "":
#         for color in record["Color"]:
#             if color in diff(scores[skinTone].keys(), colors):
#                 score = score + scores[skinTone][color]
#                 count = count + 1
#                 msg = "SK"
#
#
#
#         return getNormalizedScore(score),msg
#     else:
#         return 0,""
#
#
#
# #old logic
# # score = score + scores[skinTone][color]
# # count = count + 1
# #
# # if count==0:
# #     count = count + 1
# # return score/count
#
#
#
# def computeColorScores(record, colors):
#     score = 0
#     count = 0
#     msg = ''
#     for color in colors:
#         if color in record["Color"]:
#             score = 1
#             msg = "C"
#
#     return score,msg
#
# def diff(first, second):
#     second = set(second)
#     return [item for item in first if item not in second]
#
# # def computeProductPairingColorScore(record1, record2):
# #     return pp.scores['Color'][record1['Category']][record2['Category']][record1['Color']][record2['Color']]
# #
# # def computeProductPairingTypeScore(record1, record2):
# #     print pp.scores['Type'][record1['Sex']]
# #     print pp.scores['Type'][record1['Sex']][record1['Category']][record2['Category']]
# #     return pp.scores['Type'][record1['Sex']][record1['Category']][record2['Category']][record1['Sub_category']][record2['Sub_category']]
# #
# # def computeProductPairingPatternScore(record1, record2):
# #     return pp.scores['Pattern'][record1['Category']][record2['Category']][record1['Pattern']][record2['Pattern']]
# #
# #
# #
# # def computeProductPairingScores(record1, record2):
# #     if record2['Category'] in pp.pairingCycle[record1['Category']]:
# #         return computeProductPairingColorScore(record1, record2) + computeProductPairingTypeScore(record1, record2) + computeProductPairingPatternScore(record1, record2)
# #
# #
# # record1 = {"_id":{"$oid":"570f30d704079a789d8b2d7c"},"Category":"Topwear","Pattern":"Checks","Neck":"COLLAR","Fit":"Slim","Url":"http://www.jabong.com/Wills-Lifestyle-Green-Casual-Shirt-770832.html?pos=2101","Type":"","Sub_category":"Casual Shirts","Color":"Green","Image":"http://static4.jassets.com/p/Wills-Lifestyle-Green-Casual-Shirt-5523-238077-1-pdp_slider_l.jpg","Sex":"Men","Cost":"1689","Sleeves":"Full Sleeves","Product Name":"Green Casual Shirt","Brand":"Wills Lifestyle","Size":["39","40","42","44"]}
# # record2 = {"_id":{"$oid":"570f30d704079a789d8b2d7c"},"Category":"Bottomwear","Pattern":"Solids","Neck":"COLLAR","Fit":"Slim","Url":"http://www.jabong.com/Wills-Lifestyle-Green-Casual-Shirt-770832.html?pos=2101","Type":"","Sub_category":"Jeans","Color":"Black","Image":"http://static4.jassets.com/p/Wills-Lifestyle-Green-Casual-Shirt-5523-238077-1-pdp_slider_l.jpg","Sex":"Men","Cost":"1689","Sleeves":"Full Sleeves","Product Name":"Green Casual Shirt","Brand":"Wills Lifestyle","Size":["39","40","42","44"]}
# #
# #
# # print computeProductPairingScores(record1, record2)
#
#
#
