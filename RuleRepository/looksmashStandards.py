# from enum import Enum
#
# def enum(**enums):
#     return type('Enum', (), enums)
#
#
# class Attributes(Enum):
#     Category='Category'
#     Style='Style'
#     Neck='Neck'
#     Fit='Fit'
#     Url='Url'
#     Type='Type'
#     Sub_Category='Sub_category'
#     Color='Color'
#     Image='Image'
#     Sex='Sex'
#     Cost='Cost'
#     Sleeves='Sleeves'
#     Product_Name='Product Name'
#     Brand='Brand'
#     Size='Size'
#
#
# class Colors (Enum):
#     Blue ='Blue'
#     Grey = 'Grey'
#     Black = 'Black'
#     Navy_Blue = 'Navy Blue'
#     White = 'White'
#     Red = 'Red'
#     Green = 'Green'
#     Multicolor = 'Multicolor'
#     Yellow = 'Yellow'
#     Brown = 'Brown'
#     Maroon = 'Maroon'
#     Pink = 'Pink'
#     Purple = 'Purple'
#     Beige = 'Beige'
#     Orange = 'Orange'
#     Cream = 'Cream'
#     Olive  = 'Olive'
#     Khaki  = 'Khaki'
#     Coffee = 'Coffee'
#     Peach = 'Peach'
#     Silver = 'Silver'
#     Golden = 'Golden'
#     Tan = 'Tan'
#     Magenta = 'Magenta'
#     Turquoise = 'Turquoise'
#     Copper = 'Copper'
#     Mauve = 'Mauve'
#     Mustard = 'Mustard'
#     Nude = 'Nude'
#     Scarlet = 'Scarlet'
#     Plum = 'Plum'
#     Emerald_Green = 'Emerald Green'
#     Lime_Green = 'Lime Green'
#     Indigo = 'Indigo'
#
#
#
#
# class Category(Enum):
#     Topwear='Topwear'
#     Bottomwear='Bottomwear'
#     Footwear='Footwear'
#
#
# class Gender(Enum):
#     Men='Men'
#     Women='Women'
#
#
# class Sleeves(Enum):
#     Sleeveless='Sleeveless'
#     Cap_Sleeves='Cap Sleeves'
#     Full_Sleeves='Full Sleeves'
#     Roll_Up_Sleeves='Roll Up Sleeves'
#     Puff_Sleeves='Puff Sleeves'
#     Three_Fourth_Sleeves='3/4th Sleeves'
#     Short_Sleeves='Short Sleeves'
#     Half_Sleeves='Half Sleeves'
#     Flutter_Sleeves='Flutter Sleeves'
#
#
# class Neck(Enum):
#     Mandarin_Collar='Mandarin Collar'
#     Round_Neck='Round Neck'
#     Halter_Neck='Halter Neck'
#     V_Neck='V Neck'
#     Nehru_Collar='Nehru Collar'
#     Boat_Neck='Boat Neck'
#     Henley='Henley'
#     Polo_Neck='Polo Neck'
#     Spaghetti_Neck='Spaghetti Neck'
#     Sweetheart_Neck='Sweetheart Neck'
#     Peterpan_Collar_Combo='Peterpan Collar Combo'
#     Square_Neck='Square Neck'
#     Regular_Collar='Regular Collar'
#     Turtle_Neck='Turtle Neck'
#
#
#
#
# class Pattern(Enum):
#     Solids='Solids'
#     Florals='Florals'
#     Stripes='Stripes'
#     Checks='Checks'
#     Embroidered='Embroidered'
#     Graphic_Print='Graphic Print'
#     Printed='Printed'
#     Embellished='Embellished'
#     Acid_Wash='Acid Wash'
#     Geometric_Print='Geometric Print'
#
#
# class Type(Enum):
#     Dresses='Dresses'
#     Tops='Tops'
#     Tees='Tees'
#     Jackets='Jackets'
#     Blazers='Blazers'
#     Kurtas='Kurtas'
#     Blouses='Blouses'
#     Polo_T_Shirts='Polo T-Shirts'
#     Tunics='Tunics'
#     Shirts='Shirts'
#     Waistcoats='Waistcoats'
#     Trousers='Trousers'
#     Shorts='Shorts'
#     Jeans='Jeans'
#     Ethnic_Bottomwear='Ethnic Bottomwear'
#     Skirts='Skirts'
#     Palazzos_And_Pants='Palazzos And Pants'
#     Gym_Wear='Gym Wear'
#     Sports_Shoes='Sports Shoes'
#     Casual_Shoes='Casual Shoes'
#     Flats='Flats'
#     Formal_Shoes='Formal Shoes'
#     Boots='Boots'
#
#
# class Sub_Category(Enum):
#     Maxis='Maxis'
#     Midis='Midis'
#     Off_Shoulder_Dresses='Off Shoulder Dresses'
#     Bodycon_Dresses='Bodycon Dresses'
#     Asymmetric_Dresses='Asymmetric Dresses'
#     Peplum_Dresses='Peplum Dresses'
#     Skater_Dresses='Skater Dresses'
#     Shift_Dresses='Shift Dresses'
#     A_Line_Dresses='A-Line Dresses'
#     Dresses='Dresses'
#     Jumpsuit='Jumpsuit'
#     Crop_Tops='Crop Tops'
#     Tube_Tops='Tube Tops'
#     Tank_Tops='Tank Tops'
#     Strappy_Tops='Strappy Tops'
#     Tops='Tops'
#     Round_Neck_Tees='Round Neck Tees'
#     Turtle_Neck_Tees='Turtle Neck Tees'
#     Tees='Tees'
#     V_Neck_Tees='V-Neck Tees'
#     Sports_Jerseys='Sports Jerseys'
#     Henley_Tees='Henley Tees'
#     Mandarin_Neck_Tees='Mandarin Neck Tees'
#     Hooded_T_Shirts='Hooded T-Shirts'
#     Polo_T_shirts='Polo T-shirts'
#     Jackets='Jackets'
#     Hooded_Jackets='Hooded Jackets'
#     Bomber_Jackets='Bomber Jackets'
#     Leather_Jackets='Leather Jackets'
#     Quilted_Jackets='Quilted Jackets'
#     Winter_Jackets='Winter Jackets'
#     Single_Breasted_Blazers='Single Breasted Blazers'
#     Blazers='Blazers'
#     Tuxedo_Style_Blazer='Tuxedo Style Blazer'
#     Double_Breasted_Blazers='Double Breasted Blazers'
#     Fitted_Blazers='Fitted Blazers'
#     Casual_Blazer='Casual Blazer'
#     Nehru_Jackets='Nehru Jackets'
#     Anarkali_Suit_Unstitched='Anarkali Suit (Unstitched)'
#     A_Line='A-Line'
#     Straight_Suit='Straight Suit'
#     Anarkali='Anarkali'
#     Flared='Flared'
#     Kurtis='Kurtis'
#     Kurta_With_Side_Slits='Kurta With Side Slits'
#     Anarkali_Gown='Anarkali Gown'
#     Pakistani_Suits='Pakistani Suits'
#     Designer_Suit='Designer Suit'
#     Pathani='Pathani'
#     Ethnic_Jackets='Ethnic Jackets'
#     Kurtas='Kurtas'
#     Kurti_Fabric='Kurti Fabric'
#     Ethnic_Wear='Ethnic Wear'
#     Checked_Shirts='Checked Shirts'
#     Shirts='Shirts'
#     Casual_Shirts='Casual Shirts'
#     Formal_Shirts='Formal Shirts'
#     Shirts_Blouses='Shirts & Blouses'
#     Tunics='Tunics'
#     Waistcoats='Waistcoats'
#     Formal_Waistcoat='Formal Waistcoat'
#     Trousers='Trousers'
#     Formal_Trousers='Formal Trousers'
#     Chinos='Chinos'
#     Flat_Front_Trousers='Flat-Front Trousers'
#     Corduroy_Trousers='Corduroy Trousers'
#     Cotton_Trousers='Cotton Trousers'
#     Coloured_Pants='Coloured Pants'
#     Cargo_Pants='Cargo Pants'
#     Khakis='Khakis'
#     Chino_Shorts='Chino Shorts'
#     Beach_Shorts='Beach Shorts'
#     Three_Fourth_Shorts='3/4th Shorts'
#     Shorts='Shorts'
#     Jeggings='Jeggings'
#     Jeans='Jeans'
#     Salwars_Churidhars='Salwars & Churidhars'
#     Dhoti_Pants='Dhoti Pants'
#     Patialas='Patialas'
#     Leggings='Leggings'
#     Regular_Salwars='Regular Salwars'
#     Salwars='Salwars'
#     Patiala_Leggings='Patiala and Leggings'
#     Churidar='Churidar'
#     Dhoti='Dhoti'
#     Pencil_Skirt='Pencil Skirt'
#     A_line_Skirt='A-line Skirt'
#     Skirts='Skirts'
#     Palazzos='Palazzos'
#     Harem_Pants='Harem Pants'
#     Wrap_Palazzo_Pants='Wrap Palazzo Pants'
#     Sweat_Pants='Sweat Pants'
#     Joggers='Joggers'
#     Sports_Shoes='Sports Shoes'
#     Sneakers='Sneakers'
#     Running_Shoes='Running Shoes'
#     Walking_shoes='Walking shoes'
#     Sport_Shoes='Sport Shoes'
#     Cricket_Shoes='Cricket Shoes'
#     Badminton_Shoes='Badminton Shoes'
#     Skateboarding_Shoes='Skateboarding Shoes'
#     Indoor_Sports_Shoes='Indoor Sports Shoes'
#     Tennis_Shoes='Tennis Shoes'
#     Hiking_Shoes='Hiking Shoes'
#     Sporty_Sneakers='Sporty Sneakers'
#     Football_Shoes='Football Shoes'
#     Outdoor_Hiking_Shoes='Outdoor & Hiking Shoes'
#     Basketball_Shoes='Basketball Shoes'
#     Training_Shoes='Training Shoes'
#     Casual_Shoes='Casual Shoes'
#     Lifestyle_Shoes='Lifestyle Shoes'
#     Boat_Shoes='Boat Shoes'
#     Brogues='Brogues'
#     Canvas_Shoes='Canvas Shoes'
#     Moccasins='Moccasins'
#     Mules='Mules'
#     Casual_Sneakers='Casual Sneakers'
#     Loafers='Loafers'
#     Floaters='Floaters'
#     Sandals='Sandals'
#     Slip_On='Slip-On'
#     Flats='Flats'
#     Ballet_Flats='Ballet Flats'
#     Formal_Shoes='Formal Shoes'
#     Boots='Boots'
#     Ankle_Length_Boots='Ankle Length Boots'
#     Chelsea_Boots='Chelsea Boots'
#     Cowboy_Boots='Cowboy Boots'
#     Ugg_Boots='Ugg Boots'
#     Slouch_Boots='Slouch Boots'
#     Combat_Boots='Combat Boots'
#
#
#
#
#
# # allColors = [e.value for e in Colors]
# #
# # print allColors
#
