from header_common import *
from header_parties import *
from ID_troops import *
from ID_factions import *
from ID_party_templates import *
from ID_map_icons import *

####################################################################################################################
#  Each party record contains the following fields:
#  1) Party id: used for referencing parties in other files.
#     The prefix p_ is automatically added before each party id.
#  2) Party name.
#  3) Party flags. See header_parties.py for a list of available flags
#  4) Menu. ID of the menu to use when this party is met. The value 0 uses the default party encounter system.
#  5) Party-template. ID of the party template this party belongs to. Use pt_none as the default value.
#  6) Faction.
#  7) Personality. See header_parties.py for an explanation of personality flags.
#  8) Ai-behavior
#  9) Ai-target party
# 10) Initial coordinates.
# 11) List of stacks. Each stack record is a triple that contains the following fields:
#   11.1) Troop-id. 
#   11.2) Number of troops in this stack. 
#   11.3) Member flags. Use pmf_is_prisoner to note that this member is a prisoner.
# 12) Party direction in degrees [optional]
####################################################################################################################

no_menu = 0

parties = [
	("main_party", "Main Party", icon_people_player|pf_limit_members, no_menu, pt_none, fac_player_faction, aggressiveness_0, ai_bhvr_hold, 0, (2.55759, 50.0091), [(trp_player, 1, 0)]),

	("temp_party", "{!}temp party", icon_people_player|pf_disabled, no_menu, pt_none, fac_commoners, aggressiveness_0, ai_bhvr_hold, 0, (0.0, 0.0), []),

	("camp_bandits", "{!}camp bandits", icon_people_player|pf_disabled, no_menu, pt_none, fac_outlaws, aggressiveness_0, ai_bhvr_hold, 0, (1.0, 1.0), [(trp_temp_troop, 3, 0)]),

	("temp_party_2", "{!}temp party 2", icon_people_player|pf_disabled, no_menu, pt_none, fac_commoners, aggressiveness_0, ai_bhvr_hold, 0, (0.0, 0.0), []),

	("temp_casualties", "{!}casualties", icon_people_player|pf_disabled, no_menu, pt_none, fac_neutral, aggressiveness_0, ai_bhvr_hold, 0, (1.0, 1.0), []),

	("temp_casualties_2", "{!}casualties", icon_people_player|pf_disabled, no_menu, pt_none, fac_neutral, aggressiveness_0, ai_bhvr_hold, 0, (1.0, 1.0), []),

	("temp_casualties_3", "{!}casualties", icon_people_player|pf_disabled, no_menu, pt_none, fac_neutral, aggressiveness_0, ai_bhvr_hold, 0, (1.0, 1.0), []),

	("temp_wounded", "{!}enemies wounded", icon_people_player|pf_disabled, no_menu, pt_none, fac_neutral, aggressiveness_0, ai_bhvr_hold, 0, (1.0, 1.0), []),

	("temp_killed", "{!}enemies killed", icon_people_player|pf_disabled, no_menu, pt_none, fac_neutral, aggressiveness_0, ai_bhvr_hold, 0, (1.0, 1.0), []),

	("main_party_backup", "{!} ", icon_people_player|pf_disabled, no_menu, pt_none, fac_neutral, aggressiveness_0, ai_bhvr_hold, 0, (1.0, 1.0), []),

	("encountered_party_backup", "{!} ", icon_people_player|pf_disabled, no_menu, pt_none, fac_neutral, aggressiveness_0, ai_bhvr_hold, 0, (1.0, 1.0), []),

	("collective_friends_backup", "{!} ", icon_people_player|pf_disabled, no_menu, pt_none, fac_neutral, aggressiveness_0, ai_bhvr_hold, 0, (1.0, 1.0), []),

	("player_casualties", "{!} ", icon_people_player|pf_disabled, no_menu, pt_none, fac_neutral, aggressiveness_0, ai_bhvr_hold, 0, (1.0, 1.0), []),

	("enemy_casualties", "{!} ", icon_people_player|pf_disabled, no_menu, pt_none, fac_neutral, aggressiveness_0, ai_bhvr_hold, 0, (1.0, 1.0), []),

	("ally_casualties", "{!} ", icon_people_player|pf_disabled, no_menu, pt_none, fac_neutral, aggressiveness_0, ai_bhvr_hold, 0, (1.0, 1.0), []),

	("collective_enemy", "{!}collective enemy", icon_people_player|pf_disabled, no_menu, pt_none, fac_neutral, aggressiveness_0, ai_bhvr_hold, 0, (1.0, 1.0), []),

	("collective_ally", "{!}collective ally", icon_people_player|pf_disabled, no_menu, pt_none, fac_neutral, aggressiveness_0, ai_bhvr_hold, 0, (1.0, 1.0), []),

	("collective_friends", "{!}collective ally", icon_people_player|pf_disabled, no_menu, pt_none, fac_neutral, aggressiveness_0, ai_bhvr_hold, 0, (1.0, 1.0), []),

	("total_enemy_casualties", "{!} ", icon_people_player|pf_disabled, no_menu, pt_none, fac_neutral, aggressiveness_0, ai_bhvr_hold, 0, (1.0, 1.0), []),

	("routed_enemies", "{!}routed enemies", icon_people_player|pf_disabled, no_menu, pt_none, fac_neutral, aggressiveness_0, ai_bhvr_hold, 0, (1.0, 1.0), []),

	("freelancer_party_backup", "{!}", icon_people_player|pf_disabled, no_menu, pt_none, fac_neutral, aggressiveness_0, ai_bhvr_hold, 0, (1.0, 1.0), []),

	("zendar", "Zendar", icon_map_town_grey|pf_disabled|pf_village, no_menu, pt_none, fac_neutral, aggressiveness_0, ai_bhvr_hold, 0, (18.0, 60.0), []),

	("town_1", "Sisterton", icon_map_town_wood|pf_town, no_menu, pt_none, fac_neutral, aggressiveness_0, ai_bhvr_hold, 0, (61.4285, -128.645), [], 120.0),

	("town_3", "Saltpans", icon_map_town_wood|pf_town, no_menu, pt_none, fac_neutral, aggressiveness_0, ai_bhvr_hold, 0, (50.7736, -13.0955), [], 140.0),

	("town_6", "The Weeping Town", icon_map_town_wood|pf_town, no_menu, pt_none, fac_neutral, aggressiveness_0, ai_bhvr_hold, 0, (8.23869, 159.722), [], 225.0),

	("town_8", "Gulltown", icon_map_gulltown|pf_town, no_menu, pt_none, fac_neutral, aggressiveness_0, ai_bhvr_hold, 0, (-9.388022, -43.621235), [], 175.0),

	("town_9", "Fairmarket", icon_map_town_white|pf_town, no_menu, pt_none, fac_neutral, aggressiveness_0, ai_bhvr_hold, 0, (103.832001, -43.648701), [], 10.0),

	("town_12", "Pentos", icon_map_pentos|pf_town, no_menu, pt_none, fac_neutral, aggressiveness_0, ai_bhvr_hold, 0, (-82.9699, 60.1097), [], 270.0),

	("town_16", "King's Landing", icon_map_kings_landing|pf_town, no_menu, pt_none, fac_neutral, aggressiveness_0, ai_bhvr_hold, 0, (56.0854, 51.6812), [], 360.0),

	("town_17", "Braavos", icon_map_braavos|pf_town, no_menu, pt_none, fac_neutral, aggressiveness_0, ai_bhvr_hold, 0, (-81.9994, -96.1442), [], 180.0),

	("town_18", "Stoney Sept", icon_map_town_grey|pf_town, no_menu, pt_none, fac_neutral, aggressiveness_0, ai_bhvr_hold, 0, (111.857, 20.2177), [], 135.0),

	("town_19", "Sunspear", icon_map_sunspear|pf_town, no_menu, pt_none, fac_neutral, aggressiveness_0, ai_bhvr_hold, 0, (-12.3262, 213.842), [], 45.0),

	("town_20", "The Planky Town", icon_map_dorne_town|pf_town, no_menu, pt_none, fac_neutral, aggressiveness_0, ai_bhvr_hold, 0, (-1.87985, 215.935), [], 270.0),

	("town_23", "Dragonstone", icon_map_dragonstone|pf_town, no_menu, pt_none, fac_neutral, aggressiveness_0, ai_bhvr_hold, 0, (-4.15018, 10.5847), [], 225.0),

	("town_24", "Lannisport", icon_map_lannisport|pf_town, no_menu, pt_none, fac_neutral, aggressiveness_0, ai_bhvr_hold, 0, (200.415, 36.8791), [], 275.0),

	("town_25", "Duskendale", icon_map_town_grey|pf_town, no_menu, pt_none, fac_neutral, aggressiveness_0, ai_bhvr_hold, 0, (35.4199, 26.3671), [], 25.0),

	("town_26", "Maidenpool", icon_map_town_grey|pf_town, no_menu, pt_none, fac_neutral, aggressiveness_0, ai_bhvr_hold, 0, (36.0745, -0.514076), [], 225.0),

	("town_27", "Kayce", icon_map_town_wood|pf_town, no_menu, pt_none, fac_neutral, aggressiveness_0, ai_bhvr_hold, 0, (210.111, 27.7013), [], 225.0),

	("town_30", "Ashford", icon_map_town_white|pf_town, no_menu, pt_none, fac_neutral, aggressiveness_0, ai_bhvr_hold, 0, (94.8048, 132.559), [], 225.0),

	("town_31", "White Harbor", icon_map_white_harbor|pf_town, no_menu, pt_none, fac_neutral, aggressiveness_0, ai_bhvr_hold, 0, (75.410011, -154.519775), [], 125.0),

	("town_32", "Oldtown", icon_map_oldtown|pf_town, no_menu, pt_none, fac_neutral, aggressiveness_0, ai_bhvr_hold, 0, (190.666, 184.587), [], 300.0),

	("town_33", "Lord Harroway's Town", icon_map_town_grey|pf_town, no_menu, pt_none, fac_neutral, aggressiveness_0, ai_bhvr_hold, 0, (69.0104, -17.3567), [], 170.0),

	("town_34", "Lordsport", icon_map_town_grey|pf_town, no_menu, pt_none, fac_neutral, aggressiveness_0, ai_bhvr_hold, 0, (194.009, -40.4585), [], 225.0),

	("town_35", "Tumbleton", icon_map_town_grey|pf_town, no_menu, pt_none, fac_neutral, aggressiveness_0, ai_bhvr_hold, 0, (71.2296, 81.3346), [], 225.0),

	("town_36", "Rhyos", icon_map_essos_town|pf_town, no_menu, pt_none, fac_neutral, aggressiveness_0, ai_bhvr_hold, 0, (-93.86, 18.5796), [], 100.0),

	("town_38", "Lorath", icon_map_lorath|pf_town, no_menu, pt_none, fac_neutral, aggressiveness_0, ai_bhvr_hold, 0, (-167.387, -80.1462), [], 225.0),

	("town_40", "Lys", icon_map_lys|pf_town, no_menu, pt_none, fac_neutral, aggressiveness_0, ai_bhvr_hold, 0, (-84.6318, 242.72), [], 225.0),

	("town_41", "Barrowton", icon_map_town_wood|pf_town, no_menu, pt_none, fac_neutral, aggressiveness_0, ai_bhvr_hold, 0, (148.168808, -165.995377), [], 290.0),

	("town_42", "Goldengrove", icon_map_town_grey|pf_town, no_menu, pt_none, fac_neutral, aggressiveness_0, ai_bhvr_hold, 0, (132.195, 101.979), [], 210.0),

	("town_44", "Qohor", icon_map_essos_town|pf_town, no_menu, pt_none, fac_neutral, aggressiveness_0, ai_bhvr_hold, 0, (-218.691, 58.4213), [], 66.0),

	("town_45", "Myr", icon_map_myr|pf_town, no_menu, pt_none, fac_neutral, aggressiveness_0, ai_bhvr_hold, 0, (-111.75, 153.171), [], 225.0),

	("town_46", "Tyrosh", icon_map_tyrosh|pf_town, no_menu, pt_none, fac_neutral, aggressiveness_0, ai_bhvr_hold, 0, (-65.0088, 140.715), [], 225.0),

	("town_47", "Volantis", icon_map_volantis|pf_town, no_menu, pt_none, fac_neutral, aggressiveness_0, ai_bhvr_hold, 0, (-210.459, 227.004), [], 90.0),

	("town_48", "Volon Therys", icon_map_essos_town|pf_town, no_menu, pt_none, fac_neutral, aggressiveness_0, ai_bhvr_hold, 0, (-198.949, 201.027), [], 225.0),

	("town_49", "Valysar", icon_map_essos_town|pf_town, no_menu, pt_none, fac_neutral, aggressiveness_0, ai_bhvr_hold, 0, (-193.576, 187.107), [], 225.0),

	("town_50", "Selhorys", icon_map_essos_town|pf_town, no_menu, pt_none, fac_neutral, aggressiveness_0, ai_bhvr_hold, 0, (-196.656, 177.257), [], 225.0),

	("town_51", "Norvos", icon_map_norvos|pf_town, no_menu, pt_none, fac_neutral, aggressiveness_0, ai_bhvr_hold, 0, (-177.305, 2.86279), [], 225.0),

	("town_52", "Mhysa Faer", icon_map_essos_town|pf_town, no_menu, pt_none, fac_neutral, aggressiveness_0, ai_bhvr_hold, 0, (-166.978, 53.7172), [], 225.0),

	("town_53", "Draconys", icon_map_essos_town|pf_town, no_menu, pt_none, fac_neutral, aggressiveness_0, ai_bhvr_hold, 0, (-145.256, 148.601), [], 225.0),

	("town_54", "Aquos Dhaen", icon_map_essos_town|pf_town, no_menu, pt_none, fac_neutral, aggressiveness_0, ai_bhvr_hold, 0, (-134.672, 214.208), [], 225.0),

	("castle_1", "Strongsong", icon_map_castle_grey|pf_castle, no_menu, pt_none, fac_neutral, aggressiveness_0, ai_bhvr_hold, 0, (71.4507, -76.5227), [], 50.0),

	("castle_2", "Flint's Finger", icon_map_castle_grey|pf_castle, no_menu, pt_none, fac_neutral, aggressiveness_0, ai_bhvr_hold, 0, (185.810257, -131.114319), [], 75.0),

	("castle_3", "Bronzegate", icon_map_castle_wood_what|pf_castle, no_menu, pt_none, fac_neutral, aggressiveness_0, ai_bhvr_hold, 0, (23.9614, 89.9463), [], 100.0),

	("castle_4", "Widow's Watch", icon_map_castle_wood_what|pf_castle, no_menu, pt_none, fac_neutral, aggressiveness_0, ai_bhvr_hold, 0, (5.391174, -175.874084), [], 180.0),

	("castle_5", "Rosby", icon_map_castle_grey|pf_castle, no_menu, pt_none, fac_neutral, aggressiveness_0, ai_bhvr_hold, 0, (49.0908, 43.2746), [], 90.0),

	("castle_6", "Oldcastle", icon_map_castle_white|pf_castle, no_menu, pt_none, fac_neutral, aggressiveness_0, ai_bhvr_hold, 0, (69.604141, -142.265533), [], 55.0),

	("castle_7", "Seagard", icon_map_seagard|pf_castle, no_menu, pt_none, fac_neutral, aggressiveness_0, ai_bhvr_hold, 0, (127.129196, -65.253693), [], 45.0),

	("castle_8", "Fellwood", icon_map_castle_red|pf_castle, no_menu, pt_none, fac_neutral, aggressiveness_0, ai_bhvr_hold, 0, (46.9521, 83.4624), [], 30.0),

	("castle_9", "Moat Cailin", icon_map_moat_cailin|pf_castle, no_menu, pt_none, fac_neutral, aggressiveness_0, ai_bhvr_hold, 0, (108.399, -149.444), [], 100.0),

	("castle_10", "Haystack Hall", icon_map_castle_wood_what|pf_castle, no_menu, pt_none, fac_neutral, aggressiveness_0, ai_bhvr_hold, 0, (10.6312, 78.7436), [], 110.0),

	("castle_11", "Sharp Point", icon_map_castle_red|pf_castle, no_menu, pt_none, fac_neutral, aggressiveness_0, ai_bhvr_hold, 0, (-1.12039, 31.4895), [], 75.0),

	("castle_12", "Wickenden", icon_map_castle_grey|pf_castle, no_menu, pt_none, fac_neutral, aggressiveness_0, ai_bhvr_hold, 0, (28.9288, -10.5862), [], 95.0),

	("castle_13", "Stonedance", icon_map_castle_red|pf_castle, no_menu, pt_none, fac_neutral, aggressiveness_0, ai_bhvr_hold, 0, (-1.842, 44.3124), [], 115.0),

	("castle_14", "Iksa Keria", icon_map_castle_wood_what|pf_castle, no_menu, pt_none, fac_neutral, aggressiveness_0, ai_bhvr_hold, 0, (-118.152, -62.759), [], 90.0),

	("castle_15", "Last Hearth", icon_map_last_hearth|pf_castle, no_menu, pt_none, fac_neutral, aggressiveness_0, ai_bhvr_hold, 0, (50.5546, -292.853), [], 235.0),

	("castle_16", "Antlers", icon_map_castle_grey|pf_castle, no_menu, pt_none, fac_neutral, aggressiveness_0, ai_bhvr_hold, 0, (52.4142, 18.9423), [], 45.0),

	("castle_17", "Cerwyn Castle", icon_map_castle_grey|pf_castle, no_menu, pt_none, fac_neutral, aggressiveness_0, ai_bhvr_hold, 0, (123.313, -227.34), [], 15.0),

	("castle_18", "The Crag", icon_map_castle_grey|pf_castle, no_menu, pt_none, fac_neutral, aggressiveness_0, ai_bhvr_hold, 0, (181.654, -13.6945), [], 300.0),

	("castle_19", "Karhold", icon_map_castle_grey|pf_castle, no_menu, pt_none, fac_neutral, aggressiveness_0, ai_bhvr_hold, 0, (-1.44304, -266.578), [], 280.0),

	("castle_20", "Crow's Nest", icon_map_castle_red|pf_castle, no_menu, pt_none, fac_neutral, aggressiveness_0, ai_bhvr_hold, 0, (30.718895, 132.576828), [], 260.0),

	("castle_21", "Redfort", icon_map_castle_grey|pf_castle, no_menu, pt_none, fac_neutral, aggressiveness_0, ai_bhvr_hold, 0, (25.4718, -28.0979), [], 260.0),

	("castle_22", "Deepwood Motte", icon_map_castle_wood_what|pf_castle, no_menu, pt_none, fac_neutral, aggressiveness_0, ai_bhvr_hold, 0, (150.821884, -266.526825), [], 260.0),

	("castle_23", "Runestone", icon_map_runestone|pf_castle, no_menu, pt_none, fac_neutral, aggressiveness_0, ai_bhvr_hold, 0, (-10.500631, -53.243767), [], 80.0),

	("castle_24", "The Bloody Gate", icon_map_bloody_gate|pf_castle, no_menu, pt_none, fac_neutral, aggressiveness_0, ai_bhvr_hold, 0, (49.8653, -44.391), [], 330.0),

	("castle_25", "Evenfall Hall", icon_map_castle_red|pf_castle, no_menu, pt_none, fac_neutral, aggressiveness_0, ai_bhvr_hold, 0, (-9.25716, 96.7721), [], 260.0),

	("castle_26", "Pinkmaiden", icon_map_castle_grey|pf_castle, no_menu, pt_none, fac_neutral, aggressiveness_0, ai_bhvr_hold, 0, (129.067825, 2.357554), [], 260.0),

	("castle_27", "Mistwood", icon_map_castle_red|pf_castle, no_menu, pt_none, fac_neutral, aggressiveness_0, ai_bhvr_hold, 0, (5.22735, 148.851), [], 260.0),

	("castle_28", "Snakewood", icon_map_castle_grey|pf_castle, no_menu, pt_none, fac_neutral, aggressiveness_0, ai_bhvr_hold, 0, (8.84208, -95.1923), [], 260.0),

	("castle_29", "Harrenhal", icon_map_harrenhal|pf_castle, no_menu, pt_none, fac_neutral, aggressiveness_0, ai_bhvr_hold, 0, (70.884415, 4.789415), [], 280.0),

	("castle_30", "Salt Shore", icon_map_dorne_castle|pf_castle, no_menu, pt_none, fac_neutral, aggressiveness_0, ai_bhvr_hold, 0, (28.745, 229.747), [], 260.0),

	("castle_31", "Banefort", icon_map_castle_grey|pf_castle, no_menu, pt_none, fac_neutral, aggressiveness_0, ai_bhvr_hold, 0, (178.641, -29.6474), [], 260.0),

	("castle_32", "The Dreadfort", icon_map_dreadfort|pf_castle, no_menu, pt_none, fac_neutral, aggressiveness_0, ai_bhvr_hold, 0, (46.835072, -237.361084), [], 260.0),

	("castle_33", "Coldwater Burn", icon_map_castle_grey|pf_castle, no_menu, pt_none, fac_neutral, aggressiveness_0, ai_bhvr_hold, 0, (19.579966, -107.093178), [], 80.0),

	("castle_34", "The Eyrie", icon_map_eyrie|pf_castle, no_menu, pt_none, fac_neutral, aggressiveness_0, ai_bhvr_hold, 0, (59.5758, -56.8648), [], 260.0),

	("castle_35", "Longbow Hall", icon_map_castle_grey|pf_castle, no_menu, pt_none, fac_neutral, aggressiveness_0, ai_bhvr_hold, 0, (-4.321509, -78.679214), [], 260.0),

	("castle_36", "Old Anchor", icon_map_castle_grey|pf_castle, no_menu, pt_none, fac_neutral, aggressiveness_0, ai_bhvr_hold, 0, (-0.779003, -61.3515), [], 260.0),

	("castle_37", "The Crossing", icon_map_twins|pf_castle, no_menu, pt_none, fac_neutral, aggressiveness_0, ai_bhvr_hold, 0, (115.709, -82.2115), [], 315.0),

	("castle_39", "Acorn Hall", icon_map_castle_grey|pf_castle, no_menu, pt_none, fac_neutral, aggressiveness_0, ai_bhvr_hold, 0, (115.539, -2.11807), [], 280.0),

	("castle_40", "Blackhaven", icon_map_dorne_castle|pf_castle, no_menu, pt_none, fac_neutral, aggressiveness_0, ai_bhvr_hold, 0, (84.0002, 142.435), [], 260.0),

	("castle_41", "Lemonwood", icon_map_dorne_castle|pf_castle, no_menu, pt_none, fac_neutral, aggressiveness_0, ai_bhvr_hold, 0, (-1.88101, 221.295), [], 260.0),

	("castle_42", "Yronwood", icon_map_yronwood|pf_castle, no_menu, pt_none, fac_neutral, aggressiveness_0, ai_bhvr_hold, 0, (70.082, 189.269), [], 80.0),

	("castle_43", "Vaith", icon_map_dorne_castle|pf_castle, no_menu, pt_none, fac_neutral, aggressiveness_0, ai_bhvr_hold, 0, (44.481, 218.907), [], 260.0),

	("castle_44", "Sandstone", icon_map_dorne_castle|pf_castle, no_menu, pt_none, fac_neutral, aggressiveness_0, ai_bhvr_hold, 0, (120.101189, 227.65358), [], 260.0),

	("castle_45", "The Tor", icon_map_dorne_castle|pf_castle, no_menu, pt_none, fac_neutral, aggressiveness_0, ai_bhvr_hold, 0, (37.819981, 194.15979), [], 260.0),

	("castle_46", "Ghost Hill", icon_map_dorne_castle|pf_castle, no_menu, pt_none, fac_neutral, aggressiveness_0, ai_bhvr_hold, 0, (-2.00779, 186.386), [], 260.0),

	("castle_47", "Godsgrace", icon_map_dorne_castle|pf_castle, no_menu, pt_none, fac_neutral, aggressiveness_0, ai_bhvr_hold, 0, (19.4514, 216.705), [], 260.0),

	("castle_48", "Kingsgrave", icon_map_dorne_castle|pf_castle, no_menu, pt_none, fac_neutral, aggressiveness_0, ai_bhvr_hold, 0, (126.632, 181.7), [], 260.0),

	("castle_49", "Blackmont", icon_map_dorne_castle|pf_castle, no_menu, pt_none, fac_neutral, aggressiveness_0, ai_bhvr_hold, 0, (139.128, 192.299), [], 260.0),

	("castle_50", "Nightsong", icon_map_dorne_castle|pf_castle, no_menu, pt_none, fac_neutral, aggressiveness_0, ai_bhvr_hold, 0, (118.245, 165.0), [], 260.0),

	("castle_51", "Ashemark", icon_map_castle_grey|pf_castle, no_menu, pt_none, fac_neutral, aggressiveness_0, ai_bhvr_hold, 0, (165.775, -0.26149), [], 260.0),

	("castle_52", "Casterly Rock", icon_map_casterly_rock|pf_castle, no_menu, pt_none, fac_neutral, aggressiveness_0, ai_bhvr_hold, 0, (199.9, 33.8464), [], 280.0),

	("castle_53", "Crakehall", icon_map_castle_grey|pf_castle, no_menu, pt_none, fac_neutral, aggressiveness_0, ai_bhvr_hold, 0, (200.967, 74.7931), [], 260.0),

	("castle_54", "Sarsfield", icon_map_castle_grey|pf_castle, no_menu, pt_none, fac_neutral, aggressiveness_0, ai_bhvr_hold, 0, (171.406, 16.7714), [], 260.0),

	("castle_55", "Hornvale", icon_map_castle_grey|pf_castle, no_menu, pt_none, fac_neutral, aggressiveness_0, ai_bhvr_hold, 0, (129.23, 29.0852), [], 260.0),

	("castle_56", "Deep Den", icon_map_castle_grey|pf_castle, no_menu, pt_none, fac_neutral, aggressiveness_0, ai_bhvr_hold, 0, (129.349, 44.408), [], 260.0),

	("castle_57", "Cornfield", icon_map_castle_white|pf_castle, no_menu, pt_none, fac_neutral, aggressiveness_0, ai_bhvr_hold, 0, (166.318, 72.5274), [], 260.0),

	("castle_59", "Claw Isle", icon_map_castle_grey|pf_castle, no_menu, pt_none, fac_neutral, aggressiveness_0, ai_bhvr_hold, 0, (-18.3375, -8.12899), [], 260.0),

	("castle_60", "Three Towers", icon_map_castle_grey|pf_castle, no_menu, pt_none, fac_neutral, aggressiveness_0, ai_bhvr_hold, 0, (197.216, 204.174), [], 260.0),

	("castle_61", "Uplands", icon_map_castle_wood_what|pf_castle, no_menu, pt_none, fac_neutral, aggressiveness_0, ai_bhvr_hold, 0, (170.726, 192.779), [], 260.0),

	("castle_63", "Bandallon", icon_map_castle_grey|pf_castle, no_menu, pt_none, fac_neutral, aggressiveness_0, ai_bhvr_hold, 0, (206.862, 161.195), [], 260.0),

	("castle_64", "Old Oak", icon_map_castle_grey|pf_castle, no_menu, pt_none, fac_neutral, aggressiveness_0, ai_bhvr_hold, 0, (197.304, 107.702), [], 260.0),

	("castle_65", "Rook's Rest", icon_map_castle_grey|pf_castle, no_menu, pt_none, fac_neutral, aggressiveness_0, ai_bhvr_hold, 0, (15.7729, 7.11904), [], 260.0),

	("castle_66", "Cider Hall", icon_map_castle_grey|pf_castle, no_menu, pt_none, fac_neutral, aggressiveness_0, ai_bhvr_hold, 0, (109.848, 124.945), [], 260.0),

	("castle_67", "Grassfield Keep", icon_map_castle_grey|pf_castle, no_menu, pt_none, fac_neutral, aggressiveness_0, ai_bhvr_hold, 0, (70.1862, 94.2612), [], 260.0),

	("castle_68", "Longtable", icon_map_castle_grey|pf_castle, no_menu, pt_none, fac_neutral, aggressiveness_0, ai_bhvr_hold, 0, (92.0937, 120.343), [], 260.0),

	("castle_69", "Sunhouse", icon_map_castle_grey|pf_castle, no_menu, pt_none, fac_neutral, aggressiveness_0, ai_bhvr_hold, 0, (172.122, 222.587), [], 260.0),

	("castle_70", "Bitterbridge", icon_map_castle_grey|pf_castle, no_menu, pt_none, fac_neutral, aggressiveness_0, ai_bhvr_hold, 0, (93.7655, 105.386), [], 260.0),

	("castle_71", "Horn Hill", icon_map_tarbeck_hall|pf_castle, no_menu, pt_none, fac_neutral, aggressiveness_0, ai_bhvr_hold, 0, (153.762, 162.827), [], 260.0),

	("castle_72", "The Arbor", icon_map_arbor|pf_castle, no_menu, pt_none, fac_neutral, aggressiveness_0, ai_bhvr_hold, 0, (206.149, 231.908), [], 260.0),

	("castle_73", "Ten Towers", icon_map_ten_towers|pf_castle, no_menu, pt_none, fac_neutral, aggressiveness_0, ai_bhvr_hold, 0, (174.639, -50.2997), [], 260.0),

	("castle_74", "The Ruins of Iksa Naron", icon_map_Ruined_Castle|pf_castle, no_menu, pt_none, fac_neutral, aggressiveness_0, ai_bhvr_hold, 0, (-73.9472, -44.8949), [], 260.0),

	("castle_75", "Last Refuge", icon_map_essos_castle|pf_castle, no_menu, pt_none, fac_neutral, aggressiveness_0, ai_bhvr_hold, 0, (-62.7416, 195.225), [], 260.0),

	("castle_76", "Torturer's Deep", icon_map_essos_castle2|pf_castle, no_menu, pt_none, fac_neutral, aggressiveness_0, ai_bhvr_hold, 0, (-51.1616, 159.162), [], 260.0),

	("castle_77", "Blackwall", icon_map_essos_castle2|pf_castle, no_menu, pt_none, fac_neutral, aggressiveness_0, ai_bhvr_hold, 0, (-100.944, 156.644), [], 260.0),

	("castle_78", "Horn of the Seven", icon_map_essos_castle2|pf_castle, no_menu, pt_none, fac_neutral, aggressiveness_0, ai_bhvr_hold, 0, (-69.0912, 49.2282), [], 260.0),

	("castle_79", "Daggerstop", icon_map_essos_castle|pf_castle, no_menu, pt_none, fac_neutral, aggressiveness_0, ai_bhvr_hold, 0, (-204.608, 62.834), [], 260.0),

	("castle_80", "Skyreach", icon_map_dorne_castle|pf_castle, no_menu, pt_none, fac_neutral, aggressiveness_0, ai_bhvr_hold, 0, (125.259, 197.423), [], 260.0),

	("castle_82", "The Ruins of Iksa Calo", icon_map_Ruined_Castle|pf_castle, no_menu, pt_none, fac_neutral, aggressiveness_0, ai_bhvr_hold, 0, (-99.5793, -42.7723), [], 210.0),

	("castle_83", "Griffin's Roost", icon_map_castle_red|pf_castle, no_menu, pt_none, fac_neutral, aggressiveness_0, ai_bhvr_hold, 0, (25.3103, 120.077), [], 260.0),

	("castle_84", "Rain House", icon_map_castle_red|pf_castle, no_menu, pt_none, fac_neutral, aggressiveness_0, ai_bhvr_hold, 0, (-17.1707, 128.177), [], 260.0),

	("castle_85", "Greenstone", icon_map_castle_grey|pf_castle, no_menu, pt_none, fac_neutral, aggressiveness_0, ai_bhvr_hold, 0, (-12.1516, 152.08), [], 260.0),

	("castle_86", "Stone Hedge", icon_map_castle_white|pf_castle, no_menu, pt_none, fac_neutral, aggressiveness_0, ai_bhvr_hold, 0, (91.7356, -23.6562), [], 260.0),

	("castle_87", "Silverhall", icon_map_castle_grey|pf_castle, no_menu, pt_none, fac_neutral, aggressiveness_0, ai_bhvr_hold, 0, (140.808, 61.9112), [], 260.0),

	("castle_88", "Hornwood", icon_map_castle_white|pf_castle, no_menu, pt_none, fac_neutral, aggressiveness_0, ai_bhvr_hold, 0, (65.8877, -187.69), [], 260.0),

	("castle_89", "Raventree Hall", icon_map_castle_grey|pf_castle, no_menu, pt_none, fac_neutral, aggressiveness_0, ai_bhvr_hold, 0, (119.312, -39.4546), [], 260.0),

	("castle_90", "Faircastle", icon_map_castle_grey|pf_castle, no_menu, pt_none, fac_neutral, aggressiveness_0, ai_bhvr_hold, 0, (202.852, 10.2205), [], 260.0),

	("castle_91", "Pebbleton Tower", icon_map_castle_grey|pf_castle, no_menu, pt_none, fac_neutral, aggressiveness_0, ai_bhvr_hold, 0, (201.241, -50.5048), [], 80.0),

	("castle_92", "Feastfires", icon_map_castle_grey|pf_castle, no_menu, pt_none, fac_neutral, aggressiveness_0, ai_bhvr_hold, 0, (217.145, 34.0778), [], 260.0),

	("castle_93", "High Hermitage", icon_map_dorne_castle|pf_castle, no_menu, pt_none, fac_neutral, aggressiveness_0, ai_bhvr_hold, 0, (142.932, 196.506), [], 260.0),

	("castle_95", "Hammerhorn", icon_map_castle_wood_what|pf_castle, no_menu, pt_none, fac_neutral, aggressiveness_0, ai_bhvr_hold, 0, (210.451, -67.8734), [], 260.0),

	("castle_96", "Grey Garden", icon_map_castle_wood_what|pf_castle, no_menu, pt_none, fac_neutral, aggressiveness_0, ai_bhvr_hold, 0, (185.306, -51.6572), [], 260.0),

	("castle_99", "Wyl", icon_map_dorne_castle|pf_castle, no_menu, pt_none, fac_neutral, aggressiveness_0, ai_bhvr_hold, 0, (74.5277, 159.306), [], 260.0),

	("castle_100", "Ironoaks", icon_map_castle_white|pf_castle, no_menu, pt_none, fac_neutral, aggressiveness_0, ai_bhvr_hold, 0, (17.4688, -53.1561), [], 260.0),

	("castle_104", "Iron Holt", icon_map_castle_grey|pf_castle, no_menu, pt_none, fac_neutral, aggressiveness_0, ai_bhvr_hold, 0, (199.142, -36.3507), [], 260.0),

	("castle_105", "Brightwater Keep", icon_map_castle_grey|pf_castle, no_menu, pt_none, fac_neutral, aggressiveness_0, ai_bhvr_hold, 0, (186.571, 156.941), [], 260.0),

	("castle_106", "Heart's Home", icon_map_castle_wood_what|pf_castle, no_menu, pt_none, fac_neutral, aggressiveness_0, ai_bhvr_hold, 0, (31.2934, -82.5424), [], 260.0),

	("castle_107", "The Ruins of Sar Mell", icon_map_Ruined_Castle|pf_castle, no_menu, pt_none, fac_neutral, aggressiveness_0, ai_bhvr_hold, 0, (-202.995, 200.754), [], 260.0),

	("castle_108", "Longsister", icon_map_castle_wood_what|pf_castle, no_menu, pt_none, fac_neutral, aggressiveness_0, ai_bhvr_hold, 0, (72.7401, -122.437), [], 260.0),

	("castle_109", "Littlesister", icon_map_castle_grey|pf_castle, no_menu, pt_none, fac_neutral, aggressiveness_0, ai_bhvr_hold, 0, (50.3893, -127.916), [], 260.0),

	("castle_110", "Darry", icon_map_castle_grey|pf_castle, no_menu, pt_none, fac_neutral, aggressiveness_0, ai_bhvr_hold, 0, (63.9198, -7.58416), [], 260.0),

	("castle_111", "Oakenshield", icon_map_castle_grey|pf_castle, no_menu, pt_none, fac_neutral, aggressiveness_0, ai_bhvr_hold, 0, (196.346, 126.272), [], 260.0),

	("castle_112", "Grey Cliffs", icon_map_castle_white|pf_castle, no_menu, pt_none, fac_neutral, aggressiveness_0, ai_bhvr_hold, 0, (-153.953, -47.2907), [], 260.0),

	("castle_115", "Red Lake", icon_map_castle_grey|pf_castle, no_menu, pt_none, fac_neutral, aggressiveness_0, ai_bhvr_hold, 0, (167.247, 97.8387), [], 260.0),

	("castle_119", "Blacktyde Castle", icon_map_castle_grey|pf_castle, no_menu, pt_none, fac_neutral, aggressiveness_0, ai_bhvr_hold, 0, (192.254, -74.8964), [], 260.0),

	("castle_120", "Wyk Hall", icon_map_castle_grey|pf_castle, no_menu, pt_none, fac_neutral, aggressiveness_0, ai_bhvr_hold, 0, (206.098, -59.5372), [], 260.0),

	("castle_127", "Riverrun", icon_map_riverrun|pf_castle, no_menu, pt_none, fac_neutral, aggressiveness_0, ai_bhvr_hold, 0, (113.99, -24.3455), [], 120.0),

	("castle_128", "Aysel Keep", icon_map_dorne_castle|pf_castle, no_menu, pt_none, fac_neutral, aggressiveness_0, ai_bhvr_hold, 0, (-112.24, 185.958), [], 225.0),

	("castle_129", "Winterfell", icon_map_winterfell|pf_castle, no_menu, pt_none, fac_neutral, aggressiveness_0, ai_bhvr_hold, 0, (105.677, -230.088), [], 90.0),

	("castle_130", "Storm's End", icon_map_storms_end|pf_castle, no_menu, pt_none, fac_neutral, aggressiveness_0, ai_bhvr_hold, 0, (8.2017, 108.607), [], 155.0),

	("castle_131", "Torrhen's Square", icon_map_Clegane_Keep|pf_castle, no_menu, pt_none, fac_neutral, aggressiveness_0, ai_bhvr_hold, 0, (134.085, -202.473), [], 150.0),

	("castle_132", "Stonehelm", icon_map_dorne_castle|pf_castle, no_menu, pt_none, fac_neutral, aggressiveness_0, ai_bhvr_hold, 0, (42.9999, 143.141), [], 60.0),

	("castle_133", "Highgarden", icon_map_highgarden|pf_castle, no_menu, pt_none, fac_neutral, aggressiveness_0, ai_bhvr_hold, 0, (141.931, 141.997), [], 45.0),

	("castle_134", "Hellholt", icon_map_dorne_castle|pf_castle, no_menu, pt_none, fac_neutral, aggressiveness_0, ai_bhvr_hold, 0, (94.718697, 224.865997), [], 330.0),

	("castle_135", "Starfall", icon_map_dorne_castle|pf_castle, no_menu, pt_none, fac_neutral, aggressiveness_0, ai_bhvr_hold, 0, (150.365, 216.241), [], 225.0),

	("castle_136", "The Golden Tooth", icon_map_castle_grey|pf_castle, no_menu, pt_none, fac_neutral, aggressiveness_0, ai_bhvr_hold, 0, (144.873, 4.28708), [], 225.0),

	("castle_137", "High Tide", icon_map_castle_grey|pf_castle, no_menu, pt_none, fac_neutral, aggressiveness_0, ai_bhvr_hold, 0, (3.61879, 15.0568), [], 225.0),

	("castle_138", "Bear Island", icon_map_castle_wood_what|pf_castle, no_menu, pt_none, fac_neutral, aggressiveness_0, ai_bhvr_hold, 0, (158.039, -301.679), [], 225.0),

	("castle_139", "Stokeworth", icon_map_castle_red|pf_castle, no_menu, pt_none, fac_neutral, aggressiveness_0, ai_bhvr_hold, 0, (59.1665, 40.6229), [], 30.0),

	("castle_140", "Pyke", icon_map_pyke|pf_castle, no_menu, pt_none, fac_neutral, aggressiveness_0, ai_bhvr_hold, 0, (196.783, -41.815), [], 80.0),

	("castle_141", "Grey Gallows", icon_map_essos_castle2|pf_castle, no_menu, pt_none, fac_neutral, aggressiveness_0, ai_bhvr_hold, 0, (-54.4596, 176.245), [], 260.0),

	("castle_142", "Eryas", icon_map_essos_castle2|pf_castle, no_menu, pt_none, fac_neutral, aggressiveness_0, ai_bhvr_hold, 0, (-193.943, 82.7546), [], 260.0),

	("village_1", "The Rills", icon_village_a|pf_village, no_menu, pt_none, fac_neutral, aggressiveness_0, ai_bhvr_hold, 0, (197.983, -184.235), [], 100.0),

	("village_2", "Coldwolf", icon_village_a|pf_village, no_menu, pt_none, fac_neutral, aggressiveness_0, ai_bhvr_hold, 0, (168.969, -171.866), [], 110.0),

	("village_3", "Dragon's Neck", icon_village_a|pf_village, no_menu, pt_none, fac_neutral, aggressiveness_0, ai_bhvr_hold, 0, (177.309, -259.789), [], 120.0),

	("village_4", "Prawn Bay", icon_village_a|pf_village, no_menu, pt_none, fac_neutral, aggressiveness_0, ai_bhvr_hold, 0, (-1.6121, 155.945), [], 130.0),

	("village_5", "Whiteoak", icon_village_a|pf_village, no_menu, pt_none, fac_neutral, aggressiveness_0, ai_bhvr_hold, 0, (30.1938, -250.223), [], 170.0),

	("village_6", "Greyedge", icon_village_a|pf_village, no_menu, pt_none, fac_neutral, aggressiveness_0, ai_bhvr_hold, 0, (16.763599, -265.554993), [], 100.0),

	("village_7", "Deepcrest", icon_village_a|pf_village, no_menu, pt_none, fac_neutral, aggressiveness_0, ai_bhvr_hold, 0, (37.538898, -228.078995), [], 110.0),

	("village_8", "Eastwood", icon_village_a|pf_village, no_menu, pt_none, fac_neutral, aggressiveness_0, ai_bhvr_hold, 0, (11.9489, -181.550995), [], 120.0),

	("village_9", "Oldwall", icon_village_a|pf_village, no_menu, pt_none, fac_neutral, aggressiveness_0, ai_bhvr_hold, 0, (37.251999, -184.518005), [], 130.0),

	("village_10", "The Locke", icon_village_a|pf_village, no_menu, pt_none, fac_neutral, aggressiveness_0, ai_bhvr_hold, 0, (63.0783, -145.925995), [], 170.0),

	("village_11", "Brightfog", icon_village_a|pf_village, no_menu, pt_none, fac_neutral, aggressiveness_0, ai_bhvr_hold, 0, (83.391899, -156.061005), [], 100.0),

	("village_12", "Woolfield", icon_village_a|pf_village, no_menu, pt_none, fac_neutral, aggressiveness_0, ai_bhvr_hold, 0, (79.544601, -178.658997), [], 110.0),

	("village_13", "Pike Market", icon_village_a|pf_village, no_menu, pt_none, fac_neutral, aggressiveness_0, ai_bhvr_hold, 0, (84.9627, -147.026993), [], 120.0),

	("village_14", "Crofter's Village", icon_village_a|pf_village, no_menu, pt_none, fac_neutral, aggressiveness_0, ai_bhvr_hold, 0, (102.649002, -236.074005), [], 130.0),

	("village_15", "Wildeland", icon_village_a|pf_village, no_menu, pt_none, fac_neutral, aggressiveness_0, ai_bhvr_hold, 0, (202.828, -221.759), [], 170.0),

	("village_16", "Crow's Rest", icon_village_a|pf_village, no_menu, pt_none, fac_neutral, aggressiveness_0, ai_bhvr_hold, 0, (93.4593, -193.63), [], 170.0),

	("village_17", "Sentinel's Tree", icon_village_a|pf_village, no_menu, pt_none, fac_neutral, aggressiveness_0, ai_bhvr_hold, 0, (158.61, -204.868), [], 35.0),

	("village_18", "Blazewater Bay", icon_village_a|pf_village, no_menu, pt_none, fac_neutral, aggressiveness_0, ai_bhvr_hold, 0, (124.608002, -153.679993), [], 170.0),

	("village_19", "Goldgrass", icon_village_a|pf_village, no_menu, pt_none, fac_neutral, aggressiveness_0, ai_bhvr_hold, 0, (158.248001, -167.192993), [], 170.0),

	("village_20", "Ironrath", icon_village_a|pf_village, no_menu, pt_none, fac_neutral, aggressiveness_0, ai_bhvr_hold, 0, (126.792, -276.904), [], 170.0),

	("village_21", "Cape Kraken", icon_village_a|pf_village, no_menu, pt_none, fac_neutral, aggressiveness_0, ai_bhvr_hold, 0, (205.332, -130.32), [], 100.0),

	("village_22", "Whitehill", icon_village_a|pf_village, no_menu, pt_none, fac_neutral, aggressiveness_0, ai_bhvr_hold, 0, (105.085, -160.057), [], 110.0),

	("village_23", "Sevenstreams", icon_village_a|pf_village, no_menu, pt_none, fac_neutral, aggressiveness_0, ai_bhvr_hold, 0, (105.527, -67.4345), [], 120.0),

	("village_24", "Hag's Mire", icon_village_a|pf_village, no_menu, pt_none, fac_neutral, aggressiveness_0, ai_bhvr_hold, 0, (87.5106, -45.6726), [], 130.0),

	("village_25", "Calwick", icon_village_a|pf_village, no_menu, pt_none, fac_neutral, aggressiveness_0, ai_bhvr_hold, 0, (209.676, 15.2173), [], 170.0),

	("village_26", "The High Fall", icon_village_a|pf_village, no_menu, pt_none, fac_neutral, aggressiveness_0, ai_bhvr_hold, 0, (139.043, -41.715), [], 170.0),

	("village_27", "Sallydance", icon_village_a|pf_village, no_menu, pt_none, fac_neutral, aggressiveness_0, ai_bhvr_hold, 0, (98.964996, -27.292), [], 170.0),

	("village_28", "High Heart", icon_village_a|pf_village, no_menu, pt_none, fac_neutral, aggressiveness_0, ai_bhvr_hold, 0, (113.525, -6.18343), [], 110.0),

	("village_29", "Mousedown Mill", icon_village_a|pf_village, no_menu, pt_none, fac_neutral, aggressiveness_0, ai_bhvr_hold, 0, (127.471001, -2.12901), [], 170.0),

	("village_30", "Ramsford", icon_village_a|pf_village, no_menu, pt_none, fac_neutral, aggressiveness_0, ai_bhvr_hold, 0, (122.818001, -53.227402), [], 170.0),

	("village_31", "Elk Wood", icon_village_a|pf_village, no_menu, pt_none, fac_neutral, aggressiveness_0, ai_bhvr_hold, 0, (-98.153, -71.3071), [], 100.0),

	("village_32", "Orshore", icon_village_a|pf_village, no_menu, pt_none, fac_neutral, aggressiveness_0, ai_bhvr_hold, 0, (-76.7045, -88.8108), [], 110.0),

	("village_33", "Gull Tower", icon_village_a|pf_village, no_menu, pt_none, fac_neutral, aggressiveness_0, ai_bhvr_hold, 0, (-22.5359, -46.0682), [], 120.0),

	("village_34", "The Crab's Nest", icon_village_a|pf_village, no_menu, pt_none, fac_neutral, aggressiveness_0, ai_bhvr_hold, 0, (9.59694, -41.5961), [], 130.0),

	("village_35", "Grey Glen", icon_village_a|pf_village, no_menu, pt_none, fac_neutral, aggressiveness_0, ai_bhvr_hold, 0, (-24.2737, -54.0635), [], 170.0),

	("village_36", "Dorbarrow", icon_village_a|pf_village, no_menu, pt_none, fac_neutral, aggressiveness_0, ai_bhvr_hold, 0, (18.77, -32.4157), [], 170.0),

	("village_37", "Easthedge", icon_village_a|pf_village, no_menu, pt_none, fac_neutral, aggressiveness_0, ai_bhvr_hold, 0, (17.0668, -19.8422), [], 170.0),

	("village_38", "The Old Barrow", icon_village_a|pf_village, no_menu, pt_none, fac_neutral, aggressiveness_0, ai_bhvr_hold, 0, (50.8916, -126.794), [], 170.0),

	("village_39", "Greywall", icon_village_a|pf_village, no_menu, pt_none, fac_neutral, aggressiveness_0, ai_bhvr_hold, 0, (24.1099, -90.6154), [], 170.0),

	("village_40", "Monton", icon_village_a|pf_village, no_menu, pt_none, fac_neutral, aggressiveness_0, ai_bhvr_hold, 0, (70.9869, -65.8816), [], 170.0),

	("village_41", "Valetown", icon_village_a|pf_village, no_menu, pt_none, fac_neutral, aggressiveness_0, ai_bhvr_hold, 0, (33.6462, -52.1865), [], 100.0),

	("village_42", "Newkeep", icon_village_a|pf_village, no_menu, pt_none, fac_neutral, aggressiveness_0, ai_bhvr_hold, 0, (37.6336, -68.2871), [], 110.0),

	("village_43", "Fingermarket", icon_village_a|pf_village, no_menu, pt_none, fac_neutral, aggressiveness_0, ai_bhvr_hold, 0, (-10.8219, -92.7277), [], 120.0),

	("village_44", "Merlings Cliff", icon_village_a|pf_village, no_menu, pt_none, fac_neutral, aggressiveness_0, ai_bhvr_hold, 0, (-11.1286, -66.4733), [], 130.0),

	("village_45", "Driftwood", icon_village_a|pf_village, no_menu, pt_none, fac_neutral, aggressiveness_0, ai_bhvr_hold, 0, (32.0715, -75.9224), [], 170.0),

	("village_46", "Massey's Hook", icon_village_a|pf_village, no_menu, pt_none, fac_neutral, aggressiveness_0, ai_bhvr_hold, 0, (2.2004, 48.6981), [], 170.0),

	("village_47", "Highlock", icon_village_a|pf_village, no_menu, pt_none, fac_neutral, aggressiveness_0, ai_bhvr_hold, 0, (-3.89952, 40.3819), [], 170.0),

	("village_48", "Woodsway", icon_village_a|pf_village, no_menu, pt_none, fac_neutral, aggressiveness_0, ai_bhvr_hold, 0, (25.4738, 86.0592), [], 170.0),

	("village_49", "Poddingfield", icon_village_a|pf_village, no_menu, pt_none, fac_neutral, aggressiveness_0, ai_bhvr_hold, 0, (-1.16462, 84.6103), [], 10.0),

	("village_50", "Kingsway", icon_village_a|pf_village, no_menu, pt_none, fac_neutral, aggressiveness_0, ai_bhvr_hold, 0, (43.8751, 74.5472), [], 170.0),

	("village_51", "Crickhollow", icon_village_a|pf_village, no_menu, pt_none, fac_neutral, aggressiveness_0, ai_bhvr_hold, 0, (5.57368, 94.251), [], 100.0),

	("village_52", "Sapphire Bay ", icon_village_a|pf_village, no_menu, pt_none, fac_neutral, aggressiveness_0, ai_bhvr_hold, 0, (-14.5904, 105.884), [], 110.0),

	("village_53", "Barrowhall", icon_village_a|pf_village, no_menu, pt_none, fac_neutral, aggressiveness_0, ai_bhvr_hold, 0, (28.8366, 111.539), [], 120.0),

	("village_54", "Slayne", icon_village_a|pf_village, no_menu, pt_none, fac_neutral, aggressiveness_0, ai_bhvr_hold, 0, (39.0088, 150.822), [], 130.0),

	("village_55", "Stonebridge", icon_village_a|pf_village, no_menu, pt_none, fac_neutral, aggressiveness_0, ai_bhvr_hold, 0, (0.249902, 147.498), [], 170.0),

	("village_56", "Elmwood", icon_village_a|pf_village, no_menu, pt_none, fac_neutral, aggressiveness_0, ai_bhvr_hold, 0, (83.2206, 122.447), [], 170.0),

	("village_57", "Kellington", icon_village_a|pf_village, no_menu, pt_none, fac_neutral, aggressiveness_0, ai_bhvr_hold, 0, (25.6718, 136.227), [], 170.0),

	("village_58", "Stonehand", icon_village_a|pf_village, no_menu, pt_none, fac_neutral, aggressiveness_0, ai_bhvr_hold, 0, (-7.38265, 190.094), [], 170.0),

	("village_59", "Dellhollow", icon_village_a|pf_village, no_menu, pt_none, fac_neutral, aggressiveness_0, ai_bhvr_hold, 0, (96.1344, 38.7883), [], 170.0),

	("village_60", "Dovedale", icon_village_a|pf_village, no_menu, pt_none, fac_neutral, aggressiveness_0, ai_bhvr_hold, 0, (-14.7842, 206.74), [], 170.0),

	("village_61", "Greencrest", icon_village_a|pf_village, no_menu, pt_none, fac_neutral, aggressiveness_0, ai_bhvr_hold, 0, (4.18985, 218.515), [], 100.0),

	("village_62", "Spottswood", icon_village_a|pf_village, no_menu, pt_none, fac_neutral, aggressiveness_0, ai_bhvr_hold, 0, (93.0454, 230.85), [], 100.0),

	("village_63", "Blackmarrow", icon_village_a|pf_village, no_menu, pt_none, fac_neutral, aggressiveness_0, ai_bhvr_hold, 0, (122.425, 238.387), [], 100.0),

	("village_64", "The Farthest Reef", icon_village_a|pf_village, no_menu, pt_none, fac_neutral, aggressiveness_0, ai_bhvr_hold, 0, (-177.252, 242.015), [], 100.0),

	("village_65", "Red Dunes", icon_village_a|pf_village, no_menu, pt_none, fac_neutral, aggressiveness_0, ai_bhvr_hold, 0, (22.5999, 218.794), [], 100.0),

	("village_66", "Shandystone", icon_village_a|pf_village, no_menu, pt_none, fac_neutral, aggressiveness_0, ai_bhvr_hold, 0, (29.9253, 193.778), [], 100.0),

	("village_67", "Seamarket", icon_village_a|pf_village, no_menu, pt_none, fac_neutral, aggressiveness_0, ai_bhvr_hold, 0, (75.9722, 184.8), [], 100.0),

	("village_68", "Greywynne", icon_village_a|pf_village, no_menu, pt_none, fac_neutral, aggressiveness_0, ai_bhvr_hold, 0, (-91.3701, 42.4794), [], 100.0),

	("village_69", "Ryamsport", icon_village_a|pf_village, no_menu, pt_none, fac_neutral, aggressiveness_0, ai_bhvr_hold, 0, (176.409, 224.225), [], 100.0),

	("village_70", "Waystone", icon_village_a|pf_village, no_menu, pt_none, fac_neutral, aggressiveness_0, ai_bhvr_hold, 0, (148.433, 214.092), [], 100.0),

	("village_71", "Sandmere", icon_village_a|pf_village, no_menu, pt_none, fac_neutral, aggressiveness_0, ai_bhvr_hold, 0, (147.72, 191.814), [], 20.0),

	("village_72", "Seafair", icon_village_a|pf_village, no_menu, pt_none, fac_neutral, aggressiveness_0, ai_bhvr_hold, 0, (16.109, 229.86), [], 60.0),

	("village_73", "Bittersweet", icon_village_a|pf_village, no_menu, pt_none, fac_neutral, aggressiveness_0, ai_bhvr_hold, 0, (135.318, 163.988), [], 55.0),

	("village_74", "Falwell", icon_village_a|pf_village, no_menu, pt_none, fac_neutral, aggressiveness_0, ai_bhvr_hold, 0, (142.871, 74.3337), [], 15.0),

	("village_75", "Briarwhite", icon_village_a|pf_village, no_menu, pt_none, fac_neutral, aggressiveness_0, ai_bhvr_hold, 0, (67.2785, 24.692), [], 10.0),

	("village_76", "Landwick", icon_village_a|pf_village, no_menu, pt_none, fac_neutral, aggressiveness_0, ai_bhvr_hold, 0, (170.39, -30.8429), [], 35.0),

	("village_77", "Bluegold", icon_village_a|pf_village, no_menu, pt_none, fac_neutral, aggressiveness_0, ai_bhvr_hold, 0, (185.849, 1.62432), [], 160.0),

	("village_78", "Windbarrow", icon_village_a|pf_village, no_menu, pt_none, fac_neutral, aggressiveness_0, ai_bhvr_hold, 0, (141.268, 181.051), [], 110.0),

	("village_79", "Chelsted", icon_village_a|pf_village, no_menu, pt_none, fac_neutral, aggressiveness_0, ai_bhvr_hold, 0, (66.0145, 57.3052), []),

	("village_80", "Rollingford", icon_village_a|pf_village, no_menu, pt_none, fac_neutral, aggressiveness_0, ai_bhvr_hold, 0, (86.7732, 47.131), [], 40.0),

	("village_81", "Tumblers Hall", icon_village_a|pf_village, no_menu, pt_none, fac_neutral, aggressiveness_0, ai_bhvr_hold, 0, (86.5109, 68.1009), [], 20.0),

	("village_82", "Rushing Falls", icon_village_a|pf_village, no_menu, pt_none, fac_neutral, aggressiveness_0, ai_bhvr_hold, 0, (52.0684, -2.88046), [], 60.0),

	("village_83", "Bronzewood", icon_village_a|pf_village, no_menu, pt_none, fac_neutral, aggressiveness_0, ai_bhvr_hold, 0, (196.252, 50.8367), [], 55.0),

	("village_84", "Westden", icon_village_a|pf_village, no_menu, pt_none, fac_neutral, aggressiveness_0, ai_bhvr_hold, 0, (170.835, 54.4879), [], 15.0),

	("village_85", "Oxcross", icon_village_a|pf_village, no_menu, pt_none, fac_neutral, aggressiveness_0, ai_bhvr_hold, 0, (200.486, 21.1616), [], 10.0),

	("village_86", "Rosemere", icon_village_a|pf_village, no_menu, pt_none, fac_neutral, aggressiveness_0, ai_bhvr_hold, 0, (71.824, 76.4483), [], 35.0),

	("village_87", "Blackbridge", icon_village_a|pf_village, no_menu, pt_none, fac_neutral, aggressiveness_0, ai_bhvr_hold, 0, (142.306, 17.4184), [], 160.0),

	("village_88", "Langward", icon_village_a|pf_village, no_menu, pt_none, fac_neutral, aggressiveness_0, ai_bhvr_hold, 0, (31.4827, 34.6069), [], 180.0),

	("village_89", "Teagueton", icon_village_a|pf_village, no_menu, pt_none, fac_neutral, aggressiveness_0, ai_bhvr_hold, 0, (78.1357, -11.2767), []),

	("village_90", "Gull Point", icon_village_a|pf_village, no_menu, pt_none, fac_neutral, aggressiveness_0, ai_bhvr_hold, 0, (10.845, -110.81), [], 40.0),

	("village_91", "Roosterton", icon_village_a|pf_village, no_menu, pt_none, fac_neutral, aggressiveness_0, ai_bhvr_hold, 0, (172.554, 83.306), [], 20.0),

	("village_92", "Peckledon", icon_village_a|pf_village, no_menu, pt_none, fac_neutral, aggressiveness_0, ai_bhvr_hold, 0, (203.78, 82.3715), [], 60.0),

	("village_93", "Crossed Elms", icon_village_a|pf_village, no_menu, pt_none, fac_neutral, aggressiveness_0, ai_bhvr_hold, 0, (77.2697, 1.12846), [], 55.0),

	("village_94", "Aldbridge", icon_village_a|pf_village, no_menu, pt_none, fac_neutral, aggressiveness_0, ai_bhvr_hold, 0, (140.812, 40.0559), [], 15.0),

	("village_95", "Mormarsh", icon_village_a|pf_village, no_menu, pt_none, fac_neutral, aggressiveness_0, ai_bhvr_hold, 0, (166.353, 13.8725), [], 10.0),

	("village_96", "Charnhall", icon_village_a|pf_village, no_menu, pt_none, fac_neutral, aggressiveness_0, ai_bhvr_hold, 0, (155.837, 2.70686), [], 35.0),

	("village_97", "Westwall Way", icon_village_a|pf_village, no_menu, pt_none, fac_neutral, aggressiveness_0, ai_bhvr_hold, 0, (156.899, 25.4227), [], 160.0),

	("village_98", "Heart's Hill", icon_village_a|pf_village, no_menu, pt_none, fac_neutral, aggressiveness_0, ai_bhvr_hold, 0, (158.917, 166.999), [], 180.0),

	("village_99", "Grapegrove", icon_village_a|pf_village, no_menu, pt_none, fac_neutral, aggressiveness_0, ai_bhvr_hold, 0, (209.345, 235.451), []),

	("village_100", "Cobble Cover", icon_village_a|pf_village, no_menu, pt_none, fac_neutral, aggressiveness_0, ai_bhvr_hold, 0, (136.21, 119.524), [], 40.0),

	("village_101", "Ivy Hall", icon_village_a|pf_village, no_menu, pt_none, fac_neutral, aggressiveness_0, ai_bhvr_hold, 0, (191.954, 215.521), [], 20.0),

	("village_102", "Honeywine", icon_village_a|pf_village, no_menu, pt_none, fac_neutral, aggressiveness_0, ai_bhvr_hold, 0, (192.586, 180.39), [], 60.0),

	("village_103", "Hornrock", icon_village_a|pf_village, no_menu, pt_none, fac_neutral, aggressiveness_0, ai_bhvr_hold, 0, (163.932, 123.199), [], 55.0),

	("village_104", "Donnelwood", icon_village_a|pf_village, no_menu, pt_none, fac_neutral, aggressiveness_0, ai_bhvr_hold, 0, (208.139, 186.871), [], 15.0),

	("village_105", "The Sunset Harbor", icon_village_a|pf_village, no_menu, pt_none, fac_neutral, aggressiveness_0, ai_bhvr_hold, 0, (182.182, 143.75), [], 10.0),

	("village_106", "Honeyholt", icon_village_a|pf_village, no_menu, pt_none, fac_neutral, aggressiveness_0, ai_bhvr_hold, 0, (191.152, 190.992), [], 35.0),

	("village_107", "Lowland Hall", icon_village_a|pf_village, no_menu, pt_none, fac_neutral, aggressiveness_0, ai_bhvr_hold, 0, (175.134, 204.535), [], 160.0),

	("village_108", "Dosk", icon_village_a|pf_village, no_menu, pt_none, fac_neutral, aggressiveness_0, ai_bhvr_hold, 0, (123.233, 118.523), [], 180.0),

	("village_109", "Fairview", icon_village_a|pf_village, no_menu, pt_none, fac_neutral, aggressiveness_0, ai_bhvr_hold, 0, (157.883, 146.485), []),

	("village_110", "Cockleswent", icon_village_a|pf_village, no_menu, pt_none, fac_neutral, aggressiveness_0, ai_bhvr_hold, 0, (113.877, 139.67), [], 40.0),

	("village_111", "Beechberry", icon_village_a|pf_village, no_menu, pt_none, fac_neutral, aggressiveness_0, ai_bhvr_hold, 0, (98.6414, 131.339), [], 40.0),

	("village_112", "Ravendale", icon_village_a|pf_village, no_menu, pt_none, fac_neutral, aggressiveness_0, ai_bhvr_hold, 0, (83.8936, 150.107), [], 40.0),

	("village_113", "Oxhurst", icon_village_a|pf_village, no_menu, pt_none, fac_neutral, aggressiveness_0, ai_bhvr_hold, 0, (108.763, 160.495), [], 40.0),

	("village_114", "Fayford", icon_village_a|pf_village, no_menu, pt_none, fac_neutral, aggressiveness_0, ai_bhvr_hold, 0, (90.764, 86.0893), [], 40.0),

	("village_115", "Charcoal Hill", icon_village_a|pf_village, no_menu, pt_none, fac_neutral, aggressiveness_0, ai_bhvr_hold, 0, (72.0428, 107.929), [], 40.0),

	("village_116", "Nagga's Craddle", icon_village_a|pf_village, no_menu, pt_none, fac_neutral, aggressiveness_0, ai_bhvr_hold, 0, (188.744, -75.6748), [], 40.0),

	("village_117", "Sealskin Point", icon_village_a|pf_village, no_menu, pt_none, fac_neutral, aggressiveness_0, ai_bhvr_hold, 0, (214.119, -48.1702), [], 40.0),

	("village_118", "Saltcliffe", icon_village_a|pf_village, no_menu, pt_none, fac_neutral, aggressiveness_0, ai_bhvr_hold, 0, (212.907, -36.1766), [], 40.0),

	("village_119", "Harlaw Hall", icon_village_a|pf_village, no_menu, pt_none, fac_neutral, aggressiveness_0, ai_bhvr_hold, 0, (177.269, -58.0952), [], 40.0),

	("village_120", "Orkmont", icon_village_a|pf_village, no_menu, pt_none, fac_neutral, aggressiveness_0, ai_bhvr_hold, 0, (188.976, -65.6004), [], 40.0),

	("village_121", "Downdelving", icon_village_a|pf_village, no_menu, pt_none, fac_neutral, aggressiveness_0, ai_bhvr_hold, 0, (218.277, -62.2962), [], 40.0),

	("village_122", "Tower of Glimmering", icon_village_a|pf_village, no_menu, pt_none, fac_neutral, aggressiveness_0, ai_bhvr_hold, 0, (181.145, -47.7529), [], 40.0),

	("village_123", "The Tree of Crowns", icon_village_c|pf_village, no_menu, pt_none, fac_neutral, aggressiveness_0, ai_bhvr_hold, 0, (-130.681, 150.487), [], 40.0),

	("village_124", "Journey's End", icon_village_c|pf_village, no_menu, pt_none, fac_neutral, aggressiveness_0, ai_bhvr_hold, 0, (124.003, 177.995), [], 40.0),

	("village_125", "Barrowness", icon_village_c|pf_village, no_menu, pt_none, fac_neutral, aggressiveness_0, ai_bhvr_hold, 0, (-109.49, -81.485), [], 40.0),

	("village_126", "Wildewater", icon_village_c|pf_village, no_menu, pt_none, fac_neutral, aggressiveness_0, ai_bhvr_hold, 0, (-93.669, 11.608), [], 40.0),

	("village_127", "Redash", icon_village_c|pf_village, no_menu, pt_none, fac_neutral, aggressiveness_0, ai_bhvr_hold, 0, (-115.98, 51.9929), [], 40.0),

	("village_128", "High Hall", icon_village_c|pf_village, no_menu, pt_none, fac_neutral, aggressiveness_0, ai_bhvr_hold, 0, (61.9704, -80.4464), [], 40.0),

	("village_129", "Ester Marrow", icon_village_c|pf_village, no_menu, pt_none, fac_neutral, aggressiveness_0, ai_bhvr_hold, 0, (-101.228, -55.542), [], 40.0),

	("village_130", "Brywyne", icon_village_c|pf_village, no_menu, pt_none, fac_neutral, aggressiveness_0, ai_bhvr_hold, 0, (-103.382, -84.4395), [], 40.0),

	("village_131", "Redbarrow", icon_village_c|pf_village, no_menu, pt_none, fac_neutral, aggressiveness_0, ai_bhvr_hold, 0, (-169.508, 32.3489), [], 40.0),

	("village_132", "Spice Yard", icon_village_c|pf_village, no_menu, pt_none, fac_neutral, aggressiveness_0, ai_bhvr_hold, 0, (-87.3386, 237.853), [], 40.0),

	("village_133", "Estwynd", icon_village_c|pf_village, no_menu, pt_none, fac_neutral, aggressiveness_0, ai_bhvr_hold, 0, (-68.2028, 150.962), [], 40.0),

	("village_134", "The Amber Stream", icon_village_c|pf_village, no_menu, pt_none, fac_neutral, aggressiveness_0, ai_bhvr_hold, 0, (-213.615, 42.7065), [], 40.0),

	("village_135", "Wreckstone", icon_village_c|pf_village, no_menu, pt_none, fac_neutral, aggressiveness_0, ai_bhvr_hold, 0, (-108.566, 219.161), [], 40.0),

	("village_136", "Chyttering", icon_village_c|pf_village, no_menu, pt_none, fac_neutral, aggressiveness_0, ai_bhvr_hold, 0, (33.6163, 13.3571), [], 40.0),

	("village_137", "Darkwash", icon_village_c|pf_village, no_menu, pt_none, fac_neutral, aggressiveness_0, ai_bhvr_hold, 0, (-206.245, 56.2851), [], 40.0),

	("village_138", "Redstone", icon_village_c|pf_village, no_menu, pt_none, fac_neutral, aggressiveness_0, ai_bhvr_hold, 0, (-52.268, 145.529), [], 40.0),

	("village_139", "Ironstone", icon_village_c|pf_village, no_menu, pt_none, fac_neutral, aggressiveness_0, ai_bhvr_hold, 0, (-114.605, 143.448), [], 40.0),

	("village_140", "Bay of Myrth", icon_village_c|pf_village, no_menu, pt_none, fac_neutral, aggressiveness_0, ai_bhvr_hold, 0, (-107.58, 125.604), [], 40.0),

	("village_141", "Holyhall", icon_village_c|pf_village, no_menu, pt_none, fac_neutral, aggressiveness_0, ai_bhvr_hold, 0, (66.8684, 114.171), [], 40.0),

	("village_142", "Quarry Hill", icon_village_c|pf_village, no_menu, pt_none, fac_neutral, aggressiveness_0, ai_bhvr_hold, 0, (159.074, 216.733), [], 40.0),

	("village_143", "Linden", icon_village_c|pf_village, no_menu, pt_none, fac_neutral, aggressiveness_0, ai_bhvr_hold, 0, (-86.5195, -42.8076), [], 40.0),

	("village_144", "Uthmoor", icon_village_c|pf_village, no_menu, pt_none, fac_neutral, aggressiveness_0, ai_bhvr_hold, 0, (-92.3736, -92.7444), [], 40.0),

	("village_145", "Erimere", icon_village_c|pf_village, no_menu, pt_none, fac_neutral, aggressiveness_0, ai_bhvr_hold, 0, (-84.9846, -73.0327), [], 40.0),

	("village_146", "Valburn Hill", icon_village_c|pf_village, no_menu, pt_none, fac_neutral, aggressiveness_0, ai_bhvr_hold, 0, (-108.143, -35.4811), [], 40.0),

	("village_147", "Janash", icon_village_c|pf_village, no_menu, pt_none, fac_neutral, aggressiveness_0, ai_bhvr_hold, 0, (-112.16, 191.27), [], 40.0),

	("village_148", "Erifort", icon_village_c|pf_village, no_menu, pt_none, fac_neutral, aggressiveness_0, ai_bhvr_hold, 0, (-125.842, 71.3202), [], 40.0),

	("village_149", "Sunrise Way", icon_village_c|pf_village, no_menu, pt_none, fac_neutral, aggressiveness_0, ai_bhvr_hold, 0, (-94.2097, 60.6586), [], 40.0),

	("village_150", "Prybrook", icon_village_c|pf_village, no_menu, pt_none, fac_neutral, aggressiveness_0, ai_bhvr_hold, 0, (-63.0111, 162.415), [], 40.0),

	("village_151", "Raylyn", icon_village_c|pf_village, no_menu, pt_none, fac_neutral, aggressiveness_0, ai_bhvr_hold, 0, (-161.53, -78.3669), [], 40.0),

	("village_152", "Vale of Narrah", icon_village_c|pf_village, no_menu, pt_none, fac_neutral, aggressiveness_0, ai_bhvr_hold, 0, (-175.825, 18.7724), [], 40.0),

	("village_153", "Velvet Haven", icon_village_c|pf_village, no_menu, pt_none, fac_neutral, aggressiveness_0, ai_bhvr_hold, 0, (-148.132, 50.8598), [], 40.0),

	("village_154", "Lorness", icon_village_c|pf_village, no_menu, pt_none, fac_neutral, aggressiveness_0, ai_bhvr_hold, 0, (-106.567, 36.9769), [], 40.0),

	("village_155", "Baelors Feet", icon_village_c|pf_village, no_menu, pt_none, fac_neutral, aggressiveness_0, ai_bhvr_hold, 0, (122.209, 196.829), [], 40.0),

	("village_156", "The Mazemakers Tomb", icon_village_c|pf_village, no_menu, pt_none, fac_neutral, aggressiveness_0, ai_bhvr_hold, 0, (-168.705, -89.8841), [], 40.0),

	("village_157", "Estermont", icon_village_c|pf_village, no_menu, pt_none, fac_neutral, aggressiveness_0, ai_bhvr_hold, 0, (-15.1032, 148.825), [], 40.0),

	("village_158", "Whitemist", icon_village_c|pf_village, no_menu, pt_none, fac_neutral, aggressiveness_0, ai_bhvr_hold, 0, (-169.136, -50.9991), [], 40.0),

	("village_159", "Amberly", icon_village_a|pf_village, no_menu, pt_none, fac_neutral, aggressiveness_0, ai_bhvr_hold, 0, (-17.3739, 124.696), [], 35.0),

	("village_160", "The Whispers", icon_village_a|pf_village, no_menu, pt_none, fac_neutral, aggressiveness_0, ai_bhvr_hold, 0, (-6.32768, -1.63417), [], 35.0),

	("village_161", "Brandybottom", icon_village_a|pf_village, no_menu, pt_none, fac_neutral, aggressiveness_0, ai_bhvr_hold, 0, (121.781, 101.356), [], 35.0),

	("village_162", "Sherrer", icon_village_a|pf_village, no_menu, pt_none, fac_neutral, aggressiveness_0, ai_bhvr_hold, 0, (129.996, -44.2335), [], 35.0),

	("village_163", "Hull", icon_village_a|pf_village, no_menu, pt_none, fac_neutral, aggressiveness_0, ai_bhvr_hold, 0, (6.79138, 17.4654), [], 35.0),

	("village_164", "Sludgy Pond", icon_village_a|pf_village, no_menu, pt_none, fac_neutral, aggressiveness_0, ai_bhvr_hold, 0, (123.075, -21.7963), [], 35.0),

	("village_165", "The Lovely Crag", icon_village_c|pf_village, no_menu, pt_none, fac_neutral, aggressiveness_0, ai_bhvr_hold, 0, (-83.9468, 227.933), [], 40.0),

	("village_166", "Marshdown", icon_village_c|pf_village, no_menu, pt_none, fac_neutral, aggressiveness_0, ai_bhvr_hold, 0, (-119.917, 178.869), [], 40.0),

	("village_167", "Eastholt", icon_village_c|pf_village, no_menu, pt_none, fac_neutral, aggressiveness_0, ai_bhvr_hold, 0, (-64.5564, 192.288), [], 40.0),

	("village_168", "Honeyfinger", icon_village_c|pf_village, no_menu, pt_none, fac_neutral, aggressiveness_0, ai_bhvr_hold, 0, (-77.6191, 151.621), [], 40.0),

	("village_169", "Dune Port", icon_village_c|pf_village, no_menu, pt_none, fac_neutral, aggressiveness_0, ai_bhvr_hold, 0, (70.7003, 159.489), [], 40.0),

	("village_170", "Sweetsister", icon_village_c|pf_village, no_menu, pt_none, fac_neutral, aggressiveness_0, ai_bhvr_hold, 0, (63.8325, -127.511), [], 40.0),

	("village_171", "Utheros' Maze", icon_village_c|pf_village, no_menu, pt_none, fac_neutral, aggressiveness_0, ai_bhvr_hold, 0, (-121.294, -53.5709), [], 40.0),

	("village_172", "Grape Lake", icon_village_c|pf_village, no_menu, pt_none, fac_neutral, aggressiveness_0, ai_bhvr_hold, 0, (-117.982, 81.2559), [], 40.0),

	("village_173", "The Shivering Sea", icon_village_c|pf_village, no_menu, pt_none, fac_neutral, aggressiveness_0, ai_bhvr_hold, 0, (-180.368, -64.086), [], 40.0),

	("village_174", "The Velvet Hills", icon_village_c|pf_village, no_menu, pt_none, fac_neutral, aggressiveness_0, ai_bhvr_hold, 0, (-122.993, 31.3538), [], 40.0),

	("village_175", "Aldwell", icon_village_c|pf_village, no_menu, pt_none, fac_neutral, aggressiveness_0, ai_bhvr_hold, 0, (-167.675, -16.478), [], 40.0),

	("village_176", "Lostmoor", icon_village_c|pf_village, no_menu, pt_none, fac_neutral, aggressiveness_0, ai_bhvr_hold, 0, (-174.239, 56.7342), [], 40.0),

	("village_177", "The Orange Shore", icon_village_c|pf_village, no_menu, pt_none, fac_neutral, aggressiveness_0, ai_bhvr_hold, 0, (-188.955, 216.657), [], 40.0),

	("village_178", "Cedarwood", icon_village_c|pf_village, no_menu, pt_none, fac_neutral, aggressiveness_0, ai_bhvr_hold, 0, (-179.449, 165.004), [], 40.0),

	("village_179", "Rose's Hollow", icon_village_c|pf_village, no_menu, pt_none, fac_neutral, aggressiveness_0, ai_bhvr_hold, 0, (-190.536, 172.685), [], 40.0),

	("village_180", "Ruins of Sarhoy", icon_village_c|pf_village, no_menu, pt_none, fac_neutral, aggressiveness_0, ai_bhvr_hold, 0, (-201.864, 228.246), [], 40.0),

	("village_181", "Dunstonbury", icon_village_c|pf_village, no_menu, pt_none, fac_neutral, aggressiveness_0, ai_bhvr_hold, 0, (100.925, 116.745), [], 40.0),

	("village_182", "Pinchfire", icon_village_c|pf_village, no_menu, pt_none, fac_neutral, aggressiveness_0, ai_bhvr_hold, 0, (-192.532, 180.442), [], 40.0),

	("village_183", "Shadowton", icon_village_c|pf_village, no_menu, pt_none, fac_neutral, aggressiveness_0, ai_bhvr_hold, 0, (-6.87321, 215.891), [], 40.0),

	("village_184", "Marbleray", icon_village_c|pf_village, no_menu, pt_none, fac_neutral, aggressiveness_0, ai_bhvr_hold, 0, (-191.218, 205.043), [], 10.0),

	("village_185", "Nyel's Mountain", icon_village_c|pf_village, no_menu, pt_none, fac_neutral, aggressiveness_0, ai_bhvr_hold, 0, (-191.26, 42.5458), [], 40.0),

	("village_186", "Hills of Noom", icon_village_c|pf_village, no_menu, pt_none, fac_neutral, aggressiveness_0, ai_bhvr_hold, 0, (-158.519, 10.4711), [], 40.0),

	("village_187", "Wildelight", icon_village_c|pf_village, no_menu, pt_none, fac_neutral, aggressiveness_0, ai_bhvr_hold, 0, (-148.479, -9.06888), [], 40.0),

	("village_188", "Gallows Rock", icon_village_c|pf_village, no_menu, pt_none, fac_neutral, aggressiveness_0, ai_bhvr_hold, 0, (-77.4468, 163.007), [], 40.0),

	("village_189", "Turtle Hill", icon_village_c|pf_village, no_menu, pt_none, fac_neutral, aggressiveness_0, ai_bhvr_hold, 0, (-186.412, 189.071), [], 40.0),

	("village_190", "Waydale", icon_village_c|pf_village, no_menu, pt_none, fac_neutral, aggressiveness_0, ai_bhvr_hold, 0, (-198.933, 189.423), [], 40.0),

	("village_191", "Mallowmere", icon_village_a|pf_village, no_menu, pt_none, fac_neutral, aggressiveness_0, ai_bhvr_hold, 0, (-125.071, 165.379), [], 40.0),

	("village_192", "Rayhaven", icon_village_a|pf_village, no_menu, pt_none, fac_neutral, aggressiveness_0, ai_bhvr_hold, 0, (-125.713, 160.915), [], 40.0),

	("village_193", "Cod Town", icon_village_a|pf_village, no_menu, pt_none, fac_neutral, aggressiveness_0, ai_bhvr_hold, 0, (70.6607, -120.855), [], 40.0),

	("village_194", "Timberton", icon_village_a|pf_village, no_menu, pt_none, fac_neutral, aggressiveness_0, ai_bhvr_hold, 0, (192.07, 30.8788), [], 40.0),

	("village_195", "Plowman's Hill", icon_village_a|pf_village, no_menu, pt_none, fac_neutral, aggressiveness_0, ai_bhvr_hold, 0, (57.5282, 5.6811), [], 40.0),

	("village_196", "Pennytree", icon_village_a|pf_village, no_menu, pt_none, fac_neutral, aggressiveness_0, ai_bhvr_hold, 0, (100.903, 6.48126), [], 40.0),

	("village_197", "Greenberry", icon_village_a|pf_village, no_menu, pt_none, fac_neutral, aggressiveness_0, ai_bhvr_hold, 0, (87.2238, 127.354), [], 40.0),

	("village_198", "Crackclaw Point", icon_village_a|pf_village, no_menu, pt_none, fac_neutral, aggressiveness_0, ai_bhvr_hold, 0, (-8.09805, -8.68987), [], 40.0),

	("village_199", "Mallowcliff", icon_village_a|pf_village, no_menu, pt_none, fac_neutral, aggressiveness_0, ai_bhvr_hold, 0, (194.652, -36.5709), [], 40.0),

	("village_200", "Crow Spike Keep", icon_village_a|pf_village, no_menu, pt_none, fac_neutral, aggressiveness_0, ai_bhvr_hold, 0, (202.221, -46.7379), [], 40.0),

	("village_201", "Fieldstone", icon_village_a|pf_village, no_menu, pt_none, fac_neutral, aggressiveness_0, ai_bhvr_hold, 0, (53.6964, -19.7648), [], 40.0),

	("village_202", "Lambswold", icon_village_a|pf_village, no_menu, pt_none, fac_neutral, aggressiveness_0, ai_bhvr_hold, 0, (110.425, -30.6718), [], 40.0),

	("village_203", "Fogfield", icon_village_a|pf_village, no_menu, pt_none, fac_neutral, aggressiveness_0, ai_bhvr_hold, 0, (39.7657, 1.2082), [], 40.0),

	("village_204", "Swinebank", icon_village_a|pf_village, no_menu, pt_none, fac_neutral, aggressiveness_0, ai_bhvr_hold, 0, (60.8258, -126.001), [], 40.0),

	("village_205", "Coldriver", icon_village_a|pf_village, no_menu, pt_none, fac_neutral, aggressiveness_0, ai_bhvr_hold, 0, (118.746, 53.9107), [], 40.0),

	("village_206", "Tinhurst", icon_village_a|pf_village, no_menu, pt_none, fac_neutral, aggressiveness_0, ai_bhvr_hold, 0, (168.385, 33.479), [], 40.0),

	("village_207", "Corcrest", icon_village_a|pf_village, no_menu, pt_none, fac_neutral, aggressiveness_0, ai_bhvr_hold, 0, (194.445, 42.1083), [], 40.0),

	("village_208", "Lorassyon", icon_village_a|pf_village, no_menu, pt_none, fac_neutral, aggressiveness_0, ai_bhvr_hold, 0, (-182.786, -83.7525), [], 40.0),

	("village_209", "Glassmont", icon_village_a|pf_village, no_menu, pt_none, fac_neutral, aggressiveness_0, ai_bhvr_hold, 0, (-143.29, 157.304), [], 40.0),

	("village_210", "Baywind", icon_village_a|pf_village, no_menu, pt_none, fac_neutral, aggressiveness_0, ai_bhvr_hold, 0, (-128.608, 206.259), [], 40.0),

	("village_211", "Aelhaven", icon_village_a|pf_village, no_menu, pt_none, fac_neutral, aggressiveness_0, ai_bhvr_hold, 0, (-192.728, 71.4076), [], 40.0),

	("village_212", "Shadowwick", icon_village_a|pf_village, no_menu, pt_none, fac_neutral, aggressiveness_0, ai_bhvr_hold, 0, (-187.451, 83.1578), [], 40.0),

	("salt_mine", "Salt Mine", icon_village_a|pf_disabled|pf_village, no_menu, pt_none, fac_neutral, aggressiveness_0, ai_bhvr_hold, 0, (2.55759, 50.0091), []),

	("four_ways_inn", "Four Ways Inn", icon_village_a|pf_disabled|pf_village, no_menu, pt_none, fac_neutral, aggressiveness_0, ai_bhvr_hold, 0, (2.55759, 50.0091), []),

	("test_scene", "test scene", icon_village_a|pf_disabled|pf_village, no_menu, pt_none, fac_neutral, aggressiveness_0, ai_bhvr_hold, 0, (2.55759, 50.0091), []),

	("battlefields", "battlefields", icon_village_a|pf_disabled|pf_village, no_menu, pt_none, fac_neutral, aggressiveness_0, ai_bhvr_hold, 0, (2.55759, 50.0091), []),

	("dhorak_keep", "Dhorak Keep", icon_town_mercenary_dhorak|pf_disabled|pf_no_label|pf_village, no_menu, pt_none, fac_neutral, aggressiveness_0, ai_bhvr_hold, 0, (2.55759, 50.0091), []),

	("training_ground", "Training Ground", icon_training_ground_a|pf_disabled|pf_village, no_menu, pt_none, fac_neutral, aggressiveness_0, ai_bhvr_hold, 0, (3.0, -7.0), []),

	("training_ground_1", "Tourney Field", icon_training_ground_a|pf_disabled|pf_label_medium|pf_village, no_menu, pt_none, fac_neutral, aggressiveness_0, ai_bhvr_hold, 0, (42.8147, 102.313), [], 100.0),

	("training_ground_2", "Tourney Field", icon_training_ground_a|pf_disabled|pf_label_medium|pf_village, no_menu, pt_none, fac_neutral, aggressiveness_0, ai_bhvr_hold, 0, (64.059, 39.8267), [], 100.0),

	("training_ground_3", "Tourney Field", icon_training_ground_a|pf_disabled|pf_label_medium|pf_village, no_menu, pt_none, fac_neutral, aggressiveness_0, ai_bhvr_hold, 0, (200.013, 56.315), [], 100.0),

	("training_ground_4", "Tourney Field", icon_training_ground_b|pf_disabled|pf_label_medium|pf_village, no_menu, pt_none, fac_neutral, aggressiveness_0, ai_bhvr_hold, 0, (81.1018, 97.7642), [], 100.0),

	("training_ground_5", "Tourney Field", icon_training_ground_a|pf_disabled|pf_label_medium|pf_village, no_menu, pt_none, fac_neutral, aggressiveness_0, ai_bhvr_hold, 0, (188.75, 197.267), [], 100.0),

	("bridge_1", "{!}1", icon_bridge_a|pf_is_static|pf_always_visible|pf_no_label, no_menu, pt_none, fac_neutral, aggressiveness_0, ai_bhvr_hold, 0, (4.78743, 216.751), [], -4.07),

	("bridge_2", "{!}2", icon_bridge_a|pf_is_static|pf_always_visible|pf_no_label, no_menu, pt_none, fac_neutral, aggressiveness_0, ai_bhvr_hold, 0, (90.9179, 224.594), [], -64.07),

	("bridge_3", "{!}3", icon_bridge_a|pf_is_static|pf_always_visible|pf_no_label, no_menu, pt_none, fac_neutral, aggressiveness_0, ai_bhvr_hold, 0, (143.699, 138.847), [], -131.07),

	("bridge_4", "{!}4", icon_bridge_a|pf_is_static|pf_always_visible|pf_no_label, no_menu, pt_none, fac_neutral, aggressiveness_0, ai_bhvr_hold, 0, (122.091, 130.601), [], -144.07),

	("bridge_5", "{!}5", icon_bridge_a|pf_is_static|pf_always_visible|pf_no_label, no_menu, pt_none, fac_neutral, aggressiveness_0, ai_bhvr_hold, 0, (96.188, 107.727), [], -84.07),

	("bridge_6", "{!}6", icon_bridge_a|pf_is_static|pf_always_visible|pf_no_label, no_menu, pt_none, fac_neutral, aggressiveness_0, ai_bhvr_hold, 0, (79.2755, 47.4932), [], 3.5),

	("bridge_7", "{!}7", icon_bridge_a|pf_is_static|pf_always_visible|pf_no_label, no_menu, pt_none, fac_neutral, aggressiveness_0, ai_bhvr_hold, 0, (68.8344, -18.5061), [], -30.0),

	("bridge_8", "{!}8", icon_bridge_a|pf_is_static|pf_always_visible|pf_no_label, no_menu, pt_none, fac_neutral, aggressiveness_0, ai_bhvr_hold, 0, (113.157, -21.8358), [], 40.72),

	("bridge_9", "{!}9", icon_bridge_a|pf_is_static|pf_always_visible|pf_no_label, no_menu, pt_none, fac_neutral, aggressiveness_0, ai_bhvr_hold, 0, (114.889, -26.4567), [], -3.76),

	("bridge_10", "{!}10", icon_bridge_a|pf_is_static|pf_always_visible|pf_no_label, no_menu, pt_none, fac_neutral, aggressiveness_0, ai_bhvr_hold, 0, (78.1948, -171.549), [], -82.07),

	("bridge_11", "{!}11", icon_bridge_a|pf_is_static|pf_always_visible|pf_no_label, no_menu, pt_none, fac_neutral, aggressiveness_0, ai_bhvr_hold, 0, (102.092, -209.596), [], 161.3),

	("bridge_12", "{!}12", icon_bridge_a|pf_is_static|pf_always_visible|pf_no_label, no_menu, pt_none, fac_neutral, aggressiveness_0, ai_bhvr_hold, 0, (34.6373, -185.407), [], -43.5),

	("bridge_14", "{!}14", icon_bridge_a|pf_is_static|pf_always_visible|pf_no_label, no_menu, pt_none, fac_neutral, aggressiveness_0, ai_bhvr_hold, 0, (102.715, -46.5911), [], -17.7),

	("bridge_15", "{!}15", icon_bridge_a|pf_is_static|pf_always_visible|pf_no_label, no_menu, pt_none, fac_neutral, aggressiveness_0, ai_bhvr_hold, 0, (26.1461, -258.248), [], -74.07),

	("bridge_16", "{!}16", icon_bridge_a|pf_is_static|pf_always_visible|pf_no_label, no_menu, pt_none, fac_neutral, aggressiveness_0, ai_bhvr_hold, 0, (73.3003, 36.2958), [], -64.07),

	("bridge_17", "{!}17", icon_bridge_a|pf_is_static|pf_always_visible|pf_no_label, no_menu, pt_none, fac_neutral, aggressiveness_0, ai_bhvr_hold, 0, (-109.678, -8.4155), [], -64.07),

	("bridge_18", "{!}18", icon_bridge_a|pf_is_static|pf_always_visible|pf_no_label, no_menu, pt_none, fac_neutral, aggressiveness_0, ai_bhvr_hold, 0, (-167.643, 2.90297), [], -64.07),

	("bridge_19", "{!}19", icon_bridge_a|pf_is_static|pf_always_visible|pf_no_label, no_menu, pt_none, fac_neutral, aggressiveness_0, ai_bhvr_hold, 0, (-210.075, 59.6138), [], -64.07),

	("bridge_20", "{!}20", icon_bridge_a|pf_is_static|pf_always_visible|pf_no_label, no_menu, pt_none, fac_neutral, aggressiveness_0, ai_bhvr_hold, 0, (-203.337, 222.705), [], -94.07),

	("bridge_21", "{!}21", icon_bridge_a|pf_is_static|pf_always_visible|pf_no_label, no_menu, pt_none, fac_neutral, aggressiveness_0, ai_bhvr_hold, 0, (-117.586, 158.034), [], -44.07),

	("bridge_22", "{!}22", icon_bridge_a|pf_is_static|pf_always_visible|pf_no_label, no_menu, pt_none, fac_neutral, aggressiveness_0, ai_bhvr_hold, 0, (-200.724, 200.976), [], -84.07),

	("bridge_23", "{!}23", icon_bridge_a|pf_is_static|pf_always_visible|pf_no_label, no_menu, pt_none, fac_neutral, aggressiveness_0, ai_bhvr_hold, 0, (-146.403, 52.937), [], -65.07),

	("bridge_24", "{!}24", icon_bridge_a|pf_is_static|pf_always_visible|pf_no_label, no_menu, pt_none, fac_neutral, aggressiveness_0, ai_bhvr_hold, 0, (-162.879, 33.1884), [], -79.07),

	("volcano_rocks_1", "volcano rocks dragonstone", icon_volcano_rocks|pf_is_static|pf_always_visible|pf_no_label, no_menu, pt_none, fac_neutral, aggressiveness_0, ai_bhvr_hold, 0, (-6.86333, 11.4186), [], -79.07),

	("volcano_rocks_2", "volcano rocks valyria 1", icon_volcano_rocks|pf_is_static|pf_always_visible|pf_no_label, no_menu, pt_none, fac_neutral, aggressiveness_0, ai_bhvr_hold, 0, (-252.835, 302.739), [], -79.07),

	("volcano_rocks_3", "volcano rocks valyria 2", icon_volcano_rocks|pf_is_static|pf_always_visible|pf_no_label, no_menu, pt_none, fac_neutral, aggressiveness_0, ai_bhvr_hold, 0, (-255.045, 315.196), [], -79.07),

	("volcano_rocks_4", "volcano rocks valyria 3", icon_volcano_rocks|pf_is_static|pf_always_visible|pf_no_label, no_menu, pt_none, fac_neutral, aggressiveness_0, ai_bhvr_hold, 0, (-255.67, 343.635), [], -79.07),

	("volcano_rocks_5", "volcano rocks valyria 4", icon_volcano_rocks|pf_is_static|pf_always_visible|pf_no_label, no_menu, pt_none, fac_neutral, aggressiveness_0, ai_bhvr_hold, 0, (-244.481, 328.737), [], -79.07),

	("volcano_rocks_6", "volcano rocks valyria 5", icon_volcano_rocks|pf_is_static|pf_always_visible|pf_no_label, no_menu, pt_none, fac_neutral, aggressiveness_0, ai_bhvr_hold, 0, (-255.636, 356.107), [], -79.07),

	("port_1", "Port of King's Landing", icon_map_lighthouse|pf_village, no_menu, pt_none, fac_neutral, aggressiveness_0, ai_bhvr_hold, 0, (54.1617, 53.558), [], -64.07),

	("port_2", "Port of Duskendale", icon_map_lighthouse|pf_village, no_menu, pt_none, fac_neutral, aggressiveness_0, ai_bhvr_hold, 0, (34.0606, 27.1802), [], -64.07),

	("port_3", "Natural Harbor", icon_map_lighthouse|pf_village, no_menu, pt_none, fac_neutral, aggressiveness_0, ai_bhvr_hold, 0, (14.3555, 7.29215), [], -64.07),

	("port_4", "Natural Harbor", icon_map_lighthouse|pf_village, no_menu, pt_none, fac_neutral, aggressiveness_0, ai_bhvr_hold, 0, (-5.96776, -0.252385), [], -64.07),

	("port_5", "Natural Harbor", icon_map_lighthouse|pf_village, no_menu, pt_none, fac_neutral, aggressiveness_0, ai_bhvr_hold, 0, (-17.6105, -6.26487), [], -64.07),

	("port_6", "Natural Harbor", icon_map_lighthouse|pf_village, no_menu, pt_none, fac_neutral, aggressiveness_0, ai_bhvr_hold, 0, (-2.76598, 11.2303), [], -64.07),

	("port_7", "Port of Driftmark", icon_map_lighthouse|pf_village, no_menu, pt_none, fac_neutral, aggressiveness_0, ai_bhvr_hold, 0, (-0.03491, 14.5784), [], -64.07),

	("port_8", "Natural Harbor", icon_map_lighthouse|pf_village, no_menu, pt_none, fac_neutral, aggressiveness_0, ai_bhvr_hold, 0, (-1.10432, 29.8257), [], -64.07),

	("port_9", "Natural Harbor", icon_map_lighthouse|pf_village, no_menu, pt_none, fac_neutral, aggressiveness_0, ai_bhvr_hold, 0, (-10.3739, 88.3999), [], -64.07),

	("port_10", "Natural Harbor", icon_map_lighthouse|pf_village, no_menu, pt_none, fac_neutral, aggressiveness_0, ai_bhvr_hold, 0, (23.1399, 120.712), [], -64.07),

	("port_11", "Natural Harbor", icon_map_lighthouse|pf_village, no_menu, pt_none, fac_neutral, aggressiveness_0, ai_bhvr_hold, 0, (-10.6909, 154.299), [], -64.07),

	("port_12", "Natural Harbor", icon_map_lighthouse|pf_village, no_menu, pt_none, fac_neutral, aggressiveness_0, ai_bhvr_hold, 0, (-40.666, 160.624), [], -64.07),

	("port_13", "Natural Harbor", icon_map_lighthouse|pf_village, no_menu, pt_none, fac_neutral, aggressiveness_0, ai_bhvr_hold, 0, (-52.8906, 156.746), [], -64.07),

	("port_14", "Natural Harbor", icon_map_lighthouse|pf_village, no_menu, pt_none, fac_neutral, aggressiveness_0, ai_bhvr_hold, 0, (-54.2383, 145.842), [], -64.07),

	("port_15", "Port of Tyrosh", icon_map_lighthouse|pf_village, no_menu, pt_none, fac_neutral, aggressiveness_0, ai_bhvr_hold, 0, (-65.1738, 143.793), [], -64.07),

	("port_16", "Natural Harbor", icon_map_lighthouse|pf_village, no_menu, pt_none, fac_neutral, aggressiveness_0, ai_bhvr_hold, 0, (-61.6305, 197.065), [], -64.07),

	("port_17", "Natural Harbor", icon_map_lighthouse|pf_village, no_menu, pt_none, fac_neutral, aggressiveness_0, ai_bhvr_hold, 0, (-85.1438, 227.617), [], -64.07),

	("port_18", "Port of Lys", icon_map_lighthouse|pf_village, no_menu, pt_none, fac_neutral, aggressiveness_0, ai_bhvr_hold, 0, (-84.0746, 245.687), [], -64.07),

	("port_19", "Natural Harbor", icon_map_lighthouse|pf_village, no_menu, pt_none, fac_neutral, aggressiveness_0, ai_bhvr_hold, 0, (-107.282, 219.382), [], -64.07),

	("port_20", "Natural Harbor", icon_map_lighthouse|pf_village, no_menu, pt_none, fac_neutral, aggressiveness_0, ai_bhvr_hold, 0, (-176.482, 240.833), [], -64.07),

	("port_21", "Port of Braavos", icon_map_lighthouse|pf_village, no_menu, pt_none, fac_neutral, aggressiveness_0, ai_bhvr_hold, 0, (-83.1399, -95.6649), [], -64.07),

	("port_22", "Port of Lorath", icon_map_lighthouse|pf_village, no_menu, pt_none, fac_neutral, aggressiveness_0, ai_bhvr_hold, 0, (-168.279, -83.021), [], -64.07),

	("port_23", "Port of Myr", icon_map_lighthouse|pf_village, no_menu, pt_none, fac_neutral, aggressiveness_0, ai_bhvr_hold, 0, (-110.061, 151.746), [], -64.07),

	("port_24", "Natural Harbor", icon_map_lighthouse|pf_village, no_menu, pt_none, fac_neutral, aggressiveness_0, ai_bhvr_hold, 0, (52.1625, -128.452), [], -64.07),

	("port_25", "Port of Sisterton", icon_map_lighthouse|pf_village, no_menu, pt_none, fac_neutral, aggressiveness_0, ai_bhvr_hold, 0, (64.5055, -125.726), [], -64.07),

	("port_26", "Natural Harbor", icon_map_lighthouse|pf_village, no_menu, pt_none, fac_neutral, aggressiveness_0, ai_bhvr_hold, 0, (69.6479, -124.024), [], -64.07),

	("port_27", "Natural Harbor", icon_map_lighthouse|pf_village, no_menu, pt_none, fac_neutral, aggressiveness_0, ai_bhvr_hold, 0, (156.499, -300.272), [], -64.07),

	("port_28", "Natural Harbor", icon_map_lighthouse|pf_village, no_menu, pt_none, fac_neutral, aggressiveness_0, ai_bhvr_hold, 0, (191.474, -73.75), [], -64.07),

	("port_29", "Natural Harbor", icon_map_lighthouse|pf_village, no_menu, pt_none, fac_neutral, aggressiveness_0, ai_bhvr_hold, 0, (195.672, -61.1574), [], -64.07),

	("port_30", "Natural Harbor", icon_map_lighthouse|pf_village, no_menu, pt_none, fac_neutral, aggressiveness_0, ai_bhvr_hold, 0, (188.209, -47.8174), [], -64.07),

	("port_31", "Port of Lordsport", icon_map_lighthouse|pf_village, no_menu, pt_none, fac_neutral, aggressiveness_0, ai_bhvr_hold, 0, (193.849, -41.7138), [], -64.07),

	("port_32", "Natural Harbor", icon_map_lighthouse|pf_village, no_menu, pt_none, fac_neutral, aggressiveness_0, ai_bhvr_hold, 0, (211.157, -38.6113), [], -64.07),

	("port_33", "Natural Harbor", icon_map_lighthouse|pf_village, no_menu, pt_none, fac_neutral, aggressiveness_0, ai_bhvr_hold, 0, (203.815, -58.0245), [], -64.07),

	("port_34", "Natural Harbor", icon_map_lighthouse|pf_village, no_menu, pt_none, fac_neutral, aggressiveness_0, ai_bhvr_hold, 0, (197.646, -52.55), [], -64.07),

	("port_35", "Natural Harbor", icon_map_lighthouse|pf_village, no_menu, pt_none, fac_neutral, aggressiveness_0, ai_bhvr_hold, 0, (226.56, -60.868), [], -64.07),

	("port_36", "Natural Harbor", icon_map_lighthouse|pf_village, no_menu, pt_none, fac_neutral, aggressiveness_0, ai_bhvr_hold, 0, (201.121, 8.77153), [], -64.07),

	("port_37", "Natural Harbor", icon_map_lighthouse|pf_village, no_menu, pt_none, fac_neutral, aggressiveness_0, ai_bhvr_hold, 0, (195.622, 127.896), [], -64.07),

	("port_38", "Port of The Arbor", icon_map_lighthouse|pf_village, no_menu, pt_none, fac_neutral, aggressiveness_0, ai_bhvr_hold, 0, (206.15, 230.36), [], -64.07),

	("port_39", "Port of Gulltown", icon_map_lighthouse|pf_village, no_menu, pt_none, fac_neutral, aggressiveness_0, ai_bhvr_hold, 0, (-9.16205, -41.7424), [], -64.07),

	("port_40", "Natural Harbor", icon_map_lighthouse|pf_village, no_menu, pt_none, fac_neutral, aggressiveness_0, ai_bhvr_hold, 0, (-1.26453, -60.3114), [], -64.07),

	("port_41", "Natural Harbor", icon_map_lighthouse|pf_village, no_menu, pt_none, fac_neutral, aggressiveness_0, ai_bhvr_hold, 0, (5.26453, -115.393), [], -64.07),

	("port_42", "Natural Harbor", icon_map_lighthouse|pf_village, no_menu, pt_none, fac_neutral, aggressiveness_0, ai_bhvr_hold, 0, (30.861, -113.61), [], -64.07),

	("port_43", "Port of White Harbor", icon_map_lighthouse|pf_village, no_menu, pt_none, fac_neutral, aggressiveness_0, ai_bhvr_hold, 0, (76.525, -153.395), [], -64.07),

	("port_44", "Natural Harbor", icon_map_lighthouse|pf_village, no_menu, pt_none, fac_neutral, aggressiveness_0, ai_bhvr_hold, 0, (147.874, -275.601), [], -64.07),

	("port_45", "Natural Harbor", icon_map_lighthouse|pf_village, no_menu, pt_none, fac_neutral, aggressiveness_0, ai_bhvr_hold, 0, (207.152, -186.583), [], -64.07),

	("port_46", "Natural Harbor", icon_map_lighthouse|pf_village, no_menu, pt_none, fac_neutral, aggressiveness_0, ai_bhvr_hold, 0, (192.887, -125.876), [], -64.07),

	("port_47", "Natural Harbor", icon_map_lighthouse|pf_village, no_menu, pt_none, fac_neutral, aggressiveness_0, ai_bhvr_hold, 0, (128.195, -63.7206), [], -64.07),

	("port_48", "Port of Lannisport", icon_map_lighthouse|pf_village, no_menu, pt_none, fac_neutral, aggressiveness_0, ai_bhvr_hold, 0, (200.612, 37.9766), [], -64.07),

	("port_49", "Natural Harbor", icon_map_lighthouse|pf_village, no_menu, pt_none, fac_neutral, aggressiveness_0, ai_bhvr_hold, 0, (181.818, 141.463), [], -64.07),

	("port_50", "Port of Oldtown", icon_map_lighthouse|pf_village, no_menu, pt_none, fac_neutral, aggressiveness_0, ai_bhvr_hold, 0, (191.293, 187.758), [], -64.07),

	("port_51", "Port of Sunspear", icon_map_lighthouse|pf_village, no_menu, pt_none, fac_neutral, aggressiveness_0, ai_bhvr_hold, 0, (-14.4383, 213.686), [], -64.07),

	("port_52", "Port of Volantis", icon_map_lighthouse|pf_village, no_menu, pt_none, fac_neutral, aggressiveness_0, ai_bhvr_hold, 0, (-211.084, 223.009), [], -64.07),

	("port_53", "Natural Harbor", icon_map_lighthouse|pf_village, no_menu, pt_none, fac_neutral, aggressiveness_0, ai_bhvr_hold, 0, (-108.124, 199.697), [], -64.07),

	("port_54", "Natural Harbor", icon_map_lighthouse|pf_village, no_menu, pt_none, fac_neutral, aggressiveness_0, ai_bhvr_hold, 0, (-92.1405, 123.402), [], -64.07),

	("port_55", "Port of Pentos", icon_map_lighthouse|pf_village, no_menu, pt_none, fac_neutral, aggressiveness_0, ai_bhvr_hold, 0, (-81.6442, 61.9467), [], -64.07),

	("port_56", "Natural Harbor", icon_map_lighthouse|pf_village, no_menu, pt_none, fac_neutral, aggressiveness_0, ai_bhvr_hold, 0, (-82.4315, -90.3573), [], -64.07),

	("port_57", "Natural Harbor", icon_map_lighthouse|pf_village, no_menu, pt_none, fac_neutral, aggressiveness_0, ai_bhvr_hold, 0, (-179.297, -65.0603), [], -64.07),

	("port_58", "Natural Harbor", icon_map_lighthouse|pf_village, no_menu, pt_none, fac_neutral, aggressiveness_0, ai_bhvr_hold, 0, (-73.3531, 149.806), [], -64.07),

	("port_59", "Natural Harbor", icon_map_lighthouse|pf_village, no_menu, pt_none, fac_neutral, aggressiveness_0, ai_bhvr_hold, 0, (-105.23, 127.843), [], -64.07),

	("port_60", "Natural Harbor", icon_map_lighthouse|pf_village, no_menu, pt_none, fac_neutral, aggressiveness_0, ai_bhvr_hold, 0, (-182.807, -81.2239), [], -64.07),

	("port_61", "Natural Harbor", icon_map_lighthouse|pf_village, no_menu, pt_none, fac_neutral, aggressiveness_0, ai_bhvr_hold, 0, (189.743, 12.505), [], -64.07),

	("port_62", "Port of the Weeping Town", icon_map_lighthouse|pf_village, no_menu, pt_none, fac_neutral, aggressiveness_0, ai_bhvr_hold, 0, (9.88259, 160.744), [], -64.07),

	("port_63", "Natural Harbor", icon_map_lighthouse|pf_village, no_menu, pt_none, fac_neutral, aggressiveness_0, ai_bhvr_hold, 0, (22.0733, 54.3936), [], -64.07),

	("port_64", "Port of Saltpans", icon_map_lighthouse|pf_village, no_menu, pt_none, fac_neutral, aggressiveness_0, ai_bhvr_hold, 0, (51.0166, -11.3443), [], -64.07),

	("port_65", "Port of Maidenpool", icon_map_lighthouse|pf_village, no_menu, pt_none, fac_neutral, aggressiveness_0, ai_bhvr_hold, 0, (35.3519, -2.07221), [], -64.07),

	("port_66", "Port of Aquos Dhaen", icon_map_lighthouse|pf_village, no_menu, pt_none, fac_neutral, aggressiveness_0, ai_bhvr_hold, 0, (-134.245, 216.748), [], -64.07),

	("port_67", "Natural Harbor", icon_map_lighthouse|pf_village, no_menu, pt_none, fac_neutral, aggressiveness_0, ai_bhvr_hold, 0, (-55.1585, 174.238), [], -64.07),

	("battlemap_barrow_1", "Barrow", icon_map_barrow|pf_is_static|pf_hide_defenders, no_menu, pt_none, fac_neutral, aggressiveness_0, ai_bhvr_hold, 0, (142.16, -159.988), [], 125.0),

	("battlemap_barrow_2", "Barrow", icon_map_barrow|pf_is_static|pf_hide_defenders, no_menu, pt_none, fac_neutral, aggressiveness_0, ai_bhvr_hold, 0, (145.584, -178.033), [], 325.0),

	("battlemap_barrow_3", "Barrow", icon_map_barrow|pf_is_static|pf_hide_defenders, no_menu, pt_none, fac_neutral, aggressiveness_0, ai_bhvr_hold, 0, (115.697, -165.744), [], 155.0),

	("battlemap_barrow_4", "Barrow", icon_map_barrow|pf_is_static|pf_hide_defenders, no_menu, pt_none, fac_neutral, aggressiveness_0, ai_bhvr_hold, 0, (124.497, -198.615), [], 225.0),

	("battlemap_barrow_5", "Barrow", icon_map_barrow|pf_is_static|pf_hide_defenders, no_menu, pt_none, fac_neutral, aggressiveness_0, ai_bhvr_hold, 0, (173.015, -180.756), [], 55.0),

	("battlemap_weirwood_north_1", "Weirwood", icon_map_weirwood|pf_is_static|pf_hide_defenders, no_menu, pt_none, fac_neutral, aggressiveness_0, ai_bhvr_hold, 0, (97.79, -212.752), [], 55.0),

	("battlemap_weirwood_north_2", "Weirwood", icon_map_weirwood|pf_is_static|pf_hide_defenders, no_menu, pt_none, fac_neutral, aggressiveness_0, ai_bhvr_hold, 0, (122.94, -277.156), [], 111.0),

	("battlemap_weirwood_north_3", "Weirwood", icon_map_weirwood|pf_is_static|pf_hide_defenders, no_menu, pt_none, fac_neutral, aggressiveness_0, ai_bhvr_hold, 0, (79.743, -311.074), [], 222.0),

	("battlemap_weirwood_north_4", "Weirwood", icon_map_weirwood|pf_is_static|pf_hide_defenders, no_menu, pt_none, fac_neutral, aggressiveness_0, ai_bhvr_hold, 0, (53.7305, -251.001), [], 333.0),

	("battlemap_weirwood_north_5", "Weirwood", icon_map_weirwood|pf_is_static|pf_hide_defenders, no_menu, pt_none, fac_neutral, aggressiveness_0, ai_bhvr_hold, 0, (-7.34056, -274.796), [], 225.0),

	("battlemap_weirwood_north_6", "Weirwood", icon_map_weirwood|pf_is_static|pf_hide_defenders, no_menu, pt_none, fac_neutral, aggressiveness_0, ai_bhvr_hold, 0, (60.7016, -150.452), [], 125.0),

	("battlemap_westerlands_mine_1", "Silver Mine", icon_bandit_lair|pf_is_static|pf_hide_defenders, no_menu, pt_none, fac_neutral, aggressiveness_0, ai_bhvr_hold, 0, (182.699, 11.1696), [], 55.0),

	("battlemap_westerlands_mine_2", "Silver Mine", icon_bandit_lair|pf_is_static|pf_hide_defenders, no_menu, pt_none, fac_neutral, aggressiveness_0, ai_bhvr_hold, 0, (183.916, -1.93445), [], 115.0),

	("battlemap_westerlands_mine_3", "Gold Mine", icon_bandit_lair|pf_is_static|pf_hide_defenders, no_menu, pt_none, fac_neutral, aggressiveness_0, ai_bhvr_hold, 0, (163.084, -15.6201), [], 155.0),

	("battlemap_westerlands_mine_4", "Gold Mine", icon_bandit_lair|pf_is_static|pf_hide_defenders, no_menu, pt_none, fac_neutral, aggressiveness_0, ai_bhvr_hold, 0, (152.525, -29.7852), [], 225.0),

	("battlemap_westerlands_mine_5", "Gold Mine", icon_bandit_lair|pf_is_static|pf_hide_defenders, no_menu, pt_none, fac_neutral, aggressiveness_0, ai_bhvr_hold, 0, (169.55, 25.8952), [], 335.0),

	("battlemap_lumber_camp_north_1", "Lumber Camp", icon_map_Rodgars_Hut|pf_is_static|pf_hide_defenders, no_menu, pt_none, fac_neutral, aggressiveness_0, ai_bhvr_hold, 0, (69.7472, -224.389), [], 15.0),

	("battlemap_lumber_camp_north_2", "Lumber Camp", icon_map_Rodgars_Hut|pf_is_static|pf_hide_defenders, no_menu, pt_none, fac_neutral, aggressiveness_0, ai_bhvr_hold, 0, (160.066, -268.275), [], 55.0),

	("battlemap_lumber_camp_north_3", "Lumber Camp", icon_map_Rodgars_Hut|pf_is_static|pf_hide_defenders, no_menu, pt_none, fac_neutral, aggressiveness_0, ai_bhvr_hold, 0, (37.1858, -272.193), [], 125.0),

	("battlemap_lumber_camp_north_4", "Lumber Camp", icon_map_Rodgars_Hut|pf_is_static|pf_hide_defenders, no_menu, pt_none, fac_neutral, aggressiveness_0, ai_bhvr_hold, 0, (-7.72416, -274.586), [], 165.0),

	("battlemap_lumber_camp_north_5", "Lumber Camp", icon_map_Rodgars_Hut|pf_is_static|pf_hide_defenders, no_menu, pt_none, fac_neutral, aggressiveness_0, ai_bhvr_hold, 0, (120.715, -220.053), [], 225.0),

	("battlemap_farmland_reach_1", "Farmland", icon_map_farmland|pf_is_static|pf_hide_defenders, no_menu, pt_none, fac_neutral, aggressiveness_0, ai_bhvr_hold, 0, (111.937, 104.065), [], 15.0),

	("battlemap_farmland_reach_2", "Farmland", icon_map_farmland|pf_is_static|pf_hide_defenders, no_menu, pt_none, fac_neutral, aggressiveness_0, ai_bhvr_hold, 0, (160.604, 107.221), [], 55.0),

	("battlemap_farmland_reach_3", "Farmland", icon_map_farmland|pf_is_static|pf_hide_defenders, no_menu, pt_none, fac_neutral, aggressiveness_0, ai_bhvr_hold, 0, (99.4646, 86.2439), [], 115.0),

	("battlemap_farmland_reach_4", "Farmland", icon_map_farmland|pf_is_static|pf_hide_defenders, no_menu, pt_none, fac_neutral, aggressiveness_0, ai_bhvr_hold, 0, (128.105, 141.516), [], 155.0),

	("battlemap_farmland_reach_5", "Farmland", icon_map_farmland|pf_is_static|pf_hide_defenders, no_menu, pt_none, fac_neutral, aggressiveness_0, ai_bhvr_hold, 0, (81.7721, 82.1694), [], 225.0),

	("battlemap_farmland_reach_6", "Farmland", icon_map_farmland|pf_is_static|pf_hide_defenders, no_menu, pt_none, fac_neutral, aggressiveness_0, ai_bhvr_hold, 0, (62.4511, 74.6207), [], 275.0),

	("battlemap_farmland_reach_7", "Farmland", icon_map_farmland|pf_is_static|pf_hide_defenders, no_menu, pt_none, fac_neutral, aggressiveness_0, ai_bhvr_hold, 0, (186.865, 206.157), [], 315.0),

	("battlemap_farmland_reach_8", "Farmland", icon_map_farmland|pf_is_static|pf_hide_defenders, no_menu, pt_none, fac_neutral, aggressiveness_0, ai_bhvr_hold, 0, (193.226, 152.781), [], 345.0),

	("battlemap_orchard_essos_1", "Orchard", icon_map_farmland|pf_is_static|pf_hide_defenders, no_menu, pt_none, fac_neutral, aggressiveness_0, ai_bhvr_hold, 0, (-199.87, 216.876), [], 15.0),

	("battlemap_orchard_essos_2", "Orchard", icon_map_farmland|pf_is_static|pf_hide_defenders, no_menu, pt_none, fac_neutral, aggressiveness_0, ai_bhvr_hold, 0, (-186.265, 179.215), [], 55.0),

	("battlemap_orchard_essos_3", "Orchard", icon_map_farmland|pf_is_static|pf_hide_defenders, no_menu, pt_none, fac_neutral, aggressiveness_0, ai_bhvr_hold, 0, (-189.902, 209.916), [], 115.0),

	("battlemap_orchard_essos_4", "Orchard", icon_map_farmland|pf_is_static|pf_hide_defenders, no_menu, pt_none, fac_neutral, aggressiveness_0, ai_bhvr_hold, 0, (-194.378, 193.62), [], 155.0),

	("battlemap_orchard_essos_5", "Orchard", icon_map_farmland|pf_is_static|pf_hide_defenders, no_menu, pt_none, fac_neutral, aggressiveness_0, ai_bhvr_hold, 0, (-140.276, 210.764), [], 215.0),

	("battlemap_orchard_essos_6", "Orchard", icon_map_farmland|pf_is_static|pf_hide_defenders, no_menu, pt_none, fac_neutral, aggressiveness_0, ai_bhvr_hold, 0, (-126.827, 183.899), [], 265.0),

	("battlemap_orchard_essos_7", "Orchard", icon_map_farmland|pf_is_static|pf_hide_defenders, no_menu, pt_none, fac_neutral, aggressiveness_0, ai_bhvr_hold, 0, (-104.541, 165.368), [], 325.0),

	("battlemap_ruined_fort_1", "Ruined Fort", icon_map_Ruined_Castle|pf_is_static|pf_hide_defenders, no_menu, pt_none, fac_neutral, aggressiveness_0, ai_bhvr_hold, 0, (-76.7544, -20.5112), [], 15.0),

	("battlemap_ruined_fort_2", "Ruined Fort", icon_map_Ruined_Castle|pf_is_static|pf_hide_defenders, no_menu, pt_none, fac_neutral, aggressiveness_0, ai_bhvr_hold, 0, (-202.036, 23.9927), [], 55.0),

	("battlemap_ruined_fort_3", "Ruined Fort", icon_map_Ruined_Castle|pf_is_static|pf_hide_defenders, no_menu, pt_none, fac_neutral, aggressiveness_0, ai_bhvr_hold, 0, (-184.369, -47.124), [], 115.0),

	("battlemap_ruined_fort_4", "Ruined Fort", icon_map_Ruined_Castle|pf_is_static|pf_hide_defenders, no_menu, pt_none, fac_neutral, aggressiveness_0, ai_bhvr_hold, 0, (-127.682, 42.1217), [], 155.0),

	("battlemap_rhoynar_ruins_1", "Rhoynar Ruins", icon_map_the_sorrows|pf_is_static|pf_hide_defenders, no_menu, pt_none, fac_neutral, aggressiveness_0, ai_bhvr_hold, 0, (-172.299, 138.782), [], 15.0),

	("battlemap_rhoynar_ruins_2", "Rhoynar Ruins", icon_map_the_sorrows|pf_is_static|pf_hide_defenders, no_menu, pt_none, fac_neutral, aggressiveness_0, ai_bhvr_hold, 0, (-160.35, 112.238), [], 155.0),

	("battlemap_rhoynar_ruins_3", "Rhoynar Ruins", icon_map_the_sorrows|pf_is_static|pf_hide_defenders, no_menu, pt_none, fac_neutral, aggressiveness_0, ai_bhvr_hold, 0, (-189.434, 91.7438), [], 225.0),

	("battlemap_poleboat_1", "Greenblood Rafts", icon_ship_harbour|pf_is_static|pf_hide_defenders, no_menu, pt_none, fac_neutral, aggressiveness_0, ai_bhvr_hold, 0, (11.8118, 216.032), [], 255.0),

	("battlemap_poleboat_2", "Greenblood Rafts", icon_ship_harbour|pf_is_static|pf_hide_defenders, no_menu, pt_none, fac_neutral, aggressiveness_0, ai_bhvr_hold, 0, (24.4343, 209.808), [], 275.0),

	("battlemap_poleboat_3", "Greenblood Rafts", icon_ship_harbour|pf_is_static|pf_hide_defenders, no_menu, pt_none, fac_neutral, aggressiveness_0, ai_bhvr_hold, 0, (46.3701, 205.552), [], 285.0),

	("battlemap_old_mill_1", "Old Mill", icon_map_old_mill|pf_is_static|pf_hide_defenders, no_menu, pt_none, fac_neutral, aggressiveness_0, ai_bhvr_hold, 0, (82.6673, 33.0022), [], 15.0),

	("battlemap_old_mill_2", "Old Mill", icon_map_old_mill|pf_is_static|pf_hide_defenders, no_menu, pt_none, fac_neutral, aggressiveness_0, ai_bhvr_hold, 0, (113.565, -14.6876), [], 55.0),

	("battlemap_old_mill_3", "Old Mill", icon_map_old_mill|pf_is_static|pf_hide_defenders, no_menu, pt_none, fac_neutral, aggressiveness_0, ai_bhvr_hold, 0, (47.7317, -21.8137), [], 115.0),

	("battlemap_old_mill_4", "Old Mill", icon_map_old_mill|pf_is_static|pf_hide_defenders, no_menu, pt_none, fac_neutral, aggressiveness_0, ai_bhvr_hold, 0, (-117.945, -70.38), [], 155.0),

	("battlemap_old_mill_5", "Old Mill", icon_map_old_mill|pf_is_static|pf_hide_defenders, no_menu, pt_none, fac_neutral, aggressiveness_0, ai_bhvr_hold, 0, (0.715131, -47.0768), [], 195.0),

	("battlemap_old_mill_6", "Old Mill", icon_map_old_mill|pf_is_static|pf_hide_defenders, no_menu, pt_none, fac_neutral, aggressiveness_0, ai_bhvr_hold, 0, (9.57618, 153.643), [], 225.0),

	("battlemap_old_mill_7", "Old Mill", icon_map_old_mill|pf_is_static|pf_hide_defenders, no_menu, pt_none, fac_neutral, aggressiveness_0, ai_bhvr_hold, 0, (114.026, 148.773), [], 265.0),

	("battlemap_old_mill_8", "Old Mill", icon_map_old_mill|pf_is_static|pf_hide_defenders, no_menu, pt_none, fac_neutral, aggressiveness_0, ai_bhvr_hold, 0, (18.1309, 103.007), [], 295.0),

	("battlemap_old_mill_9", "Old Mill", icon_map_old_mill|pf_is_static|pf_hide_defenders, no_menu, pt_none, fac_neutral, aggressiveness_0, ai_bhvr_hold, 0, (111.663, 60.9796), [], 325.0),

	("battlemap_forest_bog_1", "Forest Bog", icon_map_forest_bog|pf_is_static|pf_hide_defenders, no_menu, pt_none, fac_neutral, aggressiveness_0, ai_bhvr_hold, 0, (148.826, -63.5325), [], 325.0),

	("battlemap_forest_bog_2", "Forest Bog", icon_map_forest_bog|pf_is_static|pf_hide_defenders, no_menu, pt_none, fac_neutral, aggressiveness_0, ai_bhvr_hold, 0, (100.938, -38.7199), [], 325.0),

	("battlemap_forest_bog_3", "Forest Bog", icon_map_forest_bog|pf_is_static|pf_hide_defenders, no_menu, pt_none, fac_neutral, aggressiveness_0, ai_bhvr_hold, 0, (41.3718, 17.8553), [], 325.0),

	("battlemap_forest_bog_4", "Forest Bog", icon_map_forest_bog|pf_is_static|pf_hide_defenders, no_menu, pt_none, fac_neutral, aggressiveness_0, ai_bhvr_hold, 0, (-2.24787, -11.347), [], 325.0),

	("battlemap_forest_bog_5", "Forest Bog", icon_map_forest_bog|pf_is_static|pf_hide_defenders, no_menu, pt_none, fac_neutral, aggressiveness_0, ai_bhvr_hold, 0, (157.982, 85.9916), [], 325.0),

	("battlemap_forest_bog_6", "Forest Bog", icon_map_forest_bog|pf_is_static|pf_hide_defenders, no_menu, pt_none, fac_neutral, aggressiveness_0, ai_bhvr_hold, 0, (-2.89747, 135.618), [], 325.0),

	("battlemap_forest_bog_7", "Forest Bog", icon_map_forest_bog|pf_is_static|pf_hide_defenders, no_menu, pt_none, fac_neutral, aggressiveness_0, ai_bhvr_hold, 0, (-84.6795, -34.67465), [], 325.0),

	("battlemap_forest_bog_8", "Forest Bog", icon_map_forest_bog|pf_is_static|pf_hide_defenders, no_menu, pt_none, fac_neutral, aggressiveness_0, ai_bhvr_hold, 0, (-113.336, -38.2168), [], 325.0),

	("battlemap_forest_bog_9", "Forest Bog", icon_map_forest_bog|pf_is_static|pf_hide_defenders, no_menu, pt_none, fac_neutral, aggressiveness_0, ai_bhvr_hold, 0, (-112.976, -48.6451), [], 325.0),

	("battlemap_forest_bog_10", "Forest Bog", icon_map_forest_bog|pf_is_static|pf_hide_defenders, no_menu, pt_none, fac_neutral, aggressiveness_0, ai_bhvr_hold, 0, (-151.481, -41.7481), [], 325.0),

	("battlemap_forest_bog_11", "Forest Bog", icon_map_forest_bog|pf_is_static|pf_hide_defenders, no_menu, pt_none, fac_neutral, aggressiveness_0, ai_bhvr_hold, 0, (-111.184, 5.10799), [], 325.0),

	("battlemap_forest_bog_12", "Forest Bog", icon_map_forest_bog|pf_is_static|pf_hide_defenders, no_menu, pt_none, fac_neutral, aggressiveness_0, ai_bhvr_hold, 0, (-140.905, 64.5688), [], 325.0),

	("battlemap_forest_bog_13", "Forest Bog", icon_map_forest_bog|pf_is_static|pf_hide_defenders, no_menu, pt_none, fac_neutral, aggressiveness_0, ai_bhvr_hold, 0, (-191.426, 77.5355), [], 325.0),

	("battlemap_forest_bog_14", "Forest Bog", icon_map_forest_bog|pf_is_static|pf_hide_defenders, no_menu, pt_none, fac_neutral, aggressiveness_0, ai_bhvr_hold, 0, (-121.537, 100.277), [], 325.0),

	("battlemap_abandoned_village_1", "Abandoned Village", icon_map_abandoned_village|pf_is_static|pf_hide_defenders, no_menu, pt_none, fac_neutral, aggressiveness_0, ai_bhvr_hold, 0, (108.056, 28.3039), [], 325.0),

	("battlemap_abandoned_village_2", "Abandoned Village", icon_map_abandoned_village|pf_is_static|pf_hide_defenders, no_menu, pt_none, fac_neutral, aggressiveness_0, ai_bhvr_hold, 0, (106.086, 9.88526), [], 325.0),

	("battlemap_abandoned_village_3", "Abandoned Village", icon_map_abandoned_village|pf_is_static|pf_hide_defenders, no_menu, pt_none, fac_neutral, aggressiveness_0, ai_bhvr_hold, 0, (93.1606, 5.15939), [], 325.0),

	("battlemap_abandoned_village_4", "Abandoned Village", icon_map_abandoned_village|pf_is_static|pf_hide_defenders, no_menu, pt_none, fac_neutral, aggressiveness_0, ai_bhvr_hold, 0, (65.0027, 3.11672), [], 325.0),

	("battlemap_abandoned_village_5", "Abandoned Village", icon_map_abandoned_village|pf_is_static|pf_hide_defenders, no_menu, pt_none, fac_neutral, aggressiveness_0, ai_bhvr_hold, 0, (67.951, 35.2163), [], 325.0),

	("battlemap_abandoned_village_6", "Abandoned Village", icon_map_abandoned_village|pf_is_static|pf_hide_defenders, no_menu, pt_none, fac_neutral, aggressiveness_0, ai_bhvr_hold, 0, (133.443, -13.6879), [], 325.0),

	("battlemap_dothraki_sea_1", "Abandoned Camp", icon_camp_tent|pf_is_static|pf_hide_defenders, no_menu, pt_none, fac_neutral, aggressiveness_0, ai_bhvr_hold, 0, (-201.877, 70.6389), [], 325.0),

	("battlemap_dothraki_sea_2", "Abandoned Camp", icon_camp_tent|pf_is_static|pf_hide_defenders, no_menu, pt_none, fac_neutral, aggressiveness_0, ai_bhvr_hold, 0, (-179.355, 64.6751), [], 325.0),

	("battlemap_dothraki_sea_3", "Abandoned Camp", icon_camp_tent|pf_is_static|pf_hide_defenders, no_menu, pt_none, fac_neutral, aggressiveness_0, ai_bhvr_hold, 0, (-206.365, 48.8976), [], 325.0),

	("battlemap_dothraki_sea_4", "Abandoned Camp", icon_camp_tent|pf_is_static|pf_hide_defenders, no_menu, pt_none, fac_neutral, aggressiveness_0, ai_bhvr_hold, 0, (-189.222, 106.141), [], 325.0),

	("battlemap_dothraki_sea_5", "Abandoned Camp", icon_camp_tent|pf_is_static|pf_hide_defenders, no_menu, pt_none, fac_neutral, aggressiveness_0, ai_bhvr_hold, 0, (-175.94, 165.666), [], 325.0),

	("battlemap_dothraki_sea_6", "Abandoned Camp", icon_camp_tent|pf_is_static|pf_hide_defenders, no_menu, pt_none, fac_neutral, aggressiveness_0, ai_bhvr_hold, 0, (-210.362, 217.249), [], 325.0),

	("battlemap_dothraki_sea_7", "Abandoned Camp", icon_camp_tent|pf_is_static|pf_hide_defenders, no_menu, pt_none, fac_neutral, aggressiveness_0, ai_bhvr_hold, 0, (-200.952, 193.307), [], 325.0),

	("battlemap_dothraki_sea_8", "Abandoned Camp", icon_camp_tent|pf_is_static|pf_hide_defenders, no_menu, pt_none, fac_neutral, aggressiveness_0, ai_bhvr_hold, 0, (-151.688, 70.9299), [], 325.0),

	("rodgars_hut", "Rodgars Hut", icon_map_Rodgars_Hut|pf_disabled|pf_is_static|pf_hide_defenders, no_menu, pt_none, fac_neutral, aggressiveness_0, ai_bhvr_hold, 0, (115.073, -262.267), []),

	("relic_septry", "Septry", icon_map_monastery|pf_is_static|pf_hide_defenders, no_menu, pt_none, fac_neutral, aggressiveness_0, ai_bhvr_hold, 0, (97.1917, -55.3776), []),

	("citadel_septry", "Septry", icon_map_monastery|pf_disabled|pf_is_static|pf_hide_defenders, no_menu, pt_none, fac_neutral, aggressiveness_0, ai_bhvr_hold, 0, (85.8347, -97.3181), []),

	("citadel_holdings", "Holdfast", icon_map_Clegane_Keep|pf_disabled|pf_is_static|pf_hide_defenders, no_menu, pt_none, fac_neutral, aggressiveness_0, ai_bhvr_hold, 0, (69.5301, -100.726), []),

	("citadel_barrow", "Barrow", icon_map_barrow|pf_disabled|pf_is_static|pf_hide_defenders, no_menu, pt_none, fac_neutral, aggressiveness_0, ai_bhvr_hold, 0, (60.9004, -98.4242), []),

	("renly_quest_shore", "The Beach", icon_beach_rocks|pf_disabled|pf_is_static|pf_hide_defenders, no_menu, pt_none, fac_neutral, aggressiveness_0, ai_bhvr_hold, 0, (-5.23268, 9.22319), []),

	("renly_quest_rainwood", "The Rainwood", icon_map_tree_a|pf_disabled|pf_is_static|pf_hide_defenders, no_menu, pt_none, fac_neutral, aggressiveness_0, ai_bhvr_hold, 0, (16.5836, 109.812), []),

	("renly_quest_rainwood_fire_1", "{!}1", icon_map_tree_a|pf_is_static|pf_always_visible|pf_no_label, no_menu, pt_none, fac_neutral, aggressiveness_0, ai_bhvr_hold, 0, (17.4993, 110.313), [], -4.07),

	("renly_quest_rainwood_fire_2", "{!}2", icon_map_tree_a|pf_is_static|pf_always_visible|pf_no_label, no_menu, pt_none, fac_neutral, aggressiveness_0, ai_bhvr_hold, 0, (18.5261, 109.497), [], -4.07),

	("renly_quest_rainwood_fire_3", "{!}3", icon_map_tree_a|pf_is_static|pf_always_visible|pf_no_label, no_menu, pt_none, fac_neutral, aggressiveness_0, ai_bhvr_hold, 0, (18.8878, 111.211), [], -4.07),

	("renly_quest_rainwood_fire_4", "{!}4", icon_map_tree_a|pf_is_static|pf_always_visible|pf_no_label, no_menu, pt_none, fac_neutral, aggressiveness_0, ai_bhvr_hold, 0, (19.0873, 110.465), [], -4.07),

	("isle_of_faces", "The Isle of Faces", icon_bandit_lair|pf_disabled|pf_is_static|pf_hide_defenders, no_menu, pt_none, fac_neutral, aggressiveness_0, ai_bhvr_hold, 0, (74.8269, 12.5723), []),

	("saltpans_isles", "The Quiet Isle", icon_map_monastery|pf_disabled|pf_is_static|pf_hide_defenders, no_menu, pt_none, fac_neutral, aggressiveness_0, ai_bhvr_hold, 0, (42.6021, -2.04975), []),

	("summerhall", "Ruins of Summerhall", icon_map_Ruined_Castle|pf_is_static|pf_hide_defenders, no_menu, pt_none, fac_neutral, aggressiveness_0, ai_bhvr_hold, 0, (50.0866, 110.808), []),

	("nunns_deep", "Nunn's Deep", icon_bandit_lair|pf_is_static|pf_hide_defenders, no_menu, pt_none, fac_neutral, aggressiveness_0, ai_bhvr_hold, 0, (177.985, -21.3714), []),

	("oldstones", "Oldstones", icon_map_the_sorrows|pf_is_static|pf_hide_defenders, no_menu, pt_none, fac_neutral, aggressiveness_0, ai_bhvr_hold, 0, (119.991, -51.4112), []),

	("sorrows", "The Sorrows", icon_map_the_sorrows|pf_is_static|pf_hide_defenders, no_menu, pt_none, fac_neutral, aggressiveness_0, ai_bhvr_hold, 0, (-180.202, 133.042), []),

	("abandoned_holdfast", "Abandoned Holdfast", icon_map_the_sorrows|pf_disabled|pf_is_static|pf_hide_defenders, no_menu, pt_none, fac_neutral, aggressiveness_0, ai_bhvr_hold, 0, (52.9955, -270.228), []),

	("hillhall", "Hillhall", icon_village_c|pf_disabled|pf_is_static|pf_hide_defenders, no_menu, pt_none, fac_neutral, aggressiveness_0, ai_bhvr_hold, 0, (-16.8894, -284.094), []),

	("dragonmont", "Sunken Ruins", icon_map_the_sorrows|pf_disabled|pf_is_static|pf_hide_defenders, no_menu, pt_none, fac_neutral, aggressiveness_0, ai_bhvr_hold, 0, (-194.048, 214.78), []),

	("tower_of_joy", "The Tower of Joy", icon_map_lighthouse|pf_is_static|pf_hide_defenders, no_menu, pt_none, fac_neutral, aggressiveness_0, ai_bhvr_hold, 0, (122.619, 180.908), []),

	("naggas_hill", "Nagga's Hill", icon_bandit_lair|pf_is_static|pf_hide_defenders, no_menu, pt_none, fac_neutral, aggressiveness_0, ai_bhvr_hold, 0, (227.556, -61.8565), []),

	("harrentown", "The Remains of Harrentown", icon_village_c|pf_disabled|pf_is_static|pf_hide_defenders, no_menu, pt_none, fac_neutral, aggressiveness_0, ai_bhvr_hold, 0, (67.6093, 19.2662), []),

	("bloodstone", "Bloodstone", icon_map_essos_castle2|pf_disabled|pf_is_static|pf_hide_defenders, no_menu, pt_none, fac_neutral, aggressiveness_0, ai_bhvr_hold, 0, (-41.0164, 161.638), []),

	("bloodstone_haunt", "Pirate Haunt", icon_bandit_lair|pf_disabled|pf_is_static|pf_hide_defenders, no_menu, pt_none, fac_neutral, aggressiveness_0, ai_bhvr_hold, 0, (-40.0575, 165.19), []),

	("illyrios_manse", "Illyrios Manse", icon_village_c|pf_is_static|pf_hide_defenders, no_menu, pt_none, fac_neutral, aggressiveness_0, ai_bhvr_hold, 0, (-70.6642, 61.5838), []),

	("donation_septry", "Septry", icon_map_monastery|pf_disabled|pf_is_static|pf_hide_defenders, no_menu, pt_none, fac_neutral, aggressiveness_0, ai_bhvr_hold, 0, (10.2563, -26.7682), []),

	("castle_black", "Castle Black", icon_map_nw_castle|pf_disabled|pf_is_static|pf_hide_defenders, no_menu, pt_none, fac_neutral, aggressiveness_0, ai_bhvr_hold, 0, (66.825, -334.727), []),

	("castle_black2", "Castle Black", icon_map_nw_castle|pf_disabled|pf_is_static|pf_hide_defenders, no_menu, pt_none, fac_neutral, aggressiveness_0, ai_bhvr_hold, 0, (66.825, -334.727), []),

	("castle_black3", "Castle Black", icon_map_nw_castle|pf_disabled|pf_is_static|pf_hide_defenders, no_menu, pt_none, fac_neutral, aggressiveness_0, ai_bhvr_hold, 0, (66.825, -334.727), []),

	("castle_black4", "Castle Black", icon_map_nw_castle|pf_disabled|pf_is_static|pf_hide_defenders, no_menu, pt_none, fac_neutral, aggressiveness_0, ai_bhvr_hold, 0, (66.825, -334.727), []),

	("castle_black5", "Castle Black", icon_map_nw_castle|pf_disabled|pf_is_static|pf_hide_defenders, no_menu, pt_none, fac_neutral, aggressiveness_0, ai_bhvr_hold, 0, (66.825, -334.727), []),

	("shadow_tower", "The Shadow Tower", icon_map_nw_castle|pf_disabled|pf_is_static|pf_hide_defenders, no_menu, pt_none, fac_neutral, aggressiveness_0, ai_bhvr_hold, 0, (88.4798, -335.896), []),

	("shadow_tower2", "The Shadow Tower", icon_map_nw_castle|pf_disabled|pf_is_static|pf_hide_defenders, no_menu, pt_none, fac_neutral, aggressiveness_0, ai_bhvr_hold, 0, (88.4798, -335.896), []),

	("eastwatch", "Eastwatch-by-the-Sea", icon_map_nw_castle|pf_disabled|pf_is_static|pf_hide_defenders, no_menu, pt_none, fac_neutral, aggressiveness_0, ai_bhvr_hold, 0, (37.2415, -334.746), []),

	("odin_cave", "Old Cave", icon_bandit_lair|pf_disabled|pf_is_static|pf_hide_defenders, no_menu, pt_none, fac_neutral, aggressiveness_0, ai_bhvr_hold, 0, (-129.566, 0.236816), []),

	("brookwater_keep", "Brookwater Keep", icon_map_Clegane_Keep|pf_disabled|pf_is_static|pf_hide_defenders, no_menu, pt_none, fac_neutral, aggressiveness_0, ai_bhvr_hold, 0, (37.5778, 20.5253), []),

	("dragonstone_village", "Fishing Village", icon_village_c|pf_disabled|pf_is_static|pf_hide_defenders, no_menu, pt_none, fac_neutral, aggressiveness_0, ai_bhvr_hold, 0, (-3.02082, 10.4955), []),

	("haldon_bath", "Ruined Baths", icon_village_c|pf_disabled|pf_is_static|pf_hide_defenders, no_menu, pt_none, fac_neutral, aggressiveness_0, ai_bhvr_hold, 0, (-124.19, 152.077), []),

	("horror_cave", "Old Barrow", icon_bandit_lair|pf_disabled|pf_is_static|pf_hide_defenders, no_menu, pt_none, fac_neutral, aggressiveness_0, ai_bhvr_hold, 0, (-93.9435, -59.4801), []),

	("golden_company_camp", "The Golden Company", icon_camp_entrench|pf_disabled|pf_is_static|pf_hide_defenders, no_menu, pt_none, fac_neutral, aggressiveness_0, ai_bhvr_hold, 0, (-194.914, 202.332), []),

	("cairn_hall", "Cairnhall", icon_village_c|pf_disabled|pf_is_static|pf_hide_defenders, no_menu, pt_none, fac_neutral, aggressiveness_0, ai_bhvr_hold, 0, (39.5081, 134.178), []),

	("mole_town", "Mole Town", icon_village_a|pf_disabled|pf_is_static|pf_hide_defenders, no_menu, pt_none, fac_neutral, aggressiveness_0, ai_bhvr_hold, 0, (64.7417, -326.065), []),

	("bridge_of_skulls", "The Gorge", icon_bandit_lair|pf_disabled|pf_is_static|pf_hide_defenders, no_menu, pt_none, fac_neutral, aggressiveness_0, ai_bhvr_hold, 0, (91.5332, -336.637), []),

	("wall_tunnel", "Tunnel", icon_bandit_lair|pf_disabled|pf_is_static|pf_hide_defenders, no_menu, pt_none, fac_neutral, aggressiveness_0, ai_bhvr_hold, 0, (68.2788, -335.154), []),

	("water_gardens", "The Water Gardens", icon_village_a|pf_disabled|pf_is_static|pf_hide_defenders, no_menu, pt_none, fac_neutral, aggressiveness_0, ai_bhvr_hold, 0, (-3.66968, 216.169), []),

	("nightfort", "The Nightfort", icon_map_nw_castle|pf_disabled|pf_is_static|pf_hide_defenders, no_menu, pt_none, fac_neutral, aggressiveness_0, ai_bhvr_hold, 0, (62.4094, -335.032), []),

	("ninestars_1", "Ninestars", icon_map_castle_red|pf_disabled|pf_is_static|pf_hide_defenders, no_menu, pt_none, fac_neutral, aggressiveness_0, ai_bhvr_hold, 0, (21.6767, -97.7439), []),

	("looter_spawn_point", "looter spawnpoint", icon_people_player|pf_disabled|pf_is_static, no_menu, pt_none, fac_outlaws, aggressiveness_0, ai_bhvr_hold, 0, (119.722, -13.4151), [(trp_bandit_e_looter, 15, 0)]),

	("steppe_bandit_spawn_point", "dothraki spawnpoint", icon_people_player|pf_disabled|pf_is_static, no_menu, pt_none, fac_outlaws, aggressiveness_0, ai_bhvr_hold, 0, (-172.529, 63.2477), [(trp_bandit_e_looter, 15, 0)]),

	("taiga_bandit_spawn_point", "wildling spawnpoint", icon_people_player|pf_disabled|pf_is_static, no_menu, pt_none, fac_outlaws, aggressiveness_0, ai_bhvr_hold, 0, (93.4218, -262.437), [(trp_bandit_e_looter, 15, 0)]),

	("forest_bandit_spawn_point", "the forests", icon_people_player|pf_disabled|pf_is_static, no_menu, pt_none, fac_outlaws, aggressiveness_0, ai_bhvr_hold, 0, (26.6097, 78.1656), [(trp_bandit_e_looter, 15, 0)]),

	("mountain_bandit_spawn_point", "the highlands", icon_people_player|pf_disabled|pf_is_static, no_menu, pt_none, fac_outlaws, aggressiveness_0, ai_bhvr_hold, 0, (-128.252, -7.41371), [(trp_bandit_e_looter, 15, 0)]),

	("sea_raider_spawn_point_1", "ironborn spawnpoint", icon_people_player|pf_disabled|pf_is_static, no_menu, pt_none, fac_outlaws, aggressiveness_0, ai_bhvr_hold, 0, (-85.6246, 202.268), [(trp_bandit_e_looter, 15, 0)]),

	("sea_raider_spawn_point_2", "ironborn spawnpoint", icon_people_player|pf_disabled|pf_is_static, no_menu, pt_none, fac_outlaws, aggressiveness_0, ai_bhvr_hold, 0, (-55.7771, 77.2696), [(trp_bandit_e_looter, 15, 0)]),

	("ship_raider_spawn_point_1", "pirate spawnpoint", icon_people_player|pf_disabled|pf_is_static, no_menu, pt_none, fac_outlaws, aggressiveness_0, ai_bhvr_hold, 0, (2.55759, 50.0091), [(trp_bandit_e_looter, 15, 0)]),

	("slaver_bandit_spawn_point", "slaver spawnpoint", icon_people_player|pf_disabled|pf_is_static, no_menu, pt_none, fac_outlaws, aggressiveness_0, ai_bhvr_hold, 0, (-112.274, 165.857), [(trp_bandit_e_looter, 15, 0)]),

	("escaped_slaves_spawn_point", "escaped slaves spawnpoint", icon_people_player|pf_disabled|pf_is_static, no_menu, pt_none, fac_deserters, aggressiveness_0, ai_bhvr_hold, 0, (-115.257, 73.2688), [(trp_bandit_e_looter, 15, 0)]),

	("clansmen_spawn_point", "clansmen spawnpoint", icon_people_player|pf_disabled|pf_is_static, no_menu, pt_none, fac_outlaws, aggressiveness_0, ai_bhvr_hold, 0, (16.2458, -95.5249), [(trp_bandit_e_looter, 15, 0)]),

	("raiders_spawn_point", "raiders spawnpoint", icon_people_player|pf_disabled|pf_is_static, no_menu, pt_none, fac_outlaws, aggressiveness_0, ai_bhvr_hold, 0, (91.2236, -10.956), [(trp_bandit_e_looter, 15, 0)]),

	("outlaws_spawn_point", "outlaws spawnpoint", icon_people_player|pf_disabled|pf_is_static, no_menu, pt_none, fac_outlaws, aggressiveness_0, ai_bhvr_hold, 0, (103.384, 74.3779), [(trp_bandit_e_looter, 15, 0)]),

	("rhoyne_bandits_spawn_point", "rhoyne spawnpoint", icon_people_player|pf_disabled|pf_is_static, no_menu, pt_none, fac_outlaws, aggressiveness_0, ai_bhvr_hold, 0, (-177.495, 152.184), [(trp_bandit_e_looter, 15, 0)]),

	("elite_raiders_spawn_point", "elite raiders spawnpoint", icon_people_player|pf_disabled|pf_is_static, no_menu, pt_none, fac_outlaws, aggressiveness_0, ai_bhvr_hold, 0, (105.445, -17.9214), [(trp_bandit_e_looter, 15, 0)]),

	("elite_wildlings_spawn_point", "elite wildlings spawnpoint", icon_people_player|pf_disabled|pf_is_static, no_menu, pt_none, fac_outlaws, aggressiveness_0, ai_bhvr_hold, 0, (21.3787, -268.369), [(trp_bandit_e_looter, 15, 0)]),

	("elite_dothraki_spawn_point", "elite dothraki spawnpoint", icon_people_player|pf_disabled|pf_is_static, no_menu, pt_none, fac_outlaws, aggressiveness_0, ai_bhvr_hold, 0, (-172.529, 63.2477), [(trp_bandit_e_looter, 15, 0)]),

	("crannogmen", "crannogmen", icon_people_player|pf_disabled|pf_is_static, no_menu, pt_none, fac_outlaws, aggressiveness_0, ai_bhvr_hold, 0, (125.493, -110.776), [(trp_bandit_e_looter, 15, 0)]),

	("desert_bandit_spawn_point", "sandoutlaw spawnpoint", icon_people_player|pf_disabled|pf_is_static, no_menu, pt_none, fac_outlaws, aggressiveness_0, ai_bhvr_hold, 0, (46.4902, 226.064), [(trp_bandit_e_looter, 15, 0)]),

	("spawn_points_end", "{!}last spawn point", icon_people_player|pf_disabled|pf_is_static, no_menu, pt_none, fac_commoners, aggressiveness_0, ai_bhvr_hold, 0, (0.0, 0.0), [(trp_bandit_e_looter, 15, 0)]),

	("reserved_1", "{!}last spawn point", icon_people_player|pf_disabled|pf_is_static, no_menu, pt_none, fac_commoners, aggressiveness_0, ai_bhvr_hold, 0, (0.0, 0.0), [(trp_bandit_e_looter, 15, 0)]),

	("reserved_2", "{!}last spawn point", icon_people_player|pf_disabled|pf_is_static, no_menu, pt_none, fac_commoners, aggressiveness_0, ai_bhvr_hold, 0, (0.0, 0.0), [(trp_bandit_e_looter, 15, 0)]),

	("reserved_3", "{!}last spawn point", icon_people_player|pf_disabled|pf_is_static, no_menu, pt_none, fac_commoners, aggressiveness_0, ai_bhvr_hold, 0, (0.0, 0.0), [(trp_bandit_e_looter, 15, 0)]),

	("reserved_4", "{!}last spawn point", icon_people_player|pf_disabled|pf_is_static, no_menu, pt_none, fac_commoners, aggressiveness_0, ai_bhvr_hold, 0, (0.0, 0.0), [(trp_bandit_e_looter, 15, 0)]),

	("reserved_5", "{!}last spawn point", icon_people_player|pf_disabled|pf_is_static, no_menu, pt_none, fac_commoners, aggressiveness_0, ai_bhvr_hold, 0, (0.0, 0.0), [(trp_bandit_e_looter, 15, 0)]),

	("elite_dothraki_spawn_point2", "elite dothraki spawnpoint2", icon_people_player|pf_disabled|pf_is_static, no_menu, pt_none, fac_outlaws, aggressiveness_0, ai_bhvr_hold, 0, (70.884415, 4.789415), [(trp_bandit_e_looter, 15, 0)]),

	("elite_dothraki_spawn_point3", "elite dothraki spawnpoint3", icon_people_player|pf_disabled|pf_is_static, no_menu, pt_none, fac_deserters, aggressiveness_0, ai_bhvr_hold, 0, (115.539000, -2.118070), [(trp_bandit_e_looter, 15, 0)]),

	("elite_dothraki_spawn_point4", "elite dothraki spawnpoint4", icon_people_player|pf_disabled|pf_is_static, no_menu, pt_none, fac_deserters, aggressiveness_0, ai_bhvr_hold, 0, (-77.446800, 163.007000), [(trp_bandit_e_looter, 15, 0)]),

	("elite_dothraki_spawn_point5", "elite dothraki spawnpoint5", icon_people_player|pf_disabled|pf_is_static, no_menu, pt_none, fac_outlaws, aggressiveness_0, ai_bhvr_hold, 0, (-77.446800, 163.007000), [(trp_bandit_e_looter, 15, 0)]),
	
	("elite_dothraki_spawn_point6", "elite dothraki spawnpoint6", icon_people_player|pf_disabled|pf_is_static, no_menu, pt_none, fac_outlaws, aggressiveness_0, ai_bhvr_hold, 0, (-180.202000, 133.042000), [(trp_bandit_e_looter, 15, 0)]),

	("elite_dothraki_spawn_point7", "elite dothraki spawnpoint7", icon_people_player|pf_disabled|pf_is_static, no_menu, pt_none, fac_outlaws, aggressiveness_0, ai_bhvr_hold, 0, (-180.202000, 133.042000), [(trp_bandit_e_looter, 15, 0)]),

	("elite_dothraki_spawn_point8", "elite dothraki spawnpoint8", icon_people_player|pf_disabled|pf_is_static, no_menu, pt_none, fac_outlaws, aggressiveness_0, ai_bhvr_hold, 0, (56.085400, 51.681200), [(trp_bandit_e_looter, 15, 0)]),
	
	("elite_dothraki_spawn_point9", "elite dothraki spawnpoint9", icon_people_player|pf_disabled|pf_is_static, no_menu, pt_none, fac_kingdom_2, aggressiveness_0, ai_bhvr_hold, 0, (105.677000, -230.088000), [(trp_bandit_e_looter, 15, 0)]),

	("elite_dothraki_spawn_point11", "elite dothraki spawnpoint11", icon_people_player|pf_disabled|pf_is_static, no_menu, pt_none, fac_outlaws, aggressiveness_0, ai_bhvr_hold, 0, (-166.978000, 81.255900), [(trp_bandit_e_looter, 15, 0)]),

	("elite_dothraki_spawn_point12", "elite dothraki spawnpoint12", icon_people_player|pf_disabled|pf_is_static, no_menu, pt_none, fac_outlaws, aggressiveness_0, ai_bhvr_hold, 0, (-166.978000, 81.255900), [(trp_bandit_e_looter, 15, 0)]),

]