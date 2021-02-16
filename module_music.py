from header_music import *
####################################################################################################################
#  Each track record contains the following fields:
#  1) Track id: used for referencing tracks.
#  2) Track file: filename of the track
#  3) Track flags. See header_music.py for a list of available flags
#  4) Continue Track flags: Shows in which situations or cultures the track can continue playing. See header_music.py for a list of available flags
####################################################################################################################

# WARNING: You MUST add mtf_module_track flag to the flags of the tracks located under module directory

tracks = [
	("cant_find_this", "cant_find_this.ogg", 0, 0),

	("main_menu_music_mhysa", "main_menu_music_mhysa.mp3", mtf_start_immediately|mtf_sit_main_title|mtf_module_track, 0),

	("min_ambushed_by_rhodok", "min_ambushed_by_rhodok.mp3", mtf_culture_5|mtf_sit_ambushed|mtf_sit_siege|mtf_module_track, mtf_culture_1|mtf_culture_2|mtf_culture_3|mtf_culture_4|mtf_culture_6|mtf_sit_fight|mtf_sit_multiplayer_fight),

	("min_ambushed_by_rhodok", "min_ambushed_by_rhodok.mp3", mtf_culture_5|mtf_sit_ambushed|mtf_sit_siege|mtf_module_track, mtf_culture_1|mtf_culture_2|mtf_culture_3|mtf_culture_4|mtf_culture_6|mtf_sit_fight|mtf_sit_multiplayer_fight),

	("min_ambushed_by_vaegir", "min_ambushed_by_vaegir.mp3", mtf_culture_2|mtf_sit_ambushed|mtf_sit_siege|mtf_module_track, mtf_culture_1|mtf_culture_3|mtf_culture_4|mtf_culture_5|mtf_culture_6|mtf_sit_fight|mtf_sit_multiplayer_fight),

	("min_ambushed_by_rhodok", "min_ambushed_by_rhodok.mp3", mtf_culture_5|mtf_sit_ambushed|mtf_sit_siege|mtf_module_track, mtf_culture_1|mtf_culture_2|mtf_culture_3|mtf_culture_4|mtf_culture_6|mtf_sit_fight|mtf_sit_multiplayer_fight),

	("min_ambushed_by_rhodok", "min_ambushed_by_rhodok.mp3", mtf_culture_5|mtf_sit_ambushed|mtf_sit_siege|mtf_module_track, mtf_culture_1|mtf_culture_2|mtf_culture_3|mtf_culture_4|mtf_culture_6|mtf_sit_fight|mtf_sit_multiplayer_fight),

	("min_ambushed_by_rhodok", "min_ambushed_by_rhodok.mp3", mtf_culture_5|mtf_sit_ambushed|mtf_sit_siege|mtf_module_track, mtf_culture_1|mtf_culture_2|mtf_culture_3|mtf_culture_4|mtf_culture_6|mtf_sit_fight|mtf_sit_multiplayer_fight),

	("min_ambushed_by_sarranid", "min_ambushed_by_sarranid.mp3", mtf_culture_6|mtf_sit_ambushed|mtf_sit_siege|mtf_module_track, mtf_culture_1|mtf_culture_2|mtf_culture_3|mtf_culture_4|mtf_culture_5|mtf_sit_fight|mtf_sit_multiplayer_fight),

	("min_arena_rhodok", "min_arena_rhodok.mp3", mtf_culture_5|mtf_sit_arena|mtf_module_track, 0),

	("min_arena_rhodok", "min_arena_rhodok.mp3", mtf_culture_5|mtf_sit_arena|mtf_module_track, 0),

	("min_arena_vaegir", "min_arena_vaegir.mp3", mtf_culture_2|mtf_sit_arena|mtf_module_track, 0),

	("min_arena_rhodok", "min_arena_rhodok.mp3", mtf_culture_5|mtf_sit_arena|mtf_module_track, 0),

	("min_arena_nord", "min_arena_nord.mp3", mtf_culture_4|mtf_sit_arena|mtf_module_track, 0),

	("min_arena_rhodok", "min_arena_rhodok.mp3", mtf_culture_5|mtf_sit_arena|mtf_module_track, 0),

	("min_arena_sarranid", "min_arena_sarranid.mp3", mtf_culture_6|mtf_sit_arena|mtf_module_track, 0),

	("armorer", "armorer.mp3", mtf_sit_travel|mtf_module_track, 0),

	("min_bandit_fight", "min_bandit_fight.mp3", mtf_sit_fight|mtf_sit_multiplayer_fight|mtf_sit_ambushed|mtf_module_track, 0),

	("calm_night_1", "calm_night_1.mp3", mtf_sit_night|mtf_module_track, mtf_sit_tavern|mtf_sit_town|mtf_sit_travel),

	("min_captured", "min_captured.mp3", mtf_persist_until_finished|mtf_module_track, 0),

	("min_defeated_by_neutral", "min_defeated_by_neutral.mp3", mtf_persist_until_finished|mtf_sit_killed|mtf_module_track, 0),

	("min_empty_village", "min_empty_village.mp3", mtf_persist_until_finished|mtf_module_track, 0),

	("encounter_hostile_nords", "encounter_hostile_nords.ogg", mtf_persist_until_finished|mtf_sit_encounter_hostile, 0),

	("escape", "escape.ogg", mtf_persist_until_finished, 0),

	("battle_neutral_1", "battle_neutral_1.mp3", mtf_sit_fight|mtf_sit_multiplayer_fight|mtf_sit_ambushed|mtf_module_track, 0),

	("battle_neutral_2", "battle_neutral_2.mp3", mtf_sit_fight|mtf_sit_multiplayer_fight|mtf_sit_ambushed|mtf_module_track, 0),

	("battle_neutral_3", "battle_neutral_3.mp3", mtf_sit_fight|mtf_sit_multiplayer_fight|mtf_sit_ambushed|mtf_module_track, 0),

	("battle_neutral_4", "battle_neutral_4.mp3", mtf_sit_fight|mtf_sit_multiplayer_fight|mtf_sit_ambushed|mtf_module_track, 0),

	("battle_stormlands_1", "battle_stormlands_1.mp3", mtf_culture_1|mtf_sit_fight|mtf_sit_multiplayer_fight|mtf_sit_ambushed|mtf_module_track, mtf_culture_2|mtf_culture_3|mtf_culture_4|mtf_culture_5|mtf_culture_6),

	("battle_north_1", "battle_north_1.mp3", mtf_culture_2|mtf_sit_fight|mtf_sit_multiplayer_fight|mtf_sit_ambushed|mtf_module_track, mtf_culture_1|mtf_culture_3|mtf_culture_4|mtf_culture_5|mtf_culture_6),

	("battle_ironborn_1", "battle_ironborn_1.mp3", mtf_culture_3|mtf_sit_fight|mtf_sit_multiplayer_fight|mtf_sit_ambushed|mtf_module_track, mtf_culture_1|mtf_culture_2|mtf_culture_4|mtf_culture_5|mtf_culture_6),

	("battle_westerlands_1", "battle_westerlands_1.mp3", mtf_culture_4|mtf_sit_fight|mtf_sit_multiplayer_fight|mtf_sit_ambushed|mtf_module_track, mtf_culture_1|mtf_culture_2|mtf_culture_3|mtf_culture_5|mtf_culture_6),

	("battle_free_cities_1", "battle_free_cities_1.mp3", mtf_culture_5|mtf_sit_fight|mtf_sit_multiplayer_fight|mtf_sit_ambushed|mtf_module_track, mtf_culture_1|mtf_culture_2|mtf_culture_3|mtf_culture_4|mtf_culture_6),

	("battle_westeros_1", "battle_westeros_1.mp3", mtf_culture_6|mtf_sit_fight|mtf_sit_multiplayer_fight|mtf_sit_ambushed|mtf_module_track, mtf_culture_1|mtf_culture_2|mtf_culture_3|mtf_culture_4|mtf_culture_5),

	("mounted_battle_1", "mounted_battle_1.mp3", mtf_sit_fight|mtf_sit_multiplayer_fight|mtf_sit_ambushed|mtf_module_track, 0),

	("mounted_battle_2", "mounted_battle_2.mp3", mtf_sit_fight|mtf_sit_multiplayer_fight|mtf_sit_ambushed|mtf_module_track, 0),

	("min_infiltration_swadia", "min_infiltration_swadia.mp3", mtf_culture_1|mtf_sit_town_infiltrate|mtf_module_track, mtf_culture_2|mtf_culture_3|mtf_culture_4|mtf_culture_5|mtf_culture_6),

	("min_infiltration_vaegir", "min_infiltration_vaegir.mp3", mtf_culture_2|mtf_sit_town_infiltrate|mtf_module_track, mtf_culture_1|mtf_culture_3|mtf_culture_4|mtf_culture_5|mtf_culture_6),

	("infiltration_khergit", "infiltration_khergit.ogg", mtf_culture_3|mtf_sit_town_infiltrate, mtf_culture_1|mtf_culture_2|mtf_culture_4|mtf_culture_5|mtf_culture_6),

	("min_infiltration_nord", "min_infiltration_nord.mp3", mtf_culture_4|mtf_sit_town_infiltrate|mtf_module_track, mtf_culture_1|mtf_culture_2|mtf_culture_3|mtf_culture_5|mtf_culture_6),

	("min_infiltration_rhodok", "min_infiltration_rhodok.mp3", mtf_culture_5|mtf_sit_town_infiltrate|mtf_module_track, mtf_culture_1|mtf_culture_2|mtf_culture_3|mtf_culture_4|mtf_culture_6),

	("min_infiltration_sarranid", "min_infiltration_sarranid.mp3", mtf_culture_6|mtf_sit_town_infiltrate|mtf_module_track, mtf_culture_1|mtf_culture_2|mtf_culture_3|mtf_culture_4|mtf_culture_5),

	("min_killed_by_neutral", "min_killed_by_neutral.mp3", mtf_persist_until_finished|mtf_sit_killed|mtf_module_track, 0),

	("killed_by_swadian", "killed_by_swadian.ogg", mtf_culture_1|mtf_persist_until_finished|mtf_sit_killed, 0),

	("min_killed_by_vaegir", "min_killed_by_vaegir.mp3", mtf_culture_2|mtf_persist_until_finished|mtf_sit_killed|mtf_module_track, 0),

	("killed_by_khergit", "killed_by_khergit.ogg", mtf_culture_3|mtf_persist_until_finished|mtf_sit_killed, 0),

	("min_killed_by_nord", "min_killed_by_nord.mp3", mtf_culture_4|mtf_persist_until_finished|mtf_sit_killed|mtf_module_track, 0),

	("min_killed_by_rhodok", "min_killed_by_rhodok.mp3", mtf_culture_5|mtf_persist_until_finished|mtf_sit_killed|mtf_module_track, 0),

	("min_killed_by_sarranid", "min_killed_by_sarranid.mp3", mtf_culture_6|mtf_persist_until_finished|mtf_sit_killed|mtf_module_track, 0),

	("lords_hall_rhodok", "lords_hall_rhodok.ogg", mtf_culture_5|mtf_sit_travel, mtf_culture_1|mtf_culture_2|mtf_culture_3|mtf_culture_4|mtf_culture_6|mtf_sit_tavern|mtf_sit_town|mtf_sit_night),

	("lords_hall_vaegir", "lords_hall_vaegir.ogg", mtf_culture_2|mtf_sit_travel, mtf_culture_1|mtf_culture_3|mtf_culture_4|mtf_culture_5|mtf_culture_6|mtf_sit_tavern|mtf_sit_town|mtf_sit_night),

	("lords_hall_rhodok", "lords_hall_rhodok.ogg", mtf_culture_5|mtf_sit_travel, mtf_culture_1|mtf_culture_2|mtf_culture_3|mtf_culture_4|mtf_culture_6|mtf_sit_tavern|mtf_sit_town|mtf_sit_night),

	("lords_hall_swadian", "lords_hall_swadian.ogg", mtf_culture_4|mtf_sit_travel, mtf_culture_1|mtf_culture_2|mtf_culture_3|mtf_culture_5|mtf_culture_6|mtf_sit_tavern|mtf_sit_town|mtf_sit_night),

	("lords_hall_rhodok", "lords_hall_rhodok.ogg", mtf_culture_5|mtf_sit_travel, mtf_culture_1|mtf_culture_2|mtf_culture_3|mtf_culture_4|mtf_culture_6|mtf_sit_tavern|mtf_sit_town|mtf_sit_night),

	("lords_hall_nord", "lords_hall_nord.ogg", mtf_culture_6|mtf_sit_travel, mtf_culture_1|mtf_culture_2|mtf_culture_3|mtf_culture_4|mtf_culture_5|mtf_sit_tavern|mtf_sit_town|mtf_sit_night),

	("map_travel_terrain_1", "map_travel_terrain_1.mp3", mtf_sit_travel|mtf_module_track, mtf_sit_tavern|mtf_sit_town|mtf_sit_night),

	("map_travel_terrain_2", "map_travel_terrain_2.mp3", mtf_sit_travel|mtf_module_track, mtf_sit_tavern|mtf_sit_town|mtf_sit_night),

	("map_travel_terrain_3", "map_travel_terrain_3.mp3", mtf_sit_travel|mtf_module_track, mtf_sit_tavern|mtf_sit_town|mtf_sit_night),

	("map_travel_terrain_4", "map_travel_terrain_4.mp3", mtf_sit_travel|mtf_module_track, mtf_sit_tavern|mtf_sit_town|mtf_sit_night),

	("neutral_infiltration", "neutral_infiltration.ogg", mtf_sit_town_infiltrate, 0),

	("min_retreat", "min_retreat.mp3", mtf_persist_until_finished|mtf_sit_killed|mtf_module_track, 0),

	("siege_1", "siege_1.mp3", mtf_sit_siege|mtf_module_track, mtf_sit_fight|mtf_sit_multiplayer_fight|mtf_sit_ambushed),

	("siege_2", "siege_2.mp3", mtf_sit_siege|mtf_module_track, mtf_sit_fight|mtf_sit_multiplayer_fight|mtf_sit_ambushed),

	("siege_3", "siege_3.mp3", mtf_sit_siege|mtf_module_track, mtf_sit_fight|mtf_sit_multiplayer_fight|mtf_sit_ambushed),

	("siege_4", "siege_4.mp3", mtf_sit_siege|mtf_module_track, mtf_sit_fight|mtf_sit_multiplayer_fight|mtf_sit_ambushed),

	("min_tavern_1", "min_tavern_1.mp3", mtf_sit_tavern|mtf_sit_feast|mtf_module_track, 0),

	("min_tavern_2", "min_tavern_2.mp3", mtf_sit_tavern|mtf_sit_feast|mtf_module_track, 0),

	("town_neutral_1", "town_neutral_1.mp3", mtf_sit_town|mtf_sit_travel|mtf_module_track, mtf_sit_tavern|mtf_sit_night),

	("stormlands_town_1", "stormlands_town_1.mp3", mtf_culture_1|mtf_sit_town|mtf_sit_travel|mtf_module_track, mtf_culture_2|mtf_culture_3|mtf_culture_4|mtf_culture_5|mtf_culture_6|mtf_sit_tavern|mtf_sit_night),

	("north_town_1", "north_town_1.mp3", mtf_culture_2|mtf_sit_town|mtf_sit_travel|mtf_module_track, mtf_culture_1|mtf_culture_3|mtf_culture_4|mtf_culture_5|mtf_culture_6|mtf_sit_tavern|mtf_sit_night),

	("ironborn_town_1", "ironborn_town_1.mp3", mtf_culture_3|mtf_sit_town|mtf_sit_travel|mtf_module_track, mtf_culture_1|mtf_culture_2|mtf_culture_4|mtf_culture_5|mtf_culture_6|mtf_sit_tavern|mtf_sit_night),

	("westerlands_town_1", "westerlands_town_1.mp3", mtf_culture_4|mtf_sit_town|mtf_sit_travel|mtf_module_track, mtf_culture_1|mtf_culture_2|mtf_culture_3|mtf_culture_5|mtf_culture_6|mtf_sit_tavern|mtf_sit_night),

	("town_free_cities_1", "town_free_cities_1.mp3", mtf_culture_5|mtf_sit_town|mtf_sit_travel|mtf_module_track, mtf_culture_1|mtf_culture_2|mtf_culture_3|mtf_culture_4|mtf_culture_6|mtf_sit_tavern|mtf_sit_night),

	("town_westeros_1", "town_westeros_1.mp3", mtf_culture_6|mtf_sit_town|mtf_sit_travel|mtf_module_track, mtf_culture_1|mtf_culture_2|mtf_culture_3|mtf_culture_4|mtf_culture_5|mtf_sit_tavern|mtf_sit_night),

	("travel_neutral_1", "travel_neutral_1.mp3", mtf_sit_travel|mtf_module_track, mtf_sit_tavern|mtf_sit_town|mtf_sit_night),

	("travel_neutral_2", "travel_neutral_2.mp3", mtf_sit_travel|mtf_module_track, mtf_sit_tavern|mtf_sit_town|mtf_sit_night),

	("travel_neutral_3", "travel_neutral_3.mp3", mtf_sit_travel|mtf_module_track, mtf_sit_tavern|mtf_sit_town|mtf_sit_night),

	("travel_neutral_4", "travel_neutral_4.mp3", mtf_sit_travel|mtf_module_track, mtf_sit_tavern|mtf_sit_town|mtf_sit_night),

	("travel_stormlands_1", "travel_stormlands_1.mp3", mtf_culture_1|mtf_sit_travel|mtf_module_track, mtf_culture_2|mtf_culture_3|mtf_culture_4|mtf_culture_5|mtf_culture_6|mtf_sit_tavern|mtf_sit_town|mtf_sit_night),

	("travel_stormlands_2", "travel_stormlands_2.mp3", mtf_culture_1|mtf_sit_travel|mtf_module_track, mtf_culture_2|mtf_culture_3|mtf_culture_4|mtf_culture_5|mtf_culture_6|mtf_sit_tavern|mtf_sit_town|mtf_sit_night),

	("travel_north_1", "travel_north_1.mp3", mtf_culture_2|mtf_sit_travel|mtf_module_track, mtf_culture_1|mtf_culture_3|mtf_culture_4|mtf_culture_5|mtf_culture_6|mtf_sit_tavern|mtf_sit_town|mtf_sit_night),

	("travel_north_2", "travel_north_2.mp3", mtf_culture_2|mtf_sit_travel|mtf_module_track, mtf_culture_1|mtf_culture_3|mtf_culture_4|mtf_culture_5|mtf_culture_6|mtf_sit_tavern|mtf_sit_town|mtf_sit_night),

	("travel_ironborn_1", "travel_ironborn_1.mp3", mtf_culture_3|mtf_sit_travel|mtf_module_track, mtf_culture_1|mtf_culture_2|mtf_culture_4|mtf_culture_5|mtf_culture_6|mtf_sit_tavern|mtf_sit_town|mtf_sit_night),

	("travel_ironborn_2", "travel_ironborn_2.mp3", mtf_culture_3|mtf_sit_travel|mtf_module_track, mtf_culture_1|mtf_culture_2|mtf_culture_4|mtf_culture_5|mtf_culture_6|mtf_sit_tavern|mtf_sit_town|mtf_sit_night),

	("travel_westerlands_1", "travel_westerlands_1.mp3", mtf_culture_4|mtf_sit_travel|mtf_module_track, mtf_culture_1|mtf_culture_2|mtf_culture_3|mtf_culture_5|mtf_culture_6|mtf_sit_tavern|mtf_sit_town|mtf_sit_night),

	("travel_westerlands_2", "travel_westerlands_2.mp3", mtf_culture_4|mtf_sit_travel|mtf_module_track, mtf_culture_1|mtf_culture_2|mtf_culture_3|mtf_culture_5|mtf_culture_6|mtf_sit_tavern|mtf_sit_town|mtf_sit_night),

	("travel_free_cities_1", "travel_free_cities_1.mp3", mtf_culture_5|mtf_sit_travel|mtf_module_track, mtf_culture_1|mtf_culture_2|mtf_culture_3|mtf_culture_4|mtf_culture_6|mtf_sit_tavern|mtf_sit_town|mtf_sit_night),

	("travel_free_cities_2", "travel_free_cities_2.mp3", mtf_culture_5|mtf_sit_travel|mtf_module_track, mtf_culture_1|mtf_culture_2|mtf_culture_3|mtf_culture_4|mtf_culture_6|mtf_sit_tavern|mtf_sit_town|mtf_sit_night),

	("travel_westeros_1", "travel_westeros_1.mp3", mtf_culture_6|mtf_sit_travel|mtf_module_track, mtf_culture_1|mtf_culture_2|mtf_culture_3|mtf_culture_4|mtf_culture_5|mtf_sit_tavern|mtf_sit_town|mtf_sit_night),

	("travel_westeros_2", "travel_westeros_2.mp3", mtf_culture_6|mtf_sit_travel|mtf_module_track, mtf_culture_1|mtf_culture_2|mtf_culture_3|mtf_culture_4|mtf_culture_5|mtf_sit_tavern|mtf_sit_town|mtf_sit_night),

	("uncertain_homestead", "uncertain_homestead.ogg", mtf_sit_travel, mtf_sit_tavern|mtf_sit_town|mtf_sit_night),

	("hearth_and_brotherhood", "hearth_and_brotherhood.ogg", mtf_sit_travel, mtf_sit_tavern|mtf_sit_town|mtf_sit_night),

	("min_tragic_village", "min_tragic_village.mp3", mtf_sit_travel|mtf_module_track, mtf_sit_tavern|mtf_sit_town|mtf_sit_night),

	("min_victorious_evil", "min_victorious_evil.mp3", mtf_persist_until_finished|mtf_module_track, 0),

	("victorious_neutral_1", "victorious_neutral_1.ogg", mtf_persist_until_finished|mtf_sit_victorious, 0),

	("victorious_neutral_2", "victorious_neutral_2.ogg", mtf_persist_until_finished|mtf_sit_victorious, 0),

	("victorious_neutral_3", "victorious_neutral_3.ogg", mtf_persist_until_finished|mtf_sit_victorious, 0),

	("victorious_ironborn", "victorious_ironborn.mp3", mtf_culture_5|mtf_persist_until_finished|mtf_sit_victorious, 0),

	("victorious_ironborn", "victorious_ironborn.mp3", mtf_culture_5|mtf_persist_until_finished|mtf_sit_victorious, 0),

	("victorious_ironborn", "victorious_ironborn.mp3", mtf_culture_5|mtf_persist_until_finished|mtf_sit_victorious, 0),

	("victorious_ironborn", "victorious_ironborn.mp3", mtf_culture_5|mtf_persist_until_finished|mtf_sit_victorious, 0),

	("victorious_ironborn", "victorious_ironborn.mp3", mtf_culture_5|mtf_persist_until_finished|mtf_sit_victorious, 0),

	("victorious_ironborn", "victorious_ironborn.mp3", mtf_culture_5|mtf_persist_until_finished|mtf_sit_victorious, 0),

	("wedding", "wedding.ogg", mtf_persist_until_finished, 0),

	("coronation", "coronation.ogg", mtf_persist_until_finished, 0),

]