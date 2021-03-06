import RuleRepository.looksmashStandards as ls
import DatabaseLayer.converseWithDB as cdb
import operator
import random

rules = cdb.getFullData("looksmash_rules", "pairing")[0]
domain = "Jabong"
singleBMs = ["Skirts"]

def getBucket(score):
    if score == 1 or score == .8:
        return 1
    if score == .6:
        return .6
    if score == .4 or score == .2:
        return .2

def createPairFeed(sorted_final):
    grouped_data = {}
    for pair in sorted_final:
        bucket = getBucket(pair["Score"])
        if bucket not in grouped_data.keys():
            grouped_data[bucket] = []

        grouped_data[bucket].append(pair)


    sorted_keys = grouped_data.keys()
    sorted_keys.sort(reverse=True)

    #print "==================>",sorted_keys

    pairFeed = []
    for score in sorted_keys:
        curPairs = grouped_data[score]

        random.shuffle(curPairs)

        pairFeed.extend(curPairs)

    return pairFeed

def getPatternScore(record1, record2, category, rule, pattern):
    if "Pattern" in record1.keys() and "Pattern" in record2.keys() and pattern != '':
        rules = rule[pattern]
        pattern1 = record1["Pattern"]
        pattern2 = record2["Pattern"]
        if category == ls.Category.Topwear.value:
            thatRule = [pr for pr in rules if pr[ls.Category.Bottomwear.value] == pattern1 and pr[ls.Category.Footwear.value] == pattern2]
            if len(thatRule) == 0:
                return 0
            else:
                return float(thatRule[0]["Score"])

        if category == ls.Category.Bottomwear.value:
            thatRule = [pr for pr in rules if pr[ls.Category.Topwear.value] == pattern1 and pr[ls.Category.Footwear.value] == pattern2]
            if len(thatRule) == 0:
                return 0
            else:
                return float(thatRule[0]["Score"])

        if category == ls.Category.Footwear.value:
            thatRule = [pr for pr in rules if pr[ls.Category.Topwear.value] == pattern1 and pr[ls.Category.Bottomwear.value] == pattern2]
            if len(thatRule) == 0:
                return 0
            else:
                return float(thatRule[0]["Score"])
    else:
        return 0





def pairProductTopwear(gender, color, pattern, sub_cat, rules):
    color_pairs = rules[gender][ls.Attributes.Color.value][ls.Category.Topwear.value][color]
    bm_colors = list(set([x[ls.Category.Bottomwear.value] for x in color_pairs]))
    fw_colors = list(set([x[ls.Category.Footwear.value] for x in color_pairs]))

    #print "gender",gender," sub cat",sub_cat
    subcat_pairs = rules[gender][ls.Attributes.Sub_Category.value][ls.Category.Topwear.value][sub_cat]
    bm_subCats = list(set([x[ls.Category.Bottomwear.value] for x in subcat_pairs]))
    fw_subCats = list(set([x[ls.Category.Footwear.value] for x in subcat_pairs]))

    #print "====================>"
    #print fw_subCats
    #print bm_subCats

    if gender == "Male":
        dbName = "looksmash_men"
    else:
        dbName = "looksmash_women"

    bottomwears = list(cdb.getFullDataWithColorsAndSubCategoryFromDomain("looksmash_db", dbName, [domain], bm_colors, bm_subCats))
    footwears = list(cdb.getFullDataWithColorsAndSubCategoryFromDomain("looksmash_db", dbName, [domain], fw_colors, fw_subCats))

    #print "footwear length", len(footwears)

    sorted_color_pairs = sorted(color_pairs, key=operator.itemgetter('Score'), reverse=True)
    sorted_subcat_pairs = sorted(subcat_pairs, key=operator.itemgetter('Score'), reverse=True)

    final = []


    #print sorted_color_pairs

    for color_pair in sorted_color_pairs:
        #print color_pair

        colored_bms = [bm for bm in bottomwears if color_pair['Bottomwear'] in bm['Color']]
        colored_fws = [fw for fw in footwears if color_pair['Footwear'] in fw['Color']]


        #print colored_bms
        #print colored_fws

        for subcat_pair in sorted_subcat_pairs:

            sl_bms = [bm for bm in colored_bms if bm['Sub_category'] == subcat_pair['Bottomwear']]
            sl_fws = [fw for fw in colored_fws if fw['Sub_category'] == subcat_pair['Footwear']]

            #print color_pair, subcat_pair
            #print len(sl_bms), len(sl_fws)



            for i in range(0, min(len(sl_bms), len(sl_fws))):
                value = {}
                print sl_bms[i]
                if '_id' in sl_bms[i].keys():
                    del sl_bms[i]['_id']
                if '_id' in sl_fws[i].keys():
                    del sl_fws[i]['_id']
               # print sl_bms[i]
               # print sl_fws[i]
                value["Bottomwear"] = sl_bms[i]
                value["Footwear"] = sl_fws[i]
                value["Score"] = (float(color_pair["Score"]) + float(subcat_pair["Score"]) + getPatternScore(sl_bms[i], sl_fws[i], gender, rules[gender]["Pattern"][ls.Category.Topwear.value], pattern))/3
                final.append(value)
                #print "entry", value



    #print final
    sorted_final = sorted(final, key=operator.itemgetter('Score'), reverse=True)
    return createPairFeed(sorted_final)




def pairProductBottomwear(gender, color, pattern, sub_cat, rules):
    color_pairs = rules[gender][ls.Attributes.Color.value][ls.Category.Bottomwear.value][color]
    tp_colors = list(set([x[ls.Category.Topwear.value] for x in color_pairs]))
    fw_colors = list(set([x[ls.Category.Footwear.value] for x in color_pairs]))


    subcat_pairs = rules[gender][ls.Attributes.Sub_Category.value][ls.Category.Bottomwear.value][sub_cat]
    tp_subCats = list(set([x[ls.Category.Topwear.value] for x in subcat_pairs]))
    fw_subCats = list(set([x[ls.Category.Footwear.value] for x in subcat_pairs]))

    if gender == "Male":
        dbName = "looksmash_men"
    else:
        dbName = "looksmash_women"

    topwears = list(cdb.getFullDataWithColorsAndSubCategoryFromDomain("looksmash_db", dbName, [domain], tp_colors, tp_subCats))
    footwears = list(cdb.getFullDataWithColorsAndSubCategoryFromDomain("looksmash_db", dbName, [domain], fw_colors, fw_subCats))

    sorted_color_pairs = sorted(color_pairs, key=operator.itemgetter('Score'), reverse=True)
    sorted_subcat_pairs = sorted(subcat_pairs, key=operator.itemgetter('Score'), reverse=True)

    final = []


    #print sorted_color_pairs

    for color_pair in sorted_color_pairs:
        #print color_pair

        colored_tps = [tp for tp in topwears if color_pair['Topwear'] in tp['Color']]
        colored_fws = [fw for fw in footwears if color_pair['Footwear'] in fw['Color']]




        for subcat_pair in sorted_subcat_pairs:

            sl_tps = [tp for tp in colored_tps if tp['Sub_category'] == subcat_pair['Topwear']]
            sl_fws = [fw for fw in colored_fws if fw['Sub_category'] == subcat_pair['Footwear']]

            #print color_pair, subcat_pair
            #print len(sl_tps), len(sl_fws)


            if sub_cat in singleBMs:
                for i in range(0, len(sl_fws)):
                    value = {}
                    if '_id' in sl_fws[i].keys():
                        del sl_fws[i]['_id']
                    value["Topwear"] = ""
                    value["Footwear"] = sl_fws[i]
                    value["Score"] = float(color_pair["Score"]) + float(subcat_pair["Score"])
                    final.append(value)
                    #print "entry", value
            else:
                for i in range(0, min(len(sl_tps), len(sl_fws))):
                    value = {}
                    if '_id' in sl_fws[i].keys():
                        del sl_fws[i]['_id']
                    if '_id' in sl_tps[i].keys():
                        del sl_tps[i]['_id']
                    value["Topwear"] = sl_tps[i]
                    value["Footwear"] = sl_fws[i]
                    value["Score"] = (float(color_pair["Score"]) + float(subcat_pair["Score"]) + getPatternScore(sl_tps[i], sl_fws[i], gender, rules[gender]["Pattern"][ls.Category.Bottomwear.value], pattern))/3
                    final.append(value)
                    #print "entry", value



    #print final
    sorted_final = sorted(final, key=operator.itemgetter('Score'), reverse=True)
    return createPairFeed(sorted_final)





def pairProductFootwear(gender, color, pattern, sub_cat, rules):
    color_pairs = rules[gender][ls.Attributes.Color.value][ls.Category.Footwear.value][color]
    bm_colors = list(set([x[ls.Category.Bottomwear.value] for x in color_pairs]))
    tp_colors = list(set([x[ls.Category.Topwear.value] for x in color_pairs]))


    subcat_pairs = rules[gender][ls.Attributes.Sub_Category.value][ls.Category.Footwear.value][sub_cat]
    bm_subCats = filter(None,list(set([x[ls.Category.Bottomwear.value] for x in subcat_pairs])))
    tp_subCats = filter(None,list(set([x[ls.Category.Topwear.value] for x in subcat_pairs])))

    #print bm_subCats
    #print tp_subCats

    if gender == "Male":
        dbName = "looksmash_men"
    else:
        dbName = "looksmash_women"

    bottomwears = list(cdb.getFullDataWithColorsAndSubCategoryFromDomain("looksmash_db", dbName, [domain], bm_colors, bm_subCats))
    topwears = list(cdb.getFullDataWithColorsAndSubCategoryFromDomain("looksmash_db", dbName, [domain], tp_colors, tp_subCats))



    sorted_color_pairs = sorted(color_pairs, key=operator.itemgetter('Score'), reverse=True)
    sorted_subcat_pairs = sorted(subcat_pairs, key=operator.itemgetter('Score'), reverse=True)

    final = []


    #print sorted_color_pairs

    for color_pair in sorted_color_pairs:
        #print color_pair

        colored_bms = [bm for bm in bottomwears if color_pair['Bottomwear'] in bm['Color']]
        colored_tps = [tp for tp in topwears if color_pair['Topwear'] in tp['Color']]


        #print colored_bms
        #print colored_fws

        for subcat_pair in sorted_subcat_pairs:

            sl_bms = [bm for bm in colored_bms if bm['Sub_category'] == subcat_pair['Bottomwear']]
            sl_tps = [tp for tp in colored_tps if tp['Sub_category'] == subcat_pair['Topwear']]

            #print color_pair, subcat_pair
            #print len(sl_bms), len(sl_tps)



            for i in range(0, min(len(sl_bms), len(sl_tps))):
                value = {}
                if '_id' in sl_bms[i].keys():
                    del sl_bms[i]['_id']
                if '_id' in sl_tps[i].keys():
                    del sl_tps[i]['_id']
                value["Bottomwear"] = sl_bms[i]
                value["Topwear"] = sl_tps[i]
                value["Score"] = (float(color_pair["Score"]) + float(subcat_pair["Score"]) + getPatternScore(sl_tps[i], sl_bms[i], gender, rules[gender]["Pattern"][ls.Category.Footwear.value], pattern))/3
                final.append(value)
                #print "entry", value



  #  print final
    sorted_final = sorted(final, key=operator.itemgetter('Score'), reverse=True)
    return createPairFeed(sorted_final)




#print pairProductTopwear("Male","Black","Geometric Print",ls.Sub_Category.Casual_Shirts.value,rules)