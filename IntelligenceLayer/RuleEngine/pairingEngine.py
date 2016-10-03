import RuleRepository.looksmashStandards as ls
import DatabaseLayer.converseWithDB as cdb
import operator

rules = cdb.getFullData("looksmash_rules", "pairing")[0]

def pairProduct(gender, color, pattern, sub_cat, rules):
    color_pairs = rules[gender][ls.Attributes.Color.value][ls.Category.Topwear.value][color]
    bm_colors = list(set([x[ls.Category.Bottomwear.value] for x in color_pairs]))
    fw_colors = list(set([x[ls.Category.Footwear.value] for x in color_pairs]))


    subcat_pairs = rules[gender][ls.Attributes.Sub_Category.value][ls.Category.Topwear.value][sub_cat]
    bm_subCats = list(set([x[ls.Category.Bottomwear.value] for x in subcat_pairs]))
    fw_subCats = list(set([x[ls.Category.Footwear.value] for x in subcat_pairs]))

    bottomwears = list(cdb.getFullDataWithColorsAndSubCategoryFromDomain("looksmash_db", "looksmash_women", ["ShoppersStop"], bm_colors, bm_subCats))
    footwears = list(cdb.getFullDataWithColorsAndSubCategoryFromDomain("looksmash_db", "looksmash_women", ["ShoppersStop"], fw_colors, fw_subCats))

    sorted_color_pairs = sorted(color_pairs, key=operator.itemgetter('Score'), reverse=True)
    sorted_subcat_pairs = sorted(subcat_pairs, key=operator.itemgetter('Score'), reverse=True)

    final = []


    print sorted_color_pairs

    for color_pair in sorted_color_pairs:
        #print color_pair

        colored_bms = [bm for bm in bottomwears if color_pair['Bottomwear'] in bm['Color']]
        colored_fws = [fw for fw in footwears if color_pair['Footwear'] in fw['Color']]


        #print colored_bms
        #print colored_fws

        for subcat_pair in sorted_subcat_pairs:

            sl_bms = [bm for bm in colored_bms if bm['Sub_category'] == subcat_pair['Bottomwear']]
            sl_fws = [fw for fw in colored_fws if fw['Sub_category'] == subcat_pair['Footwear']]

            print color_pair, subcat_pair
            print len(sl_bms), len(sl_fws)



            for i in range(0, min(len(sl_bms), len(sl_fws))):
                value = {}
                value["Bottomwear"] = sl_bms[i]
                value["Footwear"] = sl_fws[i]
                value["Score"] = float(color_pair["Score"]) + float(subcat_pair["Score"])
                final.append(value)
                print "entry", value



    print final
    sorted_final = sorted(final, key=operator.itemgetter('Score'), reverse=True)
    for pair in sorted_final[:10]:
        print pair["Bottomwear"]["Image"]
        print pair["Footwear"]["Image"]
        print "----"



pairProduct("Female","White","",ls.Sub_Category.Anarkali.value,rules)