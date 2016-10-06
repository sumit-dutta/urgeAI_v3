import DatabaseLayer.converseWithDB as cdb
import DatabaseLayer.converseWithStandards as cstd
import RuleRepository.looksmashStandards as ls
import RuleRepository.skinToneRules as sk
import DatabaseLayer.dataNormalization as dn
import random
import RuleRepository.normalizationRules as nr



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
test = cdb.getFullData("looksmash_rules", "pairing")[0]
# print test[0].keys()
print test["Female"]["Pattern"]

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