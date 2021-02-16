from header_map_icons import *
from module_constants import *
from header_operations import *
from header_triggers import *
from ID_sounds import *

####################################################################################################################
#  Each map icon record contains the following fields:
#  1) Map icon id: used for referencing map icons in other files.
#     The prefix icon_ is automatically added before each map icon id.
#  2) Map icon flags. See header_map icons.py for a list of available flags
#  3) Mesh name.
#  4) Scale. 
#  5) Sound.
#  6) Offset x position for the flag icon.
#  7) Offset y position for the flag icon.
#  8) Offset z position for the flag icon.
####################################################################################################################

banner_scale = 0.3
avatar_scale = 0.15

map_icons = [
	("people_player", 0, "player", avatar_scale, snd_footstep_grass, 0.15, 0.173, 0.0),

	("people_player_horseman", 0, "player_horseman", avatar_scale, snd_gallop, 0.15, 0.173, 0.0),

	("people_gray_knight", 0, "knight_a", avatar_scale, snd_gallop, 0.15, 0.173, 0.0),

	("people_vaegir_knight", 0, "knight_b", avatar_scale, snd_gallop, 0.15, 0.173, 0.0),

	("people_flagbearer_a", 0, "flagbearer_a", avatar_scale, snd_gallop, 0.15, 0.173, 0.0),

	("people_flagbearer_b", 0, "flagbearer_b", avatar_scale, snd_gallop, 0.15, 0.173, 0.0),

	("people_peasant", 0, "peasant_a", avatar_scale, snd_footstep_grass, 0.15, 0.173, 0.0),

	("people_khergit", 0, "khergit_horseman", avatar_scale, snd_gallop, 0.15, 0.173, 0.0),

	("people_khergit_horseman_b", 0, "khergit_horseman_b", avatar_scale, snd_gallop, 0.15, 0.173, 0.0),

	("people_axeman", 0, "bandit_a", avatar_scale, snd_footstep_grass, 0.15, 0.173, 0.0),

	("people_woman", 0, "woman_a", avatar_scale, snd_footstep_grass, 0.15, 0.173, 0.0),

	("people_woman_b", 0, "woman_b", avatar_scale, snd_footstep_grass, 0.15, 0.173, 0.0),

	("people_mule", 0, "icon_mule", 0.2, snd_footstep_grass, 0.15, 0.173, 0.0),

	("people_cattle", 0, "icon_cow", 0.2, snd_footstep_grass, 0.15, 0.173, 0.0),

	("new_icon_deserters", 0, "new_icon_deserters", avatar_scale, snd_footstep_grass, 0.15, 0.173, 0.0),

	("new_icon_wildlings", 0, "new_icon_wildlings", avatar_scale, snd_footstep_grass, 0.15, 0.173, 0.0),

	("new_icon_mountain_bandit", 0, "new_icon_mountain_bandit", avatar_scale, snd_footstep_grass, 0.15, 0.173, 0.0),

	("new_icon_rhoyne_outlaw", 0, "new_icon_rhoyne_outlaw", avatar_scale, snd_footstep_grass, 0.15, 0.173, 0.0),

	("new_icon_crannogmen", 0, "new_icon_crannogmen", avatar_scale, snd_footstep_grass, 0.15, 0.173, 0.0),

	("new_icon_pirates", 0, "new_icon_pirates", avatar_scale, snd_footstep_grass, 0.15, 0.173, 0.0),

	("new_icon_thieves", 0, "new_icon_thieves", avatar_scale, snd_footstep_grass, 0.15, 0.173, 0.0),

	("new_icon_bandits", 0, "new_icon_bandits", avatar_scale, snd_footstep_grass, 0.15, 0.173, 0.0),

	("new_icon_forest_bandit", 0, "new_icon_forest_bandit", avatar_scale, snd_footstep_grass, 0.15, 0.173, 0.0),

	("new_icon_raiders", 0, "new_icon_raiders", avatar_scale, snd_gallop, 0.15, 0.173, 0.0),

	("new_icon_dothraki", 0, "new_icon_dothraki", avatar_scale, snd_gallop, 0.15, 0.173, 0.0),

	("town_mercenary_zendar", mcn_no_shadow, "Westeros_Town_Red", 0.35, snd_click, 0.0, 0.0, 0.0),

	("town_mercenary_dhorak", mcn_no_shadow, "Westeros_Town_Red", 0.35, snd_click, 0.0, 0.0, 0.0),

	("town_swadia_praven", mcn_no_shadow, "Westeros_Town_Red", 0.35, snd_click, 0.0, 0.0, 0.0),

	("town_swadia_dhirim", mcn_no_shadow, "Westeros_Town_Red", 0.35, snd_click, 0.0, 0.0, 0.0),

	("town_swadia_suno", mcn_no_shadow, "Westeros_Town_Red", 0.35, snd_click, 0.0, 0.0, 0.0),

	("town_swadia_uxkhal", mcn_no_shadow, "Westeros_Town_Red", 0.35, snd_click, 0.0, 0.0, 0.0),

	("town_vaegir_curaw", mcn_no_shadow, "map_town_snow_a", 0.35, snd_click, 0.0, 0.0, 0.0),

	("town_vaegir_khudan", mcn_no_shadow, "map_town_vaegir_khudan", 0.35, snd_click, 0.0, 0.0, 0.0),

	("town_vaegir_reyvadin", mcn_no_shadow, "Westeros_Town_Red", 0.35, snd_click, 0.0, 0.0, 0.0),

	("town_vaegir_rivacheg", mcn_no_shadow, "map_town_a", 0.35, snd_click, 0.0, 0.0, 0.0),

	("town_khergit_halmar", mcn_no_shadow, "map_town_khergit_halmar", 0.35, snd_click, 0.0, 0.0, 0.0),

	("town_khergit_ichamur", mcn_no_shadow, "map_town_khergit_ichamur", 0.35, snd_click, 0.0, 0.0, 0.0),

	("town_khergit_narra", mcn_no_shadow, "map_town_khergit_narra", 0.35, snd_click, 0.0, 0.0, 0.0),

	("town_khergit_tulga", mcn_no_shadow, "map_town_khergit_tulga", 0.35, snd_click, 0.0, 0.0, 0.0),

	("town_nord_tihr", mcn_no_shadow, "map_town_nord_tihr", 0.35, snd_click, 0.0, 0.0, 0.0),

	("town_nord_sargoth", mcn_no_shadow, "map_town_a", 0.35, snd_click, 0.0, 0.0, 0.0),

	("town_nord_wercheg", mcn_no_shadow, "map_town_a", 0.35, snd_click, 0.0, 0.0, 0.0),

	("town_rhodok_jelkala", mcn_no_shadow, "map_town_a", 0.35, snd_click, 0.0, 0.0, 0.0),

	("town_rhodok_veluca", mcn_no_shadow, "map_town_a", 0.35, snd_click, 0.0, 0.0, 0.0),

	("town_rhodok_yalen", mcn_no_shadow, "map_town_a", 0.35, snd_click, 0.0, 0.0, 0.0),

	("town_sarranid_ahmerrad", mcn_no_shadow, "map_town_desert_a", 0.35, snd_click, 0.0, 0.0, 0.0),

	("town_sarranid_bariyye", mcn_no_shadow, "map_town_desert_a", 0.35, snd_click, 0.0, 0.0, 0.0),

	("town_sarranid_durquba", mcn_no_shadow, "map_town_desert_a", 0.35, snd_click, 0.0, 0.0, 0.0),

	("town_sarranid_shariz", mcn_no_shadow, "map_town_steppe_a", 0.35, snd_click, 0.0, 0.0, 0.0),

	("village_a", mcn_no_shadow, "map_village_a", 0.45, snd_click, 0.0, 0.0, 0.0),

	("village_b", mcn_no_shadow, "map_village_b", 0.45, snd_click, 0.0, 0.0, 0.0),

	("village_c", mcn_no_shadow, "map_village_c", 0.45, snd_click, 0.0, 0.0, 0.0),

	("village_burnt_a", mcn_no_shadow, "map_village_burnt_a", 0.45, snd_click, 0.0, 0.0, 0.0),

	("village_deserted_a", mcn_no_shadow, "map_village_deserted_a", 0.45, snd_click, 0.0, 0.0, 0.0),

	("village_burnt_b", mcn_no_shadow, "map_village_burnt_b", 0.45, snd_click, 0.0, 0.0, 0.0),

	("village_deserted_b", mcn_no_shadow, "map_village_deserted_b", 0.45, snd_click, 0.0, 0.0, 0.0),

	("village_burnt_c", mcn_no_shadow, "map_village_burnt_c", 0.45, snd_click, 0.0, 0.0, 0.0),

	("village_deserted_c", mcn_no_shadow, "map_village_deserted_c", 0.45, snd_click, 0.0, 0.0, 0.0),

	("village_snow_a", mcn_no_shadow, "map_village_snow_a", 0.45, snd_click, 0.0, 0.0, 0.0),

	("village_snow_burnt_a", mcn_no_shadow, "map_village_snow_burnt_a", 0.45, snd_click, 0.0, 0.0, 0.0),

	("village_snow_deserted_a", mcn_no_shadow, "map_village_snow_deserted_a", 0.45, snd_click, 0.0, 0.0, 0.0),

	("bandit_lair", mcn_no_shadow, "map_bandit_lair", 0.45, snd_click, 0.0, 0.0, 0.0),

	("camp_tent", mcn_no_shadow, "map_camp_tent", 0.13, snd_click, 0.0, 0.0, 0.0),

	("camp_plain", 0, "map_camp_plain", 1.0, snd_click, 0.0, 0.0, 0.0),

	("camp_entrench", 0, "map_camp_entrench", 1.0, snd_click, 0.0, 0.0, 0.0),

	("camp_entrench_last", 0, "map_camp_entrench_last", 1.0, snd_click, 0.0, 0.0, 0.0),

	("camp_funeral_pyre", 0, "map_camp_funeral_pyre", 1.0, snd_click, 0.0, 0.0, 0.0),

	("ship", mcn_no_shadow, "map_ship_sail_on", 0.23, snd_footstep_grass, 0.0, 0.05, 0.0),

	("ship_on_land", mcn_no_shadow, "map_ship_sail_off", 0.23, snd_click, 0.0, 0.0, 0.0),

	("ship_khergit", mcn_no_shadow, "map_ship_khergit", 0.23, snd_footstep_grass, 0.0, 0.05, 0.0),

	("ship_khergit_on_land", mcn_no_shadow, "map_ship_khergit", 0.23, snd_click, 0.0, 0.0, 0.0),

	("ship_harbour", mcn_no_shadow, "map_ship_harbour", 0.24, snd_click, 0.0, 0.0, 0.0),

	("training_ground_a", mcn_no_shadow, "training", 0.35, snd_click, 0.0, 0.0, 0.0),

	("training_ground_b", mcn_no_shadow, "map_training_ground_b", 0.35, snd_click, 0.0, 0.0, 0.0),

	("wall_khergit_a", mcn_no_shadow, "map_wall_khergit_a", 0.35, snd_click, 0.0, 0.0, 0.0),

	("wall_khergit_b", mcn_no_shadow, "map_wall_khergit_b", 0.35, snd_click, 0.0, 0.0, 0.0),

	("wall_khergit_c", mcn_no_shadow, "map_wall_khergit_c", 0.35, snd_click, 0.0, 0.0, 0.0),

	("wall_khergit_d", mcn_no_shadow, "map_wall_khergit_d", 0.35, snd_click, 0.0, 0.0, 0.0),

	("castle_derchios", mcn_no_shadow, "map_castle_pevensey", 0.45, snd_click, 0.0, 0.0, 0.0),

	("castle_haringoth", mcn_no_shadow, "map_castle_haringoth", 0.45, snd_click, 0.0, 0.0, 0.0),

	("castle_kelredan", mcn_no_shadow, "map_castle_kelredan", 0.45, snd_click, 0.0, 0.0, 0.0),

	("castle_reindi", mcn_no_shadow, "map_castle_beaumaris", 0.45, snd_click, 0.0, 0.0, 0.0),

	("castle_rindyar", mcn_no_shadow, "map_castle_rindyar", 0.45, snd_click, 0.0, 0.0, 0.0),

	("castle_ryibelet", mcn_no_shadow, "map_castle_ryibelet", 0.45, snd_click, 0.0, 0.0, 0.0),

	("castle_senuzgda", mcn_no_shadow, "map_castle_york", 0.45, snd_click, 0.0, 0.0, 0.0),

	("castle_tevarin", mcn_no_shadow, "map_castle_muiderslot", 0.45, snd_click, 0.0, 0.0, 0.0),

	("castle_tilbaut", mcn_no_shadow, "map_castle_llansteffan", 0.45, snd_click, 0.0, 0.0, 0.0),

	("castle_vyincourd", mcn_no_shadow, "map_castle_hillfort", 0.45, snd_click, 0.0, 0.0, 0.0),

	("castle_bulugha", mcn_no_shadow, "map_castle_hillfort", 0.45, snd_click, 0.0, 0.0, 0.0),

	("castle_dramug", mcn_no_shadow, "map_castle_carlisle", 0.45, snd_click, 0.0, 0.0, 0.0),

	("castle_ismirala", mcn_no_shadow, "map_castle_ismirala", 0.45, snd_click, 0.0, 0.0, 0.0),

	("castle_jeirbe", mcn_no_shadow, "map_castle_jeirbe", 0.45, snd_click, 0.0, 0.0, 0.0),

	("castle_nelag", mcn_no_shadow, "map_castle_nelag", 0.45, snd_click, 0.0, 0.0, 0.0),

	("castle_radoghir", mcn_no_shadow, "map_castle_radoghir", 0.45, snd_click, 0.0, 0.0, 0.0),

	("castle_slezkh", mcn_no_shadow, "map_castle_slezkh", 0.45, snd_click, 0.0, 0.0, 0.0),

	("castle_yruma", mcn_no_shadow, "map_castle_yruma", 0.45, snd_click, 0.0, 0.0, 0.0),

	("castle_asugan", mcn_no_shadow, "map_castle_asugan", 0.45, snd_click, 0.0, 0.0, 0.0),

	("castle_distar", mcn_no_shadow, "map_castle_distar", 0.45, snd_click, 0.0, 0.0, 0.0),

	("castle_malayurg", mcn_no_shadow, "map_castle_malayurg", 0.5, snd_click, 0.0, 0.0, 0.0),

	("castle_sungetche", mcn_no_shadow, "map_castle_sungetche", 0.45, snd_click, 0.0, 0.0, 0.0),

	("castle_tulbuk", mcn_no_shadow, "map_castle_tulbuk", 0.45, snd_click, 0.0, 0.0, 0.0),

	("castle_uhhun", mcn_no_shadow, "map_castle_uhhun", 0.45, snd_click, 0.0, 0.0, 0.0),

	("castle_unuzdaq", mcn_no_shadow, "map_castle_unuzdaq", 0.45, snd_click, 0.0, 0.0, 0.0),

	("castle_alburq", mcn_no_shadow, "map_castle_alburq", 0.45, snd_click, 0.0, 0.0, 0.0),

	("castle_chalbek", mcn_no_shadow, "map_castle_hillfort", 0.45, snd_click, 0.0, 0.0, 0.0),

	("castle_curin", mcn_no_shadow, "map_castle_curin", 0.45, snd_click, 0.0, 0.0, 0.0),

	("castle_hrus", mcn_no_shadow, "map_castle_hrus", 0.45, snd_click, 0.0, 0.0, 0.0),

	("castle_jelbegi", mcn_no_shadow, "map_castle_jelbegi", 0.45, snd_click, 0.0, 0.0, 0.0),

	("castle_knudarr", mcn_no_shadow, "map_castle_knudarr", 0.45, snd_click, 0.0, 0.0, 0.0),

	("castle_tehlrog", mcn_no_shadow, "map_castle_tehlrog", 0.45, snd_click, 0.0, 0.0, 0.0),

	("castle_almerra", mcn_no_shadow, "map_castle_almerra", 0.45, snd_click, 0.0, 0.0, 0.0),

	("castle_culmarr", mcn_no_shadow, "map_castle_culmarr", 0.45, snd_click, 0.0, 0.0, 0.0),

	("castle_ergellon", mcn_no_shadow, "map_castle_ergellon", 0.45, snd_click, 0.0, 0.0, 0.0),

	("castle_etrosq", mcn_no_shadow, "map_castle_etrosq", 0.45, snd_click, 0.0, 0.0, 0.0),

	("castle_grunwalder", mcn_no_shadow, "map_castle_conwy", 0.58, snd_click, 0.0, 0.0, 0.0),

	("castle_ibdeles", mcn_no_shadow, "map_castle_ibdeles", 0.45, snd_click, 0.0, 0.0, 0.0),

	("castle_jamiche", mcn_no_shadow, "map_castle_jamiche", 0.45, snd_click, 0.0, 0.0, 0.0),

	("castle_maras", mcn_no_shadow, "map_castle_maras", 0.45, snd_click, 0.0, 0.0, 0.0),

	("castle_bardaq", mcn_no_shadow, "map_castle_bardaq", 0.45, snd_click, 0.0, 0.0, 0.0),

	("castle_caraf", mcn_no_shadow, "map_castle_caraf", 0.45, snd_click, 0.0, 0.0, 0.0),

	("castle_durrin", mcn_no_shadow, "map_castle_durrin", 0.45, snd_click, 0.0, 0.0, 0.0),

	("castle_jameyyed", mcn_no_shadow, "map_castle_jameyyed", 0.45, snd_click, 0.0, 0.0, 0.0),

	("castle_samarra", mcn_no_shadow, "map_castle_samarra", 0.45, snd_click, 0.0, 0.0, 0.0),

	("castle_sharwa", mcn_no_shadow, "map_castle_sharwa", 0.45, snd_click, 0.0, 0.0, 0.0),

	("castle_teramma", mcn_no_shadow, "map_castle_teramma", 0.45, snd_click, 0.0, 0.0, 0.0),

	("castle_weyyah", mcn_no_shadow, "map_castle_weyyah", 0.45, snd_click, 0.0, 0.0, 0.0),

	("map_town_wood", mcn_no_shadow, "map_town_wood", 0.45, snd_click, 0.0, 0.0, 0.0),

	("map_casterly_rock", mcn_no_shadow, "Casterly_Rock", 0.45, snd_click, 0.0, 0.0, 0.0),

	("map_dragonstone", mcn_no_shadow, "Dragonstone", 0.45, snd_click, 0.0, 0.0, 0.0),

	("map_eyrie", mcn_no_shadow, "Eyrie", 0.45, snd_click, 0.0, 0.0, 0.0),

	("map_harrenhal", mcn_no_shadow, "Harrenhal", 0.45, snd_click, 0.0, 0.0, 0.0),

	("map_highgarden", mcn_no_shadow, "Highgarden", 0.45, snd_click, 0.0, 0.0, 0.0),

	("map_kings_landing", mcn_no_shadow, "Kings_Landing", 0.45, snd_click, 0.0, 0.0, 0.0),

	("map_lannisport", mcn_no_shadow, "Lannisport", 0.45, snd_click, 0.0, 0.0, 0.0),

	("map_moat_cailin", mcn_no_shadow, "Moat_Cailin", 0.6, snd_click, 0.0, 0.0, 0.0),

	("map_oldtown", mcn_no_shadow, "Oldtown", 0.45, snd_click, 0.0, 0.0, 0.0),

	("map_pyke", mcn_no_shadow, "Pyke", 0.45, snd_click, 0.0, 0.0, 0.0),

	("map_riverrun", mcn_no_shadow, "Riverrun", 0.45, snd_click, 0.0, 0.0, 0.0),

	("map_storms_end", mcn_no_shadow, "Storms_End", 0.45, snd_click, 0.0, 0.0, 0.0),

	("map_twins", mcn_no_shadow, "Twins", 0.45, snd_click, 0.0, 0.0, 0.0),

	("map_castle_red", mcn_no_shadow, "Westeros_Castle_Red", 0.45, snd_click, 0.0, 0.0, 0.0),

	("map_castle_grey", mcn_no_shadow, "Westeros_Castle_Grey", 0.45, snd_click, 0.0, 0.0, 0.0),

	("map_castle_white", mcn_no_shadow, "Westeros_Castle_White", 0.45, snd_click, 0.0, 0.0, 0.0),

	("map_town_red", mcn_no_shadow, "Westeros_Town_Red", 0.45, snd_click, 0.0, 0.0, 0.0),

	("map_town_grey", mcn_no_shadow, "Westeros_Town_Grey", 0.45, snd_click, 0.0, 0.0, 0.0),

	("map_town_white", mcn_no_shadow, "Westeros_Town_White", 0.45, snd_click, 0.0, 0.0, 0.0),

	("map_white_harbor", mcn_no_shadow, "White_Harbor", 0.45, snd_click, 0.0, 0.0, 0.0),

	("map_winterfell", mcn_no_shadow, "Winterfell", 0.45, snd_click, 0.0, 0.0, 0.0),

	("map_dorne_castle", mcn_no_shadow, "Dorne_Castle", 0.45, snd_click, 0.0, 0.0, 0.0),

	("map_dorne_town", mcn_no_shadow, "Dorne_Town", 0.45, snd_click, 0.0, 0.0, 0.0),

	("map_sunspear", mcn_no_shadow, "Sunspear", 0.45, snd_click, 0.0, 0.0, 0.0),

	("map_essos_castle", mcn_no_shadow, "Essos_Castle", 0.45, snd_click, 0.0, 0.0, 0.0),

	("map_essos_town", mcn_no_shadow, "Essos_Town", 0.45, snd_click, 0.0, 0.0, 0.0),

	("map_essos_castle2", mcn_no_shadow, "Essos_Castle2", 0.45, snd_click, 0.0, 0.0, 0.0),

	("map_essos_castle3", mcn_no_shadow, "Essos_Castle3", 0.45, snd_click, 0.0, 0.0, 0.0),

	("map_essos_town2", mcn_no_shadow, "Essos_Town2", 0.45, snd_click, 0.0, 0.0, 0.0),

	("map_essos_town3", mcn_no_shadow, "Essos_Town3", 0.45, snd_click, 0.0, 0.0, 0.0),

	("map_braavos", mcn_no_shadow, "Braavos", 0.45, snd_click, 0.0, 0.0, 0.0),

	("map_lys", mcn_no_shadow, "Lys", 0.45, snd_click, 0.0, 0.0, 0.0),

	("map_myr", mcn_no_shadow, "Myr", 0.45, snd_click, 0.0, 0.0, 0.0),

	("map_pentos", mcn_no_shadow, "Pentos", 0.45, snd_click, 0.0, 0.0, 0.0),

	("map_tyrosh", mcn_no_shadow, "Tyrosh", 0.45, snd_click, 0.0, 0.0, 0.0),

	("map_bloody_gate", mcn_no_shadow, "Bloody_Gate", 0.45, snd_click, 0.0, 0.0, 0.0),

	("map_norvos", mcn_no_shadow, "Norvos", 0.45, snd_click, 0.0, 0.0, 0.0),

	("map_volantis", mcn_no_shadow, "Volantis", 0.45, snd_click, 0.0, 0.0, 0.0),

	("map_last_hearth", mcn_no_shadow, "Last_Hearth", 0.45, snd_click, 0.0, 0.0, 0.0),

	("map_deepwood_motte", mcn_no_shadow, "Deepwood_Motte", 0.45, snd_click, 0.0, 0.0, 0.0),

	("map_dreadfort", mcn_no_shadow, "Dreadfort", 0.45, snd_click, 0.0, 0.0, 0.0),

	("map_golden_tooth", mcn_no_shadow, "Golden_Tooth", 0.45, snd_click, 0.0, 0.0, 0.0),

	("map_runestone", mcn_no_shadow, "Runestone", 0.45, snd_click, 0.0, 0.0, 0.0),

	("map_tarbeck_hall", mcn_no_shadow, "Tarbeck_Hall", 0.45, snd_click, 0.0, 0.0, 0.0),

	("map_yronwood", mcn_no_shadow, "Yronwood", 0.45, snd_click, 0.0, 0.0, 0.0),

	("map_ten_towers", mcn_no_shadow, "Ten_Towers", 0.45, snd_click, 0.0, 0.0, 0.0),

	("map_ntb_wood", mcn_no_shadow, "map_icon_wood", 0.45, snd_click, 0.0, 0.0, 0.0),

	("map_lighthouse", mcn_no_shadow, "Lighthouse", 0.55, snd_click, 0.0, 0.0, 0.0),

	("map_lighthouse_ship", mcn_no_shadow, "Ship_Lighthouse", 0.55, snd_click, 0.0, 0.0, 0.0),

	("map_lighthouse_ship_2", mcn_no_shadow, "Ship_Lighthouse_2", 0.55, snd_click, 0.0, 0.0, 0.0),

	("map_lighthouse_grey", mcn_no_shadow, "Lighthouse_2_grey", 0.55, snd_click, 0.0, 0.0, 0.0),

	("map_lighthouse_white", mcn_no_shadow, "Lighthouse_2_white", 0.55, snd_click, 0.0, 0.0, 0.0),

	("map_lighthouse_red", mcn_no_shadow, "Lighthouse_2_red", 0.55, snd_click, 0.0, 0.0, 0.0),

	("map_lighthouse_dorne", mcn_no_shadow, "Lighthouse_2_dorne", 0.55, snd_click, 0.0, 0.0, 0.0),

	("map_lighthouse_essos", mcn_no_shadow, "Lighthouse_2_essos", 0.55, snd_click, 0.0, 0.0, 0.0),

	("map_seagard", mcn_no_shadow, "Seagard", 0.45, snd_click, 0.0, 0.0, 0.0),

	("map_lorath", mcn_no_shadow, "Lorath", 0.45, snd_click, 0.0, 0.0, 0.0),

	("map_castle_wood_what", mcn_no_shadow, "map_castle_c", 0.38, snd_click, 0.0, 0.0, 0.0),

	("map_castle_wood_what2", mcn_no_shadow, "map_castle_e", 0.38, snd_click, 0.0, 0.0, 0.0),

	("map_lighthouse_essos2", mcn_no_shadow, "Lighthouse_2_essos2", 0.38, snd_click, 0.0, 0.0, 0.0),

	("map_arbor", mcn_no_shadow, "Arbor", 0.45, snd_click, 0.0, 0.0, 0.0),

	("map_stoney_sept", mcn_no_shadow, "Stoney_Sept", 0.45, snd_click, 0.0, 0.0, 0.0),

	("map_saltpans", mcn_no_shadow, "Saltpans", 0.45, snd_click, 0.0, 0.0, 0.0),

	("map_gulltown", mcn_no_shadow, "Gulltown", 0.45, snd_click, 0.0, 0.0, 0.0),

	("map_queenscrown", mcn_no_shadow, "Queenscrown", 0.45, snd_click, 0.0, 0.0, 0.0),

	("map_Ruined_Castle", mcn_no_shadow, "Ruined_Castle", 0.45, snd_click, 0.0, 0.0, 0.0),

	("map_Ruined_Town", mcn_no_shadow, "Ruined_Town", 0.45, snd_click, 0.0, 0.0, 0.0),

	("map_Clegane_Keep", mcn_no_shadow, "Clegane_Keep", 0.45, snd_click, 0.0, 0.0, 0.0),

	("map_Rodgars_Hut", mcn_no_shadow, "rodgars_hut", 0.45, snd_click, 0.0, 0.0, 0.0),

	("map_monastery", mcn_no_shadow, "map_monastery", 0.45, snd_click, 0.0, 0.0, 0.0),

	("map_the_sorrows", mcn_no_shadow, "the_sorrows", 0.45, snd_click, 0.0, 0.0, 0.0),

	("map_nw_castle", mcn_no_shadow, "nw_castle", 0.45, snd_click, 0.0, 0.0, 0.0),

	("ford_1", mcn_no_shadow, "ford_1", 0.45, snd_click, 0.0, 0.0, 0.0),

	("ford_2", mcn_no_shadow, "ford_2", 0.45, snd_click, 0.0, 0.0, 0.0),

	("ford_3", mcn_no_shadow, "ford_3", 0.45, snd_click, 0.0, 0.0, 0.0),

	("ford_4", mcn_no_shadow, "ford_4", 0.45, snd_click, 0.0, 0.0, 0.0),

	("ford_5", mcn_no_shadow, "ford_5", 0.45, snd_click, 0.0, 0.0, 0.0),

	("ford_6", mcn_no_shadow, "ford_6", 0.45, snd_click, 0.0, 0.0, 0.0),

	("volcano_rocks", mcn_no_shadow, "volcano_rocks", 0.45, snd_click, 0.0, 0.0, 0.0),

	("map_barrow", mcn_no_shadow, "map_barrow", 0.45, snd_click, 0.0, 0.0, 0.0),

	("map_tree_a", mcn_no_shadow, "map_tree_a", 0.45, snd_click, 0.0, 0.0, 0.0),

	("beach_rocks", mcn_no_shadow, "beach_rocks", 0.45, snd_click, 0.0, 0.0, 0.0),

	("map_weirwood", mcn_no_shadow, "map_weirwood", 0.45, snd_click, 0.0, 0.0, 0.0),

	("map_farmland", mcn_no_shadow, "map_farmland", 0.45, snd_click, 0.0, 0.0, 0.0),

	("map_old_mill", mcn_no_shadow, "map_old_mill", 0.45, snd_click, 0.0, 0.0, 0.0),

	("map_abandoned_village", mcn_no_shadow, "map_village_deserted_a", 0.45, snd_click, 0.0, 0.0, 0.0),

	("map_forest_bog", mcn_no_shadow, "map_forest_bog", 0.45, snd_click, 0.0, 0.0, 0.0),

	("bridge_a", mcn_no_shadow, "map_river_bridge_a", 0.8, snd_click, 0.0, 0.0, 0.0),

	("bridge_b", mcn_no_shadow, "map_river_bridge_b", 0.8, snd_click, 0.0, 0.0, 0.0),

	("bridge_c", mcn_no_shadow, "map_river_bridge_c", 1.27, snd_click, 0.0, 0.0, 0.0),

	("bridge_snow_a", mcn_no_shadow, "map_river_bridge_snow_a", 0.7, snd_click, 0.0, 0.0, 0.0),

	("bridge_snow_b", mcn_no_shadow, "map_river_bridge_snow_a", 1.27, snd_click, 0.0, 0.0, 0.0),

	("outpost", mcn_no_shadow, "map_outpost", 0.22, snd_click, 0.0, 0.0, 0.0),

	("fort_a", mcn_no_shadow, "map_castle_e", 0.22, snd_click, 0.0, 0.0, 0.0),

	("custom_banner_01", 0, "custom_map_banner_01", banner_scale, snd_click, 0.0, 0.0, 0.0, 
	[(ti_on_init_map_icon,
		[
			(store_trigger_param_1, ":trigger_param_1"),
			(party_get_slot, ":trigger_param_1_town_lord", ":trigger_param_1", slot_town_lord),
			(try_begin),
				(ge, ":trigger_param_1_town_lord", 0),
				(cur_map_icon_set_tableau_material, "tableau_custom_banner_square", ":trigger_param_1_town_lord"),
			(try_end)
		])]
	),

	("custom_banner_02", 0, "custom_map_banner_02", banner_scale, snd_click, 0.0, 0.0, 0.0, 
	[(ti_on_init_map_icon,
		[
			(store_trigger_param_1, ":trigger_param_1"),
			(party_get_slot, ":trigger_param_1_town_lord", ":trigger_param_1", slot_town_lord),
			(try_begin),
				(ge, ":trigger_param_1_town_lord", 0),
				(cur_map_icon_set_tableau_material, "tableau_custom_banner_short", ":trigger_param_1_town_lord"),
			(try_end)
		])]
	),

	("custom_banner_03", 0, "custom_map_banner_03", banner_scale, snd_click, 0.0, 0.0, 0.0, 
	[(ti_on_init_map_icon,
		[
			(store_trigger_param_1, ":trigger_param_1"),
			(party_get_slot, ":trigger_param_1_town_lord", ":trigger_param_1", slot_town_lord),
			(try_begin),
				(ge, ":trigger_param_1_town_lord", 0),
				(cur_map_icon_set_tableau_material, "tableau_custom_banner_tall", ":trigger_param_1_town_lord"),
			(try_end)
		])]
	),

	("banner_01", 0, "map_flag_01", banner_scale, snd_click, 0.0, 0.0, 0.0),

	("banner_02", 0, "map_flag_02", banner_scale, snd_click, 0.0, 0.0, 0.0),

	("banner_03", 0, "map_flag_03", banner_scale, snd_click, 0.0, 0.0, 0.0),

	("banner_04", 0, "map_flag_04", banner_scale, snd_click, 0.0, 0.0, 0.0),

	("banner_05", 0, "map_flag_05", banner_scale, snd_click, 0.0, 0.0, 0.0),

	("banner_06", 0, "map_flag_06", banner_scale, snd_click, 0.0, 0.0, 0.0),

	("banner_07", 0, "map_flag_07", banner_scale, snd_click, 0.0, 0.0, 0.0),

	("banner_08", 0, "map_flag_08", banner_scale, snd_click, 0.0, 0.0, 0.0),

	("banner_09", 0, "map_flag_09", banner_scale, snd_click, 0.0, 0.0, 0.0),

	("banner_10", 0, "map_flag_10", banner_scale, snd_click, 0.0, 0.0, 0.0),

	("banner_11", 0, "map_flag_11", banner_scale, snd_click, 0.0, 0.0, 0.0),

	("banner_12", 0, "map_flag_12", banner_scale, snd_click, 0.0, 0.0, 0.0),

	("banner_13", 0, "map_flag_13", banner_scale, snd_click, 0.0, 0.0, 0.0),

	("banner_14", 0, "map_flag_14", banner_scale, snd_click, 0.0, 0.0, 0.0),

	("banner_15", 0, "map_flag_15", banner_scale, snd_click, 0.0, 0.0, 0.0),

	("banner_16", 0, "map_flag_16", banner_scale, snd_click, 0.0, 0.0, 0.0),

	("banner_17", 0, "map_flag_17", banner_scale, snd_click, 0.0, 0.0, 0.0),

	("banner_18", 0, "map_flag_18", banner_scale, snd_click, 0.0, 0.0, 0.0),

	("banner_19", 0, "map_flag_19", banner_scale, snd_click, 0.0, 0.0, 0.0),

	("banner_20", 0, "map_flag_20", banner_scale, snd_click, 0.0, 0.0, 0.0),

	("banner_21", 0, "map_flag_21", banner_scale, snd_click, 0.0, 0.0, 0.0),

	("banner_22", 0, "map_flag_22", banner_scale, snd_click, 0.0, 0.0, 0.0),

	("banner_23", 0, "map_flag_23", banner_scale, snd_click, 0.0, 0.0, 0.0),

	("banner_24", 0, "map_flag_24", banner_scale, snd_click, 0.0, 0.0, 0.0),

	("banner_25", 0, "map_flag_25", banner_scale, snd_click, 0.0, 0.0, 0.0),

	("banner_26", 0, "map_flag_26", banner_scale, snd_click, 0.0, 0.0, 0.0),

	("banner_27", 0, "map_flag_27", banner_scale, snd_click, 0.0, 0.0, 0.0),

	("banner_28", 0, "map_flag_28", banner_scale, snd_click, 0.0, 0.0, 0.0),

	("banner_29", 0, "map_flag_29", banner_scale, snd_click, 0.0, 0.0, 0.0),

	("banner_30", 0, "map_flag_30", banner_scale, snd_click, 0.0, 0.0, 0.0),

	("banner_31", 0, "map_flag_31", banner_scale, snd_click, 0.0, 0.0, 0.0),

	("banner_32", 0, "map_flag_32", banner_scale, snd_click, 0.0, 0.0, 0.0),

	("banner_33", 0, "map_flag_33", banner_scale, snd_click, 0.0, 0.0, 0.0),

	("banner_34", 0, "map_flag_34", banner_scale, snd_click, 0.0, 0.0, 0.0),

	("banner_35", 0, "map_flag_35", banner_scale, snd_click, 0.0, 0.0, 0.0),

	("banner_36", 0, "map_flag_36", banner_scale, snd_click, 0.0, 0.0, 0.0),

	("banner_37", 0, "map_flag_37", banner_scale, snd_click, 0.0, 0.0, 0.0),

	("banner_38", 0, "map_flag_38", banner_scale, snd_click, 0.0, 0.0, 0.0),

	("banner_39", 0, "map_flag_39", banner_scale, snd_click, 0.0, 0.0, 0.0),

	("banner_40", 0, "map_flag_40", banner_scale, snd_click, 0.0, 0.0, 0.0),

	("banner_41", 0, "map_flag_41", banner_scale, snd_click, 0.0, 0.0, 0.0),

	("banner_42", 0, "map_flag_42", banner_scale, snd_click, 0.0, 0.0, 0.0),

	("banner_43", 0, "map_flag_43", banner_scale, snd_click, 0.0, 0.0, 0.0),

	("banner_44", 0, "map_flag_44", banner_scale, snd_click, 0.0, 0.0, 0.0),

	("banner_45", 0, "map_flag_45", banner_scale, snd_click, 0.0, 0.0, 0.0),

	("banner_46", 0, "map_flag_46", banner_scale, snd_click, 0.0, 0.0, 0.0),

	("banner_47", 0, "map_flag_47", banner_scale, snd_click, 0.0, 0.0, 0.0),

	("banner_48", 0, "map_flag_48", banner_scale, snd_click, 0.0, 0.0, 0.0),

	("banner_49", 0, "map_flag_49", banner_scale, snd_click, 0.0, 0.0, 0.0),

	("banner_50", 0, "map_flag_50", banner_scale, snd_click, 0.0, 0.0, 0.0),

	("banner_51", 0, "map_flag_51", banner_scale, snd_click, 0.0, 0.0, 0.0),

	("banner_52", 0, "map_flag_52", banner_scale, snd_click, 0.0, 0.0, 0.0),

	("banner_53", 0, "map_flag_53", banner_scale, snd_click, 0.0, 0.0, 0.0),

	("banner_54", 0, "map_flag_54", banner_scale, snd_click, 0.0, 0.0, 0.0),

	("banner_55", 0, "map_flag_55", banner_scale, snd_click, 0.0, 0.0, 0.0),

	("banner_56", 0, "map_flag_56", banner_scale, snd_click, 0.0, 0.0, 0.0),

	("banner_57", 0, "map_flag_57", banner_scale, snd_click, 0.0, 0.0, 0.0),

	("banner_58", 0, "map_flag_58", banner_scale, snd_click, 0.0, 0.0, 0.0),

	("banner_59", 0, "map_flag_59", banner_scale, snd_click, 0.0, 0.0, 0.0),

	("banner_60", 0, "map_flag_60", banner_scale, snd_click, 0.0, 0.0, 0.0),

	("banner_61", 0, "map_flag_61", banner_scale, snd_click, 0.0, 0.0, 0.0),

	("banner_62", 0, "map_flag_62", banner_scale, snd_click, 0.0, 0.0, 0.0),

	("banner_63", 0, "map_flag_63", banner_scale, snd_click, 0.0, 0.0, 0.0),

	("banner_64", 0, "map_flag_d01", banner_scale, snd_click, 0.0, 0.0, 0.0),

	("banner_65", 0, "map_flag_d02", banner_scale, snd_click, 0.0, 0.0, 0.0),

	("banner_66", 0, "map_flag_d03", banner_scale, snd_click, 0.0, 0.0, 0.0),

	("banner_67", 0, "map_flag_d04", banner_scale, snd_click, 0.0, 0.0, 0.0),

	("banner_68", 0, "map_flag_d05", banner_scale, snd_click, 0.0, 0.0, 0.0),

	("banner_69", 0, "map_flag_d06", banner_scale, snd_click, 0.0, 0.0, 0.0),

	("banner_70", 0, "map_flag_d07", banner_scale, snd_click, 0.0, 0.0, 0.0),

	("banner_71", 0, "map_flag_d08", banner_scale, snd_click, 0.0, 0.0, 0.0),

	("banner_72", 0, "map_flag_d09", banner_scale, snd_click, 0.0, 0.0, 0.0),

	("banner_73", 0, "map_flag_d10", banner_scale, snd_click, 0.0, 0.0, 0.0),

	("banner_74", 0, "map_flag_d11", banner_scale, snd_click, 0.0, 0.0, 0.0),

	("banner_75", 0, "map_flag_d12", banner_scale, snd_click, 0.0, 0.0, 0.0),

	("banner_76", 0, "map_flag_d13", banner_scale, snd_click, 0.0, 0.0, 0.0),

	("banner_77", 0, "map_flag_d14", banner_scale, snd_click, 0.0, 0.0, 0.0),

	("banner_78", 0, "map_flag_d15", banner_scale, snd_click, 0.0, 0.0, 0.0),

	("banner_79", 0, "map_flag_d16", banner_scale, snd_click, 0.0, 0.0, 0.0),

	("banner_80", 0, "map_flag_d17", banner_scale, snd_click, 0.0, 0.0, 0.0),

	("banner_81", 0, "map_flag_d18", banner_scale, snd_click, 0.0, 0.0, 0.0),

	("banner_82", 0, "map_flag_d19", banner_scale, snd_click, 0.0, 0.0, 0.0),

	("banner_83", 0, "map_flag_d20", banner_scale, snd_click, 0.0, 0.0, 0.0),

	("banner_84", 0, "map_flag_d21", banner_scale, snd_click, 0.0, 0.0, 0.0),

	("banner_85", 0, "map_flag_e01", banner_scale, snd_click, 0.0, 0.0, 0.0),

	("banner_86", 0, "map_flag_e02", banner_scale, snd_click, 0.0, 0.0, 0.0),

	("banner_87", 0, "map_flag_e03", banner_scale, snd_click, 0.0, 0.0, 0.0),

	("banner_88", 0, "map_flag_e04", banner_scale, snd_click, 0.0, 0.0, 0.0),

	("banner_89", 0, "map_flag_e05", banner_scale, snd_click, 0.0, 0.0, 0.0),

	("banner_90", 0, "map_flag_e06", banner_scale, snd_click, 0.0, 0.0, 0.0),

	("banner_91", 0, "map_flag_e07", banner_scale, snd_click, 0.0, 0.0, 0.0),

	("banner_92", 0, "map_flag_e08", banner_scale, snd_click, 0.0, 0.0, 0.0),

	("banner_93", 0, "map_flag_e09", banner_scale, snd_click, 0.0, 0.0, 0.0),

	("banner_94", 0, "map_flag_e10", banner_scale, snd_click, 0.0, 0.0, 0.0),

	("banner_95", 0, "map_flag_e11", banner_scale, snd_click, 0.0, 0.0, 0.0),

	("banner_96", 0, "map_flag_e12", banner_scale, snd_click, 0.0, 0.0, 0.0),

	("banner_97", 0, "map_flag_e13", banner_scale, snd_click, 0.0, 0.0, 0.0),

	("banner_98", 0, "map_flag_e14", banner_scale, snd_click, 0.0, 0.0, 0.0),

	("banner_99", 0, "map_flag_e15", banner_scale, snd_click, 0.0, 0.0, 0.0),

	("banner_100", 0, "map_flag_e16", banner_scale, snd_click, 0.0, 0.0, 0.0),

	("banner_101", 0, "map_flag_e17", banner_scale, snd_click, 0.0, 0.0, 0.0),

	("banner_102", 0, "map_flag_e18", banner_scale, snd_click, 0.0, 0.0, 0.0),

	("banner_103", 0, "map_flag_e19", banner_scale, snd_click, 0.0, 0.0, 0.0),

	("banner_104", 0, "map_flag_e20", banner_scale, snd_click, 0.0, 0.0, 0.0),

	("banner_105", 0, "map_flag_e21", banner_scale, snd_click, 0.0, 0.0, 0.0),

	("banner_106", 0, "map_flag_f01", banner_scale, snd_click, 0.0, 0.0, 0.0),

	("banner_107", 0, "map_flag_f02", banner_scale, snd_click, 0.0, 0.0, 0.0),

	("banner_108", 0, "map_flag_f03", banner_scale, snd_click, 0.0, 0.0, 0.0),

	("banner_109", 0, "map_flag_f04", banner_scale, snd_click, 0.0, 0.0, 0.0),

	("banner_110", 0, "map_flag_f05", banner_scale, snd_click, 0.0, 0.0, 0.0),

	("banner_111", 0, "map_flag_f06", banner_scale, snd_click, 0.0, 0.0, 0.0),

	("banner_112", 0, "map_flag_f07", banner_scale, snd_click, 0.0, 0.0, 0.0),

	("banner_113", 0, "map_flag_f08", banner_scale, snd_click, 0.0, 0.0, 0.0),

	("banner_114", 0, "map_flag_f09", banner_scale, snd_click, 0.0, 0.0, 0.0),

	("banner_115", 0, "map_flag_f10", banner_scale, snd_click, 0.0, 0.0, 0.0),

	("banner_116", 0, "map_flag_f11", banner_scale, snd_click, 0.0, 0.0, 0.0),

	("banner_117", 0, "map_flag_f12", banner_scale, snd_click, 0.0, 0.0, 0.0),

	("banner_118", 0, "map_flag_f13", banner_scale, snd_click, 0.0, 0.0, 0.0),

	("banner_119", 0, "map_flag_f14", banner_scale, snd_click, 0.0, 0.0, 0.0),

	("banner_120", 0, "map_flag_f15", banner_scale, snd_click, 0.0, 0.0, 0.0),

	("banner_121", 0, "map_flag_f16", banner_scale, snd_click, 0.0, 0.0, 0.0),

	("banner_122", 0, "map_flag_f17", banner_scale, snd_click, 0.0, 0.0, 0.0),

	("banner_123", 0, "map_flag_f18", banner_scale, snd_click, 0.0, 0.0, 0.0),

	("banner_124", 0, "map_flag_f19", banner_scale, snd_click, 0.0, 0.0, 0.0),

	("banner_125", 0, "map_flag_f20", banner_scale, snd_click, 0.0, 0.0, 0.0),

	("banner_126", 0, "map_flag_f21", banner_scale, snd_click, 0.0, 0.0, 0.0),

	("banner_127", 0, "map_flag_g01", banner_scale, snd_click, 0.0, 0.0, 0.0),

	("banner_128", 0, "map_flag_g02", banner_scale, snd_click, 0.0, 0.0, 0.0),

	("banner_129", 0, "map_flag_g03", banner_scale, snd_click, 0.0, 0.0, 0.0),

	("banner_130", 0, "map_flag_g04", banner_scale, snd_click, 0.0, 0.0, 0.0),

	("banner_131", 0, "map_flag_g05", banner_scale, snd_click, 0.0, 0.0, 0.0),

	("banner_132", 0, "map_flag_g06", banner_scale, snd_click, 0.0, 0.0, 0.0),

	("banner_133", 0, "map_flag_g07", banner_scale, snd_click, 0.0, 0.0, 0.0),

	("banner_134", 0, "map_flag_g08", banner_scale, snd_click, 0.0, 0.0, 0.0),

	("banner_135", 0, "map_flag_g09", banner_scale, snd_click, 0.0, 0.0, 0.0),

	("banner_136", 0, "map_flag_g10", banner_scale, snd_click, 0.0, 0.0, 0.0),

	("banner_137", 0, "map_flag_g11", banner_scale, snd_click, 0.0, 0.0, 0.0),

	("banner_138", 0, "map_flag_g12", banner_scale, snd_click, 0.0, 0.0, 0.0),

	("banner_139", 0, "map_flag_g13", banner_scale, snd_click, 0.0, 0.0, 0.0),

	("banner_140", 0, "map_flag_g14", banner_scale, snd_click, 0.0, 0.0, 0.0),

	("banner_141", 0, "map_flag_g15", banner_scale, snd_click, 0.0, 0.0, 0.0),

	("banner_142", 0, "map_flag_g16", banner_scale, snd_click, 0.0, 0.0, 0.0),

	("banner_143", 0, "map_flag_g17", banner_scale, snd_click, 0.0, 0.0, 0.0),

	("banner_144", 0, "map_flag_g18", banner_scale, snd_click, 0.0, 0.0, 0.0),

	("banner_145", 0, "map_flag_g19", banner_scale, snd_click, 0.0, 0.0, 0.0),

	("banner_146", 0, "map_flag_g20", banner_scale, snd_click, 0.0, 0.0, 0.0),

	("banner_147", 0, "map_flag_g21", banner_scale, snd_click, 0.0, 0.0, 0.0),

	("banner_148", 0, "map_flag_h01", banner_scale, snd_click, 0.0, 0.0, 0.0),

	("banner_149", 0, "map_flag_h02", banner_scale, snd_click, 0.0, 0.0, 0.0),

	("banner_150", 0, "map_flag_h03", banner_scale, snd_click, 0.0, 0.0, 0.0),

	("banner_151", 0, "map_flag_h04", banner_scale, snd_click, 0.0, 0.0, 0.0),

	("banner_152", 0, "map_flag_h05", banner_scale, snd_click, 0.0, 0.0, 0.0),

	("banner_153", 0, "map_flag_h06", banner_scale, snd_click, 0.0, 0.0, 0.0),

	("banner_154", 0, "map_flag_h07", banner_scale, snd_click, 0.0, 0.0, 0.0),

	("banner_155", 0, "map_flag_h08", banner_scale, snd_click, 0.0, 0.0, 0.0),

	("banner_156", 0, "map_flag_h09", banner_scale, snd_click, 0.0, 0.0, 0.0),

	("banner_157", 0, "map_flag_h10", banner_scale, snd_click, 0.0, 0.0, 0.0),

	("banner_158", 0, "map_flag_h11", banner_scale, snd_click, 0.0, 0.0, 0.0),

	("banner_159", 0, "map_flag_h12", banner_scale, snd_click, 0.0, 0.0, 0.0),

	("banner_160", 0, "map_flag_h13", banner_scale, snd_click, 0.0, 0.0, 0.0),

	("banner_161", 0, "map_flag_h14", banner_scale, snd_click, 0.0, 0.0, 0.0),

	("banner_162", 0, "map_flag_h15", banner_scale, snd_click, 0.0, 0.0, 0.0),

	("banner_163", 0, "map_flag_h16", banner_scale, snd_click, 0.0, 0.0, 0.0),

	("banner_164", 0, "map_flag_h17", banner_scale, snd_click, 0.0, 0.0, 0.0),

	("banner_165", 0, "map_flag_h18", banner_scale, snd_click, 0.0, 0.0, 0.0),

	("banner_166", 0, "map_flag_h19", banner_scale, snd_click, 0.0, 0.0, 0.0),

	("banner_167", 0, "map_flag_h20", banner_scale, snd_click, 0.0, 0.0, 0.0),

	("banner_168", 0, "map_flag_h21", banner_scale, snd_click, 0.0, 0.0, 0.0),

	("banner_169", 0, "map_flag_i01", banner_scale, snd_click, 0.0, 0.0, 0.0),

	("banner_170", 0, "map_flag_i02", banner_scale, snd_click, 0.0, 0.0, 0.0),

	("banner_171", 0, "map_flag_i03", banner_scale, snd_click, 0.0, 0.0, 0.0),

	("banner_172", 0, "map_flag_i04", banner_scale, snd_click, 0.0, 0.0, 0.0),

	("banner_173", 0, "map_flag_i05", banner_scale, snd_click, 0.0, 0.0, 0.0),

	("banner_174", 0, "map_flag_i06", banner_scale, snd_click, 0.0, 0.0, 0.0),

	("banner_175", 0, "map_flag_i07", banner_scale, snd_click, 0.0, 0.0, 0.0),

	("banner_176", 0, "map_flag_i08", banner_scale, snd_click, 0.0, 0.0, 0.0),

	("banner_177", 0, "map_flag_i09", banner_scale, snd_click, 0.0, 0.0, 0.0),

	("banner_178", 0, "map_flag_i10", banner_scale, snd_click, 0.0, 0.0, 0.0),

	("banner_179", 0, "map_flag_i11", banner_scale, snd_click, 0.0, 0.0, 0.0),

	("banner_180", 0, "map_flag_i12", banner_scale, snd_click, 0.0, 0.0, 0.0),

	("banner_181", 0, "map_flag_i13", banner_scale, snd_click, 0.0, 0.0, 0.0),

	("banner_182", 0, "map_flag_i14", banner_scale, snd_click, 0.0, 0.0, 0.0),

	("banner_183", 0, "map_flag_i15", banner_scale, snd_click, 0.0, 0.0, 0.0),

	("banner_184", 0, "map_flag_i16", banner_scale, snd_click, 0.0, 0.0, 0.0),

	("banner_185", 0, "map_flag_i17", banner_scale, snd_click, 0.0, 0.0, 0.0),

	("banner_186", 0, "map_flag_i18", banner_scale, snd_click, 0.0, 0.0, 0.0),

	("banner_187", 0, "map_flag_i19", banner_scale, snd_click, 0.0, 0.0, 0.0),

	("banner_188", 0, "map_flag_i20", banner_scale, snd_click, 0.0, 0.0, 0.0),

	("banner_189", 0, "map_flag_i21", banner_scale, snd_click, 0.0, 0.0, 0.0),

	("banner_190", 0, "map_flag_j01", banner_scale, snd_click, 0.0, 0.0, 0.0),

	("banner_191", 0, "map_flag_j02", banner_scale, snd_click, 0.0, 0.0, 0.0),

	("banner_192", 0, "map_flag_j03", banner_scale, snd_click, 0.0, 0.0, 0.0),

	("banner_193", 0, "map_flag_j04", banner_scale, snd_click, 0.0, 0.0, 0.0),

	("banner_194", 0, "map_flag_j05", banner_scale, snd_click, 0.0, 0.0, 0.0),

	("banner_195", 0, "map_flag_j06", banner_scale, snd_click, 0.0, 0.0, 0.0),

	("banner_196", 0, "map_flag_j07", banner_scale, snd_click, 0.0, 0.0, 0.0),

	("banner_197", 0, "map_flag_j08", banner_scale, snd_click, 0.0, 0.0, 0.0),

	("banner_198", 0, "map_flag_j09", banner_scale, snd_click, 0.0, 0.0, 0.0),

	("banner_199", 0, "map_flag_j10", banner_scale, snd_click, 0.0, 0.0, 0.0),

	("banner_200", 0, "map_flag_j11", banner_scale, snd_click, 0.0, 0.0, 0.0),

	("banner_201", 0, "map_flag_j12", banner_scale, snd_click, 0.0, 0.0, 0.0),

	("banner_202", 0, "map_flag_j13", banner_scale, snd_click, 0.0, 0.0, 0.0),

	("banner_203", 0, "map_flag_j14", banner_scale, snd_click, 0.0, 0.0, 0.0),

	("banner_204", 0, "map_flag_j15", banner_scale, snd_click, 0.0, 0.0, 0.0),

	("banner_205", 0, "map_flag_j16", banner_scale, snd_click, 0.0, 0.0, 0.0),

	("banner_206", 0, "map_flag_j17", banner_scale, snd_click, 0.0, 0.0, 0.0),

	("banner_207", 0, "map_flag_j18", banner_scale, snd_click, 0.0, 0.0, 0.0),

	("banner_208", 0, "map_flag_j19", banner_scale, snd_click, 0.0, 0.0, 0.0),

	("banner_209", 0, "map_flag_j20", banner_scale, snd_click, 0.0, 0.0, 0.0),

	("banner_210", 0, "map_flag_j21", banner_scale, snd_click, 0.0, 0.0, 0.0),

	("banner_211", 0, "map_flag_k01", banner_scale, snd_click, 0.0, 0.0, 0.0),

	("banner_212", 0, "map_flag_k02", banner_scale, snd_click, 0.0, 0.0, 0.0),

	("banner_213", 0, "map_flag_k03", banner_scale, snd_click, 0.0, 0.0, 0.0),

	("banner_214", 0, "map_flag_k04", banner_scale, snd_click, 0.0, 0.0, 0.0),

	("banner_215", 0, "map_flag_k05", banner_scale, snd_click, 0.0, 0.0, 0.0),

	("banner_216", 0, "map_flag_k06", banner_scale, snd_click, 0.0, 0.0, 0.0),

	("banner_217", 0, "map_flag_k07", banner_scale, snd_click, 0.0, 0.0, 0.0),

	("banner_218", 0, "map_flag_k08", banner_scale, snd_click, 0.0, 0.0, 0.0),

	("banner_219", 0, "map_flag_k09", banner_scale, snd_click, 0.0, 0.0, 0.0),

	("banner_220", 0, "map_flag_k10", banner_scale, snd_click, 0.0, 0.0, 0.0),

	("banner_221", 0, "map_flag_k11", banner_scale, snd_click, 0.0, 0.0, 0.0),

	("banner_222", 0, "map_flag_k12", banner_scale, snd_click, 0.0, 0.0, 0.0),

	("banner_223", 0, "map_flag_k13", banner_scale, snd_click, 0.0, 0.0, 0.0),

	("banner_224", 0, "map_flag_k14", banner_scale, snd_click, 0.0, 0.0, 0.0),

	("banner_225", 0, "map_flag_k15", banner_scale, snd_click, 0.0, 0.0, 0.0),

	("banner_226", 0, "map_flag_k16", banner_scale, snd_click, 0.0, 0.0, 0.0),

	("banner_227", 0, "map_flag_k17", banner_scale, snd_click, 0.0, 0.0, 0.0),

	("banner_228", 0, "map_flag_k18", banner_scale, snd_click, 0.0, 0.0, 0.0),

	("banner_229", 0, "map_flag_k19", banner_scale, snd_click, 0.0, 0.0, 0.0),

	("banner_230", 0, "map_flag_k20", banner_scale, snd_click, 0.0, 0.0, 0.0),

	("banner_231", 0, "map_flag_k21", banner_scale, snd_click, 0.0, 0.0, 0.0),

	("banner_232", 0, "map_flag_l01", banner_scale, snd_click, 0.0, 0.0, 0.0),

	("banner_233", 0, "map_flag_l02", banner_scale, snd_click, 0.0, 0.0, 0.0),

	("banner_234", 0, "map_flag_l03", banner_scale, snd_click, 0.0, 0.0, 0.0),

	("banner_235", 0, "map_flag_l04", banner_scale, snd_click, 0.0, 0.0, 0.0),

	("banner_236", 0, "map_flag_l05", banner_scale, snd_click, 0.0, 0.0, 0.0),

	("banner_237", 0, "map_flag_l06", banner_scale, snd_click, 0.0, 0.0, 0.0),

	("banner_238", 0, "map_flag_l07", banner_scale, snd_click, 0.0, 0.0, 0.0),

	("banner_239", 0, "map_flag_l08", banner_scale, snd_click, 0.0, 0.0, 0.0),

	("banner_240", 0, "map_flag_l09", banner_scale, snd_click, 0.0, 0.0, 0.0),

	("banner_241", 0, "map_flag_l10", banner_scale, snd_click, 0.0, 0.0, 0.0),

	("banner_242", 0, "map_flag_l11", banner_scale, snd_click, 0.0, 0.0, 0.0),

	("banner_243", 0, "map_flag_l12", banner_scale, snd_click, 0.0, 0.0, 0.0),

	("banner_244", 0, "map_flag_l13", banner_scale, snd_click, 0.0, 0.0, 0.0),

	("banner_245", 0, "map_flag_l14", banner_scale, snd_click, 0.0, 0.0, 0.0),

	("banner_246", 0, "map_flag_l15", banner_scale, snd_click, 0.0, 0.0, 0.0),

	("banner_247", 0, "map_flag_l16", banner_scale, snd_click, 0.0, 0.0, 0.0),

	("banner_248", 0, "map_flag_l17", banner_scale, snd_click, 0.0, 0.0, 0.0),

	("banner_249", 0, "map_flag_l18", banner_scale, snd_click, 0.0, 0.0, 0.0),

	("banner_250", 0, "map_flag_l19", banner_scale, snd_click, 0.0, 0.0, 0.0),

	("banner_251", 0, "map_flag_l20", banner_scale, snd_click, 0.0, 0.0, 0.0),

	("banner_252", 0, "map_flag_l21", banner_scale, snd_click, 0.0, 0.0, 0.0),

	("map_flag_lords_swadia_01", 0, "map_flag_lords_swadia01", banner_scale, snd_click, 0.0, 0.0, 0.0),

	("map_flag_lords_swadia_02", 0, "map_flag_lords_swadia02", banner_scale, snd_click, 0.0, 0.0, 0.0),

	("map_flag_lords_swadia_03", 0, "map_flag_lords_swadia03", banner_scale, snd_click, 0.0, 0.0, 0.0),

	("map_flag_lords_swadia_04", 0, "map_flag_lords_swadia04", banner_scale, snd_click, 0.0, 0.0, 0.0),

	("map_flag_lords_swadia_05", 0, "map_flag_lords_swadia05", banner_scale, snd_click, 0.0, 0.0, 0.0),

	("map_flag_lords_swadia_06", 0, "map_flag_lords_swadia06", banner_scale, snd_click, 0.0, 0.0, 0.0),

	("map_flag_lords_swadia_07", 0, "map_flag_lords_swadia07", banner_scale, snd_click, 0.0, 0.0, 0.0),

	("map_flag_lords_swadia_08", 0, "map_flag_lords_swadia08", banner_scale, snd_click, 0.0, 0.0, 0.0),

	("map_flag_lords_swadia_09", 0, "map_flag_lords_swadia09", banner_scale, snd_click, 0.0, 0.0, 0.0),

	("map_flag_lords_swadia_10", 0, "map_flag_lords_swadia10", banner_scale, snd_click, 0.0, 0.0, 0.0),

	("map_flag_lords_swadia_11", 0, "map_flag_lords_swadia11", banner_scale, snd_click, 0.0, 0.0, 0.0),

	("map_flag_lords_swadia_12", 0, "map_flag_lords_swadia12", banner_scale, snd_click, 0.0, 0.0, 0.0),

	("map_flag_lords_swadia_13", 0, "map_flag_lords_swadia13", banner_scale, snd_click, 0.0, 0.0, 0.0),

	("map_flag_lords_swadia_14", 0, "map_flag_lords_swadia14", banner_scale, snd_click, 0.0, 0.0, 0.0),

	("map_flag_lords_swadia_15", 0, "map_flag_lords_swadia15", banner_scale, snd_click, 0.0, 0.0, 0.0),

	("map_flag_lords_swadia_16", 0, "map_flag_lords_swadia16", banner_scale, snd_click, 0.0, 0.0, 0.0),

	("map_flag_lords_swadia_17", 0, "map_flag_lords_swadia17", banner_scale, snd_click, 0.0, 0.0, 0.0),

	("map_flag_lords_swadia_18", 0, "map_flag_lords_swadia18", banner_scale, snd_click, 0.0, 0.0, 0.0),

	("map_flag_lords_swadia_19", 0, "map_flag_lords_swadia19", banner_scale, snd_click, 0.0, 0.0, 0.0),

	("map_flag_lords_swadia_20", 0, "map_flag_lords_swadia20", banner_scale, snd_click, 0.0, 0.0, 0.0),

	("map_flag_lords_swadia_21", 0, "map_flag_lords_swadia21", banner_scale, snd_click, 0.0, 0.0, 0.0),

	("map_flag_lords_vaegir_01", 0, "map_flag_lords_vaegir01", banner_scale, snd_click, 0.0, 0.0, 0.0),

	("map_flag_lords_vaegir_02", 0, "map_flag_lords_vaegir02", banner_scale, snd_click, 0.0, 0.0, 0.0),

	("map_flag_lords_vaegir_03", 0, "map_flag_lords_vaegir03", banner_scale, snd_click, 0.0, 0.0, 0.0),

	("map_flag_lords_vaegir_04", 0, "map_flag_lords_vaegir04", banner_scale, snd_click, 0.0, 0.0, 0.0),

	("map_flag_lords_vaegir_05", 0, "map_flag_lords_vaegir05", banner_scale, snd_click, 0.0, 0.0, 0.0),

	("map_flag_lords_vaegir_06", 0, "map_flag_lords_vaegir06", banner_scale, snd_click, 0.0, 0.0, 0.0),

	("map_flag_lords_vaegir_07", 0, "map_flag_lords_vaegir07", banner_scale, snd_click, 0.0, 0.0, 0.0),

	("map_flag_lords_vaegir_08", 0, "map_flag_lords_vaegir08", banner_scale, snd_click, 0.0, 0.0, 0.0),

	("map_flag_lords_vaegir_09", 0, "map_flag_lords_vaegir09", banner_scale, snd_click, 0.0, 0.0, 0.0),

	("map_flag_lords_vaegir_10", 0, "map_flag_lords_vaegir10", banner_scale, snd_click, 0.0, 0.0, 0.0),

	("map_flag_lords_vaegir_11", 0, "map_flag_lords_vaegir11", banner_scale, snd_click, 0.0, 0.0, 0.0),

	("map_flag_lords_vaegir_12", 0, "map_flag_lords_vaegir12", banner_scale, snd_click, 0.0, 0.0, 0.0),

	("map_flag_lords_vaegir_13", 0, "map_flag_lords_vaegir13", banner_scale, snd_click, 0.0, 0.0, 0.0),

	("map_flag_lords_vaegir_14", 0, "map_flag_lords_vaegir14", banner_scale, snd_click, 0.0, 0.0, 0.0),

	("map_flag_lords_vaegir_15", 0, "map_flag_lords_vaegir15", banner_scale, snd_click, 0.0, 0.0, 0.0),

	("map_flag_lords_vaegir_16", 0, "map_flag_lords_vaegir16", banner_scale, snd_click, 0.0, 0.0, 0.0),

	("map_flag_lords_vaegir_17", 0, "map_flag_lords_vaegir17", banner_scale, snd_click, 0.0, 0.0, 0.0),

	("map_flag_lords_vaegir_18", 0, "map_flag_lords_vaegir18", banner_scale, snd_click, 0.0, 0.0, 0.0),

	("map_flag_lords_vaegir_19", 0, "map_flag_lords_vaegir19", banner_scale, snd_click, 0.0, 0.0, 0.0),

	("map_flag_lords_vaegir_20", 0, "map_flag_lords_vaegir20", banner_scale, snd_click, 0.0, 0.0, 0.0),

	("map_flag_lords_vaegir_21", 0, "map_flag_lords_vaegir21", banner_scale, snd_click, 0.0, 0.0, 0.0),

	("map_flag_lords_khergit_01", 0, "map_flag_lords_khergit01", banner_scale, snd_click, 0.0, 0.0, 0.0),

	("map_flag_lords_khergit_02", 0, "map_flag_lords_khergit02", banner_scale, snd_click, 0.0, 0.0, 0.0),

	("map_flag_lords_khergit_03", 0, "map_flag_lords_khergit03", banner_scale, snd_click, 0.0, 0.0, 0.0),

	("map_flag_lords_khergit_04", 0, "map_flag_lords_khergit04", banner_scale, snd_click, 0.0, 0.0, 0.0),

	("map_flag_lords_khergit_05", 0, "map_flag_lords_khergit05", banner_scale, snd_click, 0.0, 0.0, 0.0),

	("map_flag_lords_khergit_06", 0, "map_flag_lords_khergit06", banner_scale, snd_click, 0.0, 0.0, 0.0),

	("map_flag_lords_khergit_07", 0, "map_flag_lords_khergit07", banner_scale, snd_click, 0.0, 0.0, 0.0),

	("map_flag_lords_khergit_08", 0, "map_flag_lords_khergit08", banner_scale, snd_click, 0.0, 0.0, 0.0),

	("map_flag_lords_khergit_09", 0, "map_flag_lords_khergit09", banner_scale, snd_click, 0.0, 0.0, 0.0),

	("map_flag_lords_khergit_10", 0, "map_flag_lords_khergit10", banner_scale, snd_click, 0.0, 0.0, 0.0),

	("map_flag_lords_khergit_11", 0, "map_flag_lords_khergit11", banner_scale, snd_click, 0.0, 0.0, 0.0),

	("map_flag_lords_khergit_12", 0, "map_flag_lords_khergit12", banner_scale, snd_click, 0.0, 0.0, 0.0),

	("map_flag_lords_khergit_13", 0, "map_flag_lords_khergit13", banner_scale, snd_click, 0.0, 0.0, 0.0),

	("map_flag_lords_khergit_14", 0, "map_flag_lords_khergit14", banner_scale, snd_click, 0.0, 0.0, 0.0),

	("map_flag_lords_khergit_15", 0, "map_flag_lords_khergit15", banner_scale, snd_click, 0.0, 0.0, 0.0),

	("map_flag_lords_khergit_16", 0, "map_flag_lords_khergit16", banner_scale, snd_click, 0.0, 0.0, 0.0),

	("map_flag_lords_khergit_17", 0, "map_flag_lords_khergit17", banner_scale, snd_click, 0.0, 0.0, 0.0),

	("map_flag_lords_khergit_18", 0, "map_flag_lords_khergit18", banner_scale, snd_click, 0.0, 0.0, 0.0),

	("map_flag_lords_khergit_19", 0, "map_flag_lords_khergit19", banner_scale, snd_click, 0.0, 0.0, 0.0),

	("map_flag_lords_khergit_20", 0, "map_flag_lords_khergit20", banner_scale, snd_click, 0.0, 0.0, 0.0),

	("map_flag_lords_khergit_21", 0, "map_flag_lords_khergit21", banner_scale, snd_click, 0.0, 0.0, 0.0),

	("map_flag_lords_nord_01", 0, "map_flag_lords_nord01", banner_scale, snd_click, 0.0, 0.0, 0.0),

	("map_flag_lords_nord_02", 0, "map_flag_lords_nord02", banner_scale, snd_click, 0.0, 0.0, 0.0),

	("map_flag_lords_nord_03", 0, "map_flag_lords_nord03", banner_scale, snd_click, 0.0, 0.0, 0.0),

	("map_flag_lords_nord_04", 0, "map_flag_lords_nord04", banner_scale, snd_click, 0.0, 0.0, 0.0),

	("map_flag_lords_nord_05", 0, "map_flag_lords_nord05", banner_scale, snd_click, 0.0, 0.0, 0.0),

	("map_flag_lords_nord_06", 0, "map_flag_lords_nord06", banner_scale, snd_click, 0.0, 0.0, 0.0),

	("map_flag_lords_nord_07", 0, "map_flag_lords_nord07", banner_scale, snd_click, 0.0, 0.0, 0.0),

	("map_flag_lords_nord_08", 0, "map_flag_lords_nord08", banner_scale, snd_click, 0.0, 0.0, 0.0),

	("map_flag_lords_nord_09", 0, "map_flag_lords_nord09", banner_scale, snd_click, 0.0, 0.0, 0.0),

	("map_flag_lords_nord_10", 0, "map_flag_lords_nord10", banner_scale, snd_click, 0.0, 0.0, 0.0),

	("map_flag_lords_nord_11", 0, "map_flag_lords_nord11", banner_scale, snd_click, 0.0, 0.0, 0.0),

	("map_flag_lords_nord_12", 0, "map_flag_lords_nord12", banner_scale, snd_click, 0.0, 0.0, 0.0),

	("map_flag_lords_nord_13", 0, "map_flag_lords_nord13", banner_scale, snd_click, 0.0, 0.0, 0.0),

	("map_flag_lords_nord_14", 0, "map_flag_lords_nord14", banner_scale, snd_click, 0.0, 0.0, 0.0),

	("map_flag_lords_nord_15", 0, "map_flag_lords_nord15", banner_scale, snd_click, 0.0, 0.0, 0.0),

	("map_flag_lords_nord_16", 0, "map_flag_lords_nord16", banner_scale, snd_click, 0.0, 0.0, 0.0),

	("map_flag_lords_nord_17", 0, "map_flag_lords_nord17", banner_scale, snd_click, 0.0, 0.0, 0.0),

	("map_flag_lords_nord_18", 0, "map_flag_lords_nord18", banner_scale, snd_click, 0.0, 0.0, 0.0),

	("map_flag_lords_nord_19", 0, "map_flag_lords_nord19", banner_scale, snd_click, 0.0, 0.0, 0.0),

	("map_flag_lords_nord_20", 0, "map_flag_lords_nord20", banner_scale, snd_click, 0.0, 0.0, 0.0),

	("map_flag_lords_nord_21", 0, "map_flag_lords_nord21", banner_scale, snd_click, 0.0, 0.0, 0.0),

	("map_flag_lords_rhodok_01", 0, "map_flag_lords_rhodok01", banner_scale, snd_click, 0.0, 0.0, 0.0),

	("map_flag_lords_rhodok_02", 0, "map_flag_lords_rhodok02", banner_scale, snd_click, 0.0, 0.0, 0.0),

	("map_flag_lords_rhodok_03", 0, "map_flag_lords_rhodok03", banner_scale, snd_click, 0.0, 0.0, 0.0),

	("map_flag_lords_rhodok_04", 0, "map_flag_lords_rhodok04", banner_scale, snd_click, 0.0, 0.0, 0.0),

	("map_flag_lords_rhodok_05", 0, "map_flag_lords_rhodok05", banner_scale, snd_click, 0.0, 0.0, 0.0),

	("map_flag_lords_rhodok_06", 0, "map_flag_lords_rhodok06", banner_scale, snd_click, 0.0, 0.0, 0.0),

	("map_flag_lords_rhodok_07", 0, "map_flag_lords_rhodok07", banner_scale, snd_click, 0.0, 0.0, 0.0),

	("map_flag_lords_rhodok_08", 0, "map_flag_lords_rhodok08", banner_scale, snd_click, 0.0, 0.0, 0.0),

	("map_flag_lords_rhodok_09", 0, "map_flag_lords_rhodok09", banner_scale, snd_click, 0.0, 0.0, 0.0),

	("map_flag_lords_rhodok_10", 0, "map_flag_lords_rhodok10", banner_scale, snd_click, 0.0, 0.0, 0.0),

	("map_flag_lords_rhodok_11", 0, "map_flag_lords_rhodok11", banner_scale, snd_click, 0.0, 0.0, 0.0),

	("map_flag_lords_rhodok_12", 0, "map_flag_lords_rhodok12", banner_scale, snd_click, 0.0, 0.0, 0.0),

	("map_flag_lords_rhodok_13", 0, "map_flag_lords_rhodok13", banner_scale, snd_click, 0.0, 0.0, 0.0),

	("map_flag_lords_rhodok_14", 0, "map_flag_lords_rhodok14", banner_scale, snd_click, 0.0, 0.0, 0.0),

	("map_flag_lords_rhodok_15", 0, "map_flag_lords_rhodok15", banner_scale, snd_click, 0.0, 0.0, 0.0),

	("map_flag_lords_rhodok_16", 0, "map_flag_lords_rhodok16", banner_scale, snd_click, 0.0, 0.0, 0.0),

	("map_flag_lords_rhodok_17", 0, "map_flag_lords_rhodok17", banner_scale, snd_click, 0.0, 0.0, 0.0),

	("map_flag_lords_rhodok_18", 0, "map_flag_lords_rhodok18", banner_scale, snd_click, 0.0, 0.0, 0.0),

	("map_flag_lords_rhodok_19", 0, "map_flag_lords_rhodok19", banner_scale, snd_click, 0.0, 0.0, 0.0),

	("map_flag_lords_rhodok_20", 0, "map_flag_lords_rhodok20", banner_scale, snd_click, 0.0, 0.0, 0.0),

	("map_flag_lords_rhodok_21", 0, "map_flag_lords_rhodok21", banner_scale, snd_click, 0.0, 0.0, 0.0),

	("map_flag_lords_sarranid_01", 0, "map_flag_lords_sarranid01", banner_scale, snd_click, 0.0, 0.0, 0.0),

	("map_flag_lords_sarranid_02", 0, "map_flag_lords_sarranid02", banner_scale, snd_click, 0.0, 0.0, 0.0),

	("map_flag_lords_sarranid_03", 0, "map_flag_lords_sarranid03", banner_scale, snd_click, 0.0, 0.0, 0.0),

	("map_flag_lords_sarranid_04", 0, "map_flag_lords_sarranid04", banner_scale, snd_click, 0.0, 0.0, 0.0),

	("map_flag_lords_sarranid_05", 0, "map_flag_lords_sarranid05", banner_scale, snd_click, 0.0, 0.0, 0.0),

	("map_flag_lords_sarranid_06", 0, "map_flag_lords_sarranid06", banner_scale, snd_click, 0.0, 0.0, 0.0),

	("map_flag_lords_sarranid_07", 0, "map_flag_lords_sarranid07", banner_scale, snd_click, 0.0, 0.0, 0.0),

	("map_flag_lords_sarranid_08", 0, "map_flag_lords_sarranid08", banner_scale, snd_click, 0.0, 0.0, 0.0),

	("map_flag_lords_sarranid_09", 0, "map_flag_lords_sarranid09", banner_scale, snd_click, 0.0, 0.0, 0.0),

	("map_flag_lords_sarranid_10", 0, "map_flag_lords_sarranid10", banner_scale, snd_click, 0.0, 0.0, 0.0),

	("map_flag_lords_sarranid_11", 0, "map_flag_lords_sarranid11", banner_scale, snd_click, 0.0, 0.0, 0.0),

	("map_flag_lords_sarranid_12", 0, "map_flag_lords_sarranid12", banner_scale, snd_click, 0.0, 0.0, 0.0),

	("map_flag_lords_sarranid_13", 0, "map_flag_lords_sarranid13", banner_scale, snd_click, 0.0, 0.0, 0.0),

	("map_flag_lords_sarranid_14", 0, "map_flag_lords_sarranid14", banner_scale, snd_click, 0.0, 0.0, 0.0),

	("map_flag_lords_sarranid_15", 0, "map_flag_lords_sarranid15", banner_scale, snd_click, 0.0, 0.0, 0.0),

	("map_flag_lords_sarranid_16", 0, "map_flag_lords_sarranid16", banner_scale, snd_click, 0.0, 0.0, 0.0),

	("map_flag_lords_sarranid_17", 0, "map_flag_lords_sarranid17", banner_scale, snd_click, 0.0, 0.0, 0.0),

	("map_flag_lords_sarranid_18", 0, "map_flag_lords_sarranid18", banner_scale, snd_click, 0.0, 0.0, 0.0),

	("map_flag_lords_sarranid_19", 0, "map_flag_lords_sarranid19", banner_scale, snd_click, 0.0, 0.0, 0.0),

	("map_flag_lords_sarranid_20", 0, "map_flag_lords_sarranid20", banner_scale, snd_click, 0.0, 0.0, 0.0),

	("map_flag_lords_sarranid_21", 0, "map_flag_lords_sarranid21", banner_scale, snd_click, 0.0, 0.0, 0.0),

	("map_flag_companion_01", 0, "map_flag_companions01", banner_scale, snd_click, 0.0, 0.0, 0.0),

	("map_flag_companion_02", 0, "map_flag_companions02", banner_scale, snd_click, 0.0, 0.0, 0.0),

	("map_flag_companion_03", 0, "map_flag_companions03", banner_scale, snd_click, 0.0, 0.0, 0.0),

	("map_flag_companion_04", 0, "map_flag_companions04", banner_scale, snd_click, 0.0, 0.0, 0.0),

	("map_flag_companion_05", 0, "map_flag_companions05", banner_scale, snd_click, 0.0, 0.0, 0.0),

	("map_flag_companion_06", 0, "map_flag_companions06", banner_scale, snd_click, 0.0, 0.0, 0.0),

	("map_flag_companion_07", 0, "map_flag_companions07", banner_scale, snd_click, 0.0, 0.0, 0.0),

	("map_flag_companion_08", 0, "map_flag_companions08", banner_scale, snd_click, 0.0, 0.0, 0.0),

	("map_flag_companion_09", 0, "map_flag_companions09", banner_scale, snd_click, 0.0, 0.0, 0.0),

	("map_flag_companion_10", 0, "map_flag_companions10", banner_scale, snd_click, 0.0, 0.0, 0.0),

	("map_flag_companion_11", 0, "map_flag_companions11", banner_scale, snd_click, 0.0, 0.0, 0.0),

	("map_flag_companion_12", 0, "map_flag_companions12", banner_scale, snd_click, 0.0, 0.0, 0.0),

	("map_flag_companion_13", 0, "map_flag_companions13", banner_scale, snd_click, 0.0, 0.0, 0.0),

	("map_flag_companion_14", 0, "map_flag_companions14", banner_scale, snd_click, 0.0, 0.0, 0.0),

	("map_flag_companion_15", 0, "map_flag_companions15", banner_scale, snd_click, 0.0, 0.0, 0.0),

	("map_flag_companion_16", 0, "map_flag_companions16", banner_scale, snd_click, 0.0, 0.0, 0.0),

	("map_flag_companion_17", 0, "map_flag_companions17", banner_scale, snd_click, 0.0, 0.0, 0.0),

	("map_flag_companion_18", 0, "map_flag_companions18", banner_scale, snd_click, 0.0, 0.0, 0.0),

	("map_flag_companion_19", 0, "map_flag_companions19", banner_scale, snd_click, 0.0, 0.0, 0.0),

	("map_flag_companion_20", 0, "map_flag_companions20", banner_scale, snd_click, 0.0, 0.0, 0.0),

	("map_flag_companion_21", 0, "map_flag_companions21", banner_scale, snd_click, 0.0, 0.0, 0.0),

	("map_flag_companion_22", 0, "map_flag_companions22", banner_scale, snd_click, 0.0, 0.0, 0.0),

	("map_flag_bandit_a", 0, "map_flag_bandit_a", banner_scale, snd_click, 0.0, 0.0, 0.0),

	("map_flag_bandit_b", 0, "map_flag_bandit_b", banner_scale, snd_click, 0.0, 0.0, 0.0),

	("map_flag_bandit_c", 0, "map_flag_bandit_c", banner_scale, snd_click, 0.0, 0.0, 0.0),

	("map_flag_bandit_d", 0, "map_flag_bandit_a", banner_scale, snd_click, 0.0, 0.0, 0.0),

	("map_flag_bandit_e", 0, "map_flag_bandit_d", banner_scale, snd_click, 0.0, 0.0, 0.0),

	("map_flag_bandit_f", 0, "map_flag_bandit_f", banner_scale, snd_click, 0.0, 0.0, 0.0),

	("map_flag_bandit_g", 0, "map_flag_bandit_e", banner_scale, snd_click, 0.0, 0.0, 0.0),

	("map_flag_kingdom_a", 0, "map_flag_kingdom_a", banner_scale, snd_click, 0.0, 0.0, 0.0),

	("map_flag_kingdom_b", 0, "map_flag_kingdom_b", banner_scale, snd_click, 0.0, 0.0, 0.0),

	("map_flag_kingdom_c", 0, "map_flag_kingdom_c", banner_scale, snd_click, 0.0, 0.0, 0.0),

	("map_flag_kingdom_d", 0, "map_flag_kingdom_d", banner_scale, snd_click, 0.0, 0.0, 0.0),

	("map_flag_kingdom_e", 0, "map_flag_kingdom_e", banner_scale, snd_click, 0.0, 0.0, 0.0),

	("map_flag_kingdom_f", 0, "map_flag_kingdom_f", banner_scale, snd_click, 0.0, 0.0, 0.0),

	("map_flag_kingdom_g", 0, "map_flag_kingdom_g", banner_scale, snd_click, 0.0, 0.0, 0.0),

	("map_flag_kingdom_h", 0, "map_flag_kingdom_h", banner_scale, snd_click, 0.0, 0.0, 0.0),

	("map_flag_kingdom_i", 0, "map_flag_kingdom_i", banner_scale, snd_click, 0.0, 0.0, 0.0),

	("map_flag_kingdom_j", 0, "map_flag_kingdom_j", banner_scale, snd_click, 0.0, 0.0, 0.0),

	("map_flag_kingdom_k", 0, "map_flag_kingdom_k", banner_scale, snd_click, 0.0, 0.0, 0.0),

	("map_flag_kingdom_l", 0, "map_flag_kingdom_l", banner_scale, snd_click, 0.0, 0.0, 0.0),

	("map_flag_kingdom_m", 0, "map_flag_kingdom_m", banner_scale, snd_click, 0.0, 0.0, 0.0),

	("map_flag_kingdom_n", 0, "map_flag_kingdom_n", banner_scale, snd_click, 0.0, 0.0, 0.0),

]