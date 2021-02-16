from header_factions import *

####################################################################################################################
#  Each faction record contains the following fields:
#  1) Faction id: used for referencing factions in other files.
#     The prefix fac_ is automatically added before each faction id.
#  2) Faction name.
#  3) Faction flags. See header_factions.py for a list of available flags
#  4) Faction coherence. Relation between members of this faction.
#  5) Relations. This is a list of relation records.
#     Each relation record is a tuple that contains the following fields:
#    5.1) Faction. Which other faction this relation is referring to
#    5.2) Value: Relation value between the two factions.
#         Values range between -1 and 1.
#  6) Ranks
#  7) Faction color (default is gray)
####################################################################################################################

factions = [
	("no_faction", "No Faction", 0, 0.9, []),

	("commoners", "Commoners", 0, 0.1, [("player_faction",0.10),("mountain_bandits",-0.20),("outlaws",-0.60),("forest_bandits",-0.20),("undeads",-0.70)]),

	("outlaws", "Outlaws", max_player_rating(-30), 0.5, [("player_faction",-0.15),("kingdom_17",-0.05),("kingdom_12",-0.05),("kingdom_21",-0.05),("kingdom_9",-0.05),("kingdom_16",-0.05),("innocents",-0.05),("kingdom_19",-0.05),("kingdom_13",-0.05),("crannogmen",-0.05),("player_supporters_faction",-0.05),("kingdom_6",-0.05),("kingdom_3",-0.05),("merchants",-0.50),("kingdom_11",-0.05),("kingdom_4",-0.05),("kingdom_14",-0.05),("kingdom_8",-0.05),("kingdom_10",-0.05),("kingdom_5",-0.05),("commoners",-0.60),("kingdom_18",-0.05),("kingdom_22",-0.05),("kingdom_2",-0.05),("kingdom_1",-0.05),("kingdom_15",-0.05),("kingdom_20",-0.05),("manhunters",-0.60),("deserters",-0.10)], [], 0x00888888),

	("neutral", "Neutral", 0, 0.1, [], [], 0x00ffffff),

	("innocents", "Innocents", ff_always_hide_label, 0.5, [("outlaws",-0.05),("dark_knights",-0.90)]),

	("merchants", "Merchants", ff_always_hide_label, 0.5, [("mountain_bandits",-0.50),("outlaws",-0.50),("forest_bandits",-0.50),("deserters",-0.50)]),

	("dark_knights", "{!}Dark Knights", 0, 0.5, [("player_faction",-0.40),("innocents",-0.90)]),

	("culture_1", "{!}culture 1", 0, 0.9, []),

	("culture_2", "{!}culture 2", 0, 0.9, []),

	("culture_3", "{!}culture 3", 0, 0.9, []),

	("culture_4", "{!}culture 4", 0, 0.9, []),

	("culture_5", "{!}culture 5", 0, 0.9, []),

	("culture_6", "{!}culture 6", 0, 0.9, []),

	("culture_7", "{!}culture 7", 0, 0.9, []),

	("culture_8", "{!}culture 8", 0, 0.9, []),

	("culture_9", "{!}culture 9", 0, 0.9, []),

	("culture_10", "{!}culture 10", 0, 0.9, []),

	("culture_11", "{!}culture 11", 0, 0.9, []),

	("culture_12", "{!}culture 12", 0, 0.9, []),

	("culture_13", "{!}culture 13", 0, 0.9, []),

	("culture_14", "{!}culture 14", 0, 0.9, []),

	("culture_15", "{!}culture 15", 0, 0.9, []),

	("culture_16", "{!}culture 16", 0, 0.9, []),

	("culture_17", "{!}culture 17", 0, 0.9, []),

	("culture_18", "{!}culture 18", 0, 0.9, []),

	("culture_19", "{!}culture 19", 0, 0.9, []),

	("culture_20", "{!}culture 20", 0, 0.9, []),

	("culture_21", "{!}culture 21", 0, 0.9, []),

	("culture_22", "{!}culture 22", 0, 0.9, []),

	("player_faction", "Player Faction", 0, 0.9, [("fac_wights",-1.00),("black_khergits",-0.30),("mountain_bandits",-0.15),("player_supporters_faction",1.00),("ramsay_snow",-1.00),("outlaws",-0.15),("bloodborn",-1.00),("forest_bandits",-0.15),("deserters",-0.10),("commoners",0.10),("beowulf_warband",-1.00),("peasant_rebels",-0.40),("manhunters",0.10),("undeads",-0.50),("dark_knights",-0.40)]),

	("player_supporters_faction", "Player's Supporters", 0, 0.9, [("player_faction",1.00),("mountain_bandits",-0.05),("outlaws",-0.05),("forest_bandits",-0.05),("deserters",-0.02),("peasant_rebels",-0.10)], [], 0x00008ab8),

	("kingdom_1", "The Stormlands", 0, 0.9, [("kingdom_17",0.10),("kingdom_12",0.10),("kingdom_21",0.10),("kingdom_9",0.10),("kingdom_16",0.10),("kingdom_19",0.10),("kingdom_13",0.10),("black_khergits",-0.02),("mountain_bandits",-0.05),("kingdom_6",0.10),("outlaws",-0.05),("kingdom_3",0.10),("kingdom_11",0.10),("kingdom_4",0.10),("kingdom_14",0.10),("kingdom_8",0.10),("forest_bandits",-0.05),("deserters",-0.05),("kingdom_10",1.00),("kingdom_5",0.40),("kingdom_18",0.10),("peasant_rebels",-0.10),("kingdom_22",0.10),("kingdom_2",0.10),("kingdom_15",0.10),("kingdom_20",0.10)], [], 0x00ffe03d),

	("kingdom_2", "The North", 0, 0.9, [("kingdom_17",0.10),("kingdom_12",0.10),("kingdom_21",0.10),("kingdom_9",-1.00),("kingdom_16",0.10),("kingdom_19",0.10),("kingdom_13",0.10),("black_khergits",-0.02),("crannogmen",1.00),("mountain_bandits",-0.05),("kingdom_6",0.10),("outlaws",-0.05),("kingdom_3",0.10),("kingdom_11",0.10),("kingdom_4",0.10),("kingdom_14",0.10),("kingdom_8",0.10),("forest_bandits",-0.05),("deserters",-0.05),("kingdom_10",0.40),("kingdom_5",0.10),("kingdom_18",0.10),("peasant_rebels",-0.10),("kingdom_22",0.10),("kingdom_1",0.10),("kingdom_15",0.10),("kingdom_20",0.10)], [], 0x00ffffff),

	("kingdom_3", "The Vale", 0, 0.9, [("kingdom_17",0.10),("kingdom_12",0.10),("kingdom_21",0.40),("kingdom_9",0.10),("kingdom_16",0.10),("kingdom_19",0.40),("kingdom_13",0.10),("mountain_bandits",-0.05),("kingdom_6",0.10),("outlaws",-0.05),("kingdom_11",0.10),("kingdom_4",0.10),("kingdom_14",0.10),("kingdom_8",0.10),("forest_bandits",-0.05),("deserters",-0.05),("kingdom_10",0.10),("kingdom_5",0.10),("kingdom_18",0.10),("peasant_rebels",-0.10),("kingdom_22",0.40),("kingdom_2",0.10),("kingdom_1",0.10),("kingdom_15",0.10),("kingdom_20",0.40)], [], 0x003399ff),

	("kingdom_4", "Braavos", 0, 0.9, [("kingdom_17",0.10),("kingdom_12",0.10),("kingdom_21",0.10),("kingdom_9",0.10),("kingdom_16",0.10),("kingdom_19",0.10),("kingdom_13",0.10),("mountain_bandits",-0.05),("kingdom_6",0.10),("outlaws",-0.05),("kingdom_3",0.10),("kingdom_11",0.10),("kingdom_14",0.10),("kingdom_8",0.10),("forest_bandits",-0.05),("deserters",-0.05),("kingdom_10",0.10),("kingdom_5",0.10),("kingdom_18",0.10),("peasant_rebels",-0.10),("kingdom_22",0.10),("kingdom_2",0.10),("kingdom_1",0.10),("kingdom_15",0.10),("kingdom_20",0.10)], [], 0x00ff3366),

	("kingdom_5", "Qohor", 0, 0.9, [("kingdom_17",0.10),("kingdom_12",0.10),("kingdom_21",0.10),("kingdom_9",0.10),("kingdom_16",0.10),("kingdom_19",0.10),("kingdom_13",0.10),("mountain_bandits",-0.05),("kingdom_6",0.10),("outlaws",-0.05),("kingdom_3",0.10),("kingdom_11",0.10),("kingdom_4",0.10),("kingdom_14",0.10),("kingdom_8",0.10),("forest_bandits",-0.05),("deserters",-0.05),("kingdom_10",0.10),("kingdom_18",0.10),("peasant_rebels",-0.10),("kingdom_22",0.10),("kingdom_2",0.10),("kingdom_1",0.40),("kingdom_15",0.10),("kingdom_20",0.10)], [], 0x0099cc66),

	("kingdom_6", "Dorne", 0, 0.9, [("kingdom_17",0.10),("kingdom_12",0.10),("kingdom_21",0.10),("kingdom_9",0.10),("kingdom_16",0.10),("kingdom_19",0.10),("kingdom_13",0.10),("mountain_bandits",-0.05),("outlaws",-0.05),("kingdom_3",0.10),("kingdom_11",0.10),("kingdom_4",0.10),("kingdom_14",0.10),("kingdom_8",0.10),("forest_bandits",-0.05),("deserters",-0.05),("kingdom_10",0.10),("kingdom_5",0.10),("kingdom_18",0.10),("peasant_rebels",-0.10),("kingdom_22",0.10),("kingdom_2",0.10),("kingdom_1",0.10),("kingdom_15",0.10),("kingdom_20",0.10)], [], 0x00ff6600),

	("kingdom_8", "Dragonstone", 0, 0.9, [("kingdom_17",0.10),("kingdom_12",0.10),("kingdom_21",0.10),("kingdom_9",0.10),("kingdom_16",0.10),("kingdom_19",0.10),("kingdom_13",0.10),("mountain_bandits",-0.05),("kingdom_6",0.10),("outlaws",-0.05),("kingdom_3",0.10),("kingdom_11",0.10),("kingdom_4",0.10),("kingdom_14",0.10),("forest_bandits",-0.05),("deserters",-0.05),("kingdom_10",0.10),("kingdom_5",0.10),("kingdom_18",0.10),("peasant_rebels",-0.10),("kingdom_22",0.10),("kingdom_2",0.10),("kingdom_1",0.10),("kingdom_15",0.10),("kingdom_20",0.10),("crannogmen",-1.00)], [], 0x00b77171),

	("kingdom_9", "The Westerlands", 0, 0.9, [("kingdom_17",0.10),("kingdom_12",0.10),("kingdom_21",0.10),("kingdom_16",0.10),("kingdom_19",0.10),("kingdom_13",0.10),("mountain_bandits",-0.05),("kingdom_6",0.10),("outlaws",-0.05),("kingdom_3",0.10),("kingdom_11",0.10),("kingdom_4",0.10),("kingdom_14",0.10),("kingdom_8",0.10),("forest_bandits",-0.05),("deserters",-0.05),("kingdom_10",0.10),("kingdom_5",0.10),("kingdom_18",0.10),("peasant_rebels",-0.10),("kingdom_22",0.10),("kingdom_2",-1.00),("kingdom_1",0.10),("kingdom_15",0.10),("kingdom_20",0.10)], [], 0x00e02121),

	("kingdom_10", "The Reach", 0, 0.9, [("kingdom_17",0.10),("kingdom_12",0.10),("kingdom_21",0.10),("kingdom_9",0.10),("kingdom_16",0.10),("kingdom_19",0.10),("kingdom_13",0.10),("mountain_bandits",-0.05),("kingdom_6",0.10),("outlaws",-0.05),("kingdom_3",0.10),("kingdom_11",0.10),("kingdom_4",0.10),("kingdom_14",0.10),("kingdom_8",0.10),("forest_bandits",-0.05),("deserters",-0.05),("kingdom_5",0.10),("kingdom_18",0.10),("peasant_rebels",-0.10),("kingdom_22",0.10),("kingdom_2",0.40),("kingdom_1",1.00),("kingdom_15",0.10),("kingdom_20",0.10)], [], 0x0066cc66),

	("kingdom_11", "The Iron Islands", 0, 0.9, [("kingdom_17",0.10),("kingdom_12",0.10),("kingdom_21",0.10),("kingdom_9",0.10),("kingdom_16",0.10),("kingdom_19",0.10),("kingdom_13",0.10),("mountain_bandits",-0.05),("kingdom_6",0.10),("outlaws",-0.05),("kingdom_3",0.10),("kingdom_4",0.10),("kingdom_14",0.10),("kingdom_8",0.10),("forest_bandits",-0.05),("deserters",-0.05),("kingdom_10",0.10),("kingdom_5",0.10),("kingdom_18",0.10),("peasant_rebels",-0.10),("kingdom_22",0.10),("kingdom_2",0.10),("kingdom_1",0.10),("kingdom_15",0.10),("kingdom_20",0.10)], [], 0x00717171),

	("kingdom_12", "Pentos", 0, 0.9, [("kingdom_17",0.10),("kingdom_21",0.10),("kingdom_9",0.10),("kingdom_16",0.10),("kingdom_19",0.10),("kingdom_13",0.10),("mountain_bandits",-0.05),("kingdom_6",0.10),("outlaws",-0.05),("kingdom_3",0.10),("kingdom_11",0.10),("kingdom_4",0.10),("kingdom_14",0.10),("kingdom_8",0.10),("forest_bandits",-0.05),("deserters",-0.05),("kingdom_10",0.10),("kingdom_5",0.10),("kingdom_18",0.10),("peasant_rebels",-0.10),("kingdom_22",0.10),("kingdom_2",0.10),("kingdom_1",0.10),("kingdom_15",0.10),("kingdom_20",0.10)], [], 0x00ffcc99),

	("kingdom_13", "Tyrosh", 0, 0.9, [("kingdom_17",0.10),("kingdom_12",0.10),("kingdom_21",0.10),("kingdom_9",0.10),("kingdom_16",0.10),("kingdom_19",0.10),("mountain_bandits",-0.05),("kingdom_6",0.10),("outlaws",-0.05),("kingdom_3",0.10),("kingdom_11",0.10),("kingdom_4",0.10),("kingdom_14",0.40),("kingdom_8",0.10),("forest_bandits",-0.05),("deserters",-0.05),("kingdom_10",0.10),("kingdom_5",0.10),("kingdom_18",0.10),("peasant_rebels",-0.10),("kingdom_22",0.10),("kingdom_2",0.10),("kingdom_1",0.10),("kingdom_15",0.10),("kingdom_20",0.10)], [], 0x00c397ad),

	("kingdom_14", "Myr", 0, 0.9, [("kingdom_17",0.10),("kingdom_12",0.10),("kingdom_21",0.10),("kingdom_9",0.10),("kingdom_16",0.10),("kingdom_19",0.10),("kingdom_13",0.40),("mountain_bandits",-0.05),("kingdom_6",0.10),("outlaws",-0.05),("kingdom_3",0.10),("kingdom_11",0.10),("kingdom_4",0.10),("kingdom_8",0.10),("forest_bandits",-0.05),("deserters",-0.05),("kingdom_10",0.10),("kingdom_5",0.10),("kingdom_18",0.10),("peasant_rebels",-0.10),("kingdom_22",0.10),("kingdom_2",0.10),("kingdom_1",0.10),("kingdom_15",0.10),("kingdom_20",0.10)], [], 0x007171b7),

	("kingdom_15", "Lys", 0, 0.9, [("kingdom_17",0.10),("kingdom_12",0.10),("kingdom_21",0.10),("kingdom_9",0.10),("kingdom_16",0.10),("kingdom_19",0.10),("kingdom_13",0.10),("mountain_bandits",-0.05),("kingdom_6",0.10),("outlaws",-0.05),("kingdom_3",0.10),("kingdom_11",0.10),("kingdom_4",0.10),("kingdom_14",0.10),("kingdom_8",0.10),("forest_bandits",-0.05),("deserters",-0.05),("kingdom_10",0.10),("kingdom_5",0.10),("kingdom_18",0.10),("peasant_rebels",-0.10),("kingdom_22",0.10),("kingdom_2",0.10),("kingdom_1",0.10),("kingdom_20",0.10)], [], 0x00ffcc66),

	("kingdom_16", "Volantis", 0, 0.9, [("kingdom_17",0.10),("kingdom_12",0.10),("kingdom_21",0.10),("kingdom_9",0.10),("kingdom_19",0.10),("kingdom_13",0.10),("mountain_bandits",-0.05),("kingdom_6",0.10),("outlaws",-0.05),("kingdom_3",0.10),("kingdom_11",0.10),("kingdom_4",0.10),("kingdom_14",0.10),("kingdom_8",0.10),("forest_bandits",-0.05),("deserters",-0.05),("kingdom_10",0.10),("kingdom_5",0.10),("kingdom_18",0.10),("peasant_rebels",-0.10),("kingdom_22",0.10),("kingdom_2",0.10),("kingdom_1",0.10),("kingdom_15",0.10),("kingdom_20",0.10)], [], 0x0033cccc),

	("kingdom_17", "Norvos", 0, 0.9, [("kingdom_12",0.10),("kingdom_21",0.10),("kingdom_9",0.10),("kingdom_16",0.10),("kingdom_19",0.10),("kingdom_13",0.10),("mountain_bandits",-0.05),("kingdom_6",0.10),("outlaws",-0.05),("kingdom_3",0.10),("kingdom_11",0.10),("kingdom_4",0.10),("kingdom_14",0.10),("kingdom_8",0.10),("forest_bandits",-0.05),("deserters",-0.05),("kingdom_10",0.10),("kingdom_5",0.10),("kingdom_18",0.10),("peasant_rebels",-0.10),("kingdom_22",0.10),("kingdom_2",0.10),("kingdom_1",0.10),("kingdom_15",0.10),("kingdom_20",0.10)], [], 0x00f59000),

	("kingdom_18", "Lorath", 0, 0.9, [("kingdom_17",0.10),("kingdom_12",0.10),("kingdom_21",0.10),("kingdom_9",0.10),("kingdom_16",0.10),("kingdom_19",0.10),("kingdom_13",0.10),("mountain_bandits",-0.05),("kingdom_6",0.10),("outlaws",-0.05),("kingdom_3",0.10),("kingdom_11",0.10),("kingdom_4",0.10),("kingdom_14",0.10),("kingdom_8",0.10),("forest_bandits",-0.05),("deserters",-0.05),("kingdom_10",0.10),("kingdom_5",0.10),("peasant_rebels",-0.10),("kingdom_22",0.10),("kingdom_2",0.10),("kingdom_1",0.10),("kingdom_15",0.10),("kingdom_20",0.10)], [], 0x0066997f),

	("kingdom_19", "The Three Sisters", 0, 0.9, [("kingdom_17",0.10),("kingdom_12",0.10),("kingdom_9",0.10),("kingdom_16",0.10),("kingdom_13",0.10),("mountain_bandits",-0.05),("kingdom_6",0.10),("outlaws",-0.05),("kingdom_3",0.40),("kingdom_11",0.10),("kingdom_4",0.10),("kingdom_14",0.10),("kingdom_8",0.10),("forest_bandits",-0.05),("deserters",-0.05),("kingdom_10",0.10),("kingdom_5",0.10),("kingdom_18",0.10),("peasant_rebels",-0.10),("kingdom_2",0.10),("kingdom_1",0.10),("kingdom_15",0.10)], [], 0x0071b795),

	("kingdom_20", "House Targaryen", 0, 0.9, [("kingdom_17",0.10),("kingdom_12",0.10),("kingdom_9",0.10),("kingdom_16",0.10),("kingdom_13",0.10),("mountain_bandits",-0.05),("kingdom_6",0.10),("outlaws",-0.05),("kingdom_3",0.40),("kingdom_11",0.10),("kingdom_4",0.10),("kingdom_14",0.10),("kingdom_8",0.10),("forest_bandits",-0.05),("deserters",-0.05),("kingdom_10",0.10),("kingdom_5",0.10),("kingdom_18",0.10),("peasant_rebels",-0.10),("kingdom_2",0.10),("kingdom_1",0.10),("kingdom_15",0.10)], [], 0x00b72a2a),

	("kingdom_21", "The Free Folk", 0, 0.9, [("kingdom_17",0.10),("kingdom_12",0.10),("kingdom_9",0.10),("kingdom_16",0.10),("kingdom_13",0.10),("mountain_bandits",-0.05),("kingdom_6",0.10),("outlaws",-0.05),("kingdom_3",0.40),("kingdom_11",0.10),("kingdom_4",0.10),("kingdom_14",0.10),("kingdom_8",0.10),("forest_bandits",-0.05),("deserters",-0.05),("kingdom_10",0.10),("kingdom_5",0.10),("kingdom_18",0.10),("peasant_rebels",-0.10),("kingdom_2",0.10),("kingdom_1",0.10),("kingdom_15",0.10)], [], 0x00c28547),

	("kingdom_22", "The Khizra Khalasar", 0, 0.9, [("kingdom_17",0.10),("kingdom_12",0.10),("kingdom_9",0.10),("kingdom_16",0.10),("kingdom_13",0.10),("mountain_bandits",-0.05),("kingdom_6",0.10),("outlaws",-0.05),("kingdom_3",0.40),("kingdom_11",0.10),("kingdom_4",0.10),("kingdom_14",0.10),("kingdom_8",0.10),("forest_bandits",-0.05),("deserters",-0.05),("kingdom_10",0.10),("kingdom_5",0.10),("kingdom_18",0.10),("peasant_rebels",-0.10),("kingdom_2",0.10),("kingdom_1",0.10),("kingdom_15",0.10)], [], 0x00be9d64),

	("kingdoms_end", "{!}kingdoms end", 0, 0.0, []),

	("robber_knights", "{!}robber knights", 0, 0.1, []),

	("khergits", "{!}Khergits", 0, 0.5, []),

	("black_khergits", "{!}Freelancers", 0, 0.5, [("player_faction",-0.30),("kingdom_2",-0.02),("kingdom_1",-0.02)]),

	("crannogmen", "Faith of the Seven", 0, 0.5, [("mountain_bandits",-0.05),("outlaws",-0.05),("forest_bandits",-0.05),("deserters",-0.05),("peasant_rebels",-0.10),("kingdom_8",-1.00)], [], 0x00ffffff),

	("beowulf_warband", "Foraging Sellswords", 0, 0.5, [("player_faction",-1.00)], [], 0x0033ff66),

	("ramsay_snow", "The Bastard of Bolton", 0, 0.5, [("player_faction",-1.00)], [], 0x00ff6699),

	("bloodborn", "Exile Warbands", 0, 0.5, [("player_faction",-1.00)], [], 0x0000b8f5),

	("fac_wights", "Wights", 0, 0.5, [("player_faction",-1.00)], [], 0x0033ffcc),

	("manhunters", "Manhunters", 0, 0.5, [("player_faction",0.10),("mountain_bandits",-0.60),("outlaws",-0.60),("forest_bandits",-0.60),("deserters",-0.60)]),

	("deserters", "Deserters", 0, 0.5, [("player_faction",-0.10),("kingdom_17",-0.05),("kingdom_12",-0.05),("kingdom_21",-0.05),("kingdom_9",-0.05),("kingdom_16",-0.05),("kingdom_19",-0.05),("kingdom_13",-0.05),("crannogmen",-0.05),("player_supporters_faction",-0.02),("kingdom_6",-0.05),("kingdom_3",-0.05),("merchants",-0.50),("kingdom_11",-0.05),("kingdom_4",-0.05),("kingdom_14",-0.05),("kingdom_8",-0.05),("kingdom_10",-0.05),("kingdom_5",-0.05),("kingdom_18",-0.05),("kingdom_22",-0.05),("kingdom_2",-0.05),("kingdom_1",-0.05),("kingdom_15",-0.05),("kingdom_20",-0.05),("manhunters",-0.60),("outlaws",-0.10)], [], 0x00888888),

	("mountain_bandits", "Mountain Bandits", 0, 0.5, [("player_faction",-0.15),("kingdom_17",-0.05),("kingdom_12",-0.05),("kingdom_21",-0.05),("kingdom_9",-0.05),("kingdom_16",-0.05),("kingdom_19",-0.05),("kingdom_13",-0.05),("crannogmen",-0.05),("player_supporters_faction",-0.05),("kingdom_6",-0.05),("kingdom_3",-0.05),("merchants",-0.50),("kingdom_11",-0.05),("kingdom_4",-0.05),("kingdom_14",-0.05),("kingdom_8",-0.05),("kingdom_10",-0.05),("kingdom_5",-0.05),("commoners",-0.20),("kingdom_18",-0.05),("kingdom_22",-0.05),("kingdom_2",-0.05),("kingdom_1",-0.05),("kingdom_15",-0.05),("kingdom_20",-0.05),("manhunters",-0.60)], [], 0x00888888),

	("forest_bandits", "Forest Bandits", 0, 0.5, [("player_faction",-0.15),("kingdom_17",-0.05),("kingdom_12",-0.05),("kingdom_21",-0.05),("kingdom_9",-0.05),("kingdom_16",-0.05),("kingdom_19",-0.05),("kingdom_13",-0.05),("crannogmen",-0.05),("player_supporters_faction",-0.05),("kingdom_6",-0.05),("kingdom_3",-0.05),("merchants",-0.50),("kingdom_11",-0.05),("kingdom_4",-0.05),("kingdom_14",-0.05),("kingdom_8",-0.05),("kingdom_10",-0.05),("kingdom_5",-0.05),("commoners",-0.20),("kingdom_18",-0.05),("kingdom_22",-0.05),("kingdom_2",-0.05),("kingdom_1",-0.05),("kingdom_15",-0.05),("kingdom_20",-0.05),("manhunters",-0.60)], [], 0x00888888),

	("undeads", "{!}Undeads", max_player_rating(-30), 0.5, [("player_faction",-0.50),("commoners",-0.70)]),

	("slavers", "{!}Slavers", 0, 0.1, []),

	("peasant_rebels", "{!}Peasant Rebels", 0, 1.0, [("player_faction",-0.40),("kingdom_17",-0.10),("kingdom_12",-0.10),("kingdom_21",-0.10),("kingdom_9",-0.10),("kingdom_16",-0.10),("kingdom_19",-0.10),("kingdom_13",-0.10),("crannogmen",-0.10),("player_supporters_faction",-0.10),("kingdom_6",-0.10),("kingdom_3",-0.10),("kingdom_11",-0.10),("kingdom_4",-0.10),("kingdom_14",-0.10),("kingdom_8",-0.10),("kingdom_10",-0.10),("kingdom_5",-0.10),("kingdom_18",-0.10),("kingdom_22",-0.10),("kingdom_2",-0.10),("kingdom_1",-0.10),("kingdom_15",-0.10),("kingdom_20",-0.10),("noble_refugees",-1.00)]),

	("noble_refugees", "{!}Noble Refugees", 0, 0.5, [("peasant_rebels",-1.00)]),

]