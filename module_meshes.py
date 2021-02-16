from header_meshes import *

####################################################################################################################
#  Each mesh record contains the following fields:
#  1) Mesh id: used for referencing meshes in other files. The prefix mesh_ is automatically added before each mesh id.
#  2) Mesh flags. See header_meshes.py for a list of available flags
#  3) Mesh resource name: Resource name of the mesh
#  4) Mesh translation on x axis: Will be done automatically when the mesh is loaded
#  5) Mesh translation on y axis: Will be done automatically when the mesh is loaded
#  6) Mesh translation on z axis: Will be done automatically when the mesh is loaded
#  7) Mesh rotation angle over x axis: Will be done automatically when the mesh is loaded
#  8) Mesh rotation angle over y axis: Will be done automatically when the mesh is loaded
#  9) Mesh rotation angle over z axis: Will be done automatically when the mesh is loaded
#  10) Mesh x scale: Will be done automatically when the mesh is loaded
#  11) Mesh y scale: Will be done automatically when the mesh is loaded
#  12) Mesh z scale: Will be done automatically when the mesh is loaded
####################################################################################################################

meshes = [
	("pic_ships_port", 0, "pic_ships_port", 0, 0, 0, 0, 0, 0, 1, 1, 1),

	("pic_ships_rego", 0, "pic_ships_rego", 0, 0, 0, 0, 0, 0, 1, 1, 1),

	("pic_bandits", 0, "pic_bandits", 0, 0, 0, 0, 0, 0, 1, 1, 1),

	("pic_mb_warrior_1", 0, "pic_mb_warrior_1", 0, 0, 0, 0, 0, 0, 1, 1, 1),

	("pic_messenger", 0, "pic_messenger", 0, 0, 0, 0, 0, 0, 1, 1, 1),

	("pic_prisoner_man", 0, "pic_prisoner_man", 0, 0, 0, 0, 0, 0, 1, 1, 1),

	("pic_prisoner_fem", 0, "pic_prisoner_fem", 0, 0, 0, 0, 0, 0, 1, 1, 1),

	("pic_prisoner_wilderness", 0, "pic_prisoner_wilderness", 0, 0, 0, 0, 0, 0, 1, 1, 1),

	("pic_siege_sighted", 0, "pic_siege_sighted", 0, 0, 0, 0, 0, 0, 1, 1, 1),

	("pic_siege_sighted_fem", 0, "pic_siege_sighted_fem", 0, 0, 0, 0, 0, 0, 1, 1, 1),

	("pic_camp", 0, "pic_camp", 0, 0, 0, 0, 0, 0, 1, 1, 1),

	("pic_payment", 0, "pic_payment", 0, 0, 0, 0, 0, 0, 1, 1, 1),

	("pic_escape_1", 0, "pic_escape_1", 0, 0, 0, 0, 0, 0, 1, 1, 1),

	("pic_escape_1_fem", 0, "pic_escape_1_fem", 0, 0, 0, 0, 0, 0, 1, 1, 1),

	("pic_victory", 0, "pic_victory", 0, 0, 0, 0, 0, 0, 1, 1, 1),

	("pic_defeat", 0, "pic_defeat", 0, 0, 0, 0, 0, 0, 1, 1, 1),

	("pic_wounded", 0, "pic_wounded", 0, 0, 0, 0, 0, 0, 1, 1, 1),

	("pic_wounded_fem", 0, "pic_wounded_fem", 0, 0, 0, 0, 0, 0, 1, 1, 1),

	("pic_steppe_bandits", 0, "pic_steppe_bandits", 0, 0, 0, 0, 0, 0, 1, 1, 1),

	("pic_mountain_bandits", 0, "pic_mountain_bandits", 0, 0, 0, 0, 0, 0, 1, 1, 1),

	("pic_sea_raiders", 0, "pic_sea_raiders", 0, 0, 0, 0, 0, 0, 1, 1, 1),

	("pic_deserters", 0, "pic_deserters", 0, 0, 0, 0, 0, 0, 1, 1, 1),

	("pic_forest_bandits", 0, "pic_forest_bandits", 0, 0, 0, 0, 0, 0, 1, 1, 1),

	("pic_cattle", 0, "pic_cattle", 0, 0, 0, 0, 0, 0, 1, 1, 1),

	("pic_looted_village", 0, "pic_looted_village", 0, 0, 0, 0, 0, 0, 1, 1, 1),

	("pic_village_p", 0, "pic_village_p", 0, 0, 0, 0, 0, 0, 1, 1, 1),

	("pic_village_s", 0, "pic_village_s", 0, 0, 0, 0, 0, 0, 1, 1, 1),

	("pic_village_w", 0, "pic_village_w", 0, 0, 0, 0, 0, 0, 1, 1, 1),

	("pic_recruits", 0, "pic_recruits", 0, 0, 0, 0, 0, 0, 1, 1, 1),

	("pic_arms_swadian", 0, "pic_arms_swadian", 0, 0, 0, 0, 0, 0, 1, 1, 1),

	("pic_arms_vaegir", 0, "pic_arms_vaegir", 0, 0, 0, 0, 0, 0, 1, 1, 1),

	("pic_arms_khergit", 0, "pic_arms_khergit", 0, 0, 0, 0, 0, 0, 1, 1, 1),

	("pic_arms_nord", 0, "pic_arms_nord", 0, 0, 0, 0, 0, 0, 1, 1, 1),

	("pic_arms_rhodok", 0, "pic_arms_rhodok", 0, 0, 0, 0, 0, 0, 1, 1, 1),

	("pic_sarranid_arms", 0, "pic_sarranid_arms", 0, 0, 0, 0, 0, 0, 1, 1, 1),

	("pic_arms_dragonstone", 0, "pic_arms_dragonstone", 0, 0, 0, 0, 0, 0, 1, 1, 1),

	("pic_arms_westerlands", 0, "pic_arms_westerlands", 0, 0, 0, 0, 0, 0, 1, 1, 1),

	("pic_arms_reach", 0, "pic_arms_reach", 0, 0, 0, 0, 0, 0, 1, 1, 1),

	("pic_arms_ironborn", 0, "pic_arms_ironborn", 0, 0, 0, 0, 0, 0, 1, 1, 1),

	("pic_arms_pentos", 0, "pic_arms_pentos", 0, 0, 0, 0, 0, 0, 1, 1, 1),

	("pic_arms_tyrosh", 0, "pic_arms_tyrosh", 0, 0, 0, 0, 0, 0, 1, 1, 1),

	("pic_arms_myr", 0, "pic_arms_myr", 0, 0, 0, 0, 0, 0, 1, 1, 1),

	("pic_arms_lys", 0, "pic_arms_lys", 0, 0, 0, 0, 0, 0, 1, 1, 1),

	("pic_arms_volantis", 0, "pic_arms_volantis", 0, 0, 0, 0, 0, 0, 1, 1, 1),

	("pic_arms_norvos", 0, "pic_arms_norvos", 0, 0, 0, 0, 0, 0, 1, 1, 1),

	("pic_arms_lorath", 0, "pic_arms_lorath", 0, 0, 0, 0, 0, 0, 1, 1, 1),

	("pic_arms_sisters", 0, "pic_arms_sisters", 0, 0, 0, 0, 0, 0, 1, 1, 1),

	("pic_arms_targaryen", 0, "pic_arms_targaryen", 0, 0, 0, 0, 0, 0, 1, 1, 1),

	("pic_castle1", 0, "pic_castle1", 0, 0, 0, 0, 0, 0, 1, 1, 1),

	("pic_castledes", 0, "pic_castledes", 0, 0, 0, 0, 0, 0, 1, 1, 1),

	("pic_castlesnow", 0, "pic_castlesnow", 0, 0, 0, 0, 0, 0, 1, 1, 1),

	("pic_charge", 0, "pic_charge", 0, 0, 0, 0, 0, 0, 1, 1, 1),

	("pic_khergit", 0, "pic_khergit", 0, 0, 0, 0, 0, 0, 1, 1, 1),

	("pic_nord", 0, "pic_nord", 0, 0, 0, 0, 0, 0, 1, 1, 1),

	("pic_rhodock", 0, "pic_rhodock", 0, 0, 0, 0, 0, 0, 1, 1, 1),

	("pic_sally_out", 0, "pic_sally_out", 0, 0, 0, 0, 0, 0, 1, 1, 1),

	("pic_siege_attack", 0, "pic_siege_attack", 0, 0, 0, 0, 0, 0, 1, 1, 1),

	("pic_swad", 0, "pic_swad", 0, 0, 0, 0, 0, 0, 1, 1, 1),

	("pic_town1", 0, "pic_town1", 0, 0, 0, 0, 0, 0, 1, 1, 1),

	("pic_towndes", 0, "pic_towndes", 0, 0, 0, 0, 0, 0, 1, 1, 1),

	("pic_townriot", 0, "pic_townriot", 0, 0, 0, 0, 0, 0, 1, 1, 1),

	("pic_townsnow", 0, "pic_townsnow", 0, 0, 0, 0, 0, 0, 1, 1, 1),

	("pic_vaegir", 0, "pic_vaegir", 0, 0, 0, 0, 0, 0, 1, 1, 1),

	("pic_villageriot", 0, "pic_villageriot", 0, 0, 0, 0, 0, 0, 1, 1, 1),

	("pic_sarranid_encounter", 0, "pic_sarranid_encounter", 0, 0, 0, 0, 0, 0, 1, 1, 1),

	("pic_game_event_walking_woods", 0, "pic_game_event_walking_woods", 0, 0, 0, 0, 0, 0, 1, 1, 1),

	("pic_event_raven_message", 0, "pic_event_raven_message", 0, 0, 0, 0, 0, 0, 1, 1, 1),

	("pic_event_ruins", 0, "pic_event_ruins", 0, 0, 0, 0, 0, 0, 1, 1, 1),

	("pic_event_cave", 0, "pic_event_cave", 0, 0, 0, 0, 0, 0, 1, 1, 1),

	("pic_event_wall", 0, "pic_event_wall", 0, 0, 0, 0, 0, 0, 1, 1, 1),

	("pic_event_slavers_bay", 0, "pic_event_slavers_bay", 0, 0, 0, 0, 0, 0, 1, 1, 1),

	("pic_event_septry", 0, "pic_event_septry", 0, 0, 0, 0, 0, 0, 1, 1, 1),

	("pic_event_ship", 0, "pic_event_ship", 0, 0, 0, 0, 0, 0, 1, 1, 1),

	("pic_event_ruins", 0, "pic_event_ruins", 0, 0, 0, 0, 0, 0, 1, 1, 1),

	("pic_game_event_whore", 0, "pic_game_event_whore", 0, 0, 0, 0, 0, 0, 1, 1, 1),

	("pic_game_event_beggar", 0, "pic_game_event_beggar", 0, 0, 0, 0, 0, 0, 1, 1, 1),

	("pic_game_event_hunt", 0, "pic_game_event_hunt", 0, 0, 0, 0, 0, 0, 1, 1, 1),

	("pic_game_event_crowd", 0, "pic_game_event_crowd", 0, 0, 0, 0, 0, 0, 1, 1, 1),

	("pic_game_event_village_life", 0, "pic_game_event_village_life", 0, 0, 0, 0, 0, 0, 1, 1, 1),

	("pic_game_event_feast", 0, "pic_game_event_feast", 0, 0, 0, 0, 0, 0, 1, 1, 1),

	("pic_game_event_sovereign", 0, "pic_game_event_sovereign", 0, 0, 0, 0, 0, 0, 1, 1, 1),

	("pic_game_event_ship", 0, "pic_game_event_ship", 0, 0, 0, 0, 0, 0, 1, 1, 1),

	("pic_game_event_negative_event", 0, "pic_game_event_negative_event", 0, 0, 0, 0, 0, 0, 1, 1, 1),

	("pic_game_event_desert", 0, "pic_game_event_desert", 0, 0, 0, 0, 0, 0, 1, 1, 1),

	("pic_game_event_law", 0, "pic_game_event_law", 0, 0, 0, 0, 0, 0, 1, 1, 1),

	("pic_game_event_noble", 0, "pic_game_event_noble", 0, 0, 0, 0, 0, 0, 1, 1, 1),

	("pic_game_event_horror", 0, "pic_game_event_horror", 0, 0, 0, 0, 0, 0, 1, 1, 1),

	("pic_game_event_coronation", 0, "pic_game_event_coronation", 0, 0, 0, 0, 0, 0, 1, 1, 1),

	("pic_game_event_stormlands", 0, "pic_game_event_stormlands", 0, 0, 0, 0, 0, 0, 1, 1, 1),

	("pic_game_event_north", 0, "pic_game_event_north", 0, 0, 0, 0, 0, 0, 1, 1, 1),

	("pic_game_event_vale", 0, "pic_game_event_vale", 0, 0, 0, 0, 0, 0, 1, 1, 1),

	("pic_game_event_braavos", 0, "pic_game_event_braavos", 0, 0, 0, 0, 0, 0, 1, 1, 1),

	("pic_game_event_dorne", 0, "pic_game_event_dorne", 0, 0, 0, 0, 0, 0, 1, 1, 1),

	("pic_game_event_dragonstone", 0, "pic_game_event_dragonstone", 0, 0, 0, 0, 0, 0, 1, 1, 1),

	("pic_game_event_westerlands", 0, "pic_game_event_westerlands", 0, 0, 0, 0, 0, 0, 1, 1, 1),

	("pic_game_event_reach", 0, "pic_game_event_reach", 0, 0, 0, 0, 0, 0, 1, 1, 1),

	("pic_game_event_ironborn", 0, "pic_game_event_ironborn", 0, 0, 0, 0, 0, 0, 1, 1, 1),

	("pic_game_event_three_sisters", 0, "pic_game_event_three_sisters", 0, 0, 0, 0, 0, 0, 1, 1, 1),

	("pic_game_event_disputed_lands", 0, "pic_game_event_disputed_lands", 0, 0, 0, 0, 0, 0, 1, 1, 1),

	("pic_game_event_volantis", 0, "pic_game_event_volantis", 0, 0, 0, 0, 0, 0, 1, 1, 1),

	("pic_game_event_lorath", 0, "pic_game_event_lorath", 0, 0, 0, 0, 0, 0, 1, 1, 1),

	("pic_game_event_pentos", 0, "pic_game_event_pentos", 0, 0, 0, 0, 0, 0, 1, 1, 1),

	("pic_game_event_crown", 0, "pic_game_event_crown", 0, 0, 0, 0, 0, 0, 1, 1, 1),

	("pic_outlaws", 0, "pic_outlaws", 0, 0, 0, 0, 0, 0, 1, 1, 1),

	("pic_desert_outlaws", 0, "pic_desert_outlaws", 0, 0, 0, 0, 0, 0, 1, 1, 1),

	("pic_clansmen", 0, "pic_clansmen", 0, 0, 0, 0, 0, 0, 1, 1, 1),

	("pic_rhoyne_outlaws", 0, "pic_rhoyne_outlaws", 0, 0, 0, 0, 0, 0, 1, 1, 1),

	("pic_slavers", 0, "pic_slavers", 0, 0, 0, 0, 0, 0, 1, 1, 1),

	("pic_raiders", 0, "pic_raiders", 0, 0, 0, 0, 0, 0, 1, 1, 1),

	("pic_crannogmen", 0, "pic_crannogmen", 0, 0, 0, 0, 0, 0, 1, 1, 1),

	("menu_faq_window", 0, "menu_faq_window", 0, 0, 0, 0, 0, 0, 1, 1, 1),

	("mp_score_a", 0, "mp_score_a", 0, 0, 0, 0, 0, 0, 1, 1, 1),

	("mp_score_b", 0, "mp_score_b", 0, 0, 0, 0, 0, 0, 1, 1, 1),

	("portrait_blend_out", 0, "portrait_blend_out", 0, 0, 0, 0, 0, 0, 1, 1, 1),

	("load_window", 0, "load_window", 0, 0, 0, 0, 0, 0, 1, 1, 1),

	("checkbox_off", render_order_plus_1, "checkbox_off", 0, 0, 0, 0, 0, 0, 1, 1, 1),

	("checkbox_on", render_order_plus_1, "checkbox_on", 0, 0, 0, 0, 0, 0, 1, 1, 1),

	("white_plane", 0, "white_plane", 0, 0, 0, 0, 0, 0, 1, 1, 1),

	("white_dot", 0, "white_dot", 0, 0, 0, 0, 0, 0, 1, 1, 1),

	("player_dot", 0, "player_dot", 0, 0, 0, 0, 0, 0, 1, 1, 1),

	("flag_infantry", 0, "flag3_infantry", 0, 0, 0, 0, 0, 0, 1, 1, 1),

	("flag_archers", 0, "flag1_archers", 0, 0, 0, 0, 0, 0, 1, 1, 1),

	("flag_cavalry", 0, "flag2_cavalry", 0, 0, 0, 0, 0, 0, 1, 1, 1),

	("inv_slot", 0, "inv_slot", 0, 0, 0, 0, 0, 0, 1, 1, 1),

	("mp_ingame_menu", 0, "mp_ingame_menu", 0, 0, 0, 0, 0, 0, 1, 1, 1),

	("mp_inventory_left", 0, "mp_inventory_left", 0, 0, 0, 0, 0, 0, 1, 1, 1),

	("mp_inventory_right", 0, "mp_inventory_right", 0, 0, 0, 0, 0, 0, 1, 1, 1),

	("mp_inventory_choose", 0, "mp_inventory_choose", 0, 0, 0, 0, 0, 0, 1, 1, 1),

	("mp_inventory_slot_glove", 0, "mp_inventory_slot_glove", 0, 0, 0, 0, 0, 0, 1, 1, 1),

	("mp_inventory_slot_horse", 0, "mp_inventory_slot_horse", 0, 0, 0, 0, 0, 0, 1, 1, 1),

	("mp_inventory_slot_armor", 0, "mp_inventory_slot_armor", 0, 0, 0, 0, 0, 0, 1, 1, 1),

	("mp_inventory_slot_helmet", 0, "mp_inventory_slot_helmet", 0, 0, 0, 0, 0, 0, 1, 1, 1),

	("mp_inventory_slot_boot", 0, "mp_inventory_slot_boot", 0, 0, 0, 0, 0, 0, 1, 1, 1),

	("mp_inventory_slot_empty", 0, "mp_inventory_slot_empty", 0, 0, 0, 0, 0, 0, 1, 1, 1),

	("mp_inventory_slot_equip", 0, "mp_inventory_slot_equip", 0, 0, 0, 0, 0, 0, 1, 1, 1),

	("mp_inventory_left_arrow", 0, "mp_inventory_left_arrow", 0, 0, 0, 0, 0, 0, 1, 1, 1),

	("mp_inventory_right_arrow", 0, "mp_inventory_right_arrow", 0, 0, 0, 0, 0, 0, 1, 1, 1),

	("mp_ui_host_main", 0, "mp_ui_host_main", 0, 0, 0, 0, 0, 0, 1, 1, 1),

	("mp_ui_host_maps_1", 0, "mp_ui_host_maps_a1", 0, 0, 0, 0, 0, 0, 1, 1, 1),

	("mp_ui_host_maps_2", 0, "mp_ui_host_maps_a2", 0, 0, 0, 0, 0, 0, 1, 1, 1),

	("mp_ui_host_maps_3", 0, "mp_ui_host_maps_c", 0, 0, 0, 0, 0, 0, 1, 1, 1),

	("mp_ui_host_maps_4", 0, "mp_ui_host_maps_ruinedf", 0, 0, 0, 0, 0, 0, 1, 1, 1),

	("mp_ui_host_maps_5", 0, "mp_ui_host_maps_a1", 0, 0, 0, 0, 0, 0, 1, 1, 1),

	("mp_ui_host_maps_6", 0, "mp_ui_host_maps_a1", 0, 0, 0, 0, 0, 0, 1, 1, 1),

	("mp_ui_host_maps_7", 0, "mp_ui_host_maps_fieldby", 0, 0, 0, 0, 0, 0, 1, 1, 1),

	("mp_ui_host_maps_8", 0, "mp_ui_host_maps_castle2", 0, 0, 0, 0, 0, 0, 1, 1, 1),

	("mp_ui_host_maps_9", 0, "mp_ui_host_maps_snovyv", 0, 0, 0, 0, 0, 0, 1, 1, 1),

	("mp_ui_host_maps_10", 0, "mp_ui_host_maps_castle3", 0, 0, 0, 0, 0, 0, 1, 1, 1),

	("mp_ui_host_maps_11", 0, "mp_ui_host_maps_c1", 0, 0, 0, 0, 0, 0, 1, 1, 1),

	("mp_ui_host_maps_12", 0, "mp_ui_host_maps_c2", 0, 0, 0, 0, 0, 0, 1, 1, 1),

	("mp_ui_host_maps_13", 0, "mp_ui_host_maps_c3", 0, 0, 0, 0, 0, 0, 1, 1, 1),

	("mp_ui_host_maps_randomp", 0, "mp_ui_host_maps_randomp", 0, 0, 0, 0, 0, 0, 1, 1, 1),

	("mp_ui_host_maps_randoms", 0, "mp_ui_host_maps_randoms", 0, 0, 0, 0, 0, 0, 1, 1, 1),

	("mp_ui_command_panel", 0, "mp_ui_command_panel", 0, 0, 0, 0, 0, 0, 1, 1, 1),

	("mp_ui_command_border_l", 0, "mp_ui_command_border_l", 0, 0, 0, 0, 0, 0, 1, 1, 1),

	("mp_ui_command_border_r", 0, "mp_ui_command_border_r", 0, 0, 0, 0, 0, 0, 1, 1, 1),

	("mp_ui_welcome_panel", 0, "mp_ui_welcome_panel", 0, 0, 0, 0, 0, 0, 1, 1, 1),

	("flag_project_sw", 0, "flag_project_sw", 0, 0, 0, 0, 0, 0, 1, 1, 1),

	("flag_project_vg", 0, "flag_project_vg", 0, 0, 0, 0, 0, 0, 1, 1, 1),

	("flag_project_kh", 0, "flag_project_kh", 0, 0, 0, 0, 0, 0, 1, 1, 1),

	("flag_project_nd", 0, "flag_project_nd", 0, 0, 0, 0, 0, 0, 1, 1, 1),

	("flag_project_rh", 0, "flag_project_rh", 0, 0, 0, 0, 0, 0, 1, 1, 1),

	("flag_project_sr", 0, "flag_project_sr", 0, 0, 0, 0, 0, 0, 1, 1, 1),

	("flag_projects_end", 0, "0", 0, 0, 0, 0, 0, 0, 1, 1, 1),

	("flag_project_sw_miss", 0, "flag_project_sw_miss", 0, 0, 0, 0, 0, 0, 1, 1, 1),

	("flag_project_vg_miss", 0, "flag_project_vg_miss", 0, 0, 0, 0, 0, 0, 1, 1, 1),

	("flag_project_kh_miss", 0, "flag_project_kh_miss", 0, 0, 0, 0, 0, 0, 1, 1, 1),

	("flag_project_nd_miss", 0, "flag_project_nd_miss", 0, 0, 0, 0, 0, 0, 1, 1, 1),

	("flag_project_rh_miss", 0, "flag_project_rh_miss", 0, 0, 0, 0, 0, 0, 1, 1, 1),

	("flag_project_sr_miss", 0, "flag_project_sr_miss", 0, 0, 0, 0, 0, 0, 1, 1, 1),

	("flag_project_misses_end", 0, "0", 0, 0, 0, 0, 0, 0, 1, 1, 1),

	("color_picker", 0, "color_picker", 0, 0, 0, 0, 0, 0, 1, 1, 1),

	("custom_map_banner_01", 0, "custom_map_banner_01", 0, 0, 0, -90, 0, 90, 1, 1, 1),

	("custom_map_banner_02", 0, "custom_map_banner_02", 0, 0, 0, -90, 0, 90, 1, 1, 1),

	("custom_map_banner_03", 0, "custom_map_banner_03", 0, 0, 0, -90, 0, 90, 1, 1, 1),

	("custom_banner_01", 0, "custom_banner_01", 0, 0, 0, -90, 0, 0, 1, 1, 1),

	("custom_banner_02", 0, "custom_banner_02", 0, 0, 0, -90, 0, 0, 1, 1, 1),

	("custom_banner_bg", 0, "custom_banner_bg", 0, 0, 0, 0, 0, 0, 10, 10, 10),

	("custom_banner_fg01", 0, "custom_banner_fg01", 0, 0, 0, 0, 0, 0, 10, 10, 10),

	("custom_banner_fg02", 0, "custom_banner_fg02", 0, 0, 0, 0, 0, 0, 10, 10, 10),

	("custom_banner_fg03", 0, "custom_banner_fg03", 0, 0, 0, 0, 0, 0, 10, 10, 10),

	("custom_banner_fg04", 0, "custom_banner_fg04", 0, 0, 0, 0, 0, 0, 10, 10, 10),

	("custom_banner_fg05", 0, "custom_banner_fg05", 0, 0, 0, 0, 0, 0, 10, 10, 10),

	("custom_banner_fg06", 0, "custom_banner_fg06", 0, 0, 0, 0, 0, 0, 10, 10, 10),

	("custom_banner_fg07", 0, "custom_banner_fg07", 0, 0, 0, 0, 0, 0, 10, 10, 10),

	("custom_banner_fg08", 0, "custom_banner_fg08", 0, 0, 0, 0, 0, 0, 10, 10, 10),

	("custom_banner_fg09", 0, "custom_banner_fg09", 0, 0, 0, 0, 0, 0, 10, 10, 10),

	("custom_banner_fg10", 0, "custom_banner_fg10", 0, 0, 0, 0, 0, 0, 10, 10, 10),

	("custom_banner_fg11", 0, "custom_banner_fg11", 0, 0, 0, 0, 0, 0, 10, 10, 10),

	("custom_banner_fg12", 0, "custom_banner_fg12", 0, 0, 0, 0, 0, 0, 10, 10, 10),

	("custom_banner_fg13", 0, "custom_banner_fg13", 0, 0, 0, 0, 0, 0, 10, 10, 10),

	("custom_banner_fg14", 0, "custom_banner_fg14", 0, 0, 0, 0, 0, 0, 10, 10, 10),

	("custom_banner_fg15", 0, "custom_banner_fg15", 0, 0, 0, 0, 0, 0, 10, 10, 10),

	("custom_banner_fg16", 0, "custom_banner_fg16", 0, 0, 0, 0, 0, 0, 10, 10, 10),

	("custom_banner_fg17", 0, "custom_banner_fg17", 0, 0, 0, 0, 0, 0, 10, 10, 10),

	("custom_banner_fg18", 0, "custom_banner_fg18", 0, 0, 0, 0, 0, 0, 10, 10, 10),

	("custom_banner_fg19", 0, "custom_banner_fg19", 0, 0, 0, 0, 0, 0, 10, 10, 10),

	("custom_banner_fg20", 0, "custom_banner_fg20", 0, 0, 0, 0, 0, 0, 10, 10, 10),

	("custom_banner_fg21", 0, "custom_banner_fg21", 0, 0, 0, 0, 0, 0, 10, 10, 10),

	("custom_banner_fg22", 0, "custom_banner_fg22", 0, 0, 0, 0, 0, 0, 10, 10, 10),

	("custom_banner_fg23", 0, "custom_banner_fg23", 0, 0, 0, 0, 0, 0, 10, 10, 10),

	("custom_banner_charge_01", 0, "custom_banner_charge_01", 0, 0, 0, 0, 0, 0, 10, 10, 10),

	("custom_banner_charge_02", 0, "custom_banner_charge_02", 0, 0, 0, 0, 0, 0, 10, 10, 10),

	("custom_banner_charge_03", 0, "custom_banner_charge_03", 0, 0, 0, 0, 0, 0, 10, 10, 10),

	("custom_banner_charge_04", 0, "custom_banner_charge_04", 0, 0, 0, 0, 0, 0, 10, 10, 10),

	("custom_banner_charge_05", 0, "custom_banner_charge_05", 0, 0, 0, 0, 0, 0, 10, 10, 10),

	("custom_banner_charge_06", 0, "custom_banner_charge_06", 0, 0, 0, 0, 0, 0, 10, 10, 10),

	("custom_banner_charge_07", 0, "custom_banner_charge_07", 0, 0, 0, 0, 0, 0, 10, 10, 10),

	("custom_banner_charge_08", 0, "custom_banner_charge_08", 0, 0, 0, 0, 0, 0, 10, 10, 10),

	("custom_banner_charge_09", 0, "custom_banner_charge_09", 0, 0, 0, 0, 0, 0, 10, 10, 10),

	("custom_banner_charge_10", 0, "custom_banner_charge_10", 0, 0, 0, 0, 0, 0, 10, 10, 10),

	("custom_banner_charge_11", 0, "custom_banner_charge_11", 0, 0, 0, 0, 0, 0, 10, 10, 10),

	("custom_banner_charge_12", 0, "custom_banner_charge_12", 0, 0, 0, 0, 0, 0, 10, 10, 10),

	("custom_banner_charge_13", 0, "custom_banner_charge_13", 0, 0, 0, 0, 0, 0, 10, 10, 10),

	("custom_banner_charge_14", 0, "custom_banner_charge_14", 0, 0, 0, 0, 0, 0, 10, 10, 10),

	("custom_banner_charge_15", 0, "custom_banner_charge_15", 0, 0, 0, 0, 0, 0, 10, 10, 10),

	("custom_banner_charge_16", 0, "custom_banner_charge_16", 0, 0, 0, 0, 0, 0, 10, 10, 10),

	("custom_banner_charge_17", 0, "custom_banner_charge_17", 0, 0, 0, 0, 0, 0, 10, 10, 10),

	("custom_banner_charge_18", 0, "custom_banner_charge_18", 0, 0, 0, 0, 0, 0, 10, 10, 10),

	("custom_banner_charge_19", 0, "custom_banner_charge_19", 0, 0, 0, 0, 0, 0, 10, 10, 10),

	("custom_banner_charge_20", 0, "custom_banner_charge_20", 0, 0, 0, 0, 0, 0, 10, 10, 10),

	("custom_banner_charge_21", 0, "custom_banner_charge_21", 0, 0, 0, 0, 0, 0, 10, 10, 10),

	("custom_banner_charge_22", 0, "custom_banner_charge_22", 0, 0, 0, 0, 0, 0, 10, 10, 10),

	("custom_banner_charge_23", 0, "custom_banner_charge_23", 0, 0, 0, 0, 0, 0, 10, 10, 10),

	("custom_banner_charge_24", 0, "custom_banner_charge_24", 0, 0, 0, 0, 0, 0, 10, 10, 10),

	("custom_banner_charge_25", 0, "custom_banner_charge_25", 0, 0, 0, 0, 0, 0, 10, 10, 10),

	("custom_banner_charge_26", 0, "custom_banner_charge_26", 0, 0, 0, 0, 0, 0, 10, 10, 10),

	("custom_banner_charge_27", 0, "custom_banner_charge_27", 0, 0, 0, 0, 0, 0, 10, 10, 10),

	("custom_banner_charge_28", 0, "custom_banner_charge_28", 0, 0, 0, 0, 0, 0, 10, 10, 10),

	("custom_banner_charge_29", 0, "custom_banner_charge_29", 0, 0, 0, 0, 0, 0, 10, 10, 10),

	("custom_banner_charge_30", 0, "custom_banner_charge_30", 0, 0, 0, 0, 0, 0, 10, 10, 10),

	("custom_banner_charge_31", 0, "custom_banner_charge_31", 0, 0, 0, 0, 0, 0, 10, 10, 10),

	("custom_banner_charge_32", 0, "custom_banner_charge_32", 0, 0, 0, 0, 0, 0, 10, 10, 10),

	("custom_banner_charge_33", 0, "custom_banner_charge_33", 0, 0, 0, 0, 0, 0, 10, 10, 10),

	("custom_banner_charge_34", 0, "custom_banner_charge_34", 0, 0, 0, 0, 0, 0, 10, 10, 10),

	("custom_banner_charge_35", 0, "custom_banner_charge_35", 0, 0, 0, 0, 0, 0, 10, 10, 10),

	("custom_banner_charge_36", 0, "custom_banner_charge_36", 0, 0, 0, 0, 0, 0, 10, 10, 10),

	("custom_banner_charge_37", 0, "custom_banner_charge_37", 0, 0, 0, 0, 0, 0, 10, 10, 10),

	("custom_banner_charge_38", 0, "custom_banner_charge_38", 0, 0, 0, 0, 0, 0, 10, 10, 10),

	("custom_banner_charge_39", 0, "custom_banner_charge_39", 0, 0, 0, 0, 0, 0, 10, 10, 10),

	("custom_banner_charge_40", 0, "custom_banner_charge_40", 0, 0, 0, 0, 0, 0, 10, 10, 10),

	("custom_banner_charge_41", 0, "custom_banner_charge_41", 0, 0, 0, 0, 0, 0, 10, 10, 10),

	("custom_banner_charge_42", 0, "custom_banner_charge_42", 0, 0, 0, 0, 0, 0, 10, 10, 10),

	("custom_banner_charge_43", 0, "custom_banner_charge_43", 0, 0, 0, 0, 0, 0, 10, 10, 10),

	("custom_banner_charge_44", 0, "custom_banner_charge_44", 0, 0, 0, 0, 0, 0, 10, 10, 10),

	("custom_banner_charge_45", 0, "custom_banner_charge_45", 0, 0, 0, 0, 0, 0, 10, 10, 10),

	("custom_banner_charge_46", 0, "custom_banner_charge_46", 0, 0, 0, 0, 0, 0, 10, 10, 10),

	("tableau_mesh_custom_banner", 0, "tableau_mesh_custom_banner", 0, 0, 0, 0, 0, 0, 10, 10, 10),

	("tableau_mesh_custom_banner_square", 0, "tableau_mesh_custom_banner_square", 0, 0, 0, 0, 0, 0, 10, 10, 10),

	("tableau_mesh_custom_banner_tall", 0, "tableau_mesh_custom_banner_tall", 0, 0, 0, 0, 0, 0, 10, 10, 10),

	("tableau_mesh_custom_banner_short", 0, "tableau_mesh_custom_banner_short", 0, 0, 0, 0, 0, 0, 10, 10, 10),

	("tableau_mesh_shield_round_1", 0, "tableau_mesh_shield_round_1", 0, 0, 0, 0, 0, 0, 10, 10, 10),

	("tableau_mesh_shield_round_2", 0, "tableau_mesh_shield_round_2", 0, 0, 0, 0, 0, 0, 10, 10, 10),

	("tableau_mesh_shield_round_3", 0, "tableau_mesh_shield_round_3", 0, 0, 0, 0, 0, 0, 10, 10, 10),

	("tableau_mesh_shield_round_4", 0, "tableau_mesh_shield_round_4", 0, 0, 0, 0, 0, 0, 10, 10, 10),

	("tableau_mesh_shield_round_5", 0, "tableau_mesh_shield_round_5", 0, 0, 0, 0, 0, 0, 10, 10, 10),

	("tableau_mesh_shield_small_round_1", 0, "tableau_mesh_shield_small_round_1", 0, 0, 0, 0, 0, 0, 10, 10, 10),

	("tableau_mesh_shield_small_round_2", 0, "tableau_mesh_shield_small_round_2", 0, 0, 0, 0, 0, 0, 10, 10, 10),

	("tableau_mesh_shield_small_round_3", 0, "tableau_mesh_shield_small_round_3", 0, 0, 0, 0, 0, 0, 10, 10, 10),

	("tableau_mesh_shield_kite_1", 0, "tableau_mesh_shield_kite_1", 0, 0, 0, 0, 0, 0, 10, 10, 10),

	("tableau_mesh_shield_kite_2", 0, "tableau_mesh_shield_kite_2", 0, 0, 0, 0, 0, 0, 10, 10, 10),

	("tableau_mesh_shield_kite_3", 0, "tableau_mesh_shield_kite_3", 0, 0, 0, 0, 0, 0, 10, 10, 10),

	("tableau_mesh_shield_kite_4", 0, "tableau_mesh_shield_kite_4", 0, 0, 0, 0, 0, 0, 10, 10, 10),

	("tableau_mesh_shield_heater_1", 0, "tableau_mesh_shield_heater_1", 0, 0, 0, 0, 0, 0, 10, 10, 10),

	("tableau_mesh_shield_heater_2", 0, "tableau_mesh_shield_heater_2", 0, 0, 0, 0, 0, 0, 10, 10, 10),

	("tableau_mesh_shield_pavise_1", 0, "tableau_mesh_shield_pavise_1", 0, 0, 0, 0, 0, 0, 10, 10, 10),

	("tableau_mesh_shield_pavise_2", 0, "tableau_mesh_shield_pavise_2", 0, 0, 0, 0, 0, 0, 10, 10, 10),

	("heraldic_armor_bg", 0, "heraldic_armor_bg", 0, 0, 0, 0, 0, 0, 10, 10, 10),

	("tableau_mesh_heraldic_armor_a", 0, "tableau_mesh_heraldic_armor_a", 0, 0, 0, 0, 0, 0, 1, 1, 1),

	("tableau_mesh_heraldic_armor_b", 0, "tableau_mesh_heraldic_armor_b", 0, 0, 0, 0, 0, 0, 1, 1, 1),

	("tableau_mesh_heraldic_armor_c", 0, "tableau_mesh_heraldic_armor_c", 0, 0, 0, 0, 0, 0, 1, 1, 1),

	("tableau_mesh_heraldic_armor_d", 0, "tableau_mesh_heraldic_armor_d", 0, 0, 0, 0, 0, 0, 1, 1, 1),

	("ar_pla_t6_heraldic_tableau_banner", 0, "ar_pla_t6_heraldic_tableau_banner", 0, 0, 0, 0, 0, 0, 1, 1, 1),

	("ar_pla_t6_heraldic_tableau", 0, "ar_pla_t6_heraldic_tableau", 0, 0, 0, 0, 0, 0, 1, 1, 1),

	("tableau_mesh_heraldic_shirt_banner", 0, "tableau_mesh_heraldic_shirt_banner", 0, 0, 0, 0, 0, 0, 1, 1, 1),

	("tableau_mesh_heraldic_shirt", 0, "tableau_mesh_heraldic_shirt", 0, 0, 0, 0, 0, 0, 1, 1, 1),

	("tableau_mesh_heraldic_tabard_banner", 0, "tableau_mesh_heraldic_tabard_banner", 0, 0, 0, 0, 0, 0, 1, 1, 1),

	("tableau_mesh_heraldic_tabard", 0, "tableau_mesh_heraldic_tabard", 0, 0, 0, 0, 0, 0, 1, 1, 1),

	("tableau_mesh_heraldic_mail_and_plate_banner", 0, "tableau_mesh_heraldic_mail_and_plate_banner", 0, 0, 0, 0, 0, 0, 1, 1, 1),

	("tableau_mesh_heraldic_mail_and_plate", 0, "tableau_mesh_heraldic_mail_and_plate", 0, 0, 0, 0, 0, 0, 1, 1, 1),

	("tableau_mesh_heraldic_light_mail_and_plate_banner", 0, "tableau_mesh_heraldic_light_mail_and_plate_banner", 0, 0, 0, 0, 0, 0, 1, 1, 1),

	("tableau_mesh_heraldic_light_mail_and_plate", 0, "tableau_mesh_heraldic_light_mail_and_plate", 0, 0, 0, 0, 0, 0, 1, 1, 1),

	("tableau_mesh_heraldic_cuir_bouilli_banner", 0, "tableau_mesh_heraldic_cuir_bouilli_banner", 0, 0, 0, 0, 0, 0, 1, 1, 1),

	("tableau_mesh_heraldic_cuir_bouilli", 0, "tableau_mesh_heraldic_cuir_bouilli", 0, 0, 0, 0, 0, 0, 1, 1, 1),

	("tableau_mesh_heraldic_padded_cloth_banner", 0, "tableau_mesh_heraldic_padded_cloth_banner", 0, 0, 0, 0, 0, 0, 1, 1, 1),

	("tableau_mesh_heraldic_padded_cloth", 0, "tableau_mesh_heraldic_padded_cloth", 0, 0, 0, 0, 0, 0, 1, 1, 1),

	("tableau_mesh_costumes6_banner", 0, "tableau_mesh_costumes6_banner", 0, 0, 0, 0, 0, 0, 1, 1, 1),

	("tableau_mesh_costumes6", 0, "tableau_mesh_costumes6", 0, 0, 0, 0, 0, 0, 1, 1, 1),

	("tableau_mesh_costumes9_banner", 0, "tableau_mesh_costumes9_banner", 0, 0, 0, 0, 0, 0, 1, 1, 1),

	("tableau_mesh_costumes9", 0, "tableau_mesh_costumes9", 0, 0, 0, 0, 0, 0, 1, 1, 1),

	("tableau_mesh_cor_banner", 0, "tableau_mesh_cor_banner", 0, 0, 0, 0, 0, 0, 1, 1, 1),

	("tableau_mesh_cor", 0, "tableau_mesh_cor", 0, 0, 0, 0, 0, 0, 1, 1, 1),

	("tableau_mesh_mail_long_surcoat_new_heraldic", 0, "tableau_mesh_mail_long_surcoat_new_heraldic", 0, 0, 0, 0, 0, 0, 1, 1, 1),

	("tableau_mesh_brigandine_b_heraldic", 0, "tableau_mesh_brigandine_b_heraldic", 0, 0, 0, 0, 0, 0, 1, 1, 1),

	("tableau_mesh_heraldic_tunic_new", 0, "tableau_mesh_heraldic_tunic_new", 0, 0, 0, 0, 0, 0, 1, 1, 1),

	("banner_a01", 0, "banner_a01", 0, 0, 0, -90, 0, 0, 1, 1, 1),

	("banner_a02", 0, "banner_a02", 0, 0, 0, -90, 0, 0, 1, 1, 1),

	("banner_a03", 0, "banner_a03", 0, 0, 0, -90, 0, 0, 1, 1, 1),

	("banner_a04", 0, "banner_a04", 0, 0, 0, -90, 0, 0, 1, 1, 1),

	("banner_a05", 0, "banner_a05", 0, 0, 0, -90, 0, 0, 1, 1, 1),

	("banner_a06", 0, "banner_a06", 0, 0, 0, -90, 0, 0, 1, 1, 1),

	("banner_a07", 0, "banner_a07", 0, 0, 0, -90, 0, 0, 1, 1, 1),

	("banner_a08", 0, "banner_a08", 0, 0, 0, -90, 0, 0, 1, 1, 1),

	("banner_a09", 0, "banner_a09", 0, 0, 0, -90, 0, 0, 1, 1, 1),

	("banner_a10", 0, "banner_a10", 0, 0, 0, -90, 0, 0, 1, 1, 1),

	("banner_a11", 0, "banner_a11", 0, 0, 0, -90, 0, 0, 1, 1, 1),

	("banner_a12", 0, "banner_a12", 0, 0, 0, -90, 0, 0, 1, 1, 1),

	("banner_a13", 0, "banner_a13", 0, 0, 0, -90, 0, 0, 1, 1, 1),

	("banner_a14", 0, "banner_a14", 0, 0, 0, -90, 0, 0, 1, 1, 1),

	("banner_a15", 0, "banner_f21", 0, 0, 0, -90, 0, 0, 1, 1, 1),

	("banner_a16", 0, "banner_a16", 0, 0, 0, -90, 0, 0, 1, 1, 1),

	("banner_a17", 0, "banner_a17", 0, 0, 0, -90, 0, 0, 1, 1, 1),

	("banner_a18", 0, "banner_a18", 0, 0, 0, -90, 0, 0, 1, 1, 1),

	("banner_a19", 0, "banner_a19", 0, 0, 0, -90, 0, 0, 1, 1, 1),

	("banner_a20", 0, "banner_a20", 0, 0, 0, -90, 0, 0, 1, 1, 1),

	("banner_a21", 0, "banner_a21", 0, 0, 0, -90, 0, 0, 1, 1, 1),

	("banner_b01", 0, "banner_b01", 0, 0, 0, -90, 0, 0, 1, 1, 1),

	("banner_b02", 0, "banner_b02", 0, 0, 0, -90, 0, 0, 1, 1, 1),

	("banner_b03", 0, "banner_b03", 0, 0, 0, -90, 0, 0, 1, 1, 1),

	("banner_b04", 0, "banner_b04", 0, 0, 0, -90, 0, 0, 1, 1, 1),

	("banner_b05", 0, "banner_b05", 0, 0, 0, -90, 0, 0, 1, 1, 1),

	("banner_b06", 0, "banner_b06", 0, 0, 0, -90, 0, 0, 1, 1, 1),

	("banner_b07", 0, "banner_b07", 0, 0, 0, -90, 0, 0, 1, 1, 1),

	("banner_b08", 0, "banner_b08", 0, 0, 0, -90, 0, 0, 1, 1, 1),

	("banner_b09", 0, "banner_b09", 0, 0, 0, -90, 0, 0, 1, 1, 1),

	("banner_b10", 0, "banner_b10", 0, 0, 0, -90, 0, 0, 1, 1, 1),

	("banner_b11", 0, "banner_b11", 0, 0, 0, -90, 0, 0, 1, 1, 1),

	("banner_b12", 0, "banner_b12", 0, 0, 0, -90, 0, 0, 1, 1, 1),

	("banner_b13", 0, "banner_b13", 0, 0, 0, -90, 0, 0, 1, 1, 1),

	("banner_b14", 0, "banner_b14", 0, 0, 0, -90, 0, 0, 1, 1, 1),

	("banner_b15", 0, "banner_b15", 0, 0, 0, -90, 0, 0, 1, 1, 1),

	("banner_b16", 0, "banner_b16", 0, 0, 0, -90, 0, 0, 1, 1, 1),

	("banner_b17", 0, "banner_b17", 0, 0, 0, -90, 0, 0, 1, 1, 1),

	("banner_b18", 0, "banner_b18", 0, 0, 0, -90, 0, 0, 1, 1, 1),

	("banner_b19", 0, "banner_b19", 0, 0, 0, -90, 0, 0, 1, 1, 1),

	("banner_b20", 0, "banner_b20", 0, 0, 0, -90, 0, 0, 1, 1, 1),

	("banner_b21", 0, "banner_b21", 0, 0, 0, -90, 0, 0, 1, 1, 1),

	("banner_c01", 0, "banner_c01", 0, 0, 0, -90, 0, 0, 1, 1, 1),

	("banner_c02", 0, "banner_c02", 0, 0, 0, -90, 0, 0, 1, 1, 1),

	("banner_c03", 0, "banner_c03", 0, 0, 0, -90, 0, 0, 1, 1, 1),

	("banner_c04", 0, "banner_c04", 0, 0, 0, -90, 0, 0, 1, 1, 1),

	("banner_c05", 0, "banner_c05", 0, 0, 0, -90, 0, 0, 1, 1, 1),

	("banner_c06", 0, "banner_c06", 0, 0, 0, -90, 0, 0, 1, 1, 1),

	("banner_c07", 0, "banner_c07", 0, 0, 0, -90, 0, 0, 1, 1, 1),

	("banner_c08", 0, "banner_c08", 0, 0, 0, -90, 0, 0, 1, 1, 1),

	("banner_c09", 0, "banner_c09", 0, 0, 0, -90, 0, 0, 1, 1, 1),

	("banner_c10", 0, "banner_c10", 0, 0, 0, -90, 0, 0, 1, 1, 1),

	("banner_c11", 0, "banner_c11", 0, 0, 0, -90, 0, 0, 1, 1, 1),

	("banner_c12", 0, "banner_c12", 0, 0, 0, -90, 0, 0, 1, 1, 1),

	("banner_c13", 0, "banner_c13", 0, 0, 0, -90, 0, 0, 1, 1, 1),

	("banner_c14", 0, "banner_c14", 0, 0, 0, -90, 0, 0, 1, 1, 1),

	("banner_c15", 0, "banner_c15", 0, 0, 0, -90, 0, 0, 1, 1, 1),

	("banner_c16", 0, "banner_c16", 0, 0, 0, -90, 0, 0, 1, 1, 1),

	("banner_c17", 0, "banner_c17", 0, 0, 0, -90, 0, 0, 1, 1, 1),

	("banner_c18", 0, "banner_c18", 0, 0, 0, -90, 0, 0, 1, 1, 1),

	("banner_c19", 0, "banner_c19", 0, 0, 0, -90, 0, 0, 1, 1, 1),

	("banner_c20", 0, "banner_c20", 0, 0, 0, -90, 0, 0, 1, 1, 1),

	("banner_c21", 0, "banner_c21", 0, 0, 0, -90, 0, 0, 1, 1, 1),

	("banner_d01", 0, "banner_d01", 0, 0, 0, -90, 0, 0, 1, 1, 1),

	("banner_d02", 0, "banner_d02", 0, 0, 0, -90, 0, 0, 1, 1, 1),

	("banner_d03", 0, "banner_d03", 0, 0, 0, -90, 0, 0, 1, 1, 1),

	("banner_d04", 0, "banner_d04", 0, 0, 0, -90, 0, 0, 1, 1, 1),

	("banner_d05", 0, "banner_d05", 0, 0, 0, -90, 0, 0, 1, 1, 1),

	("banner_d06", 0, "banner_d06", 0, 0, 0, -90, 0, 0, 1, 1, 1),

	("banner_d07", 0, "banner_d07", 0, 0, 0, -90, 0, 0, 1, 1, 1),

	("banner_d08", 0, "banner_d08", 0, 0, 0, -90, 0, 0, 1, 1, 1),

	("banner_d09", 0, "banner_d09", 0, 0, 0, -90, 0, 0, 1, 1, 1),

	("banner_d10", 0, "banner_d10", 0, 0, 0, -90, 0, 0, 1, 1, 1),

	("banner_d11", 0, "banner_d11", 0, 0, 0, -90, 0, 0, 1, 1, 1),

	("banner_d12", 0, "banner_d12", 0, 0, 0, -90, 0, 0, 1, 1, 1),

	("banner_d13", 0, "banner_d13", 0, 0, 0, -90, 0, 0, 1, 1, 1),

	("banner_d14", 0, "banner_d14", 0, 0, 0, -90, 0, 0, 1, 1, 1),

	("banner_d15", 0, "banner_d15", 0, 0, 0, -90, 0, 0, 1, 1, 1),

	("banner_d16", 0, "banner_d16", 0, 0, 0, -90, 0, 0, 1, 1, 1),

	("banner_d17", 0, "banner_d17", 0, 0, 0, -90, 0, 0, 1, 1, 1),

	("banner_d18", 0, "banner_d18", 0, 0, 0, -90, 0, 0, 1, 1, 1),

	("banner_d19", 0, "banner_d19", 0, 0, 0, -90, 0, 0, 1, 1, 1),

	("banner_d20", 0, "banner_d20", 0, 0, 0, -90, 0, 0, 1, 1, 1),

	("banner_d21", 0, "banner_d21", 0, 0, 0, -90, 0, 0, 1, 1, 1),

	("banner_e01", 0, "banner_e01", 0, 0, 0, -90, 0, 0, 1, 1, 1),

	("banner_e02", 0, "banner_e02", 0, 0, 0, -90, 0, 0, 1, 1, 1),

	("banner_e03", 0, "banner_e03", 0, 0, 0, -90, 0, 0, 1, 1, 1),

	("banner_e04", 0, "banner_e04", 0, 0, 0, -90, 0, 0, 1, 1, 1),

	("banner_e05", 0, "banner_e05", 0, 0, 0, -90, 0, 0, 1, 1, 1),

	("banner_e06", 0, "banner_e06", 0, 0, 0, -90, 0, 0, 1, 1, 1),

	("banner_e07", 0, "banner_e07", 0, 0, 0, -90, 0, 0, 1, 1, 1),

	("banner_e08", 0, "banner_e08", 0, 0, 0, -90, 0, 0, 1, 1, 1),

	("banner_e09", 0, "banner_e09", 0, 0, 0, -90, 0, 0, 1, 1, 1),

	("banner_e10", 0, "banner_e10", 0, 0, 0, -90, 0, 0, 1, 1, 1),

	("banner_e11", 0, "banner_e11", 0, 0, 0, -90, 0, 0, 1, 1, 1),

	("banner_e12", 0, "banner_e12", 0, 0, 0, -90, 0, 0, 1, 1, 1),

	("banner_e13", 0, "banner_e13", 0, 0, 0, -90, 0, 0, 1, 1, 1),

	("banner_e14", 0, "banner_e14", 0, 0, 0, -90, 0, 0, 1, 1, 1),

	("banner_e15", 0, "banner_e15", 0, 0, 0, -90, 0, 0, 1, 1, 1),

	("banner_e16", 0, "banner_e16", 0, 0, 0, -90, 0, 0, 1, 1, 1),

	("banner_e17", 0, "banner_e17", 0, 0, 0, -90, 0, 0, 1, 1, 1),

	("banner_e18", 0, "banner_e18", 0, 0, 0, -90, 0, 0, 1, 1, 1),

	("banner_e19", 0, "banner_e19", 0, 0, 0, -90, 0, 0, 1, 1, 1),

	("banner_e20", 0, "banner_e20", 0, 0, 0, -90, 0, 0, 1, 1, 1),

	("banner_e21", 0, "banner_e21", 0, 0, 0, -90, 0, 0, 1, 1, 1),

	("banner_f01", 0, "banner_f01", 0, 0, 0, -90, 0, 0, 1, 1, 1),

	("banner_f02", 0, "banner_f02", 0, 0, 0, -90, 0, 0, 1, 1, 1),

	("banner_f03", 0, "banner_f03", 0, 0, 0, -90, 0, 0, 1, 1, 1),

	("banner_f04", 0, "banner_f04", 0, 0, 0, -90, 0, 0, 1, 1, 1),

	("banner_f05", 0, "banner_f05", 0, 0, 0, -90, 0, 0, 1, 1, 1),

	("banner_f06", 0, "banner_f06", 0, 0, 0, -90, 0, 0, 1, 1, 1),

	("banner_f07", 0, "banner_f07", 0, 0, 0, -90, 0, 0, 1, 1, 1),

	("banner_f08", 0, "banner_f08", 0, 0, 0, -90, 0, 0, 1, 1, 1),

	("banner_f09", 0, "banner_f09", 0, 0, 0, -90, 0, 0, 1, 1, 1),

	("banner_f10", 0, "banner_f10", 0, 0, 0, -90, 0, 0, 1, 1, 1),

	("banner_f11", 0, "banner_f11", 0, 0, 0, -90, 0, 0, 1, 1, 1),

	("banner_f12", 0, "banner_f12", 0, 0, 0, -90, 0, 0, 1, 1, 1),

	("banner_f13", 0, "banner_f13", 0, 0, 0, -90, 0, 0, 1, 1, 1),

	("banner_f14", 0, "banner_f14", 0, 0, 0, -90, 0, 0, 1, 1, 1),

	("banner_f15", 0, "banner_f15", 0, 0, 0, -90, 0, 0, 1, 1, 1),

	("banner_f16", 0, "banner_f16", 0, 0, 0, -90, 0, 0, 1, 1, 1),

	("banner_f17", 0, "banner_f17", 0, 0, 0, -90, 0, 0, 1, 1, 1),

	("banner_f18", 0, "banner_f18", 0, 0, 0, -90, 0, 0, 1, 1, 1),

	("banner_f19", 0, "banner_f19", 0, 0, 0, -90, 0, 0, 1, 1, 1),

	("banner_f20", 0, "banner_f20", 0, 0, 0, -90, 0, 0, 1, 1, 1),

	("banner_f21", 0, "banner_f21", 0, 0, 0, -90, 0, 0, 1, 1, 1),

	("banner_g01", 0, "banner_g01", 0, 0, 0, -90, 0, 0, 1, 1, 1),

	("banner_g02", 0, "banner_g02", 0, 0, 0, -90, 0, 0, 1, 1, 1),

	("banner_g03", 0, "banner_g03", 0, 0, 0, -90, 0, 0, 1, 1, 1),

	("banner_g04", 0, "banner_g04", 0, 0, 0, -90, 0, 0, 1, 1, 1),

	("banner_g05", 0, "banner_g05", 0, 0, 0, -90, 0, 0, 1, 1, 1),

	("banner_g06", 0, "banner_g06", 0, 0, 0, -90, 0, 0, 1, 1, 1),

	("banner_g07", 0, "banner_g07", 0, 0, 0, -90, 0, 0, 1, 1, 1),

	("banner_g08", 0, "banner_g08", 0, 0, 0, -90, 0, 0, 1, 1, 1),

	("banner_g09", 0, "banner_g09", 0, 0, 0, -90, 0, 0, 1, 1, 1),

	("banner_g10", 0, "banner_g10", 0, 0, 0, -90, 0, 0, 1, 1, 1),

	("banner_g11", 0, "banner_g11", 0, 0, 0, -90, 0, 0, 1, 1, 1),

	("banner_g12", 0, "banner_g12", 0, 0, 0, -90, 0, 0, 1, 1, 1),

	("banner_g13", 0, "banner_g13", 0, 0, 0, -90, 0, 0, 1, 1, 1),

	("banner_g14", 0, "banner_g14", 0, 0, 0, -90, 0, 0, 1, 1, 1),

	("banner_g15", 0, "banner_g15", 0, 0, 0, -90, 0, 0, 1, 1, 1),

	("banner_g16", 0, "banner_g16", 0, 0, 0, -90, 0, 0, 1, 1, 1),

	("banner_g17", 0, "banner_g17", 0, 0, 0, -90, 0, 0, 1, 1, 1),

	("banner_g18", 0, "banner_g18", 0, 0, 0, -90, 0, 0, 1, 1, 1),

	("banner_g19", 0, "banner_g19", 0, 0, 0, -90, 0, 0, 1, 1, 1),

	("banner_g20", 0, "banner_g20", 0, 0, 0, -90, 0, 0, 1, 1, 1),

	("banner_g21", 0, "banner_g21", 0, 0, 0, -90, 0, 0, 1, 1, 1),

	("banner_h01", 0, "banner_h01", 0, 0, 0, -90, 0, 0, 1, 1, 1),

	("banner_h02", 0, "banner_h02", 0, 0, 0, -90, 0, 0, 1, 1, 1),

	("banner_h03", 0, "banner_h03", 0, 0, 0, -90, 0, 0, 1, 1, 1),

	("banner_h04", 0, "banner_h04", 0, 0, 0, -90, 0, 0, 1, 1, 1),

	("banner_h05", 0, "banner_h05", 0, 0, 0, -90, 0, 0, 1, 1, 1),

	("banner_h06", 0, "banner_h06", 0, 0, 0, -90, 0, 0, 1, 1, 1),

	("banner_h07", 0, "banner_h07", 0, 0, 0, -90, 0, 0, 1, 1, 1),

	("banner_h08", 0, "banner_h08", 0, 0, 0, -90, 0, 0, 1, 1, 1),

	("banner_h09", 0, "banner_h09", 0, 0, 0, -90, 0, 0, 1, 1, 1),

	("banner_h10", 0, "banner_h10", 0, 0, 0, -90, 0, 0, 1, 1, 1),

	("banner_h11", 0, "banner_h11", 0, 0, 0, -90, 0, 0, 1, 1, 1),

	("banner_h12", 0, "banner_h12", 0, 0, 0, -90, 0, 0, 1, 1, 1),

	("banner_h13", 0, "banner_h13", 0, 0, 0, -90, 0, 0, 1, 1, 1),

	("banner_h14", 0, "banner_h14", 0, 0, 0, -90, 0, 0, 1, 1, 1),

	("banner_h15", 0, "banner_h15", 0, 0, 0, -90, 0, 0, 1, 1, 1),

	("banner_h16", 0, "banner_h16", 0, 0, 0, -90, 0, 0, 1, 1, 1),

	("banner_h17", 0, "banner_h17", 0, 0, 0, -90, 0, 0, 1, 1, 1),

	("banner_h18", 0, "banner_h18", 0, 0, 0, -90, 0, 0, 1, 1, 1),

	("banner_h19", 0, "banner_h19", 0, 0, 0, -90, 0, 0, 1, 1, 1),

	("banner_h20", 0, "banner_h20", 0, 0, 0, -90, 0, 0, 1, 1, 1),

	("banner_h21", 0, "banner_h21", 0, 0, 0, -90, 0, 0, 1, 1, 1),

	("banner_i01", 0, "banner_i01", 0, 0, 0, -90, 0, 0, 1, 1, 1),

	("banner_i02", 0, "banner_i02", 0, 0, 0, -90, 0, 0, 1, 1, 1),

	("banner_i03", 0, "banner_i03", 0, 0, 0, -90, 0, 0, 1, 1, 1),

	("banner_i04", 0, "banner_i04", 0, 0, 0, -90, 0, 0, 1, 1, 1),

	("banner_i05", 0, "banner_i05", 0, 0, 0, -90, 0, 0, 1, 1, 1),

	("banner_i06", 0, "banner_i06", 0, 0, 0, -90, 0, 0, 1, 1, 1),

	("banner_i07", 0, "banner_i07", 0, 0, 0, -90, 0, 0, 1, 1, 1),

	("banner_i08", 0, "banner_i08", 0, 0, 0, -90, 0, 0, 1, 1, 1),

	("banner_i09", 0, "banner_i09", 0, 0, 0, -90, 0, 0, 1, 1, 1),

	("banner_i10", 0, "banner_i10", 0, 0, 0, -90, 0, 0, 1, 1, 1),

	("banner_i11", 0, "banner_i11", 0, 0, 0, -90, 0, 0, 1, 1, 1),

	("banner_i12", 0, "banner_i12", 0, 0, 0, -90, 0, 0, 1, 1, 1),

	("banner_i13", 0, "banner_i13", 0, 0, 0, -90, 0, 0, 1, 1, 1),

	("banner_i14", 0, "banner_i14", 0, 0, 0, -90, 0, 0, 1, 1, 1),

	("banner_i15", 0, "banner_i15", 0, 0, 0, -90, 0, 0, 1, 1, 1),

	("banner_i16", 0, "banner_i16", 0, 0, 0, -90, 0, 0, 1, 1, 1),

	("banner_i17", 0, "banner_i17", 0, 0, 0, -90, 0, 0, 1, 1, 1),

	("banner_i18", 0, "banner_i18", 0, 0, 0, -90, 0, 0, 1, 1, 1),

	("banner_i19", 0, "banner_i19", 0, 0, 0, -90, 0, 0, 1, 1, 1),

	("banner_i20", 0, "banner_i20", 0, 0, 0, -90, 0, 0, 1, 1, 1),

	("banner_i21", 0, "banner_i21", 0, 0, 0, -90, 0, 0, 1, 1, 1),

	("banner_j01", 0, "banner_j01", 0, 0, 0, -90, 0, 0, 1, 1, 1),

	("banner_j02", 0, "banner_j02", 0, 0, 0, -90, 0, 0, 1, 1, 1),

	("banner_j03", 0, "banner_j03", 0, 0, 0, -90, 0, 0, 1, 1, 1),

	("banner_j04", 0, "banner_j04", 0, 0, 0, -90, 0, 0, 1, 1, 1),

	("banner_j05", 0, "banner_j05", 0, 0, 0, -90, 0, 0, 1, 1, 1),

	("banner_j06", 0, "banner_j06", 0, 0, 0, -90, 0, 0, 1, 1, 1),

	("banner_j07", 0, "banner_j07", 0, 0, 0, -90, 0, 0, 1, 1, 1),

	("banner_j08", 0, "banner_j08", 0, 0, 0, -90, 0, 0, 1, 1, 1),

	("banner_j09", 0, "banner_j09", 0, 0, 0, -90, 0, 0, 1, 1, 1),

	("banner_j10", 0, "banner_j10", 0, 0, 0, -90, 0, 0, 1, 1, 1),

	("banner_j11", 0, "banner_j11", 0, 0, 0, -90, 0, 0, 1, 1, 1),

	("banner_j12", 0, "banner_j12", 0, 0, 0, -90, 0, 0, 1, 1, 1),

	("banner_j13", 0, "banner_j13", 0, 0, 0, -90, 0, 0, 1, 1, 1),

	("banner_j14", 0, "banner_j14", 0, 0, 0, -90, 0, 0, 1, 1, 1),

	("banner_j15", 0, "banner_j15", 0, 0, 0, -90, 0, 0, 1, 1, 1),

	("banner_j16", 0, "banner_j16", 0, 0, 0, -90, 0, 0, 1, 1, 1),

	("banner_j17", 0, "banner_j17", 0, 0, 0, -90, 0, 0, 1, 1, 1),

	("banner_j18", 0, "banner_j18", 0, 0, 0, -90, 0, 0, 1, 1, 1),

	("banner_j19", 0, "banner_j19", 0, 0, 0, -90, 0, 0, 1, 1, 1),

	("banner_j20", 0, "banner_j20", 0, 0, 0, -90, 0, 0, 1, 1, 1),

	("banner_j21", 0, "banner_j21", 0, 0, 0, -90, 0, 0, 1, 1, 1),

	("banner_k01", 0, "banner_k01", 0, 0, 0, -90, 0, 0, 1, 1, 1),

	("banner_k02", 0, "banner_k02", 0, 0, 0, -90, 0, 0, 1, 1, 1),

	("banner_k03", 0, "banner_k03", 0, 0, 0, -90, 0, 0, 1, 1, 1),

	("banner_k04", 0, "banner_k04", 0, 0, 0, -90, 0, 0, 1, 1, 1),

	("banner_k05", 0, "banner_k05", 0, 0, 0, -90, 0, 0, 1, 1, 1),

	("banner_k06", 0, "banner_k06", 0, 0, 0, -90, 0, 0, 1, 1, 1),

	("banner_k07", 0, "banner_k07", 0, 0, 0, -90, 0, 0, 1, 1, 1),

	("banner_k08", 0, "banner_k08", 0, 0, 0, -90, 0, 0, 1, 1, 1),

	("banner_k09", 0, "banner_k09", 0, 0, 0, -90, 0, 0, 1, 1, 1),

	("banner_k10", 0, "banner_k10", 0, 0, 0, -90, 0, 0, 1, 1, 1),

	("banner_k11", 0, "banner_k11", 0, 0, 0, -90, 0, 0, 1, 1, 1),

	("banner_k12", 0, "banner_k12", 0, 0, 0, -90, 0, 0, 1, 1, 1),

	("banner_k13", 0, "banner_k13", 0, 0, 0, -90, 0, 0, 1, 1, 1),

	("banner_k14", 0, "banner_k14", 0, 0, 0, -90, 0, 0, 1, 1, 1),

	("banner_k15", 0, "banner_k15", 0, 0, 0, -90, 0, 0, 1, 1, 1),

	("banner_k16", 0, "banner_k16", 0, 0, 0, -90, 0, 0, 1, 1, 1),

	("banner_k17", 0, "banner_k17", 0, 0, 0, -90, 0, 0, 1, 1, 1),

	("banner_k18", 0, "banner_k18", 0, 0, 0, -90, 0, 0, 1, 1, 1),

	("banner_k19", 0, "banner_k19", 0, 0, 0, -90, 0, 0, 1, 1, 1),

	("banner_k20", 0, "banner_k20", 0, 0, 0, -90, 0, 0, 1, 1, 1),

	("banner_k21", 0, "banner_k21", 0, 0, 0, -90, 0, 0, 1, 1, 1),

	("banner_l01", 0, "banner_l01", 0, 0, 0, -90, 0, 0, 1, 1, 1),

	("banner_l02", 0, "banner_l02", 0, 0, 0, -90, 0, 0, 1, 1, 1),

	("banner_l03", 0, "banner_l03", 0, 0, 0, -90, 0, 0, 1, 1, 1),

	("banner_l04", 0, "banner_l04", 0, 0, 0, -90, 0, 0, 1, 1, 1),

	("banner_l05", 0, "banner_l05", 0, 0, 0, -90, 0, 0, 1, 1, 1),

	("banner_l06", 0, "banner_l06", 0, 0, 0, -90, 0, 0, 1, 1, 1),

	("banner_l07", 0, "banner_l07", 0, 0, 0, -90, 0, 0, 1, 1, 1),

	("banner_l08", 0, "banner_l08", 0, 0, 0, -90, 0, 0, 1, 1, 1),

	("banner_l09", 0, "banner_l09", 0, 0, 0, -90, 0, 0, 1, 1, 1),

	("banner_l10", 0, "banner_l10", 0, 0, 0, -90, 0, 0, 1, 1, 1),

	("banner_l11", 0, "banner_l11", 0, 0, 0, -90, 0, 0, 1, 1, 1),

	("banner_l12", 0, "banner_l12", 0, 0, 0, -90, 0, 0, 1, 1, 1),

	("banner_l13", 0, "banner_l13", 0, 0, 0, -90, 0, 0, 1, 1, 1),

	("banner_l14", 0, "banner_l14", 0, 0, 0, -90, 0, 0, 1, 1, 1),

	("banner_l15", 0, "banner_l15", 0, 0, 0, -90, 0, 0, 1, 1, 1),

	("banner_l16", 0, "banner_l16", 0, 0, 0, -90, 0, 0, 1, 1, 1),

	("banner_l17", 0, "banner_l17", 0, 0, 0, -90, 0, 0, 1, 1, 1),

	("banner_l18", 0, "banner_l18", 0, 0, 0, -90, 0, 0, 1, 1, 1),

	("banner_l19", 0, "banner_l19", 0, 0, 0, -90, 0, 0, 1, 1, 1),

	("banner_l20", 0, "banner_l20", 0, 0, 0, -90, 0, 0, 1, 1, 1),

	("banner_l21", 0, "banner_l21", 0, 0, 0, -90, 0, 0, 1, 1, 1),

	("banner_lords_swadia01", 0, "banner_lords_swadia01", 0, 0, 0, -90, 0, 0, 1, 1, 1),

	("banner_lords_swadia02", 0, "banner_lords_swadia02", 0, 0, 0, -90, 0, 0, 1, 1, 1),

	("banner_lords_swadia03", 0, "banner_lords_swadia03", 0, 0, 0, -90, 0, 0, 1, 1, 1),

	("banner_lords_swadia04", 0, "banner_lords_swadia04", 0, 0, 0, -90, 0, 0, 1, 1, 1),

	("banner_lords_swadia05", 0, "banner_lords_swadia05", 0, 0, 0, -90, 0, 0, 1, 1, 1),

	("banner_lords_swadia06", 0, "banner_lords_swadia06", 0, 0, 0, -90, 0, 0, 1, 1, 1),

	("banner_lords_swadia07", 0, "banner_lords_swadia07", 0, 0, 0, -90, 0, 0, 1, 1, 1),

	("banner_lords_swadia08", 0, "banner_lords_swadia08", 0, 0, 0, -90, 0, 0, 1, 1, 1),

	("banner_lords_swadia09", 0, "banner_lords_swadia09", 0, 0, 0, -90, 0, 0, 1, 1, 1),

	("banner_lords_swadia10", 0, "banner_lords_swadia10", 0, 0, 0, -90, 0, 0, 1, 1, 1),

	("banner_lords_swadia11", 0, "banner_lords_swadia11", 0, 0, 0, -90, 0, 0, 1, 1, 1),

	("banner_lords_swadia12", 0, "banner_lords_swadia12", 0, 0, 0, -90, 0, 0, 1, 1, 1),

	("banner_lords_swadia13", 0, "banner_lords_swadia13", 0, 0, 0, -90, 0, 0, 1, 1, 1),

	("banner_lords_swadia14", 0, "banner_lords_swadia14", 0, 0, 0, -90, 0, 0, 1, 1, 1),

	("banner_lords_swadia15", 0, "banner_lords_swadia15", 0, 0, 0, -90, 0, 0, 1, 1, 1),

	("banner_lords_swadia16", 0, "banner_lords_swadia16", 0, 0, 0, -90, 0, 0, 1, 1, 1),

	("banner_lords_swadia17", 0, "banner_lords_swadia17", 0, 0, 0, -90, 0, 0, 1, 1, 1),

	("banner_lords_swadia18", 0, "banner_lords_swadia18", 0, 0, 0, -90, 0, 0, 1, 1, 1),

	("banner_lords_swadia19", 0, "banner_lords_swadia19", 0, 0, 0, -90, 0, 0, 1, 1, 1),

	("banner_lords_swadia20", 0, "banner_lords_swadia20", 0, 0, 0, -90, 0, 0, 1, 1, 1),

	("banner_lords_swadia21", 0, "banner_lords_swadia21", 0, 0, 0, -90, 0, 0, 1, 1, 1),

	("banner_lords_vaegir01", 0, "banner_lords_vaegir01", 0, 0, 0, -90, 0, 0, 1, 1, 1),

	("banner_lords_vaegir02", 0, "banner_lords_vaegir02", 0, 0, 0, -90, 0, 0, 1, 1, 1),

	("banner_lords_vaegir03", 0, "banner_lords_vaegir03", 0, 0, 0, -90, 0, 0, 1, 1, 1),

	("banner_lords_vaegir04", 0, "banner_lords_vaegir04", 0, 0, 0, -90, 0, 0, 1, 1, 1),

	("banner_lords_vaegir05", 0, "banner_lords_vaegir05", 0, 0, 0, -90, 0, 0, 1, 1, 1),

	("banner_lords_vaegir06", 0, "banner_lords_vaegir06", 0, 0, 0, -90, 0, 0, 1, 1, 1),

	("banner_lords_vaegir07", 0, "banner_lords_vaegir07", 0, 0, 0, -90, 0, 0, 1, 1, 1),

	("banner_lords_vaegir08", 0, "banner_lords_vaegir08", 0, 0, 0, -90, 0, 0, 1, 1, 1),

	("banner_lords_vaegir09", 0, "banner_lords_vaegir09", 0, 0, 0, -90, 0, 0, 1, 1, 1),

	("banner_lords_vaegir10", 0, "banner_lords_vaegir10", 0, 0, 0, -90, 0, 0, 1, 1, 1),

	("banner_lords_vaegir11", 0, "banner_lords_vaegir11", 0, 0, 0, -90, 0, 0, 1, 1, 1),

	("banner_lords_vaegir12", 0, "banner_lords_vaegir12", 0, 0, 0, -90, 0, 0, 1, 1, 1),

	("banner_lords_vaegir13", 0, "banner_lords_vaegir13", 0, 0, 0, -90, 0, 0, 1, 1, 1),

	("banner_lords_vaegir14", 0, "banner_lords_vaegir14", 0, 0, 0, -90, 0, 0, 1, 1, 1),

	("banner_lords_vaegir15", 0, "banner_lords_vaegir15", 0, 0, 0, -90, 0, 0, 1, 1, 1),

	("banner_lords_vaegir16", 0, "banner_lords_vaegir16", 0, 0, 0, -90, 0, 0, 1, 1, 1),

	("banner_lords_vaegir17", 0, "banner_lords_vaegir17", 0, 0, 0, -90, 0, 0, 1, 1, 1),

	("banner_lords_vaegir18", 0, "banner_lords_vaegir18", 0, 0, 0, -90, 0, 0, 1, 1, 1),

	("banner_lords_vaegir19", 0, "banner_lords_vaegir19", 0, 0, 0, -90, 0, 0, 1, 1, 1),

	("banner_lords_vaegir20", 0, "banner_lords_vaegir20", 0, 0, 0, -90, 0, 0, 1, 1, 1),

	("banner_lords_vaegir21", 0, "banner_lords_vaegir21", 0, 0, 0, -90, 0, 0, 1, 1, 1),

	("banner_lords_khergit01", 0, "banner_lords_khergit01", 0, 0, 0, -90, 0, 0, 1, 1, 1),

	("banner_lords_khergit02", 0, "banner_lords_khergit02", 0, 0, 0, -90, 0, 0, 1, 1, 1),

	("banner_lords_khergit03", 0, "banner_lords_khergit03", 0, 0, 0, -90, 0, 0, 1, 1, 1),

	("banner_lords_khergit04", 0, "banner_lords_khergit04", 0, 0, 0, -90, 0, 0, 1, 1, 1),

	("banner_lords_khergit05", 0, "banner_lords_khergit05", 0, 0, 0, -90, 0, 0, 1, 1, 1),

	("banner_lords_khergit06", 0, "banner_lords_khergit06", 0, 0, 0, -90, 0, 0, 1, 1, 1),

	("banner_lords_khergit07", 0, "banner_lords_khergit07", 0, 0, 0, -90, 0, 0, 1, 1, 1),

	("banner_lords_khergit08", 0, "banner_lords_khergit08", 0, 0, 0, -90, 0, 0, 1, 1, 1),

	("banner_lords_khergit09", 0, "banner_lords_khergit09", 0, 0, 0, -90, 0, 0, 1, 1, 1),

	("banner_lords_khergit10", 0, "banner_lords_khergit10", 0, 0, 0, -90, 0, 0, 1, 1, 1),

	("banner_lords_khergit11", 0, "banner_lords_khergit11", 0, 0, 0, -90, 0, 0, 1, 1, 1),

	("banner_lords_khergit12", 0, "banner_lords_khergit12", 0, 0, 0, -90, 0, 0, 1, 1, 1),

	("banner_lords_khergit13", 0, "banner_lords_khergit13", 0, 0, 0, -90, 0, 0, 1, 1, 1),

	("banner_lords_khergit14", 0, "banner_lords_khergit14", 0, 0, 0, -90, 0, 0, 1, 1, 1),

	("banner_lords_khergit15", 0, "banner_lords_khergit15", 0, 0, 0, -90, 0, 0, 1, 1, 1),

	("banner_lords_khergit16", 0, "banner_lords_khergit16", 0, 0, 0, -90, 0, 0, 1, 1, 1),

	("banner_lords_khergit17", 0, "banner_lords_khergit17", 0, 0, 0, -90, 0, 0, 1, 1, 1),

	("banner_lords_khergit18", 0, "banner_lords_khergit18", 0, 0, 0, -90, 0, 0, 1, 1, 1),

	("banner_lords_khergit19", 0, "banner_lords_khergit19", 0, 0, 0, -90, 0, 0, 1, 1, 1),

	("banner_lords_khergit20", 0, "banner_lords_khergit20", 0, 0, 0, -90, 0, 0, 1, 1, 1),

	("banner_lords_khergit21", 0, "banner_lords_khergit21", 0, 0, 0, -90, 0, 0, 1, 1, 1),

	("banner_lords_nord01", 0, "banner_lords_nord01", 0, 0, 0, -90, 0, 0, 1, 1, 1),

	("banner_lords_nord02", 0, "banner_lords_nord02", 0, 0, 0, -90, 0, 0, 1, 1, 1),

	("banner_lords_nord03", 0, "banner_lords_nord03", 0, 0, 0, -90, 0, 0, 1, 1, 1),

	("banner_lords_nord04", 0, "banner_lords_nord04", 0, 0, 0, -90, 0, 0, 1, 1, 1),

	("banner_lords_nord05", 0, "banner_lords_nord05", 0, 0, 0, -90, 0, 0, 1, 1, 1),

	("banner_lords_nord06", 0, "banner_lords_nord06", 0, 0, 0, -90, 0, 0, 1, 1, 1),

	("banner_lords_nord07", 0, "banner_lords_nord07", 0, 0, 0, -90, 0, 0, 1, 1, 1),

	("banner_lords_nord08", 0, "banner_lords_nord08", 0, 0, 0, -90, 0, 0, 1, 1, 1),

	("banner_lords_nord09", 0, "banner_lords_nord09", 0, 0, 0, -90, 0, 0, 1, 1, 1),

	("banner_lords_nord10", 0, "banner_lords_nord10", 0, 0, 0, -90, 0, 0, 1, 1, 1),

	("banner_lords_nord11", 0, "banner_lords_nord11", 0, 0, 0, -90, 0, 0, 1, 1, 1),

	("banner_lords_nord12", 0, "banner_lords_nord12", 0, 0, 0, -90, 0, 0, 1, 1, 1),

	("banner_lords_nord13", 0, "banner_lords_nord13", 0, 0, 0, -90, 0, 0, 1, 1, 1),

	("banner_lords_nord14", 0, "banner_lords_nord14", 0, 0, 0, -90, 0, 0, 1, 1, 1),

	("banner_lords_nord15", 0, "banner_lords_nord15", 0, 0, 0, -90, 0, 0, 1, 1, 1),

	("banner_lords_nord16", 0, "banner_lords_nord16", 0, 0, 0, -90, 0, 0, 1, 1, 1),

	("banner_lords_nord17", 0, "banner_lords_nord17", 0, 0, 0, -90, 0, 0, 1, 1, 1),

	("banner_lords_nord18", 0, "banner_lords_nord18", 0, 0, 0, -90, 0, 0, 1, 1, 1),

	("banner_lords_nord19", 0, "banner_lords_nord19", 0, 0, 0, -90, 0, 0, 1, 1, 1),

	("banner_lords_nord20", 0, "banner_lords_nord20", 0, 0, 0, -90, 0, 0, 1, 1, 1),

	("banner_lords_nord21", 0, "banner_lords_nord21", 0, 0, 0, -90, 0, 0, 1, 1, 1),

	("banner_lords_rhodok01", 0, "banner_lords_rhodok01", 0, 0, 0, -90, 0, 0, 1, 1, 1),

	("banner_lords_rhodok02", 0, "banner_lords_rhodok02", 0, 0, 0, -90, 0, 0, 1, 1, 1),

	("banner_lords_rhodok03", 0, "banner_lords_rhodok03", 0, 0, 0, -90, 0, 0, 1, 1, 1),

	("banner_lords_rhodok04", 0, "banner_lords_rhodok04", 0, 0, 0, -90, 0, 0, 1, 1, 1),

	("banner_lords_rhodok05", 0, "banner_lords_rhodok05", 0, 0, 0, -90, 0, 0, 1, 1, 1),

	("banner_lords_rhodok06", 0, "banner_lords_rhodok06", 0, 0, 0, -90, 0, 0, 1, 1, 1),

	("banner_lords_rhodok07", 0, "banner_lords_rhodok07", 0, 0, 0, -90, 0, 0, 1, 1, 1),

	("banner_lords_rhodok08", 0, "banner_lords_rhodok08", 0, 0, 0, -90, 0, 0, 1, 1, 1),

	("banner_lords_rhodok09", 0, "banner_lords_rhodok09", 0, 0, 0, -90, 0, 0, 1, 1, 1),

	("banner_lords_rhodok10", 0, "banner_lords_rhodok10", 0, 0, 0, -90, 0, 0, 1, 1, 1),

	("banner_lords_rhodok11", 0, "banner_lords_rhodok11", 0, 0, 0, -90, 0, 0, 1, 1, 1),

	("banner_lords_rhodok12", 0, "banner_lords_rhodok12", 0, 0, 0, -90, 0, 0, 1, 1, 1),

	("banner_lords_rhodok13", 0, "banner_lords_rhodok13", 0, 0, 0, -90, 0, 0, 1, 1, 1),

	("banner_lords_rhodok14", 0, "banner_lords_rhodok14", 0, 0, 0, -90, 0, 0, 1, 1, 1),

	("banner_lords_rhodok15", 0, "banner_lords_rhodok15", 0, 0, 0, -90, 0, 0, 1, 1, 1),

	("banner_lords_rhodok16", 0, "banner_lords_rhodok16", 0, 0, 0, -90, 0, 0, 1, 1, 1),

	("banner_lords_rhodok17", 0, "banner_lords_rhodok17", 0, 0, 0, -90, 0, 0, 1, 1, 1),

	("banner_lords_rhodok18", 0, "banner_lords_rhodok18", 0, 0, 0, -90, 0, 0, 1, 1, 1),

	("banner_lords_rhodok19", 0, "banner_lords_rhodok19", 0, 0, 0, -90, 0, 0, 1, 1, 1),

	("banner_lords_rhodok20", 0, "banner_lords_rhodok20", 0, 0, 0, -90, 0, 0, 1, 1, 1),

	("banner_lords_rhodok21", 0, "banner_lords_rhodok21", 0, 0, 0, -90, 0, 0, 1, 1, 1),

	("banner_lords_sarranid01", 0, "banner_lords_sarranid01", 0, 0, 0, -90, 0, 0, 1, 1, 1),

	("banner_lords_sarranid02", 0, "banner_lords_sarranid02", 0, 0, 0, -90, 0, 0, 1, 1, 1),

	("banner_lords_sarranid03", 0, "banner_lords_sarranid03", 0, 0, 0, -90, 0, 0, 1, 1, 1),

	("banner_lords_sarranid04", 0, "banner_lords_sarranid04", 0, 0, 0, -90, 0, 0, 1, 1, 1),

	("banner_lords_sarranid05", 0, "banner_lords_sarranid05", 0, 0, 0, -90, 0, 0, 1, 1, 1),

	("banner_lords_sarranid06", 0, "banner_lords_sarranid06", 0, 0, 0, -90, 0, 0, 1, 1, 1),

	("banner_lords_sarranid07", 0, "banner_lords_sarranid07", 0, 0, 0, -90, 0, 0, 1, 1, 1),

	("banner_lords_sarranid08", 0, "banner_lords_sarranid08", 0, 0, 0, -90, 0, 0, 1, 1, 1),

	("banner_lords_sarranid09", 0, "banner_lords_sarranid09", 0, 0, 0, -90, 0, 0, 1, 1, 1),

	("banner_lords_sarranid10", 0, "banner_lords_sarranid10", 0, 0, 0, -90, 0, 0, 1, 1, 1),

	("banner_lords_sarranid11", 0, "banner_lords_sarranid11", 0, 0, 0, -90, 0, 0, 1, 1, 1),

	("banner_lords_sarranid12", 0, "banner_lords_sarranid12", 0, 0, 0, -90, 0, 0, 1, 1, 1),

	("banner_lords_sarranid13", 0, "banner_lords_sarranid13", 0, 0, 0, -90, 0, 0, 1, 1, 1),

	("banner_lords_sarranid14", 0, "banner_lords_sarranid14", 0, 0, 0, -90, 0, 0, 1, 1, 1),

	("banner_lords_sarranid15", 0, "banner_lords_sarranid15", 0, 0, 0, -90, 0, 0, 1, 1, 1),

	("banner_lords_sarranid16", 0, "banner_lords_sarranid16", 0, 0, 0, -90, 0, 0, 1, 1, 1),

	("banner_lords_sarranid17", 0, "banner_lords_sarranid17", 0, 0, 0, -90, 0, 0, 1, 1, 1),

	("banner_lords_sarranid18", 0, "banner_lords_sarranid18", 0, 0, 0, -90, 0, 0, 1, 1, 1),

	("banner_lords_sarranid19", 0, "banner_lords_sarranid19", 0, 0, 0, -90, 0, 0, 1, 1, 1),

	("banner_lords_sarranid20", 0, "banner_lords_sarranid20", 0, 0, 0, -90, 0, 0, 1, 1, 1),

	("banner_lords_sarranid21", 0, "banner_lords_sarranid21", 0, 0, 0, -90, 0, 0, 1, 1, 1),

	("banner_companions01", 0, "banner_companions01", 0, 0, 0, -90, 0, 0, 1, 1, 1),

	("banner_companions02", 0, "banner_companions02", 0, 0, 0, -90, 0, 0, 1, 1, 1),

	("banner_companions03", 0, "banner_companions03", 0, 0, 0, -90, 0, 0, 1, 1, 1),

	("banner_companions04", 0, "banner_companions04", 0, 0, 0, -90, 0, 0, 1, 1, 1),

	("banner_companions05", 0, "banner_companions05", 0, 0, 0, -90, 0, 0, 1, 1, 1),

	("banner_companions06", 0, "banner_companions06", 0, 0, 0, -90, 0, 0, 1, 1, 1),

	("banner_companions07", 0, "banner_companions07", 0, 0, 0, -90, 0, 0, 1, 1, 1),

	("banner_companions08", 0, "banner_companions08", 0, 0, 0, -90, 0, 0, 1, 1, 1),

	("banner_companions09", 0, "banner_companions09", 0, 0, 0, -90, 0, 0, 1, 1, 1),

	("banner_companions10", 0, "banner_companions10", 0, 0, 0, -90, 0, 0, 1, 1, 1),

	("banner_companions11", 0, "banner_companions11", 0, 0, 0, -90, 0, 0, 1, 1, 1),

	("banner_companions12", 0, "banner_companions12", 0, 0, 0, -90, 0, 0, 1, 1, 1),

	("banner_companions13", 0, "banner_companions13", 0, 0, 0, -90, 0, 0, 1, 1, 1),

	("banner_companions14", 0, "banner_companions14", 0, 0, 0, -90, 0, 0, 1, 1, 1),

	("banner_companions15", 0, "banner_companions15", 0, 0, 0, -90, 0, 0, 1, 1, 1),

	("banner_companions16", 0, "banner_companions16", 0, 0, 0, -90, 0, 0, 1, 1, 1),

	("banner_companions17", 0, "banner_companions17", 0, 0, 0, -90, 0, 0, 1, 1, 1),

	("banner_companions18", 0, "banner_companions18", 0, 0, 0, -90, 0, 0, 1, 1, 1),

	("banner_companions19", 0, "banner_companions19", 0, 0, 0, -90, 0, 0, 1, 1, 1),

	("banner_companions20", 0, "banner_companions20", 0, 0, 0, -90, 0, 0, 1, 1, 1),

	("banner_companions21", 0, "banner_companions21", 0, 0, 0, -90, 0, 0, 1, 1, 1),

	("banner_companions22", 0, "banner_companions22", 0, 0, 0, -90, 0, 0, 1, 1, 1),

	("banner_bandits01", 0, "banner_bandits01", 0, 0, 0, -90, 0, 0, 1, 1, 1),

	("banner_bandits02", 0, "banner_bandits02", 0, 0, 0, -90, 0, 0, 1, 1, 1),

	("banner_bandits03", 0, "banner_bandits03", 0, 0, 0, -90, 0, 0, 1, 1, 1),

	("banner_bandits04", 0, "banner_bandits04", 0, 0, 0, -90, 0, 0, 1, 1, 1),

	("banner_bandits05", 0, "banner_bandits05", 0, 0, 0, -90, 0, 0, 1, 1, 1),

	("banner_bandits06", 0, "banner_bandits06", 0, 0, 0, -90, 0, 0, 1, 1, 1),

	("banner_bandits07", 0, "banner_bandits07", 0, 0, 0, -90, 0, 0, 1, 1, 1),

	("banner_kingdom_a", 0, "banner_kingdom_a", 0, 0, 0, -90, 0, 0, 1, 1, 1),

	("banner_kingdom_b", 0, "banner_kingdom_b", 0, 0, 0, -90, 0, 0, 1, 1, 1),

	("banner_kingdom_c", 0, "banner_kingdom_c", 0, 0, 0, -90, 0, 0, 1, 1, 1),

	("banner_kingdom_d", 0, "banner_kingdom_d", 0, 0, 0, -90, 0, 0, 1, 1, 1),

	("banner_kingdom_e", 0, "banner_kingdom_e", 0, 0, 0, -90, 0, 0, 1, 1, 1),

	("banner_kingdom_f", 0, "banner_kingdom_f", 0, 0, 0, -90, 0, 0, 1, 1, 1),

	("banner_kingdom_g", 0, "banner_kingdom_g", 0, 0, 0, -90, 0, 0, 1, 1, 1),

	("banner_kingdom_h", 0, "banner_kingdom_h", 0, 0, 0, -90, 0, 0, 1, 1, 1),

	("banner_kingdom_i", 0, "banner_kingdom_i", 0, 0, 0, -90, 0, 0, 1, 1, 1),

	("banner_kingdom_j", 0, "banner_kingdom_j", 0, 0, 0, -90, 0, 0, 1, 1, 1),

	("banner_kingdom_k", 0, "banner_kingdom_k", 0, 0, 0, -90, 0, 0, 1, 1, 1),

	("banner_kingdom_l", 0, "banner_kingdom_l", 0, 0, 0, -90, 0, 0, 1, 1, 1),

	("banner_kingdom_m", 0, "banner_kingdom_m", 0, 0, 0, -90, 0, 0, 1, 1, 1),

	("banner_kingdom_n", 0, "banner_kingdom_n", 0, 0, 0, -90, 0, 0, 1, 1, 1),

	("arms_a01", 0, "arms_a01", 0, 0, 0, -90, 0, 0, 1, 1, 1),

	("arms_a02", 0, "arms_a02", 0, 0, 0, -90, 0, 0, 1, 1, 1),

	("arms_a03", 0, "arms_a03", 0, 0, 0, -90, 0, 0, 1, 1, 1),

	("arms_a04", 0, "arms_a04", 0, 0, 0, -90, 0, 0, 1, 1, 1),

	("arms_a05", 0, "arms_a05", 0, 0, 0, -90, 0, 0, 1, 1, 1),

	("arms_a06", 0, "arms_a06", 0, 0, 0, -90, 0, 0, 1, 1, 1),

	("arms_a07", 0, "arms_a07", 0, 0, 0, -90, 0, 0, 1, 1, 1),

	("arms_a08", 0, "arms_a08", 0, 0, 0, -90, 0, 0, 1, 1, 1),

	("arms_a09", 0, "arms_a09", 0, 0, 0, -90, 0, 0, 1, 1, 1),

	("arms_a10", 0, "arms_a10", 0, 0, 0, -90, 0, 0, 1, 1, 1),

	("arms_a11", 0, "arms_a11", 0, 0, 0, -90, 0, 0, 1, 1, 1),

	("arms_a12", 0, "arms_a12", 0, 0, 0, -90, 0, 0, 1, 1, 1),

	("arms_a13", 0, "arms_a13", 0, 0, 0, -90, 0, 0, 1, 1, 1),

	("arms_a14", 0, "arms_a14", 0, 0, 0, -90, 0, 0, 1, 1, 1),

	("arms_a15", 0, "arms_a15", 0, 0, 0, -90, 0, 0, 1, 1, 1),

	("arms_a16", 0, "arms_a16", 0, 0, 0, -90, 0, 0, 1, 1, 1),

	("arms_a17", 0, "arms_a17", 0, 0, 0, -90, 0, 0, 1, 1, 1),

	("arms_a18", 0, "arms_a18", 0, 0, 0, -90, 0, 0, 1, 1, 1),

	("arms_a19", 0, "arms_a19", 0, 0, 0, -90, 0, 0, 1, 1, 1),

	("arms_a20", 0, "arms_a20", 0, 0, 0, -90, 0, 0, 1, 1, 1),

	("arms_a21", 0, "arms_a21", 0, 0, 0, -90, 0, 0, 1, 1, 1),

	("arms_b01", 0, "arms_b01", 0, 0, 0, -90, 0, 0, 1, 1, 1),

	("arms_b02", 0, "arms_b02", 0, 0, 0, -90, 0, 0, 1, 1, 1),

	("arms_b03", 0, "arms_b03", 0, 0, 0, -90, 0, 0, 1, 1, 1),

	("arms_b04", 0, "arms_b04", 0, 0, 0, -90, 0, 0, 1, 1, 1),

	("arms_b05", 0, "arms_b05", 0, 0, 0, -90, 0, 0, 1, 1, 1),

	("arms_b06", 0, "arms_b06", 0, 0, 0, -90, 0, 0, 1, 1, 1),

	("arms_b07", 0, "arms_b07", 0, 0, 0, -90, 0, 0, 1, 1, 1),

	("arms_b08", 0, "arms_b08", 0, 0, 0, -90, 0, 0, 1, 1, 1),

	("arms_b09", 0, "arms_b09", 0, 0, 0, -90, 0, 0, 1, 1, 1),

	("arms_b10", 0, "arms_b10", 0, 0, 0, -90, 0, 0, 1, 1, 1),

	("arms_b11", 0, "arms_b11", 0, 0, 0, -90, 0, 0, 1, 1, 1),

	("arms_b12", 0, "arms_b12", 0, 0, 0, -90, 0, 0, 1, 1, 1),

	("arms_b13", 0, "arms_b13", 0, 0, 0, -90, 0, 0, 1, 1, 1),

	("arms_b14", 0, "arms_b14", 0, 0, 0, -90, 0, 0, 1, 1, 1),

	("arms_b15", 0, "arms_b15", 0, 0, 0, -90, 0, 0, 1, 1, 1),

	("arms_b16", 0, "arms_b16", 0, 0, 0, -90, 0, 0, 1, 1, 1),

	("arms_b17", 0, "arms_b17", 0, 0, 0, -90, 0, 0, 1, 1, 1),

	("arms_b18", 0, "arms_b18", 0, 0, 0, -90, 0, 0, 1, 1, 1),

	("arms_b19", 0, "arms_b19", 0, 0, 0, -90, 0, 0, 1, 1, 1),

	("arms_b20", 0, "arms_b20", 0, 0, 0, -90, 0, 0, 1, 1, 1),

	("arms_b21", 0, "arms_b21", 0, 0, 0, -90, 0, 0, 1, 1, 1),

	("arms_c01", 0, "arms_c01", 0, 0, 0, -90, 0, 0, 1, 1, 1),

	("arms_c02", 0, "arms_c02", 0, 0, 0, -90, 0, 0, 1, 1, 1),

	("arms_c03", 0, "arms_c03", 0, 0, 0, -90, 0, 0, 1, 1, 1),

	("arms_c04", 0, "arms_c04", 0, 0, 0, -90, 0, 0, 1, 1, 1),

	("arms_c05", 0, "arms_c05", 0, 0, 0, -90, 0, 0, 1, 1, 1),

	("arms_c06", 0, "arms_c06", 0, 0, 0, -90, 0, 0, 1, 1, 1),

	("arms_c07", 0, "arms_c07", 0, 0, 0, -90, 0, 0, 1, 1, 1),

	("arms_c08", 0, "arms_c08", 0, 0, 0, -90, 0, 0, 1, 1, 1),

	("arms_c09", 0, "arms_c09", 0, 0, 0, -90, 0, 0, 1, 1, 1),

	("arms_c10", 0, "arms_c10", 0, 0, 0, -90, 0, 0, 1, 1, 1),

	("arms_c11", 0, "arms_c11", 0, 0, 0, -90, 0, 0, 1, 1, 1),

	("arms_c12", 0, "arms_c12", 0, 0, 0, -90, 0, 0, 1, 1, 1),

	("arms_c13", 0, "arms_c13", 0, 0, 0, -90, 0, 0, 1, 1, 1),

	("arms_c14", 0, "arms_c14", 0, 0, 0, -90, 0, 0, 1, 1, 1),

	("arms_c15", 0, "arms_c15", 0, 0, 0, -90, 0, 0, 1, 1, 1),

	("arms_c16", 0, "arms_c16", 0, 0, 0, -90, 0, 0, 1, 1, 1),

	("arms_c17", 0, "arms_c17", 0, 0, 0, -90, 0, 0, 1, 1, 1),

	("arms_c18", 0, "arms_c18", 0, 0, 0, -90, 0, 0, 1, 1, 1),

	("arms_c19", 0, "arms_c19", 0, 0, 0, -90, 0, 0, 1, 1, 1),

	("arms_c20", 0, "arms_c20", 0, 0, 0, -90, 0, 0, 1, 1, 1),

	("arms_c21", 0, "arms_c21", 0, 0, 0, -90, 0, 0, 1, 1, 1),

	("arms_d01", 0, "arms_d01", 0, 0, 0, -90, 0, 0, 1, 1, 1),

	("arms_d02", 0, "arms_d02", 0, 0, 0, -90, 0, 0, 1, 1, 1),

	("arms_d03", 0, "arms_d03", 0, 0, 0, -90, 0, 0, 1, 1, 1),

	("arms_d04", 0, "arms_d04", 0, 0, 0, -90, 0, 0, 1, 1, 1),

	("arms_d05", 0, "arms_d05", 0, 0, 0, -90, 0, 0, 1, 1, 1),

	("arms_d06", 0, "arms_d06", 0, 0, 0, -90, 0, 0, 1, 1, 1),

	("arms_d07", 0, "arms_d07", 0, 0, 0, -90, 0, 0, 1, 1, 1),

	("arms_d08", 0, "arms_d08", 0, 0, 0, -90, 0, 0, 1, 1, 1),

	("arms_d09", 0, "arms_d09", 0, 0, 0, -90, 0, 0, 1, 1, 1),

	("arms_d10", 0, "arms_d10", 0, 0, 0, -90, 0, 0, 1, 1, 1),

	("arms_d11", 0, "arms_d11", 0, 0, 0, -90, 0, 0, 1, 1, 1),

	("arms_d12", 0, "arms_d12", 0, 0, 0, -90, 0, 0, 1, 1, 1),

	("arms_d13", 0, "arms_d13", 0, 0, 0, -90, 0, 0, 1, 1, 1),

	("arms_d14", 0, "arms_d14", 0, 0, 0, -90, 0, 0, 1, 1, 1),

	("arms_d15", 0, "arms_d15", 0, 0, 0, -90, 0, 0, 1, 1, 1),

	("arms_d16", 0, "arms_d16", 0, 0, 0, -90, 0, 0, 1, 1, 1),

	("arms_d17", 0, "arms_d17", 0, 0, 0, -90, 0, 0, 1, 1, 1),

	("arms_d18", 0, "arms_d18", 0, 0, 0, -90, 0, 0, 1, 1, 1),

	("arms_d19", 0, "arms_d19", 0, 0, 0, -90, 0, 0, 1, 1, 1),

	("arms_d20", 0, "arms_d20", 0, 0, 0, -90, 0, 0, 1, 1, 1),

	("arms_d21", 0, "arms_d21", 0, 0, 0, -90, 0, 0, 1, 1, 1),

	("arms_e01", 0, "arms_e01", 0, 0, 0, -90, 0, 0, 1, 1, 1),

	("arms_e02", 0, "arms_e02", 0, 0, 0, -90, 0, 0, 1, 1, 1),

	("arms_e03", 0, "arms_e03", 0, 0, 0, -90, 0, 0, 1, 1, 1),

	("arms_e04", 0, "arms_e04", 0, 0, 0, -90, 0, 0, 1, 1, 1),

	("arms_e05", 0, "arms_e05", 0, 0, 0, -90, 0, 0, 1, 1, 1),

	("arms_e06", 0, "arms_e06", 0, 0, 0, -90, 0, 0, 1, 1, 1),

	("arms_e07", 0, "arms_e07", 0, 0, 0, -90, 0, 0, 1, 1, 1),

	("arms_e08", 0, "arms_e08", 0, 0, 0, -90, 0, 0, 1, 1, 1),

	("arms_e09", 0, "arms_e09", 0, 0, 0, -90, 0, 0, 1, 1, 1),

	("arms_e10", 0, "arms_e10", 0, 0, 0, -90, 0, 0, 1, 1, 1),

	("arms_e11", 0, "arms_e11", 0, 0, 0, -90, 0, 0, 1, 1, 1),

	("arms_e12", 0, "arms_e12", 0, 0, 0, -90, 0, 0, 1, 1, 1),

	("arms_e13", 0, "arms_e13", 0, 0, 0, -90, 0, 0, 1, 1, 1),

	("arms_e14", 0, "arms_e14", 0, 0, 0, -90, 0, 0, 1, 1, 1),

	("arms_e15", 0, "arms_e15", 0, 0, 0, -90, 0, 0, 1, 1, 1),

	("arms_e16", 0, "arms_e16", 0, 0, 0, -90, 0, 0, 1, 1, 1),

	("arms_e17", 0, "arms_e17", 0, 0, 0, -90, 0, 0, 1, 1, 1),

	("arms_e18", 0, "arms_e18", 0, 0, 0, -90, 0, 0, 1, 1, 1),

	("arms_e19", 0, "arms_e19", 0, 0, 0, -90, 0, 0, 1, 1, 1),

	("arms_e20", 0, "arms_e20", 0, 0, 0, -90, 0, 0, 1, 1, 1),

	("arms_e21", 0, "arms_e21", 0, 0, 0, -90, 0, 0, 1, 1, 1),

	("arms_f01", 0, "arms_f01", 0, 0, 0, -90, 0, 0, 1, 1, 1),

	("arms_f02", 0, "arms_f02", 0, 0, 0, -90, 0, 0, 1, 1, 1),

	("arms_f03", 0, "arms_f03", 0, 0, 0, -90, 0, 0, 1, 1, 1),

	("arms_f04", 0, "arms_f04", 0, 0, 0, -90, 0, 0, 1, 1, 1),

	("arms_f05", 0, "arms_f05", 0, 0, 0, -90, 0, 0, 1, 1, 1),

	("arms_f06", 0, "arms_f06", 0, 0, 0, -90, 0, 0, 1, 1, 1),

	("arms_f07", 0, "arms_f07", 0, 0, 0, -90, 0, 0, 1, 1, 1),

	("arms_f08", 0, "arms_f08", 0, 0, 0, -90, 0, 0, 1, 1, 1),

	("arms_f09", 0, "arms_f09", 0, 0, 0, -90, 0, 0, 1, 1, 1),

	("arms_f10", 0, "arms_f10", 0, 0, 0, -90, 0, 0, 1, 1, 1),

	("arms_f11", 0, "arms_f11", 0, 0, 0, -90, 0, 0, 1, 1, 1),

	("arms_f12", 0, "arms_f12", 0, 0, 0, -90, 0, 0, 1, 1, 1),

	("arms_f13", 0, "arms_f13", 0, 0, 0, -90, 0, 0, 1, 1, 1),

	("arms_f14", 0, "arms_f14", 0, 0, 0, -90, 0, 0, 1, 1, 1),

	("arms_f15", 0, "arms_f15", 0, 0, 0, -90, 0, 0, 1, 1, 1),

	("arms_f16", 0, "arms_f16", 0, 0, 0, -90, 0, 0, 1, 1, 1),

	("arms_f17", 0, "arms_f17", 0, 0, 0, -90, 0, 0, 1, 1, 1),

	("arms_f18", 0, "arms_f18", 0, 0, 0, -90, 0, 0, 1, 1, 1),

	("arms_f19", 0, "arms_f19", 0, 0, 0, -90, 0, 0, 1, 1, 1),

	("arms_f20", 0, "arms_f20", 0, 0, 0, -90, 0, 0, 1, 1, 1),

	("arms_f21", 0, "arms_f21", 0, 0, 0, -90, 0, 0, 1, 1, 1),

	("arms_g01", 0, "arms_g01", 0, 0, 0, -90, 0, 0, 1, 1, 1),

	("arms_g02", 0, "arms_g02", 0, 0, 0, -90, 0, 0, 1, 1, 1),

	("arms_g03", 0, "arms_g03", 0, 0, 0, -90, 0, 0, 1, 1, 1),

	("arms_g04", 0, "arms_g04", 0, 0, 0, -90, 0, 0, 1, 1, 1),

	("arms_g05", 0, "arms_g05", 0, 0, 0, -90, 0, 0, 1, 1, 1),

	("arms_g06", 0, "arms_g06", 0, 0, 0, -90, 0, 0, 1, 1, 1),

	("arms_g07", 0, "arms_g07", 0, 0, 0, -90, 0, 0, 1, 1, 1),

	("arms_g08", 0, "arms_g08", 0, 0, 0, -90, 0, 0, 1, 1, 1),

	("arms_g09", 0, "arms_g09", 0, 0, 0, -90, 0, 0, 1, 1, 1),

	("arms_g10", 0, "arms_g10", 0, 0, 0, -90, 0, 0, 1, 1, 1),

	("arms_g11", 0, "arms_g11", 0, 0, 0, -90, 0, 0, 1, 1, 1),

	("arms_g12", 0, "arms_g12", 0, 0, 0, -90, 0, 0, 1, 1, 1),

	("arms_g13", 0, "arms_g13", 0, 0, 0, -90, 0, 0, 1, 1, 1),

	("arms_g14", 0, "arms_g14", 0, 0, 0, -90, 0, 0, 1, 1, 1),

	("arms_g15", 0, "arms_g15", 0, 0, 0, -90, 0, 0, 1, 1, 1),

	("arms_g16", 0, "arms_g16", 0, 0, 0, -90, 0, 0, 1, 1, 1),

	("arms_g17", 0, "arms_g17", 0, 0, 0, -90, 0, 0, 1, 1, 1),

	("arms_g18", 0, "arms_g18", 0, 0, 0, -90, 0, 0, 1, 1, 1),

	("arms_g19", 0, "arms_g19", 0, 0, 0, -90, 0, 0, 1, 1, 1),

	("arms_g20", 0, "arms_g20", 0, 0, 0, -90, 0, 0, 1, 1, 1),

	("arms_g21", 0, "arms_g21", 0, 0, 0, -90, 0, 0, 1, 1, 1),

	("arms_h01", 0, "arms_h01", 0, 0, 0, -90, 0, 0, 1, 1, 1),

	("arms_h02", 0, "arms_h02", 0, 0, 0, -90, 0, 0, 1, 1, 1),

	("arms_h03", 0, "arms_h03", 0, 0, 0, -90, 0, 0, 1, 1, 1),

	("arms_h04", 0, "arms_h04", 0, 0, 0, -90, 0, 0, 1, 1, 1),

	("arms_h05", 0, "arms_h05", 0, 0, 0, -90, 0, 0, 1, 1, 1),

	("arms_h06", 0, "arms_h06", 0, 0, 0, -90, 0, 0, 1, 1, 1),

	("arms_h07", 0, "arms_h07", 0, 0, 0, -90, 0, 0, 1, 1, 1),

	("arms_h08", 0, "arms_h08", 0, 0, 0, -90, 0, 0, 1, 1, 1),

	("arms_h09", 0, "arms_h09", 0, 0, 0, -90, 0, 0, 1, 1, 1),

	("arms_h10", 0, "arms_h10", 0, 0, 0, -90, 0, 0, 1, 1, 1),

	("arms_h11", 0, "arms_h11", 0, 0, 0, -90, 0, 0, 1, 1, 1),

	("arms_h12", 0, "arms_h12", 0, 0, 0, -90, 0, 0, 1, 1, 1),

	("arms_h13", 0, "arms_h13", 0, 0, 0, -90, 0, 0, 1, 1, 1),

	("arms_h14", 0, "arms_h14", 0, 0, 0, -90, 0, 0, 1, 1, 1),

	("arms_h15", 0, "arms_h15", 0, 0, 0, -90, 0, 0, 1, 1, 1),

	("arms_h16", 0, "arms_h16", 0, 0, 0, -90, 0, 0, 1, 1, 1),

	("arms_h17", 0, "arms_h17", 0, 0, 0, -90, 0, 0, 1, 1, 1),

	("arms_h18", 0, "arms_h18", 0, 0, 0, -90, 0, 0, 1, 1, 1),

	("arms_h19", 0, "arms_h19", 0, 0, 0, -90, 0, 0, 1, 1, 1),

	("arms_h20", 0, "arms_h20", 0, 0, 0, -90, 0, 0, 1, 1, 1),

	("arms_h21", 0, "arms_h21", 0, 0, 0, -90, 0, 0, 1, 1, 1),

	("arms_i01", 0, "arms_i01", 0, 0, 0, -90, 0, 0, 1, 1, 1),

	("arms_i02", 0, "arms_i02", 0, 0, 0, -90, 0, 0, 1, 1, 1),

	("arms_i03", 0, "arms_i03", 0, 0, 0, -90, 0, 0, 1, 1, 1),

	("arms_i04", 0, "arms_i04", 0, 0, 0, -90, 0, 0, 1, 1, 1),

	("arms_i05", 0, "arms_i05", 0, 0, 0, -90, 0, 0, 1, 1, 1),

	("arms_i06", 0, "arms_i06", 0, 0, 0, -90, 0, 0, 1, 1, 1),

	("arms_i07", 0, "arms_i07", 0, 0, 0, -90, 0, 0, 1, 1, 1),

	("arms_i08", 0, "arms_i08", 0, 0, 0, -90, 0, 0, 1, 1, 1),

	("arms_i09", 0, "arms_i09", 0, 0, 0, -90, 0, 0, 1, 1, 1),

	("arms_i10", 0, "arms_i10", 0, 0, 0, -90, 0, 0, 1, 1, 1),

	("arms_i11", 0, "arms_i11", 0, 0, 0, -90, 0, 0, 1, 1, 1),

	("arms_i12", 0, "arms_i12", 0, 0, 0, -90, 0, 0, 1, 1, 1),

	("arms_i13", 0, "arms_i13", 0, 0, 0, -90, 0, 0, 1, 1, 1),

	("arms_i14", 0, "arms_i14", 0, 0, 0, -90, 0, 0, 1, 1, 1),

	("arms_i15", 0, "arms_i15", 0, 0, 0, -90, 0, 0, 1, 1, 1),

	("arms_i16", 0, "arms_i16", 0, 0, 0, -90, 0, 0, 1, 1, 1),

	("arms_i17", 0, "arms_i17", 0, 0, 0, -90, 0, 0, 1, 1, 1),

	("arms_i18", 0, "arms_i18", 0, 0, 0, -90, 0, 0, 1, 1, 1),

	("arms_i19", 0, "arms_i19", 0, 0, 0, -90, 0, 0, 1, 1, 1),

	("arms_i20", 0, "arms_i20", 0, 0, 0, -90, 0, 0, 1, 1, 1),

	("arms_i21", 0, "arms_i21", 0, 0, 0, -90, 0, 0, 1, 1, 1),

	("arms_j01", 0, "arms_j01", 0, 0, 0, -90, 0, 0, 1, 1, 1),

	("arms_j02", 0, "arms_j02", 0, 0, 0, -90, 0, 0, 1, 1, 1),

	("arms_j03", 0, "arms_j03", 0, 0, 0, -90, 0, 0, 1, 1, 1),

	("arms_j04", 0, "arms_j04", 0, 0, 0, -90, 0, 0, 1, 1, 1),

	("arms_j05", 0, "arms_j05", 0, 0, 0, -90, 0, 0, 1, 1, 1),

	("arms_j06", 0, "arms_j06", 0, 0, 0, -90, 0, 0, 1, 1, 1),

	("arms_j07", 0, "arms_j07", 0, 0, 0, -90, 0, 0, 1, 1, 1),

	("arms_j08", 0, "arms_j08", 0, 0, 0, -90, 0, 0, 1, 1, 1),

	("arms_j09", 0, "arms_j09", 0, 0, 0, -90, 0, 0, 1, 1, 1),

	("arms_j10", 0, "arms_j10", 0, 0, 0, -90, 0, 0, 1, 1, 1),

	("arms_j11", 0, "arms_j11", 0, 0, 0, -90, 0, 0, 1, 1, 1),

	("arms_j12", 0, "arms_j12", 0, 0, 0, -90, 0, 0, 1, 1, 1),

	("arms_j13", 0, "arms_j13", 0, 0, 0, -90, 0, 0, 1, 1, 1),

	("arms_j14", 0, "arms_j14", 0, 0, 0, -90, 0, 0, 1, 1, 1),

	("arms_j15", 0, "arms_j15", 0, 0, 0, -90, 0, 0, 1, 1, 1),

	("arms_j16", 0, "arms_j16", 0, 0, 0, -90, 0, 0, 1, 1, 1),

	("arms_j17", 0, "arms_j17", 0, 0, 0, -90, 0, 0, 1, 1, 1),

	("arms_j18", 0, "arms_j18", 0, 0, 0, -90, 0, 0, 1, 1, 1),

	("arms_j19", 0, "arms_j19", 0, 0, 0, -90, 0, 0, 1, 1, 1),

	("arms_j20", 0, "arms_j20", 0, 0, 0, -90, 0, 0, 1, 1, 1),

	("arms_j21", 0, "arms_j21", 0, 0, 0, -90, 0, 0, 1, 1, 1),

	("arms_k01", 0, "arms_k01", 0, 0, 0, -90, 0, 0, 1, 1, 1),

	("arms_k02", 0, "arms_k02", 0, 0, 0, -90, 0, 0, 1, 1, 1),

	("arms_k03", 0, "arms_k03", 0, 0, 0, -90, 0, 0, 1, 1, 1),

	("arms_k04", 0, "arms_k04", 0, 0, 0, -90, 0, 0, 1, 1, 1),

	("arms_k05", 0, "arms_k05", 0, 0, 0, -90, 0, 0, 1, 1, 1),

	("arms_k06", 0, "arms_k06", 0, 0, 0, -90, 0, 0, 1, 1, 1),

	("arms_k07", 0, "arms_k07", 0, 0, 0, -90, 0, 0, 1, 1, 1),

	("arms_k08", 0, "arms_k08", 0, 0, 0, -90, 0, 0, 1, 1, 1),

	("arms_k09", 0, "arms_k09", 0, 0, 0, -90, 0, 0, 1, 1, 1),

	("arms_k10", 0, "arms_k10", 0, 0, 0, -90, 0, 0, 1, 1, 1),

	("arms_k11", 0, "arms_k11", 0, 0, 0, -90, 0, 0, 1, 1, 1),

	("arms_k12", 0, "arms_k12", 0, 0, 0, -90, 0, 0, 1, 1, 1),

	("arms_k13", 0, "arms_k13", 0, 0, 0, -90, 0, 0, 1, 1, 1),

	("arms_k14", 0, "arms_k14", 0, 0, 0, -90, 0, 0, 1, 1, 1),

	("arms_k15", 0, "arms_k15", 0, 0, 0, -90, 0, 0, 1, 1, 1),

	("arms_k16", 0, "arms_k16", 0, 0, 0, -90, 0, 0, 1, 1, 1),

	("arms_k17", 0, "arms_k17", 0, 0, 0, -90, 0, 0, 1, 1, 1),

	("arms_k18", 0, "arms_k18", 0, 0, 0, -90, 0, 0, 1, 1, 1),

	("arms_k19", 0, "arms_k19", 0, 0, 0, -90, 0, 0, 1, 1, 1),

	("arms_k20", 0, "arms_k20", 0, 0, 0, -90, 0, 0, 1, 1, 1),

	("arms_k21", 0, "arms_k21", 0, 0, 0, -90, 0, 0, 1, 1, 1),

	("arms_l01", 0, "arms_l01", 0, 0, 0, -90, 0, 0, 1, 1, 1),

	("arms_l02", 0, "arms_l02", 0, 0, 0, -90, 0, 0, 1, 1, 1),

	("arms_l03", 0, "arms_l03", 0, 0, 0, -90, 0, 0, 1, 1, 1),

	("arms_l04", 0, "arms_l04", 0, 0, 0, -90, 0, 0, 1, 1, 1),

	("arms_l05", 0, "arms_l05", 0, 0, 0, -90, 0, 0, 1, 1, 1),

	("arms_l06", 0, "arms_l06", 0, 0, 0, -90, 0, 0, 1, 1, 1),

	("arms_l07", 0, "arms_l07", 0, 0, 0, -90, 0, 0, 1, 1, 1),

	("arms_l08", 0, "arms_l08", 0, 0, 0, -90, 0, 0, 1, 1, 1),

	("arms_l09", 0, "arms_l09", 0, 0, 0, -90, 0, 0, 1, 1, 1),

	("arms_l10", 0, "arms_l10", 0, 0, 0, -90, 0, 0, 1, 1, 1),

	("arms_l11", 0, "arms_l11", 0, 0, 0, -90, 0, 0, 1, 1, 1),

	("arms_l12", 0, "arms_l12", 0, 0, 0, -90, 0, 0, 1, 1, 1),

	("arms_l13", 0, "arms_l13", 0, 0, 0, -90, 0, 0, 1, 1, 1),

	("arms_l14", 0, "arms_l14", 0, 0, 0, -90, 0, 0, 1, 1, 1),

	("arms_l15", 0, "arms_l15", 0, 0, 0, -90, 0, 0, 1, 1, 1),

	("arms_l16", 0, "arms_l16", 0, 0, 0, -90, 0, 0, 1, 1, 1),

	("arms_l17", 0, "arms_l17", 0, 0, 0, -90, 0, 0, 1, 1, 1),

	("arms_l18", 0, "arms_l18", 0, 0, 0, -90, 0, 0, 1, 1, 1),

	("arms_l19", 0, "arms_l19", 0, 0, 0, -90, 0, 0, 1, 1, 1),

	("arms_l20", 0, "arms_l20", 0, 0, 0, -90, 0, 0, 1, 1, 1),

	("arms_l21", 0, "arms_l21", 0, 0, 0, -90, 0, 0, 1, 1, 1),

	("arms_lords_swadia01", 0, "arms_lords_swadia01", 0, 0, 0, -90, 0, 0, 1, 1, 1),

	("arms_lords_swadia02", 0, "arms_lords_swadia02", 0, 0, 0, -90, 0, 0, 1, 1, 1),

	("arms_lords_swadia03", 0, "arms_lords_swadia03", 0, 0, 0, -90, 0, 0, 1, 1, 1),

	("arms_lords_swadia04", 0, "arms_lords_swadia04", 0, 0, 0, -90, 0, 0, 1, 1, 1),

	("arms_lords_swadia05", 0, "arms_lords_swadia05", 0, 0, 0, -90, 0, 0, 1, 1, 1),

	("arms_lords_swadia06", 0, "arms_lords_swadia06", 0, 0, 0, -90, 0, 0, 1, 1, 1),

	("arms_lords_swadia07", 0, "arms_lords_swadia07", 0, 0, 0, -90, 0, 0, 1, 1, 1),

	("arms_lords_swadia08", 0, "arms_lords_swadia08", 0, 0, 0, -90, 0, 0, 1, 1, 1),

	("arms_lords_swadia09", 0, "arms_lords_swadia09", 0, 0, 0, -90, 0, 0, 1, 1, 1),

	("arms_lords_swadia10", 0, "arms_lords_swadia10", 0, 0, 0, -90, 0, 0, 1, 1, 1),

	("arms_lords_swadia11", 0, "arms_lords_swadia11", 0, 0, 0, -90, 0, 0, 1, 1, 1),

	("arms_lords_swadia12", 0, "arms_lords_swadia12", 0, 0, 0, -90, 0, 0, 1, 1, 1),

	("arms_lords_swadia13", 0, "arms_lords_swadia13", 0, 0, 0, -90, 0, 0, 1, 1, 1),

	("arms_lords_swadia14", 0, "arms_lords_swadia14", 0, 0, 0, -90, 0, 0, 1, 1, 1),

	("arms_lords_swadia15", 0, "arms_lords_swadia15", 0, 0, 0, -90, 0, 0, 1, 1, 1),

	("arms_lords_swadia16", 0, "arms_lords_swadia16", 0, 0, 0, -90, 0, 0, 1, 1, 1),

	("arms_lords_swadia17", 0, "arms_lords_swadia17", 0, 0, 0, -90, 0, 0, 1, 1, 1),

	("arms_lords_swadia18", 0, "arms_lords_swadia18", 0, 0, 0, -90, 0, 0, 1, 1, 1),

	("arms_lords_swadia19", 0, "arms_lords_swadia19", 0, 0, 0, -90, 0, 0, 1, 1, 1),

	("arms_lords_swadia20", 0, "arms_lords_swadia20", 0, 0, 0, -90, 0, 0, 1, 1, 1),

	("arms_lords_swadia21", 0, "arms_lords_swadia21", 0, 0, 0, -90, 0, 0, 1, 1, 1),

	("arms_lords_vaegir01", 0, "arms_lords_vaegir01", 0, 0, 0, -90, 0, 0, 1, 1, 1),

	("arms_lords_vaegir02", 0, "arms_lords_vaegir02", 0, 0, 0, -90, 0, 0, 1, 1, 1),

	("arms_lords_vaegir03", 0, "arms_lords_vaegir03", 0, 0, 0, -90, 0, 0, 1, 1, 1),

	("arms_lords_vaegir04", 0, "arms_lords_vaegir04", 0, 0, 0, -90, 0, 0, 1, 1, 1),

	("arms_lords_vaegir05", 0, "arms_lords_vaegir05", 0, 0, 0, -90, 0, 0, 1, 1, 1),

	("arms_lords_vaegir06", 0, "arms_lords_vaegir06", 0, 0, 0, -90, 0, 0, 1, 1, 1),

	("arms_lords_vaegir07", 0, "arms_lords_vaegir07", 0, 0, 0, -90, 0, 0, 1, 1, 1),

	("arms_lords_vaegir08", 0, "arms_lords_vaegir08", 0, 0, 0, -90, 0, 0, 1, 1, 1),

	("arms_lords_vaegir09", 0, "arms_lords_vaegir09", 0, 0, 0, -90, 0, 0, 1, 1, 1),

	("arms_lords_vaegir10", 0, "arms_lords_vaegir10", 0, 0, 0, -90, 0, 0, 1, 1, 1),

	("arms_lords_vaegir11", 0, "arms_lords_vaegir11", 0, 0, 0, -90, 0, 0, 1, 1, 1),

	("arms_lords_vaegir12", 0, "arms_lords_vaegir12", 0, 0, 0, -90, 0, 0, 1, 1, 1),

	("arms_lords_vaegir13", 0, "arms_lords_vaegir13", 0, 0, 0, -90, 0, 0, 1, 1, 1),

	("arms_lords_vaegir14", 0, "arms_lords_vaegir14", 0, 0, 0, -90, 0, 0, 1, 1, 1),

	("arms_lords_vaegir15", 0, "arms_lords_vaegir15", 0, 0, 0, -90, 0, 0, 1, 1, 1),

	("arms_lords_vaegir16", 0, "arms_lords_vaegir16", 0, 0, 0, -90, 0, 0, 1, 1, 1),

	("arms_lords_vaegir17", 0, "arms_lords_vaegir17", 0, 0, 0, -90, 0, 0, 1, 1, 1),

	("arms_lords_vaegir18", 0, "arms_lords_vaegir18", 0, 0, 0, -90, 0, 0, 1, 1, 1),

	("arms_lords_vaegir19", 0, "arms_lords_vaegir19", 0, 0, 0, -90, 0, 0, 1, 1, 1),

	("arms_lords_vaegir20", 0, "arms_lords_vaegir20", 0, 0, 0, -90, 0, 0, 1, 1, 1),

	("arms_lords_vaegir21", 0, "arms_lords_vaegir21", 0, 0, 0, -90, 0, 0, 1, 1, 1),

	("arms_lords_khergit01", 0, "arms_lords_khergit01", 0, 0, 0, -90, 0, 0, 1, 1, 1),

	("arms_lords_khergit02", 0, "arms_lords_khergit02", 0, 0, 0, -90, 0, 0, 1, 1, 1),

	("arms_lords_khergit03", 0, "arms_lords_khergit03", 0, 0, 0, -90, 0, 0, 1, 1, 1),

	("arms_lords_khergit04", 0, "arms_lords_khergit04", 0, 0, 0, -90, 0, 0, 1, 1, 1),

	("arms_lords_khergit05", 0, "arms_lords_khergit05", 0, 0, 0, -90, 0, 0, 1, 1, 1),

	("arms_lords_khergit06", 0, "arms_lords_khergit06", 0, 0, 0, -90, 0, 0, 1, 1, 1),

	("arms_lords_khergit07", 0, "arms_lords_khergit07", 0, 0, 0, -90, 0, 0, 1, 1, 1),

	("arms_lords_khergit08", 0, "arms_lords_khergit08", 0, 0, 0, -90, 0, 0, 1, 1, 1),

	("arms_lords_khergit09", 0, "arms_lords_khergit09", 0, 0, 0, -90, 0, 0, 1, 1, 1),

	("arms_lords_khergit10", 0, "arms_lords_khergit10", 0, 0, 0, -90, 0, 0, 1, 1, 1),

	("arms_lords_khergit11", 0, "arms_lords_khergit11", 0, 0, 0, -90, 0, 0, 1, 1, 1),

	("arms_lords_khergit12", 0, "arms_lords_khergit12", 0, 0, 0, -90, 0, 0, 1, 1, 1),

	("arms_lords_khergit13", 0, "arms_lords_khergit13", 0, 0, 0, -90, 0, 0, 1, 1, 1),

	("arms_lords_khergit14", 0, "arms_lords_khergit14", 0, 0, 0, -90, 0, 0, 1, 1, 1),

	("arms_lords_khergit15", 0, "arms_lords_khergit15", 0, 0, 0, -90, 0, 0, 1, 1, 1),

	("arms_lords_khergit16", 0, "arms_lords_khergit16", 0, 0, 0, -90, 0, 0, 1, 1, 1),

	("arms_lords_khergit17", 0, "arms_lords_khergit17", 0, 0, 0, -90, 0, 0, 1, 1, 1),

	("arms_lords_khergit18", 0, "arms_lords_khergit18", 0, 0, 0, -90, 0, 0, 1, 1, 1),

	("arms_lords_khergit19", 0, "arms_lords_khergit19", 0, 0, 0, -90, 0, 0, 1, 1, 1),

	("arms_lords_khergit20", 0, "arms_lords_khergit20", 0, 0, 0, -90, 0, 0, 1, 1, 1),

	("arms_lords_khergit21", 0, "arms_lords_khergit21", 0, 0, 0, -90, 0, 0, 1, 1, 1),

	("arms_lords_nord01", 0, "arms_lords_nord01", 0, 0, 0, -90, 0, 0, 1, 1, 1),

	("arms_lords_nord02", 0, "arms_lords_nord02", 0, 0, 0, -90, 0, 0, 1, 1, 1),

	("arms_lords_nord03", 0, "arms_lords_nord03", 0, 0, 0, -90, 0, 0, 1, 1, 1),

	("arms_lords_nord04", 0, "arms_lords_nord04", 0, 0, 0, -90, 0, 0, 1, 1, 1),

	("arms_lords_nord05", 0, "arms_lords_nord05", 0, 0, 0, -90, 0, 0, 1, 1, 1),

	("arms_lords_nord06", 0, "arms_lords_nord06", 0, 0, 0, -90, 0, 0, 1, 1, 1),

	("arms_lords_nord07", 0, "arms_lords_nord07", 0, 0, 0, -90, 0, 0, 1, 1, 1),

	("arms_lords_nord08", 0, "arms_lords_nord08", 0, 0, 0, -90, 0, 0, 1, 1, 1),

	("arms_lords_nord09", 0, "arms_lords_nord09", 0, 0, 0, -90, 0, 0, 1, 1, 1),

	("arms_lords_nord10", 0, "arms_lords_nord10", 0, 0, 0, -90, 0, 0, 1, 1, 1),

	("arms_lords_nord11", 0, "arms_lords_nord11", 0, 0, 0, -90, 0, 0, 1, 1, 1),

	("arms_lords_nord12", 0, "arms_lords_nord12", 0, 0, 0, -90, 0, 0, 1, 1, 1),

	("arms_lords_nord13", 0, "arms_lords_nord13", 0, 0, 0, -90, 0, 0, 1, 1, 1),

	("arms_lords_nord14", 0, "arms_lords_nord14", 0, 0, 0, -90, 0, 0, 1, 1, 1),

	("arms_lords_nord15", 0, "arms_lords_nord15", 0, 0, 0, -90, 0, 0, 1, 1, 1),

	("arms_lords_nord16", 0, "arms_lords_nord16", 0, 0, 0, -90, 0, 0, 1, 1, 1),

	("arms_lords_nord17", 0, "arms_lords_nord17", 0, 0, 0, -90, 0, 0, 1, 1, 1),

	("arms_lords_nord18", 0, "arms_lords_nord18", 0, 0, 0, -90, 0, 0, 1, 1, 1),

	("arms_lords_nord19", 0, "arms_lords_nord19", 0, 0, 0, -90, 0, 0, 1, 1, 1),

	("arms_lords_nord20", 0, "arms_lords_nord20", 0, 0, 0, -90, 0, 0, 1, 1, 1),

	("arms_lords_nord21", 0, "arms_lords_nord21", 0, 0, 0, -90, 0, 0, 1, 1, 1),

	("arms_lords_rhodok01", 0, "arms_lords_rhodok01", 0, 0, 0, -90, 0, 0, 1, 1, 1),

	("arms_lords_rhodok02", 0, "arms_lords_rhodok02", 0, 0, 0, -90, 0, 0, 1, 1, 1),

	("arms_lords_rhodok03", 0, "arms_lords_rhodok03", 0, 0, 0, -90, 0, 0, 1, 1, 1),

	("arms_lords_rhodok04", 0, "arms_lords_rhodok04", 0, 0, 0, -90, 0, 0, 1, 1, 1),

	("arms_lords_rhodok05", 0, "arms_lords_rhodok05", 0, 0, 0, -90, 0, 0, 1, 1, 1),

	("arms_lords_rhodok06", 0, "arms_lords_rhodok06", 0, 0, 0, -90, 0, 0, 1, 1, 1),

	("arms_lords_rhodok07", 0, "arms_lords_rhodok07", 0, 0, 0, -90, 0, 0, 1, 1, 1),

	("arms_lords_rhodok08", 0, "arms_lords_rhodok08", 0, 0, 0, -90, 0, 0, 1, 1, 1),

	("arms_lords_rhodok09", 0, "arms_lords_rhodok09", 0, 0, 0, -90, 0, 0, 1, 1, 1),

	("arms_lords_rhodok10", 0, "arms_lords_rhodok10", 0, 0, 0, -90, 0, 0, 1, 1, 1),

	("arms_lords_rhodok11", 0, "arms_lords_rhodok11", 0, 0, 0, -90, 0, 0, 1, 1, 1),

	("arms_lords_rhodok12", 0, "arms_lords_rhodok12", 0, 0, 0, -90, 0, 0, 1, 1, 1),

	("arms_lords_rhodok13", 0, "arms_lords_rhodok13", 0, 0, 0, -90, 0, 0, 1, 1, 1),

	("arms_lords_rhodok14", 0, "arms_lords_rhodok14", 0, 0, 0, -90, 0, 0, 1, 1, 1),

	("arms_lords_rhodok15", 0, "arms_lords_rhodok15", 0, 0, 0, -90, 0, 0, 1, 1, 1),

	("arms_lords_rhodok16", 0, "arms_lords_rhodok16", 0, 0, 0, -90, 0, 0, 1, 1, 1),

	("arms_lords_rhodok17", 0, "arms_lords_rhodok17", 0, 0, 0, -90, 0, 0, 1, 1, 1),

	("arms_lords_rhodok18", 0, "arms_lords_rhodok18", 0, 0, 0, -90, 0, 0, 1, 1, 1),

	("arms_lords_rhodok19", 0, "arms_lords_rhodok19", 0, 0, 0, -90, 0, 0, 1, 1, 1),

	("arms_lords_rhodok20", 0, "arms_lords_rhodok20", 0, 0, 0, -90, 0, 0, 1, 1, 1),

	("arms_lords_rhodok21", 0, "arms_lords_rhodok21", 0, 0, 0, -90, 0, 0, 1, 1, 1),

	("arms_lords_sarranid01", 0, "arms_lords_sarranid01", 0, 0, 0, -90, 0, 0, 1, 1, 1),

	("arms_lords_sarranid02", 0, "arms_lords_sarranid02", 0, 0, 0, -90, 0, 0, 1, 1, 1),

	("arms_lords_sarranid03", 0, "arms_lords_sarranid03", 0, 0, 0, -90, 0, 0, 1, 1, 1),

	("arms_lords_sarranid04", 0, "arms_lords_sarranid04", 0, 0, 0, -90, 0, 0, 1, 1, 1),

	("arms_lords_sarranid05", 0, "arms_lords_sarranid05", 0, 0, 0, -90, 0, 0, 1, 1, 1),

	("arms_lords_sarranid06", 0, "arms_lords_sarranid06", 0, 0, 0, -90, 0, 0, 1, 1, 1),

	("arms_lords_sarranid07", 0, "arms_lords_sarranid07", 0, 0, 0, -90, 0, 0, 1, 1, 1),

	("arms_lords_sarranid08", 0, "arms_lords_sarranid08", 0, 0, 0, -90, 0, 0, 1, 1, 1),

	("arms_lords_sarranid09", 0, "arms_lords_sarranid09", 0, 0, 0, -90, 0, 0, 1, 1, 1),

	("arms_lords_sarranid10", 0, "arms_lords_sarranid10", 0, 0, 0, -90, 0, 0, 1, 1, 1),

	("arms_lords_sarranid11", 0, "arms_lords_sarranid11", 0, 0, 0, -90, 0, 0, 1, 1, 1),

	("arms_lords_sarranid12", 0, "arms_lords_sarranid12", 0, 0, 0, -90, 0, 0, 1, 1, 1),

	("arms_lords_sarranid13", 0, "arms_lords_sarranid13", 0, 0, 0, -90, 0, 0, 1, 1, 1),

	("arms_lords_sarranid14", 0, "arms_lords_sarranid14", 0, 0, 0, -90, 0, 0, 1, 1, 1),

	("arms_lords_sarranid15", 0, "arms_lords_sarranid15", 0, 0, 0, -90, 0, 0, 1, 1, 1),

	("arms_lords_sarranid16", 0, "arms_lords_sarranid16", 0, 0, 0, -90, 0, 0, 1, 1, 1),

	("arms_lords_sarranid17", 0, "arms_lords_sarranid17", 0, 0, 0, -90, 0, 0, 1, 1, 1),

	("arms_lords_sarranid18", 0, "arms_lords_sarranid18", 0, 0, 0, -90, 0, 0, 1, 1, 1),

	("arms_lords_sarranid19", 0, "arms_lords_sarranid19", 0, 0, 0, -90, 0, 0, 1, 1, 1),

	("arms_lords_sarranid20", 0, "arms_lords_sarranid20", 0, 0, 0, -90, 0, 0, 1, 1, 1),

	("arms_lords_sarranid21", 0, "arms_lords_sarranid21", 0, 0, 0, -90, 0, 0, 1, 1, 1),

	("arms_companions01", 0, "arms_companions01", 0, 0, 0, -90, 0, 0, 1, 1, 1),

	("arms_companions02", 0, "arms_companions02", 0, 0, 0, -90, 0, 0, 1, 1, 1),

	("arms_companions03", 0, "arms_companions03", 0, 0, 0, -90, 0, 0, 1, 1, 1),

	("arms_companions04", 0, "arms_companions04", 0, 0, 0, -90, 0, 0, 1, 1, 1),

	("arms_companions05", 0, "arms_companions05", 0, 0, 0, -90, 0, 0, 1, 1, 1),

	("arms_companions06", 0, "arms_companions06", 0, 0, 0, -90, 0, 0, 1, 1, 1),

	("arms_companions07", 0, "arms_companions07", 0, 0, 0, -90, 0, 0, 1, 1, 1),

	("arms_companions08", 0, "arms_companions08", 0, 0, 0, -90, 0, 0, 1, 1, 1),

	("arms_companions09", 0, "arms_companions09", 0, 0, 0, -90, 0, 0, 1, 1, 1),

	("arms_companions10", 0, "arms_companions10", 0, 0, 0, -90, 0, 0, 1, 1, 1),

	("arms_companions11", 0, "arms_companions11", 0, 0, 0, -90, 0, 0, 1, 1, 1),

	("arms_companions12", 0, "arms_companions12", 0, 0, 0, -90, 0, 0, 1, 1, 1),

	("arms_companions13", 0, "arms_companions13", 0, 0, 0, -90, 0, 0, 1, 1, 1),

	("arms_companions14", 0, "arms_companions14", 0, 0, 0, -90, 0, 0, 1, 1, 1),

	("arms_companions15", 0, "arms_companions15", 0, 0, 0, -90, 0, 0, 1, 1, 1),

	("arms_companions16", 0, "arms_companions16", 0, 0, 0, -90, 0, 0, 1, 1, 1),

	("arms_companions17", 0, "arms_companions17", 0, 0, 0, -90, 0, 0, 1, 1, 1),

	("arms_companions18", 0, "arms_companions18", 0, 0, 0, -90, 0, 0, 1, 1, 1),

	("arms_companions19", 0, "arms_companions19", 0, 0, 0, -90, 0, 0, 1, 1, 1),

	("arms_companions20", 0, "arms_companions20", 0, 0, 0, -90, 0, 0, 1, 1, 1),

	("arms_companions21", 0, "arms_companions21", 0, 0, 0, -90, 0, 0, 1, 1, 1),

	("arms_companions22", 0, "arms_companions22", 0, 0, 0, -90, 0, 0, 1, 1, 1),

	("arms_bandits01", 0, "arms_bandits01", 0, 0, 0, -90, 0, 0, 1, 1, 1),

	("arms_bandits02", 0, "arms_bandits02", 0, 0, 0, -90, 0, 0, 1, 1, 1),

	("arms_bandits03", 0, "arms_bandits03", 0, 0, 0, -90, 0, 0, 1, 1, 1),

	("arms_bandits04", 0, "arms_bandits04", 0, 0, 0, -90, 0, 0, 1, 1, 1),

	("arms_bandits05", 0, "arms_bandits05", 0, 0, 0, -90, 0, 0, 1, 1, 1),

	("arms_bandits06", 0, "arms_bandits06", 0, 0, 0, -90, 0, 0, 1, 1, 1),

	("arms_bandits07", 0, "arms_bandits07", 0, 0, 0, -90, 0, 0, 1, 1, 1),

	("arms_kingdom_a", 0, "arms_kingdom_a", 0, 0, 0, -90, 0, 0, 1, 1, 1),

	("arms_kingdom_b", 0, "arms_kingdom_b", 0, 0, 0, -90, 0, 0, 1, 1, 1),

	("arms_kingdom_c", 0, "arms_kingdom_c", 0, 0, 0, -90, 0, 0, 1, 1, 1),

	("arms_kingdom_d", 0, "arms_kingdom_d", 0, 0, 0, -90, 0, 0, 1, 1, 1),

	("arms_kingdom_e", 0, "arms_kingdom_e", 0, 0, 0, -90, 0, 0, 1, 1, 1),

	("arms_kingdom_f", 0, "arms_kingdom_f", 0, 0, 0, -90, 0, 0, 1, 1, 1),

	("arms_kingdom_g", 0, "arms_kingdom_g", 0, 0, 0, -90, 0, 0, 1, 1, 1),

	("arms_kingdom_h", 0, "arms_kingdom_h", 0, 0, 0, -90, 0, 0, 1, 1, 1),

	("arms_kingdom_i", 0, "arms_kingdom_i", 0, 0, 0, -90, 0, 0, 1, 1, 1),

	("arms_kingdom_j", 0, "arms_kingdom_j", 0, 0, 0, -90, 0, 0, 1, 1, 1),

	("arms_kingdom_k", 0, "arms_kingdom_k", 0, 0, 0, -90, 0, 0, 1, 1, 1),

	("arms_kingdom_l", 0, "arms_kingdom_l", 0, 0, 0, -90, 0, 0, 1, 1, 1),

	("arms_kingdom_m", 0, "arms_kingdom_m", 0, 0, 0, -90, 0, 0, 1, 1, 1),

	("arms_kingdom_n", 0, "arms_kingdom_n", 0, 0, 0, -90, 0, 0, 1, 1, 1),

	("banners_default_a", 0, "banners_default_a", 0, 0, 0, -90, 0, 0, 1, 1, 1),

	("banners_default_b", 0, "banners_default_b", 0, 0, 0, -90, 0, 0, 1, 1, 1),

	("banners_default_c", 0, "banners_default_c", 0, 0, 0, -90, 0, 0, 1, 1, 1),

	("banners_default_d", 0, "banners_default_d", 0, 0, 0, -90, 0, 0, 1, 1, 1),

	("banners_default_e", 0, "banners_default_e", 0, 0, 0, -90, 0, 0, 1, 1, 1),

	("troop_label_banner", 0, "troop_label_banner", 0, 0, 0, 0, 0, 0, 10, 10, 10),

	("ui_kingdom_shield_1", 0, "ui_kingdom_shield_1", 0, 0, 0, 0, 0, 0, 1, 1, 1),

	("ui_kingdom_shield_2", 0, "ui_kingdom_shield_2", 0, 0, 0, 0, 0, 0, 1, 1, 1),

	("ui_kingdom_shield_3", 0, "ui_kingdom_shield_3", 0, 0, 0, 0, 0, 0, 1, 1, 1),

	("ui_kingdom_shield_4", 0, "ui_kingdom_shield_4", 0, 0, 0, 0, 0, 0, 1, 1, 1),

	("ui_kingdom_shield_5", 0, "ui_kingdom_shield_5", 0, 0, 0, 0, 0, 0, 1, 1, 1),

	("ui_kingdom_shield_6", 0, "ui_kingdom_shield_6", 0, 0, 0, 0, 0, 0, 1, 1, 1),

	("mouse_arrow_down", 0, "mouse_arrow_down", 0, 0, 0, 0, 0, 0, 1, 1, 1),

	("mouse_arrow_right", 0, "mouse_arrow_right", 0, 0, 0, 0, 0, 0, 1, 1, 1),

	("mouse_arrow_left", 0, "mouse_arrow_left", 0, 0, 0, 0, 0, 0, 1, 1, 1),

	("mouse_arrow_up", 0, "mouse_arrow_up", 0, 0, 0, 0, 0, 0, 1, 1, 1),

	("mouse_arrow_plus", 0, "mouse_arrow_plus", 0, 0, 0, 0, 0, 0, 1, 1, 1),

	("mouse_left_click", 0, "mouse_left_click", 0, 0, 0, 0, 0, 0, 1, 1, 1),

	("mouse_right_click", 0, "mouse_right_click", 0, 0, 0, 0, 0, 0, 1, 1, 1),

	("status_ammo_ready", 0, "status_ammo_ready", 0, 0, 0, 0, 0, 0, 1, 1, 1),

	("main_menu_background", 0, "main_menu_nord", 0, 0, 0, 0, 0, 0, 1, 1, 1),

	("loading_background", 0, "load_screen_2", 0, 0, 0, 0, 0, 0, 1, 1, 1),

	("ui_quick_battle_a", 0, "ui_quick_battle_a", 0, 0, 0, 0, 0, 0, 1, 1, 1),

	("white_bg_plane_a", 0, "white_bg_plane_a", 0, 0, 0, 0, 0, 0, 1, 1, 1),

	("cb_ui_icon_infantry", 0, "cb_ui_icon_infantry", 0, 0, 0, 0, 0, 0, 1, 1, 1),

	("cb_ui_icon_archer", 0, "cb_ui_icon_archer", 0, 0, 0, 0, 0, 0, 1, 1, 1),

	("cb_ui_icon_horseman", 0, "cb_ui_icon_horseman", 0, 0, 0, 0, 0, 0, 1, 1, 1),

	("cb_ui_main", 0, "cb_ui_main", 0, 0, 0, 0, 0, 0, 1, 1, 1),

	("cb_ui_maps_scene_01", 0, "cb_ui_maps_scene_01", 0, 0, 0, 0, 0, 0, 1, 1, 1),

	("cb_ui_maps_scene_02", 0, "cb_ui_maps_scene_02", 0, 0, 0, 0, 0, 0, 1, 1, 1),

	("cb_ui_maps_scene_03", 0, "cb_ui_maps_scene_03", 0, 0, 0, 0, 0, 0, 1, 1, 1),

	("cb_ui_maps_scene_04", 0, "cb_ui_maps_scene_04", 0, 0, 0, 0, 0, 0, 1, 1, 1),

	("cb_ui_maps_scene_05", 0, "cb_ui_maps_scene_05", 0, 0, 0, 0, 0, 0, 1, 1, 1),

	("cb_ui_maps_scene_06", 0, "cb_ui_maps_scene_06", 0, 0, 0, 0, 0, 0, 1, 1, 1),

	("cb_ui_maps_scene_07", 0, "cb_ui_maps_scene_07", 0, 0, 0, 0, 0, 0, 1, 1, 1),

	("cb_ui_maps_scene_08", 0, "cb_ui_maps_scene_08", 0, 0, 0, 0, 0, 0, 1, 1, 1),

	("cb_ui_maps_scene_09", 0, "cb_ui_maps_scene_09", 0, 0, 0, 0, 0, 0, 1, 1, 1),

	("mp_ui_host_maps_14", 0, "mp_ui_host_maps_c4", 0, 0, 0, 0, 0, 0, 1, 1, 1),

	("mp_ui_host_maps_15", 0, "mp_ui_host_maps_c5", 0, 0, 0, 0, 0, 0, 1, 1, 1),

	("quit_adv", 0, "quit_adv", 0, 0, 0, 0, 0, 0, 1, 1, 1),

	("quit_adv_b", 0, "quit_adv_b", 0, 0, 0, 0, 0, 0, 1, 1, 1),

	("ui_kingdom_shield_7", 0, "ui_kingdom_shield_7", 0, 0, 0, 0, 0, 0, 1, 1, 1),

	("flag_project_rb", 0, "flag_project_rb", 0, 0, 0, 0, 0, 0, 1, 1, 1),

	("flag_project_rb_miss", 0, "flag_project_rb_miss", 0, 0, 0, 0, 0, 0, 1, 1, 1),

	("mp_ui_host_maps_16", 0, "mp_ui_host_maps_d1", 0, 0, 0, 0, 0, 0, 1, 1, 1),

	("mp_ui_host_maps_17", 0, "mp_ui_host_maps_d2", 0, 0, 0, 0, 0, 0, 1, 1, 1),

	("mp_ui_host_maps_18", 0, "mp_ui_host_maps_d3", 0, 0, 0, 0, 0, 0, 1, 1, 1),

	("longer_button", 0, "longer_button", 0, 0, 0, 0, 0, 0, 0, 0, 0),

	("longer_button_down", 0, "longer_button_down", 0, 0, 0, 0, 0, 0, 0, 0, 0),

	("options_window", 0, "options_window", 0, 0, 0, 0, 0, 0, 1, 1, 1),

	("message_window", 0, "message_window", 0, 0, 0, 0, 0, 0, 0, 0, 0),

	("note_window", 0, "note_window", 0, 0, 0, 0, 0, 0, 1, 1, 1),

	("drop_button", 0, "button_drop", 0, 0, 0, 0, 0, 0, 1, 0, 0),

	("drop_button_down", 0, "button_drop_clicked", 0, 0, 0, 0, 0, 0, 1, 0, 0),

	("drop_button_hl", 0, "button_drop_hl", 0, 0, 0, 0, 0, 0, 1, 0, 0),

	("drop_button_child", 0, "button_drop_child", 0, 0, 0, 0, 0, 0, 1, 0, 0),

	("drop_button_child_down", 0, "button_drop_child_clicked", 0, 0, 0, 0, 0, 0, 1, 0, 0),

	("drop_button_child_hl", 0, "button_drop_child_hl", 0, 0, 0, 0, 0, 0, 1, 0, 0),

	("message_window", 0, "message_window", 0, 0, 0, 0, 0, 0, 0, 0, 0),

	("message_window", 0, "message_window", 0, 0, 0, 0, 0, 0, 0, 0, 0),

	("face_gen_window", 0, "face_gen_window", 0, 0, 0, 0, 0, 0, 1, 1, 1),

	("companion_overview", 0, "companion_overview", 0, 0, 0, 0, 0, 0, 1, 1, 1),

	("companion_overview_details", 0, "companion_overview_details", 0, 0, 0, 0, 0, 0, 1, 1, 1),

	("game_log_window", 0, "game_log_window", 0, 0, 0, 0, 0, 0, 1, 1, 1),

	("mp_ui_host_maps_muiderslot", 0, "mp_ui_host_maps_muiderslot", 0, 0, 0, 0, 0, 0, 1, 1, 1),

	("note_window_bottom", 0, "note_window", 0, 0, 0, 0, 0, 0, 1, 1, 1),

	("order_frame", 0, "order_frame", 0, 0, 0, 0, 0, 0, 1, 1, 1),

	("flag4", 0, "flag4", 0, 0, 0, 0, 0, 0, 1, 1, 1),

	("flag5", 0, "flag5", 0, 0, 0, 0, 0, 0, 1, 1, 1),

	("flag6", 0, "flag6", 0, 0, 0, 0, 0, 0, 1, 1, 1),

	("flag7", 0, "flag7", 0, 0, 0, 0, 0, 0, 1, 1, 1),

	("flag8", 0, "flag8", 0, 0, 0, 0, 0, 0, 1, 1, 1),

	("flag9", 0, "flag9", 0, 0, 0, 0, 0, 0, 1, 1, 1),

	("pic_soldier_world_map", 0, "pic_soldier_world_map", 0, 0, 0, 0, 0, 0, 1, 1, 1),

	("pic_soldier_rebel", 0, "pic_soldier_rebel", 0, 0, 0, 0, 0, 0, 1, 1, 1),

	("pic_soldier_desert", 0, "pic_soldier_desert", 0, 0, 0, 0, 0, 0, 1, 1, 1),

	("background_general", 0, "pic_camp", 0, 0, 0, 0, 0, 0, 1, 1, 1),

	("lco_background", 0, "mp_ui_bg", 0, 0, 0, 0, 0, 0, 1, 1, 1),

	("lco_background_split", 0, "mp_ui_profile", 0, 0, 0, 0, 0, 0, 1, 1, 1),

	("lco_panel", 0, "longer_button", 0, 0, 0, 0, 0, 0, 1, 1, 1),

	("lco_panel_down", 0, "longer_button_down", 0, 0, 0, 0, 0, 0, 1, 1, 1),

	("lco_garbage_area", 0, "mp_score_b", 0, 0, 0, 0, 0, 0, 1, 1, 1),

	("lco_sort_inventory", 0, "small_arrow_down", 0, 0, 0, 0, 0, 0, 1, 1, 1),

	("lco_sort_inventory_down", 0, "small_arrow_down_clicked", 0, 0, 0, 0, 0, 0, 1, 1, 1),

	("lco_gold_icon", 0, "mp_ico_gold", 0, 0, 0, 0, 0, 0, 1, 1, 1),

	("lco_square_button_up", 0, "button1_up", 0, 0, 0, 0, 0, 0, 1, 1, 1),

	("lco_square_button_down", 0, "button1_down", 0, 0, 0, 0, 0, 0, 1, 1, 1),

	("pic_map_calradia_half", 0, "pic_map_calradia_half", 0, 0, 0, 0, 0, 0, 1, 0, 0),

	("character_creator", 0, "character_creation", 0, 0, 0, 0, 0, 0, 1, 0, 0),

	("golden_coins", 0, "mp_ico_gold", 0, 0, 0, 0, 0, 0, 1, 0, 0),

	("weapon_bow", 0, "ico_bow", 0, 0, 0, 0, 0, 0, 1, 0, 0),

	("weapon_crossbow", 0, "ico_crossbow", 0, 0, 0, 0, 0, 0, 1, 0, 0),

	("weapon_onehand", 0, "ico_swordone", 0, 0, 0, 0, 0, 0, 1, 0, 0),

	("weapon_twohand", 0, "ico_swordtwo", 0, 0, 0, 0, 0, 0, 1, 0, 0),

	("weapon_thorwing", 0, "ico_knifethrow", 0, 0, 0, 0, 0, 0, 1, 0, 0),

	("weapon_polearm", 0, "ico_spear", 0, 0, 0, 0, 0, 0, 1, 0, 0),

	("status_renown", 0, "mp_ico_gold_renown", 0, 0, 0, 0, 0, 0, 1, 0, 0),

]