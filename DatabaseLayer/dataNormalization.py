import RuleRepository.normalizationRules as nr
import RuleRepository.looksmashStandards as ls
import DatabaseLayer.converseWithDB as cdb

def filter_string(string):
    string = string.replace(' ', '')
    string = string.title()
    return string


def formatDict(old_dict):
    dict = {}
    for k,v in old_dict.iteritems() :
        dict.update(dict.fromkeys(v, k))

    return dict

def unionDict(dict1, dict2):
    return dict(list(dict1.items()) + list(dict2.items()))


def normalize_color(document, colors_dict):
    c = []
    color = document['Color']
    if isinstance(color, list):
        for col in color:
            col = col.strip()
            new_color = color_replace(col, colors_dict, c)
            document['Color'] = new_color
    else:
        color = color.strip()
        new_color = color_replace(color, colors_dict, c)
        document['Color'] = new_color

    return document


def color_replace(color, colors_dict, c):
    new_color = ''
    if color in colors_dict:
        new_color = colors_dict[color]
    c.append(new_color)
    return c

def normalize_sleeve(document, sleeves_dict):
    sleeve = document['Sleeves'].strip()
    new_sleeve = sleeve_replace(sleeve, sleeves_dict)
    document['Sleeves'] = new_sleeve
    return document

def sleeve_replace(sleeve, sleeves_dict):
    new_sleeve = ''
    if sleeve in sleeves_dict:
        new_sleeve = sleeves_dict[sleeve]
    return new_sleeve

def normalize_neck(document, necks_dict):
    neck = document['Neck'].strip()
    new_neck = neck_replace(neck, necks_dict)
    document['Neck'] = new_neck
    return document

def neck_replace(neck, necks_dict):
    new_neck = ''
    if neck in necks_dict:
        new_neck = necks_dict[neck]
    return new_neck

def normalize_pattern(document, patterns_dict):
    pattern = document['Pattern'].strip()
    new_pattern = pattern_replace(pattern, patterns_dict)
    document['Pattern'] = new_pattern
    return document

def pattern_replace(pattern, patterns_dict):
    new_pattern = ''
    if pattern in patterns_dict.keys():
        new_pattern = patterns_dict[pattern]
    return new_pattern

def normalize_sub(document, sub_categories_dict):
    print document['Sub_category']
    sub = document['Sub_category'].strip()
    if ls.Attributes.Type.value in document.keys():
        typ = document['Type'].strip()
    else:
        typ = ''
    new_sub = sub_replace(sub, sub_categories_dict)
    new_type = sub_replace(typ, sub_categories_dict)
    if new_sub != '':
        document['Sub_category'] = new_sub
    else:
        document['Sub_category'] = new_type
    print document['Sub_category']
    return document

def sub_replace(sub, sub_categories_dict):
    new_sub = ''
    if sub in sub_categories_dict:
        new_sub = sub_categories_dict[sub]
    return new_sub

def normalize_type(document, type_dict):
    typ = document["Sub_category"].strip()
    print "subcat for type", typ
    new_type = type_replace(typ, type_dict)
    document['Type'] = new_type
    return document

def type_replace(typ, type_dict):
    new_type = ''
    if typ in type_dict.keys():
        new_type = type_dict[typ]
    return new_type


#document = {"_id":{"$oid":"56f3e92b6dbeae7a00842aa7"},"Category":"Topwear","Style":"","Neck":"Chinese Collar Combo Type","Fit":"","Url":"http://dl.flipkart.com/dl/azio-design-single-breasted-solid-men-s-suit/p/itme9cvztqjazsbf?pid=SUIE9CVZEGZGGH3N\u0026affid=affiliate278","Type":"","Sub_category":"Suits","Color":"Plum","Image":"http://img.fkcdn.com/image/suit/9/f/2/su-7127-azio-design-40-800x800-imae96wq4hwkzz8m.jpeg","Sex":"","Cost":5299.0,"Sleeves":"No","Product Name":"Azio Design Single Breasted Solid Men's Suit","Brand":"Azio Design","Size":"38"}



def normalize_data(document, normalization):

    print "---------------------------start---------------------------------"
    print document
    doc = document
    if 'Color' in document.keys():
        doc = normalize_color(doc, unionDict(nr.colors_dict,formatDict(normalization["Color"])))
    if 'Sleeves' in document.keys():
        doc = normalize_sleeve(doc, unionDict(nr.sleeves_dict, formatDict(normalization["Sleeves"])))
    if 'Neck' in document.keys():
        doc= normalize_neck(doc, unionDict(nr.necks_dict, formatDict(normalization["Neck"])))
    if 'Pattern' in document.keys():
        doc= normalize_pattern(doc, unionDict(nr.patterns_dict, formatDict(normalization["Pattern"])))
    if 'Sub_category' in document.keys():
        doc= normalize_sub(doc, unionDict(nr.sub_categories_dict, formatDict(normalization["Sub_category"])))
    if 'Type' in document.keys():
        doc= normalize_type(doc, unionDict(nr.types_dict, formatDict(normalization["Type"])))
    print doc
    print "----------------------------end------------------------------------"
    #cdb.replaceDocument("looksmash_db", "looksmash_women", doc)
    return doc






doc = {'Category': 'Topwear', 'Style': u'Casual', 'Sub_category': u'Tees and Polos', 'Fit': u'Slim', 'Color': u'Multicolour', 'Pattern': '', 'Image': u'http://3d978f8b966e64b0cfec-6729d756a2f36342416a9128f1759751.r41.cf3.rackcdn.com/1000004585418-Bspssm1602-Multicolor-Sunshine-Var1-1000004585418-Var1_01-517.jpg', 'Sex': 'Men', 'Url': 'http://www.landmarkshops.in//Men/Tops/Tees-and-Polos/MAX-MAX-Striped-Polo-T-Shirt/p/1000004585418-Bspssm1602-Multicolor-Sunshine-Var1', 'Length': '', 'Cost': u'499', 'Sleeves': u'Half Sleeve', 'Neck': '', 'Product Name': u'Striped Polo T-Shirt', 'Occasion': '', 'Size': [u'S', u'M', u'L', u'XL', u'XXL'], 'Type': u'Polo', 'Brand': u'MAX', 'Fabric': ''}




test = cdb.getFullData("looksmash_normalization", "normalization")[0]
print normalize_data(doc, test)