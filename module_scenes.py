from header_common import *
from header_operations import *
from header_triggers import *
from header_scenes import *
from module_constants import *

####################################################################################################################
#  Each scene record contains the following fields:
#  1) Scene id {string}: used for referencing scenes in other files. The prefix scn_ is automatically added before each scene-id.
#  2) Scene flags {int}. See header_scenes.py for a list of available flags
#  3) Mesh name {string}: This is used for indoor scenes only. Use the keyword "none" for outdoor scenes.
#  4) Body name {string}: This is used for indoor scenes only. Use the keyword "none" for outdoor scenes.
#  5) Min-pos {(float,float)}: minimum (x,y) coordinate. Player can't move beyond this limit.
#  6) Max-pos {(float,float)}: maximum (x,y) coordinate. Player can't move beyond this limit.
#  7) Water-level {float}. 
#  8) Terrain code {string}: You can obtain the terrain code by copying it from the terrain generator screen
#  9) List of other scenes accessible from this scene {list of strings}.
#     (deprecated. This will probably be removed in future versions of the module system)
#     (In the new system passages are used to travel between scenes and
#     the passage's variation-no is used to select the game menu item that the passage leads to.)
# 10) List of chest-troops used in this scene {list of strings}. You can access chests by placing them in edit mode.
#     The chest's variation-no is used with this list for selecting which troop's inventory it will access.
#  town_1   Sargoth     #plain
#  town_2   Tihr        #steppe
#  town_3   Veluca      #steppe
#  town_4   Suno        #plain
#  town_5   Jelkala     #plain
#  town_6   Praven      #plain
#  town_7   Uxkhal      #plain
#  town_8   Reyvadin    #plain
#  town_9   Khudan      #snow
#  town_10  Tulga       #steppe
#  town_11  Curaw       #snow
#  town_12  Wercheg     #plain
#  town_13  Rivacheg    #plain
#  town_14  Halmar      #steppe
#  town_15  Yalen
#  town_16  Dhirim
#  town_17  Ichamur
#  town_18  Narra
#  town_19  Shariz
#  town_20  Durquba
#  town_21  Ahmerrad
#  town_22  Bariyye
####################################################################################################################

scenes = [
	("random_scene", sf_generate|sf_randomize|sf_auto_entry_points, "none", "none", (0.00, 0.00), (240.00, 240.00), -0.5, "0x300028000003e8fa0000034e00004b34000059be", [], []),

	("conversation_scene", 0, "encounter_spot", "bo_encounter_spot", (-40.00, -40.00), (40.00, 40.00), -100.0, "0", [], []),

	("water", 0, "none", "none", (-1000.00, -1000.00), (1000.00, 1000.00), -0.5, "0", [], []),

	("random_scene_steppe", sf_generate|sf_randomize|sf_auto_entry_points, "none", "none", (0.00, 0.00), (240.00, 240.00), -0.5, "0x00000000222005000005e57900004e47000058cc000039bd", [], [], "outer_terrain_steppe_rnd"),

	("random_scene_plain", sf_generate|sf_randomize|sf_auto_entry_points, "none", "none", (0.00, 0.00), (240.00, 240.00), -0.5, "0x00000000322005000005e57900004e47000058cc000039bd", [], [], "outer_terrain_plain_rnd"),

	("random_scene_snow", sf_generate|sf_randomize|sf_auto_entry_points, "none", "none", (0.00, 0.00), (240.00, 240.00), -0.5, "0x0000000229602800000691a400003efe00004b34000059be", [], [], "outer_terrain_snow_rnd"),

	("random_scene_desert", sf_generate|sf_randomize|sf_auto_entry_points, "none", "none", (0.00, 0.00), (240.00, 240.00), -0.5, "0x00000000522005000005e57900004e47000058cc000039bd", [], [], "outer_terrain_desert_rnd"),

	("random_scene_steppe_forest", sf_generate|sf_randomize|sf_auto_entry_points, "none", "none", (0.00, 0.00), (240.00, 240.00), -0.5, "0x00000000a5a005000005e57900004e47000058cc000039bd", [], [], "outer_terrain_steppe_rnd"),

	("random_scene_plain_forest", sf_generate|sf_randomize|sf_auto_entry_points, "none", "none", (0.00, 0.00), (240.00, 240.00), -0.5, "0x0000000038e0050000061d7900004e47000058cc000039bd", [], [], "outer_terrain_plain_rnd"),

	("random_scene_snow_forest", sf_generate|sf_randomize|sf_auto_entry_points, "none", "none", (0.00, 0.00), (240.00, 240.00), -0.5, "0x300028000003e8fa0000034e00004b34000059be", [], [], "outer_terrain_snow"),

	("random_scene_desert_forest", sf_generate|sf_randomize|sf_auto_entry_points, "none", "none", (0.00, 0.00), (240.00, 240.00), -0.5, "0x00000000dc60050000061d7900004e47000058cc000039bd", [], [], "outer_terrain_desert_rnd"),

	("camp_scene", sf_generate|sf_auto_entry_points, "none", "none", (0.00, 0.00), (240.00, 240.00), -0.5, "0x300028000003e8fa0000034e00004b34000059be", [], [], "outer_terrain_plain"),

	("camp_scene_horse_track", sf_generate|sf_auto_entry_points, "none", "none", (0.00, 0.00), (240.00, 240.00), -0.5, "0x300028000003e8fa0000034e00004b34000059be", [], [], "outer_terrain_plain"),

	("four_ways_inn", sf_generate, "none", "none", (0.00, 0.00), (120.00, 120.00), -100.0, "0x0000000030015f2b000350d4000011a4000017ee000054af", [], [], "outer_terrain_thir_new"),

	("test_scene", sf_generate, "none", "none", (0.00, 0.00), (120.00, 120.00), -100.0, "0x0230817a00028ca300007f4a0000479400161992", [], [], "outer_terrain_plain"),

	("quick_battle_1", sf_generate, "none", "none", (0.00, 0.00), (120.00, 120.00), -100.0, "0x30401ee300059966000001bf0000299a0000638f", [], [], "outer_terrain_plain"),

	("quick_battle_2", sf_generate, "none", "none", (0.00, 0.00), (120.00, 120.00), -100.0, "0xa0425ccf0004a92a000063d600005a8a00003d9a", [], [], "outer_terrain_steppe"),

	("quick_battle_3", sf_generate, "none", "none", (0.00, 0.00), (120.00, 120.00), -100.0, "0x4c6024e3000691a400001b7c0000591500007b52", [], [], "outer_terrain_snow"),

	("quick_battle_4", sf_generate, "none", "none", (0.00, 0.00), (120.00, 120.00), -100.0, "0x00001d63c005114300006228000053bf00004eb9", [], [], "outer_terrain_plain"),

	("quick_battle_5", sf_generate, "none", "none", (0.00, 0.00), (120.00, 120.00), -100.0, "0x3a078bb2000589630000667200002fb90000179c", [], [], "outer_terrain_plain"),

	("quick_battle_6", sf_generate, "none", "none", (0.00, 0.00), (120.00, 120.00), -100.0, "0xa0425ccf0004a92a000063d600005a8a00003d9a", [], [], "outer_terrain_steppe"),

	("quick_battle_7", sf_generate, "none", "none", (0.00, 0.00), (100.00, 100.00), -100.0, "0x314d060900036cd70000295300002ec9000025f3", [], [], "outer_terrain_plain"),

	("salt_mine", sf_generate, "none", "none", (-200.00, -200.00), (200.00, 200.00), -100.0, "0x2a07b23200025896000023ee00007f9c000022a8", [], [], "outer_terrain_steppe"),

	("novice_ground", sf_indoors, "training_house_a", "bo_training_house_a", (-100.00, -100.00), (100.00, 100.00), -100.0, "0", [], []),

	("zendar_arena", sf_generate, "none", "none", (0.00, 0.00), (100.00, 100.00), -100.0, "0xa0001d9300031ccb0000156f000048ba0000361c", [], [], "outer_terrain_plain"),

	("dhorak_keep", sf_generate, "none", "none", (0.00, 0.00), (120.00, 120.00), -100.0, "0x33a7946000028ca300007f4a0000479400161992", ["exit"], []),

	("reserved4", sf_generate, "none", "none", (0.00, 0.00), (120.00, 120.00), -100.0, "28791", [], []),

	("reserved5", sf_generate, "none", "none", (0.00, 0.00), (120.00, 120.00), -100.0, "117828", [], []),

	("reserved6", sf_generate, "none", "none", (0.00, 0.00), (100.00, 100.00), -100.0, "6849", [], []),

	("reserved7", sf_generate, "none", "none", (0.00, 0.00), (100.00, 100.00), -100.0, "6849", [], []),

	("reserved8", sf_generate, "none", "none", (0.00, 0.00), (100.00, 100.00), -100.0, "13278", [], []),

	("reserved9", sf_indoors, "thirsty_lion", "bo_thirsty_lion", (-100.00, -100.00), (100.00, 100.00), -100.0, "0", [], []),

	("reserved10", 0, "none", "none", (-100.00, -100.00), (100.00, 100.00), -100.0, "0", [], []),

	("reserved11", 0, "none", "none", (-100.00, -100.00), (100.00, 100.00), -100.0, "0", [], []),

	("reserved12", sf_indoors, "thirsty_lion", "bo_thirsty_lion", (-100.00, -100.00), (100.00, 100.00), -100.0, "0", [], []),

	("training_ground", sf_generate, "none", "none", (0.00, 0.00), (120.00, 120.00), -100.0, "0x30000500400360d80000189f00002a8380006d91", [], ["tutorial_chest_1", "tutorial_chest_2"], "outer_terrain_plain"),

	("tutorial_1", sf_indoors, "tutorial_1_scene", "bo_tutorial_1_scene", (-100.00, -100.00), (100.00, 100.00), -100.0, "0", [], []),

	("tutorial_2", sf_indoors, "tutorial_2_scene", "bo_tutorial_2_scene", (-100.00, -100.00), (100.00, 100.00), -100.0, "0", [], []),

	("tutorial_3", sf_indoors, "tutorial_3_scene", "bo_tutorial_3_scene", (-100.00, -100.00), (100.00, 100.00), -100.0, "0", [], []),

	("tutorial_4", sf_generate, "none", "none", (0.00, 0.00), (120.00, 120.00), -100.0, "0x30000500400360d80000189f00002a8380006d91", [], [], "outer_terrain_plain"),

	("tutorial_5", sf_generate, "none", "none", (0.00, 0.00), (120.00, 120.00), -100.0, "0x3a06dca80005715c0000537400001377000011fe", [], [], "outer_terrain_plain"),

	("training_ground_horse_track_1", sf_generate, "none", "none", (0.00, 0.00), (120.00, 120.00), -100.0, "0x00000000337553240004d53700000c0500002a0f80006267", [], [], "outer_terrain_plain_farmountain"),

	("training_ground_horse_track_2", sf_generate, "none", "none", (0.00, 0.00), (120.00, 120.00), -100.0, "0x00000000301553240004d5370000466000002a0f800073f1", [], [], "outer_terrain_plain_farmountain"),

	("training_ground_horse_track_3", sf_generate, "none", "none", (0.00, 0.00), (120.00, 120.00), -100.0, "0x00000000400c12b2000515470000216b0000485e00006928", [], [], "outer_terrain_snow"),

	("training_ground_horse_track_4", sf_generate, "none", "none", (0.00, 0.00), (120.00, 120.00), -100.0, "0x00000000200b60320004a5290000180d0000452f00000e90", [], [], "outer_terrain_steppe"),

	("training_ground_horse_track_5", sf_generate, "none", "none", (0.00, 0.00), (120.00, 120.00), -100.0, "0x000000003008208e0006419000000f730000440f00003c86", [], [], "outer_terrain_plain"),

	("training_ground_ranged_melee_1", sf_generate, "none", "none", (0.00, 0.00), (120.00, 120.00), -100.0, "0x00000001350455c20005194a000041cb00005ae800000ff5", [], [], "outer_terrain_plain_farmountain"),

	("training_ground_ranged_melee_2", sf_generate, "none", "none", (0.00, 0.00), (120.00, 120.00), -100.0, "0x0000000532c8dccb0005194a000041cb00005ae800001bdd", [], [], "outer_terrain_plain_farmountain"),

	("training_ground_ranged_melee_3", sf_generate, "none", "none", (0.00, 0.00), (120.00, 120.00), -100.0, "0x000000054327dcba0005194a00001b1d00005ae800004d63", [], [], "outer_terrain_snow"),

	("training_ground_ranged_melee_4", sf_generate, "none", "none", (0.00, 0.00), (120.00, 120.00), -100.0, "0x000000012247dcba0005194a000041ef00005ae8000050af", [], [], "outer_terrain_steppe"),

	("training_ground_ranged_melee_5", sf_generate, "none", "none", (0.00, 0.00), (120.00, 120.00), -100.0, "0x00000001324a9cba0005194a000041ef00005ae800003c55", [], [], "outer_terrain_plain"),

	("zendar_center", sf_generate, "none", "none", (0.00, 0.00), (100.00, 100.00), -100.0, "0x300bc5430001e0780000448a0000049f00007932", ["the_happy_boar", "random_scene", "zendar_merchant"], [], "outer_terrain_plain"),

	("the_happy_boar", sf_indoors, "interior_town_house_f", "bo_interior_town_house_f", (-100.00, -100.00), (100.00, 100.00), -100.0, "0", ["zendar_center"], ["zendar_chest"]),

	("zendar_merchant", sf_indoors, "interior_town_house_i", "bo_interior_town_house_i", (-100.00, -100.00), (100.00, 100.00), -100.0, "0", [], []),

	("town_1_center", sf_generate, "none", "none", (0.00, 0.00), (100.00, 100.00), -100.0, "0x00000000b00005000004a92800003aea00006c97000006be", [], [], "outer_terrain_sisterton"),

	("town_3_center", sf_generate, "none", "none", (0.00, 0.00), (100.00, 100.00), -100.0, "0x000000013003d7e30005053f00003b4e0000146300006e84", [], [], "outer_terrain_beach"),

	("town_6_center", sf_generate, "none", "none", (0.00, 0.00), (100.00, 100.00), -100.0, "0x0000000030000913400d2348000013980000600500006b66", [], [], "outer_terrain_beach"),

	("town_8_center", sf_generate, "none", "none", (0.00, 0.00), (100.00, 100.00), -100.0, "0x000000033000124c000acab40000280700000c9f00000ab5", [], [], "outer_terrain_none"),

	("town_9_center", sf_generate, "none", "none", (0.00, 0.00), (100.00, 100.00), -100.0, "0x00000000300005000005294700007e2b00004b9f00002394", [], [], "outer_terrain_plain"),

	("town_12_center", sf_generate, "none", "none", (0.00, 0.00), (100.00, 100.00), -100.0, "0x0000000050111563000ba6ee000009af00005bab00003394", [], [], "sea_outer_terrain_2"),

	("town_16_center", sf_generate, "none", "none", (0.00, 0.00), (100.00, 100.00), -100.0, "0x00000002200005000005f57b00005885000046bd00006d9c", [], [], "sea_outer_terrain_2"),

	("town_17_center", sf_generate, "none", "none", (0.00, 0.00), (100.00, 100.00), -100.0, "0x000000012002a0b20004992700006e54000007fe00001fd2", [], [], "sea_outer_terrain_2"),

	("town_18_center", sf_generate, "none", "none", (0.00, 0.00), (100.00, 100.00), -100.0, "0x30001d9300031ccb0000156f000048ba0000361c", [], [], "outer_terrain_plain"),

	("town_19_center", sf_generate, "none", "none", (0.00, 0.00), (100.00, 100.00), -100.0, "0x0000000050000500000d23480000055e00007ba600002d66", [], [], "outer_terrain_desert"),

	("town_20_center", sf_generate, "none", "none", (0.00, 0.00), (100.00, 100.00), -100.0, "0x00000a0650001e9a00a505418000581f000028c800000143", [], [], "outer_terrain_desert"),

	("town_23_center", sf_generate, "none", "none", (0.00, 0.00), (100.00, 100.00), -100.0, "0x00000000300005000008f63b00001d5700005904000031b7", [], [], "sea_outer_terrain_2"),

	("town_24_center", sf_generate, "none", "none", (0.00, 0.00), (100.00, 100.00), -100.0, "0x00000000300005000009424e00000d2900007e38000038b3", [], [], "outer_terrain_thir_new"),

	("town_25_center", sf_generate, "none", "none", (0.00, 0.00), (100.00, 100.00), -100.0, "0x00000001300659630003c8f300003ca000006a8900003c89", [], [], "outer_terrain_beach"),

	("town_26_center", sf_generate, "none", "none", (0.00, 0.00), (100.00, 100.00), -100.0, "0x000000013003d7e30005053f00003b4e0000146300006e84", [], [], "outer_terrain_beach"),

	("town_27_center", sf_generate, "none", "none", (0.00, 0.00), (100.00, 100.00), -100.0, "0x0000000030000913400d2348000013980000600500006b66", [], [], "outer_terrain_beach"),

	("town_30_center", sf_generate, "none", "none", (0.00, 0.00), (100.00, 100.00), -100.0, "0x00000000300b1063000b5edb000042c00000676600001c6b", [], [], "outer_terrain_plain"),

	("town_31_center", sf_generate, "none", "none", (0.00, 0.00), (100.00, 100.00), -100.0, "0x00000002200005000005f57b00005885000046bd00006d9c", [], [], "outer_terrain_beach"),

	("town_32_center", sf_generate, "none", "none", (0.00, 0.00), (100.00, 100.00), -100.0, "0x000000012002a0b20004992700006e54000007fe00001fd2", [], [], "sea_outer_terrain_2"),

	("town_33_center", sf_generate, "none", "none", (0.00, 0.00), (100.00, 100.00), -100.0, "0x00000000300005000005294700007e2b00004b9f00002394", [], [], "outer_terrain_plain"),

	("town_34_center", sf_generate, "none", "none", (0.00, 0.00), (100.00, 100.00), -100.0, "0x00000001300659630003c8f300003ca000006a8900003c89", [], [], "outer_terrain_beach"),

	("town_35_center", sf_generate, "none", "none", (0.00, 0.00), (100.00, 100.00), -100.0, "0x3000148000025896000074e600006c260000125a", [], [], "outer_terrain_plain"),

	("town_36_center", sf_generate, "none", "none", (0.00, 0.00), (100.00, 100.00), -100.0, "0x00000002300491830004a529000036230000312a00003653", [], [], "outer_terrain_plain"),

	("town_38_center", sf_generate, "none", "none", (0.00, 0.00), (100.00, 100.00), -100.0, "0x0000000020045abc000308c4000029d9000033bd000009b9", [], [], "outer_terrain_steppe_mountain"),

	("town_40_center", sf_generate, "none", "none", (0.00, 0.00), (100.00, 100.00), -100.0, "0x000000013002ab630004651800000d7a00007f3100002701", [], [], "sea_outer_terrain_2"),

	("town_41_center", sf_generate, "none", "none", (0.00, 0.00), (100.00, 100.00), -100.0, "0x0000000130010e0e0005fd84000011c60000285b00005cbe", [], [], "outer_terrain_plain"),

	("town_42_center", sf_generate, "none", "none", (0.00, 0.00), (100.00, 100.00), -100.0, "0x00000000300005000005294700007e2b00004b9f00002394", [], [], "outer_terrain_plain"),

	("town_44_center", sf_generate, "none", "none", (0.00, 0.00), (100.00, 100.00), -100.0, "0x00000000200016da000364d9000060f500007591000064e7", [], [], "outer_terrain_steppe"),

	("town_45_center", sf_generate, "none", "none", (0.00, 0.00), (100.00, 100.00), -100.0, "0x0000000020049cbd00025896000048e90000164400002b3f", [], [], "outer_terrain_steppe"),

	("town_46_center", sf_generate, "none", "none", (0.00, 0.00), (100.00, 100.00), -100.0, "0x000000003000050000085e1900005f5e00005fa700002d1d", [], [], "sea_outer_terrain_2"),

	("town_47_center", sf_generate, "none", "none", (0.00, 0.00), (100.00, 100.00), -100.0, "0x0000000020000500000aaa1000000a4500006d740000437a", [], [], "outer_terrain_steppe"),

	("town_48_center", sf_generate, "none", "none", (0.00, 0.00), (100.00, 100.00), -100.0, "0x0000000020049cbd00025896000048e90000164400002b3f", [], [], "outer_terrain_steppe"),

	("town_49_center", sf_generate, "none", "none", (0.00, 0.00), (100.00, 100.00), -100.0, "0x0000000020049cbd00025896000048e90000164400002b3f", [], [], "outer_terrain_steppe"),

	("town_50_center", sf_generate, "none", "none", (0.00, 0.00), (100.00, 100.00), -100.0, "0x0000000020049cbd00025896000048e90000164400002b3f", [], [], "outer_terrain_steppe"),

	("town_51_center", sf_generate, "none", "none", (0.00, 0.00), (100.00, 100.00), -100.0, "0x00000000300d97e300050d420000482a0000341d00005ecb", [], [], "outer_terrain_plain_farmountain"),

	("town_52_center", sf_generate, "none", "none", (0.00, 0.00), (100.00, 100.00), -100.0, "0x00000002300491830004a529000036230000312a00003653", [], [], "outer_terrain_plain"),

	("town_53_center", sf_generate, "none", "none", (0.00, 0.00), (100.00, 100.00), -100.0, "0x00000002300491830004a529000036230000312a00003653", [], [], "outer_terrain_plain"),

	("town_54_center", sf_generate, "none", "none", (0.00, 0.00), (100.00, 100.00), -100.0, "0x00000002300491830004a529000036230000312a00003653", [], [], "outer_terrain_plain"),

	("town_1_castle", sf_indoors, "interior_castle_a", "bo_interior_castle_a", (-100.00, -100.00), (100.00, 100.00), -100.0, "0", ["exit"], ["town_1_seneschal"]),

	("town_3_castle", sf_indoors, "interior_castle_k", "bo_interior_castle_k", (-100.00, -100.00), (100.00, 100.00), -100.0, "0", ["exit"], ["town_3_seneschal"]),

	("town_6_castle", sf_indoors, "interior_castle_k", "bo_interior_castle_k", (-100.00, -100.00), (100.00, 100.00), -100.0, "0", ["exit"], ["town_6_seneschal"]),

	("town_8_castle", sf_indoors, "interior_castle_v", "bo_interior_castle_v", (-100.00, -100.00), (100.00, 100.00), -100.0, "0", ["exit"], ["town_8_seneschal"]),

	("town_9_castle", sf_indoors, "interior_castle_a", "bo_interior_castle_a", (-100.00, -100.00), (100.00, 100.00), -100.0, "0", ["exit"], ["town_9_seneschal"]),

	("town_12_castle", sf_indoors, "arabian_interior_keep_b", "bo_arabian_interior_keep_b", (-100.00, -100.00), (100.00, 100.00), -100.0, "0", ["exit"], ["town_12_seneschal"]),

	("town_16_castle", sf_indoors, "tywins_chamber", "bo_tywins_chamber", (-100.00, -100.00), (100.00, 100.00), -100.0, "0", ["exit"], ["town_16_seneschal"]),

	("town_17_castle", sf_generate, "none", "none", (0.00, 0.00), (100.00, 100.00), -100.0, "0x000000012002a0b20004992700006e54000007fe00001fd2", ["exit"], ["town_17_seneschal"], "sea_outer_terrain_2"),

	("town_18_castle", sf_indoors, "interior_castle_a", "bo_interior_castle_a", (-100.00, -100.00), (100.00, 100.00), -100.0, "0", ["exit"], ["town_18_seneschal"]),

	("town_19_castle", sf_indoors, "arabian_interior_keep_b", "bo_arabian_interior_keep_b", (-100.00, -100.00), (100.00, 100.00), -100.0, "0", ["exit"], ["town_19_seneschal"]),

	("town_20_castle", sf_indoors, "arabian_interior_keep_b", "bo_arabian_interior_keep_b", (-100.00, -100.00), (100.00, 100.00), -100.0, "0", ["exit"], ["town_20_seneschal"]),

	("town_23_castle", sf_indoors, "interior_castle_q", "bo_interior_castle_q", (-100.00, -100.00), (100.00, 100.00), -100.0, "0", ["exit"], ["town_23_seneschal"]),

	("town_24_castle", sf_indoors, "interior_castle_v", "bo_interior_castle_v", (-100.00, -100.00), (100.00, 100.00), -100.0, "0", ["exit"], ["town_24_seneschal"]),

	("town_25_castle", sf_indoors, "interior_castle_v", "bo_interior_castle_v", (-100.00, -100.00), (100.00, 100.00), -100.0, "0", ["exit"], ["town_25_seneschal"]),

	("town_26_castle", sf_indoors, "interior_castle_v", "bo_interior_castle_v", (-100.00, -100.00), (100.00, 100.00), -100.0, "0", ["exit"], ["town_26_seneschal"]),

	("town_27_castle", sf_indoors, "interior_castle_k", "bo_interior_castle_k", (-100.00, -100.00), (100.00, 100.00), -100.0, "0", ["exit"], ["town_27_seneschal"]),

	("town_30_castle", sf_indoors, "interior_castle_v", "bo_interior_castle_v", (-100.00, -100.00), (100.00, 100.00), -100.0, "0", ["exit"], ["town_30_seneschal"]),

	("town_31_castle", sf_indoors, "white_harbor_scene", "bo_interior_castle_t", (-100.00, -100.00), (100.00, 100.00), -100.0, "0", ["exit"], ["town_31_seneschal"]),

	("town_32_castle", sf_generate, "none", "none", (0.00, 0.00), (100.00, 100.00), -100.0, "0x000000012002a0b20004992700006e54000007fe00001fd2", ["exit"], ["town_32_seneschal"], "sea_outer_terrain_2"),

	("town_33_castle", sf_indoors, "interior_castle_v", "bo_interior_castle_v", (-100.00, -100.00), (100.00, 100.00), -100.0, "0", ["exit"], ["town_33_seneschal"]),

	("town_34_castle", sf_indoors, "interior_castle_a", "bo_interior_castle_a", (-100.00, -100.00), (100.00, 100.00), -100.0, "0", ["exit"], ["town_34_seneschal"]),

	("town_35_castle", sf_indoors, "interior_castle_a", "bo_interior_castle_a", (-100.00, -100.00), (100.00, 100.00), -100.0, "0", ["exit"], ["town_35_seneschal"]),

	("town_36_castle", sf_indoors, "interior_castle_g_square_keep_b", "bo_interior_castle_g_square_keep_b", (-100.00, -100.00), (100.00, 100.00), -100.0, "0", ["exit"], ["town_36_seneschal"]),

	("town_38_castle", sf_indoors, "interior_castle_g_square_keep", "bo_interior_castle_g_square_keep", (-100.00, -100.00), (100.00, 100.00), -100.0, "0", ["exit"], ["town_38_seneschal"]),

	("town_40_castle", sf_indoors, "arabian_interior_keep_a", "bo_arabian_interior_keep_a", (-100.00, -100.00), (100.00, 100.00), -100.0, "0", ["exit"], ["town_40_seneschal"]),

	("town_41_castle", sf_indoors, "interior_castle_k", "bo_interior_castle_k", (-100.00, -100.00), (100.00, 100.00), -100.0, "0", ["exit"], ["town_41_seneschal"]),

	("town_42_castle", sf_indoors, "interior_castle_v", "bo_interior_castle_v", (-100.00, -100.00), (100.00, 100.00), -100.0, "0", ["exit"], ["town_42_seneschal"]),

	("town_44_castle", sf_indoors, "interior_castle_g_square_keep_b", "bo_interior_castle_g_square_keep_b", (-100.00, -100.00), (100.00, 100.00), -100.0, "0", ["exit"], ["town_44_seneschal"]),

	("town_45_castle", sf_indoors, "arabian_interior_keep_a", "bo_arabian_interior_keep_a", (-100.00, -100.00), (100.00, 100.00), -100.0, "0", ["exit"], ["town_45_seneschal"]),

	("town_46_castle", sf_indoors, "arabian_interior_keep_a", "bo_arabian_interior_keep_a", (-100.00, -100.00), (100.00, 100.00), -100.0, "0", ["exit"], ["town_46_seneschal"]),

	("town_47_castle", sf_indoors, "arabian_interior_keep_a", "bo_arabian_interior_keep_a", (-100.00, -100.00), (100.00, 100.00), -100.0, "0", ["exit"], ["town_47_seneschal"]),

	("town_48_castle", sf_indoors, "arabian_interior_keep_b", "bo_arabian_interior_keep_b", (-100.00, -100.00), (100.00, 100.00), -100.0, "0", ["exit"], ["town_48_seneschal"]),

	("town_49_castle", sf_indoors, "arabian_interior_keep_b", "bo_arabian_interior_keep_b", (-100.00, -100.00), (100.00, 100.00), -100.0, "0", ["exit"], ["town_49_seneschal"]),

	("town_50_castle", sf_indoors, "arabian_interior_keep_b", "bo_arabian_interior_keep_b", (-100.00, -100.00), (100.00, 100.00), -100.0, "0", ["exit"], ["town_50_seneschal"]),

	("town_51_castle", sf_indoors, "interior_castle_g_square_keep_b", "bo_interior_castle_g_square_keep_b", (-100.00, -100.00), (100.00, 100.00), -100.0, "0", ["exit"], ["town_51_seneschal"]),

	("town_52_castle", sf_indoors, "interior_castle_g_square_keep_b", "bo_interior_castle_g_square_keep_b", (-100.00, -100.00), (100.00, 100.00), -100.0, "0", ["exit"], ["town_52_seneschal"]),

	("town_53_castle", sf_indoors, "interior_castle_g_square_keep_b", "bo_interior_castle_g_square_keep_b", (-100.00, -100.00), (100.00, 100.00), -100.0, "0", ["exit"], ["town_53_seneschal"]),

	("town_54_castle", sf_indoors, "interior_castle_g_square_keep_b", "bo_interior_castle_g_square_keep_b", (-100.00, -100.00), (100.00, 100.00), -100.0, "0", ["exit"], ["town_54_seneschal"]),

	("town_1_tavern", sf_indoors, "viking_interior_tavern_a", "bo_viking_interior_tavern_a", (-100.00, -100.00), (100.00, 100.00), -100.0, "0", ["exit"], []),

	("town_3_tavern", sf_indoors, "interior_tavern_g", "bo_interior_tavern_g", (-100.00, -100.00), (100.00, 100.00), -100.0, "0", ["exit"], []),

	("town_6_tavern", sf_indoors, "interior_tavern_f", "bo_interior_tavern_f", (-100.00, -100.00), (100.00, 100.00), -100.0, "0", ["exit"], []),

	("town_8_tavern", sf_indoors, "interior_town_house_f", "bo_interior_town_house_f", (-100.00, -100.00), (100.00, 100.00), -100.0, "0", ["exit"], []),

	("town_9_tavern", sf_indoors, "interior_tavern_b", "bo_interior_tavern_b", (-100.00, -100.00), (100.00, 100.00), -100.0, "0", ["exit"], []),

	("town_12_tavern", sf_indoors, "interior_town_house_steppe_g", "bo_interior_town_house_steppe_g", (-100.00, -100.00), (100.00, 100.00), -100.0, "0", ["exit"], []),

	("town_16_tavern", sf_indoors, "interior_tavern_c", "bo_interior_tavern_c", (-100.00, -100.00), (100.00, 100.00), -100.0, "0", ["exit"], []),

	("town_17_tavern", sf_indoors, "interior_tavern_h", "bo_interior_tavern_h", (-100.00, -100.00), (100.00, 100.00), -100.0, "0", ["exit"], []),

	("town_18_tavern", sf_indoors, "interior_rhodok_houses_d", "bo_interior_rhodok_houses_d", (-100.00, -100.00), (100.00, 100.00), -100.0, "0", ["exit"], []),

	("town_19_tavern", sf_indoors, "interior_town_house_steppe_c", "bo_interior_town_house_steppe_c", (-100.00, -100.00), (100.00, 100.00), -100.0, "0", ["exit"], []),

	("town_20_tavern", sf_indoors, "interior_town_house_steppe_g", "bo_interior_town_house_steppe_g", (-100.00, -100.00), (100.00, 100.00), -100.0, "0", ["exit"], []),

	("town_23_tavern", sf_indoors, "interior_tavern_g", "bo_interior_tavern_g", (-100.00, -100.00), (100.00, 100.00), -100.0, "0", ["exit"], []),

	("town_24_tavern", sf_indoors, "interior_rhodok_houses_b", "bo_interior_rhodok_houses_b", (-100.00, -100.00), (100.00, 100.00), -100.0, "0", ["exit"], []),

	("town_25_tavern", sf_indoors, "interior_tavern_g", "bo_interior_tavern_g", (-100.00, -100.00), (100.00, 100.00), -100.0, "0", ["exit"], []),

	("town_26_tavern", sf_indoors, "interior_tavern_b", "bo_interior_tavern_b", (-100.00, -100.00), (100.00, 100.00), -100.0, "0", ["exit"], []),

	("town_27_tavern", sf_indoors, "viking_interior_tavern_a", "bo_viking_interior_tavern_a", (-100.00, -100.00), (100.00, 100.00), -100.0, "0", ["exit"], []),

	("town_30_tavern", sf_indoors, "interior_tavern_b", "bo_interior_tavern_b", (-100.00, -100.00), (100.00, 100.00), -100.0, "0", ["exit"], []),

	("town_31_tavern", sf_indoors, "interior_tavern_g", "bo_interior_tavern_g", (-100.00, -100.00), (100.00, 100.00), -100.0, "0", ["exit"], []),

	("town_32_tavern", sf_indoors, "interior_tavern_g", "bo_interior_tavern_g", (-100.00, -100.00), (100.00, 100.00), -100.0, "0", ["exit"], []),

	("town_33_tavern", sf_indoors, "viking_interior_tavern_a", "bo_viking_interior_tavern_a", (-100.00, -100.00), (100.00, 100.00), -100.0, "0", ["exit"], []),

	("town_34_tavern", sf_indoors, "viking_interior_tavern_a", "bo_viking_interior_tavern_a", (-100.00, -100.00), (100.00, 100.00), -100.0, "0", ["exit"], []),

	("town_35_tavern", sf_indoors, "viking_interior_tavern_a", "bo_viking_interior_tavern_a", (-100.00, -100.00), (100.00, 100.00), -100.0, "0", ["exit"], []),

	("town_36_tavern", sf_indoors, "interior_town_house_steppe_c", "bo_interior_town_house_steppe_c", (-100.00, -100.00), (100.00, 100.00), -100.0, "0", ["exit"], []),

	("town_38_tavern", sf_indoors, "interior_tavern_g", "bo_interior_tavern_g", (-100.00, -100.00), (100.00, 100.00), -100.0, "0", ["exit"], []),

	("town_40_tavern", sf_indoors, "interior_town_house_steppe_c", "bo_interior_town_house_steppe_c", (-100.00, -100.00), (100.00, 100.00), -100.0, "0", ["exit"], []),

	("town_41_tavern", sf_indoors, "viking_interior_tavern_a", "bo_viking_interior_tavern_a", (-100.00, -100.00), (100.00, 100.00), -100.0, "0", ["exit"], []),

	("town_42_tavern", sf_indoors, "interior_tavern_g", "bo_interior_tavern_g", (-100.00, -100.00), (100.00, 100.00), -100.0, "0", ["exit"], []),

	("town_44_tavern", sf_indoors, "interior_town_house_steppe_d", "bo_interior_town_house_steppe_d", (-100.00, -100.00), (100.00, 100.00), -100.0, "0", ["exit"], []),

	("town_45_tavern", sf_indoors, "interior_town_house_steppe_c", "bo_interior_town_house_steppe_c", (-100.00, -100.00), (100.00, 100.00), -100.0, "0", ["exit"], []),

	("town_46_tavern", sf_indoors, "interior_town_house_steppe_g", "bo_interior_town_house_steppe_g", (-100.00, -100.00), (100.00, 100.00), -100.0, "0", ["exit"], []),

	("town_47_tavern", sf_indoors, "interior_town_house_steppe_c", "bo_interior_town_house_steppe_c", (-100.00, -100.00), (100.00, 100.00), -100.0, "0", ["exit"], []),

	("town_48_tavern", sf_indoors, "interior_town_house_steppe_c", "bo_interior_town_house_steppe_c", (-100.00, -100.00), (100.00, 100.00), -100.0, "0", ["exit"], []),

	("town_49_tavern", sf_indoors, "interior_town_house_steppe_c", "bo_interior_town_house_steppe_c", (-100.00, -100.00), (100.00, 100.00), -100.0, "0", ["exit"], []),

	("town_50_tavern", sf_indoors, "interior_town_house_steppe_c", "bo_interior_town_house_steppe_c", (-100.00, -100.00), (100.00, 100.00), -100.0, "0", ["exit"], []),

	("town_51_tavern", sf_indoors, "interior_town_house_steppe_c", "bo_interior_town_house_steppe_c", (-100.00, -100.00), (100.00, 100.00), -100.0, "0", ["exit"], []),

	("town_52_tavern", sf_indoors, "interior_town_house_steppe_c", "bo_interior_town_house_steppe_c", (-100.00, -100.00), (100.00, 100.00), -100.0, "0", ["exit"], []),

	("town_53_tavern", sf_indoors, "interior_town_house_steppe_c", "bo_interior_town_house_steppe_c", (-100.00, -100.00), (100.00, 100.00), -100.0, "0", ["exit"], []),

	("town_54_tavern", sf_indoors, "interior_town_house_steppe_c", "bo_interior_town_house_steppe_c", (-100.00, -100.00), (100.00, 100.00), -100.0, "0", ["exit"], []),

	("town_1_store", sf_indoors, "viking_interior_merchant_a", "bo_viking_interior_merchant_a", (-100.00, -100.00), (100.00, 100.00), -100.0, "0", ["exit"], []),

	("town_3_store", sf_indoors, "interior_rhodok_houses_d", "bo_interior_rhodok_houses_d", (-100.00, -100.00), (100.00, 100.00), -100.0, "0", ["exit"], []),

	("town_6_store", sf_indoors, "interior_town_house_j", "bo_interior_town_house_j", (-100.00, -100.00), (100.00, 100.00), -100.0, "0", ["exit"], []),

	("town_8_store", sf_indoors, "interior_house_b", "bo_interior_house_b", (-100.00, -100.00), (100.00, 100.00), -100.0, "0", ["exit"], []),

	("town_9_store", sf_indoors, "interior_tavern_a", "bo_interior_tavern_a", (-100.00, -100.00), (100.00, 100.00), -100.0, "0", ["exit"], []),

	("town_12_store", sf_indoors, "viking_interior_merchant_a", "bo_viking_interior_merchant_a", (-100.00, -100.00), (100.00, 100.00), -100.0, "0", ["exit"], []),

	("town_16_store", sf_indoors, "interior_town_house_i", "bo_interior_town_house_i", (-100.00, -100.00), (100.00, 100.00), -100.0, "0", ["exit"], []),

	("town_17_store", sf_indoors, "interior_town_house_steppe_g", "bo_interior_town_house_steppe_g", (-100.00, -100.00), (100.00, 100.00), -100.0, "0", ["exit"], []),

	("town_18_store", sf_indoors, "interior_town_house_steppe_d", "bo_interior_town_house_steppe_d", (-100.00, -100.00), (100.00, 100.00), -100.0, "0", ["exit"], []),

	("town_19_store", sf_indoors, "interior_town_house_steppe_d", "bo_interior_town_house_steppe_d", (-100.00, -100.00), (100.00, 100.00), -100.0, "0", ["exit"], []),

	("town_20_store", sf_indoors, "interior_town_house_steppe_d", "bo_interior_town_house_steppe_d", (-100.00, -100.00), (100.00, 100.00), -100.0, "0", ["exit"], []),

	("town_23_store", sf_indoors, "interior_town_house_j", "bo_interior_town_house_j", (-100.00, -100.00), (100.00, 100.00), -100.0, "0", ["exit"], []),

	("town_24_store", sf_indoors, "interior_house_b", "bo_interior_house_b", (-100.00, -100.00), (100.00, 100.00), -100.0, "0", ["exit"], []),

	("town_25_store", sf_indoors, "interior_house_b", "bo_interior_house_b", (-100.00, -100.00), (100.00, 100.00), -100.0, "0", ["exit"], []),

	("town_26_store", sf_indoors, "interior_house_b", "bo_interior_house_b", (-100.00, -100.00), (100.00, 100.00), -100.0, "0", ["exit"], []),

	("town_27_store", sf_indoors, "interior_rhodok_houses_b", "bo_interior_rhodok_houses_b", (-100.00, -100.00), (100.00, 100.00), -100.0, "0", ["exit"], []),

	("town_30_store", sf_indoors, "interior_town_house_j", "bo_interior_town_house_j", (-100.00, -100.00), (100.00, 100.00), -100.0, "0", ["exit"], []),

	("town_31_store", sf_indoors, "interior_town_house_j", "bo_interior_town_house_j", (-100.00, -100.00), (100.00, 100.00), -100.0, "0", ["exit"], []),

	("town_32_store", sf_indoors, "interior_house_b", "bo_interior_house_b", (-100.00, -100.00), (100.00, 100.00), -100.0, "0", ["exit"], []),

	("town_33_store", sf_indoors, "interior_town_house_steppe_d", "bo_interior_town_house_steppe_d", (-100.00, -100.00), (100.00, 100.00), -100.0, "0", ["exit"], []),

	("town_34_store", sf_indoors, "interior_town_house_steppe_d", "bo_interior_town_house_steppe_d", (-100.00, -100.00), (100.00, 100.00), -100.0, "0", ["exit"], []),

	("town_35_store", sf_indoors, "viking_interior_merchant_a", "bo_viking_interior_merchant_a", (-100.00, -100.00), (100.00, 100.00), -100.0, "0", ["exit"], []),

	("town_36_store", sf_indoors, "interior_town_house_j", "bo_interior_town_house_j", (-100.00, -100.00), (100.00, 100.00), -100.0, "0", ["exit"], []),

	("town_38_store", sf_indoors, "interior_town_house_steppe_d", "bo_interior_town_house_steppe_d", (-100.00, -100.00), (100.00, 100.00), -100.0, "0", ["exit"], []),

	("town_40_store", sf_indoors, "interior_house_extension_h", "bo_interior_house_extension_h", (-100.00, -100.00), (100.00, 100.00), -100.0, "0", ["exit"], []),

	("town_41_store", sf_indoors, "interior_house_extension_h", "bo_interior_house_extension_h", (-100.00, -100.00), (100.00, 100.00), -100.0, "0", ["exit"], []),

	("town_42_store", sf_indoors, "interior_town_house_steppe_g", "bo_interior_town_house_steppe_g", (-100.00, -100.00), (100.00, 100.00), -100.0, "0", ["exit"], []),

	("town_44_store", sf_indoors, "interior_town_house_steppe_g", "bo_interior_town_house_steppe_g", (-100.00, -100.00), (100.00, 100.00), -100.0, "0", ["exit"], []),

	("town_45_store", sf_indoors, "interior_town_house_steppe_d", "bo_interior_town_house_steppe_d", (-100.00, -100.00), (100.00, 100.00), -100.0, "0", ["exit"], []),

	("town_46_store", sf_indoors, "interior_town_house_steppe_d", "bo_interior_town_house_steppe_d", (-100.00, -100.00), (100.00, 100.00), -100.0, "0", ["exit"], []),

	("town_47_store", sf_indoors, "interior_town_house_steppe_d", "bo_interior_town_house_steppe_d", (-100.00, -100.00), (100.00, 100.00), -100.0, "0", ["exit"], []),

	("town_48_store", sf_indoors, "interior_town_house_steppe_d", "bo_interior_town_house_steppe_d", (-100.00, -100.00), (100.00, 100.00), -100.0, "0", ["exit"], []),

	("town_49_store", sf_indoors, "interior_town_house_steppe_d", "bo_interior_town_house_steppe_d", (-100.00, -100.00), (100.00, 100.00), -100.0, "0", ["exit"], []),

	("town_50_store", sf_indoors, "interior_town_house_steppe_d", "bo_interior_town_house_steppe_d", (-100.00, -100.00), (100.00, 100.00), -100.0, "0", ["exit"], []),

	("town_51_store", sf_indoors, "interior_town_house_steppe_d", "bo_interior_town_house_steppe_d", (-100.00, -100.00), (100.00, 100.00), -100.0, "0", ["exit"], []),

	("town_52_store", sf_indoors, "interior_town_house_steppe_d", "bo_interior_town_house_steppe_d", (-100.00, -100.00), (100.00, 100.00), -100.0, "0", ["exit"], []),

	("town_53_store", sf_indoors, "interior_town_house_steppe_d", "bo_interior_town_house_steppe_d", (-100.00, -100.00), (100.00, 100.00), -100.0, "0", ["exit"], []),

	("town_54_store", sf_indoors, "interior_town_house_steppe_d", "bo_interior_town_house_steppe_d", (-100.00, -100.00), (100.00, 100.00), -100.0, "0", ["exit"], []),

	("town_1_arena", sf_generate, "none", "none", (0.00, 0.00), (100.00, 100.00), -100.0, "0x000000003000050000042d0d000045dd0000243500004ef7", [], [], "outer_terrain_plain_farmountain"),

	("town_3_arena", sf_generate, "none", "none", (0.00, 0.00), (100.00, 100.00), -100.0, "0x000000003000050000042d0d000045dd0000243500004ef7", [], [], "outer_terrain_plain_farmountain"),

	("town_6_arena", sf_generate, "none", "none", (0.00, 0.00), (100.00, 100.00), -100.0, "0x000000003000050000042d0d000045dd0000243500004ef7", [], [], "outer_terrain_plain_farmountain"),

	("town_8_arena", sf_generate, "none", "none", (0.00, 0.00), (100.00, 100.00), -100.0, "0x000000003000050000042d0d000045dd0000243500004ef7", [], [], "outer_terrain_plain_farmountain"),

	("town_9_arena", sf_generate, "none", "none", (0.00, 0.00), (100.00, 100.00), -100.0, "0x000000003000050000042d0d000045dd0000243500004ef7", [], [], "outer_terrain_plain_farmountain"),

	("town_12_arena", sf_generate, "none", "none", (0.00, 0.00), (100.00, 100.00), -100.0, "0x00000002200005000005f57b00005885000046bd00006d9c", [], [], "outer_terrain_steppe"),

	("town_16_arena", sf_generate, "none", "none", (0.00, 0.00), (100.00, 100.00), -100.0, "0x000000003000050000042d0d000045dd0000243500004ef7", [], [], "outer_terrain_plain_farmountain"),

	("town_17_arena", sf_generate, "none", "none", (0.00, 0.00), (100.00, 100.00), -100.0, "0x000000003000050000042d0d000045dd0000243500004ef7", [], [], "outer_terrain_plain_farmountain"),

	("town_18_arena", sf_generate, "none", "none", (0.00, 0.00), (100.00, 100.00), -100.0, "0x000000003000050000042d0d000045dd0000243500004ef7", [], [], "outer_terrain_plain_farmountain"),

	("town_19_arena", sf_generate, "none", "none", (0.00, 0.00), (100.00, 100.00), -100.0, "0x00000002200005000005f57b00005885000046bd00006d9c", [], [], "outer_terrain_desert"),

	("town_20_arena", sf_generate, "none", "none", (0.00, 0.00), (100.00, 100.00), -100.0, "0x00000002200005000005f57b00005885000046bd00006d9c", [], [], "outer_terrain_desert"),

	("town_23_arena", sf_generate, "none", "none", (0.00, 0.00), (100.00, 100.00), -100.0, "0x000000003000050000042d0d000045dd0000243500004ef7", [], [], "outer_terrain_plain_farmountain"),

	("town_24_arena", sf_generate, "none", "none", (0.00, 0.00), (100.00, 100.00), -100.0, "0x00000000300005000005194600005b6f000052a900000129", [], [], "outer_terrain_plain_farmountain"),

	("town_25_arena", sf_generate, "none", "none", (0.00, 0.00), (100.00, 100.00), -100.0, "0x000000003000050000042d0d000045dd0000243500004ef7", [], [], "outer_terrain_plain_farmountain"),

	("town_26_arena", sf_generate, "none", "none", (0.00, 0.00), (100.00, 100.00), -100.0, "0x000000003000050000042d0d000045dd0000243500004ef7", [], [], "outer_terrain_plain_farmountain"),

	("town_27_arena", sf_generate, "none", "none", (0.00, 0.00), (100.00, 100.00), -100.0, "0x000000003000050000042d0d000045dd0000243500004ef7", [], [], "outer_terrain_plain_farmountain"),

	("town_30_arena", sf_generate, "none", "none", (0.00, 0.00), (100.00, 100.00), -100.0, "0x000000003000050000042d0d000045dd0000243500004ef7", [], [], "outer_terrain_plain_farmountain"),

	("town_31_arena", sf_generate, "none", "none", (0.00, 0.00), (100.00, 100.00), -100.0, "0x000000003000050000042d0d000045dd0000243500004ef7", [], [], "outer_terrain_plain_farmountain"),

	("town_32_arena", sf_generate, "none", "none", (0.00, 0.00), (100.00, 100.00), -100.0, "0x000000003000050000042d0d000045dd0000243500004ef7", [], [], "outer_terrain_plain_farmountain"),

	("town_33_arena", sf_generate, "none", "none", (0.00, 0.00), (100.00, 100.00), -100.0, "0x000000003000050000042d0d000045dd0000243500004ef7", [], [], "outer_terrain_plain_farmountain"),

	("town_34_arena", sf_generate, "none", "none", (0.00, 0.00), (100.00, 100.00), -100.0, "0x000000003000050000042d0d000045dd0000243500004ef7", [], [], "outer_terrain_plain_farmountain"),

	("town_35_arena", sf_generate, "none", "none", (0.00, 0.00), (100.00, 100.00), -100.0, "0x000000003000050000042d0d000045dd0000243500004ef7", [], [], "outer_terrain_plain_farmountain"),

	("town_36_arena", sf_generate, "none", "none", (0.00, 0.00), (100.00, 100.00), -100.0, "0x00000002200005000005f57b00005885000046bd00006d9c", [], [], "outer_terrain_steppe"),

	("town_38_arena", sf_generate, "none", "none", (0.00, 0.00), (100.00, 100.00), -100.0, "0x00000002200005000005f57b00005885000046bd00006d9c", [], [], "outer_terrain_steppe"),

	("town_40_arena", sf_generate, "none", "none", (0.00, 0.00), (100.00, 100.00), -100.0, "0x00000002200005000005f57b00005885000046bd00006d9c", [], [], "outer_terrain_desert"),

	("town_41_arena", sf_generate, "none", "none", (0.00, 0.00), (100.00, 100.00), -100.0, "0x000000003000050000042d0d000045dd0000243500004ef7", [], [], "outer_terrain_plain_farmountain"),

	("town_42_arena", sf_generate, "none", "none", (0.00, 0.00), (100.00, 100.00), -100.0, "0x000000003000050000042d0d000045dd0000243500004ef7", [], [], "outer_terrain_plain_farmountain"),

	("town_44_arena", sf_generate, "none", "none", (0.00, 0.00), (100.00, 100.00), -100.0, "0x00000002200005000005f57b00005885000046bd00006d9c", [], [], "outer_terrain_steppe"),

	("town_45_arena", sf_generate, "none", "none", (0.00, 0.00), (100.00, 100.00), -100.0, "0x00000002200005000005f57b00005885000046bd00006d9c", [], [], "outer_terrain_steppe"),

	("town_46_arena", sf_generate, "none", "none", (0.00, 0.00), (100.00, 100.00), -100.0, "0x00000002200005000005f57b00005885000046bd00006d9c", [], [], "outer_terrain_desert"),

	("town_47_arena", sf_generate, "none", "none", (0.00, 0.00), (100.00, 100.00), -100.0, "0x00000002200005000005f57b00005885000046bd00006d9c", [], [], "outer_terrain_steppe"),

	("town_48_arena", sf_generate, "none", "none", (0.00, 0.00), (100.00, 100.00), -100.0, "0x00000002200005000005f57b00005885000046bd00006d9c", [], [], "outer_terrain_steppe"),

	("town_49_arena", sf_generate, "none", "none", (0.00, 0.00), (100.00, 100.00), -100.0, "0x00000002200005000005f57b00005885000046bd00006d9c", [], [], "outer_terrain_steppe"),

	("town_50_arena", sf_generate, "none", "none", (0.00, 0.00), (100.00, 100.00), -100.0, "0x00000002200005000005f57b00005885000046bd00006d9c", [], [], "outer_terrain_steppe"),

	("town_51_arena", sf_generate, "none", "none", (0.00, 0.00), (100.00, 100.00), -100.0, "0x00000002200005000005f57b00005885000046bd00006d9c", [], [], "outer_terrain_desert"),

	("town_52_arena", sf_generate, "none", "none", (0.00, 0.00), (100.00, 100.00), -100.0, "0x00000002200005000005f57b00005885000046bd00006d9c", [], [], "outer_terrain_desert"),

	("town_53_arena", sf_generate, "none", "none", (0.00, 0.00), (100.00, 100.00), -100.0, "0x00000002200005000005f57b00005885000046bd00006d9c", [], [], "outer_terrain_desert"),

	("town_54_arena", sf_generate, "none", "none", (0.00, 0.00), (100.00, 100.00), -100.0, "0x00000002200005000005f57b00005885000046bd00006d9c", [], [], "outer_terrain_desert"),

	("town_1_prison", sf_indoors, "interior_prison_j", "bo_interior_prison_j", (-100.00, -100.00), (100.00, 100.00), -100.0, "0", ["exit"], []),

	("town_3_prison", sf_indoors, "interior_prison_j", "bo_interior_prison_j", (-100.00, -100.00), (100.00, 100.00), -100.0, "0", ["exit"], []),

	("town_6_prison", sf_indoors, "interior_prison_j", "bo_interior_prison_j", (-100.00, -100.00), (100.00, 100.00), -100.0, "0", ["exit"], []),

	("town_8_prison", sf_indoors, "interior_prison_j", "bo_interior_prison_j", (-100.00, -100.00), (100.00, 100.00), -100.0, "0", ["exit"], []),

	("town_9_prison", sf_indoors, "interior_prison_j", "bo_interior_prison_j", (-100.00, -100.00), (100.00, 100.00), -100.0, "0", ["exit"], []),

	("town_12_prison", sf_indoors, "interior_prison_n", "bo_interior_prison_n", (-100.00, -100.00), (100.00, 100.00), -100.0, "0", ["exit"], []),

	("town_16_prison", sf_indoors, "interior_prison_n", "bo_interior_prison_n", (-100.00, -100.00), (100.00, 100.00), -100.0, "0", ["exit"], []),

	("town_17_prison", sf_indoors, "interior_prison_n", "bo_interior_prison_n", (-100.00, -100.00), (100.00, 100.00), -100.0, "0", ["exit"], []),

	("town_18_prison", sf_indoors, "interior_prison_n", "bo_interior_prison_n", (-100.00, -100.00), (100.00, 100.00), -100.0, "0", ["exit"], []),

	("town_19_prison", sf_indoors, "interior_prison_n", "bo_interior_prison_n", (-100.00, -100.00), (100.00, 100.00), -100.0, "0", ["exit"], []),

	("town_20_prison", sf_indoors, "interior_prison_n", "bo_interior_prison_n", (-100.00, -100.00), (100.00, 100.00), -100.0, "0", ["exit"], []),

	("town_23_prison", sf_indoors, "interior_prison_k", "bo_interior_prison_k", (-100.00, -100.00), (100.00, 100.00), -100.0, "0", ["exit"], []),

	("town_24_prison", sf_indoors, "interior_prison_k", "bo_interior_prison_k", (-100.00, -100.00), (100.00, 100.00), -100.0, "0", ["exit"], []),

	("town_25_prison", sf_indoors, "interior_prison_k", "bo_interior_prison_k", (-100.00, -100.00), (100.00, 100.00), -100.0, "0", ["exit"], []),

	("town_26_prison", sf_indoors, "interior_prison_k", "bo_interior_prison_k", (-100.00, -100.00), (100.00, 100.00), -100.0, "0", ["exit"], []),

	("town_27_prison", sf_indoors, "interior_prison_k", "bo_interior_prison_k", (-100.00, -100.00), (100.00, 100.00), -100.0, "0", ["exit"], []),

	("town_30_prison", sf_indoors, "interior_prison_k", "bo_interior_prison_k", (-100.00, -100.00), (100.00, 100.00), -100.0, "0", ["exit"], []),

	("town_31_prison", sf_indoors, "interior_prison_o", "bo_interior_prison_o", (-100.00, -100.00), (100.00, 100.00), -100.0, "0", ["exit"], []),

	("town_32_prison", sf_indoors, "interior_prison_o", "bo_interior_prison_o", (-100.00, -100.00), (100.00, 100.00), -100.0, "0", ["exit"], []),

	("town_33_prison", sf_indoors, "interior_prison_o", "bo_interior_prison_o", (-100.00, -100.00), (100.00, 100.00), -100.0, "0", ["exit"], []),

	("town_34_prison", sf_indoors, "interior_prison_o", "bo_interior_prison_o", (-100.00, -100.00), (100.00, 100.00), -100.0, "0", ["exit"], []),

	("town_35_prison", sf_indoors, "interior_prison_o", "bo_interior_prison_o", (-100.00, -100.00), (100.00, 100.00), -100.0, "0", ["exit"], []),

	("town_36_prison", sf_indoors, "interior_prison_o", "bo_interior_prison_o", (-100.00, -100.00), (100.00, 100.00), -100.0, "0", ["exit"], []),

	("town_38_prison", sf_indoors, "interior_prison_o", "bo_interior_prison_o", (-100.00, -100.00), (100.00, 100.00), -100.0, "0", ["exit"], []),

	("town_40_prison", sf_indoors, "interior_prison_o", "bo_interior_prison_o", (-100.00, -100.00), (100.00, 100.00), -100.0, "0", ["exit"], []),

	("town_41_prison", sf_indoors, "dungeon_cell_b", "bo_dungeon_cell_b", (-100.00, -100.00), (100.00, 100.00), -100.0, "0", ["exit"], []),

	("town_42_prison", sf_indoors, "dungeon_cell_b", "bo_dungeon_cell_b", (-100.00, -100.00), (100.00, 100.00), -100.0, "0", ["exit"], []),

	("town_44_prison", sf_indoors, "dungeon_cell_b", "bo_dungeon_cell_b", (-100.00, -100.00), (100.00, 100.00), -100.0, "0", ["exit"], []),

	("town_45_prison", sf_indoors, "dungeon_cell_b", "bo_dungeon_cell_b", (-100.00, -100.00), (100.00, 100.00), -100.0, "0", ["exit"], []),

	("town_46_prison", sf_indoors, "dungeon_cell_b", "bo_dungeon_cell_b", (-100.00, -100.00), (100.00, 100.00), -100.0, "0", ["exit"], []),

	("town_47_prison", sf_indoors, "dungeon_cell_b", "bo_dungeon_cell_b", (-100.00, -100.00), (100.00, 100.00), -100.0, "0", ["exit"], []),

	("town_48_prison", sf_indoors, "dungeon_cell_b", "bo_dungeon_cell_b", (-100.00, -100.00), (100.00, 100.00), -100.0, "0", ["exit"], []),

	("town_49_prison", sf_indoors, "dungeon_cell_b", "bo_dungeon_cell_b", (-100.00, -100.00), (100.00, 100.00), -100.0, "0", ["exit"], []),

	("town_50_prison", sf_indoors, "dungeon_cell_b", "bo_dungeon_cell_b", (-100.00, -100.00), (100.00, 100.00), -100.0, "0", ["exit"], []),

	("town_51_prison", sf_indoors, "dungeon_cell_b", "bo_dungeon_cell_b", (-100.00, -100.00), (100.00, 100.00), -100.0, "0", ["exit"], []),

	("town_52_prison", sf_indoors, "dungeon_cell_b", "bo_dungeon_cell_b", (-100.00, -100.00), (100.00, 100.00), -100.0, "0", ["exit"], []),

	("town_53_prison", sf_indoors, "dungeon_cell_b", "bo_dungeon_cell_b", (-100.00, -100.00), (100.00, 100.00), -100.0, "0", ["exit"], []),

	("town_54_prison", sf_indoors, "dungeon_cell_b", "bo_dungeon_cell_b", (-100.00, -100.00), (100.00, 100.00), -100.0, "0", ["exit"], []),

	("town_1_walls", sf_generate, "none", "none", (0.00, 0.00), (100.00, 100.00), -100.0, "0x00000000b00005000004a92800003aea00006c97000006be", [], [], "outer_terrain_sisterton"),

	("town_3_walls", sf_generate, "none", "none", (0.00, 0.00), (100.00, 100.00), -100.0, "0x000000013003d7e30005053f00003b4e0000146300006e84", [], [], "outer_terrain_beach"),

	("town_6_walls", sf_generate, "none", "none", (0.00, 0.00), (100.00, 100.00), -100.0, "0x0000000030000913400d2348000013980000600500006b66", [], [], "outer_terrain_beach"),

	("town_8_walls", sf_generate, "none", "none", (0.00, 0.00), (100.00, 100.00), -100.0, "0x000000033000124c000acab40000280700000c9f00000ab5", [], [], "outer_terrain_none"),

	("town_9_walls", sf_generate, "none", "none", (0.00, 0.00), (100.00, 100.00), -100.0, "0x00000000300005000005294700007e2b00004b9f00002394", [], [], "outer_terrain_plain"),

	("town_12_walls", sf_generate, "none", "none", (0.00, 0.00), (100.00, 100.00), -100.0, "0x0000000050111563000ba6ee000009af00005bab00003394", [], [], "sea_outer_terrain_2"),

	("town_16_walls", sf_generate, "none", "none", (0.00, 0.00), (100.00, 100.00), -100.0, "0x00000002200005000005f57b00005885000046bd00006d9c", [], [], "sea_outer_terrain_2"),

	("town_17_walls", sf_generate, "none", "none", (0.00, 0.00), (100.00, 100.00), -100.0, "0x000000012002a0b20004992700006e54000007fe00001fd2", [], [], "sea_outer_terrain_2"),

	("town_18_walls", sf_generate, "none", "none", (0.00, 0.00), (100.00, 100.00), -100.0, "0x00000001300010c800054d5c00004af000005d3f00002ca0", [], [], "outer_terrain_plain"),

	("town_19_walls", sf_generate, "none", "none", (0.00, 0.00), (100.00, 100.00), -100.0, "0x0000000050000500000d23480000055e00007ba600002d66", [], [], "outer_terrain_desert"),

	("town_20_walls", sf_generate, "none", "none", (0.00, 0.00), (100.00, 100.00), -100.0, "0x00000a0650001e9a00a505418000581f000028c800000143", [], [], "outer_terrain_desert"),

	("town_23_walls", sf_generate, "none", "none", (0.00, 0.00), (100.00, 100.00), -100.0, "0x00000000300005000008f63b00001d5700005904000031b7", [], [], "sea_outer_terrain_2"),

	("town_24_walls", sf_generate, "none", "none", (0.00, 0.00), (100.00, 100.00), -100.0, "0x00000000300005000009424e00000d2900007e38000038b3", [], [], "outer_terrain_thir_new"),

	("town_25_walls", sf_generate, "none", "none", (0.00, 0.00), (100.00, 100.00), -100.0, "0x00000001300659630003c8f300003ca000006a8900003c89", [], [], "outer_terrain_beach"),

	("town_26_walls", sf_generate, "none", "none", (0.00, 0.00), (100.00, 100.00), -100.0, "0x000000013003d7e30005053f00003b4e0000146300006e84", [], [], "outer_terrain_beach"),

	("town_27_walls", sf_generate, "none", "none", (0.00, 0.00), (100.00, 100.00), -100.0, "0x0000000030000913400d2348000013980000600500006b66", [], [], "outer_terrain_bleach"),

	("town_30_walls", sf_generate, "none", "none", (0.00, 0.00), (100.00, 100.00), -100.0, "0x00000000300b1063000b5edb000042c00000676600001c6b", [], [], "outer_terrain_plain"),

	("town_31_walls", sf_generate, "none", "none", (0.00, 0.00), (100.00, 100.00), -100.0, "0x0000000030015f2b000350d4000011a4000017ee000054af", [], [], "outer_terrain_plain"),

	("town_32_walls", sf_generate, "none", "none", (0.00, 0.00), (100.00, 100.00), -100.0, "0x000000012002a0b20004992700006e54000007fe00001fd2", [], [], "sea_outer_terrain_2"),

	("town_33_walls", sf_generate, "none", "none", (0.00, 0.00), (100.00, 100.00), -100.0, "0x00000000300005000005294700007e2b00004b9f00002394", [], [], "outer_terrain_plain"),

	("town_34_walls", sf_generate, "none", "none", (0.00, 0.00), (100.00, 100.00), -100.0, "0x00000001300659630003c8f300003ca000006a8900003c89", [], [], "outer_terrain_beach"),

	("town_35_walls", sf_generate, "none", "none", (0.00, 0.00), (100.00, 100.00), -100.0, "0x000000013002491600055157000000d20000152a0000611a", [], [], "outer_terrain_plain"),

	("town_36_walls", sf_generate, "none", "none", (0.00, 0.00), (100.00, 100.00), -100.0, "0x00000002300491830004a529000036230000312a00003653", [], [], "outer_terrain_plain"),

	("town_38_walls", sf_generate, "none", "none", (0.00, 0.00), (100.00, 100.00), -100.0, "0x00000002200011af00065192000067110000688300003435", [], [], "outer_terrain_steppe_mountain"),

	("town_40_walls", sf_generate, "none", "none", (0.00, 0.00), (100.00, 100.00), -100.0, "0x0000000050111563000ba6ee000009af00005bab00003394", [], [], "sea_outer_terrain_2"),

	("town_41_walls", sf_generate, "none", "none", (0.00, 0.00), (100.00, 100.00), -100.0, "0x0000000130010e0e0005fd84000011c60000285b00005cbe", [], [], "outer_terrain_plain"),

	("town_42_walls", sf_generate, "none", "none", (0.00, 0.00), (100.00, 100.00), -100.0, "0x00000000300005000005294700007e2b00004b9f00002394", [], [], "outer_terrain_plain"),

	("town_44_walls", sf_generate, "none", "none", (0.00, 0.00), (100.00, 100.00), -100.0, "0x00000002200011af00065192000067110000688300003435", [], [], "outer_terrain_steppe"),

	("town_45_walls", sf_generate, "none", "none", (0.00, 0.00), (100.00, 100.00), -100.0, "0x00000002200011af00065192000067110000688300003435", [], [], "outer_terrain_steppe"),

	("town_46_walls", sf_generate, "none", "none", (0.00, 0.00), (100.00, 100.00), -100.0, "0x000000003000050000085e1900005f5e00005fa700002d1d", [], [], "sea_outer_terrain_2"),

	("town_47_walls", sf_generate, "none", "none", (0.00, 0.00), (100.00, 100.00), -100.0, "0x00000002200011af00065192000067110000688300003435", [], [], "outer_terrain_steppe"),

	("town_48_walls", sf_generate, "none", "none", (0.00, 0.00), (100.00, 100.00), -100.0, "0x00000002200011af00065192000067110000688300003435", [], [], "outer_terrain_steppe"),

	("town_49_walls", sf_generate, "none", "none", (0.00, 0.00), (100.00, 100.00), -100.0, "0x00000002200011af00065192000067110000688300003435", [], [], "outer_terrain_steppe"),

	("town_50_walls", sf_generate, "none", "none", (0.00, 0.00), (100.00, 100.00), -100.0, "0x00000002200011af00065192000067110000688300003435", [], [], "outer_terrain_steppe"),

	("town_51_walls", sf_generate, "none", "none", (0.00, 0.00), (100.00, 100.00), -100.0, "0x00000000300d97e300050d420000482a0000341d00005ecb", [], [], "outer_terrain_plain_farmountain"),

	("town_52_walls", sf_generate, "none", "none", (0.00, 0.00), (100.00, 100.00), -100.0, "0x00000002300491830004a529000036230000312a00003653", [], [], "outer_terrain_plain"),

	("town_53_walls", sf_generate, "none", "none", (0.00, 0.00), (100.00, 100.00), -100.0, "0x00000002300491830004a529000036230000312a00003653", [], [], "outer_terrain_plain"),

	("town_54_walls", sf_generate, "none", "none", (0.00, 0.00), (100.00, 100.00), -100.0, "0x00000002300491830004a529000036230000312a00003653", [], [], "outer_terrain_plain"),

	("town_1_alley", sf_generate, "none", "none", (0.00, 0.00), (100.00, 100.00), -100.0, "0x00000000b00005000004a92800003aea00006c97000006be", [], [], "outer_terrain_sisterton"),

	("town_3_alley", sf_generate, "none", "none", (0.00, 0.00), (100.00, 100.00), -100.0, "0x000000013003d7e30005053f00003b4e0000146300006e84", [], [], "outer_terrain_beach"),

	("town_6_alley", sf_generate, "none", "none", (0.00, 0.00), (100.00, 100.00), -100.0, "0x0000000030000913400d2348000013980000600500006b66", [], [], "outer_terrain_beach"),

	("town_8_alley", sf_generate, "none", "none", (0.00, 0.00), (100.00, 100.00), -100.0, "0x000000033000124c000acab40000280700000c9f00000ab5", [], [], "outer_terrain_none"),

	("town_9_alley", sf_generate, "none", "none", (0.00, 0.00), (100.00, 100.00), -100.0, "0x00000000300005000005294700007e2b00004b9f00002394", [], [], "outer_terrain_plain"),

	("town_12_alley", sf_generate, "none", "none", (0.00, 0.00), (100.00, 100.00), -100.0, "0x0000000050111563000ba6ee000009af00005bab00003394", [], [], "sea_outer_terrain_2"),

	("town_16_alley", sf_generate, "none", "none", (0.00, 0.00), (100.00, 100.00), -100.0, "0x00000002200005000005f57b00005885000046bd00006d9c", [], [], "sea_outer_terrain_2"),

	("town_17_alley", sf_generate, "none", "none", (0.00, 0.00), (100.00, 100.00), -100.0, "0x000000012002a0b20004992700006e54000007fe00001fd2", [], [], "sea_outer_terrain_2"),

	("town_18_alley", sf_generate, "none", "none", (0.00, 0.00), (100.00, 100.00), -100.0, "0x30001d9300031ccb0000156f000048ba0000361c", [], [], "outer_terrain_plain"),

	("town_19_alley", sf_generate, "none", "none", (0.00, 0.00), (100.00, 100.00), -100.0, "0x0000000050000500000d23480000055e00007ba600002d66", [], [], "outer_terrain_desert"),

	("town_20_alley", sf_generate, "none", "none", (0.00, 0.00), (100.00, 100.00), -100.0, "0x00000a0650001e9a00a505418000581f000028c800000143", [], [], "outer_terrain_desert"),

	("town_23_alley", sf_generate, "none", "none", (0.00, 0.00), (100.00, 100.00), -100.0, "0x00000000300005000008f63b00001d5700005904000031b7", [], [], "sea_outer_terrain_2"),

	("town_24_alley", sf_generate, "none", "none", (0.00, 0.00), (100.00, 100.00), -100.0, "0x00000000300005000009424e00000d2900007e38000038b3", [], [], "outer_terrain_thir_new"),

	("town_25_alley", sf_generate, "none", "none", (0.00, 0.00), (100.00, 100.00), -100.0, "0x00000001300659630003c8f300003ca000006a8900003c89", [], [], "outer_terrain_beach"),

	("town_26_alley", sf_generate, "none", "none", (0.00, 0.00), (100.00, 100.00), -100.0, "0x000000013003d7e30005053f00003b4e0000146300006e84", [], [], "outer_terrain_beach"),

	("town_27_alley", sf_generate, "none", "none", (0.00, 0.00), (100.00, 100.00), -100.0, "0x0000000030000913400d2348000013980000600500006b66", [], [], "outer_terrain_beach"),

	("town_30_alley", sf_generate, "none", "none", (0.00, 0.00), (100.00, 100.00), -100.0, "0x00000000300b1063000b5edb000042c00000676600001c6b", [], [], "outer_terrain_plain"),

	("town_31_alley", sf_generate, "none", "none", (0.00, 0.00), (100.00, 100.00), -100.0, "0x00000002200005000005f57b00005885000046bd00006d9c", [], [], "outer_terrain_beach"),

	("town_32_alley", sf_generate, "none", "none", (0.00, 0.00), (100.00, 100.00), -100.0, "0x000000012002a0b20004992700006e54000007fe00001fd2", [], [], "sea_outer_terrain_2"),

	("town_33_alley", sf_generate, "none", "none", (0.00, 0.00), (100.00, 100.00), -100.0, "0x00000000300005000005294700007e2b00004b9f00002394", [], [], "outer_terrain_plain"),

	("town_34_alley", sf_generate, "none", "none", (0.00, 0.00), (100.00, 100.00), -100.0, "0x00000001300659630003c8f300003ca000006a8900003c89", [], [], "outer_terrain_beach"),

	("town_35_alley", sf_generate, "none", "none", (0.00, 0.00), (100.00, 100.00), -100.0, "0x3000148000025896000074e600006c260000125a", [], [], "outer_terrain_plain"),

	("town_36_alley", sf_generate, "none", "none", (0.00, 0.00), (100.00, 100.00), -100.0, "0x00000002300491830004a529000036230000312a00003653", [], [], "outer_terrain_plain"),

	("town_38_alley", sf_generate, "none", "none", (0.00, 0.00), (100.00, 100.00), -100.0, "0x0000000020045abc000308c4000029d9000033bd000009b9", [], [], "outer_terrain_steppe_mountain"),

	("town_40_alley", sf_generate, "none", "none", (0.00, 0.00), (100.00, 100.00), -100.0, "0x0000000050111563000ba6ee000009af00005bab00003394", [], [], "sea_outer_terrain_2"),

	("town_41_alley", sf_generate, "none", "none", (0.00, 0.00), (100.00, 100.00), -100.0, "0x0000000130010e0e0005fd84000011c60000285b00005cbe", [], [], "outer_terrain_plain"),

	("town_42_alley", sf_generate, "none", "none", (0.00, 0.00), (100.00, 100.00), -100.0, "0x00000000300005000005294700007e2b00004b9f00002394", [], [], "outer_terrain_plain"),

	("town_44_alley", sf_generate, "none", "none", (0.00, 0.00), (100.00, 100.00), -100.0, "0x00000000200016da000364d9000060f500007591000064e7", [], [], "outer_terrain_steppe"),

	("town_45_alley", sf_generate, "none", "none", (0.00, 0.00), (100.00, 100.00), -100.0, "0x0000000020049cbd00025896000048e90000164400002b3f", [], [], "outer_terrain_steppe"),

	("town_46_alley", sf_generate, "none", "none", (0.00, 0.00), (100.00, 100.00), -100.0, "0x000000003000050000085e1900005f5e00005fa700002d1d", [], [], "sea_outer_terrain_2"),

	("town_47_alley", sf_generate, "none", "none", (0.00, 0.00), (100.00, 100.00), -100.0, "0x0000000020000500000aaa1000000a4500006d740000437a", [], [], "outer_terrain_steppe"),

	("town_48_alley", sf_generate, "none", "none", (0.00, 0.00), (100.00, 100.00), -100.0, "0x0000000020049cbd00025896000048e90000164400002b3f", [], [], "outer_terrain_steppe"),

	("town_49_alley", sf_generate, "none", "none", (0.00, 0.00), (100.00, 100.00), -100.0, "0x0000000020049cbd00025896000048e90000164400002b3f", [], [], "outer_terrain_steppe"),

	("town_50_alley", sf_generate, "none", "none", (0.00, 0.00), (100.00, 100.00), -100.0, "0x0000000020049cbd00025896000048e90000164400002b3f", [], [], "outer_terrain_steppe"),

	("town_51_alley", sf_generate, "none", "none", (0.00, 0.00), (100.00, 100.00), -100.0, "0x00000000300d97e300050d420000482a0000341d00005ecb", [], [], "outer_terrain_plain_farmountain"),

	("town_52_alley", sf_generate, "none", "none", (0.00, 0.00), (100.00, 100.00), -100.0, "0x00000002300491830004a529000036230000312a00003653", [], [], "outer_terrain_plain"),

	("town_53_alley", sf_generate, "none", "none", (0.00, 0.00), (100.00, 100.00), -100.0, "0x00000002300491830004a529000036230000312a00003653", [], [], "outer_terrain_plain"),

	("town_54_alley", sf_generate, "none", "none", (0.00, 0.00), (100.00, 100.00), -100.0, "0x00000002300491830004a529000036230000312a00003653", [], [], "outer_terrain_plain"),

	("castle_1_exterior", sf_generate, "none", "none", (0.00, 0.00), (100.00, 100.00), -100.0, "0x30054da28004050000005a76800022aa00002e3b", [], [], "outer_terrain_castle_9"),

	("castle_1_interior", sf_indoors, "interior_castle_e", "bo_interior_castle_e", (-100.00, -100.00), (100.00, 100.00), -100.0, "0", ["exit"], ["castle_1_seneschal"]),

	("castle_1_prison", sf_indoors, "interior_prison_e", "bo_interior_prison_e", (-100.00, -100.00), (100.00, 100.00), -100.0, "0", [], []),

	("castle_2_exterior", sf_generate, "none", "none", (0.00, 0.00), (100.00, 100.00), -100.0, "0xa00363638005c16d00003c82000037e000002303", [], [], "outer_terrain_plain"),

	("castle_2_interior", sf_indoors, "interior_castle_v", "bo_interior_castle_v", (-100.00, -100.00), (100.00, 100.00), -100.0, "0", ["exit"], ["castle_2_seneschal"]),

	("castle_2_prison", sf_indoors, "interior_prison_e", "bo_interior_prison_e", (-100.00, -100.00), (100.00, 100.00), -100.0, "0", [], []),

	("castle_3_exterior", sf_generate, "none", "none", (0.00, 0.00), (100.00, 100.00), -100.0, "0x0000000030044e900003dd02000077b20000400100005697", [], [], "outer_terrain_plain"),

	("castle_3_interior", sf_indoors, "interior_castle_j", "bo_interior_castle_j", (-100.00, -100.00), (100.00, 100.00), -100.0, "0", ["exit"], ["castle_3_seneschal"]),

	("castle_3_prison", sf_indoors, "interior_prison_e", "bo_interior_prison_e", (-100.00, -100.00), (100.00, 100.00), -100.0, "0", [], []),

	("castle_4_exterior", sf_generate, "none", "none", (0.00, 0.00), (100.00, 100.00), -100.0, "0x0000000030044e900003dd02000077b20000400100005697", [], [], "outer_terrain_castle_9"),

	("castle_4_interior", sf_indoors, "interior_castle_j", "bo_interior_castle_j", (-100.00, -100.00), (100.00, 100.00), -100.0, "0", ["exit"], ["castle_4_seneschal"]),

	("castle_4_prison", sf_indoors, "interior_prison_i", "bo_interior_prison_i", (-100.00, -100.00), (100.00, 100.00), -100.0, "0", [], []),

	("castle_5_exterior", sf_generate, "none", "none", (0.00, 0.00), (100.00, 100.00), -100.0, "0x0000000230011ab20005d57800003a2600004b7a000071ef", [], [], "outer_terrain_castle_9"),

	("castle_5_interior", sf_indoors, "interior_castle_v", "bo_interior_castle_v", (-100.00, -100.00), (100.00, 100.00), -100.0, "0", ["exit"], ["castle_5_seneschal"]),

	("castle_5_prison", sf_indoors, "interior_prison_e", "bo_interior_prison_e", (-100.00, -100.00), (100.00, 100.00), -100.0, "0", [], []),

	("castle_6_exterior", sf_generate, "none", "none", (0.00, 0.00), (100.00, 100.00), -100.0, "0xa00363638005c16d00003c82000037e000002303", [], [], "outer_terrain_plain"),

	("castle_6_interior", sf_indoors, "white_interior_scene_basic", "bo_interior_castle_n", (-100.00, -100.00), (100.00, 100.00), -100.0, "0", ["exit"], ["castle_6_seneschal"]),

	("castle_6_prison", sf_indoors, "interior_prison_e", "bo_interior_prison_e", (-100.00, -100.00), (100.00, 100.00), -100.0, "0", [], []),

	("castle_7_exterior", sf_generate, "none", "none", (0.00, 0.00), (100.00, 100.00), -100.0, "0x00000000300789b200025896000035260000064a00003382", [], [], "outer_terrain_plain"),

	("castle_7_interior", sf_indoors, "interior_castle_v", "bo_interior_castle_v", (-100.00, -100.00), (100.00, 100.00), -100.0, "0", ["exit"], ["castle_7_seneschal"]),

	("castle_7_prison", sf_indoors, "interior_prison_e", "bo_interior_prison_e", (-100.00, -100.00), (100.00, 100.00), -100.0, "0", [], []),

	("castle_8_exterior", sf_generate, "none", "none", (0.00, 0.00), (100.00, 100.00), -100.0, "0x0000000030000500000b32cb00004a2700000f0b00005ba7", [], [], "outer_terrain_plain"),

	("castle_8_interior", sf_indoors, "interior_castle_b", "bo_interior_castle_b", (-100.00, -100.00), (100.00, 100.00), -100.0, "0", ["exit"], ["castle_8_seneschal"]),

	("castle_8_prison", sf_indoors, "interior_prison_e", "bo_interior_prison_e", (-100.00, -100.00), (100.00, 100.00), -100.0, "0", [], []),

	("castle_9_exterior", sf_generate, "none", "none", (0.00, 0.00), (100.00, 100.00), -100.0, "0x0000000020000a63000806030000537900001eba00001f25", [], [], "outer_terrain_steppe"),

	("castle_9_interior", sf_indoors, "dungeon_cell_a", "bo_dungeon_cell_a", (-100.00, -100.00), (100.00, 100.00), -100.0, "0", ["exit"], ["castle_9_seneschal"]),

	("castle_9_prison", sf_indoors, "interior_prison_e", "bo_interior_prison_e", (-100.00, -100.00), (100.00, 100.00), -100.0, "0", [], []),

	("castle_10_exterior", sf_generate, "none", "none", (0.00, 0.00), (100.00, 100.00), -100.0, "0x000000023007b23200049d2a00003c37000040ef000037cd", [], [], "outer_terrain_plain_farmountain"),

	("castle_10_interior", sf_indoors, "interior_castle_k", "bo_interior_castle_k", (-100.00, -100.00), (100.00, 100.00), -100.0, "0", ["exit"], ["castle_10_seneschal"]),

	("castle_10_prison", sf_indoors, "interior_prison_e", "bo_interior_prison_e", (-100.00, -100.00), (100.00, 100.00), -100.0, "0", [], []),

	("castle_11_exterior", sf_generate, "none", "none", (0.00, 0.00), (100.00, 100.00), -100.0, "0x00000000300005000008f63b00001d5700005904000031b7", [], [], "sea_outer_terrain_2"),

	("castle_11_interior", sf_indoors, "interior_castle_v", "bo_interior_castle_v", (-100.00, -100.00), (100.00, 100.00), -100.0, "0", ["exit"], ["castle_11_seneschal"]),

	("castle_11_prison", sf_indoors, "interior_prison_e", "bo_interior_prison_e", (-100.00, -100.00), (100.00, 100.00), -100.0, "0", [], []),

	("castle_12_exterior", sf_generate, "none", "none", (0.00, 0.00), (100.00, 100.00), -100.0, "0x0000000030044e900003dd02000077b20000400100005697", [], [], "outer_terrain_plain"),

	("castle_12_interior", sf_indoors, "interior_castle_v", "bo_interior_castle_v", (-100.00, -100.00), (100.00, 100.00), -100.0, "0", ["exit"], ["castle_12_seneschal"]),

	("castle_12_prison", sf_indoors, "interior_prison_e", "bo_interior_prison_e", (-100.00, -100.00), (100.00, 100.00), -100.0, "0", [], []),

	("castle_13_exterior", sf_generate, "none", "none", (0.00, 0.00), (100.00, 100.00), -100.0, "0x0000000230054f630005fd820000222a00003de000005f00", [], [], "outer_terrain_plain"),

	("castle_13_interior", sf_indoors, "interior_castle_e", "bo_interior_castle_e", (-100.00, -100.00), (100.00, 100.00), -100.0, "0", ["exit"], ["castle_13_seneschal"]),

	("castle_13_prison", sf_indoors, "interior_prison_e", "bo_interior_prison_e", (-100.00, -100.00), (100.00, 100.00), -100.0, "0", [], []),

	("castle_14_exterior", sf_generate, "none", "none", (0.00, 0.00), (100.00, 100.00), -100.0, "0x000000023007a3b20005795e0000706d0000381800000bbc", [], [], "outer_terrain_castle_9"),

	("castle_14_interior", sf_indoors, "interior_castle_j", "bo_interior_castle_j", (-100.00, -100.00), (100.00, 100.00), -100.0, "0", ["exit"], ["castle_14_seneschal"]),

	("castle_14_prison", sf_indoors, "interior_prison_e", "bo_interior_prison_e", (-100.00, -100.00), (100.00, 100.00), -100.0, "0", [], []),

	("castle_15_exterior", sf_generate, "none", "none", (0.00, 0.00), (100.00, 100.00), -100.0, "0x0000000230054f630005fd820000222a00003de000005f00", [], [], "outer_terrain_castle_9"),

	("castle_15_interior", sf_indoors, "interior_castle_a", "bo_interior_castle_a", (-100.00, -100.00), (100.00, 100.00), -100.0, "0", ["exit"], ["castle_15_seneschal"]),

	("castle_15_prison", sf_indoors, "interior_prison_e", "bo_interior_prison_e", (-100.00, -100.00), (100.00, 100.00), -100.0, "0", [], []),

	("castle_16_exterior", sf_generate, "none", "none", (0.00, 0.00), (100.00, 100.00), -100.0, "0x0000000230011ab20005d57800003a2600004b7a000071ef", [], [], "outer_terrain_castle_9"),

	("castle_16_interior", sf_indoors, "interior_castle_v", "bo_interior_castle_v", (-100.00, -100.00), (100.00, 100.00), -100.0, "0", ["exit"], ["castle_16_seneschal"]),

	("castle_16_prison", sf_indoors, "interior_prison_e", "bo_interior_prison_e", (-100.00, -100.00), (100.00, 100.00), -100.0, "0", [], []),

	("castle_17_exterior", sf_generate, "none", "none", (0.00, 0.00), (100.00, 100.00), -100.0, "0x00000000b00037630002308c00000c9400005d4c00000f3a", [], [], "outer_terrain_plain"),

	("castle_17_interior", sf_indoors, "interior_castle_b", "bo_interior_castle_b", (-100.00, -100.00), (100.00, 100.00), -100.0, "0", ["exit"], ["castle_17_seneschal"]),

	("castle_17_prison", sf_indoors, "interior_prison_e", "bo_interior_prison_e", (-100.00, -100.00), (100.00, 100.00), -100.0, "0", [], []),

	("castle_18_exterior", sf_generate, "none", "none", (0.00, 0.00), (100.00, 100.00), -100.0, "0x0000000030044e900003dd02000077b20000400100005697", [], [], "outer_terrain_plain"),

	("castle_18_interior", sf_indoors, "interior_castle_v", "bo_interior_castle_v", (-100.00, -100.00), (100.00, 100.00), -100.0, "0", ["exit"], ["castle_18_seneschal"]),

	("castle_18_prison", sf_indoors, "interior_prison_e", "bo_interior_prison_e", (-100.00, -100.00), (100.00, 100.00), -100.0, "0", [], []),

	("castle_19_exterior", sf_generate, "none", "none", (0.00, 0.00), (100.00, 100.00), -100.0, "0x0000000331e7879a0005f57d00006f4600007c0400001e95", [], [], "outer_terrain_town_thir_1"),

	("castle_19_interior", sf_indoors, "interior_castle_a", "bo_interior_castle_a", (-100.00, -100.00), (100.00, 100.00), -100.0, "0", ["exit"], ["castle_19_seneschal"]),

	("castle_19_prison", sf_indoors, "interior_prison_e", "bo_interior_prison_e", (-100.00, -100.00), (100.00, 100.00), -100.0, "0", [], []),

	("castle_20_exterior", sf_generate, "none", "none", (0.00, 0.00), (100.00, 100.00), -100.0, "0x00000000b009723200059d6800005f4f0000757f000069cd", [], [], "outer_terrain_plain"),

	("castle_20_interior", sf_indoors, "interior_castle_b", "bo_interior_castle_b", (-100.00, -100.00), (100.00, 100.00), -100.0, "0", ["exit"], ["castle_20_seneschal"]),

	("castle_20_prison", sf_indoors, "interior_prison_e", "bo_interior_prison_e", (-100.00, -100.00), (100.00, 100.00), -100.0, "0", [], []),

	("castle_21_exterior", sf_generate, "none", "none", (0.00, 0.00), (100.00, 100.00), -100.0, "0x0000000230011ab20005d57800003a2600004b7a000071ef", [], [], "outer_terrain_castle_9"),

	("castle_21_interior", sf_indoors, "interior_castle_v", "bo_interior_castle_v", (-100.00, -100.00), (100.00, 100.00), -100.0, "0", ["exit"], ["castle_21_seneschal"]),

	("castle_21_prison", sf_indoors, "interior_prison_e", "bo_interior_prison_e", (-100.00, -100.00), (100.00, 100.00), -100.0, "0", [], []),

	("castle_22_exterior", sf_generate, "none", "none", (0.00, 0.00), (100.00, 100.00), -100.0, "0x0000000230084fac00057d5f00002ba900004a7a000060be", [], [], "outer_terrain_plain_farmountain"),

	("castle_22_interior", sf_indoors, "interior_castle_k", "bo_interior_castle_k", (-100.00, -100.00), (100.00, 100.00), -100.0, "0", ["exit"], ["castle_22_seneschal"]),

	("castle_22_prison", sf_indoors, "interior_prison_e", "bo_interior_prison_e", (-100.00, -100.00), (100.00, 100.00), -100.0, "0", [], []),

	("castle_23_exterior", sf_generate, "none", "none", (0.00, 0.00), (100.00, 100.00), -100.0, "0x0000000040000c910003e8fa0000538900003e9e00005301", [], [], "outer_terrain_plain_farmountain"),

	("castle_23_interior", sf_indoors, "interior_castle_v", "bo_interior_castle_v", (-100.00, -100.00), (100.00, 100.00), -100.0, "0", ["exit"], ["castle_23_seneschal"]),

	("castle_23_prison", sf_indoors, "interior_prison_e", "bo_interior_prison_e", (-100.00, -100.00), (100.00, 100.00), -100.0, "0", [], []),

	("castle_24_exterior", sf_generate, "none", "none", (0.00, 0.00), (100.00, 100.00), -100.0, "0x0000000130021f63000721ca000055be000079d90000156d", [], [], "outer_terrain_plain_farmountain"),

	("castle_24_interior", sf_indoors, "dungeon_cell_b", "bo_dungeon_cell_b", (-100.00, -100.00), (100.00, 100.00), -100.0, "0", ["exit"], ["castle_24_seneschal"]),

	("castle_24_prison", sf_indoors, "interior_prison_e", "bo_interior_prison_e", (-100.00, -100.00), (100.00, 100.00), -100.0, "0", [], []),

	("castle_25_exterior", sf_generate, "none", "none", (0.00, 0.00), (100.00, 100.00), -100.0, "0x000000013004e0a600061989000053d50000749800005f64", [], [], "outer_terrain_plain_farmountain"),

	("castle_25_interior", sf_indoors, "interior_castle_e", "bo_interior_castle_e", (-100.00, -100.00), (100.00, 100.00), -100.0, "0", ["exit"], ["castle_25_seneschal"]),

	("castle_25_prison", sf_indoors, "interior_prison_e", "bo_interior_prison_e", (-100.00, -100.00), (100.00, 100.00), -100.0, "0", [], []),

	("castle_26_exterior", sf_generate, "none", "none", (0.00, 0.00), (100.00, 100.00), -100.0, "0x0000000230011ab20005d57800003a2600004b7a000071ef", [], [], "outer_terrain_castle_9"),

	("castle_26_interior", sf_indoors, "interior_castle_v", "bo_interior_castle_v", (-100.00, -100.00), (100.00, 100.00), -100.0, "0", ["exit"], ["castle_26_seneschal"]),

	("castle_26_prison", sf_indoors, "interior_prison_e", "bo_interior_prison_e", (-100.00, -100.00), (100.00, 100.00), -100.0, "0", [], []),

	("castle_27_exterior", sf_generate, "none", "none", (0.00, 0.00), (100.00, 100.00), -100.0, "0x000000013007b23200070dbc000041de00000c4900003cfc", [], [], "outer_terrain_plain"),

	("castle_27_interior", sf_indoors, "interior_castle_b", "bo_interior_castle_b", (-100.00, -100.00), (100.00, 100.00), -100.0, "0", ["exit"], ["castle_27_seneschal"]),

	("castle_27_prison", sf_indoors, "interior_prison_e", "bo_interior_prison_e", (-100.00, -100.00), (100.00, 100.00), -100.0, "0", [], []),

	("castle_28_exterior", sf_generate, "none", "none", (0.00, 0.00), (100.00, 100.00), -100.0, "0x000000013007b232000715c50000084c00001b5b000018ec", [], [], "outer_terrain_castle_9"),

	("castle_28_interior", sf_indoors, "interior_castle_v", "bo_interior_castle_v", (-100.00, -100.00), (100.00, 100.00), -100.0, "0", ["exit"], ["castle_28_seneschal"]),

	("castle_28_prison", sf_indoors, "interior_prison_e", "bo_interior_prison_e", (-100.00, -100.00), (100.00, 100.00), -100.0, "0", [], []),

	("castle_29_exterior", sf_generate, "none", "none", (0.00, 0.00), (100.00, 100.00), -100.0, "0x0000000130010e0e0005fd84000011c60000285b00005cbe", [], [], "outer_terrain_plain"),

	("castle_29_interior", sf_indoors, "castle_h_interior_a", "bo_castle_h_interior_a", (-100.00, -100.00), (100.00, 100.00), -100.0, "0", ["exit"], ["castle_29_seneschal"]),

	("castle_29_prison", sf_indoors, "interior_prison_e", "bo_interior_prison_e", (-100.00, -100.00), (100.00, 100.00), -100.0, "0", [], []),

	("castle_30_exterior", sf_generate, "none", "none", (0.00, 0.00), (100.00, 100.00), -100.0, "0x0000000220035e32000611840000147f00003dac00000660", [], [], "outer_terrain_desert"),

	("castle_30_interior", sf_indoors, "arabian_interior_keep_b", "bo_arabian_interior_keep_b", (-100.00, -100.00), (100.00, 100.00), -100.0, "0", ["exit"], ["castle_30_seneschal"]),

	("castle_30_prison", sf_indoors, "interior_prison_e", "bo_interior_prison_e", (-100.00, -100.00), (100.00, 100.00), -100.0, "0", [], []),

	("castle_31_exterior", sf_generate, "none", "none", (0.00, 0.00), (100.00, 100.00), -100.0, "0x00000000b009723200059d6800005f4f0000757f000069cd", [], [], "outer_terrain_plain"),

	("castle_31_interior", sf_indoors, "interior_castle_b", "bo_interior_castle_b", (-100.00, -100.00), (100.00, 100.00), -100.0, "0", ["exit"], ["castle_31_seneschal"]),

	("castle_31_prison", sf_indoors, "interior_prison_d", "bo_interior_prison_d", (-100.00, -100.00), (100.00, 100.00), -100.0, "0", [], []),

	("castle_32_exterior", sf_generate, "none", "none", (0.00, 0.00), (100.00, 100.00), -100.0, "0x0000000230084fac00057d5f00002ba900004a7a000060be", [], [], "outer_terrain_plain_farmountain"),

	("castle_32_interior", sf_indoors, "interior_castle_g", "bo_interior_castle_g", (-100.00, -100.00), (100.00, 100.00), -100.0, "0", ["exit"], ["castle_32_seneschal"]),

	("castle_32_prison", sf_indoors, "interior_prison_d", "bo_interior_prison_d", (-100.00, -100.00), (100.00, 100.00), -100.0, "0", [], []),

	("castle_33_exterior", sf_generate, "none", "none", (0.00, 0.00), (100.00, 100.00), -100.0, "0x0000000230029cb2000709c200003c9500004b9b00002f4d", [], [], "outer_terrain_castle_9"),

	("castle_33_interior", sf_indoors, "interior_castle_v", "bo_interior_castle_v", (-100.00, -100.00), (100.00, 100.00), -100.0, "0", ["exit"], ["castle_33_seneschal"]),

	("castle_33_prison", sf_indoors, "interior_prison_d", "bo_interior_prison_d", (-100.00, -100.00), (100.00, 100.00), -100.0, "0", [], []),

	("castle_34_exterior", sf_generate, "none", "none", (0.00, 0.00), (100.00, 100.00), -100.0, "0x000000003012b732000729ca0000370d0000671200004f47", [], [], "outer_terrain_plain_farmountain"),

	("castle_34_interior", sf_indoors, "white_interior_scene_basic", "bo_interior_castle_n", (-100.00, -100.00), (100.00, 100.00), -100.0, "0", ["exit"], ["castle_34_seneschal"]),

	("castle_34_prison", sf_indoors, "interior_prison_e", "bo_interior_prison_e", (-100.00, -100.00), (100.00, 100.00), -100.0, "0", [], []),

	("castle_35_exterior", sf_generate, "none", "none", (0.00, 0.00), (100.00, 100.00), -100.0, "0x0000000130031be30006f9bc00000aae00000fb80000243f", [], [], "outer_terrain_plain_farmountain"),

	("castle_35_interior", sf_indoors, "interior_castle_v", "bo_interior_castle_v", (-100.00, -100.00), (100.00, 100.00), -100.0, "0", ["exit"], ["castle_35_seneschal"]),

	("castle_35_prison", sf_indoors, "interior_prison_d", "bo_interior_prison_d", (-100.00, -100.00), (100.00, 100.00), -100.0, "0", [], []),

	("castle_36_exterior", sf_generate, "none", "none", (0.00, 0.00), (100.00, 100.00), -100.0, "0x000000013007b2630005695c00001ebe0000028e00007e37", [], [], "outer_terrain_castle_9"),

	("castle_36_interior", sf_indoors, "interior_castle_b", "bo_interior_castle_b", (-100.00, -100.00), (100.00, 100.00), -100.0, "0", ["exit"], ["castle_36_seneschal"]),

	("castle_36_prison", sf_indoors, "interior_prison_d", "bo_interior_prison_d", (-100.00, -100.00), (100.00, 100.00), -100.0, "0", [], []),

	("castle_37_exterior", sf_generate, "none", "none", (0.00, 0.00), (100.00, 100.00), -100.0, "0x0000000130010e0e0005fd84000011c60000285b00005cbe", [], [], "outer_terrain_plain"),

	("castle_37_interior", sf_indoors, "interior_castle_e", "bo_interior_castle_e", (-100.00, -100.00), (100.00, 100.00), -100.0, "0", ["exit"], ["castle_37_seneschal"]),

	("castle_37_prison", sf_indoors, "interior_prison_d", "bo_interior_prison_d", (-100.00, -100.00), (100.00, 100.00), -100.0, "0", [], []),

	("castle_39_exterior", sf_generate, "none", "none", (0.00, 0.00), (100.00, 100.00), -100.0, "0x0000000230011ab20005d57800003a2600004b7a000071ef", [], [], "outer_terrain_castle_9"),

	("castle_39_interior", sf_indoors, "interior_castle_v", "bo_interior_castle_v", (-100.00, -100.00), (100.00, 100.00), -100.0, "0", ["exit"], ["castle_39_seneschal"]),

	("castle_39_prison", sf_indoors, "interior_prison_d", "bo_interior_prison_d", (-100.00, -100.00), (100.00, 100.00), -100.0, "0", [], []),

	("castle_40_exterior", sf_generate, "none", "none", (0.00, 0.00), (100.00, 100.00), -100.0, "0x000000012007985300055550000064d500005c060000759e", [], [], "outer_terrain_steppe"),

	("castle_40_interior", sf_indoors, "arabian_interior_keep_b", "bo_arabian_interior_keep_b", (-100.00, -100.00), (100.00, 100.00), -100.0, "0", ["exit"], ["castle_40_seneschal"]),

	("castle_40_prison", sf_indoors, "interior_prison_i", "bo_interior_prison_i", (-100.00, -100.00), (100.00, 100.00), -100.0, "0", [], []),

	("castle_41_exterior", sf_generate, "none", "none", (0.00, 0.00), (100.00, 100.00), -100.0, "0x000000005a0932320004cd3000004e7d00007d6e00006c58", [], [], "outer_terrain_desert"),

	("castle_41_interior", sf_indoors, "arabian_interior_keep_b", "bo_arabian_interior_keep_b", (-100.00, -100.00), (100.00, 100.00), -100.0, "0", ["exit"], ["castle_41_seneschal"]),

	("castle_41_prison", sf_indoors, "interior_prison_i", "bo_interior_prison_i", (-100.00, -100.00), (100.00, 100.00), -100.0, "0", [], []),

	("castle_42_exterior", sf_generate, "none", "none", (0.00, 0.00), (100.00, 100.00), -100.0, "0x000000005a039fb20005114400004f690000467a00004400", [], [], "outer_terrain_desert"),

	("castle_42_interior", sf_indoors, "arabian_interior_keep_b", "bo_arabian_interior_keep_b", (-100.00, -100.00), (100.00, 100.00), -100.0, "0", ["exit"], ["castle_42_seneschal"]),

	("castle_42_prison", sf_indoors, "interior_prison_i", "bo_interior_prison_i", (-100.00, -100.00), (100.00, 100.00), -100.0, "0", [], []),

	("castle_43_exterior", sf_generate, "none", "none", (0.00, 0.00), (100.00, 100.00), -100.0, "0x000000005a0ae6480004952400003e1800005d9f00002c7e", [], [], "outer_terrain_desert"),

	("castle_43_interior", sf_indoors, "arabian_interior_keep_b", "bo_arabian_interior_keep_b", (-100.00, -100.00), (100.00, 100.00), -100.0, "0", ["exit"], ["castle_43_seneschal"]),

	("castle_43_prison", sf_indoors, "interior_prison_i", "bo_interior_prison_i", (-100.00, -100.00), (100.00, 100.00), -100.0, "0", [], []),

	("castle_44_exterior", sf_generate, "none", "none", (0.00, 0.00), (100.00, 100.00), -100.0, "0x0000000053e3b2320004ed3800001eb400006277000068ea", [], [], "outer_terrain_desert"),

	("castle_44_interior", sf_indoors, "arabian_interior_keep_b", "bo_arabian_interior_keep_b", (-100.00, -100.00), (100.00, 100.00), -100.0, "0", ["exit"], ["castle_44_seneschal"]),

	("castle_44_prison", sf_indoors, "interior_prison_i", "bo_interior_prison_i", (-100.00, -100.00), (100.00, 100.00), -100.0, "0", [], []),

	("castle_45_exterior", sf_generate, "none", "none", (0.00, 0.00), (100.00, 100.00), -100.0, "0x0000000254c2ec0000042509000016da0000017200000ed3", [], [], "outer_terrain_desert"),

	("castle_45_interior", sf_indoors, "arabian_interior_keep_b", "bo_arabian_interior_keep_b", (-100.00, -100.00), (100.00, 100.00), -100.0, "0", ["exit"], ["castle_45_seneschal"]),

	("castle_45_prison", sf_indoors, "interior_prison_i", "bo_interior_prison_i", (-100.00, -100.00), (100.00, 100.00), -100.0, "0", [], []),

	("castle_46_exterior", sf_generate, "none", "none", (0.00, 0.00), (100.00, 100.00), -100.0, "0x0000000050000600000a769f00000d160000612a0000584f", [], [], "outer_terrain_desert"),

	("castle_46_interior", sf_indoors, "arabian_interior_keep_b", "bo_arabian_interior_keep_b", (-100.00, -100.00), (100.00, 100.00), -100.0, "0", ["exit"], ["castle_46_seneschal"]),

	("castle_46_prison", sf_indoors, "interior_prison_i", "bo_interior_prison_i", (-100.00, -100.00), (100.00, 100.00), -100.0, "0", [], []),

	("castle_47_exterior", sf_generate, "none", "none", (0.00, 0.00), (100.00, 100.00), -100.0, "0x000000005a07b2320002b8ad000036c80000409d00001987", [], [], "outer_terrain_desert"),

	("castle_47_interior", sf_indoors, "arabian_interior_keep_b", "bo_arabian_interior_keep_b", (-100.00, -100.00), (100.00, 100.00), -100.0, "0", ["exit"], ["castle_47_seneschal"]),

	("castle_47_prison", sf_indoors, "interior_prison_i", "bo_interior_prison_i", (-100.00, -100.00), (100.00, 100.00), -100.0, "0", [], []),

	("castle_48_exterior", sf_generate, "none", "none", (0.00, 0.00), (100.00, 100.00), -100.0, "0x0000000056c3da200003a0e6000002a900002d7a0000409e", [], [], "outer_terrain_desert"),

	("castle_48_interior", sf_indoors, "arabian_interior_keep_b", "bo_arabian_interior_keep_b", (-100.00, -100.00), (100.00, 100.00), -100.0, "0", ["exit"], ["castle_48_seneschal"]),

	("castle_48_prison", sf_indoors, "interior_prison_i", "bo_interior_prison_i", (-100.00, -100.00), (100.00, 100.00), -100.0, "0", [], []),

	("castle_49_exterior", sf_generate, "none", "none", (0.00, 0.00), (100.00, 100.00), -100.0, "0x000000005a07b2320002b8ad000036c80000409d00001987", [], [], "outer_terrain_desert"),

	("castle_49_interior", sf_indoors, "arabian_interior_keep_b", "bo_arabian_interior_keep_b", (-100.00, -100.00), (100.00, 100.00), -100.0, "0", ["exit"], ["castle_49_seneschal"]),

	("castle_49_prison", sf_indoors, "interior_prison_i", "bo_interior_prison_i", (-100.00, -100.00), (100.00, 100.00), -100.0, "0", [], []),

	("castle_50_exterior", sf_generate, "none", "none", (0.00, 0.00), (100.00, 100.00), -100.0, "0x000000012007985300055550000064d500005c060000759e", [], [], "outer_terrain_steppe"),

	("castle_50_interior", sf_indoors, "arabian_interior_keep_b", "bo_arabian_interior_keep_b", (-100.00, -100.00), (100.00, 100.00), -100.0, "0", ["exit"], ["castle_50_seneschal"]),

	("castle_50_prison", sf_indoors, "interior_prison_i", "bo_interior_prison_i", (-100.00, -100.00), (100.00, 100.00), -100.0, "0", [], []),

	("castle_51_exterior", sf_generate, "none", "none", (0.00, 0.00), (100.00, 100.00), -100.0, "0x00000001300389800003a4ea000058340000637a0000399b", [], [], "outer_terrain_plain"),

	("castle_51_interior", sf_indoors, "interior_castle_v", "bo_interior_castle_v", (-100.00, -100.00), (100.00, 100.00), -100.0, "0", ["exit"], ["castle_51_seneschal"]),

	("castle_51_prison", sf_indoors, "interior_prison_i", "bo_interior_prison_i", (-100.00, -100.00), (100.00, 100.00), -100.0, "0", [], []),

	("castle_52_exterior", sf_generate, "none", "none", (0.00, 0.00), (100.00, 100.00), -100.0, "0x00000000300005000009424e00000d2900007e38000038b3", [], [], "outer_terrain_thir_new"),

	("castle_52_interior", sf_indoors, "interior_castle_w", "bo_interior_castle_w", (-100.00, -100.00), (100.00, 100.00), -100.0, "0", ["exit"], ["castle_52_seneschal"]),

	("castle_52_prison", sf_indoors, "interior_prison_i", "bo_interior_prison_i", (-100.00, -100.00), (100.00, 100.00), -100.0, "0", [], []),

	("castle_53_exterior", sf_generate, "none", "none", (0.00, 0.00), (100.00, 100.00), -100.0, "0x00000000b009723200059d6800005f4f0000757f000069cd", [], [], "outer_terrain_plain"),

	("castle_53_interior", sf_indoors, "interior_castle_v", "bo_interior_castle_v", (-100.00, -100.00), (100.00, 100.00), -100.0, "0", ["exit"], ["castle_53_seneschal"]),

	("castle_53_prison", sf_indoors, "interior_prison_i", "bo_interior_prison_i", (-100.00, -100.00), (100.00, 100.00), -100.0, "0", [], []),

	("castle_54_exterior", sf_generate, "none", "none", (0.00, 0.00), (100.00, 100.00), -100.0, "0x0000000030044e900003dd02000077b20000400100005697", [], [], "outer_terrain_plain"),

	("castle_54_interior", sf_indoors, "interior_castle_e", "bo_interior_castle_e", (-100.00, -100.00), (100.00, 100.00), -100.0, "0", ["exit"], ["castle_54_seneschal"]),

	("castle_54_prison", sf_indoors, "interior_prison_d", "bo_interior_prison_d", (-100.00, -100.00), (100.00, 100.00), -100.0, "0", [], []),

	("castle_55_exterior", sf_generate, "none", "none", (0.00, 0.00), (100.00, 100.00), -100.0, "0x0000000030044e900003dd02000077b20000400100005697", [], [], "outer_terrain_plain"),

	("castle_55_interior", sf_indoors, "interior_castle_v", "bo_interior_castle_v", (-100.00, -100.00), (100.00, 100.00), -100.0, "0", ["exit"], ["castle_55_seneschal"]),

	("castle_55_prison", sf_indoors, "interior_prison_d", "bo_interior_prison_d", (-100.00, -100.00), (100.00, 100.00), -100.0, "0", [], []),

	("castle_56_exterior", sf_generate, "none", "none", (0.00, 0.00), (100.00, 100.00), -100.0, "0x0000000030044e900003dd02000077b20000400100005697", [], [], "outer_terrain_plain"),

	("castle_56_interior", sf_indoors, "interior_castle_v", "bo_interior_castle_v", (-100.00, -100.00), (100.00, 100.00), -100.0, "0", ["exit"], ["castle_56_seneschal"]),

	("castle_56_prison", sf_indoors, "interior_prison_d", "bo_interior_prison_d", (-100.00, -100.00), (100.00, 100.00), -100.0, "0", [], []),

	("castle_57_exterior", sf_generate, "none", "none", (0.00, 0.00), (100.00, 100.00), -100.0, "0xa00363638005c16d00003c82000037e000002303", [], [], "outer_terrain_plain"),

	("castle_57_interior", sf_indoors, "white_interior_scene_basic", "bo_interior_castle_n", (-100.00, -100.00), (100.00, 100.00), -100.0, "0", ["exit"], ["castle_57_seneschal"]),

	("castle_57_prison", sf_indoors, "interior_prison_e", "bo_interior_prison_e", (-100.00, -100.00), (100.00, 100.00), -100.0, "0", [], []),

	("castle_59_exterior", sf_generate, "none", "none", (0.00, 0.00), (100.00, 100.00), -100.0, "0x00000001300389800003a4ea000058340000637a0000399b", [], [], "sea_outer_terrain_2"),

	("castle_59_interior", sf_indoors, "interior_castle_e", "bo_interior_castle_e", (-100.00, -100.00), (100.00, 100.00), -100.0, "0", ["exit"], ["castle_59_seneschal"]),

	("castle_59_prison", sf_indoors, "interior_prison_i", "bo_interior_prison_i", (-100.00, -100.00), (100.00, 100.00), -100.0, "0", [], []),

	("castle_60_exterior", sf_generate, "none", "none", (0.00, 0.00), (100.00, 100.00), -100.0, "0x0000000130021f63000721ca000055be000079d90000156d", [], [], "outer_terrain_plain"),

	("castle_60_interior", sf_indoors, "interior_castle_v", "bo_interior_castle_v", (-100.00, -100.00), (100.00, 100.00), -100.0, "0", ["exit"], ["castle_60_seneschal"]),

	("castle_60_prison", sf_indoors, "interior_prison_i", "bo_interior_prison_i", (-100.00, -100.00), (100.00, 100.00), -100.0, "0", [], []),

	("castle_61_exterior", sf_generate, "none", "none", (0.00, 0.00), (100.00, 100.00), -100.0, "0x0000000030044e900003dd02000077b20000400100005697", [], [], "outer_terrain_plain"),

	("castle_61_interior", sf_indoors, "interior_castle_j", "bo_interior_castle_j", (-100.00, -100.00), (100.00, 100.00), -100.0, "0", ["exit"], ["castle_61_seneschal"]),

	("castle_61_prison", sf_indoors, "interior_prison_i", "bo_interior_prison_i", (-100.00, -100.00), (100.00, 100.00), -100.0, "0", [], []),

	("castle_63_exterior", sf_generate, "none", "none", (0.00, 0.00), (100.00, 100.00), -100.0, "0x0000000030044e900003dd02000077b20000400100005697", [], [], "outer_terrain_plain"),

	("castle_63_interior", sf_indoors, "interior_castle_v", "bo_interior_castle_v", (-100.00, -100.00), (100.00, 100.00), -100.0, "0", ["exit"], ["castle_63_seneschal"]),

	("castle_63_prison", sf_indoors, "interior_prison_i", "bo_interior_prison_i", (-100.00, -100.00), (100.00, 100.00), -100.0, "0", [], []),

	("castle_64_exterior", sf_generate, "none", "none", (0.00, 0.00), (100.00, 100.00), -100.0, "0x0000000030044e900003dd02000077b20000400100005697", [], [], "outer_terrain_plain"),

	("castle_64_interior", sf_indoors, "interior_castle_v", "bo_interior_castle_v", (-100.00, -100.00), (100.00, 100.00), -100.0, "0", ["exit"], ["castle_64_seneschal"]),

	("castle_64_prison", sf_indoors, "interior_prison_e", "bo_interior_prison_e", (-100.00, -100.00), (100.00, 100.00), -100.0, "0", [], []),

	("castle_65_exterior", sf_generate, "none", "none", (0.00, 0.00), (100.00, 100.00), -100.0, "0x0000000030044e900003dd02000077b20000400100005697", [], [], "outer_terrain_plain"),

	("castle_65_interior", sf_indoors, "interior_castle_b", "bo_interior_castle_b", (-100.00, -100.00), (100.00, 100.00), -100.0, "0", ["exit"], ["castle_65_seneschal"]),

	("castle_65_prison", sf_indoors, "interior_prison_i", "bo_interior_prison_i", (-100.00, -100.00), (100.00, 100.00), -100.0, "0", [], []),

	("castle_66_exterior", sf_generate, "none", "none", (0.00, 0.00), (100.00, 100.00), -100.0, "0x00000002b007b232000715c50000084c00001b5b00006580", [], [], "outer_terrain_castle_9"),

	("castle_66_interior", sf_indoors, "interior_castle_v", "bo_interior_castle_v", (-100.00, -100.00), (100.00, 100.00), -100.0, "0", ["exit"], ["castle_66_seneschal"]),

	("castle_66_prison", sf_indoors, "interior_prison_i", "bo_interior_prison_i", (-100.00, -100.00), (100.00, 100.00), -100.0, "0", [], []),

	("castle_67_exterior", sf_generate, "none", "none", (0.00, 0.00), (100.00, 100.00), -100.0, "0x0000000030044e900003dd02000077b20000400100005697", [], [], "outer_terrain_plain"),

	("castle_67_interior", sf_indoors, "interior_castle_v", "bo_interior_castle_v", (-100.00, -100.00), (100.00, 100.00), -100.0, "0", ["exit"], ["castle_67_seneschal"]),

	("castle_67_prison", sf_indoors, "interior_prison_i", "bo_interior_prison_i", (-100.00, -100.00), (100.00, 100.00), -100.0, "0", [], []),

	("castle_68_exterior", sf_generate, "none", "none", (0.00, 0.00), (100.00, 100.00), -100.0, "0x00000002b007b232000715c50000084c00001b5b00006580", [], [], "outer_terrain_castle_9"),

	("castle_68_interior", sf_indoors, "interior_castle_v", "bo_interior_castle_v", (-100.00, -100.00), (100.00, 100.00), -100.0, "0", ["exit"], ["castle_68_seneschal"]),

	("castle_68_prison", sf_indoors, "interior_prison_i", "bo_interior_prison_i", (-100.00, -100.00), (100.00, 100.00), -100.0, "0", [], []),

	("castle_69_exterior", sf_generate, "none", "none", (0.00, 0.00), (100.00, 100.00), -100.0, "0x0000000130021f63000721ca000055be000079d90000156d", [], [], "outer_terrain_plain"),

	("castle_69_interior", sf_indoors, "interior_castle_e", "bo_interior_castle_e", (-100.00, -100.00), (100.00, 100.00), -100.0, "0", ["exit"], ["castle_69_seneschal"]),

	("castle_69_prison", sf_indoors, "interior_prison_i", "bo_interior_prison_i", (-100.00, -100.00), (100.00, 100.00), -100.0, "0", [], []),

	("castle_70_exterior", sf_generate, "none", "none", (0.00, 0.00), (100.00, 100.00), -100.0, "0x000000003000050000090a4200006573000069830000640b", [], [], "outer_terrain_castle_9"),

	("castle_70_interior", sf_indoors, "interior_castle_v", "bo_interior_castle_v", (-100.00, -100.00), (100.00, 100.00), -100.0, "0", ["exit"], ["castle_70_seneschal"]),

	("castle_70_prison", sf_indoors, "interior_prison_i", "bo_interior_prison_i", (-100.00, -100.00), (100.00, 100.00), -100.0, "0", [], []),

	("castle_71_exterior", sf_generate, "none", "none", (0.00, 0.00), (100.00, 100.00), -100.0, "0x00000002b007b232000715c50000084c00001b5b00006580", [], [], "outer_terrain_castle_9"),

	("castle_71_interior", sf_indoors, "interior_castle_v", "bo_interior_castle_v", (-100.00, -100.00), (100.00, 100.00), -100.0, "0", ["exit"], ["castle_71_seneschal"]),

	("castle_71_prison", sf_indoors, "interior_prison_i", "bo_interior_prison_i", (-100.00, -100.00), (100.00, 100.00), -100.0, "0", [], []),

	("castle_72_exterior", sf_generate, "none", "none", (0.00, 0.00), (100.00, 100.00), -100.0, "0x000000003017d032000aa6a100005082000079d9000075a5", [], [], "outer_terrain_beach"),

	("castle_72_interior", sf_indoors, "white_interior_scene_basic", "bo_interior_castle_n", (-100.00, -100.00), (100.00, 100.00), -100.0, "0", ["exit"], ["castle_72_seneschal"]),

	("castle_72_prison", sf_indoors, "interior_prison_i", "bo_interior_prison_i", (-100.00, -100.00), (100.00, 100.00), -100.0, "0", [], []),

	("castle_73_exterior", sf_generate, "none", "none", (0.00, 0.00), (100.00, 100.00), -100.0, "0x000000003010e6b200084a1c00004bca0000627e00006b28", [], [], "outer_terrain_beach"),

	("castle_73_interior", sf_indoors, "interior_castle_a", "bo_interior_castle_a", (-100.00, -100.00), (100.00, 100.00), -100.0, "0", ["exit"], ["castle_73_seneschal"]),

	("castle_73_prison", sf_indoors, "interior_prison_d", "bo_interior_prison_d", (-100.00, -100.00), (100.00, 100.00), -100.0, "0", [], []),

	("castle_74_exterior", sf_generate, "none", "none", (0.00, 0.00), (100.00, 100.00), -100.0, "0x00000000300005000004b92b0000449f000064e600000581", [], [], "outer_terrain_plain_farmountain"),

	("castle_74_interior", sf_indoors, "interior_castle_a", "bo_interior_castle_a", (-100.00, -100.00), (100.00, 100.00), -100.0, "0", ["exit"], ["castle_74_seneschal"]),

	("castle_74_prison", sf_indoors, "interior_prison_i", "bo_interior_prison_i", (-100.00, -100.00), (100.00, 100.00), -100.0, "0", [], []),

	("castle_75_exterior", sf_generate, "none", "none", (0.00, 0.00), (100.00, 100.00), -100.0, "0x000000005a07b2320002b8ad000036c80000409d00001987", [], [], "outer_terrain_desert"),

	("castle_75_interior", sf_indoors, "arabian_interior_keep_b", "bo_arabian_interior_keep_b", (-100.00, -100.00), (100.00, 100.00), -100.0, "0", ["exit"], ["castle_75_seneschal"]),

	("castle_75_prison", sf_indoors, "interior_prison_i", "bo_interior_prison_i", (-100.00, -100.00), (100.00, 100.00), -100.0, "0", [], []),

	("castle_76_exterior", sf_generate, "none", "none", (0.00, 0.00), (100.00, 100.00), -100.0, "0x000000012007985300055550000064d500005c060000759e", [], [], "outer_terrain_steppe_mountain"),

	("castle_76_interior", sf_indoors, "arabian_interior_keep_b", "bo_arabian_interior_keep_b", (-100.00, -100.00), (100.00, 100.00), -100.0, "0", ["exit"], ["castle_76_seneschal"]),

	("castle_76_prison", sf_indoors, "interior_prison_i", "bo_interior_prison_i", (-100.00, -100.00), (100.00, 100.00), -100.0, "0", [], []),

	("castle_77_exterior", sf_generate, "none", "none", (0.00, 0.00), (100.00, 100.00), -100.0, "0x000000012007985300055550000064d500005c060000759e", [], [], "outer_terrain_steppe_mountain"),

	("castle_77_interior", sf_indoors, "arabian_interior_keep_b", "bo_arabian_interior_keep_b", (-100.00, -100.00), (100.00, 100.00), -100.0, "0", ["exit"], ["castle_76_seneschal"]),

	("castle_77_prison", sf_indoors, "interior_prison_i", "bo_interior_prison_i", (-100.00, -100.00), (100.00, 100.00), -100.0, "0", [], []),

	("castle_78_exterior", sf_generate, "none", "none", (0.00, 0.00), (100.00, 100.00), -100.0, "0x000000012007985300055550000064d500005c060000759e", [], [], "outer_terrain_steppe_mountain"),

	("castle_78_interior", sf_indoors, "interior_castle_g_square_keep_b", "bo_interior_castle_g_square_keep_b", (-100.00, -100.00), (100.00, 100.00), -100.0, "0", ["exit"], ["town_44_seneschal"]),

	("castle_78_prison", sf_indoors, "interior_prison_a", "bo_interior_prison_a", (-100.00, -100.00), (100.00, 100.00), -100.0, "0", [], []),

	("castle_79_exterior", sf_generate, "none", "none", (0.00, 0.00), (100.00, 100.00), -100.0, "0x000000012007985300055550000064d500005c060000759e", [], [], "outer_terrain_steppe_mountain"),

	("castle_79_interior", sf_indoors, "interior_castle_g_square_keep_b", "bo_interior_castle_g_square_keep_b", (-100.00, -100.00), (100.00, 100.00), -100.0, "0", ["exit"], ["town_44_seneschal"]),

	("castle_79_prison", sf_indoors, "interior_prison_a", "bo_interior_prison_a", (-100.00, -100.00), (100.00, 100.00), -100.0, "0", [], []),

	("castle_80_exterior", sf_generate, "none", "none", (0.00, 0.00), (100.00, 100.00), -100.0, "0x000000005a0932320004cd3000004e7d00007d6e00006c58", [], [], "outer_terrain_desert"),

	("castle_80_interior", sf_indoors, "arabian_interior_keep_b", "bo_arabian_interior_keep_b", (-100.00, -100.00), (100.00, 100.00), -100.0, "0", ["exit"], ["castle_80_seneschal"]),

	("castle_80_prison", sf_indoors, "interior_prison_i", "bo_interior_prison_i", (-100.00, -100.00), (100.00, 100.00), -100.0, "0", [], []),

	("castle_82_exterior", sf_generate, "none", "none", (0.00, 0.00), (100.00, 100.00), -100.0, "0x00000000300005000004b92b0000449f000064e600000581", [], [], "outer_terrain_plain_farmountain"),

	("castle_82_interior", sf_indoors, "interior_castle_a", "bo_interior_castle_a", (-100.00, -100.00), (100.00, 100.00), -100.0, "0", ["exit"], ["castle_82_seneschal"]),

	("castle_82_prison", sf_indoors, "interior_prison_j", "bo_interior_prison_j", (-100.00, -100.00), (100.00, 100.00), -100.0, "0", [], []),

	("castle_83_exterior", sf_generate, "none", "none", (0.00, 0.00), (100.00, 100.00), -100.0, "0x0000000130021f63000721ca000055be000079d90000156d", [], [], "outer_terrain_plain"),

	("castle_83_interior", sf_indoors, "interior_castle_v", "bo_interior_castle_v", (-100.00, -100.00), (100.00, 100.00), -100.0, "0", ["exit"], ["castle_83_seneschal"]),

	("castle_83_prison", sf_indoors, "interior_prison_i", "bo_interior_prison_i", (-100.00, -100.00), (100.00, 100.00), -100.0, "0", [], []),

	("castle_84_exterior", sf_generate, "none", "none", (0.00, 0.00), (100.00, 100.00), -100.0, "0x000000013004e0a600061989000053d50000749800005f64", [], [], "outer_terrain_plain_farmountain"),

	("castle_84_interior", sf_indoors, "interior_castle_v", "bo_interior_castle_v", (-100.00, -100.00), (100.00, 100.00), -100.0, "0", ["exit"], ["castle_84_seneschal"]),

	("castle_84_prison", sf_indoors, "interior_prison_e", "bo_interior_prison_e", (-100.00, -100.00), (100.00, 100.00), -100.0, "0", [], []),

	("castle_85_exterior", sf_generate, "none", "none", (0.00, 0.00), (100.00, 100.00), -100.0, "0x00000000300005000008f63b00001d5700005904000031b7", [], [], "sea_outer_terrain_2"),

	("castle_85_interior", sf_indoors, "interior_castle_v", "bo_interior_castle_v", (-100.00, -100.00), (100.00, 100.00), -100.0, "0", ["exit"], ["castle_85_seneschal"]),

	("castle_85_prison", sf_indoors, "interior_prison_i", "bo_interior_prison_i", (-100.00, -100.00), (100.00, 100.00), -100.0, "0", [], []),

	("castle_86_exterior", sf_generate, "none", "none", (0.00, 0.00), (100.00, 100.00), -100.0, "0xa00363638005c16d00003c82000037e000002303", [], [], "outer_terrain_plain"),

	("castle_86_interior", sf_indoors, "white_interior_scene_basic", "bo_interior_castle_n", (-100.00, -100.00), (100.00, 100.00), -100.0, "0", ["exit"], ["castle_86_seneschal"]),

	("castle_86_prison", sf_indoors, "interior_prison_d", "bo_interior_prison_d", (-100.00, -100.00), (100.00, 100.00), -100.0, "0", [], []),

	("castle_87_exterior", sf_generate, "none", "none", (0.00, 0.00), (100.00, 100.00), -100.0, "0x0000000030044e900003dd02000077b20000400100005697", [], [], "outer_terrain_plain"),

	("castle_87_interior", sf_indoors, "interior_castle_v", "bo_interior_castle_v", (-100.00, -100.00), (100.00, 100.00), -100.0, "0", ["exit"], ["castle_87_seneschal"]),

	("castle_87_prison", sf_indoors, "interior_prison_j", "bo_interior_prison_j", (-100.00, -100.00), (100.00, 100.00), -100.0, "0", [], []),

	("castle_88_exterior", sf_generate, "none", "none", (0.00, 0.00), (100.00, 100.00), -100.0, "0xa00363638005c16d00003c82000037e000002303", [], [], "outer_terrain_plain"),

	("castle_88_interior", sf_indoors, "white_interior_scene_basic", "bo_interior_castle_n", (-100.00, -100.00), (100.00, 100.00), -100.0, "0", ["exit"], ["castle_88_seneschal"]),

	("castle_88_prison", sf_indoors, "interior_prison_d", "bo_interior_prison_d", (-100.00, -100.00), (100.00, 100.00), -100.0, "0", [], []),

	("castle_89_exterior", sf_generate, "none", "none", (0.00, 0.00), (100.00, 100.00), -100.0, "0x00000004300005000006c1ae000074be000022a300000dd6", [], [], "outer_terrain_castle_9"),

	("castle_89_interior", sf_indoors, "interior_castle_v", "bo_interior_castle_v", (-100.00, -100.00), (100.00, 100.00), -100.0, "0", ["exit"], ["castle_89_seneschal"]),

	("castle_89_prison", sf_indoors, "interior_prison_d", "bo_interior_prison_d", (-100.00, -100.00), (100.00, 100.00), -100.0, "0", [], []),

	("castle_90_exterior", sf_generate, "none", "none", (0.00, 0.00), (100.00, 100.00), -100.0, "0x00000000300005000008f63b00001d5700005904000031b7", [], [], "sea_outer_terrain_2"),

	("castle_90_interior", sf_indoors, "interior_castle_e", "bo_interior_castle_e", (-100.00, -100.00), (100.00, 100.00), -100.0, "0", ["exit"], ["castle_90_seneschal"]),

	("castle_90_prison", sf_indoors, "interior_prison_d", "bo_interior_prison_d", (-100.00, -100.00), (100.00, 100.00), -100.0, "0", [], []),

	("castle_91_exterior", sf_generate, "none", "none", (0.00, 0.00), (100.00, 100.00), -100.0, "0x0000000030044e900003dd02000077b20000400100005697", [], [], "outer_terrain_plain"),

	("castle_91_interior", sf_indoors, "interior_castle_a", "bo_interior_castle_a", (-100.00, -100.00), (100.00, 100.00), -100.0, "0", ["exit"], ["castle_91_seneschal"]),

	("castle_91_prison", sf_indoors, "interior_prison_d", "bo_interior_prison_d", (-100.00, -100.00), (100.00, 100.00), -100.0, "0", [], []),

	("castle_92_exterior", sf_generate, "none", "none", (0.00, 0.00), (100.00, 100.00), -100.0, "0x0000000030044e900003dd02000077b20000400100005697", [], [], "outer_terrain_plain"),

	("castle_92_interior", sf_indoors, "interior_castle_v", "bo_interior_castle_v", (-100.00, -100.00), (100.00, 100.00), -100.0, "0", ["exit"], ["castle_92_seneschal"]),

	("castle_92_prison", sf_indoors, "interior_prison_d", "bo_interior_prison_d", (-100.00, -100.00), (100.00, 100.00), -100.0, "0", [], []),

	("castle_93_exterior", sf_generate, "none", "none", (0.00, 0.00), (100.00, 100.00), -100.0, "0x000000005a07b2320002b8ad000036c80000409d00001987", [], [], "outer_terrain_desert"),

	("castle_93_interior", sf_indoors, "arabian_interior_keep_b", "bo_arabian_interior_keep_b", (-100.00, -100.00), (100.00, 100.00), -100.0, "0", ["exit"], ["castle_93_seneschal"]),

	("castle_93_prison", sf_indoors, "interior_prison_i", "bo_interior_prison_i", (-100.00, -100.00), (100.00, 100.00), -100.0, "0", [], []),

	("castle_95_exterior", sf_generate, "none", "none", (0.00, 0.00), (100.00, 100.00), -100.0, "0x00000002300658bc0007bded000025520000093800006114", [], [], "outer_terrain_thir_new"),

	("castle_95_interior", sf_indoors, "interior_castle_k", "bo_interior_castle_k", (-100.00, -100.00), (100.00, 100.00), -100.0, "0", ["exit"], ["castle_95_seneschal"]),

	("castle_95_prison", sf_indoors, "interior_prison_d", "bo_interior_prison_d", (-100.00, -100.00), (100.00, 100.00), -100.0, "0", [], []),

	("castle_96_exterior", sf_generate, "none", "none", (0.00, 0.00), (100.00, 100.00), -100.0, "0x00000002300658bc0007bded000025520000093800006114", [], [], "outer_terrain_thir_new"),

	("castle_96_interior", sf_indoors, "interior_castle_j", "bo_interior_castle_j", (-100.00, -100.00), (100.00, 100.00), -100.0, "0", ["exit"], ["castle_96_seneschal"]),

	("castle_96_prison", sf_indoors, "interior_prison_d", "bo_interior_prison_d", (-100.00, -100.00), (100.00, 100.00), -100.0, "0", [], []),

	("castle_99_exterior", sf_generate, "none", "none", (0.00, 0.00), (100.00, 100.00), -100.0, "0x000000005a0932320004cd3000004e7d00007d6e00006c58", [], [], "outer_terrain_desert"),

	("castle_99_interior", sf_indoors, "arabian_interior_keep_b", "bo_arabian_interior_keep_b", (-100.00, -100.00), (100.00, 100.00), -100.0, "0", ["exit"], ["castle_99_seneschal"]),

	("castle_99_prison", sf_indoors, "interior_prison_i", "bo_interior_prison_i", (-100.00, -100.00), (100.00, 100.00), -100.0, "0", [], []),

	("castle_100_exterior", sf_generate, "none", "none", (0.00, 0.00), (100.00, 100.00), -100.0, "0xa00363638005c16d00003c82000037e000002303", [], [], "outer_terrain_plain"),

	("castle_100_interior", sf_indoors, "white_interior_scene_basic", "bo_interior_castle_n", (-100.00, -100.00), (100.00, 100.00), -100.0, "0", ["exit"], ["castle_100_seneschal"]),

	("castle_100_prison", sf_indoors, "interior_prison_d", "bo_interior_prison_d", (-100.00, -100.00), (100.00, 100.00), -100.0, "0", [], []),

	("castle_104_exterior", sf_generate, "none", "none", (0.00, 0.00), (100.00, 100.00), -100.0, "0x0000000030044e900003dd02000077b20000400100005697", [], [], "outer_terrain_plain"),

	("castle_104_interior", sf_indoors, "interior_castle_a", "bo_interior_castle_a", (-100.00, -100.00), (100.00, 100.00), -100.0, "0", ["exit"], ["castle_104_seneschal"]),

	("castle_104_prison", sf_indoors, "interior_prison_d", "bo_interior_prison_d", (-100.00, -100.00), (100.00, 100.00), -100.0, "0", [], []),

	("castle_105_exterior", sf_generate, "none", "none", (0.00, 0.00), (100.00, 100.00), -100.0, "0x0000000333478d9f000509380000738a0000307a000018e9", [], [], "outer_terrain_plain"),

	("castle_105_interior", sf_indoors, "interior_castle_v", "bo_interior_castle_v", (-100.00, -100.00), (100.00, 100.00), -100.0, "0", ["exit"], ["castle_105_seneschal"]),

	("castle_105_prison", sf_indoors, "interior_prison_i", "bo_interior_prison_i", (-100.00, -100.00), (100.00, 100.00), -100.0, "0", [], []),

	("castle_106_exterior", sf_generate, "none", "none", (0.00, 0.00), (100.00, 100.00), -100.0, "0x00000002300658bc0007bded000025520000093800006114", [], [], "outer_terrain_thir_new"),

	("castle_106_interior", sf_indoors, "interior_castle_k", "bo_interior_castle_k", (-100.00, -100.00), (100.00, 100.00), -100.0, "0", ["exit"], ["castle_106_seneschal"]),

	("castle_106_prison", sf_indoors, "interior_prison_d", "bo_interior_prison_d", (-100.00, -100.00), (100.00, 100.00), -100.0, "0", [], []),

	("castle_107_exterior", sf_generate, "none", "none", (0.00, 0.00), (100.00, 100.00), -100.0, "0x0000000130010e0e0005fd84000011c60000285b00005cbe", [], [], "outer_terrain_plain"),

	("castle_107_interior", sf_indoors, "dungeon_tower_cell_a", "bo_dungeon_tower_cell_a", (-100.00, -100.00), (100.00, 100.00), -100.0, "0", ["exit"], ["castle_107_seneschal"]),

	("castle_107_prison", sf_indoors, "interior_prison_i", "bo_interior_prison_i", (-100.00, -100.00), (100.00, 100.00), -100.0, "0", [], []),

	("castle_108_exterior", sf_generate, "none", "none", (0.00, 0.00), (100.00, 100.00), -100.0, "0x00000002300658bc0007bded000025520000093800006114", [], [], "outer_terrain_thir_new"),

	("castle_108_interior", sf_indoors, "interior_castle_k", "bo_interior_castle_k", (-100.00, -100.00), (100.00, 100.00), -100.0, "0", ["exit"], ["castle_108_seneschal"]),

	("castle_108_prison", sf_indoors, "interior_prison_d", "bo_interior_prison_d", (-100.00, -100.00), (100.00, 100.00), -100.0, "0", [], []),

	("castle_109_exterior", sf_generate, "none", "none", (0.00, 0.00), (100.00, 100.00), -100.0, "0x00000001300389800003a4ea000058340000637a0000399b", [], [], "sea_outer_terrain_2"),

	("castle_109_interior", sf_indoors, "interior_castle_a", "bo_interior_castle_a", (-100.00, -100.00), (100.00, 100.00), -100.0, "0", ["exit"], ["castle_109_seneschal"]),

	("castle_109_prison", sf_indoors, "interior_prison_d", "bo_interior_prison_d", (-100.00, -100.00), (100.00, 100.00), -100.0, "0", [], []),

	("castle_110_exterior", sf_generate, "none", "none", (0.00, 0.00), (100.00, 100.00), -100.0, "0x00000001300389800003a4ea000058340000637a0000399b", [], [], "outer_terrain_plain"),

	("castle_110_interior", sf_indoors, "interior_castle_v", "bo_interior_castle_v", (-100.00, -100.00), (100.00, 100.00), -100.0, "0", ["exit"], ["castle_110_seneschal"]),

	("castle_110_prison", sf_indoors, "interior_prison_d", "bo_interior_prison_d", (-100.00, -100.00), (100.00, 100.00), -100.0, "0", [], []),

	("castle_111_exterior", sf_generate, "none", "none", (0.00, 0.00), (100.00, 100.00), -100.0, "0x00000000300005000008f63b00001d5700005904000031b7", [], [], "sea_outer_terrain_2"),

	("castle_111_interior", sf_indoors, "interior_castle_v", "bo_interior_castle_v", (-100.00, -100.00), (100.00, 100.00), -100.0, "0", ["exit"], ["castle_111_seneschal"]),

	("castle_111_prison", sf_indoors, "interior_prison_i", "bo_interior_prison_i", (-100.00, -100.00), (100.00, 100.00), -100.0, "0", [], []),

	("castle_112_exterior", sf_generate, "none", "none", (0.00, 0.00), (100.00, 100.00), -100.0, "0xa00363638005c16d00003c82000037e000002303", [], [], "outer_terrain_plain"),

	("castle_112_interior", sf_indoors, "white_interior_scene_basic", "bo_interior_castle_n", (-100.00, -100.00), (100.00, 100.00), -100.0, "0", ["exit"], ["castle_112_seneschal"]),

	("castle_112_prison", sf_indoors, "interior_prison_i", "bo_interior_prison_i", (-100.00, -100.00), (100.00, 100.00), -100.0, "0", [], []),

	("castle_115_exterior", sf_generate, "none", "none", (0.00, 0.00), (100.00, 100.00), -100.0, "0x0000000030044e900003dd02000077b20000400100005697", [], [], "outer_terrain_plain"),

	("castle_115_interior", sf_indoors, "interior_castle_v", "bo_interior_castle_v", (-100.00, -100.00), (100.00, 100.00), -100.0, "0", ["exit"], ["castle_115_seneschal"]),

	("castle_115_prison", sf_indoors, "interior_prison_k", "bo_interior_prison_k", (-100.00, -100.00), (100.00, 100.00), -100.0, "0", [], []),

	("castle_119_exterior", sf_generate, "none", "none", (0.00, 0.00), (100.00, 100.00), -100.0, "0x0000000030044e900003dd02000077b20000400100005697", [], [], "outer_terrain_plain"),

	("castle_119_interior", sf_indoors, "interior_castle_a", "bo_interior_castle_a", (-100.00, -100.00), (100.00, 100.00), -100.0, "0", ["exit"], ["castle_119_seneschal"]),

	("castle_119_prison", sf_indoors, "interior_prison_k", "bo_interior_prison_k", (-100.00, -100.00), (100.00, 100.00), -100.0, "0", [], []),

	("castle_120_exterior", sf_generate, "none", "none", (0.00, 0.00), (100.00, 100.00), -100.0, "0x0000000030044e900003dd02000077b20000400100005697", [], [], "outer_terrain_plain"),

	("castle_120_interior", sf_indoors, "interior_castle_a", "bo_interior_castle_a", (-100.00, -100.00), (100.00, 100.00), -100.0, "0", ["exit"], ["castle_120_seneschal"]),

	("castle_120_prison", sf_indoors, "interior_prison_k", "bo_interior_prison_k", (-100.00, -100.00), (100.00, 100.00), -100.0, "0", [], []),

	("castle_127_exterior", sf_generate, "none", "none", (0.00, 0.00), (100.00, 100.00), -100.0, "0x0000000130038980000fffff000058340000637a0000399b", [], [], "outer_terrain_riverrun"),

	("castle_127_interior", sf_generate, "none", "none", (0.00, 0.00), (100.00, 100.00), -100.0, "0x0000000130038980000fffff000058340000637a0000399b", ["exit"], ["castle_127_seneschal"], "outer_terrain_riverrun"),

	("castle_127_prison", sf_indoors, "interior_prison_e", "bo_interior_prison_e", (-100.00, -100.00), (100.00, 100.00), -100.0, "0", [], []),

	("castle_128_exterior", sf_generate, "none", "none", (0.00, 0.00), (100.00, 100.00), -100.0, "0x0000000254c2ec0000042509000016da0000017200000ed3", [], [], "outer_terrain_desert"),

	("castle_128_interior", sf_indoors, "arabian_interior_keep_b", "bo_arabian_interior_keep_b", (-100.00, -100.00), (100.00, 100.00), -100.0, "0", ["exit"], ["castle_128_seneschal"]),

	("castle_128_prison", sf_indoors, "interior_prison_i", "bo_interior_prison_i", (-100.00, -100.00), (100.00, 100.00), -100.0, "0", [], []),

	("castle_129_exterior", sf_generate, "none", "none", (0.00, 0.00), (100.00, 100.00), -100.0, "0x00000000200005000005213200004f2900003331000050ef", [], [], "outer_terrain_steppe_farmountain"),

	("castle_129_interior", sf_indoors, "interior_castle_z", "bo_interior_castle_z", (-100.00, -100.00), (100.00, 100.00), -100.0, "0", ["exit"], ["castle_129_seneschal"]),

	("castle_129_prison", sf_indoors, "interior_prison_e", "bo_interior_prison_e", (-100.00, -100.00), (100.00, 100.00), -100.0, "0", [], []),

	("castle_130_exterior", sf_generate, "none", "none", (0.00, 0.00), (100.00, 100.00), -100.0, "0x000000033000124c000acab40000280700000c9f00000ab5", [], [], "outer_terrain_none"),

	("castle_130_interior", sf_indoors, "interior_castle_x", "bo_interior_castle_x", (-100.00, -100.00), (100.00, 100.00), -100.0, "0", ["exit"], ["castle_130_seneschal"]),

	("castle_130_prison", sf_indoors, "interior_prison_e", "bo_interior_prison_e", (-100.00, -100.00), (100.00, 100.00), -100.0, "0", [], []),

	("castle_131_exterior", sf_generate, "none", "none", (0.00, 0.00), (100.00, 100.00), -100.0, "0x00000000b00037630002308c00000c9400005d4c00000f3a", [], [], "outer_terrain_plain"),

	("castle_131_interior", sf_indoors, "interior_castle_v", "bo_interior_castle_v", (-100.00, -100.00), (100.00, 100.00), -100.0, "0", ["exit"], ["castle_131_seneschal"]),

	("castle_131_prison", sf_indoors, "interior_prison_e", "bo_interior_prison_e", (-100.00, -100.00), (100.00, 100.00), -100.0, "0", [], []),

	("castle_132_exterior", sf_generate, "none", "none", (0.00, 0.00), (100.00, 100.00), -100.0, "0x000000012007985300055550000064d500005c060000759e", [], [], "outer_terrain_steppe"),

	("castle_132_interior", sf_indoors, "arabian_interior_keep_b", "bo_arabian_interior_keep_b", (-100.00, -100.00), (100.00, 100.00), -100.0, "0", ["exit"], ["castle_132_seneschal"]),

	("castle_132_prison", sf_indoors, "interior_prison_e", "bo_interior_prison_e", (-100.00, -100.00), (100.00, 100.00), -100.0, "0", [], []),

	("castle_133_exterior", sf_generate, "none", "none", (0.00, 0.00), (100.00, 100.00), -100.0, "0x00000000300005000005394b000065b000004f6c0000349a", [], [], "outer_terrain_plain"),

	("castle_133_interior", sf_generate, "none", "none", (0.00, 0.00), (100.00, 100.00), -100.0, "0x00000000300005000005394b000065b000004f6c0000349a", ["exit"], ["castle_133_seneschal"], "outer_terrain_plain"),

	("castle_133_prison", sf_indoors, "interior_prison_e", "bo_interior_prison_e", (-100.00, -100.00), (100.00, 100.00), -100.0, "0", [], []),

	("castle_134_exterior", sf_generate, "none", "none", (0.00, 0.00), (100.00, 100.00), -100.0, "0x000000012007985300055550000064d500005c060000759e", [], [], "outer_terrain_steppe"),

	("castle_134_interior", sf_indoors, "arabian_interior_keep_b", "bo_arabian_interior_keep_b", (-100.00, -100.00), (100.00, 100.00), -100.0, "0", ["exit"], ["castle_134_seneschal"]),

	("castle_134_prison", sf_indoors, "interior_prison_i", "bo_interior_prison_i", (-100.00, -100.00), (100.00, 100.00), -100.0, "0", [], []),

	("castle_135_exterior", sf_generate, "none", "none", (0.00, 0.00), (100.00, 100.00), -100.0, "0x0000000050000500000d23480000482c0000383900002fd6", [], [], "outer_terrain_desert"),

	("castle_135_interior", sf_indoors, "arabian_interior_keep_b", "bo_arabian_interior_keep_b", (-100.00, -100.00), (100.00, 100.00), -100.0, "0", ["exit"], ["castle_135_seneschal"]),

	("castle_135_prison", sf_indoors, "interior_prison_i", "bo_interior_prison_i", (-100.00, -100.00), (100.00, 100.00), -100.0, "0", [], []),

	("castle_136_exterior", sf_generate, "none", "none", (0.00, 0.00), (100.00, 100.00), -100.0, "0x0000000020000500000ae6b700001cea0000225900000bfd", [], [], "outer_terrain_plain"),

	("castle_136_interior", sf_indoors, "interior_castle_v", "bo_interior_castle_v", (-100.00, -100.00), (100.00, 100.00), -100.0, "0", ["exit"], ["castle_136_seneschal"]),

	("castle_136_prison", sf_indoors, "interior_prison_e", "bo_interior_prison_e", (-100.00, -100.00), (100.00, 100.00), -100.0, "0", [], []),

	("castle_137_exterior", sf_generate, "none", "none", (0.00, 0.00), (100.00, 100.00), -100.0, "0x000000033000124c000acab40000280700000c9f00000ab5", [], [], "sea_outer_terrain_2"),

	("castle_137_interior", sf_indoors, "interior_castle_v", "bo_interior_castle_v", (-100.00, -100.00), (100.00, 100.00), -100.0, "0", ["exit"], ["castle_137_seneschal"]),

	("castle_137_prison", sf_indoors, "interior_prison_e", "bo_interior_prison_e", (-100.00, -100.00), (100.00, 100.00), -100.0, "0", [], []),

	("castle_138_exterior", sf_generate, "none", "none", (0.00, 0.00), (100.00, 100.00), -100.0, "0x0000000230084fac00057d5f00002ba900004a7a000060be", [], [], "outer_terrain_plain_farmountain"),

	("castle_138_interior", sf_indoors, "interior_castle_k", "bo_interior_castle_k", (-100.00, -100.00), (100.00, 100.00), -100.0, "0", ["exit"], ["castle_138_seneschal"]),

	("castle_138_prison", sf_indoors, "interior_prison_e", "bo_interior_prison_e", (-100.00, -100.00), (100.00, 100.00), -100.0, "0", [], []),

	("castle_139_exterior", sf_generate, "none", "none", (0.00, 0.00), (100.00, 100.00), -100.0, "0x314d060900036cd70000295300002ec9000025f3", [], [], "outer_terrain_plain"),

	("castle_139_interior", sf_indoors, "interior_castle_e", "bo_interior_castle_e", (-100.00, -100.00), (100.00, 100.00), -100.0, "0", ["exit"], ["castle_139_seneschal"]),

	("castle_139_prison", sf_indoors, "interior_prison_e", "bo_interior_prison_e", (-100.00, -100.00), (100.00, 100.00), -100.0, "0", [], []),

	("castle_140_exterior", sf_generate, "none", "none", (0.00, 0.00), (100.00, 100.00), -100.0, "0x000000003000050000042d0d000045dd0000243500004ef7", [], [], "sea_outer_terrain_2"),

	("castle_140_interior", sf_generate, "none", "none", (0.00, 0.00), (100.00, 100.00), -100.0, "0x000000003000050000042d0d000045dd0000243500004ef7", ["exit"], ["castle_140_seneschal"], "sea_outer_terrain_2"),

	("castle_140_prison", sf_indoors, "interior_prison_e", "bo_interior_prison_e", (-100.00, -100.00), (100.00, 100.00), -100.0, "0", [], []),

	("castle_141_exterior", sf_generate, "none", "none", (0.00, 0.00), (100.00, 100.00), -100.0, "0x000000012007985300055550000064d500005c060000759e", [], [], "outer_terrain_steppe_mountain"),

	("castle_141_interior", sf_indoors, "arabian_interior_keep_b", "bo_arabian_interior_keep_b", (-100.00, -100.00), (100.00, 100.00), -100.0, "0", ["exit"], ["castle_141_seneschal"]),

	("castle_141_prison", sf_indoors, "interior_prison_i", "bo_interior_prison_i", (-100.00, -100.00), (100.00, 100.00), -100.0, "0", [], []),

	("castle_142_exterior", sf_generate, "none", "none", (0.00, 0.00), (100.00, 100.00), -100.0, "0x000000012007985300055550000064d500005c060000759e", [], [], "outer_terrain_steppe_mountain"),

	("castle_142_interior", sf_indoors, "arabian_interior_keep_b", "bo_arabian_interior_keep_b", (-100.00, -100.00), (100.00, 100.00), -100.0, "0", ["exit"], ["castle_142_seneschal"]),

	("castle_142_prison", sf_indoors, "interior_prison_i", "bo_interior_prison_i", (-100.00, -100.00), (100.00, 100.00), -100.0, "0", [], []),

	("village_1", sf_generate, "none", "none", (0.00, 0.00), (100.00, 100.00), -100.0, "0x0000000030081763000589620000338e00004f2c00005cfb", [], [], "outer_terrain_plain"),

	("village_2", sf_generate, "none", "none", (0.00, 0.00), (100.00, 100.00), -100.0, "0x000000003007a21c0003ecfe000001f0000073b100000fd2", [], [], "outer_terrain_plain"),

	("village_3", sf_generate, "none", "none", (0.00, 0.00), (100.00, 100.00), -100.0, "0x000000023003dc4e0006118b000029f8000034670000105f", [], [], "outer_terrain_thir_new"),

	("village_4", sf_generate, "none", "none", (0.00, 0.00), (100.00, 100.00), -100.0, "0x0000000030044e900003dd02000077b20000400100005697", [], [], "outer_terrain_plain_farmountain"),

	("village_5", sf_generate, "none", "none", (0.00, 0.00), (100.00, 100.00), -100.0, "0x000000003001ce100006097d0000134c000016d8000042a2", [], [], "outer_terrain_thir_new"),

	("village_6", sf_generate, "none", "none", (0.00, 0.00), (100.00, 100.00), -100.0, "0x0000000020000a63000806030000537900001eba00001f25", [], [], "outer_terrain_steppe"),

	("village_7", sf_generate, "none", "none", (0.00, 0.00), (100.00, 100.00), -100.0, "0x0000000031059a0d0004792000005c3a00004df500000dbc", [], [], "outer_terrain_plain"),

	("village_8", sf_generate, "none", "none", (0.00, 0.00), (100.00, 100.00), -100.0, "0x00000002300798320006499200002acc000040d70000421d", [], [], "outer_terrain_plain"),

	("village_9", sf_generate, "none", "none", (0.00, 0.00), (100.00, 100.00), -100.0, "0x000000013005dad40005f57b0000543e0000279d000052b4", [], [], "outer_terrain_plain"),

	("village_10", sf_generate, "none", "none", (0.00, 0.00), (100.00, 100.00), -100.0, "0x000000013005dad40005f57b0000543e0000279d000052b4", [], [], "outer_terrain_plain"),

	("village_11", sf_generate, "none", "none", (0.00, 0.00), (100.00, 100.00), -100.0, "0x0000000220029c4400077de100002dcc00002edf00003925", [], [], "outer_terrain_steppe_mountain"),

	("village_12", sf_generate, "none", "none", (0.00, 0.00), (100.00, 100.00), -100.0, "0x0000000020000a63000806030000537900001eba00001f25", [], [], "outer_terrain_steppe"),

	("village_13", sf_generate, "none", "none", (0.00, 0.00), (100.00, 100.00), -100.0, "0x00000002300019500006c1b4000065c700002bea0000154e", [], [], "sea_outer_terrain_2"),

	("village_14", sf_generate, "none", "none", (0.00, 0.00), (100.00, 100.00), -100.0, "0x0000000230029ce30004912400002acc000040d7000077db", [], [], "outer_terrain_plain"),

	("village_15", sf_generate, "none", "none", (0.00, 0.00), (100.00, 100.00), -100.0, "0x0000000020000a63000806030000537900001eba00001f25", [], [], "outer_terrain_steppe"),

	("village_16", sf_generate, "none", "none", (0.00, 0.00), (100.00, 100.00), -100.0, "0x000000013005dad40005f57b0000543e0000279d000052b4", [], [], "outer_terrain_plain"),

	("village_17", sf_generate, "none", "none", (0.00, 0.00), (100.00, 100.00), -100.0, "0x000000003001ce100006097d0000134c000016d8000042a2", [], [], "outer_terrain_thir_new"),

	("village_18", sf_generate, "none", "none", (0.00, 0.00), (100.00, 100.00), -100.0, "0x0000000020000a63000806030000537900001eba00001f25", [], [], "outer_terrain_steppe"),

	("village_19", sf_generate, "none", "none", (0.00, 0.00), (100.00, 100.00), -100.0, "0x0000000220029c4400077de100002dcc00002edf00003925", [], [], "outer_terrain_steppe_mountain"),

	("village_20", sf_generate, "none", "none", (0.00, 0.00), (100.00, 100.00), -100.0, "0x000000003001ce100006097d0000134c000016d8000042a2", [], [], "outer_terrain_thir_new"),

	("village_21", sf_generate, "none", "none", (0.00, 0.00), (100.00, 100.00), -100.0, "0x0000000220029c4400077de100002dcc00002edf00003925", [], [], "outer_terrain_steppe_mountain"),

	("village_22", sf_generate, "none", "none", (0.00, 0.00), (100.00, 100.00), -100.0, "0x0000000220029c4400077de100002dcc00002edf00003925", [], [], "outer_terrain_steppe_mountain"),

	("village_23", sf_generate, "none", "none", (0.00, 0.00), (100.00, 100.00), -100.0, "0x00000002300415380007b5e600005f7b00000a9200001615", [], [], "outer_terrain_plain_farmountain"),

	("village_24", sf_generate, "none", "none", (0.00, 0.00), (100.00, 100.00), -100.0, "0x000000022004d36300077dd600002e08000036ab00004651", [], [], "outer_terrain_steppe_mountain"),

	("village_25", sf_generate, "none", "none", (0.00, 0.00), (100.00, 100.00), -100.0, "0x000000013001c98a0004dd3000001a5e00005c6200001ec9", [], [], "outer_terrain_plain"),

	("village_26", sf_generate, "none", "none", (0.00, 0.00), (100.00, 100.00), -100.0, "0x0000000230020a008005294c000063fc0000771c0000216f", [], [], "outer_terrain_plain_farmountain"),

	("village_27", sf_generate, "none", "none", (0.00, 0.00), (100.00, 100.00), -100.0, "0x000000022004d36300077dd600002e08000036ab00004651", [], [], "outer_terrain_steppe_mountain"),

	("village_28", sf_generate, "none", "none", (0.00, 0.00), (100.00, 100.00), -100.0, "0x000000022002de4c00077ddd00007e1300000af400006de1", [], [], "outer_terrain_steppe"),

	("village_29", sf_generate, "none", "none", (0.00, 0.00), (100.00, 100.00), -100.0, "0x000000023007b2320004f93c000023ed000053e500002949", [], [], "outer_terrain_plain"),

	("village_30", sf_generate, "none", "none", (0.00, 0.00), (100.00, 100.00), -100.0, "0x0000000230025e0a0004dd3700004822000032ea0000011b", [], [], "outer_terrain_plain_farmountain"),

	("village_31", sf_generate, "none", "none", (0.00, 0.00), (100.00, 100.00), -100.0, "0x000000012002a0b20004992700006e54000007fe00001fd2", [], [], "outer_terrain_steppe"),

	("village_32", sf_generate, "none", "none", (0.00, 0.00), (100.00, 100.00), -100.0, "0x000000012002a0b20004992700006e54000007fe00001fd2", [], [], "outer_terrain_steppe"),

	("village_33", sf_generate, "none", "none", (0.00, 0.00), (100.00, 100.00), -100.0, "0x0000000130001700000649920000423900007768000062c3", [], [], "outer_terrain_plain"),

	("village_34", sf_generate, "none", "none", (0.00, 0.00), (100.00, 100.00), -100.0, "0x00000002300323e3000611860000392d00005c05000067e1", [], [], "outer_terrain_plain"),

	("village_35", sf_generate, "none", "none", (0.00, 0.00), (100.00, 100.00), -100.0, "0x0000000230079cb20005394e00001ef90000753000000731", [], [], "outer_terrain_thir_new"),

	("village_36", sf_generate, "none", "none", (0.00, 0.00), (100.00, 100.00), -100.0, "0x000000013003a1560006118d00003ce300004123000043b2", [], [], "outer_terrain_thir_new"),

	("village_37", sf_generate, "none", "none", (0.00, 0.00), (100.00, 100.00), -100.0, "0x000000022004d36300077dd600002e08000036ab00004651", [], [], "outer_terrain_steppe_mountain"),

	("village_38", sf_generate, "none", "none", (0.00, 0.00), (100.00, 100.00), -100.0, "0x0000000220031f6300076dda000056f100004f6d000070b3", [], [], "outer_terrain_plain_farmountain"),

	("village_39", sf_generate, "none", "none", (0.00, 0.00), (100.00, 100.00), -100.0, "0x000000013003e5990005fd78000069670000446c00007476", [], [], "outer_terrain_plain_farmountain"),

	("village_40", sf_generate, "none", "none", (0.00, 0.00), (100.00, 100.00), -100.0, "0x0000000220031f6300076dda000056f100004f6d000070b3", [], [], "outer_terrain_plain_farmountain"),

	("village_41", sf_generate, "none", "none", (0.00, 0.00), (100.00, 100.00), -100.0, "0x000000022000a3e300062d8d0000444e0000276e00006eb1", [], [], "outer_terrain_steppe_mountain"),

	("village_42", sf_generate, "none", "none", (0.00, 0.00), (100.00, 100.00), -100.0, "0x000000022007b23200062d8d000060b900003b8b00006c93", [], [], "outer_terrain_steppe_mountain"),

	("village_43", sf_generate, "none", "none", (0.00, 0.00), (100.00, 100.00), -100.0, "0x000000022000320e0005856300001d770000792700002aa1", [], [], "outer_terrain_steppe"),

	("village_44", sf_generate, "none", "none", (0.00, 0.00), (100.00, 100.00), -100.0, "0x00000002200020200005c574000075480000002d00004be7", [], [], "outer_terrain_steppe"),

	("village_45", sf_generate, "none", "none", (0.00, 0.00), (100.00, 100.00), -100.0, "0x000000012007a3df0004e52b0000167700005180000051ea", [], [], "outer_terrain_steppe"),

	("village_46", sf_generate, "none", "none", (0.00, 0.00), (100.00, 100.00), -100.0, "0x00000002300019500006c1b4000065c700002bea0000154e", [], [], "sea_outer_terrain_2"),

	("village_47", sf_generate, "none", "none", (0.00, 0.00), (100.00, 100.00), -100.0, "0x000000022004d36300077dd600002e08000036ab00004651", [], [], "outer_terrain_steppe_mountain"),

	("village_48", sf_generate, "none", "none", (0.00, 0.00), (100.00, 100.00), -100.0, "0x00000001b0051ebc00062d8b0000570d00005b3900001ae1", [], [], "outer_terrain_plain"),

	("village_49", sf_generate, "none", "none", (0.00, 0.00), (100.00, 100.00), -100.0, "0x0000000020000a63000806030000537900001eba00001f25", [], [], "outer_terrain_steppe"),

	("village_50", sf_generate, "none", "none", (0.00, 0.00), (100.00, 100.00), -100.0, "0x0000000031059a0d0004792000005c3a00004df500000dbc", [], [], "outer_terrain_plain"),

	("village_51", sf_generate, "none", "none", (0.00, 0.00), (100.00, 100.00), -100.0, "0x0000000030000f630005796000003b2200004fa800002ab1", [], [], "outer_terrain_plain"),

	("village_52", sf_generate, "none", "none", (0.00, 0.00), (100.00, 100.00), -100.0, "0x0000000220011de30005655900002c2300003b2400000d47", [], [], "outer_terrain_steppe_mountain"),

	("village_53", sf_generate, "none", "none", (0.00, 0.00), (100.00, 100.00), -100.0, "0x0000000030081763000589620000338e00004f2c00005cfb", [], [], "outer_terrain_plain"),

	("village_54", sf_generate, "none", "none", (0.00, 0.00), (100.00, 100.00), -100.0, "0x00000002300032300005c5740000243e000056aa00003a7a", [], [], "outer_terrain_plain"),

	("village_55", sf_generate, "none", "none", (0.00, 0.00), (100.00, 100.00), -100.0, "0x00000002300019500006c1b4000065c700002bea0000154e", [], [], "outer_terrain_plain"),

	("village_56", sf_generate, "none", "none", (0.00, 0.00), (100.00, 100.00), -100.0, "0x00000002300296320006b5aa00006f3200003a5000004fed", [], [], "outer_terrain_thir_new"),

	("village_57", sf_generate, "none", "none", (0.00, 0.00), (100.00, 100.00), -100.0, "0x00000002300027b200065d9700004dcf0000212800001bf0", [], [], "outer_terrain_plain"),

	("village_58", sf_generate, "none", "none", (0.00, 0.00), (100.00, 100.00), -100.0, "0x00000001500410320005a96800006b5300004edc00000d11", [], [], "outer_terrain_desert"),

	("village_59", sf_generate, "none", "none", (0.00, 0.00), (100.00, 100.00), -100.0, "0x00000000300005000004b53500007e3100007ff700000359", [], [], "outer_terrain_plain"),

	("village_60", sf_generate, "none", "none", (0.00, 0.00), (100.00, 100.00), -100.0, "0x00000001500410320005a96800006b5300004edc00000d11", [], [], "outer_terrain_desert"),

	("village_61", sf_generate, "none", "none", (0.00, 0.00), (100.00, 100.00), -100.0, "0x00000001500410320005a96800006b5300004edc00000d11", [], [], "outer_terrain_desert"),

	("village_62", sf_generate, "none", "none", (0.00, 0.00), (100.00, 100.00), -100.0, "0x00000001500410320005a96800006b5300004edc00000d11", [], [], "outer_terrain_desert"),

	("village_63", sf_generate, "none", "none", (0.00, 0.00), (100.00, 100.00), -100.0, "0x00000001500410320005a96800006b5300004edc00000d11", [], [], "outer_terrain_desert"),

	("village_64", sf_generate, "none", "none", (0.00, 0.00), (100.00, 100.00), -100.0, "0x00000001500410320005a96800006b5300004edc00000d11", [], [], "outer_terrain_desert"),

	("village_65", sf_generate, "none", "none", (0.00, 0.00), (100.00, 100.00), -100.0, "0x00000001500410320005a96800006b5300004edc00000d11", [], [], "outer_terrain_desert"),

	("village_66", sf_generate, "none", "none", (0.00, 0.00), (100.00, 100.00), -100.0, "0x00000001500410320005a96800006b5300004edc00000d11", [], [], "outer_terrain_desert"),

	("village_67", sf_generate, "none", "none", (0.00, 0.00), (100.00, 100.00), -100.0, "0x00000001500410320005a96800006b5300004edc00000d11", [], [], "outer_terrain_desert"),

	("village_68", sf_generate, "none", "none", (0.00, 0.00), (100.00, 100.00), -100.0, "0x000000012002a0b20004992700006e54000007fe00001fd2", [], [], "outer_terrain_steppe"),

	("village_69", sf_generate, "none", "none", (0.00, 0.00), (100.00, 100.00), -100.0, "0x00000002200005000005f57b00005885000046bd00006d9c", [], [], "outer_terrain_beach"),

	("village_70", sf_generate, "none", "none", (0.00, 0.00), (100.00, 100.00), -100.0, "0x00000001500410320005a96800006b5300004edc00000d11", [], [], "outer_terrain_desert"),

	("village_71", sf_generate, "none", "none", (0.00, 0.00), (100.00, 100.00), -100.0, "0x00000001500410320005a96800006b5300004edc00000d11", [], [], "outer_terrain_desert"),

	("village_72", sf_generate, "none", "none", (0.00, 0.00), (100.00, 100.00), -100.0, "0x00000001500410320005a96800006b5300004edc00000d11", [], [], "outer_terrain_desert"),

	("village_73", sf_generate, "none", "none", (0.00, 0.00), (100.00, 100.00), -100.0, "0x000000012002cd900005314c00001f6d00006d7700003493", [], [], "outer_terrain_thir_new"),

	("village_74", sf_generate, "none", "none", (0.00, 0.00), (100.00, 100.00), -100.0, "0x00000002300794320005f17c00003187000051540000350a", [], [], "outer_terrain_plain"),

	("village_75", sf_generate, "none", "none", (0.00, 0.00), (100.00, 100.00), -100.0, "0x000000013002541c00062d8b00000a01000068cb00006d9b", [], [], "outer_terrain_plain"),

	("village_76", sf_generate, "none", "none", (0.00, 0.00), (100.00, 100.00), -100.0, "0x000000022007a7b200045d19000004920000076d00003b0a", [], [], "outer_terrain_steppe_mountain"),

	("village_77", sf_generate, "none", "none", (0.00, 0.00), (100.00, 100.00), -100.0, "0x000000023009629a0005615800005564000023590000579e", [], [], "outer_terrain_plain"),

	("village_78", sf_generate, "none", "none", (0.00, 0.00), (100.00, 100.00), -100.0, "0x00000001500410320005a96800006b5300004edc00000d11", [], [], "outer_terrain_desert"),

	("village_79", sf_generate, "none", "none", (0.00, 0.00), (100.00, 100.00), -100.0, "0x000000012002cd900005314c00001f6d00006d7700003493", [], [], "outer_terrain_thir_new"),

	("village_80", sf_generate, "none", "none", (0.00, 0.00), (100.00, 100.00), -100.0, "0x0000000030000f630005796000003b2200004fa800002ab1", [], [], "outer_terrain_plain"),

	("village_81", sf_generate, "none", "none", (0.00, 0.00), (100.00, 100.00), -100.0, "0x00000000300005000004b53500007e3100007ff700000359", [], [], "outer_terrain_plain"),

	("village_82", sf_generate, "none", "none", (0.00, 0.00), (100.00, 100.00), -100.0, "0x000000013002541c00062d8b00000a01000068cb00006d9b", [], [], "outer_terrain_plain"),

	("village_83", sf_generate, "none", "none", (0.00, 0.00), (100.00, 100.00), -100.0, "0x0000000030000f630005796000003b2200004fa800002ab1", [], [], "outer_terrain_plain"),

	("village_84", sf_generate, "none", "none", (0.00, 0.00), (100.00, 100.00), -100.0, "0x0000000130069b270004dd390000689b00002d3b00001876", [], [], "outer_terrain_plain_farmountain"),

	("village_85", sf_generate, "none", "none", (0.00, 0.00), (100.00, 100.00), -100.0, "0x0000000030000f630005796000003b2200004fa800002ab1", [], [], "outer_terrain_plain"),

	("village_86", sf_generate, "none", "none", (0.00, 0.00), (100.00, 100.00), -100.0, "0x00000002300798320006499200002acc000040d70000421d", [], [], "outer_terrain_plain"),

	("village_87", sf_generate, "none", "none", (0.00, 0.00), (100.00, 100.00), -100.0, "0x000000013001c98a0004dd3000001a5e00005c6200001ec9", [], [], "outer_terrain_plain"),

	("village_88", sf_generate, "none", "none", (0.00, 0.00), (100.00, 100.00), -100.0, "0x000000012002cd900005314c00001f6d00006d7700003493", [], [], "outer_terrain_thir_new"),

	("village_89", sf_generate, "none", "none", (0.00, 0.00), (100.00, 100.00), -100.0, "0x00000001200513940005314c00001f6d00006d7700006698", [], [], "outer_terrain_steppe"),

	("village_90", sf_generate, "none", "none", (0.00, 0.00), (100.00, 100.00), -100.0, "0x000000012002cd900005314c00001f6d00006d7700003493", [], [], "outer_terrain_steppe"),

	("village_91", sf_generate, "none", "none", (0.00, 0.00), (100.00, 100.00), -100.0, "0x000000013002541c00062d8b00000a01000068cb00006d9b", [], [], "outer_terrain_plain"),

	("village_92", sf_generate, "none", "none", (0.00, 0.00), (100.00, 100.00), -100.0, "0x000000023009629a0005615800005564000023590000579e", [], [], "outer_terrain_plain"),

	("village_93", sf_generate, "none", "none", (0.00, 0.00), (100.00, 100.00), -100.0, "0x000000013002541c00062d8b00000a01000068cb00006d9b", [], [], "outer_terrain_plain"),

	("village_94", sf_generate, "none", "none", (0.00, 0.00), (100.00, 100.00), -100.0, "0x0000000020000a63000806030000537900001eba00001f25", [], [], "outer_terrain_steppe"),

	("village_95", sf_generate, "none", "none", (0.00, 0.00), (100.00, 100.00), -100.0, "0x00000002300798320006499200002acc000040d70000421d", [], [], "outer_terrain_plain"),

	("village_96", sf_generate, "none", "none", (0.00, 0.00), (100.00, 100.00), -100.0, "0x00000002300798320006499200002acc000040d70000421d", [], [], "outer_terrain_plain"),

	("village_97", sf_generate, "none", "none", (0.00, 0.00), (100.00, 100.00), -100.0, "0x000000013001b21e0004f13e000042b2000058e400007fce", [], [], "outer_terrain_plain"),

	("village_98", sf_generate, "none", "none", (0.00, 0.00), (100.00, 100.00), -100.0, "0x0000000230035598000761df000058ea000006f3000005e7", [], [], "outer_terrain_plain"),

	("village_99", sf_generate, "none", "none", (0.00, 0.00), (100.00, 100.00), -100.0, "0x0000000020000a63000806030000537900001eba00001f25", [], [], "outer_terrain_steppe"),

	("village_100", sf_generate, "none", "none", (0.00, 0.00), (100.00, 100.00), -100.0, "0x0000000230035598000761df000058ea000006f3000005e7", [], [], "outer_terrain_plain"),

	("village_101", sf_generate, "none", "none", (0.00, 0.00), (100.00, 100.00), -100.0, "0x0000000030000f630005796000003b2200004fa800002ab1", [], [], "outer_terrain_plain"),

	("village_102", sf_generate, "none", "none", (0.00, 0.00), (100.00, 100.00), -100.0, "0x0000000230035598000761df000058ea000006f3000005e7", [], [], "outer_terrain_plain"),

	("village_103", sf_generate, "none", "none", (0.00, 0.00), (100.00, 100.00), -100.0, "0x0000000020000a63000806030000537900001eba00001f25", [], [], "outer_terrain_steppe"),

	("village_104", sf_generate, "none", "none", (0.00, 0.00), (100.00, 100.00), -100.0, "0x0000000030000f630005796000003b2200004fa800002ab1", [], [], "outer_terrain_plain"),

	("village_105", sf_generate, "none", "none", (0.00, 0.00), (100.00, 100.00), -100.0, "0x0000000030000f630005796000003b2200004fa800002ab1", [], [], "outer_terrain_plain"),

	("village_106", sf_generate, "none", "none", (0.00, 0.00), (100.00, 100.00), -100.0, "0x0000000030000f630005796000003b2200004fa800002ab1", [], [], "outer_terrain_plain"),

	("village_107", sf_generate, "none", "none", (0.00, 0.00), (100.00, 100.00), -100.0, "0x0000000230035598000761df000058ea000006f3000005e7", [], [], "outer_terrain_plain"),

	("village_108", sf_generate, "none", "none", (0.00, 0.00), (100.00, 100.00), -100.0, "0x0000000230035598000761df000058ea000006f3000005e7", [], [], "outer_terrain_plain"),

	("village_109", sf_generate, "none", "none", (0.00, 0.00), (100.00, 100.00), -100.0, "0x0000000230035598000761df000058ea000006f3000005e7", [], [], "outer_terrain_plain"),

	("village_110", sf_generate, "none", "none", (0.00, 0.00), (100.00, 100.00), -100.0, "0x0000000020000a63000806030000537900001eba00001f25", [], [], "outer_terrain_steppe"),

	("village_111", sf_generate, "none", "none", (0.00, 0.00), (100.00, 100.00), -100.0, "0x0000000030000f630005796000003b2200004fa800002ab1", [], [], "outer_terrain_plain"),

	("village_112", sf_generate, "none", "none", (0.00, 0.00), (100.00, 100.00), -100.0, "0x00000000300005000004b53500007e3100007ff700000359", [], [], "outer_terrain_plain"),

	("village_113", sf_generate, "none", "none", (0.00, 0.00), (100.00, 100.00), -100.0, "0x000000013001c98a0004dd3000001a5e00005c6200001ec9", [], [], "outer_terrain_plain"),

	("village_114", sf_generate, "none", "none", (0.00, 0.00), (100.00, 100.00), -100.0, "0x000000022007a7b200045d19000004920000076d00003b0a", [], [], "outer_terrain_steppe_mountain"),

	("village_115", sf_generate, "none", "none", (0.00, 0.00), (100.00, 100.00), -100.0, "0x000000022007a7b200045d19000004920000076d00003b0a", [], [], "outer_terrain_steppe_mountain"),

	("village_116", sf_generate, "none", "none", (0.00, 0.00), (100.00, 100.00), -100.0, "0x0000000230079cb20005394e00001ef90000753000000731", [], [], "outer_terrain_thir_new"),

	("village_117", sf_generate, "none", "none", (0.00, 0.00), (100.00, 100.00), -100.0, "0x0000000220031f6300076dda000056f100004f6d000070b3", [], [], "outer_terrain_plain_farmountain"),

	("village_118", sf_generate, "none", "none", (0.00, 0.00), (100.00, 100.00), -100.0, "0x00000002300019500006c1b4000065c700002bea0000154e", [], [], "sea_outer_terrain_2"),

	("village_119", sf_generate, "none", "none", (0.00, 0.00), (100.00, 100.00), -100.0, "0x000000023009629a0005615800005564000023590000579e", [], [], "outer_terrain_plain"),

	("village_120", sf_generate, "none", "none", (0.00, 0.00), (100.00, 100.00), -100.0, "0x0000000230079cb20005394e00001ef90000753000000731", [], [], "outer_terrain_thir_new"),

	("village_121", sf_generate, "none", "none", (0.00, 0.00), (100.00, 100.00), -100.0, "0x0000000230079cb20005394e00001ef90000753000000731", [], [], "outer_terrain_thir_new"),

	("village_122", sf_generate, "none", "none", (0.00, 0.00), (100.00, 100.00), -100.0, "0x0000000230079cb20005394e00001ef90000753000000731", [], [], "outer_terrain_thir_new"),

	("village_123", sf_generate, "none", "none", (0.00, 0.00), (100.00, 100.00), -100.0, "0x000000022007b23200062d8d000060b900003b8b00006c93", [], [], "outer_terrain_steppe_mountain"),

	("village_124", sf_generate, "none", "none", (0.00, 0.00), (100.00, 100.00), -100.0, "0x00000001500410320005a96800006b5300004edc00000d11", [], [], "outer_terrain_desert"),

	("village_125", sf_generate, "none", "none", (0.00, 0.00), (100.00, 100.00), -100.0, "0x00000000300005000004b53500007e3100007ff700000359", [], [], "outer_terrain_plain"),

	("village_126", sf_generate, "none", "none", (0.00, 0.00), (100.00, 100.00), -100.0, "0x000000012002a0b20004992700006e54000007fe00001fd2", [], [], "outer_terrain_steppe"),

	("village_127", sf_generate, "none", "none", (0.00, 0.00), (100.00, 100.00), -100.0, "0x000000012002a0b20004992700006e54000007fe00001fd2", [], [], "outer_terrain_steppe"),

	("village_128", sf_generate, "none", "none", (0.00, 0.00), (100.00, 100.00), -100.0, "0x000000022007b23200062d8d000060b900003b8b00006c93", [], [], "outer_terrain_steppe_mountain"),

	("village_129", sf_generate, "none", "none", (0.00, 0.00), (100.00, 100.00), -100.0, "0x000000022000320e0005856300001d770000792700002aa1", [], [], "outer_terrain_steppe"),

	("village_130", sf_generate, "none", "none", (0.00, 0.00), (100.00, 100.00), -100.0, "0x000000023009629a0005615800005564000023590000579e", [], [], "outer_terrain_plain"),

	("village_131", sf_generate, "none", "none", (0.00, 0.00), (100.00, 100.00), -100.0, "0x000000022000320e0005856300001d770000792700002aa1", [], [], "outer_terrain_steppe"),

	("village_132", sf_generate, "none", "none", (0.00, 0.00), (100.00, 100.00), -100.0, "0x000000022000a3e300062d8d0000444e0000276e00006eb1", [], [], "outer_terrain_steppe_mountain"),

	("village_133", sf_generate, "none", "none", (0.00, 0.00), (100.00, 100.00), -100.0, "0x00000001500410320005a96800006b5300004edc00000d11", [], [], "outer_terrain_desert"),

	("village_134", sf_generate, "none", "none", (0.00, 0.00), (100.00, 100.00), -100.0, "0x000000022007b23200062d8d000060b900003b8b00006c93", [], [], "outer_terrain_steppe_mountain"),

	("village_135", sf_generate, "none", "none", (0.00, 0.00), (100.00, 100.00), -100.0, "0x00000001500410320005a96800006b5300004edc00000d11", [], [], "outer_terrain_desert"),

	("village_136", sf_generate, "none", "none", (0.00, 0.00), (100.00, 100.00), -100.0, "0x0000000030000f630005796000003b2200004fa800002ab1", [], [], "outer_terrain_plain"),

	("village_137", sf_generate, "none", "none", (0.00, 0.00), (100.00, 100.00), -100.0, "0x000000012007a3df0004e52b0000167700005180000051ea", [], [], "outer_terrain_steppe"),

	("village_138", sf_generate, "none", "none", (0.00, 0.00), (100.00, 100.00), -100.0, "0x000000022000a3e300062d8d0000444e0000276e00006eb1", [], [], "outer_terrain_steppe_mountain"),

	("village_139", sf_generate, "none", "none", (0.00, 0.00), (100.00, 100.00), -100.0, "0x00000000300005000004b53500007e3100007ff700000359", [], [], "outer_terrain_plain"),

	("village_140", sf_generate, "none", "none", (0.00, 0.00), (100.00, 100.00), -100.0, "0x000000012002a0b20004992700006e54000007fe00001fd2", [], [], "outer_terrain_steppe"),

	("village_141", sf_generate, "none", "none", (0.00, 0.00), (100.00, 100.00), -100.0, "0x0000000020000a63000806030000537900001eba00001f25", [], [], "outer_terrain_steppe"),

	("village_142", sf_generate, "none", "none", (0.00, 0.00), (100.00, 100.00), -100.0, "0x000000022000a3e300062d8d0000444e0000276e00006eb1", [], [], "outer_terrain_steppe_mountain"),

	("village_143", sf_generate, "none", "none", (0.00, 0.00), (100.00, 100.00), -100.0, "0x00000000300005000004b53500007e3100007ff700000359", [], [], "outer_terrain_plain"),

	("village_144", sf_generate, "none", "none", (0.00, 0.00), (100.00, 100.00), -100.0, "0x00000000300005000004b53500007e3100007ff700000359", [], [], "outer_terrain_plain"),

	("village_145", sf_generate, "none", "none", (0.00, 0.00), (100.00, 100.00), -100.0, "0x00000000300005000004b53500007e3100007ff700000359", [], [], "outer_terrain_plain"),

	("village_146", sf_generate, "none", "none", (0.00, 0.00), (100.00, 100.00), -100.0, "0x000000012007a3df0004e52b0000167700005180000051ea", [], [], "outer_terrain_steppe"),

	("village_147", sf_generate, "none", "none", (0.00, 0.00), (100.00, 100.00), -100.0, "0x00000001500410320005a96800006b5300004edc00000d11", [], [], "outer_terrain_desert"),

	("village_148", sf_generate, "none", "none", (0.00, 0.00), (100.00, 100.00), -100.0, "0x000000022000320e0005856300001d770000792700002aa1", [], [], "outer_terrain_steppe"),

	("village_149", sf_generate, "none", "none", (0.00, 0.00), (100.00, 100.00), -100.0, "0x000000012007a3df0004e52b0000167700005180000051ea", [], [], "outer_terrain_steppe"),

	("village_150", sf_generate, "none", "none", (0.00, 0.00), (100.00, 100.00), -100.0, "0x00000001500410320005a96800006b5300004edc00000d11", [], [], "outer_terrain_desert"),

	("village_151", sf_generate, "none", "none", (0.00, 0.00), (100.00, 100.00), -100.0, "0x00000002200020200005c574000075480000002d00004be7", [], [], "outer_terrain_steppe"),

	("village_152", sf_generate, "none", "none", (0.00, 0.00), (100.00, 100.00), -100.0, "0x00000002200020200005c574000075480000002d00004be7", [], [], "outer_terrain_steppe"),

	("village_153", sf_generate, "none", "none", (0.00, 0.00), (100.00, 100.00), -100.0, "0x00000002200020200005c574000075480000002d00004be7", [], [], "outer_terrain_steppe"),

	("village_154", sf_generate, "none", "none", (0.00, 0.00), (100.00, 100.00), -100.0, "0x000000012007a3df0004e52b0000167700005180000051ea", [], [], "outer_terrain_steppe"),

	("village_155", sf_generate, "none", "none", (0.00, 0.00), (100.00, 100.00), -100.0, "0x000000005a0932320004cd3000004e7d00007d6e00006c58", [], [], "outer_terrain_desert"),

	("village_156", sf_generate, "none", "none", (0.00, 0.00), (100.00, 100.00), -100.0, "0x00000002200020200005c574000075480000002d00004be7", [], [], "outer_terrain_steppe"),

	("village_157", sf_generate, "none", "none", (0.00, 0.00), (100.00, 100.00), -100.0, "0x000000022000a3e300062d8d0000444e0000276e00006eb1", [], [], "outer_terrain_steppe_mountain"),

	("village_158", sf_generate, "none", "none", (0.00, 0.00), (100.00, 100.00), -100.0, "0x00000002200020200005c574000075480000002d00004be7", [], [], "outer_terrain_steppe"),

	("village_159", sf_generate, "none", "none", (0.00, 0.00), (100.00, 100.00), -100.0, "0x0000000030000f630005796000003b2200004fa800002ab1", [], [], "outer_terrain_plain"),

	("village_160", sf_generate, "none", "none", (0.00, 0.00), (100.00, 100.00), -100.0, "0x00000002300019500006c1b4000065c700002bea0000154e", [], [], "sea_outer_terrain_2"),

	("village_161", sf_generate, "none", "none", (0.00, 0.00), (100.00, 100.00), -100.0, "0x000000012002cd900005314c00001f6d00006d7700003493", [], [], "outer_terrain_thir_new"),

	("village_162", sf_generate, "none", "none", (0.00, 0.00), (100.00, 100.00), -100.0, "0x000000013001c98a0004dd3000001a5e00005c6200001ec9", [], [], "outer_terrain_plain"),

	("village_163", sf_generate, "none", "none", (0.00, 0.00), (100.00, 100.00), -100.0, "0x000000013001c98a0004dd3000001a5e00005c6200001ec9", [], [], "outer_terrain_plain"),

	("village_164", sf_generate, "none", "none", (0.00, 0.00), (100.00, 100.00), -100.0, "0x000000013001c98a0004dd3000001a5e00005c6200001ec9", [], [], "outer_terrain_plain"),

	("village_165", sf_generate, "none", "none", (0.00, 0.00), (100.00, 100.00), -100.0, "0x00000001500410320005a96800006b5300004edc00000d11", [], [], "outer_terrain_desert"),

	("village_166", sf_generate, "none", "none", (0.00, 0.00), (100.00, 100.00), -100.0, "0x00000002300018e38005e58300000376000027e70000015c", [], [], "outer_terrain_thir_new"),

	("village_167", sf_generate, "none", "none", (0.00, 0.00), (100.00, 100.00), -100.0, "0x00000001500410320005a96800006b5300004edc00000d11", [], [], "outer_terrain_desert"),

	("village_168", sf_generate, "none", "none", (0.00, 0.00), (100.00, 100.00), -100.0, "0x00000001500410320005a96800006b5300004edc00000d11", [], [], "outer_terrain_desert"),

	("village_169", sf_generate, "none", "none", (0.00, 0.00), (100.00, 100.00), -100.0, "0x00000001500410320005a96800006b5300004edc00000d11", [], [], "outer_terrain_desert"),

	("village_170", sf_generate, "none", "none", (0.00, 0.00), (100.00, 100.00), -100.0, "0x0000000030081763000589620000338e00004f2c00005cfb", [], [], "outer_terrain_plain"),

	("village_171", sf_generate, "none", "none", (0.00, 0.00), (100.00, 100.00), -100.0, "0x00000001200513940005314c00001f6d00006d7700006698", [], [], "outer_terrain_steppe"),

	("village_172", sf_generate, "none", "none", (0.00, 0.00), (100.00, 100.00), -100.0, "0x00000000300005000004b53500007e3100007ff700000359", [], [], "outer_terrain_plain"),

	("village_173", sf_generate, "none", "none", (0.00, 0.00), (100.00, 100.00), -100.0, "0x00000001200513940005314c00001f6d00006d7700006698", [], [], "outer_terrain_steppe"),

	("village_174", sf_generate, "none", "none", (0.00, 0.00), (100.00, 100.00), -100.0, "0x000000012002a0b20004992700006e54000007fe00001fd2", [], [], "outer_terrain_steppe"),

	("village_175", sf_generate, "none", "none", (0.00, 0.00), (100.00, 100.00), -100.0, "0x00000001200513940005314c00001f6d00006d7700006698", [], [], "outer_terrain_steppe"),

	("village_176", sf_generate, "none", "none", (0.00, 0.00), (100.00, 100.00), -100.0, "0x00000001200513940005314c00001f6d00006d7700006698", [], [], "outer_terrain_steppe"),

	("village_177", sf_generate, "none", "none", (0.00, 0.00), (100.00, 100.00), -100.0, "0x00000001500410320005a96800006b5300004edc00000d11", [], [], "outer_terrain_desert"),

	("village_178", sf_generate, "none", "none", (0.00, 0.00), (100.00, 100.00), -100.0, "0x00000001200513940005314c00001f6d00006d7700006698", [], [], "outer_terrain_steppe"),

	("village_179", sf_generate, "none", "none", (0.00, 0.00), (100.00, 100.00), -100.0, "0x000000012002a0b20004992700006e54000007fe00001fd2", [], [], "outer_terrain_steppe"),

	("village_180", sf_generate, "none", "none", (0.00, 0.00), (100.00, 100.00), -100.0, "0x00000001500410320005a96800006b5300004edc00000d11", [], [], "outer_terrain_desert"),

	("village_181", sf_generate, "none", "none", (0.00, 0.00), (100.00, 100.00), -100.0, "0x00000000300005000004b53500007e3100007ff700000359", [], [], "outer_terrain_plain"),

	("village_182", sf_generate, "none", "none", (0.00, 0.00), (100.00, 100.00), -100.0, "0x000000012002a0b20004992700006e54000007fe00001fd2", [], [], "outer_terrain_steppe"),

	("village_183", sf_generate, "none", "none", (0.00, 0.00), (100.00, 100.00), -100.0, "0x00000001500410320005a96800006b5300004edc00000d11", [], [], "outer_terrain_desert"),

	("village_184", sf_generate, "none", "none", (0.00, 0.00), (100.00, 100.00), -100.0, "0x00000001200513940005314c00001f6d00006d7700006698", [], [], "outer_terrain_steppe"),

	("village_185", sf_generate, "none", "none", (0.00, 0.00), (100.00, 100.00), -100.0, "0x00000001200513940005314c00001f6d00006d7700006698", [], [], "outer_terrain_steppe"),

	("village_186", sf_generate, "none", "none", (0.00, 0.00), (100.00, 100.00), -100.0, "0x00000001200513940005314c00001f6d00006d7700006698", [], [], "outer_terrain_steppe"),

	("village_187", sf_generate, "none", "none", (0.00, 0.00), (100.00, 100.00), -100.0, "0x00000000300005000004b53500007e3100007ff700000359", [], [], "outer_terrain_plain"),

	("village_188", sf_generate, "none", "none", (0.00, 0.00), (100.00, 100.00), -100.0, "0x00000001500410320005a96800006b5300004edc00000d11", [], [], "outer_terrain_desert"),

	("village_189", sf_generate, "none", "none", (0.00, 0.00), (100.00, 100.00), -100.0, "0x000000012002a0b20004992700006e54000007fe00001fd2", [], [], "outer_terrain_steppe"),

	("village_190", sf_generate, "none", "none", (0.00, 0.00), (100.00, 100.00), -100.0, "0x00000001200513940005314c00001f6d00006d7700006698", [], [], "outer_terrain_steppe"),

	("village_191", sf_generate, "none", "none", (0.00, 0.00), (100.00, 100.00), -100.0, "0x00000000300005000004b53500007e3100007ff700000359", [], [], "outer_terrain_plain"),

	("village_192", sf_generate, "none", "none", (0.00, 0.00), (100.00, 100.00), -100.0, "0x000000012002a0b20004992700006e54000007fe00001fd2", [], [], "outer_terrain_steppe"),

	("village_193", sf_generate, "none", "none", (0.00, 0.00), (100.00, 100.00), -100.0, "0x0000000030081763000589620000338e00004f2c00005cfb", [], [], "outer_terrain_plain"),

	("village_194", sf_generate, "none", "none", (0.00, 0.00), (100.00, 100.00), -100.0, "0x000000022007b23200062d8d000060b900003b8b00006c93", [], [], "outer_terrain_steppe_mountain"),

	("village_195", sf_generate, "none", "none", (0.00, 0.00), (100.00, 100.00), -100.0, "0x000000013001b21e0004f13e000042b2000058e400007fce", [], [], "outer_terrain_plain"),

	("village_196", sf_generate, "none", "none", (0.00, 0.00), (100.00, 100.00), -100.0, "0x000000013001b21e0004f13e000042b2000058e400007fce", [], [], "outer_terrain_plain"),

	("village_197", sf_generate, "none", "none", (0.00, 0.00), (100.00, 100.00), -100.0, "0x000000012002cd900005314c00001f6d00006d7700003493", [], [], "outer_terrain_steppe"),

	("village_198", sf_generate, "none", "none", (0.00, 0.00), (100.00, 100.00), -100.0, "0x000000012002cd900005314c00001f6d00006d7700003493", [], [], "outer_terrain_steppe"),

	("village_199", sf_generate, "none", "none", (0.00, 0.00), (100.00, 100.00), -100.0, "0x000000012002cd900005314c00001f6d00006d7700003493", [], [], "outer_terrain_steppe"),

	("village_200", sf_generate, "none", "none", (0.00, 0.00), (100.00, 100.00), -100.0, "0x00000002300019500006c1b4000065c700002bea0000154e", [], [], "sea_outer_terrain_2"),

	("village_201", sf_generate, "none", "none", (0.00, 0.00), (100.00, 100.00), -100.0, "0x000000012002cd900005314c00001f6d00006d7700003493", [], [], "outer_terrain_steppe"),

	("village_202", sf_generate, "none", "none", (0.00, 0.00), (100.00, 100.00), -100.0, "0x0000000020000a63000806030000537900001eba00001f25", [], [], "outer_terrain_steppe"),

	("village_203", sf_generate, "none", "none", (0.00, 0.00), (100.00, 100.00), -100.0, "0x0000000030000f630005796000003b2200004fa800002ab1", [], [], "outer_terrain_plain"),

	("village_204", sf_generate, "none", "none", (0.00, 0.00), (100.00, 100.00), -100.0, "0x00000002300019500006c1b4000065c700002bea0000154e", [], [], "sea_outer_terrain_2"),

	("village_205", sf_generate, "none", "none", (0.00, 0.00), (100.00, 100.00), -100.0, "0x000000012002cd900005314c00001f6d00006d7700003493", [], [], "outer_terrain_steppe"),

	("village_206", sf_generate, "none", "none", (0.00, 0.00), (100.00, 100.00), -100.0, "0x000000012002cd900005314c00001f6d00006d7700003493", [], [], "outer_terrain_steppe"),

	("village_207", sf_generate, "none", "none", (0.00, 0.00), (100.00, 100.00), -100.0, "0x000000012002cd900005314c00001f6d00006d7700003493", [], [], "outer_terrain_steppe"),

	("village_208", sf_generate, "none", "none", (0.00, 0.00), (100.00, 100.00), -100.0, "0x000000012002a0b20004992700006e54000007fe00001fd2", [], [], "outer_terrain_steppe"),

	("village_209", sf_generate, "none", "none", (0.00, 0.00), (100.00, 100.00), -100.0, "0x000000012002a0b20004992700006e54000007fe00001fd2", [], [], "outer_terrain_steppe"),

	("village_210", sf_generate, "none", "none", (0.00, 0.00), (100.00, 100.00), -100.0, "0x000000012002a0b20004992700006e54000007fe00001fd2", [], [], "outer_terrain_steppe"),

	("village_211", sf_generate, "none", "none", (0.00, 0.00), (100.00, 100.00), -100.0, "0x000000012002a0b20004992700006e54000007fe00001fd2", [], [], "outer_terrain_steppe"),

	("village_212", sf_generate, "none", "none", (0.00, 0.00), (100.00, 100.00), -100.0, "0x000000012002a0b20004992700006e54000007fe00001fd2", [], [], "outer_terrain_steppe"),

	("field_1", sf_generate, "none", "none", (0.00, 0.00), (100.00, 100.00), -100.0, "0x000000033a059a5a0009525600002005000060e300001175", [], [], "outer_terrain_plain"),

	("field_2", sf_generate, "none", "none", (0.00, 0.00), (100.00, 100.00), -100.0, "0x000000033a079a3f000a3a8000006dfd000030a100006522", [], [], "outer_terrain_steppe"),

	("field_3", sf_generate, "none", "none", (0.00, 0.00), (100.00, 100.00), -100.0, "0x30054da28004050000005a76800022aa00002e3b", [], [], "outer_terrain_steppe"),

	("field_4", sf_generate, "none", "none", (0.00, 0.00), (100.00, 100.00), -100.0, "0x30054da28004050000005a76800022aa00002e3b", [], [], "outer_terrain_steppe"),

	("field_5", sf_generate, "none", "none", (0.00, 0.00), (100.00, 100.00), -100.0, "0x30054da28004050000005a76800022aa00002e3b", [], [], "outer_terrain_steppe"),

	("test2", sf_generate, "none", "none", (0.00, 0.00), (100.00, 100.00), -100.0, "0x00000000b0078cb20003fd0000005e480000288c0000286f", [], [], "outer_terrain_steppe"),

	("test3", sf_generate, "none", "none", (0.00, 0.00), (100.00, 100.00), -100.0, "0x00000000b00511d98004b12e0000039f00004e6300005c7d", [], [], "outer_terrain_plain"),

	("multi_scene_1", sf_generate, "none", "none", (0.00, 0.00), (100.00, 100.00), -100.0, "0x00000002200005000005f57b00005885000046bd00006d9c", [], [], "sea_outer_terrain_2"),

	("multi_scene_2", sf_generate, "none", "none", (0.00, 0.00), (100.00, 100.00), -100.0, "0x000000003c6005000005c5700000076b000010f8000059aa", [], [], "outer_terrain_plain"),

	("multi_scene_3", sf_generate, "none", "none", (0.00, 0.00), (100.00, 100.00), -100.0, "0x000000013002e0b20005154500006e540000235600007b55", [], [], "outer_terrain_plain"),

	("multi_scene_4", sf_generate, "none", "none", (0.00, 0.00), (100.00, 100.00), -100.0, "0x00000001300659630003c8f300003ca000006a8900003c89", [], [], "outer_terrain_plain"),

	("multi_scene_5", sf_generate, "none", "none", (0.00, 0.00), (100.00, 100.00), -100.0, "0x000000023002a1ba0004210900003ca000006a8900007a7b", [], [], "outer_terrain_plain"),

	("multi_scene_6", sf_generate, "none", "none", (0.00, 0.00), (100.00, 100.00), -100.0, "0x00000002300494b200048524000059e80000453300001d32", [], [], "outer_terrain_plain"),

	("multi_scene_7", sf_generate, "none", "none", (0.00, 0.00), (100.00, 100.00), -100.0, "0x0000000130010e0e0005fd84000011c60000285b00005cbe", [], [], "outer_terrain_plain"),

	("multi_scene_8", sf_generate, "none", "none", (0.00, 0.00), (100.00, 100.00), -100.0, "0x0000000020004db18004611400005c918000397b00004c2e", [], [], "outer_terrain_plain"),

	("multi_scene_9", sf_generate, "none", "none", (0.00, 0.00), (100.00, 100.00), -100.0, "0x00000000400032320003c0f300001f9e000011180000031c", [], [], "outer_terrain_snow"),

	("multi_scene_10", sf_generate, "none", "none", (0.00, 0.00), (100.00, 100.00), -100.0, "0x000000003009cde1000599630000423b00005756000000af", [], [], "outer_terrain_plain"),

	("multi_scene_11", sf_generate, "none", "none", (0.00, 0.00), (100.00, 100.00), -100.0, "0x0000000030015f2b000350d4000011a4000017ee000054af", [], [], "outer_terrain_plain"),

	("multi_scene_12", sf_generate, "none", "none", (0.00, 0.00), (100.00, 100.00), -100.0, "0x000000013003d7e30005053f00003b4e0000146300006e84", [], [], "outer_terrain_beach"),

	("multi_scene_13", sf_generate, "none", "none", (0.00, 0.00), (100.00, 100.00), -100.0, "0x00000001300389800003a4ea000058340000637a0000399b", [], [], "outer_terrain_plain"),

	("multi_scene_14", sf_generate, "none", "none", (0.00, 0.00), (100.00, 100.00), -100.0, "0x0000000040000c910003e8fa0000538900003e9e00005301", [], [], "outer_terrain_snow"),

	("multi_scene_15", sf_generate, "none", "none", (0.00, 0.00), (100.00, 100.00), -100.0, "0x00000000500b1d158005394c00001230800072880000018f", [], [], "outer_terrain_desert"),

	("multi_scene_16", sf_generate, "none", "none", (0.00, 0.00), (100.00, 100.00), -100.0, "0x00000000d007abd20002c8b1000050c50000752a0000788c", [], [], "outer_terrain_desert"),

	("multi_scene_17", sf_generate, "none", "none", (0.00, 0.00), (100.00, 100.00), -100.0, "0x00000002200005000005f57b00005885000046bd00006d9c", [], [], "outer_terrain_plain"),

	("multi_scene_18", sf_generate|sf_muddy_water, "none", "none", (0.00, 0.00), (100.00, 100.00), -100.0, "0x00000000b00037630002308c00000c9400005d4c00000f3a", [], [], "outer_terrain_plain"),

	("multi_scene_19", sf_generate, "none", "none", (0.00, 0.00), (100.00, 100.00), -100.0, "0x00000001300389800003a4ea000058340000637a0000399b", [], [], "outer_terrain_plain"),

	("multi_scene_20", sf_generate, "none", "none", (0.00, 0.00), (100.00, 100.00), -100.0, "0x000000013002ab630004651800000d7a00007f3100002701", [], [], "outer_terrain_plain"),

	("random_multi_plain_medium", sf_generate|sf_randomize|sf_auto_entry_points, "none", "none", (0.00, 0.00), (240.00, 240.00), -0.5, "0x00000001394018dd000649920004406900002920000056d7", [], [], "outer_terrain_plain"),

	("random_multi_plain_large", sf_generate|sf_randomize|sf_auto_entry_points, "none", "none", (0.00, 0.00), (240.00, 240.00), -0.5, "0x000000013a001853000aa6a40004406900002920001e4f81", [], [], "outer_terrain_plain"),

	("random_multi_steppe_medium", sf_generate|sf_randomize|sf_auto_entry_points, "none", "none", (0.00, 0.00), (100.00, 100.00), -0.5, "0x0000000128601ae300063d8f0004406900002920001e4f81", [], [], "outer_terrain_steppe"),

	("random_multi_steppe_large", sf_generate|sf_randomize|sf_auto_entry_points, "none", "none", (0.00, 0.00), (100.00, 100.00), -0.5, "0x000000012a00d8630009fe7f0004406900002920001e4f81", [], [], "outer_terrain_steppe"),

	("multiplayer_maps_end", sf_generate, "none", "none", (0.00, 0.00), (100.00, 100.00), -100.0, "0x00000001300389800003a4ea000058340000637a0000399b", [], [], "outer_terrain_plain"),

	("wedding", sf_indoors, "castle_h_interior_a", "bo_castle_h_interior_a", (-100.00, -100.00), (100.00, 100.00), -100.0, "0", [], []),

	("lair_steppe_bandits", sf_generate, "none", "none", (0.00, 0.00), (100.00, 100.00), -100.0, "0x00000000200c69ac80043d0d0000556b0000768400003ea9", [], [], "outer_terrain_steppe"),

	("lair_taiga_bandits", sf_generate, "none", "none", (0.00, 0.00), (100.00, 100.00), -100.0, "0x000000004c079c3e000499280000420f0000495d000048d6", [], [], "outer_terrain_snow"),

	("lair_desert_bandits", sf_generate, "none", "none", (0.00, 0.00), (100.00, 100.00), -100.0, "0x000000005024cd120005595400003882000037a90000673e", [], [], "outer_terrain_desert_rocky"),

	("lair_forest_bandits", sf_generate, "none", "none", (0.00, 0.00), (100.00, 100.00), -100.0, "0x00000000300005000005194600005b6f000052a900000129", [], [], "outer_terrain_plain"),

	("lair_mountain_bandits", sf_generate, "none", "none", (0.00, 0.00), (100.00, 100.00), -100.0, "0x00000000200434070004450c000022bf00006ad6000060ed", [], [], "outer_terrain_steppe"),

	("lair_sea_raiders", sf_generate, "none", "none", (0.00, 0.00), (100.00, 100.00), -100.0, "0x00000000b00562e200040900000063f40000679f00006cda", [], [], "outer_terrain_thir_new"),

	("quick_battle_scene_1", sf_generate, "none", "none", (0.00, 0.00), (120.00, 120.00), -100.0, "0x000000023002dee300045d1d000001bf0000299a0000638f", [], [], "outer_terrain_plain"),

	("quick_battle_scene_2", sf_generate, "none", "none", (0.00, 0.00), (120.00, 120.00), -100.0, "0x0000000250001d630005114300006228000053bf00004eb9", [], [], "outer_terrain_desert_b"),

	("quick_battle_scene_3", sf_generate, "none", "none", (0.00, 0.00), (120.00, 120.00), -100.0, "0x000000023002b76300046d2400000190000076300000692a", [], [], "outer_terrain_plain"),

	("quick_battle_scene_4", sf_generate, "none", "none", (0.00, 0.00), (120.00, 120.00), -100.0, "0x000000025a00f23700057d5f00006d6a000050ba000036df", [], [], "outer_terrain_desert_b"),

	("quick_battle_scene_5", sf_generate, "none", "none", (0.00, 0.00), (100.00, 100.00), -100.0, "0x000000012007985300055550000064d500005c060000759e", [], [], "outer_terrain_plain"),

	("quick_battle_maps_end", sf_generate, "none", "none", (0.00, 0.00), (100.00, 100.00), -100.0, "0x00000001300389800003a4ea000058340000637a0000399b", [], [], "outer_terrain_plain"),

	("tutorial_training_ground", sf_generate, "none", "none", (0.00, 0.00), (120.00, 120.00), -100.0, "0x000000003000050000046d1b0000189f00002a8380006d91", [], [], "outer_terrain_plain_farmountain"),

	("town_1_room", sf_indoors, "viking_interior_tavern_a", "bo_viking_interior_tavern_a", (-100.00, -100.00), (100.00, 100.00), -100.0, "0", [], []),

	("town_5_room", sf_indoors, "interior_town_house_d", "bo_interior_town_house_d", (-100.00, -100.00), (100.00, 100.00), -100.0, "0", ["exit"], []),

	("town_6_room", sf_indoors, "viking_interior_tavern_a", "bo_viking_interior_tavern_a", (-100.00, -100.00), (100.00, 100.00), -100.0, "0", ["exit"], []),

	("town_8_room", sf_indoors, "interior_house_b", "bo_interior_house_b", (-100.00, -100.00), (100.00, 100.00), -100.0, "0", ["exit"], []),

	("town_10_room", sf_indoors, "interior_town_house_steppe_c", "bo_interior_town_house_steppe_c", (-100.00, -100.00), (100.00, 100.00), -100.0, "0", ["exit"], []),

	("town_19_room", sf_indoors, "interior_town_house_steppe_d", "bo_interior_town_house_steppe_d", (-100.00, -100.00), (100.00, 100.00), -100.0, "0", ["exit"], []),

	("meeting_scene_steppe", 0, "ch_meet_steppe_a", "bo_encounter_spot", (-40.00, -40.00), (40.00, 40.00), -100.0, "0", [], []),

	("meeting_scene_plain", 0, "ch_meet_plain_a", "bo_encounter_spot", (-40.00, -40.00), (40.00, 40.00), -100.0, "0", [], []),

	("meeting_scene_snow", 0, "ch_meet_snow_a", "bo_encounter_spot", (-40.00, -40.00), (40.00, 40.00), -100.0, "0", [], []),

	("meeting_scene_desert", 0, "ch_meet_desert_a", "bo_encounter_spot", (-40.00, -40.00), (40.00, 40.00), -100.0, "0", [], []),

	("meeting_scene_steppe_forest", 0, "ch_meet_steppe_a", "bo_encounter_spot", (-40.00, -40.00), (40.00, 40.00), -100.0, "0", [], []),

	("meeting_scene_plain_forest", 0, "ch_meet_plain_a", "bo_encounter_spot", (-40.00, -40.00), (40.00, 40.00), -100.0, "0", [], []),

	("meeting_scene_snow_forest", 0, "ch_meet_snow_a", "bo_encounter_spot", (-40.00, -40.00), (40.00, 40.00), -100.0, "0", [], []),

	("meeting_scene_desert_forest", 0, "ch_meet_desert_a", "bo_encounter_spot", (-40.00, -40.00), (40.00, 40.00), -100.0, "0", [], []),

	("enterprise_tannery", sf_generate, "ch_meet_steppe_a", "bo_encounter_spot", (-40.00, -40.00), (40.00, 40.00), -100.0, "0x000000012004480500040902000041cb00005ae800000ff5", [], []),

	("enterprise_winery", sf_indoors, "winery_interior", "bo_winery_interior", (-40.00, -40.00), (40.00, 40.00), -100.0, "0", [], []),

	("enterprise_mill", sf_indoors, "mill_interior", "bo_mill_interior", (-40.00, -40.00), (40.00, 40.00), -100.0, "0", [], []),

	("enterprise_smithy", sf_indoors, "smithy_interior", "bo_smithy_interior", (-40.00, -40.00), (40.00, 40.00), -100.0, "0", [], []),

	("enterprise_dyeworks", sf_indoors, "weavery_interior", "bo_weavery_interior", (-40.00, -40.00), (40.00, 40.00), -100.0, "0", [], []),

	("enterprise_linen_weavery", sf_indoors, "weavery_interior", "bo_weavery_interior", (-40.00, -40.00), (40.00, 40.00), -100.0, "0", [], []),

	("enterprise_wool_weavery", sf_indoors, "weavery_interior", "bo_weavery_interior", (-40.00, -40.00), (40.00, 40.00), -100.0, "0", [], []),

	("enterprise_brewery", sf_indoors, "brewery_interior", "bo_brewery_interior", (-40.00, -40.00), (40.00, 40.00), -100.0, "0", [], []),

	("enterprise_oil_press", sf_indoors, "oil_press_interior", "bo_oil_press_interior", (-40.00, -40.00), (40.00, 40.00), -100.0, "0", [], []),

	("entrenched_steppe", sf_generate, "none", "none", (0.00, 0.00), (450.00, 450.00), -0.5, "0x0000000421220f00400d2348000064170000197b00002ad3", [], [], "outer_terrain_steppe"),

	("entrenched_plain", sf_generate, "none", "none", (0.00, 0.00), (450.00, 450.00), -0.5, "0x000000043464c8d1400d23480000065100007b430000254d", [], [], "outer_terrain_plain"),

	("entrenched_snow", sf_generate, "none", "none", (0.00, 0.00), (450.00, 450.00), -0.5, "0x0000000042448e00000d2348000063bb000076e200002307", [], [], "outer_terrain_snow"),

	("entrenched_desert", sf_generate, "none", "none", (0.00, 0.00), (450.00, 450.00), -0.5, "0x000000045002ca80000a9eae0000310200002bc000001ed5", [], [], "outer_terrain_desert_b"),

	("entrenched_steppe_forest", sf_generate, "none", "none", (0.00, 0.00), (450.00, 450.00), -0.5, "0x00000000a7218a95000d234800003de1000034650000243b", [], [], "outer_terrain_plain"),

	("entrenched_plain_forest", sf_generate, "none", "none", (0.00, 0.00), (200.00, 200.00), -0.5, "0x00000000b8e79732000d234800004b1500004628000064e5", [], [], "outer_terrain_plain"),

	("entrenched_snow_forest", sf_generate, "none", "none", (0.00, 0.00), (450.00, 450.00), -0.5, "0x00000000ca0511b1000d234800003f82000065a500007fc9", [], [], "outer_terrain_snow"),

	("entrenched_desert_forest", sf_generate, "none", "none", (0.00, 0.00), (450.00, 450.00), -0.5, "0x00000004da02cb320009c2730000614c000069a4000033f6", [], [], "outer_terrain_desert"),

	("not_entrenched_steppe", sf_generate, "none", "none", (0.00, 0.00), (450.00, 450.00), -0.5, "0x0000000020000500000769d2000061f700006d3100002d4c", [], [], "outer_terrain_steppe"),

	("not_entrenched_plain", sf_generate, "none", "none", (0.00, 0.00), (450.00, 450.00), -0.5, "0x000000043464c8d1400d23480000065100007b430000254d", [], [], "outer_terrain_plain"),

	("not_entrenched_snow", sf_generate, "none", "none", (0.00, 0.00), (450.00, 450.00), -0.5, "0x0000000042448e00000d2348000063bb000076e200002307", [], [], "outer_terrain_snow"),

	("not_entrenched_desert", sf_generate, "none", "none", (0.00, 0.00), (450.00, 450.00), -0.5, "0x000000045002ca80000a9eae0000310200002bc000001ed5", [], [], "outer_terrain_desert_b"),

	("not_entrenched_steppe_forest", sf_generate, "none", "none", (0.00, 0.00), (450.00, 450.00), -0.5, "0x00000000a7218a95000d234800003de1000034650000243b", [], [], "outer_terrain_plain"),

	("not_entrenched_plain_forest", sf_generate, "none", "none", (0.00, 0.00), (200.00, 200.00), -0.5, "0x00000000b8e79732000d234800004b1500004628000064e5", [], [], "outer_terrain_plain"),

	("not_entrenched_snow_forest", sf_generate, "none", "none", (0.00, 0.00), (450.00, 450.00), -0.5, "0x00000000ca0511b1000d234800003f82000065a500007fc9", [], [], "outer_terrain_snow"),

	("not_entrenched_desert_forest", sf_generate, "none", "none", (0.00, 0.00), (450.00, 450.00), -0.5, "0x000000045002ca80000a9eae0000310200002bc000001ed5", [], [], "outer_terrain_desert"),

	("cozur_custom_ford_1", sf_generate, "none", "none", (0.00, 0.00), (100.00, 100.00), -100.0, "0x00000000200005000005f17a0000023f0000043d00001956", [], [], "outer_terrain_ford"),

	("cozur_custom_plains_1", sf_generate|sf_auto_entry_points, "none", "none", (0.00, 0.00), (100.00, 100.00), -100.0, "0x00000000300005000006fdc2000011df00001c1600002028", [], [], "outer_terrain_plain_rnd"),

	("cozur_custom_plains_2", sf_generate|sf_auto_entry_points, "none", "none", (0.00, 0.00), (100.00, 100.00), -100.0, "0x00000000300005000006fdc2000029b600001c1600002028", [], [], "outer_terrain_plain_rnd"),

	("cozur_custom_plains_3", sf_generate|sf_auto_entry_points, "none", "none", (0.00, 0.00), (100.00, 100.00), -100.0, "0x00000000300005000006fdc20000562f000019fd00000f4b", [], [], "outer_terrain_plain_rnd"),

	("cozur_custom_plains_4", sf_generate|sf_auto_entry_points, "none", "none", (0.00, 0.00), (100.00, 100.00), -100.0, "0x0000000030000500000709c800002afd000032ac000056dc", [], [], "outer_terrain_plain_rnd"),

	("cozur_custom_plains_5", sf_generate|sf_auto_entry_points, "none", "none", (0.00, 0.00), (100.00, 100.00), -100.0, "0x0000000030000500000709c800003df1000032ac000056dc", [], [], "outer_terrain_plain_rnd"),

	("cozur_custom_plains_6", sf_generate|sf_auto_entry_points, "none", "none", (0.00, 0.00), (100.00, 100.00), -100.0, "0x0000000030000500000709c800003df1000032ac000056dc", [], [], "outer_terrain_plain_rnd"),

	("cozur_custom_plains_7", sf_generate|sf_auto_entry_points, "none", "none", (0.00, 0.00), (100.00, 100.00), -100.0, "0x0000000032600963000709c800004b4b00007522000027af", [], [], "outer_terrain_plain_rnd"),

	("cozur_custom_plains_8", sf_generate|sf_auto_entry_points, "none", "none", (0.00, 0.00), (100.00, 100.00), -100.0, "0x0000000032600963000709c800007ac8000040b200006c4e", [], [], "outer_terrain_plain_rnd"),

	("cozur_custom_plains_9", sf_generate|sf_auto_entry_points, "none", "none", (0.00, 0.00), (100.00, 100.00), -100.0, "0x00000000326009630007adea00003b36000051650000114d", [], [], "outer_terrain_plain_rnd"),

	("cozur_custom_plains_10", sf_generate|sf_auto_entry_points, "none", "none", (0.00, 0.00), (100.00, 100.00), -100.0, "0x00000000326009630007adea00000df70000316000000e16", [], [], "outer_terrain_plain_rnd"),

	("cozur_custom_default_steppe_1", sf_generate|sf_auto_entry_points, "none", "none", (0.00, 0.00), (100.00, 100.00), -100.0, "0x0000000020000a63000806030000537900001eba00001f25", [], [], "outer_terrain_steppe_rnd"),

	("cozur_custom_default_steppe_2", sf_generate|sf_auto_entry_points, "none", "none", (0.00, 0.00), (100.00, 100.00), -100.0, "0x0000000020000a630008060300006429000028d200007752", [], [], "outer_terrain_steppe_rnd"),

	("cozur_custom_default_steppe_3", sf_generate|sf_auto_entry_points, "none", "none", (0.00, 0.00), (100.00, 100.00), -100.0, "0x0000000020000a630008060300003ba700003cc800000577", [], [], "outer_terrain_steppe_rnd"),

	("cozur_custom_default_steppe_4", sf_generate|sf_auto_entry_points, "none", "none", (0.00, 0.00), (100.00, 100.00), -100.0, "0x0000000020000a63000806030000537900001eba00001f25", [], [], "outer_terrain_steppe_rnd"),

	("cozur_custom_default_steppe_5", sf_generate|sf_auto_entry_points, "none", "none", (0.00, 0.00), (100.00, 100.00), -100.0, "0x0000000020000a630008060300006429000028d200007752", [], [], "outer_terrain_steppe_rnd"),

	("cozur_custom_default_steppe_6", sf_generate|sf_auto_entry_points, "none", "none", (0.00, 0.00), (100.00, 100.00), -100.0, "0x0000000020000a630008060300003ba700003cc800000577", [], [], "outer_terrain_steppe_rnd"),

	("cozur_custom_default_steppe_7", sf_generate|sf_auto_entry_points, "none", "none", (0.00, 0.00), (100.00, 100.00), -100.0, "0x00000000a3c005630007adf300006f2000005c0e00007cba", [], [], "outer_terrain_steppe_rnd"),

	("cozur_custom_default_steppe_8", sf_generate|sf_auto_entry_points, "none", "none", (0.00, 0.00), (100.00, 100.00), -100.0, "0x00000000a3c005630007adf30000069a00001fe300002a70", [], [], "outer_terrain_steppe_rnd"),

	("cozur_custom_default_steppe_9", sf_generate|sf_auto_entry_points, "none", "none", (0.00, 0.00), (100.00, 100.00), -100.0, "0x0000000025c011e30007adf30000262d000063d700006038", [], [], "outer_terrain_steppe_rnd"),

	("cozur_custom_default_steppe_10", sf_generate|sf_auto_entry_points, "none", "none", (0.00, 0.00), (100.00, 100.00), -100.0, "0x0000000025c011e30007adf300001a34000007dc00006236", [], [], "outer_terrain_steppe_rnd"),

	("cozur_custom_default_steppe_forest_1", sf_generate|sf_auto_entry_points, "none", "none", (0.00, 0.00), (100.00, 100.00), -100.0, "0x00000000ac6010630007adf3000077ab00003c0300002fe7", [], [], "outer_terrain_steppe_rnd"),

	("cozur_custom_default_steppe_forest_2", sf_generate|sf_auto_entry_points, "none", "none", (0.00, 0.00), (100.00, 100.00), -100.0, "0x00000000ac6010630007adf300001ffd00003b2600007f0b", [], [], "outer_terrain_steppe_rnd"),

	("cozur_custom_default_steppe_forest_3", sf_generate|sf_auto_entry_points, "none", "none", (0.00, 0.00), (100.00, 100.00), -100.0, "0x00000000ac6010630007adf300002c7f00002356000030a4", [], [], "outer_terrain_steppe_rnd"),

	("cozur_custom_default_steppe_forest_4", sf_generate|sf_auto_entry_points, "none", "none", (0.00, 0.00), (100.00, 100.00), -100.0, "0x00000000ac6005630007adf300006472000056cb00002028", [], [], "outer_terrain_steppe_rnd"),

	("cozur_custom_default_steppe_forest_5", sf_generate|sf_auto_entry_points, "none", "none", (0.00, 0.00), (100.00, 100.00), -100.0, "0x00000000ac6005630007adf3000016190000357100007231", [], [], "outer_terrain_steppe_rnd"),

	("cozur_custom_default_plain_forest_1", sf_generate|sf_auto_entry_points, "none", "none", (0.00, 0.00), (100.00, 100.00), -100.0, "0x00000000bc6005630007adf30000016700002a8100007034", [], [], "outer_terrain_plain_rnd"),

	("cozur_custom_default_plain_forest_2", sf_generate|sf_auto_entry_points, "none", "none", (0.00, 0.00), (100.00, 100.00), -100.0, "0x00000000bc6005630007adf30000508400002fed00006b28", [], [], "outer_terrain_plain_rnd"),

	("cozur_custom_default_plain_forest_3", sf_generate|sf_auto_entry_points, "none", "none", (0.00, 0.00), (100.00, 100.00), -100.0, "0x00000000bc6011e30007adf30000492a0000124c00000a47", [], [], "outer_terrain_plain_rnd"),

	("cozur_custom_default_plain_forest_4", sf_generate|sf_auto_entry_points, "none", "none", (0.00, 0.00), (100.00, 100.00), -100.0, "0x00000000bc6045000006719900004fe200007d88000045a1", [], [], "outer_terrain_plain_rnd"),

	("cozur_custom_default_plain_forest_5", sf_generate|sf_auto_entry_points, "none", "none", (0.00, 0.00), (100.00, 100.00), -100.0, "0x00000000bc790a63000601880000288e000011ac000065a2", [], [], "outer_terrain_plain_rnd"),

	("cozur_custom_deserts_1", sf_generate|sf_auto_entry_points, "none", "none", (0.00, 0.00), (100.00, 100.00), -100.0, "0x000000005c6009e30007adf30000264f00007e5f00007107", [], [], "outer_terrain_desert_rnd"),

	("cozur_custom_deserts_2", sf_generate|sf_auto_entry_points, "none", "none", (0.00, 0.00), (100.00, 100.00), -100.0, "0x000000005c6009e30007adf300003088000077300000345c", [], [], "outer_terrain_desert_rnd"),

	("cozur_custom_deserts_3", sf_generate|sf_auto_entry_points, "none", "none", (0.00, 0.00), (100.00, 100.00), -100.0, "0x000000005c6009e30007adf30000510f0000431e00003368", [], [], "outer_terrain_desert_rnd"),

	("cozur_custom_deserts_4", sf_generate|sf_auto_entry_points, "none", "none", (0.00, 0.00), (100.00, 100.00), -100.0, "0x000000005c6009e30007adf300002c56000078f900004e65", [], [], "outer_terrain_desert_rnd"),

	("cozur_custom_deserts_5", sf_generate|sf_auto_entry_points, "none", "none", (0.00, 0.00), (100.00, 100.00), -100.0, "0x000000005c6009e30007adf300004afb00002e110000679d", [], [], "outer_terrain_desert_rnd"),

	("cozur_custom_deserts_6", sf_generate|sf_auto_entry_points, "none", "none", (0.00, 0.00), (100.00, 100.00), -100.0, "0x000000005c6009e30007adf30000188200004689000011ba", [], [], "outer_terrain_desert_rnd"),

	("cozur_custom_deserts_7", sf_generate|sf_auto_entry_points, "none", "none", (0.00, 0.00), (100.00, 100.00), -100.0, "0x000000005c6009e30007adf300002a0d00000aa6000067e2", [], [], "outer_terrain_desert_rnd"),

	("cozur_custom_deserts_8", sf_generate|sf_auto_entry_points, "none", "none", (0.00, 0.00), (100.00, 100.00), -100.0, "0x000000005c6009e30007adf3000018970000476800006eae", [], [], "outer_terrain_desert_rnd"),

	("cozur_custom_deserts_9", sf_generate|sf_auto_entry_points, "none", "none", (0.00, 0.00), (100.00, 100.00), -100.0, "0x000000005c6010630007adf300004ed70000228900001d43", [], [], "outer_terrain_desert_rnd"),

	("cozur_custom_deserts_10", sf_generate|sf_auto_entry_points, "none", "none", (0.00, 0.00), (100.00, 100.00), -100.0, "0x000000005c6010630007adf300002d7800003c0300002fe7", [], [], "outer_terrain_desert_rnd"),

	("cozur_custom_swamps_1", sf_generate, "none", "none", (0.00, 0.00), (100.00, 100.00), -100.0, "0x00000000200005000004a928000056f100006c9700002e11", [], [], "outer_terrain_steppe"),

	("cozur_custom_swamps_2", sf_generate, "none", "none", (0.00, 0.00), (100.00, 100.00), -100.0, "0x00000000200005000004a9280000463000006c9700002e11", [], [], "outer_terrain_steppe"),

	("cozur_custom_swamps_3", sf_generate, "none", "none", (0.00, 0.00), (100.00, 100.00), -100.0, "0x00000000200005000004a9280000639b00006c9700002e11", [], [], "outer_terrain_steppe"),

	("cozur_custom_swamps_4", sf_generate, "none", "none", (0.00, 0.00), (100.00, 100.00), -100.0, "0x00000000200016000004a928000017c600006c9700002e11", [], [], "outer_terrain_steppe_mountain"),

	("cozur_custom_swamps_5", sf_generate, "none", "none", (0.00, 0.00), (100.00, 100.00), -100.0, "0x00000000200487000004a92800004f8800006c9700002e11", [], [], "outer_terrain_steppe_mountain"),

	("cozur_custom_neck_1", sf_generate|sf_auto_entry_points, "none", "none", (0.00, 0.00), (100.00, 100.00), -100.0, "0x00000000b00005000004a92800004f8800006c9700002e11", [], [], "outer_terrain_plain_rnd"),

	("cozur_custom_neck_2", sf_generate|sf_auto_entry_points, "none", "none", (0.00, 0.00), (100.00, 100.00), -100.0, "0x00000000b00005000004a9280000680000006c9700002e11", [], [], "outer_terrain_plain_rnd"),

	("cozur_custom_neck_3", sf_generate|sf_auto_entry_points, "none", "none", (0.00, 0.00), (100.00, 100.00), -100.0, "0x00000000b00005000004a92800003aea00006c97000006be", [], [], "outer_terrain_plain_rnd"),

	("cozur_custom_neck_4", sf_generate|sf_auto_entry_points, "none", "none", (0.00, 0.00), (100.00, 100.00), -100.0, "0x00000000b00005000004a9280000468b00006c9700004c02", [], [], "outer_terrain_plain_rnd"),

	("special_room_painted_table", sf_generate, "none", "none", (0.00, 0.00), (100.00, 100.00), -100.0, "0x00000000300005000008f63b00001d5700005904000031b7", [], [], "sea_outer_terrain_2"),

	("special_room_iron_throne_room", sf_generate, "none", "none", (0.00, 0.00), (100.00, 100.00), -100.0, "0x00000002200005000005f57b00005885000046bd00006d9c", [], [], "sea_outer_terrain_2"),

	("special_room_citadel", sf_indoors, "castle_h_interior_b", "bo_castle_h_interior_b", (-100.00, -100.00), (100.00, 100.00), -100.0, "0", [], []),

	("special_room_archives", sf_indoors, "interior_castle_d", "bo_interior_castle_d", (-100.00, -100.00), (100.00, 100.00), -100.0, "0", [], []),

	("special_room_coppersmiths_wynd", sf_indoors, "interior_house_extension_h", "bo_interior_house_extension_h", (-100.00, -100.00), (100.00, 100.00), -100.0, "0", [], []),

	("black_cells_1", sf_indoors, "dungeon_cell_a", "bo_dungeon_cell_a", (-100.00, -100.00), (100.00, 100.00), -100.0, "0", [], []),

	("black_cells_2", sf_indoors, "dungeon_cell_a", "bo_dungeon_cell_a", (-100.00, -100.00), (100.00, 100.00), -100.0, "0", [], []),

	("thirsty_goat", sf_indoors, "weavery_interior", "bo_weavery_interior", (-100.00, -100.00), (100.00, 100.00), -100.0, "0", [], []),

	("renly_quest_shore", sf_generate, "none", "none", (0.00, 0.00), (100.00, 100.00), -100.0, "0x00000000300005000008f63b00001d5700005904000031b7", [], [], "sea_outer_terrain_2"),

	("ninestars_1", sf_generate, "none", "none", (0.00, 0.00), (100.00, 100.00), -100.0, "0x00000000200005000006258d00001b8400005ff1000072c0", [], [], "outer_terrain_steppe_farmountain"),

	("ninestars_prison", sf_indoors, "interior_prison_e", "bo_interior_prison_e", (-100.00, -100.00), (100.00, 100.00), -100.0, "0", [], []),

	("ninestars_chambers", sf_indoors, "interior_castle_a", "bo_interior_castle_a", (-100.00, -100.00), (100.00, 100.00), -100.0, "0", ["exit"], ["castle_11_seneschal"]),

	("ninestars_trial", sf_generate, "none", "none", (0.00, 0.00), (100.00, 100.00), -100.0, "0x00000000200005000006258d00001b8400005ff1000072c0", [], [], "outer_terrain_steppe_farmountain"),

	("ninestars_trial_woods", sf_generate, "none", "none", (0.00, 0.00), (100.00, 100.00), -100.0, "0x00000000bc604500000458c6000017d20000151500003ecf", [], [], "outer_terrain_plain_farmountain"),

	("riverlands_village", sf_generate, "none", "none", (0.00, 0.00), (100.00, 100.00), -100.0, "0x0000000030000f630005796000003b2200004fa800002ab1", [], [], "outer_terrain_plain"),

	("northern_village", sf_generate, "none", "none", (0.00, 0.00), (100.00, 100.00), -100.0, "0x0000000020000a63000806030000537900001eba00001f25", [], [], "outer_terrain_steppe"),

	("westerlands_village", sf_generate, "none", "none", (0.00, 0.00), (100.00, 100.00), -100.0, "0x0000000020000a63000806030000537900001eba00001f25", [], [], "outer_terrain_steppe"),

	("battlemap_barrow", sf_generate, "none", "none", (0.00, 0.00), (100.00, 100.00), -100.0, "0x0000000020190b86000615880000608800001856000010b0", [], [], "outer_terrain_steppe"),

	("battlemap_weirwood", sf_generate, "none", "none", (0.00, 0.00), (100.00, 100.00), -100.0, "0x00000000ac6005010005b96f0000080b0000474d000060a6", [], [], "outer_terrain_steppe_farmountain"),

	("battlemap_mine", sf_generate, "none", "none", (0.00, 0.00), (100.00, 100.00), -100.0, "0x000000002000050000056d5b00005f580000134e00006779", [], [], "outer_terrain_steppe"),

	("battlemap_lumber_camp", sf_generate, "none", "none", (0.00, 0.00), (100.00, 100.00), -100.0, "0x00000000aa19116300059d6400000477000009ff000028e0", [], [], "outer_terrain_steppe"),

	("battlemap_farmland", sf_generate, "none", "none", (0.00, 0.00), (100.00, 100.00), -100.0, "0x00000000300005000005e17800000477000009ff000028e0", [], [], "outer_terrain_plain"),

	("battlemap_rhoynar_ruins", sf_generate, "none", "none", (0.00, 0.00), (100.00, 100.00), -100.0, "0x00000000300005000003c0ee00000de600007cf800005d42", [], [], "outer_terrain_plain"),

	("battlemap_ruined_fort", sf_generate, "none", "none", (0.00, 0.00), (100.00, 100.00), -100.0, "0x000000003c6005000005c5700000076b000010f8000059aa", [], [], "outer_terrain_plain"),

	("battlemap_orchard", sf_generate, "none", "none", (0.00, 0.00), (100.00, 100.00), -100.0, "0x0000000130010e0e0005fd84000011c60000285b00005cbe", [], [], "outer_terrain_plain"),

	("battlemap_poleboat", sf_generate, "none", "none", (0.00, 0.00), (100.00, 100.00), -100.0, "0x00000000d00005000005ad68000046ef00003947000073f7", [], [], "outer_terrain_desert"),

	("battlemap_old_mill", sf_generate, "none", "none", (0.00, 0.00), (100.00, 100.00), -100.0, "0x00000000300417e300062d8b0000580100000cb900001fcb", [], [], "outer_terrain_plain"),

	("battlemap_forest_bog", sf_generate, "none", "none", (0.00, 0.00), (100.00, 100.00), -100.0, "0x00000000b0000500000555550000407b000034b800000c75", [], [], "outer_terrain_plain"),

	("battlemap_abandoned_village", sf_generate, "none", "none", (0.00, 0.00), (100.00, 100.00), -100.0, "0x000000002000050000059968000051200000788100001b70", [], [], "outer_terrain_steppe"),

	("battlemap_dothraki_sea_1", sf_generate, "none", "none", (0.00, 0.00), (100.00, 100.00), -100.0, "0x00000000200005630002e51d000008fc0000133100007a7f", [], [], "outer_terrain_steppe_dothraki"),

	("battlemap_dothraki_sea_2", sf_generate, "none", "none", (0.00, 0.00), (100.00, 100.00), -100.0, "0x00000000200005630002e51d000008fc0000133100007a7f", [], [], "outer_terrain_steppe_dothraki"),

	("water_gardens", sf_generate, "none", "none", (0.00, 0.00), (100.00, 100.00), -100.0, "0x00000000500005820003b4ee00007329000048ab00006cd9", [], [], "outer_terrain_desert_rocky"),

	("odin_cave", sf_generate, "none", "none", (0.00, 0.00), (100.00, 100.00), -100.0, "0x00000000300005000003fcfc000021160000222400005607", [], [], "outer_terrain_plain_farmountain"),

	("cairn_hall", sf_generate, "none", "none", (0.00, 0.00), (100.00, 100.00), -100.0, "0x0000000020000500000318c700000b6900001d0600002404", [], [], "outer_terrain_steppe_farmountain"),

	("mole_town", sf_generate, "none", "none", (0.00, 0.00), (100.00, 100.00), -100.0, "0x000000002c60050000054952000041ae000045ca00005e2b", [], [], "outer_terrain_steppe_farmountain"),

	("bridge_of_skulls", sf_generate, "none", "none", (0.00, 0.00), (100.00, 100.00), -100.0, "0x0000000040192ee300058962000078f500000d64000012e4", [], [], "outer_terrain_snow_mountain"),

	("wall_tunnel", sf_indoors, "tunnel_crossing_supports", "bo_tunnel_crossing_supports", (-100.00, -100.00), (100.00, 100.00), -100.0, "0", ["exit"], []),

	("haldon_bath", sf_generate, "none", "none", (0.00, 0.00), (100.00, 100.00), -100.0, "0x00000000300005000003fcfc000021160000222400005607", [], [], "outer_terrain_plain"),

	("golden_company_camp", sf_generate, "none", "none", (0.00, 0.00), (100.00, 100.00), -100.0, "0x0000000020000500000318c700000b6900001d0600002404", [], [], "outer_terrain_steppe"),

	("horror_cave", sf_generate, "none", "none", (0.00, 0.00), (100.00, 100.00), -100.0, "0x00000000300005000003fcfc000021160000222400005607", [], [], "outer_terrain_plain"),

	("brookwater_keep", sf_generate, "none", "none", (0.00, 0.00), (100.00, 100.00), -100.0, "0x00000000300005000003fcfc000021160000222400005607", [], [], "outer_terrain_plain"),

	("shadow_tower", sf_generate, "none", "none", (0.00, 0.00), (100.00, 100.00), -100.0, "0x00000000400005000005314c000032c100002621000012bd", [], [], "outer_terrain_snow_mountain"),

	("shadow_tower2", sf_generate, "none", "none", (0.00, 0.00), (100.00, 100.00), -100.0, "0x00000000400005000005314c000032c100002621000012bd", [], [], "outer_terrain_snow_mountain"),

	("castle_black", sf_generate, "none", "none", (0.00, 0.00), (100.00, 100.00), -100.0, "0x00000000400005000005314c000032c100002621000012bd", [], [], "outer_terrain_snow"),

	("castle_black2", sf_generate, "none", "none", (0.00, 0.00), (100.00, 100.00), -100.0, "0x00000000400005000005314c000032c100002621000012bd", [], [], "outer_terrain_snow"),

	("castle_black3", sf_generate, "none", "none", (0.00, 0.00), (100.00, 100.00), -100.0, "0x00000000400005000005314c000032c100002621000012bd", [], [], "outer_terrain_snow"),

	("castle_black4", sf_generate, "none", "none", (0.00, 0.00), (100.00, 100.00), -100.0, "0x00000000400005000005314c000032c100002621000012bd", [], [], "outer_terrain_snow"),

	("castle_black5", sf_generate, "none", "none", (0.00, 0.00), (100.00, 100.00), -100.0, "0x00000000400005000005314c000032c100002621000012bd", [], [], "outer_terrain_snow"),

	("eastwatch", sf_generate, "none", "none", (0.00, 0.00), (100.00, 100.00), -100.0, "0x00000000400005000005314c000032c100002621000012bd", [], [], "sea_outer_terrain_2"),

	("illyrios_manse", sf_generate, "none", "none", (0.00, 0.00), (100.00, 100.00), -100.0, "0x0000000030000500000368da00002dae0000153e000017ca", [], [], "sea_outer_terrain_2"),

	("bloodstone_battlefield", sf_generate, "none", "none", (0.00, 0.00), (100.00, 100.00), -100.0, "0x00000000500005000004250f000051a700001f60000038e3", [], [], "outer_terrain_desert_rocky"),

	("bloodstone", sf_generate, "none", "none", (0.00, 0.00), (100.00, 100.00), -100.0, "0x00000000500005000004250f000051a700001f60000038e3", [], [], "sea_outer_terrain_2"),

	("bloodstone_haunt", sf_generate, "none", "none", (0.00, 0.00), (100.00, 100.00), -100.0, "0x000000033000124c000acab40000280700000c9f00000ab5", [], [], "sea_outer_terrain_2"),

	("daznaks_pit", sf_generate, "none", "none", (0.00, 0.00), (100.00, 100.00), -100.0, "0x00000000500005000004250f000051a700001f60000038e3", [], [], "outer_terrain_desert_rocky"),

	("way_to_meereen", sf_generate, "none", "none", (0.00, 0.00), (100.00, 100.00), -100.0, "0x00000000500005000004250f000051a700001f60000038e3", [], [], "outer_terrain_desert_rocky"),

	("meereen_throne_room", sf_generate, "none", "none", (0.00, 0.00), (100.00, 100.00), -100.0, "0x00000000500005000003c0ee00001317000035ad000077c0", [], [], "outer_terrain_steppe_farmountain"),

	("yunkai_ship_1", sf_generate, "none", "none", (0.00, 0.00), (100.00, 100.00), -100.0, "0x0000000030000500000258960000573a00005d4500004a60", [], [], "sea_outer_terrain_2"),

	("yunkai_ship_2", sf_generate, "none", "none", (0.00, 0.00), (100.00, 100.00), -100.0, "0x0000000030000500000258960000573a00005d4500004a60", [], [], "sea_outer_terrain_2"),

	("yunkai_ship_3", sf_generate, "none", "none", (0.00, 0.00), (100.00, 100.00), -100.0, "0x0000000030000500000258960000573a00005d4500004a60", [], [], "sea_outer_terrain_2"),

	("yunkai_ship_4", sf_generate, "none", "none", (0.00, 0.00), (100.00, 100.00), -100.0, "0x0000000030000500000258960000573a00005d4500004a60", [], [], "sea_outer_terrain_2"),

	("nightfort", sf_indoors, "essos_dungeon_1", "bo_essos_dungeon_1", (-100.00, -100.00), (100.00, 100.00), -100.0, "0", ["exit"], []),

	("nightfort_rat_cook", sf_indoors, "essos_dungeon_1", "bo_essos_dungeon_1", (-100.00, -100.00), (100.00, 100.00), -100.0, "0", ["exit"], []),

	("nightfort_mad_axe", sf_indoors, "essos_dungeon_1", "bo_essos_dungeon_1", (-100.00, -100.00), (100.00, 100.00), -100.0, "0", ["exit"], []),

	("nightfort_nights_king", sf_indoors, "essos_dungeon_1", "bo_essos_dungeon_1", (-100.00, -100.00), (100.00, 100.00), -100.0, "0", ["exit"], []),

	("yunkai", sf_generate, "none", "none", (0.00, 0.00), (100.00, 100.00), -100.0, "0x00000000500005000003c0ee00001317000035ad000077c0", [], [], "outer_terrain_desert_rocky"),

	("meereen", sf_generate, "none", "none", (0.00, 0.00), (100.00, 100.00), -100.0, "0x00000000500005000003c0ee00001317000035ad000077c0", [], [], "outer_terrain_desert_rocky"),

	("harrentown", sf_generate, "none", "none", (0.00, 0.00), (100.00, 100.00), -100.0, "0x0000000230084fac00057d5f00002ba900004a7a000060be", [], [], "outer_terrain_plain"),

	("tower_of_joy", sf_generate, "none", "none", (0.00, 0.00), (100.00, 100.00), -100.0, "0x000000005000050000078de30000011b0000579a000046fc", [], [], "outer_terrain_desert_rocky"),

	("bear_island", sf_generate, "none", "none", (0.00, 0.00), (100.00, 100.00), -100.0, "0x00000000200005000009aa6c0000414900003d270000397b", [], [], "sea_outer_terrain_2"),

	("naggas_hill", sf_generate, "none", "none", (0.00, 0.00), (100.00, 100.00), -100.0, "0x00000000200005000009aa6c0000414900003d270000397b", [], [], "sea_outer_terrain_2"),

	("hillhall", sf_generate, "none", "none", (0.00, 0.00), (100.00, 100.00), -100.0, "0x000000002c691de30006b1a800002b840000064f000021aa", [], [], "outer_terrain_steppe"),

	("abandoned_holdfast", sf_generate, "none", "none", (0.00, 0.00), (100.00, 100.00), -100.0, "0x0000000230084fac00057d5f00002ba900004a7a000060be", [], [], "outer_terrain_plain_farmountain"),

	("rodgars_hut", sf_generate, "none", "none", (0.00, 0.00), (100.00, 100.00), -100.0, "0x0000000230084fac00057d5f00002ba900004a7a000060be", [], [], "outer_terrain_plain_farmountain"),

	("donation_septry", sf_generate, "none", "none", (0.00, 0.00), (100.00, 100.00), -100.0, "0x00000000301905630005454d000075d300007d74000019d4", [], [], "outer_terrain_plain_farmountain"),

	("relic_septry", sf_generate, "none", "none", (0.00, 0.00), (100.00, 100.00), -100.0, "0x0000000230084fac00057d5f00002ba900004a7a000060be", [], [], "outer_terrain_plain_farmountain"),

	("citadel_septry", sf_generate, "none", "none", (0.00, 0.00), (100.00, 100.00), -100.0, "0x00000000200f9a9f0004e5360000761e0000357800006f35", [], [], "outer_terrain_plain_farmountain"),

	("citadel_holdings", sf_indoors, "interior_castle_g", "bo_interior_castle_g", (-100.00, -100.00), (100.00, 100.00), -100.0, "0", [], []),

	("citadel_barrow", sf_generate, "none", "none", (0.00, 0.00), (100.00, 100.00), -100.0, "0x00000000200f9ae300055d550000213b00006f0800006fb4", [], [], "outer_terrain_plain_farmountain"),

	("isle_of_faces", sf_generate, "none", "none", (0.00, 0.00), (100.00, 100.00), -100.0, "0x0000000230084fac00057d5f00002ba900004a7a000060be", [], [], "sea_outer_terrain_2"),

	("saltpans_isles", sf_generate, "none", "none", (0.00, 0.00), (100.00, 100.00), -100.0, "0x0000000230084fac00057d5f00002ba900004a7a000060be", [], [], "sea_outer_terrain_2"),

	("summerhall", sf_generate, "none", "none", (0.00, 0.00), (100.00, 100.00), -100.0, "0x0000000230084fac00057d5f00002ba900004a7a000060be", [], [], "outer_terrain_plain_farmountain"),

	("nunns_deep", sf_generate, "none", "none", (0.00, 0.00), (100.00, 100.00), -100.0, "0x0000000230084fac00057d5f00002ba900004a7a000060be", [], [], "outer_terrain_plain_farmountain"),

	("oldstones", sf_generate, "none", "none", (0.00, 0.00), (100.00, 100.00), -100.0, "0x0000000230084fac00057d5f00002ba900004a7a000060be", [], [], "outer_terrain_plain"),

	("sorrows", sf_generate, "none", "none", (0.00, 0.00), (100.00, 100.00), -100.0, "0x0000000020000500000318c700000b6900001d0600002404", [], [], "outer_terrain_steppe"),

	("dragonmont", sf_generate, "none", "none", (0.00, 0.00), (100.00, 100.00), -100.0, "0x00000000200005000009aa6c0000414900003d270000397b", [], [], "outer_terrain_steppe_farmountain"),

	("dragonstone_village", sf_generate, "none", "none", (0.00, 0.00), (100.00, 100.00), -100.0, "0x00000000300005000008f63b00001d5700005904000031b7", [], [], "sea_outer_terrain_2"),

	("wildfire_wight_battle", sf_generate, "none", "none", (0.00, 0.00), (100.00, 100.00), -100.0, "0x00000000200005000009aa6c0000414900003d270000397b", [], [], "outer_terrain_steppe_farmountain"),

	("ford_1", sf_generate|sf_auto_entry_points, "none", "none", (0.00, 0.00), (100.00, 100.00), -100.0, "0x000000002c60050000054952000041ae000045ca00005e2b", [], [], "outer_terrain_steppe"),

	("ford_2", sf_generate|sf_auto_entry_points, "none", "none", (0.00, 0.00), (100.00, 100.00), -100.0, "0x000000002c60050000054952000073270000156100006763", [], [], "outer_terrain_steppe"),

	("camp_steppe", sf_generate, "none", "none", (0.00, 0.00), (450.00, 450.00), -0.5, "0x0000000020018807000d234800001c0d00006c30000076b9", [], [], "outer_terrain_steppe"),

	("camp_plain", sf_generate, "none", "none", (0.00, 0.00), (450.00, 450.00), -0.5, "0x0000000030018807000d234800001c0d00006c3000002e42", [], [], "outer_terrain_plain"),

	("camp_snow", sf_generate, "none", "none", (0.00, 0.00), (450.00, 450.00), -0.5, "0x0000000040010889000d234800005cc50000262a00003686", [], [], "outer_terrain_snow"),

	("camp_desert", sf_generate, "none", "none", (0.00, 0.00), (450.00, 450.00), -0.5, "0x000000005a030b16000d23480000037d00004bf2000073c3", [], [], "outer_terrain_desert_b"),

	("camp_steppe_forest", sf_generate, "none", "none", (0.00, 0.00), (450.00, 450.00), -0.5, "0x00000000a0060822000d234800001abc00007cbb00001a1c", [], [], "outer_terrain_plain"),

	("camp_plain_forest", sf_generate, "none", "none", (0.00, 0.00), (200.00, 200.00), -0.5, "0x00000000b0c78a83000d234800003aca0000432f0000226d", [], [], "outer_terrain_plain"),

	("camp_snow_forest", sf_generate, "none", "none", (0.00, 0.00), (450.00, 450.00), -0.5, "0x00000000c206cb10000d23480000355100002c360000370d", [], [], "outer_terrain_snow"),

	("camp_desert_forest", sf_generate, "none", "none", (0.00, 0.00), (450.00, 450.00), -0.5, "0x000000005a030b16000d23480000037d00004bf2000073c3", [], [], "outer_terrain_desert"),

	("sea_1", sf_generate, "none", "none", (0.00, 0.00), (240.00, 240.00), -0.5, "0x0000000030000000c00d2348000000008000000000000000", [], [], "sea_outer_terrain_2"),

	("sea_2", sf_generate, "none", "none", (0.00, 0.00), (240.00, 240.00), -0.5, "0x0000000030000000c00d2348000000008000000000000000", [], [], "sea_outer_terrain_2"),

	("sea_3", sf_generate, "none", "none", (0.00, 0.00), (240.00, 240.00), -0.5, "0x0000000030000000c00d2348000000008000000000000000", [], [], "sea_outer_terrain_2"),

]