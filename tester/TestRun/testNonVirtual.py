import DatabaseLayer.converseWithDB as cdb
import DatabaseLayer.converseWithStandards as cstd
import RuleRepository.looksmashStandards as ls
import RuleRepository.skinToneRules as sk
import DatabaseLayer.dataNormalization as dn
import random
import RuleRepository.normalizationRules as nr
import Services.RatingService as rs
import IntelligenceLayer.PhraseParser.phraseParser as pp



#print cdb.getColumnValuesForDomain("looksmash_db", "looksmash_women","Type", "Jabong")
#
# cdb.renameFieldInDocument("looksmash_rules", "rules", "arms.3/4 sleeves", "arms.3/4th Sleeves")
#
# test = cdb.getColumnValues("looksmash_db","amazon_data", "Sub_category")
# print test
#
# looksmash_normals = nr.sub_categories_dict.keys()
# print looksmash_normals
#
# outliers = []
# for subCat in test:
#
#     print subCat
#     if subCat not in looksmash_normals:
#         outliers.append(subCat)
#
#
# print outliers
# print random.randint(0,0
#
# test = cdb.getGenderDataFromDomainWithCategory("looksmash_db", "looksmash_men", "Men", "ShoppersStop", "Footwear")
# # print test[0].keys()
#
# for doc in test:
#     print doc["Sub_category"], "->",doc["Product Name"]



# test = cdb.getFullDataWithColorsAndTypesFromDomain("looksmash_db", "looksmash_women",["ShoppersStop", "Jabong"], [], [])
#
# for doc in test:
#     print doc

pp.exractPrefsFromPhrase("black shoes", "Female")


# doc = { "Category" : "Footwear", "Url" : "https://www.shoppersstop.com/life-womens-casual-ankle-buckle-closure-heel-sandal/p-200835034", "Upper Material" : "Synthetic leather", "Occasion" : "", "Type" : "", "Sub_category" : "Heels", "Color" : "Beige", "Image" : "https://sslimages5.shoppersstop.com/sys-master/images/h54/h2c/9282154922014/200835034_9111.png_1088Wx1632H?output-format=jpg&background-color=f8f8f8", "Sex" : "Women", "Cost" : "1499", "Product Name" : "Womens Casual Ankle Buckle Closure Heel Sandal", "Brand" : "LIFE", "Size" : [ "5.5", "6.0", "6.5", "7.5", "8.5" ] }
# userpref = {
#     "accentuate": {
#         "arms": False,
#         "bust": False,
#         "waist": False,
#         "legs" : True
#     },
#
#     "bodyType": {
#         "Oval": False,
#         "Trapezoid": False,
#         "Rectangle": False
#     },
#
#     "hide": {
#         "arms": False,
#         "bust": False,
#         "stomach": False,
#         "hips and thighs": False
#     },
#
#     "skinTone" : "fair"
# }
#
# print rs.getRatings(doc, userpref)

# t = ["one", "two", "three", "four", "five"]
#
# random.shuffle(t)
#
# print t

# t = {
#     "ek": ["one", "ik", "vaaan"],
#     "do": ["two", "dui", "don"]
# }
#
# dict = {}
# for k,v in t.iteritems() :
#     print k,v
#     dict.update(dict.fromkeys(v, k))
#
#
# print dict


#
# sub_categories_dict = dict.fromkeys(['a', 'b'], ls.Sub_Category.Sport_Shoes.value)
# print sub_categories_dict
# del group[1][1]
# print group
#
# cdb.getSchemaDetails("looksmash_db", "looksmash_women")

# shorts_data = cdb.getSubCategoryDataFromDomain("looksmash_db", "looksmash_women", "Jabong",ls.Sub_Category.Shorts.value, ls.Sub_Category.Beach_Shorts.value, ls.Sub_Category.Chino_Shorts.value, ls.Sub_Category.Three_Fourth_Shorts.value)
#
# for doc in shorts_data:
#     doc = dn.normalize_data(doc)
#     cdb.replaceDocument("looksmash_db", "looksmash_women", doc)