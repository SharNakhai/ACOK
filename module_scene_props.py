# -*- coding: cp1252 -*-
from header_common import *
from header_scene_props import *
from header_operations import *
from header_triggers import *
from header_sounds import *
from module_constants import *
import string

####################################################################################################################
#  Each scene prop record contains the following fields:
#  1) Scene prop id: used for referencing scene props in other files. The prefix spr_ is automatically added before each scene prop id.
#  2) Scene prop flags. See header_scene_props.py for a list of available flags
#  3) Mesh name: Name of the mesh.
#  4) Physics object name:
#  5) Triggers: Simple triggers that are associated with the scene prop
####################################################################################################################

scene_props = [
	("invalid_object", 0, "question_mark", "0", []),

	("inventory", sokf_type_container|sokf_place_at_origin, "chest_b", "bobaggage", []),

	("empty", 0, "0", "0", []),

	("chest_a", sokf_type_container, "chest_gothic", "bochest_gothic", []),

	("container_small_chest", sokf_type_container, "chest_b", "bobaggage", []),

	("container_chest_b", sokf_type_container, "chest_b", "bo_chest_b", []),

	("container_chest_c", sokf_type_container, "chest_c", "bo_chest_c", []),

	("player_chest", sokf_type_container, "player_chest_new", "bo_player_chest", []),

	("locked_player_chest", 0, "player_chest_new", "bo_player_chest", []),

	("light_sun", sokf_invisible, "light_sphere", "0", 
	[(ti_on_scene_prop_init,
		[
			(neg|is_currently_night),
			(store_trigger_param_1, ":trigger_param_1"),
			(set_fixed_point_multiplier, 100),
			(prop_instance_get_scale, 5, ":trigger_param_1"),
			(position_get_scale_x, ":position_scale_x_5", 5),
			(store_time_of_day, reg12),
			(try_begin),
				(is_between, reg12, 5, 20),
				(store_mul, ":value", 1000, ":position_scale_x_5"),
				(store_mul, ":value_2", 965, ":position_scale_x_5"),
				(store_mul, ":value_3", 900, ":position_scale_x_5"),
			(else_try),
				(store_mul, ":value", 450, ":position_scale_x_5"),
				(store_mul, ":value_2", 575, ":position_scale_x_5"),
				(store_mul, ":value_3", 750, ":position_scale_x_5"),
			(try_end),
			(val_div, ":value", 100),
			(val_div, ":value_2", 100),
			(val_div, ":value_3", 100),
			(set_current_color, ":value", ":value_2", ":value_3"),
			(set_position_delta, 0, 0, 0),
			(add_point_light_to_entity, 0, 0)
		])
	]),

	("light", sokf_invisible, "light_sphere", "0", 
	[(ti_on_scene_prop_init,
		[
			(store_trigger_param_1, ":trigger_param_1"),
			(set_fixed_point_multiplier, 100),
			(prop_instance_get_scale, 5, ":trigger_param_1"),
			(position_get_scale_x, ":position_scale_x_5", 5),
			(store_mul, ":value", 600, ":position_scale_x_5"),
			(store_mul, ":value_2", 435, ":position_scale_x_5"),
			(store_mul, ":value_3", 135, ":position_scale_x_5"),
			(val_div, ":value", 100),
			(val_div, ":value_2", 100),
			(val_div, ":value_3", 100),
			(set_current_color, ":value", ":value_2", ":value_3"),
			(set_position_delta, 0, 0, 0),
			(add_point_light_to_entity, 10, 30)
		])
	]),

	("light_red", sokf_invisible, "light_sphere", "0", 
	[(ti_on_scene_prop_init,
		[
			(store_trigger_param_1, ":trigger_param_1"),
			(set_fixed_point_multiplier, 100),
			(prop_instance_get_scale, 5, ":trigger_param_1"),
			(position_get_scale_x, ":position_scale_x_5", 5),
			(store_mul, ":value", 340, ":position_scale_x_5"),
			(store_mul, ":value_2", 200, ":position_scale_x_5"),
			(store_mul, ":value_3", 60, ":position_scale_x_5"),
			(val_div, ":value", 100),
			(val_div, ":value_2", 100),
			(val_div, ":value_3", 100),
			(set_current_color, ":value", ":value_2", ":value_3"),
			(set_position_delta, 0, 0, 0),
			(add_point_light_to_entity, 20, 30)
		])
	]),

	("light_night", sokf_invisible, "light_sphere", "0", 
	[(ti_on_scene_prop_init,
		[
			(is_currently_night, 0),
			(store_trigger_param_1, ":trigger_param_1"),
			(set_fixed_point_multiplier, 100),
			(prop_instance_get_scale, 5, ":trigger_param_1"),
			(position_get_scale_x, ":position_scale_x_5", 5),
			(store_mul, ":value", 480, ":position_scale_x_5"),
			(store_mul, ":value_2", 435, ":position_scale_x_5"),
			(store_mul, ":value_3", 300, ":position_scale_x_5"),
			(val_div, ":value", 100),
			(val_div, ":value_2", 100),
			(val_div, ":value_3", 100),
			(set_current_color, ":value", ":value_2", ":value_3"),
			(set_position_delta, 0, 0, 0),
			(add_point_light_to_entity, 10, 30)
		])
	]),

	("torch", 0, "torch_a", "0", 
	[(ti_on_scene_prop_init,
		[
			(set_position_delta, 0, -35, 48),
			(particle_system_add_new, "psys_torch_fire"),
			(particle_system_add_new, "psys_torch_smoke"),
			(particle_system_add_new, "psys_torch_fire_sparks"),
			(play_sound, "snd_torch_loop", 0),
			(set_position_delta, 0, -35, 56),
			(particle_system_add_new, "psys_fire_glow_1"),
			(get_trigger_object_position, 2),
			(set_position_delta, 0, 0, 0),
			(position_move_y, 2, -35),
			(position_move_z, 2, 55),
			(particle_system_burst, "psys_fire_glow_fixed", 2, 1)
		])
	]),

	("torch_night", 0, "torch_a", "0", 
	[(ti_on_scene_prop_init,
		[
			(is_currently_night, 0),
			(set_position_delta, 0, -35, 48),
			(particle_system_add_new, "psys_torch_fire"),
			(particle_system_add_new, "psys_torch_smoke"),
			(particle_system_add_new, "psys_torch_fire_sparks"),
			(set_position_delta, 0, -35, 56),
			(particle_system_add_new, "psys_fire_glow_1"),
			(particle_system_emit, "psys_fire_glow_1", 9000000),
			(play_sound, "snd_torch_loop", 0)
		])
	]),

	("barrier_20m", sokf_type_barrier|sokf_invisible, "barrier_20m", "bo_barrier_20m", []),

	("barrier_16m", sokf_type_barrier|sokf_invisible, "barrier_16m", "bo_barrier_16m", []),

	("barrier_8m", sokf_type_barrier|sokf_invisible, "barrier_8m", "bo_barrier_8m", []),

	("barrier_4m", sokf_type_barrier|sokf_invisible, "barrier_4m", "bo_barrier_4m", []),

	("barrier_2m", sokf_type_barrier|sokf_invisible, "barrier_2m", "bo_barrier_2m", []),

	("exit_4m", sokf_type_barrier_leave|sokf_invisible, "barrier_4m", "bo_barrier_4m", []),

	("exit_8m", sokf_type_barrier_leave|sokf_invisible, "barrier_8m", "bo_barrier_8m", []),

	("exit_16m", sokf_type_barrier_leave|sokf_invisible, "barrier_16m", "bo_barrier_16m", []),

	("ai_limiter_2m", sokf_type_ai_limiter|sokf_invisible, "barrier_2m", "bo_barrier_2m", []),

	("ai_limiter_4m", sokf_type_ai_limiter|sokf_invisible, "barrier_4m", "bo_barrier_4m", []),

	("ai_limiter_8m", sokf_type_ai_limiter|sokf_invisible, "barrier_8m", "bo_barrier_8m", []),

	("ai_limiter_16m", sokf_type_ai_limiter|sokf_invisible, "barrier_16m", "bo_barrier_16m", []),

	("Shield", sokf_dynamic, "0", "boshield", []),

	("shelves", 0, "shelves", "boshelves", []),

	("table_tavern", 0, "table_tavern", "botable_tavern", []),

	("table_castle_a", 0, "table_castle_a", "bo_table_castle_a", []),

	("chair_castle_a", 0, "chair_castle_a", "bo_chair_castle_a", []),

	("pillow_a", 0, "pillow_a", "bo_pillow", []),

	("pillow_b", 0, "pillow_b", "bo_pillow", []),

	("pillow_c", 0, "pillow_c", "0", []),

	("interior_castle_g_square_keep_b", 0, "interior_castle_g_square_keep_b", "bo_interior_castle_g_square_keep_b", []),

	("carpet_with_pillows_a", 0, "carpet_with_pillows_a", "bo_carpet_with_pillows", []),

	("carpet_with_pillows_b", 0, "carpet_with_pillows_b", "bo_carpet_with_pillows", []),

	("table_round_a", 0, "table_round_a", "bo_table_round_a", []),

	("table_round_b", 0, "table_round_b", "bo_table_round_b", []),

	("fireplace_b", 0, "fireplace_b", "bo_fireplace_b", []),

	("fireplace_c", 0, "fireplace_c", "bo_fireplace_c", []),

	("sofa_a", 0, "sofa_a", "bo_sofa", []),

	("sofa_b", 0, "sofa_b", "bo_sofa", []),

	("ewer_a", 0, "ewer_a_new", "bo_ewer_a", []),

	("end_table_a", 0, "end_table_a", "bo_end_table_a", []),

	("fake_houses_steppe_a", 0, "fake_houses_steppe_a", "0", []),

	("fake_houses_steppe_b", 0, "fake_houses_steppe_b", "0", []),

	("fake_houses_steppe_c", 0, "fake_houses_steppe_c", "0", []),

	("boat_destroy", 0, "boat_destroy", "bo_boat_destroy", []),

	("destroy_house_a", 0, "destroy_house_a", "bo_destroy_house_a", []),

	("destroy_house_b", 0, "destroy_house_b", "bo_destroy_house_b", []),

	("destroy_house_c", 0, "destroy_house_c", "bo_destroy_house_c", []),

	("destroy_heap", 0, "destroy_heap", "bo_destroy_heap", []),

	("destroy_castle_a", 0, "destroy_castle_a", "bo_destroy_castle_a", []),

	("destroy_castle_b", 0, "destroy_castle_b", "bo_destroy_castle_b", []),

	("destroy_castle_c", 0, "destroy_castle_c", "bo_destroy_castle_c", []),

	("destroy_castle_c_desert", 0, "destroy_castle_c_desert", "bo_destroy_castle_c_desert", []),

	("destroy_castle_d", 0, "destroy_castle_d", "bo_destroy_castle_d", []),

	("destroy_windmill", 0, "destroy_windmill", "bo_destroy_windmill", []),

	("destroy_tree_a", 0, "destroy_tree_a", "bo_destroy_tree_a", []),

	("destroy_tree_b", 0, "destroy_tree_b", "bo_destroy_tree_b", []),

	("destroy_bridge_a", 0, "destroy_bridge_a", "bo_destroy_bridge_a", []),

	("destroy_bridge_b", 0, "destroy_bridge_b", "bo_destroy_bridge_b", []),

	("catapult", 0, "Catapult", "bo_Catapult", []),

	("catapult_destructible", sokf_show_hit_point_bar|sokf_destructible|sokf_moveable, "Catapult", "bo_Catapult", 
	[(ti_on_scene_prop_init,
		[
			(store_trigger_param_1, ":trigger_param_1"),
			(scene_prop_set_hit_points, ":trigger_param_1", 1600)
		]),

		(ti_on_scene_prop_destroy,
		[
			(play_sound, "snd_dummy_destroyed"),
			(try_begin),
				(this_or_next|multiplayer_is_server),
				(neg|game_in_multiplayer_mode),
				(store_trigger_param_1, ":trigger_param_1"),
				(prop_instance_get_position, 1, ":trigger_param_1"),
				(particle_system_burst, "psys_dummy_smoke_big", 1, 100),
				(particle_system_burst, "psys_dummy_straw_big", 1, 100),
				(position_move_z, 1, -500),
				(position_rotate_x, 1, 90),
				(prop_instance_animate_to_position, ":trigger_param_1", 1, 300),
				(try_begin),
					(eq, "$g_round_ended", 0),
					(scene_prop_get_team, ":scene_prop_team_trigger_param_1", ":trigger_param_1"),
					(try_begin),
						(eq, ":scene_prop_team_trigger_param_1", 0),
						(assign, ":value", -1),
					(else_try),
						(assign, ":value", 1),
					(try_end),
					(try_begin),
						(eq, "$g_number_of_targets_destroyed", 0),
						(store_mul, ":value_2", ":value", 1),
						(call_script, "script_show_multiplayer_message", 15, ":value_2"),
						(get_max_players, ":max_players"),
						(try_for_range, ":number", 1, ":max_players"),
							(player_is_active, ":number"),
							(multiplayer_send_2_int_to_player, ":number", 68, 15, ":value_2"),
						(try_end),
						(val_add, "$g_number_of_targets_destroyed", 1),
					(else_try),
						(store_mul, ":value_2", ":value", 9),
						(call_script, "script_show_multiplayer_message", 15, ":value_2"),
						(get_max_players, ":max_players"),
						(try_for_range, ":number", 1, ":max_players"),
							(player_is_active, ":number"),
							(multiplayer_send_2_int_to_player, ":number", 68, 15, ":value_2"),
						(try_end),
						(val_add, "$g_number_of_targets_destroyed", 1),
					(try_end),
				(try_end),
				(assign, ":var_7", 0),
				(get_max_players, ":max_players"),
				(try_for_range, ":number", 0, ":max_players"),
					(player_is_active, ":number"),
					(try_begin),
						(eq, "spr_catapult_destructible", "$g_destructible_target_1"),
						(player_get_slot, ":number_damage_given_to_target_1", ":number", slot_player_damage_given_to_target_1),
					(else_try),
						(player_get_slot, ":number_damage_given_to_target_1", ":number", slot_player_damage_given_to_target_2),
					(try_end),
					(val_add, ":var_7", ":number_damage_given_to_target_1"),
				(try_end),
				(assign, ":value_3", 0),
				(get_max_players, ":max_players"),
				(try_for_range, ":number", 0, ":max_players"),
					(player_is_active, ":number"),
					(val_add, ":value_3", 50),
				(try_end),
				(try_begin),
					(ge, ":value_3", 1500),
					(assign, ":value_3", 1500),
				(try_end),
				(val_mul, ":value_3", "$g_multiplayer_battle_earnings_multiplier"),
				(val_div, ":value_3", 100),
				(get_max_players, ":max_players"),
				(try_for_range, ":number", 0, ":max_players"),
					(player_is_active, ":number"),
					(try_begin),
						(eq, "spr_catapult_destructible", "$g_destructible_target_1"),
						(player_get_slot, ":number_damage_given_to_target_1", ":number", slot_player_damage_given_to_target_1),
					(else_try),
						(player_get_slot, ":number_damage_given_to_target_1", ":number", slot_player_damage_given_to_target_2),
					(try_end),
					(player_get_gold, ":gold_number", ":number"),
					(val_mul, ":number_damage_given_to_target_1", ":value_3"),
					(try_begin),
						(ge, ":var_7", ":number_damage_given_to_target_1"),
						(gt, ":number_damage_given_to_target_1", 0),
						(store_div, ":value_4", ":number_damage_given_to_target_1", ":var_7"),
					(else_try),
						(assign, ":value_4", 0),
					(try_end),
					(val_add, ":gold_number", ":value_4"),
					(player_set_gold, ":number", ":gold_number", 15000),
				(try_end),
			(try_end)
		]),

		(ti_on_scene_prop_hit,
		[
			(store_trigger_param_1, ":trigger_param_1"),
			(store_trigger_param_2, ":trigger_param_2"),
			(try_begin),
				(scene_prop_get_hit_points, ":scene_prop_hit_points_trigger_param_1", ":trigger_param_1"),
				(val_sub, ":scene_prop_hit_points_trigger_param_1", ":trigger_param_2"),
				(gt, ":scene_prop_hit_points_trigger_param_1", 0),
				(play_sound, "snd_dummy_hit"),
			(else_try),
				(neg|multiplayer_is_server),
				(play_sound, "snd_dummy_destroyed"),
			(try_end),
			(try_begin),
				(this_or_next|multiplayer_is_server),
				(neg|game_in_multiplayer_mode),
				(particle_system_burst, "psys_dummy_smoke", 1, 3),
				(particle_system_burst, "psys_dummy_straw", 1, 10),
				(set_fixed_point_multiplier, 1),
				(position_get_x, ":position_x_2", 2),
				(try_begin),
					(ge, ":position_x_2", 0),
					(agent_is_alive, ":position_x_2"),
					(agent_is_human, ":position_x_2"),
					(neg|agent_is_non_player, ":position_x_2"),
					(agent_get_player_id, ":player_id_position_x_2", ":position_x_2"),
					(ge, ":player_id_position_x_2", 0),
					(player_is_active, ":player_id_position_x_2"),
					(try_begin),
						(eq, "spr_catapult_destructible", "$g_destructible_target_1"),
						(player_get_slot, ":player_id_position_x_2_damage_given_to_target_1", ":player_id_position_x_2", slot_player_damage_given_to_target_1),
						(val_add, ":player_id_position_x_2_damage_given_to_target_1", ":trigger_param_2"),
						(player_set_slot, ":player_id_position_x_2", slot_player_damage_given_to_target_1, ":player_id_position_x_2_damage_given_to_target_1"),
					(else_try),
						(player_get_slot, ":player_id_position_x_2_damage_given_to_target_1", ":player_id_position_x_2", slot_player_damage_given_to_target_2),
						(val_add, ":player_id_position_x_2_damage_given_to_target_1", ":trigger_param_2"),
						(player_set_slot, ":player_id_position_x_2", slot_player_damage_given_to_target_2, ":player_id_position_x_2_damage_given_to_target_1"),
					(try_end),
				(try_end),
			(try_end)
		])
	]),

	("broom", 0, "broom", "0", []),

	("garlic", 0, "garlic", "0", []),

	("garlic_b", 0, "garlic_b", "0", []),

	("destroy_a", 0, "destroy_a", "0", []),

	("destroy_b", 0, "destroy_b", "0", []),

	("bridge_wooden", 0, "bridge_wooden", "bo_bridge_wooden", []),

	("bridge_wooden_snowy", 0, "bridge_wooden_snowy", "bo_bridge_wooden", []),

	("grave_a", 0, "grave_a", "bo_grave_a", []),

	("village_house_e", 0, "village_house_e", "bo_village_house_e", []),

	("village_house_f", 0, "village_house_f", "bo_village_house_f", []),

	("village_house_g", 0, "village_house_g", "bo_village_house_g", []),

	("village_house_h", 0, "village_house_h", "bo_village_house_h", []),

	("village_house_i", 0, "village_house_i", "bo_village_house_i", []),

	("village_house_j", 0, "village_house_j", "bo_village_house_j", []),

	("village_wall_a", 0, "village_wall_a", "bo_village_wall_a", []),

	("village_wall_b", 0, "village_wall_b", "bo_village_wall_b", []),

	("village_snowy_house_a", 0, "village_snowy_house_a", "bo_village_snowy_house_a", []),

	("village_snowy_house_b", 0, "village_snowy_house_b", "bo_village_snowy_house_b", []),

	("village_snowy_house_c", 0, "village_snowy_house_c", "bo_village_snowy_house_c", []),

	("village_snowy_house_d", 0, "village_snowy_house_d", "bo_village_snowy_house_d", []),

	("village_snowy_house_e", 0, "village_snowy_house_e", "bo_village_snowy_house_e", []),

	("village_snowy_house_f", 0, "village_snowy_house_f", "bo_village_snowy_house_f", []),

	("town_house_steppe_a", 0, "town_house_steppe_a", "bo_town_house_steppe_a", []),

	("town_house_steppe_b", 0, "town_house_steppe_b", "bo_town_house_steppe_b", []),

	("town_house_steppe_c", 0, "town_house_steppe_c", "bo_town_house_steppe_c", []),

	("town_house_steppe_d", 0, "town_house_steppe_d", "bo_town_house_steppe_d", []),

	("town_house_steppe_e", 0, "town_house_steppe_e", "bo_town_house_steppe_e", []),

	("town_house_steppe_f", 0, "town_house_steppe_f", "bo_town_house_steppe_f", []),

	("town_house_steppe_g", 0, "town_house_steppe_g", "bo_town_house_steppe_g", []),

	("town_house_steppe_h", 0, "town_house_steppe_h", "bo_town_house_steppe_h", []),

	("town_house_steppe_i", 0, "town_house_steppe_i", "bo_town_house_steppe_i", []),

	("carpet_a", 0, "carpet_a", "0", []),

	("carpet_b", 0, "carpet_b", "0", []),

	("carpet_c", 0, "carpet_c", "0", []),

	("carpet_d", 0, "carpet_d", "0", []),

	("carpet_e", 0, "carpet_e", "0", []),

	("carpet_f", 0, "carpet_f", "0", []),

	("awning_a", 0, "awning_a", "bo_awning", []),

	("awning_b", 0, "general_awning_b", "bo_awning", []),

	("awning_c", 0, "awning_c", "bo_awning", []),

	("awning_long", 0, "general_awning_long", "bo_awning_long", []),

	("awning_long_b", 0, "awning_long_b", "bo_awning_long", []),

	("awning_d", 0, "general_awning_d", "bo_awning_d", []),

	("ship", 0, "ship", "bo_ship", []),

	("ship_b", 0, "ship_b", "bo_ship_b", []),

	("ship_c", 0, "ship_c", "bo_ship_c", []),

	("ship_d", 0, "ship_d", "bo_ship_d", []),

	("snowy_barrel_a", 0, "winter_snowy_barrel_a", "bo_snowy_barrel_a", []),

	("snowy_fence", 0, "snowy_fence", "bo_snowy_fence", []),

	("snowy_wood_heap", 0, "snowy_wood_heap", "bo_snowy_wood_heap", []),

	("village_snowy_stable_a", 0, "village_snowy_stable_a", "bo_village_snowy_stable_a", []),

	("village_straw_house_a", 0, "village_straw_house_a", "bo_village_straw_house_a", []),

	("village_stable_a", 0, "village_stable_a", "bo_village_stable_a", []),

	("village_shed_a", 0, "village_shed_a", "bo_village_shed_a", []),

	("village_shed_b", 0, "village_shed_b", "bo_village_shed_b", []),

	("dungeon_door_cell_a", 0, "dungeon_door_cell_a", "bo_dungeon_door_cell_a", []),

	("dungeon_door_cell_b", 0, "dungeon_door_cell_b", "bo_dungeon_door_cell_b", []),

	("dungeon_door_entry_a", 0, "dungeon_door_entry_a", "bo_dungeon_door_entry_a", []),

	("dungeon_door_entry_b", 0, "dungeon_door_entry_b", "bo_dungeon_door_entry_a", []),

	("dungeon_door_entry_c", 0, "dungeon_door_entry_c", "bo_dungeon_door_entry_a", []),

	("dungeon_door_direction_a", 0, "dungeon_door_direction_a", "bo_dungeon_door_direction_a", []),

	("dungeon_door_direction_b", 0, "dungeon_door_direction_b", "bo_dungeon_door_direction_a", []),

	("dungeon_door_stairs_a", 0, "dungeon_door_stairs_a", "bo_dungeon_door_stairs_a", []),

	("dungeon_door_stairs_b", 0, "dungeon_door_stairs_b", "bo_dungeon_door_stairs_a", []),

	("dungeon_bed_a", 0, "dungeon_bed_a", "0", []),

	("dungeon_bed_b", 0, "dungeon_bed_b", "bo_dungeon_bed_b", []),

	("torture_tool_a", 0, "torture_tool_a", "bo_torture_tool_a", []),

	("torture_tool_b", 0, "torture_tool_b", "0", []),

	("torture_tool_c", 0, "torture_tool_c", "bo_torture_tool_c", []),

	("skeleton_head", 0, "skeleton_head_new", "0", []),

	("skeleton_bone", 0, "skeleton_bone_new", "0", []),

	("dungeon_stairs_a", sokf_type_ladder, "dungeon_stairs_a", "bo_dungeon_stairs_a", []),

	("dungeon_stairs_b", sokf_type_ladder, "dungeon_stairs_b", "bo_dungeon_stairs_a", []),

	("dungeon_torture_room_a", 0, "dungeon_torture_room_a", "bo_dungeon_torture_room_a", []),

	("dungeon_entry_a", 0, "dungeon_entry_a", "bo_dungeon_entry_a", []),

	("dungeon_entry_b", 0, "dungeon_entry_b", "bo_dungeon_entry_b", []),

	("dungeon_entry_c", 0, "dungeon_entry_c", "bo_dungeon_entry_c", []),

	("dungeon_cell_a", 0, "dungeon_cell_a", "bo_dungeon_cell_a", []),

	("dungeon_cell_b", 0, "dungeon_cell_b", "bo_dungeon_cell_b", []),

	("dungeon_cell_c", 0, "dungeon_cell_c", "bo_dungeon_cell_c", []),

	("dungeon_corridor_a", 0, "dungeon_corridor_a", "bo_dungeon_corridor_a", []),

	("dungeon_corridor_b", 0, "dungeon_corridor_b", "bo_dungeon_corridor_b", []),

	("dungeon_corridor_c", 0, "dungeon_corridor_c", "bo_dungeon_corridor_b", []),

	("dungeon_corridor_d", 0, "dungeon_corridor_d", "bo_dungeon_corridor_b", []),

	("dungeon_direction_a", 0, "dungeon_direction_a", "bo_dungeon_direction_a", []),

	("dungeon_direction_b", 0, "dungeon_direction_b", "bo_dungeon_direction_a", []),

	("dungeon_room_a", 0, "dungeon_room_a", "bo_dungeon_room_a", []),

	("dungeon_tower_stairs_a", sokf_type_ladder, "dungeon_tower_stairs_a", "bo_dungeon_tower_stairs_a", []),

	("dungeon_tower_cell_a", 0, "dungeon_tower_cell_a", "bo_dungeon_tower_cell_a", []),

	("tunnel_a", 0, "tunnel_a", "bo_tunnel_a", []),

	("tunnel_salt", 0, "tunnel_salt", "bo_tunnel_salt", []),

	("salt_a", 0, "salt_a", "bo_salt_a", []),

	("door_destructible", sokf_show_hit_point_bar|sokf_destructible|sokf_moveable|spr_use_time(2), "tutorial_door_a", "bo_tutorial_door_a", 
	[(ti_on_scene_prop_use,
		[
			(store_trigger_param_1, ":trigger_param_1"),
			(store_trigger_param_2, ":trigger_param_2"),
			(call_script, "script_use_item", ":trigger_param_2", ":trigger_param_1"),
			(get_max_players, ":max_players"),
			(try_for_range, ":number", 1, ":max_players"),
				(player_is_active, ":number"),
				(multiplayer_send_2_int_to_player, ":number", 76, ":trigger_param_2", ":trigger_param_1"),
			(try_end)
		]),

		(ti_on_scene_prop_init,
		[
			(store_trigger_param_1, ":trigger_param_1"),
			(scene_prop_set_hit_points, ":trigger_param_1", 2000)
		]),

		(ti_on_scene_prop_destroy,
		[
			(play_sound, "snd_dummy_destroyed"),
			(assign, ":var_1", 86),
			(try_begin),
				(this_or_next|multiplayer_is_server),
				(neg|game_in_multiplayer_mode),
				(store_trigger_param_1, ":trigger_param_1"),
				(store_trigger_param_2, ":trigger_param_2"),
				(set_fixed_point_multiplier, 100),
				(prop_instance_get_position, 1, ":trigger_param_1"),
				(try_begin),
					(ge, ":trigger_param_2", 0),
					(agent_get_position, 2, ":trigger_param_2"),
					(try_begin),
						(position_is_behind_position, 2, 1),
						(val_mul, ":var_1", -1),
					(try_end),
				(try_end),
				(init_position, 3),
				(try_begin),
					(ge, ":var_1", 0),
					(position_move_y, 3, -100),
				(else_try),
					(position_move_y, 3, 100),
				(try_end),
				(position_move_x, 3, -50),
				(position_transform_position_to_parent, 4, 1, 3),
				(position_move_z, 4, 100),
				(position_get_distance_to_ground_level, ":position_distance_to_ground_level_4", 4),
				(val_sub, ":position_distance_to_ground_level_4", 100),
				(assign, ":var_5", ":position_distance_to_ground_level_4"),
				(val_div, ":var_5", 3),
				(try_begin),
					(ge, ":var_1", 0),
					(val_add, ":var_1", ":var_5"),
				(else_try),
					(val_sub, ":var_1", ":var_5"),
				(try_end),
				(position_rotate_x, 1, ":var_1"),
				(prop_instance_animate_to_position, ":trigger_param_1", 1, 70),
			(try_end)
		]),

		(ti_on_scene_prop_hit,
		[
			(play_sound, "snd_dummy_hit"),
			(particle_system_burst, "psys_dummy_smoke", 1, 3),
			(particle_system_burst, "psys_dummy_straw", 1, 10)
		])
	]),

	("tutorial_door_a", sokf_moveable, "tutorial_door_a", "bo_tutorial_door_a", []),

	("tutorial_door_b", sokf_moveable, "tutorial_door_b", "bo_tutorial_door_b", []),

	("tutorial_flag_yellow", sokf_moveable|sokf_face_player, "tutorial_flag_yellow", "0", []),

	("tutorial_flag_red", sokf_moveable|sokf_face_player, "tutorial_flag_red", "0", []),

	("tutorial_flag_blue", sokf_moveable|sokf_face_player, "tutorial_flag_blue", "0", []),

	("interior_prison_a", 0, "interior_prison_a", "bo_interior_prison_a", []),

	("interior_prison_b", 0, "interior_prison_b", "bo_interior_prison_b", []),

	("interior_prison_cell_a", 0, "interior_prison_cell_a", "bo_interior_prison_cell_a", []),

	("interior_prison_d", 0, "interior_prison_d", "bo_interior_prison_d", []),

	("arena_archery_target_a", 0, "arena_archery_target_a", "bo_arena_archery_target_a", []),

	("archery_butt_a", 0, "archery_butt", "bo_archery_butt", 
	[(ti_on_scene_prop_hit,
		[
			(store_trigger_param_1, ":trigger_param_1"),
			(prop_instance_get_position, 2, ":trigger_param_1"),
			(get_player_agent_no, ":player_agent_no"),
			(agent_get_position, 3, ":player_agent_no"),
			(get_distance_between_positions, ":distance_between_positions_3_2", 3, 2),
			(position_transform_position_to_local, 4, 2, 1),
			(position_set_y, 4, 0),
			(position_set_x, 2, 0),
			(position_set_y, 2, 0),
			(position_set_z, 2, 0),
			(get_distance_between_positions, ":distance_between_positions_4_2", 4, 2),
			(assign, ":value", 43),
			(val_sub, ":value", ":distance_between_positions_4_2"),
			(val_mul, ":value", 1299),
			(val_div, ":value", 4300),
			(try_begin),
				(lt, ":value", 0),
				(assign, ":value", 0),
			(try_end),
			(val_div, ":distance_between_positions_3_2", 91),
			(assign, reg60, ":value"),
			(assign, reg61, ":distance_between_positions_3_2"),
			(display_message, "str_archery_target_hit")
		])
	]),

	("archery_target_with_hit_a", 0, "arena_archery_target_a", "bo_arena_archery_target_a", 
	[(ti_on_scene_prop_hit,
		[
			(set_fixed_point_multiplier, 100),
			(store_trigger_param_1, ":trigger_param_1"),
			(position_get_x, ":position_x_2", 2),
			(val_div, ":position_x_2", 100),
			(get_player_agent_no, ":player_agent_no"),
			(try_begin),
				(eq, ":player_agent_no", ":position_x_2"),
				(prop_instance_get_position, 2, ":trigger_param_1"),
				(agent_get_position, 3, ":player_agent_no"),
				(get_distance_between_positions, ":distance_between_positions_3_2", 3, 2),
				(position_transform_position_to_local, 4, 2, 1),
				(position_set_y, 4, 0),
				(position_set_x, 2, 0),
				(position_set_y, 2, 0),
				(position_set_z, 2, 0),
				(get_distance_between_positions, ":distance_between_positions_4_2", 4, 2),
				(assign, ":value", 43),
				(val_sub, ":value", ":distance_between_positions_4_2"),
				(val_mul, ":value", 1299),
				(val_div, ":value", 4300),
				(try_begin),
					(lt, ":value", 0),
					(assign, ":value", 0),
				(try_end),
				(assign, "$g_last_archery_point_earned", ":value"),
				(val_div, ":distance_between_positions_3_2", 91),
				(assign, reg60, ":value"),
				(assign, reg61, ":distance_between_positions_3_2"),
				(display_message, "str_archery_target_hit"),
				(eq, "$g_tutorial_training_ground_horseman_trainer_state", 6),
				(eq, "$g_tutorial_training_ground_horseman_trainer_completed_chapters", 2),
				(prop_instance_get_variation_id_2, ":prop_instance_variation_id_2_trigger_param_1", ":trigger_param_1"),
				(val_sub, ":prop_instance_variation_id_2_trigger_param_1", 1),
				(eq, "$g_tutorial_training_ground_current_score", ":prop_instance_variation_id_2_trigger_param_1"),
				(val_add, "$g_tutorial_training_ground_current_score", 1),
			(try_end)
		])
	]),

	("dummy_a", sokf_destructible|sokf_moveable, "arena_archery_target_b", "bo_arena_archery_target_b", 
	[(ti_on_scene_prop_destroy,
		[
			(store_trigger_param_1, ":trigger_param_1"),
			(prop_instance_get_starting_position, 1, ":trigger_param_1"),
			(get_player_agent_no, ":player_agent_no"),
			(agent_get_position, 2, ":player_agent_no"),
			(assign, ":var_3", 80),
			(try_begin),
				(position_is_behind_position, 2, 1),
				(val_mul, ":var_3", -1),
			(try_end),
			(position_rotate_x, 1, ":var_3"),
			(prop_instance_animate_to_position, ":trigger_param_1", 1, 70),
			(val_add, "$tutorial_num_total_dummies_destroyed", 1),
			(play_sound, "snd_dummy_destroyed")
		]),

		(ti_on_scene_prop_hit,
		[
			(store_trigger_param_1, ":trigger_param_1"),
			(store_trigger_param_2, ":trigger_param_2"),
			(assign, reg60, ":trigger_param_2"),
			(val_div, ":trigger_param_2", 8),
			(prop_instance_get_position, 2, ":trigger_param_1"),
			(get_player_agent_no, ":player_agent_no"),
			(agent_get_position, 3, ":player_agent_no"),
			(try_begin),
				(position_is_behind_position, 3, 2),
				(val_mul, ":trigger_param_2", -1),
			(try_end),
			(position_rotate_x, 2, ":trigger_param_2"),
			(display_message, "str_delivered_damage"),
			(prop_instance_animate_to_position, ":trigger_param_1", 2, 30),
			(play_sound, "snd_dummy_hit"),
			(particle_system_burst, "psys_dummy_smoke", 1, 3),
			(particle_system_burst, "psys_dummy_straw", 1, 10)
		])
	]),

	("band_a", 0, "band_a", "0", []),

	("arena_sign", 0, "arena_arms", "0", []),

	("castle_h_battlement_a", 0, "castle_h_battlement_a", "bo_castle_h_battlement_a", []),

	("castle_h_battlement_b", 0, "castle_h_battlement_b", "bo_castle_h_battlement_b", []),

	("castle_h_battlement_c", 0, "castle_h_battlement_c", "bo_castle_h_battlement_c", []),

	("castle_h_battlement_a2", 0, "castle_h_battlement_a2", "bo_castle_h_battlement_a2", []),

	("castle_h_battlement_b2", 0, "castle_h_battlement_b2", "bo_castle_h_battlement_b2", []),

	("castle_h_corner_a", 0, "castle_h_corner_a", "bo_castle_h_corner_a", []),

	("castle_h_corner_c", 0, "castle_h_corner_c", "bo_castle_h_corner_c", []),

	("castle_h_stairs_a", sokf_type_ladder, "castle_h_stairs_a", "bo_castle_h_stairs_a", []),

	("castle_h_stairs_b", 0, "castle_h_stairs_b", "bo_castle_h_stairs_b", []),

	("castle_h_gatehouse_a", 0, "castle_h_gatehouse_a", "bo_castle_h_gatehouse_a", []),

	("castle_h_keep_a", 0, "castle_h_keep_a", "bo_castle_h_keep_a", []),

	("castle_h_keep_b", 0, "castle_h_keep_b", "bo_castle_h_keep_b", []),

	("castle_h_house_a", 0, "castle_h_house_a", "bo_castle_h_house_a", []),

	("castle_h_house_b", 0, "castle_h_house_b", "bo_castle_h_house_b", []),

	("castle_h_house_c", 0, "castle_h_house_c", "bo_castle_h_house_b", []),

	("castle_h_battlement_barrier", 0, "castle_h_battlement_barrier", "bo_castle_h_battlement_barrier", []),

	("full_keep_b", sokf_type_ladder, "full_keep_b", "bo_full_keep_b", []),

	("castle_f_keep_a", 0, "castle_f_keep_a", "bo_castle_f_keep_a", []),

	("castle_f_battlement_a", 0, "castle_f_battlement_a", "bo_castle_f_battlement_a", []),

	("castle_f_battlement_a_destroyed", 0, "castle_f_battlement_a_destroyed", "bo_castle_f_battlement_a_destroyed", []),

	("castle_f_battlement_b", 0, "castle_f_battlement_b", "bo_castle_f_battlement_b", []),

	("castle_f_battlement_c", 0, "castle_f_battlement_c", "bo_castle_f_battlement_c", []),

	("castle_f_battlement_d", 0, "castle_f_battlement_d", "bo_castle_f_battlement_d", []),

	("castle_f_battlement_e", 0, "castle_f_battlement_e", "bo_castle_f_battlement_e", []),

	("castle_f_sally_port_elevation", 0, "castle_f_sally_port_elevation", "bo_castle_f_sally_port_elevation", []),

	("castle_f_battlement_corner_a", 0, "castle_f_battlement_corner_a", "bo_castle_f_battlement_corner_a", []),

	("castle_f_battlement_corner_b", 0, "castle_f_battlement_corner_b", "bo_castle_f_battlement_corner_b", []),

	("castle_f_battlement_corner_c", 0, "castle_f_battlement_corner_c", "bo_castle_f_battlement_corner_c", []),

	("castle_f_door_a", sokf_show_hit_point_bar|sokf_destructible|sokf_moveable, "castle_f_door_a", "bo_castle_f_door_a", 
	[(ti_on_scene_prop_use,
		[
			(store_trigger_param_1, ":trigger_param_1"),
			(store_trigger_param_2, ":trigger_param_2"),
			(agent_get_position, 1, ":trigger_param_1"),
			(prop_instance_get_starting_position, 2, ":trigger_param_2"),
			(scene_prop_get_slot, ":scene_prop_slot_trigger_param_2_scene_prop_open_or_close_slot", ":trigger_param_2", slot_scene_prop_open_or_close_slot),
			(try_begin),
				(ge, ":trigger_param_1", 0),
				(agent_get_team, ":team_trigger_param_1", ":trigger_param_1"),
				(this_or_next|eq, ":team_trigger_param_1", 0),
				(eq, ":scene_prop_slot_trigger_param_2_scene_prop_open_or_close_slot", 1),
				(try_begin),
					(call_script, "script_use_item", ":trigger_param_2", ":trigger_param_1"),
					(get_max_players, ":max_players"),
					(try_for_range, ":number", 1, ":max_players"),
						(player_is_active, ":number"),
						(multiplayer_send_2_int_to_player, ":number", 76, ":trigger_param_2", ":trigger_param_1"),
					(try_end),
				(try_end),
			(try_end)
		]),

		(ti_on_scene_prop_init,
		[
			(store_trigger_param_1, ":trigger_param_1"),
			(scene_prop_set_hit_points, ":trigger_param_1", 1000)
		]),

		(ti_on_scene_prop_destroy,
		[
			(play_sound, "snd_dummy_destroyed"),
			(assign, ":var_1", 86),
			(try_begin),
				(this_or_next|multiplayer_is_server),
				(neg|game_in_multiplayer_mode),
				(store_trigger_param_1, ":trigger_param_1"),
				(store_trigger_param_2, ":trigger_param_2"),
				(set_fixed_point_multiplier, 100),
				(prop_instance_get_position, 1, ":trigger_param_1"),
				(try_begin),
					(ge, ":trigger_param_2", 0),
					(agent_get_position, 2, ":trigger_param_2"),
					(try_begin),
						(position_is_behind_position, 2, 1),
						(val_mul, ":var_1", -1),
					(try_end),
				(try_end),
				(init_position, 3),
				(try_begin),
					(ge, ":var_1", 0),
					(position_move_y, 3, -100),
				(else_try),
					(position_move_y, 3, 100),
				(try_end),
				(position_move_x, 3, -50),
				(position_transform_position_to_parent, 4, 1, 3),
				(position_move_z, 4, 100),
				(position_get_distance_to_ground_level, ":position_distance_to_ground_level_4", 4),
				(val_sub, ":position_distance_to_ground_level_4", 100),
				(assign, ":var_5", ":position_distance_to_ground_level_4"),
				(val_div, ":var_5", 3),
				(try_begin),
					(ge, ":var_1", 0),
					(val_add, ":var_1", ":var_5"),
				(else_try),
					(val_sub, ":var_1", ":var_5"),
				(try_end),
				(position_rotate_x, 1, ":var_1"),
				(prop_instance_animate_to_position, ":trigger_param_1", 1, 70),
			(try_end)
		]),

		(ti_on_scene_prop_hit,
		[
			(store_trigger_param_1, ":trigger_param_1"),
			(store_trigger_param_2, ":trigger_param_2"),
			(try_begin),
				(scene_prop_get_hit_points, ":scene_prop_hit_points_trigger_param_1", ":trigger_param_1"),
				(val_sub, ":scene_prop_hit_points_trigger_param_1", ":trigger_param_2"),
				(gt, ":scene_prop_hit_points_trigger_param_1", 0),
				(play_sound, "snd_dummy_hit"),
			(else_try),
				(neg|multiplayer_is_server),
				(play_sound, "snd_dummy_destroyed"),
			(try_end),
			(try_begin),
				(this_or_next|multiplayer_is_server),
				(neg|game_in_multiplayer_mode),
				(particle_system_burst, "psys_dummy_smoke", 1, 3),
				(particle_system_burst, "psys_dummy_straw", 1, 10),
			(try_end)
		])
	]),

	("castle_f_doors_top_a", 0, "castle_f_doors_top_a", "bo_castle_f_doors_top_a", []),

	("castle_f_sally_door_a", sokf_show_hit_point_bar|sokf_destructible|sokf_moveable, "castle_f_sally_door_a", "bo_castle_f_sally_door_a", 
	[(ti_on_scene_prop_use,
		[
			(store_trigger_param_1, ":trigger_param_1"),
			(store_trigger_param_2, ":trigger_param_2"),
			(agent_get_position, 1, ":trigger_param_1"),
			(prop_instance_get_starting_position, 2, ":trigger_param_2"),
			(scene_prop_get_slot, ":scene_prop_slot_trigger_param_2_scene_prop_open_or_close_slot", ":trigger_param_2", slot_scene_prop_open_or_close_slot),
			(try_begin),
				(this_or_next|position_is_behind_position, 1, 2),
				(eq, ":scene_prop_slot_trigger_param_2_scene_prop_open_or_close_slot", 1),
				(try_begin),
					(call_script, "script_use_item", ":trigger_param_2", ":trigger_param_1"),
					(get_max_players, ":max_players"),
					(try_for_range, ":number", 1, ":max_players"),
						(player_is_active, ":number"),
						(multiplayer_send_2_int_to_player, ":number", 76, ":trigger_param_2", ":trigger_param_1"),
					(try_end),
				(try_end),
			(try_end)
		]),

		(ti_on_scene_prop_init,
		[
			(store_trigger_param_1, ":trigger_param_1"),
			(scene_prop_set_hit_points, ":trigger_param_1", 1000)
		]),

		(ti_on_scene_prop_destroy,
		[
			(play_sound, "snd_dummy_destroyed"),
			(assign, ":var_1", 86),
			(try_begin),
				(this_or_next|multiplayer_is_server),
				(neg|game_in_multiplayer_mode),
				(store_trigger_param_1, ":trigger_param_1"),
				(store_trigger_param_2, ":trigger_param_2"),
				(set_fixed_point_multiplier, 100),
				(prop_instance_get_position, 1, ":trigger_param_1"),
				(try_begin),
					(ge, ":trigger_param_2", 0),
					(agent_get_position, 2, ":trigger_param_2"),
					(try_begin),
						(position_is_behind_position, 2, 1),
						(val_mul, ":var_1", -1),
					(try_end),
				(try_end),
				(init_position, 3),
				(try_begin),
					(ge, ":var_1", 0),
					(position_move_y, 3, -100),
				(else_try),
					(position_move_y, 3, 100),
				(try_end),
				(position_move_x, 3, -50),
				(position_transform_position_to_parent, 4, 1, 3),
				(position_move_z, 4, 100),
				(position_get_distance_to_ground_level, ":position_distance_to_ground_level_4", 4),
				(val_sub, ":position_distance_to_ground_level_4", 100),
				(assign, ":var_5", ":position_distance_to_ground_level_4"),
				(val_div, ":var_5", 3),
				(try_begin),
					(ge, ":var_1", 0),
					(val_add, ":var_1", ":var_5"),
				(else_try),
					(val_sub, ":var_1", ":var_5"),
				(try_end),
				(position_rotate_x, 1, ":var_1"),
				(prop_instance_animate_to_position, ":trigger_param_1", 1, 70),
			(try_end)
		]),

		(ti_on_scene_prop_hit,
		[
			(store_trigger_param_1, ":trigger_param_1"),
			(store_trigger_param_2, ":trigger_param_2"),
			(try_begin),
				(scene_prop_get_hit_points, ":scene_prop_hit_points_trigger_param_1", ":trigger_param_1"),
				(val_sub, ":scene_prop_hit_points_trigger_param_1", ":trigger_param_2"),
				(gt, ":scene_prop_hit_points_trigger_param_1", 0),
				(play_sound, "snd_dummy_hit"),
			(else_try),
				(neg|multiplayer_is_server),
				(play_sound, "snd_dummy_destroyed"),
			(try_end),
			(try_begin),
				(this_or_next|multiplayer_is_server),
				(neg|game_in_multiplayer_mode),
				(particle_system_burst, "psys_dummy_smoke", 1, 3),
				(particle_system_burst, "psys_dummy_straw", 1, 10),
			(try_end)
		])
	]),

	("castle_f_stairs_a", sokf_type_ladder, "castle_f_stairs_a", "bo_castle_f_stairs_a", []),

	("castle_f_tower_a", sokf_type_ladder, "castle_f_tower_a", "bo_castle_f_tower_a", []),

	("castle_f_wall_stairs_a", sokf_type_ladder, "castle_f_wall_stairs_a", "bo_castle_f_wall_stairs_a", []),

	("castle_f_wall_stairs_b", sokf_type_ladder, "castle_f_wall_stairs_b", "bo_castle_f_wall_stairs_b", []),

	("castle_f_wall_way_a", 0, "castle_f_wall_way_a", "bo_castle_f_wall_way_a", []),

	("castle_f_wall_way_b", 0, "castle_f_wall_way_b", "bo_castle_f_wall_way_b", []),

	("castle_f_gatehouse_a", 0, "castle_f_gatehouse_a", "bo_castle_f_gatehouse_a", []),

	("castle_g_battlement_a", 0, "castle_g_battlement_a", "bo_castle_g_battlement_a", []),

	("castle_g_battlement_a1", 0, "castle_g_battlement_a1", "bo_castle_g_battlement_a1", []),

	("castle_g_battlement_c", 0, "castle_g_battlement_c", "bo_castle_g_battlement_c", []),

	("castle_g_corner_a", 0, "castle_g_corner_a", "bo_castle_g_corner_a", []),

	("castle_g_corner_c", 0, "castle_g_corner_c", "bo_castle_g_corner_c", []),

	("castle_g_tower_a", sokf_type_ladder, "castle_g_tower_a", "bo_castle_g_tower_a", []),

	("castle_g_gate_house", 0, "castle_g_gate_house", "bo_castle_g_gate_house", []),

	("castle_g_gate_house_door_a", 0, "castle_g_gate_house_door_a", "bo_castle_g_gate_house_door_a", []),

	("castle_g_gate_house_door_b", 0, "castle_g_gate_house_door_b", "bo_castle_g_gate_house_door_b", []),

	("castle_g_square_keep_a", 0, "castle_g_square_keep_a", "bo_castle_g_square_keep_a", []),

	("castle_i_battlement_a", 0, "castle_i_battlement_a", "bo_castle_i_battlement_a", []),

	("castle_i_battlement_a1", 0, "castle_i_battlement_a1", "bo_castle_i_battlement_a1", []),

	("castle_i_battlement_c", 0, "castle_i_battlement_c", "bo_castle_i_battlement_c", []),

	("castle_i_corner_a", 0, "castle_i_corner_a", "bo_castle_i_corner_a", []),

	("castle_i_corner_c", 0, "castle_i_corner_c", "bo_castle_i_corner_c", []),

	("castle_i_tower_a", sokf_type_ladder, "castle_i_tower_a", "bo_castle_i_tower_a", []),

	("castle_i_gate_house", 0, "castle_i_gate_house", "bo_castle_i_gate_house", []),

	("castle_i_gate_house_door_a", 0, "castle_i_gate_house_door_a", "bo_castle_i_gate_house_door_a", []),

	("castle_i_gate_house_door_b", 0, "castle_i_gate_house_door_b", "bo_castle_i_gate_house_door_b", []),

	("castle_i_square_keep_a", 0, "castle_i_square_keep_a", "bo_castle_i_square_keep_a", []),

	("mosque_a", 0, "mosque_a", "bo_mosque_a", []),

	("stone_minaret_a", 0, "stone_minaret_a", "bo_stone_minaret_a", []),

	("stone_house_a", 0, "stone_house_a", "bo_stone_house_a", []),

	("stone_house_b", 0, "stone_house_b", "bo_stone_house_b", []),

	("stone_house_c", 0, "stone_house_c", "bo_stone_house_c", []),

	("stone_house_d", 0, "stone_house_d", "bo_stone_house_d", []),

	("stone_house_e", 0, "stone_house_e", "bo_stone_house_e", []),

	("stone_house_f", 0, "stone_house_f", "bo_stone_house_f", []),

	("banner_pole", sokf_moveable, "banner_pole", "bo_banner_pole", []),

	("custom_banner_01", 0, "custom_banner_01", "0", 
	[(ti_on_scene_prop_init,
		[
			(party_get_slot, ":g_encountered_party_town_lord", "$g_encountered_party", slot_town_lord),
			(try_begin),
				(ge, ":g_encountered_party_town_lord", 0),
				(cur_scene_prop_set_tableau_material, "tableau_custom_banner_default", ":g_encountered_party_town_lord"),
			(try_end)
		])
	]),

	("custom_banner_02", 0, "custom_banner_02", "0", 
	[(ti_on_scene_prop_init,
		[
			(party_get_slot, ":g_encountered_party_town_lord", "$g_encountered_party", slot_town_lord),
			(try_begin),
				(ge, ":g_encountered_party_town_lord", 0),
				(cur_scene_prop_set_tableau_material, "tableau_custom_banner_default", ":g_encountered_party_town_lord"),
			(try_end)
		])
	]),

	("banner_a", 0, "banner_a01", "0", []),

	("banner_b", 0, "banner_a02", "0", []),

	("banner_c", 0, "banner_a03", "0", []),

	("banner_d", 0, "banner_a04", "0", []),

	("banner_e", 0, "banner_a05", "0", []),

	("banner_f", 0, "banner_a06", "0", []),

	("banner_g", 0, "banner_a07", "0", []),

	("banner_h", 0, "banner_a08", "0", []),

	("banner_i", 0, "banner_a09", "0", []),

	("banner_j", 0, "banner_a10", "0", []),

	("banner_k", 0, "banner_a11", "0", []),

	("banner_l", 0, "banner_a12", "0", []),

	("banner_m", 0, "banner_a13", "0", []),

	("banner_n", 0, "banner_a14", "0", []),

	("banner_o", 0, "banner_a15", "0", []),

	("banner_p", 0, "banner_a16", "0", []),

	("banner_q", 0, "banner_a17", "0", []),

	("banner_r", 0, "banner_a18", "0", []),

	("banner_s", 0, "banner_a19", "0", []),

	("banner_t", 0, "banner_a20", "0", []),

	("banner_u", 0, "banner_a21", "0", []),

	("banner_ba", 0, "banner_b01", "0", []),

	("banner_bb", 0, "banner_b02", "0", []),

	("banner_bc", 0, "banner_b03", "0", []),

	("banner_bd", 0, "banner_b04", "0", []),

	("banner_be", 0, "banner_b05", "0", []),

	("banner_bf", 0, "banner_b06", "0", []),

	("banner_bg", 0, "banner_b07", "0", []),

	("banner_bh", 0, "banner_b08", "0", []),

	("banner_bi", 0, "banner_b09", "0", []),

	("banner_bj", 0, "banner_b10", "0", []),

	("banner_bk", 0, "banner_b11", "0", []),

	("banner_bl", 0, "banner_b12", "0", []),

	("banner_bm", 0, "banner_b13", "0", []),

	("banner_bn", 0, "banner_b14", "0", []),

	("banner_bo", 0, "banner_b15", "0", []),

	("banner_bp", 0, "banner_b16", "0", []),

	("banner_bq", 0, "banner_b17", "0", []),

	("banner_br", 0, "banner_b18", "0", []),

	("banner_bs", 0, "banner_b19", "0", []),

	("banner_bt", 0, "banner_b20", "0", []),

	("banner_bu", 0, "banner_b21", "0", []),

	("banner_ca", 0, "banner_c01", "0", []),

	("banner_cb", 0, "banner_c02", "0", []),

	("banner_cc", 0, "banner_c03", "0", []),

	("banner_cd", 0, "banner_c04", "0", []),

	("banner_ce", 0, "banner_c05", "0", []),

	("banner_cf", 0, "banner_c06", "0", []),

	("banner_cg", 0, "banner_c07", "0", []),

	("banner_ch", 0, "banner_c08", "0", []),

	("banner_ci", 0, "banner_c09", "0", []),

	("banner_cj", 0, "banner_c10", "0", []),

	("banner_ck", 0, "banner_c11", "0", []),

	("banner_cl", 0, "banner_c12", "0", []),

	("banner_cm", 0, "banner_c13", "0", []),

	("banner_cn", 0, "banner_c14", "0", []),

	("banner_co", 0, "banner_c15", "0", []),

	("banner_cp", 0, "banner_c16", "0", []),

	("banner_cq", 0, "banner_c17", "0", []),

	("banner_cr", 0, "banner_c18", "0", []),

	("banner_cs", 0, "banner_c19", "0", []),

	("banner_ct", 0, "banner_c20", "0", []),

	("banner_cu", 0, "banner_c21", "0", []),

	("banner_da", 0, "banner_d01", "0", []),

	("banner_db", 0, "banner_d02", "0", []),

	("banner_dc", 0, "banner_d03", "0", []),

	("banner_dd", 0, "banner_d04", "0", []),

	("banner_de", 0, "banner_d05", "0", []),

	("banner_df", 0, "banner_d06", "0", []),

	("banner_dg", 0, "banner_d07", "0", []),

	("banner_dh", 0, "banner_d08", "0", []),

	("banner_di", 0, "banner_d09", "0", []),

	("banner_dj", 0, "banner_d10", "0", []),

	("banner_dk", 0, "banner_d11", "0", []),

	("banner_dl", 0, "banner_d12", "0", []),

	("banner_dm", 0, "banner_d13", "0", []),

	("banner_dn", 0, "banner_d14", "0", []),

	("banner_do", 0, "banner_d15", "0", []),

	("banner_dp", 0, "banner_d16", "0", []),

	("banner_dq", 0, "banner_d17", "0", []),

	("banner_dr", 0, "banner_d18", "0", []),

	("banner_ds", 0, "banner_d19", "0", []),

	("banner_dt", 0, "banner_d20", "0", []),

	("banner_du", 0, "banner_d21", "0", []),

	("banner_ea", 0, "banner_e01", "0", []),

	("banner_eb", 0, "banner_e02", "0", []),

	("banner_ec", 0, "banner_e03", "0", []),

	("banner_ed", 0, "banner_e04", "0", []),

	("banner_ee", 0, "banner_e05", "0", []),

	("banner_ef", 0, "banner_e06", "0", []),

	("banner_eg", 0, "banner_e07", "0", []),

	("banner_eh", 0, "banner_e08", "0", []),

	("banner_ei", 0, "banner_e09", "0", []),

	("banner_ej", 0, "banner_e10", "0", []),

	("banner_ek", 0, "banner_e11", "0", []),

	("banner_el", 0, "banner_e12", "0", []),

	("banner_em", 0, "banner_e13", "0", []),

	("banner_en", 0, "banner_e14", "0", []),

	("banner_eo", 0, "banner_e15", "0", []),

	("banner_ep", 0, "banner_e16", "0", []),

	("banner_eq", 0, "banner_e17", "0", []),

	("banner_er", 0, "banner_e18", "0", []),

	("banner_es", 0, "banner_e19", "0", []),

	("banner_et", 0, "banner_e20", "0", []),

	("banner_eu", 0, "banner_e21", "0", []),

	("banner_f01", 0, "banner_f01", "0", []),

	("banner_f02", 0, "banner_f02", "0", []),

	("banner_f03", 0, "banner_f03", "0", []),

	("banner_f04", 0, "banner_f04", "0", []),

	("banner_f05", 0, "banner_f05", "0", []),

	("banner_f06", 0, "banner_f06", "0", []),

	("banner_f07", 0, "banner_f07", "0", []),

	("banner_f08", 0, "banner_f08", "0", []),

	("banner_f09", 0, "banner_f09", "0", []),

	("banner_f10", 0, "banner_f10", "0", []),

	("banner_f11", 0, "banner_f11", "0", []),

	("banner_f12", 0, "banner_f12", "0", []),

	("banner_f13", 0, "banner_f13", "0", []),

	("banner_f14", 0, "banner_f14", "0", []),

	("banner_f15", 0, "banner_f15", "0", []),

	("banner_f16", 0, "banner_f16", "0", []),

	("banner_f17", 0, "banner_f17", "0", []),

	("banner_f18", 0, "banner_f18", "0", []),

	("banner_f19", 0, "banner_f19", "0", []),

	("banner_f20", 0, "banner_f20", "0", []),

	("banner_f21", 0, "banner_f21", "0", []),

	("banner_g01", 0, "banner_g01", "0", []),

	("banner_g02", 0, "banner_g02", "0", []),

	("banner_g03", 0, "banner_g03", "0", []),

	("banner_g04", 0, "banner_g04", "0", []),

	("banner_g05", 0, "banner_g05", "0", []),

	("banner_g06", 0, "banner_g06", "0", []),

	("banner_g07", 0, "banner_g07", "0", []),

	("banner_g08", 0, "banner_g08", "0", []),

	("banner_g09", 0, "banner_g09", "0", []),

	("banner_g10", 0, "banner_g10", "0", []),

	("banner_g11", 0, "banner_g11", "0", []),

	("banner_g12", 0, "banner_g12", "0", []),

	("banner_g13", 0, "banner_g13", "0", []),

	("banner_g14", 0, "banner_g14", "0", []),

	("banner_g15", 0, "banner_g15", "0", []),

	("banner_g16", 0, "banner_g16", "0", []),

	("banner_g17", 0, "banner_g17", "0", []),

	("banner_g18", 0, "banner_g18", "0", []),

	("banner_g19", 0, "banner_g19", "0", []),

	("banner_g20", 0, "banner_g20", "0", []),

	("banner_g21", 0, "banner_g21", "0", []),

	("banner_h01", 0, "banner_h01", "0", []),

	("banner_h02", 0, "banner_h02", "0", []),

	("banner_h03", 0, "banner_h03", "0", []),

	("banner_h04", 0, "banner_h04", "0", []),

	("banner_h05", 0, "banner_h05", "0", []),

	("banner_h06", 0, "banner_h06", "0", []),

	("banner_h07", 0, "banner_h07", "0", []),

	("banner_h08", 0, "banner_h08", "0", []),

	("banner_h09", 0, "banner_h09", "0", []),

	("banner_h10", 0, "banner_h10", "0", []),

	("banner_h11", 0, "banner_h11", "0", []),

	("banner_h12", 0, "banner_h12", "0", []),

	("banner_h13", 0, "banner_h13", "0", []),

	("banner_h14", 0, "banner_h14", "0", []),

	("banner_h15", 0, "banner_h15", "0", []),

	("banner_h16", 0, "banner_h16", "0", []),

	("banner_h17", 0, "banner_h17", "0", []),

	("banner_h18", 0, "banner_h18", "0", []),

	("banner_h19", 0, "banner_h19", "0", []),

	("banner_h20", 0, "banner_h20", "0", []),

	("banner_h21", 0, "banner_h21", "0", []),

	("banner_i01", 0, "banner_i01", "0", []),

	("banner_i02", 0, "banner_i02", "0", []),

	("banner_i03", 0, "banner_i03", "0", []),

	("banner_i04", 0, "banner_i04", "0", []),

	("banner_i05", 0, "banner_i05", "0", []),

	("banner_i06", 0, "banner_i06", "0", []),

	("banner_i07", 0, "banner_i07", "0", []),

	("banner_i08", 0, "banner_i08", "0", []),

	("banner_i09", 0, "banner_i09", "0", []),

	("banner_i10", 0, "banner_i10", "0", []),

	("banner_i11", 0, "banner_i11", "0", []),

	("banner_i12", 0, "banner_i12", "0", []),

	("banner_i13", 0, "banner_i13", "0", []),

	("banner_i14", 0, "banner_i14", "0", []),

	("banner_i15", 0, "banner_i15", "0", []),

	("banner_i16", 0, "banner_i16", "0", []),

	("banner_i17", 0, "banner_i17", "0", []),

	("banner_i18", 0, "banner_i18", "0", []),

	("banner_i19", 0, "banner_i19", "0", []),

	("banner_i20", 0, "banner_i20", "0", []),

	("banner_i21", 0, "banner_i21", "0", []),

	("banner_j01", 0, "banner_j01", "0", []),

	("banner_j02", 0, "banner_j02", "0", []),

	("banner_j03", 0, "banner_j03", "0", []),

	("banner_j04", 0, "banner_j04", "0", []),

	("banner_j05", 0, "banner_j05", "0", []),

	("banner_j06", 0, "banner_j06", "0", []),

	("banner_j07", 0, "banner_j07", "0", []),

	("banner_j08", 0, "banner_j08", "0", []),

	("banner_j09", 0, "banner_j09", "0", []),

	("banner_j10", 0, "banner_j10", "0", []),

	("banner_j11", 0, "banner_j11", "0", []),

	("banner_j12", 0, "banner_j12", "0", []),

	("banner_j13", 0, "banner_j13", "0", []),

	("banner_j14", 0, "banner_j14", "0", []),

	("banner_j15", 0, "banner_j15", "0", []),

	("banner_j16", 0, "banner_j16", "0", []),

	("banner_j17", 0, "banner_j17", "0", []),

	("banner_j18", 0, "banner_j18", "0", []),

	("banner_j19", 0, "banner_j19", "0", []),

	("banner_j20", 0, "banner_j20", "0", []),

	("banner_j21", 0, "banner_j21", "0", []),

	("banner_k01", 0, "banner_k01", "0", []),

	("banner_k02", 0, "banner_k02", "0", []),

	("banner_k03", 0, "banner_k03", "0", []),

	("banner_k04", 0, "banner_k04", "0", []),

	("banner_k05", 0, "banner_k05", "0", []),

	("banner_k06", 0, "banner_k06", "0", []),

	("banner_k07", 0, "banner_k07", "0", []),

	("banner_k08", 0, "banner_k08", "0", []),

	("banner_k09", 0, "banner_k09", "0", []),

	("banner_k10", 0, "banner_k10", "0", []),

	("banner_k11", 0, "banner_k11", "0", []),

	("banner_k12", 0, "banner_k12", "0", []),

	("banner_k13", 0, "banner_k13", "0", []),

	("banner_k14", 0, "banner_k14", "0", []),

	("banner_k15", 0, "banner_k15", "0", []),

	("banner_k16", 0, "banner_k16", "0", []),

	("banner_k17", 0, "banner_k17", "0", []),

	("banner_k18", 0, "banner_k18", "0", []),

	("banner_k19", 0, "banner_k19", "0", []),

	("banner_k20", 0, "banner_k20", "0", []),

	("banner_k21", 0, "banner_k21", "0", []),

	("banner_l01", 0, "banner_l01", "0", []),

	("banner_l02", 0, "banner_l02", "0", []),

	("banner_l03", 0, "banner_l03", "0", []),

	("banner_l04", 0, "banner_l04", "0", []),

	("banner_l05", 0, "banner_l05", "0", []),

	("banner_l06", 0, "banner_l06", "0", []),

	("banner_l07", 0, "banner_l07", "0", []),

	("banner_l08", 0, "banner_l08", "0", []),

	("banner_l09", 0, "banner_l09", "0", []),

	("banner_l10", 0, "banner_l10", "0", []),

	("banner_l11", 0, "banner_l11", "0", []),

	("banner_l12", 0, "banner_l12", "0", []),

	("banner_l13", 0, "banner_l13", "0", []),

	("banner_l14", 0, "banner_l14", "0", []),

	("banner_l15", 0, "banner_l15", "0", []),

	("banner_l16", 0, "banner_l16", "0", []),

	("banner_l17", 0, "banner_l17", "0", []),

	("banner_l18", 0, "banner_l18", "0", []),

	("banner_l19", 0, "banner_l19", "0", []),

	("banner_l20", 0, "banner_l20", "0", []),

	("banner_l21", 0, "banner_l21", "0", []),

	("banner_lords_swadia01", 0, "banner_lords_swadia01", "0", []),

	("banner_lords_swadia02", 0, "banner_lords_swadia02", "0", []),

	("banner_lords_swadia03", 0, "banner_lords_swadia03", "0", []),

	("banner_lords_swadia04", 0, "banner_lords_swadia04", "0", []),

	("banner_lords_swadia05", 0, "banner_lords_swadia05", "0", []),

	("banner_lords_swadia06", 0, "banner_lords_swadia06", "0", []),

	("banner_lords_swadia07", 0, "banner_lords_swadia07", "0", []),

	("banner_lords_swadia08", 0, "banner_lords_swadia08", "0", []),

	("banner_lords_swadia09", 0, "banner_lords_swadia09", "0", []),

	("banner_lords_swadia10", 0, "banner_lords_swadia10", "0", []),

	("banner_lords_swadia11", 0, "banner_lords_swadia11", "0", []),

	("banner_lords_swadia12", 0, "banner_lords_swadia12", "0", []),

	("banner_lords_swadia13", 0, "banner_lords_swadia13", "0", []),

	("banner_lords_swadia14", 0, "banner_lords_swadia14", "0", []),

	("banner_lords_swadia15", 0, "banner_lords_swadia15", "0", []),

	("banner_lords_swadia16", 0, "banner_lords_swadia16", "0", []),

	("banner_lords_swadia17", 0, "banner_lords_swadia17", "0", []),

	("banner_lords_swadia18", 0, "banner_lords_swadia18", "0", []),

	("banner_lords_swadia19", 0, "banner_lords_swadia19", "0", []),

	("banner_lords_swadia20", 0, "banner_lords_swadia20", "0", []),

	("banner_lords_swadia21", 0, "banner_lords_swadia21", "0", []),

	("banner_lords_vaegir01", 0, "banner_lords_vaegir01", "0", []),

	("banner_lords_vaegir02", 0, "banner_lords_vaegir02", "0", []),

	("banner_lords_vaegir03", 0, "banner_lords_vaegir03", "0", []),

	("banner_lords_vaegir04", 0, "banner_lords_vaegir04", "0", []),

	("banner_lords_vaegir05", 0, "banner_lords_vaegir05", "0", []),

	("banner_lords_vaegir06", 0, "banner_lords_vaegir06", "0", []),

	("banner_lords_vaegir07", 0, "banner_lords_vaegir07", "0", []),

	("banner_lords_vaegir08", 0, "banner_lords_vaegir08", "0", []),

	("banner_lords_vaegir09", 0, "banner_lords_vaegir09", "0", []),

	("banner_lords_vaegir10", 0, "banner_lords_vaegir10", "0", []),

	("banner_lords_vaegir11", 0, "banner_lords_vaegir11", "0", []),

	("banner_lords_vaegir12", 0, "banner_lords_vaegir12", "0", []),

	("banner_lords_vaegir13", 0, "banner_lords_vaegir13", "0", []),

	("banner_lords_vaegir14", 0, "banner_lords_vaegir14", "0", []),

	("banner_lords_vaegir15", 0, "banner_lords_vaegir15", "0", []),

	("banner_lords_vaegir16", 0, "banner_lords_vaegir16", "0", []),

	("banner_lords_vaegir17", 0, "banner_lords_vaegir17", "0", []),

	("banner_lords_vaegir18", 0, "banner_lords_vaegir18", "0", []),

	("banner_lords_vaegir19", 0, "banner_lords_vaegir19", "0", []),

	("banner_lords_vaegir20", 0, "banner_lords_vaegir20", "0", []),

	("banner_lords_vaegir21", 0, "banner_lords_vaegir21", "0", []),

	("banner_lords_khergit01", 0, "banner_lords_khergit01", "0", []),

	("banner_lords_khergit02", 0, "banner_lords_khergit02", "0", []),

	("banner_lords_khergit03", 0, "banner_lords_khergit03", "0", []),

	("banner_lords_khergit04", 0, "banner_lords_khergit04", "0", []),

	("banner_lords_khergit05", 0, "banner_lords_khergit05", "0", []),

	("banner_lords_khergit06", 0, "banner_lords_khergit06", "0", []),

	("banner_lords_khergit07", 0, "banner_lords_khergit07", "0", []),

	("banner_lords_khergit08", 0, "banner_lords_khergit08", "0", []),

	("banner_lords_khergit09", 0, "banner_lords_khergit09", "0", []),

	("banner_lords_khergit10", 0, "banner_lords_khergit10", "0", []),

	("banner_lords_khergit11", 0, "banner_lords_khergit11", "0", []),

	("banner_lords_khergit12", 0, "banner_lords_khergit12", "0", []),

	("banner_lords_khergit13", 0, "banner_lords_khergit13", "0", []),

	("banner_lords_khergit14", 0, "banner_lords_khergit14", "0", []),

	("banner_lords_khergit15", 0, "banner_lords_khergit15", "0", []),

	("banner_lords_khergit16", 0, "banner_lords_khergit16", "0", []),

	("banner_lords_khergit17", 0, "banner_lords_khergit17", "0", []),

	("banner_lords_khergit18", 0, "banner_lords_khergit18", "0", []),

	("banner_lords_khergit19", 0, "banner_lords_khergit19", "0", []),

	("banner_lords_khergit20", 0, "banner_lords_khergit20", "0", []),

	("banner_lords_khergit21", 0, "banner_lords_khergit21", "0", []),

	("banner_lords_nord01", 0, "banner_lords_nord01", "0", []),

	("banner_lords_nord02", 0, "banner_lords_nord02", "0", []),

	("banner_lords_nord03", 0, "banner_lords_nord03", "0", []),

	("banner_lords_nord04", 0, "banner_lords_nord04", "0", []),

	("banner_lords_nord05", 0, "banner_lords_nord05", "0", []),

	("banner_lords_nord06", 0, "banner_lords_nord06", "0", []),

	("banner_lords_nord07", 0, "banner_lords_nord07", "0", []),

	("banner_lords_nord08", 0, "banner_lords_nord08", "0", []),

	("banner_lords_nord09", 0, "banner_lords_nord09", "0", []),

	("banner_lords_nord10", 0, "banner_lords_nord10", "0", []),

	("banner_lords_nord11", 0, "banner_lords_nord11", "0", []),

	("banner_lords_nord12", 0, "banner_lords_nord12", "0", []),

	("banner_lords_nord13", 0, "banner_lords_nord13", "0", []),

	("banner_lords_nord14", 0, "banner_lords_nord14", "0", []),

	("banner_lords_nord15", 0, "banner_lords_nord15", "0", []),

	("banner_lords_nord16", 0, "banner_lords_nord16", "0", []),

	("banner_lords_nord17", 0, "banner_lords_nord17", "0", []),

	("banner_lords_nord18", 0, "banner_lords_nord18", "0", []),

	("banner_lords_nord19", 0, "banner_lords_nord19", "0", []),

	("banner_lords_nord20", 0, "banner_lords_nord20", "0", []),

	("banner_lords_nord21", 0, "banner_lords_nord21", "0", []),

	("banner_lords_rhodok01", 0, "banner_lords_rhodok01", "0", []),

	("banner_lords_rhodok02", 0, "banner_lords_rhodok02", "0", []),

	("banner_lords_rhodok03", 0, "banner_lords_rhodok03", "0", []),

	("banner_lords_rhodok04", 0, "banner_lords_rhodok04", "0", []),

	("banner_lords_rhodok05", 0, "banner_lords_rhodok05", "0", []),

	("banner_lords_rhodok06", 0, "banner_lords_rhodok06", "0", []),

	("banner_lords_rhodok07", 0, "banner_lords_rhodok07", "0", []),

	("banner_lords_rhodok08", 0, "banner_lords_rhodok08", "0", []),

	("banner_lords_rhodok09", 0, "banner_lords_rhodok09", "0", []),

	("banner_lords_rhodok10", 0, "banner_lords_rhodok10", "0", []),

	("banner_lords_rhodok11", 0, "banner_lords_rhodok11", "0", []),

	("banner_lords_rhodok12", 0, "banner_lords_rhodok12", "0", []),

	("banner_lords_rhodok13", 0, "banner_lords_rhodok13", "0", []),

	("banner_lords_rhodok14", 0, "banner_lords_rhodok14", "0", []),

	("banner_lords_rhodok15", 0, "banner_lords_rhodok15", "0", []),

	("banner_lords_rhodok16", 0, "banner_lords_rhodok16", "0", []),

	("banner_lords_rhodok17", 0, "banner_lords_rhodok17", "0", []),

	("banner_lords_rhodok18", 0, "banner_lords_rhodok18", "0", []),

	("banner_lords_rhodok19", 0, "banner_lords_rhodok19", "0", []),

	("banner_lords_rhodok20", 0, "banner_lords_rhodok20", "0", []),

	("banner_lords_rhodok21", 0, "banner_lords_rhodok21", "0", []),

	("banner_lords_sarranid01", 0, "banner_lords_sarranid01", "0", []),

	("banner_lords_sarranid02", 0, "banner_lords_sarranid02", "0", []),

	("banner_lords_sarranid03", 0, "banner_lords_sarranid03", "0", []),

	("banner_lords_sarranid04", 0, "banner_lords_sarranid04", "0", []),

	("banner_lords_sarranid05", 0, "banner_lords_sarranid05", "0", []),

	("banner_lords_sarranid06", 0, "banner_lords_sarranid06", "0", []),

	("banner_lords_sarranid07", 0, "banner_lords_sarranid07", "0", []),

	("banner_lords_sarranid08", 0, "banner_lords_sarranid08", "0", []),

	("banner_lords_sarranid09", 0, "banner_lords_sarranid09", "0", []),

	("banner_lords_sarranid10", 0, "banner_lords_sarranid10", "0", []),

	("banner_lords_sarranid11", 0, "banner_lords_sarranid11", "0", []),

	("banner_lords_sarranid12", 0, "banner_lords_sarranid12", "0", []),

	("banner_lords_sarranid13", 0, "banner_lords_sarranid13", "0", []),

	("banner_lords_sarranid14", 0, "banner_lords_sarranid14", "0", []),

	("banner_lords_sarranid15", 0, "banner_lords_sarranid15", "0", []),

	("banner_lords_sarranid16", 0, "banner_lords_sarranid16", "0", []),

	("banner_lords_sarranid17", 0, "banner_lords_sarranid17", "0", []),

	("banner_lords_sarranid18", 0, "banner_lords_sarranid18", "0", []),

	("banner_lords_sarranid19", 0, "banner_lords_sarranid19", "0", []),

	("banner_lords_sarranid20", 0, "banner_lords_sarranid20", "0", []),

	("banner_lords_sarranid21", 0, "banner_lords_sarranid21", "0", []),

	("banner_companions01", 0, "banner_companions01", "0", []),

	("banner_companions02", 0, "banner_companions02", "0", []),

	("banner_companions03", 0, "banner_companions03", "0", []),

	("banner_companions04", 0, "banner_companions04", "0", []),

	("banner_companions05", 0, "banner_companions05", "0", []),

	("banner_companions06", 0, "banner_companions06", "0", []),

	("banner_companions07", 0, "banner_companions07", "0", []),

	("banner_companions08", 0, "banner_companions08", "0", []),

	("banner_companions09", 0, "banner_companions09", "0", []),

	("banner_companions10", 0, "banner_companions10", "0", []),

	("banner_companions11", 0, "banner_companions11", "0", []),

	("banner_companions12", 0, "banner_companions12", "0", []),

	("banner_companions13", 0, "banner_companions13", "0", []),

	("banner_companions14", 0, "banner_companions14", "0", []),

	("banner_companions15", 0, "banner_companions15", "0", []),

	("banner_companions16", 0, "banner_companions16", "0", []),

	("banner_companions17", 0, "banner_companions17", "0", []),

	("banner_companions18", 0, "banner_companions18", "0", []),

	("banner_companions19", 0, "banner_companions19", "0", []),

	("banner_companions20", 0, "banner_companions20", "0", []),

	("banner_companions21", 0, "banner_companions21", "0", []),

	("banner_companions22", 0, "banner_companions22", "0", []),

	("banner_bandits01", 0, "banner_bandits01", "0", []),

	("banner_bandits02", 0, "banner_bandits02", "0", []),

	("banner_bandits03", 0, "banner_bandits03", "0", []),

	("banner_bandits04", 0, "banner_bandits04", "0", []),

	("banner_bandits05", 0, "banner_bandits05", "0", []),

	("banner_bandits06", 0, "banner_bandits06", "0", []),

	("banner_bandits07", 0, "banner_bandits07", "0", []),

	("banner_kingdom_a", 0, "banner_kingdom_a", "0", []),

	("banner_kingdom_b", 0, "banner_kingdom_b", "0", []),

	("banner_kingdom_c", 0, "banner_kingdom_c", "0", []),

	("banner_kingdom_d", 0, "banner_kingdom_d", "0", []),

	("banner_kingdom_e", 0, "banner_kingdom_e", "0", []),

	("banner_kingdom_f", 0, "banner_kingdom_f", "0", []),

	("banner_kingdom_g", 0, "banner_kingdom_g", "0", []),

	("banner_kingdom_h", 0, "banner_kingdom_h", "0", []),

	("banner_kingdom_i", 0, "banner_kingdom_i", "0", []),

	("banner_kingdom_j", 0, "banner_kingdom_j", "0", []),

	("banner_kingdom_k", 0, "banner_kingdom_k", "0", []),

	("banner_kingdom_l", 0, "banner_kingdom_l", "0", []),

	("banner_kingdom_m", 0, "banner_kingdom_m", "0", []),

	("banner_kingdom_n", 0, "banner_kingdom_n", "0", []),

	("tavern_chair_a", 0, "tavern_chair_a", "bo_tavern_chair_a", []),

	("tavern_chair_b", 0, "tavern_chair_b", "bo_tavern_chair_b", []),

	("tavern_table_a", 0, "tavern_table_a", "bo_tavern_table_a", []),

	("tavern_table_b", 0, "tavern_table_b", "bo_tavern_table_b", []),

	("fireplace_a", 0, "fireplace_a", "bo_fireplace_a", []),

	("barrel", 0, "general_barrel_new", "bobarrel", []),

	("bench_tavern", 0, "bench_tavern", "bobench_tavern", []),

	("bench_tavern_b", 0, "bench_tavern_b", "bo_bench_tavern_b", []),

	("bowl_wood", 0, "bowl_wood", "0", []),

	("chandelier_table", 0, "chandelier_table_new", "0", []),

	("chandelier_tavern", 0, "chandelier_tavern_new", "0", []),

	("chest_gothic", 0, "chest_gothic", "bochest_gothic", []),

	("chest_b", 0, "chest_b_new", "bo_chest_b", []),

	("chest_c", 0, "chest_c_new", "bo_chest_c", []),

	("counter_tavern", 0, "counter_tavern", "bocounter_tavern", []),

	("cup", 0, "cup", "0", []),

	("dish_metal", 0, "dish_metal_new", "0", []),

	("gothic_chair", 0, "gothic_chair_new", "bogothic_chair", []),

	("gothic_stool", 0, "gothic_stool", "bogothic_stool", []),

	("grate", 0, "grate", "bograte", []),

	("jug", 0, "jug_new", "0", []),

	("potlamp", 0, "potlamp_new", "0", []),

	("weapon_rack", 0, "weapon_rack", "boweapon_rack", []),

	("weapon_rack_big", 0, "weapon_rack_big", "boweapon_rack_big", []),

	("tavern_barrel", 0, "barrel_new", "bobarrel", []),

	("tavern_barrel_b", 0, "tavern_barrel_b_new", "bo_tavern_barrel_b", []),

	("merchant_sign", 0, "merchant_sign", "bo_tavern_sign", []),

	("tavern_sign", 0, "tavern_sign", "bo_tavern_sign", []),

	("sack", 0, "sack_new", "0", []),

	("skull_a", 0, "skull_a", "0", []),

	("skull_b", 0, "skull_b", "0", []),

	("skull_c", 0, "skull_c", "0", []),

	("skull_d", 0, "skull_d", "0", []),

	("skeleton_cow", 0, "skeleton_cow_new", "0", []),

	("cupboard_a", 0, "cupboard_a", "bo_cupboard_a", []),

	("box_a", 0, "box_a_new", "bo_box_a", []),

	("bucket_a", 0, "bucket_a_new", "bo_bucket_a", []),

	("cloth_a", 0, "cloth_a", "0", []),

	("cloth_b", 0, "cloth_b", "0", []),

	("mat_a", 0, "mat_a", "0", []),

	("mat_b", 0, "mat_b", "0", []),

	("mat_c", 0, "rushes_1", "0", []),

	("mat_d", 0, "rushes_2", "0", []),

	("mat_e", 0, "new_rug_3", "0", []),

	("mat_f", 0, "new_rug_4", "0", []),

	("mat_g", 0, "new_rug_5", "0", []),

	("mat_h", 0, "new_rug_1", "0", []),

	("mat_i", 0, "new_rug_2", "0", []),

	("wood_a", 0, "wood_a", "bo_wood_a", []),

	("wood_b", 0, "wood_b", "bo_wood_b", []),

	("wood_heap", 0, "wood_heap_a", "bo_wood_heap_a", []),

	("wood_heap_b", 0, "wood_heap_b", "bo_wood_heap_b", []),

	("water_well_a", 0, "water_well_a", "bo_water_well_a", []),

	("net_a", 0, "net_a", "bo_net_a", []),

	("net_b", 0, "net_b", "0", []),

	("meat_hook", 0, "meat_hook", "0", []),

	("cooking_pole", 0, "cooking_pole", "0", []),

	("bowl_a", 0, "bowl_a_new", "0", []),

	("bucket_b", 0, "bucket_b_new", "0", []),

	("washtub_a", 0, "washtub_a_new", "bo_washtub_a", []),

	("washtub_b", 0, "washtub_b_new", "bo_washtub_b", []),

	("table_trunk_a", 0, "table_trunk_a", "bo_table_trunk_a", []),

	("chair_trunk_a", 0, "chair_trunk_a", "bo_chair_trunk_a", []),

	("chair_trunk_b", 0, "chair_trunk_b", "bo_chair_trunk_b", []),

	("chair_trunk_c", 0, "chair_trunk_c", "bo_chair_trunk_c", []),

	("table_trestle_long", 0, "table_trestle_long", "bo_table_trestle_long", []),

	("table_trestle_small", 0, "table_trestle_small", "bo_table_trestle_small", []),

	("chair_trestle", 0, "chair_trestle", "bo_chair_trestle", []),

	("wheel", 0, "wheel", "bo_wheel", []),

	("ladder", sokf_type_ladder, "ladder", "boladder", []),

	("cart", 0, "cart", "bo_cart", []),

	("village_stand", 0, "general_village_stand", "bo_general_village_stand", []),

	("wooden_stand", 0, "general_wooden_stand", "bo_general_wooden_stand", []),

	("table_small", 0, "table_small", "bo_table_small", []),

	("table_small_b", 0, "table_small_b", "bo_table_small_b", []),

	("small_timber_frame_house_a", 0, "small_timber_frame_house_a", "bo_small_timber_frame_house_a", []),

	("timber_frame_house_b", 0, "tf_house_b", "bo_tf_house_b", []),

	("timber_frame_house_c", 0, "tf_house_c", "bo_tf_house_c", []),

	("timber_frame_extension_a", 0, "timber_frame_extension_a", "bo_timber_frame_extension_a", []),

	("timber_frame_extension_b", 0, "timber_frame_extension_b", "bo_timber_frame_extension_b", []),

	("stone_stairs_a", sokf_type_ladder, "stone_stairs_a", "bo_stone_stairs_a", []),

	("stone_stairs_b", sokf_type_ladder, "stone_stairs_b", "bo_stone_stairs_b", []),

	("railing_a", 0, "railing_a", "bo_railing_a", []),

	("side_building_a", 0, "side_building_a", "bo_side_building_a", []),

	("battlement_a", 0, "battlement_a", "bo_battlement_a", []),

	("battlement_a_destroyed", 0, "battlement_a_destroyed", "bo_battlement_a_destroyed", []),

	("round_tower_a", 0, "round_tower_a", "bo_round_tower_a", []),

	("small_round_tower_a", 0, "small_round_tower_a", "bo_small_round_tower_a", []),

	("small_round_tower_roof_a", 0, "small_round_tower_roof_a", "bo_small_round_tower_roof_a", []),

	("square_keep_a", 0, "square_keep_a", "bo_square_keep_a", []),

	("square_tower_roof_a", 0, "square_tower_roof_a", "0", []),

	("gate_house_a", 0, "gate_house_a", "bo_gate_house_a", []),

	("gate_house_b", 0, "gate_house_b", "bo_gate_house_b", []),

	("small_wall_a", 0, "small_wall_a", "bo_small_wall_a", []),

	("small_wall_b", 0, "small_wall_b", "bo_small_wall_b", []),

	("small_wall_c", 0, "small_wall_c", "bo_small_wall_c", []),

	("small_wall_c_destroy", 0, "small_wall_c_destroy", "bo_small_wall_c_destroy", []),

	("small_wall_d", 0, "small_wall_d", "bo_small_wall_d", []),

	("small_wall_e", 0, "small_wall_e", "bo_small_wall_d", []),

	("small_wall_f", 0, "small_wall_f", "bo_small_wall_f", []),

	("small_wall_f2", 0, "small_wall_f2", "bo_small_wall_f2", []),

	("town_house_a", 0, "town_house_a", "bo_town_house_a", []),

	("town_house_b", 0, "town_house_b", "bo_town_house_b", []),

	("town_house_c", 0, "town_house_c", "bo_town_house_c", []),

	("town_house_d", 0, "town_house_d", "bo_town_house_d", []),

	("town_house_e", 0, "town_house_e", "bo_town_house_e", []),

	("town_house_f", 0, "town_house_f", "bo_town_house_f", []),

	("town_house_g", 0, "town_house_g", "bo_town_house_g", []),

	("town_house_h", 0, "town_house_h", "bo_town_house_h", []),

	("town_house_i", 0, "town_house_i", "bo_town_house_i", []),

	("town_house_j", 0, "town_house_j", "bo_town_house_j", []),

	("town_house_l", 0, "town_house_l", "bo_town_house_l", []),

	("town_house_m", 0, "town_house_m", "bo_town_house_m", []),

	("town_house_n", 0, "town_house_n", "bo_town_house_n", []),

	("town_house_o", 0, "town_house_o", "bo_town_house_o", []),

	("town_house_p", 0, "town_house_p", "bo_town_house_p", []),

	("town_house_q", 0, "town_house_q", "bo_town_house_q", []),

	("passage_house_a", 0, "passage_house_a", "bo_passage_house_a", []),

	("passage_house_b", 0, "passage_house_b", "bo_passage_house_b", []),

	("passage_house_c", 0, "passage_house_c", "bo_passage_house_c", []),

	("passage_house_d", 0, "passage_house_d", "bo_passage_house_d", []),

	("passage_house_c_door", 0, "passage_house_c_door", "bo_passage_house_c_door", []),

	("house_extension_a", 0, "house_extension_a", "bo_house_extension_a", []),

	("house_extension_b", 0, "house_extension_b", "bo_house_extension_b", []),

	("house_extension_c", 0, "house_extension_c", "bo_house_extension_a", []),

	("house_extension_d", 0, "house_extension_d", "bo_house_extension_d", []),

	("house_extension_e", 0, "house_extension_e", "bo_house_extension_e", []),

	("house_extension_f", 0, "house_extension_f", "bo_house_extension_f", []),

	("house_extension_f2", 0, "house_extension_f2", "bo_house_extension_f", []),

	("house_extension_g", 0, "house_extension_g", "bo_house_extension_g", []),

	("house_extension_g2", 0, "house_extension_g2", "bo_house_extension_g", []),

	("house_extension_h", 0, "house_extension_h", "bo_house_extension_h", []),

	("house_extension_i", 0, "house_extension_i", "bo_house_extension_i", []),

	("house_roof_door", 0, "house_roof_door", "bo_house_roof_door", []),

	("door_extension_a", 0, "door_extension_a", "bo_door_extension_a", []),

	("stairs_arch_a", sokf_type_ladder, "stairs_arch_a", "bo_stairs_arch_a", []),

	("town_house_r", 0, "town_house_r", "bo_town_house_r", []),

	("town_house_s", 0, "town_house_s", "bo_town_house_s", []),

	("town_house_t", 0, "town_house_t", "bo_town_house_t", []),

	("town_house_u", 0, "town_house_u", "bo_town_house_u", []),

	("town_house_v", 0, "town_house_v", "bo_town_house_v", []),

	("town_house_w", 0, "town_house_w", "bo_town_house_w", []),

	("town_house_y", 0, "town_house_y", "bo_town_house_y", []),

	("town_house_z", 0, "town_house_z", "bo_town_house_z", []),

	("town_house_za", 0, "town_house_za", "bo_town_house_za", []),

	("windmill", 0, "windmill", "bo_windmill", []),

	("windmill_fan_turning", sokf_moveable, "windmill_fan_turning", "bo_windmill_fan_turning", []),

	("windmill_fan", 0, "windmill_fan", "bo_windmill_fan", []),

	("fake_house_a", 0, "fake_house_a", "bo_fake_house_a", []),

	("fake_house_b", 0, "fake_house_b", "bo_fake_house_b", []),

	("fake_house_c", 0, "fake_house_c", "bo_fake_house_c", []),

	("fake_house_d", 0, "fake_house_d", "bo_fake_house_d", []),

	("fake_house_e", 0, "fake_house_e", "bo_fake_house_e", []),

	("fake_house_f", 0, "fake_house_f", "bo_fake_house_f", []),

	("fake_house_snowy_a", 0, "fake_house_snowy_a", "bo_fake_house_a", []),

	("fake_house_snowy_b", 0, "fake_house_snowy_b", "bo_fake_house_b", []),

	("fake_house_snowy_c", 0, "fake_house_snowy_c", "bo_fake_house_c", []),

	("fake_house_snowy_d", 0, "fake_house_snowy_d", "bo_fake_house_d", []),

	("fake_house_far_a", 0, "fake_house_far_a", "0", []),

	("fake_house_far_b", 0, "fake_house_far_b", "0", []),

	("fake_house_far_c", 0, "fake_house_far_c", "0", []),

	("fake_house_far_d", 0, "fake_house_far_d", "0", []),

	("fake_house_far_e", 0, "fake_house_far_e", "0", []),

	("fake_house_far_f", 0, "fake_house_far_f", "0", []),

	("fake_house_far_snowycrude_a", 0, "fake_house_far_snowy_a", "0", []),

	("fake_house_far_snowy_b", 0, "fake_house_far_snowy_b", "0", []),

	("fake_house_far_snowy_c", 0, "fake_house_far_snowy_c", "0", []),

	("fake_house_far_snowy_d", 0, "fake_house_far_snowy_d", "0", []),

	("earth_wall_a", 0, "earth_wall_a", "bo_earth_wall_a", []),

	("earth_wall_a2", 0, "earth_wall_a2", "bo_earth_wall_a2", []),

	("earth_wall_b", 0, "earth_wall_b", "bo_earth_wall_b", []),

	("earth_wall_b2", 0, "earth_wall_b2", "bo_earth_wall_b2", []),

	("earth_stairs_a", sokf_type_ladder, "earth_stairs_a", "bo_earth_stairs_a", []),

	("earth_stairs_b", sokf_type_ladder, "earth_stairs_b", "bo_earth_stairs_b", []),

	("earth_tower_small_a", 0, "earth_tower_small_a", "bo_earth_tower_small_a", []),

	("earth_gate_house_a", 0, "earth_gate_house_a", "bo_earth_gate_house_a", []),

	("earth_gate_a", 0, "earth_gate_a", "bo_earth_gate_a", []),

	("earth_square_keep_a", 0, "earth_square_keep_a", "bo_earth_square_keep_a", []),

	("earth_house_a", 0, "earth_house_a", "bo_earth_house_a", []),

	("earth_house_b", 0, "earth_house_b", "bo_earth_house_b", []),

	("earth_house_c", 0, "earth_house_c", "bo_earth_house_c", []),

	("earth_house_d", 0, "earth_house_d", "bo_earth_house_d", []),

	("village_steppe_a", 0, "village_steppe_a", "bo_village_steppe_a", []),

	("village_steppe_b", 0, "village_steppe_b", "bo_village_steppe_b", []),

	("village_steppe_c", 0, "village_steppe_c", "bo_village_steppe_c", []),

	("village_steppe_d", 0, "village_steppe_d", "bo_village_steppe_d", []),

	("village_steppe_e", 0, "village_steppe_e", "bo_village_steppe_e", []),

	("village_steppe_f", 0, "village_steppe_f", "bo_village_steppe_f", []),

	("town_house_aa", 0, "town_house_aa", "bo_town_house_aa", []),

	("snowy_house_a", 0, "snowy_house_a", "bo_snowy_house_a", []),

	("snowy_house_b", 0, "snowy_house_b", "bo_snowy_house_b", []),

	("snowy_house_c", 0, "snowy_house_c", "bo_snowy_house_c", []),

	("snowy_house_d", 0, "snowy_house_d", "bo_snowy_house_d", []),

	("snowy_house_e", 0, "snowy_house_e", "bo_snowy_house_e", []),

	("snowy_house_f", 0, "snowy_house_f", "bo_snowy_house_f", []),

	("snowy_house_g", 0, "winter_snowy_house_g", "bo_snowy_house_g", []),

	("snowy_house_h", 0, "snowy_house_h", "bo_snowy_house_h", []),

	("snowy_house_i", 0, "winter_snowy_house_i", "bo_snowy_house_i", []),

	("snowy_wall_a", 0, "winter_snowy_wall_a", "bo_snowy_wall_a", []),

	("snowy_stand", 0, "snowy_stand", "bo_snowy_stand", []),

	("snowy_heap_a", 0, "snowy_heap_a", "bo_snowy_heap_a", []),

	("snowy_trunks_a", 0, "snowy_trunks_a", "bo_snowy_trunks_a", []),

	("snowy_castle_tower_a", 0, "snowy_castle_tower_a", "bo_snowy_castle_tower_a", []),

	("snowy_castle_battlement_a", 0, "snowy_castle_battlement_a", "bo_snowy_castle_battlement_a", []),

	("snowy_castle_battlement_a_destroyed", 0, "snowy_castle_battlement_a_destroyed", "bo_snowy_castle_battlement_a_destroyed", []),

	("snowy_castle_battlement_b", 0, "snowy_castle_battlement_b", "bo_snowy_castle_battlement_b", []),

	("snowy_castle_battlement_corner_a", 0, "snowy_castle_battlement_corner_a", "bo_snowy_castle_battlement_corner_a", []),

	("snowy_castle_battlement_corner_b", 0, "snowy_castle_battlement_corner_b", "bo_snowy_castle_battlement_corner_b", []),

	("snowy_castle_battlement_corner_c", 0, "snowy_castle_battlement_corner_c", "bo_snowy_castle_battlement_corner_c", []),

	("snowy_castle_battlement_stairs_a", 0, "snowy_castle_battlement_stairs_a", "bo_snowy_castle_battlement_stairs_a", []),

	("snowy_castle_battlement_stairs_b", 0, "snowy_castle_battlement_stairs_b", "bo_snowy_castle_battlement_stairs_b", []),

	("snowy_castle_gate_house_a", 0, "snowy_castle_gate_house_a", "bo_snowy_castle_gate_house_a", []),

	("snowy_castle_round_tower_a", 0, "snowy_castle_round_tower_a", "bo_snowy_castle_round_tower_a", []),

	("snowy_castle_square_keep_a", 0, "snowy_castle_square_keep_a", "bo_snowy_castle_square_keep_a", []),

	("snowy_castle_stairs_a", sokf_type_ladder, "snowy_castle_stairs_a", "bo_snowy_castle_stairs_a", []),

	("square_keep_b", 0, "square_keep_b", "bo_square_keep_b", []),

	("square_keep_c", 0, "square_keep_c", "bo_square_keep_c", []),

	("square_keep_d", 0, "square_keep_d", "bo_square_keep_d", []),

	("square_keep_e", 0, "square_keep_e", "bo_square_keep_e", []),

	("square_keep_f", 0, "square_keep_f", "bo_square_keep_f", []),

	("square_extension_a", 0, "square_extension_a", "bo_square_extension_a", []),

	("square_stairs_a", 0, "square_stairs_a", "bo_square_stairs_a", []),

	("castle_courtyard_house_a", 0, "castle_courtyard_house_a", "bo_castle_courtyard_house_a", []),

	("castle_courtyard_house_b", 0, "castle_courtyard_house_b", "bo_castle_courtyard_house_b", []),

	("castle_courtyard_house_c", 0, "castle_courtyard_house_c", "bo_castle_courtyard_house_c", []),

	("castle_courtyard_a", 0, "castle_courtyard_a", "bo_castle_courtyard_a", []),

	("gatehouse_b", 0, "gatehouse_b", "bo_gatehouse_b", []),

	("castle_gaillard", 0, "castle_gaillard", "bo_castle_gaillard", []),

	("castle_e_battlement_a", 0, "castle_e_battlement_a", "bo_castle_e_battlement_a", []),

	("castle_e_battlement_c", 0, "castle_e_battlement_c", "bo_castle_e_battlement_c", []),

	("castle_e_battlement_a_destroyed", 0, "castle_e_battlement_a_destroyed", "bo_castle_e_battlement_a_destroyed", []),

	("castle_e_sally_door_a", sokf_show_hit_point_bar|sokf_destructible|sokf_moveable, "castle_e_sally_door_a", "bo_castle_e_sally_door_a", 
	[(ti_on_scene_prop_use,
		[
			(store_trigger_param_1, ":trigger_param_1"),
			(store_trigger_param_2, ":trigger_param_2"),
			(agent_get_position, 1, ":trigger_param_1"),
			(prop_instance_get_starting_position, 2, ":trigger_param_2"),
			(scene_prop_get_slot, ":scene_prop_slot_trigger_param_2_scene_prop_open_or_close_slot", ":trigger_param_2", slot_scene_prop_open_or_close_slot),
			(try_begin),
				(this_or_next|position_is_behind_position, 1, 2),
				(eq, ":scene_prop_slot_trigger_param_2_scene_prop_open_or_close_slot", 1),
				(try_begin),
					(call_script, "script_use_item", ":trigger_param_2", ":trigger_param_1"),
					(get_max_players, ":max_players"),
					(try_for_range, ":number", 1, ":max_players"),
						(player_is_active, ":number"),
						(multiplayer_send_2_int_to_player, ":number", 76, ":trigger_param_2", ":trigger_param_1"),
					(try_end),
				(try_end),
			(try_end)
		]),

		(ti_on_scene_prop_init,
		[
			(store_trigger_param_1, ":trigger_param_1"),
			(scene_prop_set_hit_points, ":trigger_param_1", 3000)
		]),

		(ti_on_scene_prop_destroy,
		[
			(play_sound, "snd_dummy_destroyed"),
			(assign, ":var_1", 86),
			(try_begin),
				(this_or_next|multiplayer_is_server),
				(neg|game_in_multiplayer_mode),
				(store_trigger_param_1, ":trigger_param_1"),
				(store_trigger_param_2, ":trigger_param_2"),
				(set_fixed_point_multiplier, 100),
				(prop_instance_get_position, 1, ":trigger_param_1"),
				(try_begin),
					(ge, ":trigger_param_2", 0),
					(agent_get_position, 2, ":trigger_param_2"),
					(try_begin),
						(position_is_behind_position, 2, 1),
						(val_mul, ":var_1", -1),
					(try_end),
				(try_end),
				(init_position, 3),
				(try_begin),
					(ge, ":var_1", 0),
					(position_move_y, 3, -100),
				(else_try),
					(position_move_y, 3, 100),
				(try_end),
				(position_move_x, 3, -50),
				(position_transform_position_to_parent, 4, 1, 3),
				(position_move_z, 4, 100),
				(position_get_distance_to_ground_level, ":position_distance_to_ground_level_4", 4),
				(val_sub, ":position_distance_to_ground_level_4", 100),
				(assign, ":var_5", ":position_distance_to_ground_level_4"),
				(val_div, ":var_5", 3),
				(try_begin),
					(ge, ":var_1", 0),
					(val_add, ":var_1", ":var_5"),
				(else_try),
					(val_sub, ":var_1", ":var_5"),
				(try_end),
				(position_rotate_x, 1, ":var_1"),
				(prop_instance_animate_to_position, ":trigger_param_1", 1, 70),
			(try_end)
		]),

		(ti_on_scene_prop_hit,
		[
			(store_trigger_param_1, ":trigger_param_1"),
			(store_trigger_param_2, ":trigger_param_2"),
			(try_begin),
				(scene_prop_get_hit_points, ":scene_prop_hit_points_trigger_param_1", ":trigger_param_1"),
				(val_sub, ":scene_prop_hit_points_trigger_param_1", ":trigger_param_2"),
				(gt, ":scene_prop_hit_points_trigger_param_1", 0),
				(play_sound, "snd_dummy_hit"),
			(else_try),
				(neg|multiplayer_is_server),
				(play_sound, "snd_dummy_destroyed"),
			(try_end),
			(try_begin),
				(this_or_next|multiplayer_is_server),
				(neg|game_in_multiplayer_mode),
				(particle_system_burst, "psys_dummy_smoke", 1, 3),
				(particle_system_burst, "psys_dummy_straw", 1, 10),
			(try_end)
		])
	]),

	("castle_e_corner", 0, "castle_e_corner", "bo_castle_e_corner", []),

	("castle_e_corner_b", 0, "castle_e_corner_b", "bo_castle_e_corner_b", []),

	("castle_e_corner_c", 0, "castle_e_corner_c", "bo_castle_e_corner_c", []),

	("castle_e_stairs_a", 0, "castle_e_stairs_a", "bo_castle_e_stairs_a", []),

	("castle_e_tower_arabian", 0, "castle_e_tower_arabian", "bo_castle_e_tower", []),

	("castle_e_tower", 0, "castle_e_tower", "bo_castle_e_tower", []),

	("castle_e_gate_house_a", 0, "castle_e_gate_house_a", "bo_castle_e_gate_house_a", []),

	("castle_e_keep_a", 0, "castle_e_keep_a", "bo_castle_e_keep_a", []),

	("stand_thatched", 0, "general_stand_thatched", "bo_stand_thatched", []),

	("stand_cloth", 0, "general_stand_cloth", "bo_stand_cloth", []),

	("castle_e_house_a", 0, "castle_e_house_a", "bo_castle_e_house_a", []),

	("castle_e_house_b", 0, "castle_e_house_b", "bo_castle_e_house_b", []),

	("arena_block_a", 0, "arena_block_a", "bo_arena_block_ab", []),

	("arena_block_b", 0, "arena_block_b", "bo_arena_block_ab", []),

	("arena_block_c", 0, "arena_block_c", "bo_arena_block_c", []),

	("arena_block_d", 0, "arena_block_d", "bo_arena_block_def", []),

	("arena_block_e", 0, "arena_block_e", "bo_arena_block_def", []),

	("arena_block_f", 0, "arena_block_f", "bo_arena_block_def", []),

	("arena_block_g", 0, "arena_block_g", "bo_arena_block_ghi", []),

	("arena_block_h", 0, "arena_block_h", "bo_arena_block_ghi", []),

	("arena_block_i", 0, "arena_block_i", "bo_arena_block_ghi", []),

	("arena_block_j", 0, "arena_block_j", "bo_arena_block_j", []),

	("arena_block_j_awning", 0, "arena_block_j_awning", "bo_arena_block_j_awning", []),

	("arena_palisade_a", 0, "arena_palisade_a", "bo_arena_palisade_a", []),

	("arena_wall_a", 0, "arena_wall_a", "bo_arena_wall_ab", []),

	("arena_wall_b", 0, "arena_wall_b", "bo_arena_wall_ab", []),

	("arena_barrier_a", 0, "arena_barrier_a", "bo_arena_barrier_a", []),

	("arena_barrier_b", 0, "arena_barrier_b", "bo_arena_barrier_bc", []),

	("arena_barrier_c", 0, "arena_barrier_c", "bo_arena_barrier_bc", []),

	("arena_tower_a", 0, "arena_tower_a", "bo_arena_tower_abc", []),

	("arena_tower_b", 0, "arena_tower_b", "bo_arena_tower_abc", []),

	("arena_tower_c", 0, "arena_tower_c", "bo_arena_tower_abc", []),

	("arena_spectator_a", 0, "nobleman_spectator_1", "0", []),

	("arena_spectator_b", 0, "nobleman_spectator_2", "0", []),

	("arena_spectator_c", 0, "nobleman_spectator_3", "0", []),

	("arena_spectator_sitting_a", 0, "arena_spectator_sitting_a", "0", []),

	("arena_spectator_sitting_b", 0, "arena_spectator_sitting_b", "0", []),

	("arena_spectator_sitting_c", 0, "arena_spectator_sitting_c", "0", []),

	("courtyard_gate_a", 0, "courtyard_entry_a", "bo_courtyard_entry_a", []),

	("courtyard_gate_b", 0, "courtyard_entry_b", "bo_courtyard_entry_b", []),

	("courtyard_gate_c", 0, "courtyard_entry_c", "bo_courtyard_entry_c", []),

	("courtyard_gate_snowy", 0, "courtyard_entry_snowy", "bo_courtyard_entry_a", []),

	("castle_tower_a", 0, "castle_tower_a", "bo_castle_tower_a", []),

	("castle_battlement_a", 0, "castle_battlement_a", "bo_castle_battlement_a", []),

	("castle_battlement_b", 0, "castle_battlement_b", "bo_castle_battlement_b", []),

	("castle_battlement_c", 0, "castle_battlement_c", "bo_castle_battlement_c", []),

	("castle_battlement_a_destroyed", 0, "castle_battlement_a_destroyed", "bo_castle_battlement_a_destroyed", []),

	("castle_battlement_b_destroyed", 0, "castle_battlement_b_destroyed", "bo_castle_battlement_b_destroyed", []),

	("castle_battlement_corner_a", 0, "castle_battlement_corner_a", "bo_castle_battlement_corner_a", []),

	("castle_battlement_corner_b", 0, "castle_battlement_corner_b", "bo_castle_battlement_corner_b", []),

	("castle_battlement_corner_c", 0, "castle_battlement_corner_c", "bo_castle_battlement_corner_c", []),

	("castle_battlement_stairs_a", 0, "castle_battlement_stairs_a", "bo_castle_battlement_stairs_a", []),

	("castle_battlement_stairs_b", 0, "castle_battlement_stairs_b", "bo_castle_battlement_stairs_b", []),

	("castle_gate_house_a", 0, "castle_gate_house_a", "bo_castle_gate_house_a", []),

	("castle_round_tower_a", 0, "castle_round_tower_a", "bo_castle_round_tower_a", []),

	("castle_square_keep_a", 0, "castle_square_keep_a", "bo_castle_square_keep_a", []),

	("castle_stairs_a", sokf_type_ladder, "castle_stairs_a", "bo_castle_stairs_a", []),

	("castle_drawbridge_open", 0, "castle_drawbridges_open", "bo_castle_drawbridges_open", []),

	("castle_drawbridge_closed", 0, "castle_drawbridges_closed", "bo_castle_drawbridges_closed", []),

	("spike_group_a", 0, "spike_group_a", "bo_spike_group_a", []),

	("spike_a", 0, "spike_a", "bo_spike_a", []),

	("belfry_a", sokf_moveable, "belfry_a", "bo_belfry_a", []),

	("belfry_b", sokf_moveable, "belfry_b", "bo_belfry_b", []),

	("belfry_b_platform_a", sokf_moveable, "belfry_b_platform_a", "bo_belfry_b_platform_a", []),

	("belfry_old", 0, "belfry_a", "bo_belfry_a", []),

	("belfry_platform_a", sokf_moveable, "belfry_platform_a", "bo_belfry_platform_a", []),

	("belfry_platform_b", sokf_moveable, "belfry_platform_b", "bo_belfry_platform_b", []),

	("belfry_platform_old", 0, "belfry_platform_b", "bo_belfry_platform_b", []),

	("belfry_wheel", sokf_moveable, "belfry_wheel", "0", []),

	("belfry_wheel_old", 0, "belfry_wheel", "0", []),

	("mangonel", 0, "mangonel", "bo_mangonel", []),

	("trebuchet_old", 0, "trebuchet_old", "bo_trebuchet_old", []),

	("trebuchet_new", 0, "trebuchet_new", "bo_trebuchet_old", []),

	("trebuchet_destructible", sokf_show_hit_point_bar|sokf_destructible|sokf_moveable, "trebuchet_new", "bo_trebuchet_old", 
	[(ti_on_scene_prop_init,
		[
			(store_trigger_param_1, ":trigger_param_1"),
			(scene_prop_set_hit_points, ":trigger_param_1", 2400)
		]),

		(ti_on_scene_prop_destroy,
		[
			(play_sound, "snd_dummy_destroyed"),
			(try_begin),
				(this_or_next|multiplayer_is_server),
				(neg|game_in_multiplayer_mode),
				(store_trigger_param_1, ":trigger_param_1"),
				(prop_instance_get_position, 1, ":trigger_param_1"),
				(particle_system_burst, "psys_dummy_smoke_big", 1, 100),
				(particle_system_burst, "psys_dummy_straw_big", 1, 100),
				(position_move_z, 1, -500),
				(position_rotate_x, 1, 90),
				(prop_instance_animate_to_position, ":trigger_param_1", 1, 300),
				(try_begin),
					(eq, "$g_round_ended", 0),
					(scene_prop_get_team, ":scene_prop_team_trigger_param_1", ":trigger_param_1"),
					(try_begin),
						(eq, ":scene_prop_team_trigger_param_1", 0),
						(assign, ":value", -1),
					(else_try),
						(assign, ":value", 1),
					(try_end),
					(try_begin),
						(eq, "$g_number_of_targets_destroyed", 0),
						(store_mul, ":value_2", ":value", 2),
						(call_script, "script_show_multiplayer_message", 15, ":value_2"),
						(get_max_players, ":max_players"),
						(try_for_range, ":number", 1, ":max_players"),
							(player_is_active, ":number"),
							(multiplayer_send_2_int_to_player, ":number", 68, 15, ":value_2"),
						(try_end),
						(val_add, "$g_number_of_targets_destroyed", 1),
					(else_try),
						(store_mul, ":value_2", ":value", 9),
						(call_script, "script_show_multiplayer_message", 15, ":value_2"),
						(get_max_players, ":max_players"),
						(try_for_range, ":number", 1, ":max_players"),
							(player_is_active, ":number"),
							(multiplayer_send_2_int_to_player, ":number", 68, 15, ":value_2"),
						(try_end),
						(val_add, "$g_number_of_targets_destroyed", 1),
					(try_end),
				(try_end),
				(assign, ":var_7", 0),
				(get_max_players, ":max_players"),
				(try_for_range, ":number", 0, ":max_players"),
					(player_is_active, ":number"),
					(try_begin),
						(eq, "spr_trebuchet_destructible", "$g_destructible_target_1"),
						(player_get_slot, ":number_damage_given_to_target_1", ":number", slot_player_damage_given_to_target_1),
					(else_try),
						(player_get_slot, ":number_damage_given_to_target_1", ":number", slot_player_damage_given_to_target_2),
					(try_end),
					(val_add, ":var_7", ":number_damage_given_to_target_1"),
				(try_end),
				(assign, ":value_3", 0),
				(get_max_players, ":max_players"),
				(try_for_range, ":number", 0, ":max_players"),
					(player_is_active, ":number"),
					(val_add, ":value_3", 50),
				(try_end),
				(try_begin),
					(ge, ":value_3", 1500),
					(assign, ":value_3", 1500),
				(try_end),
				(val_mul, ":value_3", "$g_multiplayer_battle_earnings_multiplier"),
				(val_div, ":value_3", 100),
				(get_max_players, ":max_players"),
				(try_for_range, ":number", 0, ":max_players"),
					(player_is_active, ":number"),
					(try_begin),
						(eq, "spr_trebuchet_destructible", "$g_destructible_target_1"),
						(player_get_slot, ":number_damage_given_to_target_1", ":number", slot_player_damage_given_to_target_1),
					(else_try),
						(player_get_slot, ":number_damage_given_to_target_1", ":number", slot_player_damage_given_to_target_2),
					(try_end),
					(player_get_gold, ":gold_number", ":number"),
					(val_mul, ":number_damage_given_to_target_1", ":value_3"),
					(store_div, ":value_4", ":number_damage_given_to_target_1", ":var_7"),
					(val_add, ":gold_number", ":value_4"),
					(player_set_gold, ":number", ":gold_number", 15000),
				(try_end),
			(try_end)
		]),

		(ti_on_scene_prop_hit,
		[
			(store_trigger_param_1, ":trigger_param_1"),
			(store_trigger_param_2, ":trigger_param_2"),
			(try_begin),
				(scene_prop_get_hit_points, ":scene_prop_hit_points_trigger_param_1", ":trigger_param_1"),
				(val_sub, ":scene_prop_hit_points_trigger_param_1", ":trigger_param_2"),
				(gt, ":scene_prop_hit_points_trigger_param_1", 0),
				(play_sound, "snd_dummy_hit"),
			(else_try),
				(neg|multiplayer_is_server),
				(play_sound, "snd_dummy_destroyed"),
			(try_end),
			(try_begin),
				(this_or_next|multiplayer_is_server),
				(neg|game_in_multiplayer_mode),
				(particle_system_burst, "psys_dummy_smoke", 1, 3),
				(particle_system_burst, "psys_dummy_straw", 1, 10),
				(set_fixed_point_multiplier, 1),
				(position_get_x, ":position_x_2", 2),
				(try_begin),
					(ge, ":position_x_2", 0),
					(agent_is_alive, ":position_x_2"),
					(agent_is_human, ":position_x_2"),
					(neg|agent_is_non_player, ":position_x_2"),
					(agent_get_player_id, ":player_id_position_x_2", ":position_x_2"),
					(ge, ":player_id_position_x_2", 0),
					(player_is_active, ":player_id_position_x_2"),
					(try_begin),
						(eq, "spr_trebuchet_destructible", "$g_destructible_target_1"),
						(player_get_slot, ":player_id_position_x_2_damage_given_to_target_1", ":player_id_position_x_2", slot_player_damage_given_to_target_1),
						(val_add, ":player_id_position_x_2_damage_given_to_target_1", ":trigger_param_2"),
						(player_set_slot, ":player_id_position_x_2", slot_player_damage_given_to_target_1, ":player_id_position_x_2_damage_given_to_target_1"),
					(else_try),
						(player_get_slot, ":player_id_position_x_2_damage_given_to_target_1", ":player_id_position_x_2", slot_player_damage_given_to_target_2),
						(val_add, ":player_id_position_x_2_damage_given_to_target_1", ":trigger_param_2"),
						(player_set_slot, ":player_id_position_x_2", slot_player_damage_given_to_target_2, ":player_id_position_x_2_damage_given_to_target_1"),
					(try_end),
				(try_end),
			(try_end)
		])
	]),

	("stone_ball", 0, "stone_ball", "0", []),

	("village_house_a", 0, "village_house_a", "bo_village_house_a", []),

	("village_house_b", 0, "village_house_b", "bo_village_house_b", []),

	("village_house_c", 0, "village_house_c", "bo_village_house_c", []),

	("village_house_d", 0, "village_house_d", "bo_village_house_d", []),

	("farm_house_a", 0, "farm_house_a", "bo_farm_house_a", []),

	("farm_house_b", 0, "farm_house_b", "bo_farm_house_b", []),

	("farm_house_c", 0, "farm_house_c", "bo_farm_house_c", []),

	("mountain_house_a", 0, "mountain_house_a", "bo_mountain_house_a", []),

	("mountain_house_b", 0, "mountain_house_b", "bo_mountain_house_b", []),

	("village_hut_a", 0, "village_hut_a", "bo_village_hut_a", []),

	("crude_fence", 0, "fence", "bo_fence", []),

	("crude_fence_small", 0, "crude_fence_small", "bo_crude_fence_small", []),

	("crude_fence_small_b", 0, "crude_fence_small_b", "bo_crude_fence_small_b", []),

	("ramp_12m", 0, "ramp_12m", "bo_ramp_12m", []),

	("ramp_14m", 0, "ramp_14m", "bo_ramp_14m", []),

	("siege_ladder_6m", sokf_type_ladder, "siege_ladder_move_6m", "bo_siege_ladder_move_6m", []),

	("siege_ladder_8m", sokf_type_ladder, "siege_ladder_move_8m", "bo_siege_ladder_move_8m", []),

	("siege_ladder_10m", sokf_type_ladder, "siege_ladder_move_10m", "bo_siege_ladder_move_10m", []),

	("siege_ladder_12m", sokf_type_ladder, "siege_ladder_12m", "bo_siege_ladder_12m", []),

	("siege_ladder_14m", sokf_type_ladder, "siege_ladder_14m", "bo_siege_ladder_14m", []),

	("siege_ladder_move_6m", sokf_type_ladder|sokf_moveable|spr_use_time(2), "siege_ladder_move_6m", "bo_siege_ladder_move_6m", 
	[(ti_on_scene_prop_use,
		[
			(store_trigger_param_1, ":trigger_param_1"),
			(store_trigger_param_2, ":trigger_param_2"),
			(call_script, "script_use_item", ":trigger_param_2", ":trigger_param_1"),
			(get_max_players, ":max_players"),
			(try_for_range, ":number", 1, ":max_players"),
				(player_is_active, ":number"),
				(multiplayer_send_2_int_to_player, ":number", 76, ":trigger_param_2", ":trigger_param_1"),
			(try_end)
		]),

		(ti_on_scene_prop_is_animating,
		[
			(store_trigger_param_1, ":trigger_param_1"),
			(store_trigger_param_2, ":trigger_param_2"),
			(call_script, "script_check_creating_ladder_dust_effect", ":trigger_param_1", ":trigger_param_2")
		]),

		(ti_on_scene_prop_animation_finished,
		[
			(store_trigger_param_1, ":trigger_param_1"),
			(prop_instance_enable_physics, ":trigger_param_1", 1)
		])
	]),

	("siege_ladder_move_8m", sokf_type_ladder|sokf_moveable|spr_use_time(2), "siege_ladder_move_8m", "bo_siege_ladder_move_8m", 
	[(ti_on_scene_prop_use,
		[
			(store_trigger_param_1, ":trigger_param_1"),
			(store_trigger_param_2, ":trigger_param_2"),
			(call_script, "script_use_item", ":trigger_param_2", ":trigger_param_1"),
			(get_max_players, ":max_players"),
			(try_for_range, ":number", 1, ":max_players"),
				(player_is_active, ":number"),
				(multiplayer_send_2_int_to_player, ":number", 76, ":trigger_param_2", ":trigger_param_1"),
			(try_end)
		]),

		(ti_on_scene_prop_is_animating,
		[
			(store_trigger_param_1, ":trigger_param_1"),
			(store_trigger_param_2, ":trigger_param_2"),
			(call_script, "script_check_creating_ladder_dust_effect", ":trigger_param_1", ":trigger_param_2")
		]),

		(ti_on_scene_prop_animation_finished,
		[
			(store_trigger_param_1, ":trigger_param_1"),
			(prop_instance_enable_physics, ":trigger_param_1", 1)
		])
	]),

	("siege_ladder_move_10m", sokf_type_ladder|sokf_moveable|spr_use_time(3), "siege_ladder_move_10m", "bo_siege_ladder_move_10m", 
	[(ti_on_scene_prop_use,
		[
			(store_trigger_param_1, ":trigger_param_1"),
			(store_trigger_param_2, ":trigger_param_2"),
			(call_script, "script_use_item", ":trigger_param_2", ":trigger_param_1"),
			(get_max_players, ":max_players"),
			(try_for_range, ":number", 1, ":max_players"),
				(player_is_active, ":number"),
				(multiplayer_send_2_int_to_player, ":number", 76, ":trigger_param_2", ":trigger_param_1"),
			(try_end)
		]),

		(ti_on_scene_prop_is_animating,
		[
			(store_trigger_param_1, ":trigger_param_1"),
			(store_trigger_param_2, ":trigger_param_2"),
			(call_script, "script_check_creating_ladder_dust_effect", ":trigger_param_1", ":trigger_param_2")
		]),

		(ti_on_scene_prop_animation_finished,
		[
			(store_trigger_param_1, ":trigger_param_1"),
			(prop_instance_enable_physics, ":trigger_param_1", 1)
		])
	]),

	("siege_ladder_move_12m", sokf_type_ladder|sokf_moveable|spr_use_time(3), "siege_ladder_move_12m", "bo_siege_ladder_move_12m", 
	[(ti_on_scene_prop_use,
		[
			(store_trigger_param_1, ":trigger_param_1"),
			(store_trigger_param_2, ":trigger_param_2"),
			(call_script, "script_use_item", ":trigger_param_2", ":trigger_param_1"),
			(get_max_players, ":max_players"),
			(try_for_range, ":number", 1, ":max_players"),
				(player_is_active, ":number"),
				(multiplayer_send_2_int_to_player, ":number", 76, ":trigger_param_2", ":trigger_param_1"),
			(try_end)
		]),

		(ti_on_scene_prop_is_animating,
		[
			(store_trigger_param_1, ":trigger_param_1"),
			(store_trigger_param_2, ":trigger_param_2"),
			(call_script, "script_check_creating_ladder_dust_effect", ":trigger_param_1", ":trigger_param_2")
		]),

		(ti_on_scene_prop_animation_finished,
		[
			(store_trigger_param_1, ":trigger_param_1"),
			(prop_instance_enable_physics, ":trigger_param_1", 1)
		])
	]),

	("siege_ladder_move_14m", sokf_type_ladder|sokf_moveable|spr_use_time(4), "siege_ladder_move_14m", "bo_siege_ladder_move_14m", 
	[(ti_on_scene_prop_use,
		[
			(store_trigger_param_1, ":trigger_param_1"),
			(store_trigger_param_2, ":trigger_param_2"),
			(call_script, "script_use_item", ":trigger_param_2", ":trigger_param_1"),
			(get_max_players, ":max_players"),
			(try_for_range, ":number", 1, ":max_players"),
				(player_is_active, ":number"),
				(multiplayer_send_2_int_to_player, ":number", 76, ":trigger_param_2", ":trigger_param_1"),
			(try_end)
		]),

		(ti_on_scene_prop_is_animating,
		[
			(store_trigger_param_1, ":trigger_param_1"),
			(store_trigger_param_2, ":trigger_param_2"),
			(call_script, "script_check_creating_ladder_dust_effect", ":trigger_param_1", ":trigger_param_2")
		]),

		(ti_on_scene_prop_animation_finished,
		[
			(store_trigger_param_1, ":trigger_param_1"),
			(prop_instance_enable_physics, ":trigger_param_1", 1)
		])
	]),

	("portcullis", sokf_moveable, "portcullis_a", "bo_portcullis_a", []),

	("bed_a", 0, "bed_a", "bo_bed_a", []),

	("bed_b", 0, "bed_b", "bo_bed_b", []),

	("bed_c", 0, "bed_c", "bo_bed_c", []),

	("bed_d", 0, "bed_d", "bo_bed_d", []),

	("bed_e", 0, "bed_e_new", "bo_bed_e", []),

	("bed_f", 0, "bed_f", "bo_bed_f", []),

	("towngate_door_left", sokf_moveable, "door_g_left", "bo_door_left", []),

	("towngate_door_right", sokf_moveable, "door_g_right", "bo_door_right", []),

	("towngate_rectangle_door_left", sokf_moveable, "towngate_rectangle_door_left", "bo_towngate_rectangle_door_left", []),

	("towngate_rectangle_door_right", sokf_moveable, "towngate_rectangle_door_right", "bo_towngate_rectangle_door_right", []),

	("door_screen", sokf_moveable, "door_screen", "0", []),

	("door_a", sokf_moveable, "door_a", "bo_door_a", []),

	("door_b", sokf_moveable, "door_b", "bo_door_a", []),

	("door_c", sokf_moveable, "door_c", "bo_door_a", []),

	("door_d", sokf_moveable, "door_d", "bo_door_a", []),

	("tavern_door_a", sokf_moveable, "tavern_door_a", "bo_tavern_door_a", []),

	("tavern_door_b", sokf_moveable, "tavern_door_b", "bo_tavern_door_a", []),

	("door_e_left", sokf_moveable, "door_e_left", "bo_door_left", []),

	("door_e_right", sokf_moveable, "door_e_right", "bo_door_right", []),

	("door_f_left", sokf_moveable, "door_f_left", "bo_door_left", []),

	("door_f_right", sokf_moveable, "door_f_right", "bo_door_right", []),

	("door_h_left", sokf_moveable, "door_g_left", "bo_door_left", []),

	("door_h_right", sokf_moveable, "door_g_right", "bo_door_right", []),

	("draw_bridge_a", 0, "draw_bridge_a", "bo_draw_bridge_a", []),

	("chain_1m", 0, "chain_1m", "0", []),

	("chain_2m", 0, "chain_2m", "0", []),

	("chain_5m", 0, "chain_5m", "0", []),

	("chain_10m", 0, "chain_10m", "0", []),

	("bridge_modular_a", 0, "bridge_modular_a", "bo_bridge_modular_a", []),

	("bridge_modular_b", 0, "bridge_modular_b", "bo_bridge_modular_b", []),

	("church_a", 0, "church_a", "bo_church_a", []),

	("church_tower_a", 0, "church_tower_a", "bo_church_tower_a", []),

	("stone_step_a", 0, "floor_stone_a", "bo_floor_stone_a", []),

	("stone_step_b", 0, "stone_step_b", "0", []),

	("stone_step_c", 0, "stone_step_c", "0", []),

	("stone_heap", 0, "stone_heap", "bo_stone_heap", []),

	("stone_heap_b", 0, "stone_heap_b", "bo_stone_heap", []),

	("panel_door_a", 0, "house_door_a", "bo_house_door_a", []),

	("panel_door_b", 0, "house_door_b", "bo_house_door_a", []),

	("smoke_stain", 0, "soot_a", "0", []),

	("brazier_with_fire", 0, "brazier_new", "bo_brazier", 
	[(ti_on_scene_prop_init,
		[
			(set_position_delta, 0, 0, 85),
			(particle_system_add_new, "psys_brazier_fire_1"),
			(particle_system_add_new, "psys_fire_sparks_1"),
			(set_position_delta, 0, 0, 100),
			(particle_system_add_new, "psys_fire_glow_1"),
			(particle_system_emit, "psys_fire_glow_1", 9000000)
		])
	]),

	("cooking_fire", 0, "fire_floor", "0", 
	[(ti_on_scene_prop_init,
		[
			(set_position_delta, 0, 0, 12),
			(particle_system_add_new, "psys_cooking_fire_1"),
			(particle_system_add_new, "psys_fire_sparks_1"),
			(particle_system_add_new, "psys_cooking_smoke"),
			(set_position_delta, 0, 0, 50),
			(particle_system_add_new, "psys_fire_glow_1"),
			(particle_system_emit, "psys_fire_glow_1", 9000000)
		])
	]),

	("cauldron_a", 0, "cauldron_a", "bo_cauldron_a", []),

	("fry_pan_a", 0, "fry_pan_a_new", "0", []),

	("tripod_cauldron_a", 0, "tripod_cauldron_a", "bo_tripod_cauldron_a", []),

	("tripod_cauldron_b", 0, "tripod_cauldron_b", "bo_tripod_cauldron_b", []),

	("open_stable_a", 0, "open_stable_a", "bo_open_stable_a", []),

	("open_stable_b", 0, "open_stable_b", "bo_open_stable_b", []),

	("plate_a", 0, "plate_a_new", "0", []),

	("plate_b", 0, "plate_b_new", "0", []),

	("plate_c", 0, "plate_c_new", "0", []),

	("lettuce", 0, "lettuce_new", "0", []),

	("hanger", 0, "hanger", "0", []),

	("knife_eating", 0, "knife_eating_new", "0", []),

	("colander", 0, "colander_new", "0", []),

	("ladle", 0, "ladle_new", "0", []),

	("spoon", 0, "spoon_new", "0", []),

	("skewer", 0, "skewer", "0", []),

	("grape_a", 0, "grape_a_new", "0", []),

	("grape_b", 0, "grape_b_new", "0", []),

	("apple_a", 0, "apple_a_new", "0", []),

	("apple_b", 0, "apple_b_new", "0", []),

	("maize_a", 0, "maize_a", "0", []),

	("maize_b", 0, "maize_b", "0", []),

	("cabbage", 0, "cabbage_new", "0", []),

	("flax_bundle", 0, "trade_raw_flax", "0", []),

	("olive_plane", 0, "olive_plane", "0", []),

	("grapes_plane", 0, "grapes_plane", "0", []),

	("date_fruit_plane", 0, "date_fruit_plane", "0", []),

	("bowl", 0, "bowl_big_new", "0", []),

	("bowl_small", 0, "bowl_small_new", "0", []),

	("dye_blue", 0, "raw_dye_blue", "0", []),

	("dye_red", 0, "raw_dye_red", "0", []),

	("dye_yellow", 0, "raw_dye_yellow", "0", []),

	("basket", 0, "basket_small", "0", []),

	("basket_big", 0, "basket_large", "0", []),

	("basket_big_green", 0, "basket_big", "0", []),

	("leatherwork_frame", 0, "trade_leatherwork", "0", []),

	("cabbage_b", 0, "cabbage_b_new", "0", []),

	("bean", 0, "bean", "0", []),

	("basket_a", 0, "basket_a_new", "bo_basket_a", []),

	("feeding_trough_a", 0, "feeding_trough_a", "bo_feeding_trough_a", []),

	("marrow_a", 0, "marrow_a_new", "0", []),

	("marrow_b", 0, "marrow_b_new", "0", []),

	("squash_plant", 0, "marrow_c", "0", []),

	("gatehouse_new_a", sokf_type_ladder, "gatehouse_new_a", "bo_gatehouse_new_a", []),

	("gatehouse_new_b", sokf_type_ladder, "gatehouse_new_b", "bo_gatehouse_new_b", []),

	("gatehouse_new_snowy_a", 0, "gatehouse_new_snowy_a", "bo_gatehouse_new_b", []),

	("winch", sokf_moveable, "winch", "bo_winch", []),

	("winch_b", sokf_moveable|spr_use_time(5), "winch_b", "bo_winch", 
	[(ti_on_scene_prop_use,
		[
			(store_trigger_param_1, ":trigger_param_1"),
			(store_trigger_param_2, ":trigger_param_2"),
			(call_script, "script_use_item", ":trigger_param_2", ":trigger_param_1"),
			(get_max_players, ":max_players"),
			(try_for_range, ":number", 1, ":max_players"),
				(player_is_active, ":number"),
				(multiplayer_send_2_int_to_player, ":number", 76, ":trigger_param_2", ":trigger_param_1"),
			(try_end)
		])
	]),

	("drawbridge", 0, "drawbridge", "bo_drawbridge", []),

	("gatehouse_door_left", sokf_moveable, "gatehouse_door_left", "bo_gatehouse_door_left", []),

	("gatehouse_door_right", sokf_moveable, "gatehouse_door_right", "bo_gatehouse_door_right", []),

	("cheese_a", 0, "cheese_a_new", "0", []),

	("cheese_b", 0, "cheese_b_new", "0", []),

	("cheese_slice_a", 0, "cheese_slice_a_new", "0", []),

	("bread_a", 0, "bread_a_new", "0", []),

	("bread_b", 0, "bread_b_new", "0", []),

	("bread_slice_a", 0, "bread_slice_a_new", "0", []),

	("fish_a", 0, "fish_a", "0", []),

	("fish_roasted_a", 0, "fish_roasted_a", "0", []),

	("chicken_roasted", 0, "trade_chicken_new", "0", []),

	("food_steam", 0, "0", "0", 
	[(ti_on_scene_prop_init,
		[
			(set_position_delta, 0, 0, 0),
			(particle_system_add_new, "psys_food_steam")
		])
	]),

	("city_smoke", 0, "0", "0", 
	[(ti_on_scene_prop_init,
		[
			(store_time_of_day, reg12),
			(neg|is_between, reg12, 5, 20),
			(set_position_delta, 0, 0, 0),
			(particle_system_add_new, "psys_night_smoke_1")
		])
	]),

	("city_fire_fly_night", 0, "0", "0", 
	[(ti_on_scene_prop_init,
		[
			(store_time_of_day, reg12),
			(neg|is_between, reg12, 5, 20),
			(set_position_delta, 0, 0, 0),
			(particle_system_add_new, "psys_fire_fly_1")
		])
	]),

	("city_fly_day", 0, "0", "0", 
	[(ti_on_scene_prop_init,
		[
			(particle_system_add_new, "psys_bug_fly_1")
		])
	]),

	("flue_smoke_tall", 0, "0", "0", 
	[(ti_on_scene_prop_init,
		[
			(particle_system_add_new, "psys_flue_smoke_tall")
		])
	]),

	("flue_smoke_short", 0, "0", "0", 
	[(ti_on_scene_prop_init,
		[
			(particle_system_add_new, "psys_flue_smoke_short")
		])
	]),

	("moon_beam", 0, "0", "0", 
	[(ti_on_scene_prop_init,
		[
			(particle_system_add_new, "psys_moon_beam_1"),
			(particle_system_add_new, "psys_moon_beam_paricle_1")
		])
	]),

	("fire_small", 0, "0", "0", 
	[(ti_on_scene_prop_init,
		[
			(particle_system_add_new, "psys_fireplace_fire_small")
		])
	]),

	("fire_small_blue", 0, "0", "0", 
	[(ti_on_scene_prop_init,
		[
			(particle_system_add_new, "psys_fireplace_fire_small_blue")
		])
	]),

	("fire_big", 0, "0", "0", 
	[(ti_on_scene_prop_init,
		[
			(particle_system_add_new, "psys_fireplace_fire_big")
		])
	]),

	("battle_field_smoke", 0, "0", "0", 
	[(ti_on_scene_prop_init,
		[
			(particle_system_add_new, "psys_war_smoke_tall")
		])
	]),

	("Village_fire_big", 0, "0", "0", 
	[(ti_on_scene_prop_init,
		[
			(particle_system_add_new, "psys_village_fire_big"),
			(set_position_delta, 0, 0, 100),
			(particle_system_add_new, "psys_village_fire_smoke_big")
		])
	]),

	("Village_fire_big_wildfire", 0, "0", "0", 
	[(ti_on_scene_prop_init,
		[
			(particle_system_add_new, "psys_wildfire_village_fire_big"),
			(set_position_delta, 0, 0, 100),
			(particle_system_add_new, "psys_village_fire_smoke_big")
		])
	]),

	("Village_fire_embers", 0, "0", "0", 
	[(ti_on_scene_prop_init,
		[
			(particle_system_add_new, "psys_fire_sparks_1"),
			(set_position_delta, 0, 0, 100),
			(particle_system_add_new, "psys_torch_fire_sparks")
		])
	]),

	("candle_a", 0, "candle_a", "0", 
	[(ti_on_scene_prop_init,
		[
			(set_position_delta, 0, 0, 27),
			(particle_system_add_new, "psys_candle_light")
		])
	]),

	("candle_b", 0, "candle_b", "0", 
	[(ti_on_scene_prop_init,
		[
			(set_position_delta, 0, 0, 25),
			(particle_system_add_new, "psys_candle_light")
		])
	]),

	("candle_c", 0, "candle_c", "0", 
	[(ti_on_scene_prop_init,
		[
			(set_position_delta, 0, 0, 10),
			(particle_system_add_new, "psys_candle_light_small")
		])
	]),

	("lamp_a", 0, "lamp_a", "0", 
	[(ti_on_scene_prop_init,
		[
			(set_position_delta, 66, 0, 2),
			(particle_system_add_new, "psys_candle_light")
		])
	]),

	("lamp_b", 0, "lamp_b", "0", 
	[(ti_on_scene_prop_init,
		[
			(set_position_delta, 65, 0, -7),
			(particle_system_add_new, "psys_lamp_fire"),
			(set_position_delta, 70, 0, -5),
			(particle_system_add_new, "psys_fire_glow_1"),
			(particle_system_emit, "psys_fire_glow_1", 9000000),
			(play_sound, "snd_fire_loop", 0)
		])
	]),

	("hook_a", 0, "hook_a", "0", []),

	("window_night", 0, "window_night", "0", []),

	("fried_pig", 0, "trade_pork_new", "0", []),

	("village_oven", 0, "village_oven", "bo_village_oven", []),

	("dungeon_water_drops", 0, "0", "0", 
	[(ti_on_scene_prop_init,
		[
			(particle_system_add_new, "psys_dungeon_water_drops")
		])
	]),

	("shadow_circle_1", 0, "shadow_circle_1", "0", []),

	("shadow_circle_2", 0, "shadow_circle_2", "0", []),

	("shadow_square_1", 0, "shadow_square_1", "0", []),

	("shadow_square_2", 0, "shadow_square_2", "0", []),

	("wheelbarrow", 0, "wheelbarrow", "bo_wheelbarrow", []),

	("gourd", sokf_destructible|sokf_moveable|sokf_enforce_shadows|spr_hit_points(1), "gourd", "bo_gourd", 
	[(ti_on_scene_prop_destroy,
		[
			(store_trigger_param_1, ":trigger_param_1"),
			(val_add, "$g_last_destroyed_gourds", 1),
			(prop_instance_get_position, 1, ":trigger_param_1"),
			(copy_position, 2, 1),
			(position_set_z, 2, -100000),
			(particle_system_burst, "psys_gourd_smoke", 1, 2),
			(particle_system_burst, "psys_gourd_piece_1", 1, 1),
			(particle_system_burst, "psys_gourd_piece_2", 1, 5),
			(prop_instance_animate_to_position, ":trigger_param_1", 2, 1),
			(play_sound, "snd_gourd_destroyed")
		])
	]),

	("gourd_spike", sokf_moveable, "gourd_spike", "bo_gourd_spike", []),

	("obstacle_fence_1", 0, "fence", "bo_fence", []),

	("obstacle_fallen_tree_a", 0, "destroy_tree_a", "bo_destroy_tree_a", []),

	("obstacle_fallen_tree_b", 0, "destroy_tree_b", "bo_destroy_tree_b", []),

	("siege_wall_a", 0, "siege_wall_a", "bo_siege_wall_a", []),

	("siege_large_shield_a", 0, "siege_large_shield_a", "bo_siege_large_shield_a", []),

	("granary_a", 0, "granary_a", "bo_granary_a", []),

	("small_wall_connect_a", 0, "small_wall_connect_a", "bo_small_wall_connect_a", []),

	("full_stable_a", 0, "full_stable_a", "bo_full_stable_a", []),

	("full_stable_b", 0, "full_stable_b", "bo_full_stable_b", []),

	("full_stable_c", 0, "full_stable_c", "bo_full_stable_c", []),

	("full_stable_d", 0, "full_stable_d", "bo_full_stable_d", []),

	("arabian_house_a", 0, "arabian_house_a", "bo_arabian_house_a", []),

	("arabian_house_b", 0, "arabian_house_b", "bo_arabian_house_b", []),

	("arabian_house_c", 0, "arabian_house_c", "bo_arabian_house_c", []),

	("arabian_house_d", 0, "arabian_house_d", "bo_arabian_house_d", []),

	("arabian_house_e", 0, "arabian_house_e", "bo_arabian_house_e", []),

	("arabian_house_f", 0, "arabian_house_f", "bo_arabian_house_f", []),

	("arabian_house_g", 0, "arabian_house_g", "bo_arabian_house_g", []),

	("arabian_house_h", 0, "arabian_house_h", "bo_arabian_house_h", []),

	("arabian_house_i", 0, "arabian_house_i", "bo_arabian_house_i", []),

	("arabian_square_keep_a", 0, "arabian_square_keep_a", "bo_arabian_square_keep_a", []),

	("arabian_passage_house_a", 0, "arabian_passage_house_a", "bo_arabian_passage_house_a", []),

	("arabian_wall_a", 0, "arabian_wall_a", "bo_arabian_wall_a", []),

	("arabian_wall_b", 0, "arabian_wall_b", "bo_arabian_wall_b", []),

	("arabian_ground_a", 0, "arabian_ground_a", "bo_arabian_ground_a", []),

	("arabian_parterre_a", 0, "arabian_parterre_a", "bo_arabian_parterre_a", []),

	("well_shaft", 0, "well_shaft", "bo_well_shaft", []),

	("horse_mill", 0, "horse_mill", "bo_horse_mill", []),

	("horse_mill_collar", 0, "horse_mill_collar", "bo_horse_mill_collar", []),

	("arabian_stable", 0, "arabian_stable", "bo_arabian_stable", []),

	("arabian_tent", 0, "arabian_tent", "bo_arabian_tent", []),

	("arabian_tent_b", 0, "arabian_tent_b", "bo_arabian_tent_b", []),

	("desert_plant_a", 0, "desert_plant_a", "0", []),

	("mongol_house_1", 0, "mongol_house_1", "bo_mongol_house_1", []),

	("mongol_house_2", 0, "mongol_house_2", "bo_mongol_house_2", []),

	("mongol_house_3", 0, "mongol_house_3", "bo_mongol_house_3", []),

	("mongol_house_4", 0, "mongol_house_4", "bo_mongol_house_4", []),

	("mongol_house_5", 0, "mongol_house_5", "bo_mongol_house_5", []),

	("mongol_house_6", 0, "mongol_house_6", "bo_mongol_house_6", []),

	("mongol_house_7", 0, "mongol_house_7", "bo_mongol_house_7", []),

	("arabian_castle_battlement_a", 0, "arabian_castle_battlement_a", "bo_arabian_castle_battlement_a", []),

	("arabian_castle_battlement_b_destroyed", 0, "arabian_castle_battlement_b_destroyed", "bo_arabian_castle_battlement_b_destroyed", []),

	("arabian_castle_battlement_c", 0, "arabian_castle_battlement_c", "bo_arabian_castle_battlement_c", []),

	("arabian_castle_battlement_d", 0, "arabian_castle_battlement_d", "bo_arabian_castle_battlement_d", []),

	("arabian_castle_corner_a", 0, "arabian_castle_corner_a", "bo_arabian_castle_corner_a", []),

	("arabian_castle_stairs", sokf_type_ladder, "arabian_castle_stairs", "bo_arabian_castle_stairs", []),

	("arabian_castle_stairs_b", sokf_type_ladder, "arabian_castle_stairs_b", "bo_arabian_castle_stairs_b", []),

	("arabian_castle_stairs_c", sokf_type_ladder, "arabian_castle_stairs_c", "bo_arabian_castle_stairs_c", []),

	("arabian_castle_battlement_section_a", 0, "arabian_castle_battlement_section_a", "bo_arabian_castle_battlement_section_a", []),

	("arabian_castle_gate_house_a", 0, "arabian_castle_gate_house_a", "bo_arabian_castle_gate_house_a", []),

	("arabian_castle_house_a", 0, "arabian_castle_house_a", "bo_arabian_castle_house_a", []),

	("arabian_castle_house_b", 0, "arabian_castle_house_b", "bo_arabian_castle_house_b", []),

	("arabian_castle_keep_a", 0, "arabian_castle_keep_a", "bo_arabian_castle_keep_a", []),

	("arabian_house_a2", 0, "arabian_house_a2", "bo_arabian_house_a2", []),

	("arabian_village_house_a", 0, "arabian_village_house_a", "bo_arabian_village_house_a", []),

	("arabian_village_house_b", 0, "arabian_village_house_b", "bo_arabian_village_house_b", []),

	("arabian_village_house_c", 0, "arabian_village_house_c", "bo_arabian_village_house_c", []),

	("arabian_village_house_d", 0, "arabian_village_house_d", "bo_arabian_village_house_d", []),

	("arabian_village_stable", 0, "arabian_village_stable", "bo_arabian_village_stable", []),

	("arabian_village_hut", 0, "arabian_village_hut", "bo_arabian_village_hut", []),

	("arabian_village_stairs", sokf_type_ladder, "arabian_village_stairs", "bo_arabian_village_stairs", []),

	("tree_a01", 0, "tree_a01", "bo_tree_a01", []),

	("stairs_a", sokf_type_ladder, "stairs_a", "bo_stairs_a", []),

	("headquarters_flag_red", sokf_moveable|sokf_face_player, "tutorial_flag_red", "0", []),

	("headquarters_flag_blue", sokf_moveable|sokf_face_player, "tutorial_flag_blue", "0", []),

	("headquarters_flag_gray", sokf_moveable|sokf_face_player, "tutorial_flag_yellow", "0", []),

	("headquarters_flag_red_code_only", sokf_moveable|sokf_face_player, "mp_flag_red", "0", []),

	("headquarters_flag_blue_code_only", sokf_moveable|sokf_face_player, "mp_flag_blue", "0", []),

	("headquarters_flag_gray_code_only", sokf_moveable|sokf_face_player, "mp_flag_white", "0", []),

	("headquarters_pole_code_only", sokf_moveable, "mp_flag_pole", "0", []),

	("headquarters_flag_swadian", sokf_moveable|sokf_face_player, "flag_swadian", "0", []),

	("headquarters_flag_vaegir", sokf_moveable|sokf_face_player, "flag_vaegir", "0", []),

	("headquarters_flag_khergit", sokf_moveable|sokf_face_player, "flag_khergit", "0", []),

	("headquarters_flag_nord", sokf_moveable|sokf_face_player, "flag_nord", "0", []),

	("headquarters_flag_rhodok", sokf_moveable|sokf_face_player, "flag_rhodok", "0", []),

	("headquarters_flag_sarranid", sokf_moveable|sokf_face_player, "flag_sarranid", "0", []),

	("glow_a", 0, "glow_a", "0", []),

	("glow_b", 0, "glow_b", "0", []),

	("arabian_castle_corner_b", 0, "arabian_castle_corner_b", "bo_arabian_castle_corner_b", []),

	("dummy_a_undestructable", sokf_destructible, "arena_archery_target_b", "bo_arena_archery_target_b", 
	[(ti_on_scene_prop_init,
		[
			(store_trigger_param_1, ":trigger_param_1"),
			(scene_prop_set_hit_points, ":trigger_param_1", 10000000)
		]),

		(ti_on_scene_prop_hit,
		[
			(store_trigger_param_1, ":trigger_param_1"),
			(store_trigger_param_2, ":trigger_param_2"),
			(try_begin),
				(set_fixed_point_multiplier, 1),
				(position_get_x, ":position_x_2", 2),
				(get_player_agent_no, ":player_agent_no"),
				(eq, ":player_agent_no", ":position_x_2"),
				(assign, reg60, ":trigger_param_2"),
				(display_message, "str_delivered_damage"),
				(eq, "$g_tutorial_training_ground_horseman_trainer_state", 6),
				(eq, "$g_tutorial_training_ground_horseman_trainer_completed_chapters", 1),
				(prop_instance_get_variation_id_2, ":prop_instance_variation_id_2_trigger_param_1", ":trigger_param_1"),
				(val_sub, ":prop_instance_variation_id_2_trigger_param_1", 1),
				(eq, "$g_tutorial_training_ground_current_score", ":prop_instance_variation_id_2_trigger_param_1"),
				(val_add, "$g_tutorial_training_ground_current_score", 1),
			(try_end),
			(play_sound, "snd_dummy_hit"),
			(particle_system_burst, "psys_dummy_smoke", 1, 3),
			(particle_system_burst, "psys_dummy_straw", 1, 10)
		])
	]),

	("cave_entrance_1", 0, "cave_entrance_1", "bo_cave_entrance_1", []),

	("pointer_arrow", 0, "pointer_arrow", "0", []),

	("fireplace_d_interior", 0, "fireplace_d", "bo_fireplace_d", []),

	("ship_sail_off", 0, "ship_sail_off", "bo_ship_sail_off", []),

	("ship_sail_off_b", 0, "ship_sail_off_b", "bo_ship_sail_off", []),

	("ship_c_sail_off", 0, "ship_c_sail_off", "bo_ship_c_sail_off", []),

	("ramp_small_a", 0, "ramp_small_a", "bo_ramp_small_a", []),

	("castle_g_battlement_b", 0, "castle_g_battlement_b", "bo_castle_g_battlement_b", []),

	("box_a_dynamic", sokf_moveable|sokf_dynamic_physics, "box_a", "bo_box_a", []),

	("desert_field", 0, "desert_field", "bo_desert_field", []),

	("water_river", 0, "water_plane", "0", []),

	("viking_house_a", 0, "viking_house_a", "bo_viking_house_a", []),

	("viking_house_b", 0, "viking_house_b", "bo_viking_house_b", []),

	("viking_house_c", 0, "viking_house_c", "bo_viking_house_c", []),

	("viking_house_d", 0, "viking_house_d", "bo_viking_house_d", []),

	("viking_house_e", 0, "viking_house_e", "bo_viking_house_e", []),

	("viking_stable_a", 0, "viking_stable_a", "bo_viking_stable_a", []),

	("viking_keep", 0, "viking_keep", "bo_viking_keep", []),

	("viking_house_c_destroy", 0, "viking_house_c_destroy", "bo_viking_house_c_destroy", []),

	("viking_house_b_destroy", 0, "viking_house_b_destroy", "bo_viking_house_b_destroy", []),

	("harbour_a", 0, "harbour_a", "bo_harbour_a", []),

	("sea_foam_a", 0, "0", "0", 
	[(ti_on_scene_prop_init,
		[
			(particle_system_add_new, "psys_sea_foam_a")
		])
	]),

	("viking_keep_destroy", 0, "viking_keep_destroy", "bo_viking_keep_destroy", []),

	("viking_keep_destroy_door", 0, "viking_keep_destroy_door", "bo_viking_keep_destroy_door", []),

	("earth_tower_small_b", 0, "earth_tower_small_b", "bo_earth_tower_small_b", []),

	("earth_gate_house_b", 0, "earth_gate_house_b", "bo_earth_gate_house_b", []),

	("earth_tower_a", 0, "earth_tower_a", "bo_earth_tower_a", []),

	("earth_stairs_c", 0, "earth_stairs_c", "bo_earth_stairs_c", []),

	("earth_sally_gate_left", sokf_show_hit_point_bar|sokf_destructible|sokf_moveable, "earth_sally_gate_left", "bo_earth_sally_gate_left", 
	[(ti_on_scene_prop_use,
		[
			(store_trigger_param_1, ":trigger_param_1"),
			(store_trigger_param_2, ":trigger_param_2"),
			(agent_get_position, 1, ":trigger_param_1"),
			(prop_instance_get_starting_position, 2, ":trigger_param_2"),
			(scene_prop_get_slot, ":scene_prop_slot_trigger_param_2_scene_prop_open_or_close_slot", ":trigger_param_2", slot_scene_prop_open_or_close_slot),
			(try_begin),
				(prop_instance_get_scene_prop_kind, ":prop_instance_scene_prop_kind_trigger_param_2", ":trigger_param_2"),
				(assign, ":value", 0),
				(try_begin),
					(neq, ":prop_instance_scene_prop_kind_trigger_param_2", "spr_viking_keep_destroy_sally_door_right"),
					(neq, ":prop_instance_scene_prop_kind_trigger_param_2", "spr_viking_keep_destroy_sally_door_left"),
					(neq, ":prop_instance_scene_prop_kind_trigger_param_2", "spr_earth_sally_gate_right"),
					(neq, ":prop_instance_scene_prop_kind_trigger_param_2", "spr_earth_sally_gate_left"),
					(position_is_behind_position, 1, 2),
					(assign, ":value", 1),
				(else_try),
					(this_or_next|eq, ":prop_instance_scene_prop_kind_trigger_param_2", "spr_viking_keep_destroy_sally_door_right"),
					(this_or_next|eq, ":prop_instance_scene_prop_kind_trigger_param_2", "spr_viking_keep_destroy_sally_door_left"),
					(this_or_next|eq, ":prop_instance_scene_prop_kind_trigger_param_2", "spr_earth_sally_gate_right"),
					(eq, ":prop_instance_scene_prop_kind_trigger_param_2", "spr_earth_sally_gate_left"),
					(neg|position_is_behind_position, 1, 2),
					(assign, ":value", 1),
				(try_end),
				(this_or_next|eq, ":value", 1),
				(eq, ":scene_prop_slot_trigger_param_2_scene_prop_open_or_close_slot", 1),
				(try_begin),
					(call_script, "script_use_item", ":trigger_param_2", ":trigger_param_1"),
					(get_max_players, ":max_players"),
					(try_for_range, ":number", 1, ":max_players"),
						(player_is_active, ":number"),
						(multiplayer_send_2_int_to_player, ":number", 76, ":trigger_param_2", ":trigger_param_1"),
					(try_end),
				(try_end),
			(try_end)
		]),

		(ti_on_scene_prop_init,
		[
			(store_trigger_param_1, ":trigger_param_1"),
			(scene_prop_set_hit_points, ":trigger_param_1", 2000)
		]),

		(ti_on_scene_prop_destroy,
		[
			(play_sound, "snd_dummy_destroyed"),
			(assign, ":var_1", 86),
			(try_begin),
				(this_or_next|multiplayer_is_server),
				(neg|game_in_multiplayer_mode),
				(store_trigger_param_1, ":trigger_param_1"),
				(store_trigger_param_2, ":trigger_param_2"),
				(set_fixed_point_multiplier, 100),
				(prop_instance_get_position, 1, ":trigger_param_1"),
				(try_begin),
					(ge, ":trigger_param_2", 0),
					(agent_get_position, 2, ":trigger_param_2"),
					(try_begin),
						(position_is_behind_position, 2, 1),
						(val_mul, ":var_1", -1),
					(try_end),
				(try_end),
				(init_position, 3),
				(try_begin),
					(ge, ":var_1", 0),
					(position_move_y, 3, -100),
				(else_try),
					(position_move_y, 3, 100),
				(try_end),
				(position_move_x, 3, -50),
				(position_transform_position_to_parent, 4, 1, 3),
				(position_move_z, 4, 100),
				(position_get_distance_to_ground_level, ":position_distance_to_ground_level_4", 4),
				(val_sub, ":position_distance_to_ground_level_4", 100),
				(assign, ":var_5", ":position_distance_to_ground_level_4"),
				(val_div, ":var_5", 3),
				(try_begin),
					(ge, ":var_1", 0),
					(val_add, ":var_1", ":var_5"),
				(else_try),
					(val_sub, ":var_1", ":var_5"),
				(try_end),
				(position_rotate_x, 1, ":var_1"),
				(prop_instance_animate_to_position, ":trigger_param_1", 1, 70),
			(try_end)
		]),

		(ti_on_scene_prop_hit,
		[
			(store_trigger_param_1, ":trigger_param_1"),
			(store_trigger_param_2, ":trigger_param_2"),
			(try_begin),
				(scene_prop_get_hit_points, ":scene_prop_hit_points_trigger_param_1", ":trigger_param_1"),
				(val_sub, ":scene_prop_hit_points_trigger_param_1", ":trigger_param_2"),
				(gt, ":scene_prop_hit_points_trigger_param_1", 0),
				(play_sound, "snd_dummy_hit"),
			(else_try),
				(neg|multiplayer_is_server),
				(play_sound, "snd_dummy_destroyed"),
			(try_end),
			(try_begin),
				(this_or_next|multiplayer_is_server),
				(neg|game_in_multiplayer_mode),
				(particle_system_burst, "psys_dummy_smoke", 1, 3),
				(particle_system_burst, "psys_dummy_straw", 1, 10),
			(try_end)
		])
	]),

	("earth_sally_gate_right", sokf_show_hit_point_bar|sokf_destructible|sokf_moveable, "earth_sally_gate_right", "bo_earth_sally_gate_right", 
	[(ti_on_scene_prop_use,
		[
			(store_trigger_param_1, ":trigger_param_1"),
			(store_trigger_param_2, ":trigger_param_2"),
			(agent_get_position, 1, ":trigger_param_1"),
			(prop_instance_get_starting_position, 2, ":trigger_param_2"),
			(scene_prop_get_slot, ":scene_prop_slot_trigger_param_2_scene_prop_open_or_close_slot", ":trigger_param_2", slot_scene_prop_open_or_close_slot),
			(try_begin),
				(prop_instance_get_scene_prop_kind, ":prop_instance_scene_prop_kind_trigger_param_2", ":trigger_param_2"),
				(assign, ":value", 0),
				(try_begin),
					(neq, ":prop_instance_scene_prop_kind_trigger_param_2", "spr_viking_keep_destroy_sally_door_right"),
					(neq, ":prop_instance_scene_prop_kind_trigger_param_2", "spr_viking_keep_destroy_sally_door_left"),
					(neq, ":prop_instance_scene_prop_kind_trigger_param_2", "spr_earth_sally_gate_right"),
					(neq, ":prop_instance_scene_prop_kind_trigger_param_2", "spr_earth_sally_gate_left"),
					(position_is_behind_position, 1, 2),
					(assign, ":value", 1),
				(else_try),
					(this_or_next|eq, ":prop_instance_scene_prop_kind_trigger_param_2", "spr_viking_keep_destroy_sally_door_right"),
					(this_or_next|eq, ":prop_instance_scene_prop_kind_trigger_param_2", "spr_viking_keep_destroy_sally_door_left"),
					(this_or_next|eq, ":prop_instance_scene_prop_kind_trigger_param_2", "spr_earth_sally_gate_right"),
					(eq, ":prop_instance_scene_prop_kind_trigger_param_2", "spr_earth_sally_gate_left"),
					(neg|position_is_behind_position, 1, 2),
					(assign, ":value", 1),
				(try_end),
				(this_or_next|eq, ":value", 1),
				(eq, ":scene_prop_slot_trigger_param_2_scene_prop_open_or_close_slot", 1),
				(try_begin),
					(call_script, "script_use_item", ":trigger_param_2", ":trigger_param_1"),
					(get_max_players, ":max_players"),
					(try_for_range, ":number", 1, ":max_players"),
						(player_is_active, ":number"),
						(multiplayer_send_2_int_to_player, ":number", 76, ":trigger_param_2", ":trigger_param_1"),
					(try_end),
				(try_end),
			(try_end)
		]),

		(ti_on_scene_prop_init,
		[
			(store_trigger_param_1, ":trigger_param_1"),
			(scene_prop_set_hit_points, ":trigger_param_1", 2000)
		]),

		(ti_on_scene_prop_destroy,
		[
			(play_sound, "snd_dummy_destroyed"),
			(assign, ":var_1", 86),
			(try_begin),
				(this_or_next|multiplayer_is_server),
				(neg|game_in_multiplayer_mode),
				(store_trigger_param_1, ":trigger_param_1"),
				(store_trigger_param_2, ":trigger_param_2"),
				(set_fixed_point_multiplier, 100),
				(prop_instance_get_position, 1, ":trigger_param_1"),
				(try_begin),
					(ge, ":trigger_param_2", 0),
					(agent_get_position, 2, ":trigger_param_2"),
					(try_begin),
						(position_is_behind_position, 2, 1),
						(val_mul, ":var_1", -1),
					(try_end),
				(try_end),
				(init_position, 3),
				(try_begin),
					(ge, ":var_1", 0),
					(position_move_y, 3, -100),
				(else_try),
					(position_move_y, 3, 100),
				(try_end),
				(position_move_x, 3, -50),
				(position_transform_position_to_parent, 4, 1, 3),
				(position_move_z, 4, 100),
				(position_get_distance_to_ground_level, ":position_distance_to_ground_level_4", 4),
				(val_sub, ":position_distance_to_ground_level_4", 100),
				(assign, ":var_5", ":position_distance_to_ground_level_4"),
				(val_div, ":var_5", 3),
				(try_begin),
					(ge, ":var_1", 0),
					(val_add, ":var_1", ":var_5"),
				(else_try),
					(val_sub, ":var_1", ":var_5"),
				(try_end),
				(position_rotate_x, 1, ":var_1"),
				(prop_instance_animate_to_position, ":trigger_param_1", 1, 70),
			(try_end)
		]),

		(ti_on_scene_prop_hit,
		[
			(store_trigger_param_1, ":trigger_param_1"),
			(store_trigger_param_2, ":trigger_param_2"),
			(try_begin),
				(scene_prop_get_hit_points, ":scene_prop_hit_points_trigger_param_1", ":trigger_param_1"),
				(val_sub, ":scene_prop_hit_points_trigger_param_1", ":trigger_param_2"),
				(gt, ":scene_prop_hit_points_trigger_param_1", 0),
				(play_sound, "snd_dummy_hit"),
			(else_try),
				(neg|multiplayer_is_server),
				(play_sound, "snd_dummy_destroyed"),
			(try_end),
			(try_begin),
				(this_or_next|multiplayer_is_server),
				(neg|game_in_multiplayer_mode),
				(particle_system_burst, "psys_dummy_smoke", 1, 3),
				(particle_system_burst, "psys_dummy_straw", 1, 10),
			(try_end)
		])
	]),

	("barrier_box", sokf_type_barrier3d|sokf_invisible, "barrier_box", "bo_barrier_box", []),

	("barrier_capsule", sokf_type_barrier3d|sokf_invisible, "barrier_capsule", "bo_barrier_capsule", []),

	("barrier_cone", sokf_type_barrier3d|sokf_invisible, "barrier_cone", "bo_barrier_cone", []),

	("barrier_sphere", sokf_type_barrier3d|sokf_invisible, "barrier_sphere", "bo_barrier_sphere", []),

	("viking_keep_destroy_sally_door_right", sokf_show_hit_point_bar|sokf_destructible|sokf_moveable, "viking_keep_destroy_sally_door_right", "bo_viking_keep_destroy_sally_door_right", 
	[(ti_on_scene_prop_use,
		[
			(store_trigger_param_1, ":trigger_param_1"),
			(store_trigger_param_2, ":trigger_param_2"),
			(agent_get_position, 1, ":trigger_param_1"),
			(prop_instance_get_starting_position, 2, ":trigger_param_2"),
			(scene_prop_get_slot, ":scene_prop_slot_trigger_param_2_scene_prop_open_or_close_slot", ":trigger_param_2", slot_scene_prop_open_or_close_slot),
			(try_begin),
				(prop_instance_get_scene_prop_kind, ":prop_instance_scene_prop_kind_trigger_param_2", ":trigger_param_2"),
				(assign, ":value", 0),
				(try_begin),
					(neq, ":prop_instance_scene_prop_kind_trigger_param_2", "spr_viking_keep_destroy_sally_door_right"),
					(neq, ":prop_instance_scene_prop_kind_trigger_param_2", "spr_viking_keep_destroy_sally_door_left"),
					(neq, ":prop_instance_scene_prop_kind_trigger_param_2", "spr_earth_sally_gate_right"),
					(neq, ":prop_instance_scene_prop_kind_trigger_param_2", "spr_earth_sally_gate_left"),
					(position_is_behind_position, 1, 2),
					(assign, ":value", 1),
				(else_try),
					(this_or_next|eq, ":prop_instance_scene_prop_kind_trigger_param_2", "spr_viking_keep_destroy_sally_door_right"),
					(this_or_next|eq, ":prop_instance_scene_prop_kind_trigger_param_2", "spr_viking_keep_destroy_sally_door_left"),
					(this_or_next|eq, ":prop_instance_scene_prop_kind_trigger_param_2", "spr_earth_sally_gate_right"),
					(eq, ":prop_instance_scene_prop_kind_trigger_param_2", "spr_earth_sally_gate_left"),
					(neg|position_is_behind_position, 1, 2),
					(assign, ":value", 1),
				(try_end),
				(this_or_next|eq, ":value", 1),
				(eq, ":scene_prop_slot_trigger_param_2_scene_prop_open_or_close_slot", 1),
				(try_begin),
					(call_script, "script_use_item", ":trigger_param_2", ":trigger_param_1"),
					(get_max_players, ":max_players"),
					(try_for_range, ":number", 1, ":max_players"),
						(player_is_active, ":number"),
						(multiplayer_send_2_int_to_player, ":number", 76, ":trigger_param_2", ":trigger_param_1"),
					(try_end),
				(try_end),
			(try_end)
		]),

		(ti_on_scene_prop_init,
		[
			(store_trigger_param_1, ":trigger_param_1"),
			(scene_prop_set_hit_points, ":trigger_param_1", 3000)
		]),

		(ti_on_scene_prop_destroy,
		[
			(play_sound, "snd_dummy_destroyed"),
			(assign, ":var_1", 86),
			(try_begin),
				(this_or_next|multiplayer_is_server),
				(neg|game_in_multiplayer_mode),
				(store_trigger_param_1, ":trigger_param_1"),
				(store_trigger_param_2, ":trigger_param_2"),
				(set_fixed_point_multiplier, 100),
				(prop_instance_get_position, 1, ":trigger_param_1"),
				(try_begin),
					(ge, ":trigger_param_2", 0),
					(agent_get_position, 2, ":trigger_param_2"),
					(try_begin),
						(position_is_behind_position, 2, 1),
						(val_mul, ":var_1", -1),
					(try_end),
				(try_end),
				(init_position, 3),
				(try_begin),
					(ge, ":var_1", 0),
					(position_move_y, 3, -100),
				(else_try),
					(position_move_y, 3, 100),
				(try_end),
				(position_move_x, 3, -50),
				(position_transform_position_to_parent, 4, 1, 3),
				(position_move_z, 4, 100),
				(position_get_distance_to_ground_level, ":position_distance_to_ground_level_4", 4),
				(val_sub, ":position_distance_to_ground_level_4", 100),
				(assign, ":var_5", ":position_distance_to_ground_level_4"),
				(val_div, ":var_5", 3),
				(try_begin),
					(ge, ":var_1", 0),
					(val_add, ":var_1", ":var_5"),
				(else_try),
					(val_sub, ":var_1", ":var_5"),
				(try_end),
				(position_rotate_x, 1, ":var_1"),
				(prop_instance_animate_to_position, ":trigger_param_1", 1, 70),
			(try_end)
		]),

		(ti_on_scene_prop_hit,
		[
			(store_trigger_param_1, ":trigger_param_1"),
			(store_trigger_param_2, ":trigger_param_2"),
			(try_begin),
				(scene_prop_get_hit_points, ":scene_prop_hit_points_trigger_param_1", ":trigger_param_1"),
				(val_sub, ":scene_prop_hit_points_trigger_param_1", ":trigger_param_2"),
				(gt, ":scene_prop_hit_points_trigger_param_1", 0),
				(play_sound, "snd_dummy_hit"),
			(else_try),
				(neg|multiplayer_is_server),
				(play_sound, "snd_dummy_destroyed"),
			(try_end),
			(try_begin),
				(this_or_next|multiplayer_is_server),
				(neg|game_in_multiplayer_mode),
				(particle_system_burst, "psys_dummy_smoke", 1, 3),
				(particle_system_burst, "psys_dummy_straw", 1, 10),
			(try_end)
		])
	]),

	("viking_keep_destroy_sally_door_left", sokf_show_hit_point_bar|sokf_destructible|sokf_moveable, "viking_keep_destroy_sally_door_left", "bo_viking_keep_destroy_sally_door_left", 
	[(ti_on_scene_prop_use,
		[
			(store_trigger_param_1, ":trigger_param_1"),
			(store_trigger_param_2, ":trigger_param_2"),
			(agent_get_position, 1, ":trigger_param_1"),
			(prop_instance_get_starting_position, 2, ":trigger_param_2"),
			(scene_prop_get_slot, ":scene_prop_slot_trigger_param_2_scene_prop_open_or_close_slot", ":trigger_param_2", slot_scene_prop_open_or_close_slot),
			(try_begin),
				(prop_instance_get_scene_prop_kind, ":prop_instance_scene_prop_kind_trigger_param_2", ":trigger_param_2"),
				(assign, ":value", 0),
				(try_begin),
					(neq, ":prop_instance_scene_prop_kind_trigger_param_2", "spr_viking_keep_destroy_sally_door_right"),
					(neq, ":prop_instance_scene_prop_kind_trigger_param_2", "spr_viking_keep_destroy_sally_door_left"),
					(neq, ":prop_instance_scene_prop_kind_trigger_param_2", "spr_earth_sally_gate_right"),
					(neq, ":prop_instance_scene_prop_kind_trigger_param_2", "spr_earth_sally_gate_left"),
					(position_is_behind_position, 1, 2),
					(assign, ":value", 1),
				(else_try),
					(this_or_next|eq, ":prop_instance_scene_prop_kind_trigger_param_2", "spr_viking_keep_destroy_sally_door_right"),
					(this_or_next|eq, ":prop_instance_scene_prop_kind_trigger_param_2", "spr_viking_keep_destroy_sally_door_left"),
					(this_or_next|eq, ":prop_instance_scene_prop_kind_trigger_param_2", "spr_earth_sally_gate_right"),
					(eq, ":prop_instance_scene_prop_kind_trigger_param_2", "spr_earth_sally_gate_left"),
					(neg|position_is_behind_position, 1, 2),
					(assign, ":value", 1),
				(try_end),
				(this_or_next|eq, ":value", 1),
				(eq, ":scene_prop_slot_trigger_param_2_scene_prop_open_or_close_slot", 1),
				(try_begin),
					(call_script, "script_use_item", ":trigger_param_2", ":trigger_param_1"),
					(get_max_players, ":max_players"),
					(try_for_range, ":number", 1, ":max_players"),
						(player_is_active, ":number"),
						(multiplayer_send_2_int_to_player, ":number", 76, ":trigger_param_2", ":trigger_param_1"),
					(try_end),
				(try_end),
			(try_end)
		]),

		(ti_on_scene_prop_init,
		[
			(store_trigger_param_1, ":trigger_param_1"),
			(scene_prop_set_hit_points, ":trigger_param_1", 3000)
		]),

		(ti_on_scene_prop_destroy,
		[
			(play_sound, "snd_dummy_destroyed"),
			(assign, ":var_1", 86),
			(try_begin),
				(this_or_next|multiplayer_is_server),
				(neg|game_in_multiplayer_mode),
				(store_trigger_param_1, ":trigger_param_1"),
				(store_trigger_param_2, ":trigger_param_2"),
				(set_fixed_point_multiplier, 100),
				(prop_instance_get_position, 1, ":trigger_param_1"),
				(try_begin),
					(ge, ":trigger_param_2", 0),
					(agent_get_position, 2, ":trigger_param_2"),
					(try_begin),
						(position_is_behind_position, 2, 1),
						(val_mul, ":var_1", -1),
					(try_end),
				(try_end),
				(init_position, 3),
				(try_begin),
					(ge, ":var_1", 0),
					(position_move_y, 3, -100),
				(else_try),
					(position_move_y, 3, 100),
				(try_end),
				(position_move_x, 3, -50),
				(position_transform_position_to_parent, 4, 1, 3),
				(position_move_z, 4, 100),
				(position_get_distance_to_ground_level, ":position_distance_to_ground_level_4", 4),
				(val_sub, ":position_distance_to_ground_level_4", 100),
				(assign, ":var_5", ":position_distance_to_ground_level_4"),
				(val_div, ":var_5", 3),
				(try_begin),
					(ge, ":var_1", 0),
					(val_add, ":var_1", ":var_5"),
				(else_try),
					(val_sub, ":var_1", ":var_5"),
				(try_end),
				(position_rotate_x, 1, ":var_1"),
				(prop_instance_animate_to_position, ":trigger_param_1", 1, 70),
			(try_end)
		]),

		(ti_on_scene_prop_hit,
		[
			(store_trigger_param_1, ":trigger_param_1"),
			(store_trigger_param_2, ":trigger_param_2"),
			(try_begin),
				(scene_prop_get_hit_points, ":scene_prop_hit_points_trigger_param_1", ":trigger_param_1"),
				(val_sub, ":scene_prop_hit_points_trigger_param_1", ":trigger_param_2"),
				(gt, ":scene_prop_hit_points_trigger_param_1", 0),
				(play_sound, "snd_dummy_hit"),
			(else_try),
				(neg|multiplayer_is_server),
				(play_sound, "snd_dummy_destroyed"),
			(try_end),
			(try_begin),
				(this_or_next|multiplayer_is_server),
				(neg|game_in_multiplayer_mode),
				(particle_system_burst, "psys_dummy_smoke", 1, 3),
				(particle_system_burst, "psys_dummy_straw", 1, 10),
			(try_end)
		])
	]),

	("castle_f_door_b", sokf_show_hit_point_bar|sokf_destructible|sokf_moveable, "castle_e_sally_door_a", "bo_castle_e_sally_door_a", 
	[(ti_on_scene_prop_use,
		[
			(store_trigger_param_1, ":trigger_param_1"),
			(store_trigger_param_2, ":trigger_param_2"),
			(agent_get_position, 1, ":trigger_param_1"),
			(prop_instance_get_starting_position, 2, ":trigger_param_2"),
			(scene_prop_get_slot, ":scene_prop_slot_trigger_param_2_scene_prop_open_or_close_slot", ":trigger_param_2", slot_scene_prop_open_or_close_slot),
			(try_begin),
				(ge, ":trigger_param_1", 0),
				(agent_get_team, ":team_trigger_param_1", ":trigger_param_1"),
				(this_or_next|eq, ":team_trigger_param_1", 0),
				(eq, ":scene_prop_slot_trigger_param_2_scene_prop_open_or_close_slot", 1),
				(try_begin),
					(call_script, "script_use_item", ":trigger_param_2", ":trigger_param_1"),
					(get_max_players, ":max_players"),
					(try_for_range, ":number", 1, ":max_players"),
						(player_is_active, ":number"),
						(multiplayer_send_2_int_to_player, ":number", 76, ":trigger_param_2", ":trigger_param_1"),
					(try_end),
				(try_end),
			(try_end)
		]),

		(ti_on_scene_prop_init,
		[
			(store_trigger_param_1, ":trigger_param_1"),
			(scene_prop_set_hit_points, ":trigger_param_1", 1000)
		]),

		(ti_on_scene_prop_destroy,
		[
			(play_sound, "snd_dummy_destroyed"),
			(assign, ":var_1", 86),
			(try_begin),
				(this_or_next|multiplayer_is_server),
				(neg|game_in_multiplayer_mode),
				(store_trigger_param_1, ":trigger_param_1"),
				(store_trigger_param_2, ":trigger_param_2"),
				(set_fixed_point_multiplier, 100),
				(prop_instance_get_position, 1, ":trigger_param_1"),
				(try_begin),
					(ge, ":trigger_param_2", 0),
					(agent_get_position, 2, ":trigger_param_2"),
					(try_begin),
						(position_is_behind_position, 2, 1),
						(val_mul, ":var_1", -1),
					(try_end),
				(try_end),
				(init_position, 3),
				(try_begin),
					(ge, ":var_1", 0),
					(position_move_y, 3, -100),
				(else_try),
					(position_move_y, 3, 100),
				(try_end),
				(position_move_x, 3, -50),
				(position_transform_position_to_parent, 4, 1, 3),
				(position_move_z, 4, 100),
				(position_get_distance_to_ground_level, ":position_distance_to_ground_level_4", 4),
				(val_sub, ":position_distance_to_ground_level_4", 100),
				(assign, ":var_5", ":position_distance_to_ground_level_4"),
				(val_div, ":var_5", 3),
				(try_begin),
					(ge, ":var_1", 0),
					(val_add, ":var_1", ":var_5"),
				(else_try),
					(val_sub, ":var_1", ":var_5"),
				(try_end),
				(position_rotate_x, 1, ":var_1"),
				(prop_instance_animate_to_position, ":trigger_param_1", 1, 70),
			(try_end)
		]),

		(ti_on_scene_prop_hit,
		[
			(store_trigger_param_1, ":trigger_param_1"),
			(store_trigger_param_2, ":trigger_param_2"),
			(try_begin),
				(scene_prop_get_hit_points, ":scene_prop_hit_points_trigger_param_1", ":trigger_param_1"),
				(val_sub, ":scene_prop_hit_points_trigger_param_1", ":trigger_param_2"),
				(gt, ":scene_prop_hit_points_trigger_param_1", 0),
				(play_sound, "snd_dummy_hit"),
			(else_try),
				(neg|multiplayer_is_server),
				(play_sound, "snd_dummy_destroyed"),
			(try_end),
			(try_begin),
				(this_or_next|multiplayer_is_server),
				(neg|game_in_multiplayer_mode),
				(particle_system_burst, "psys_dummy_smoke", 1, 3),
				(particle_system_burst, "psys_dummy_straw", 1, 10),
			(try_end)
		])
	]),

	("ctf_flag_kingdom_1", sokf_moveable|sokf_face_player, "ctf_flag_kingdom_1", "0", []),

	("ctf_flag_kingdom_2", sokf_moveable|sokf_face_player, "ctf_flag_kingdom_2", "0", []),

	("ctf_flag_kingdom_3", sokf_moveable|sokf_face_player, "ctf_flag_kingdom_3", "0", []),

	("ctf_flag_kingdom_4", sokf_moveable|sokf_face_player, "ctf_flag_kingdom_4", "0", []),

	("ctf_flag_kingdom_5", sokf_moveable|sokf_face_player, "ctf_flag_kingdom_5", "0", []),

	("ctf_flag_kingdom_6", sokf_moveable|sokf_face_player, "ctf_flag_kingdom_6", "0", []),

	("ctf_flag_kingdom_7", sokf_moveable|sokf_face_player, "ctf_flag_kingdom_7", "0", []),

	("headquarters_flag_rebel", sokf_moveable|sokf_face_player, "flag_rebel", "0", []),

	("arabian_lighthouse_a", 0, "arabian_lighthouse_a", "bo_arabian_lighthouse_a", []),

	("arabian_ramp_a", 0, "arabian_ramp_a", "bo_arabian_ramp_a", []),

	("arabian_ramp_b", 0, "arabian_ramp_b", "bo_arabian_ramp_b", []),

	("winery_interior", 0, "winery_interior", "bo_winery_interior", []),

	("winery_barrel_shelf", 0, "winery_barrel_shelf", "bo_winery_barrel_shelf", []),

	("winery_wall_shelf", 0, "winery_wall_shelf", "bo_winery_wall_shelf", []),

	("winery_huge_barrel", 0, "winery_huge_barrel", "bo_winery_huge_barrel", []),

	("winery_wine_press", 0, "winery_wine_press", "bo_winery_wine_press", []),

	("winery_middle_barrel", 0, "winery_middle_barrel", "bo_winery_middle_barrel", []),

	("winery_wine_cart_small_loaded", 0, "winery_wine_cart_small_loaded", "bo_winery_wine_cart_small_loaded", []),

	("winery_wine_cart_small_empty", 0, "winery_wine_cart_small_empty", "bo_winery_wine_cart_small_empty", []),

	("winery_wine_cart_empty", 0, "winery_wine_cart_empty", "bo_winery_wine_cart_empty", []),

	("winery_wine_cart_loaded", 0, "winery_wine_cart_loaded", "bo_winery_wine_cart_loaded", []),

	("weavery_interior", 0, "weavery_interior", "bo_weavery_interior", []),

	("weavery_loom_a", 0, "weavery_loom_a", "bo_weavery_loom_a", []),

	("weavery_spinning_wheel", 0, "weavery_spinning_wheel", "bo_weavery_spinning_wheel", []),

	("mill_interior", 0, "mill_interior", "bo_mill_interior", []),

	("mill_flour_sack", 0, "mill_flour_sack", "bo_mill_flour_sack", []),

	("mill_flour_sack_desk_a", 0, "mill_flour_sack_desk_a", "bo_mill_flour_sack_desk_a", []),

	("mill_flour_sack_desk_b", 0, "mill_flour_sack_desk_b", "bo_mill_flour_sack_desk_b", []),

	("smithy_interior", 0, "smithy_interior", "bo_smithy_interior", []),

	("smithy_grindstone_wheel", 0, "smithy_grindstone_wheel", "bo_smithy_grindstone_wheel", []),

	("smithy_forge_bellows", 0, "smithy_forge_bellows", "bo_smithy_forge_bellows", []),

	("smithy_forge", 0, "smithy_forge", "bo_smithy_forge", []),

	("smithy_anvil", 0, "smithy_anvil", "bo_smithy_anvil", []),

	("tannery_hide_a", 0, "tannery_hide_a", "bo_tannery_hide_a", []),

	("tannery_hide_b", 0, "tannery_hide_b", "bo_tannery_hide_b", []),

	("tannery_pools_a", 0, "tannery_pools_a", "bo_tannery_pools_a", []),

	("tannery_pools_b", 0, "tannery_pools_b", "bo_tannery_pools_b", []),

	("fountain", 0, "fountain", "bo_fountain", []),

	("rhodok_houses_a", 0, "rhodok_houses_a", "bo_rhodok_houses_a", []),

	("rhodok_houses_b", 0, "rhodok_houses_b", "bo_rhodok_houses_b", []),

	("rhodok_houses_c", 0, "rhodok_houses_c", "bo_rhodok_houses_c", []),

	("rhodok_houses_d", 0, "rhodok_houses_d", "bo_rhodok_houses_d", []),

	("rhodok_houses_e", 0, "rhodok_houses_e", "bo_rhodok_houses_e", []),

	("rhodok_house_passage_a", 0, "rhodok_house_passage_a", "bo_rhodok_house_passage_a", []),

	("bridge_b", 0, "bridge_b", "bo_bridge_b", []),

	("brewery_pool", 0, "brewery_pool", "bo_brewery_pool", []),

	("brewery_big_bucket", 0, "brewery_big_bucket", "bo_brewery_big_bucket", []),

	("brewery_interior", 0, "brewery_interior", "bo_brewery_interior", []),

	("brewery_bucket_platform_a", 0, "brewery_bucket_platform_a", "bo_brewery_bucket_platform_a", []),

	("brewery_bucket_platform_b", 0, "brewery_bucket_platform_b", "bo_brewery_bucket_platform_b", []),

	("weavery_dye_pool_r", 0, "weavery_dye_pool_r", "bo_weavery_dye_pool_r", []),

	("weavery_dye_pool_y", 0, "weavery_dye_pool_y", "bo_weavery_dye_pool_y", []),

	("weavery_dye_pool_b", 0, "weavery_dye_pool_b", "bo_weavery_dye_pool_b", []),

	("weavery_dye_pool_p", 0, "weavery_dye_pool_p", "bo_weavery_dye_pool_p", []),

	("weavery_dye_pool_g", 0, "weavery_dye_pool_g", "bo_weavery_dye_pool_g", []),

	("oil_press_interior", 0, "oil_press_interior", "bo_oil_press_interior", []),

	("city_swad_01", 0, "city_swad_01", "bo_city_swad_01", []),

	("city_swad_02", 0, "city_swad_02", "bo_city_swad_02", []),

	("city_swad_03", 0, "city_swad_03", "bo_city_swad_03", []),

	("city_swad_04", 0, "city_swad_04", "bo_city_swad_04", []),

	("city_swad_passage_01", 0, "city_swad_passage_01", "bo_city_swad_passage_01", []),

	("city_swad_05", 0, "city_swad_05", "bo_city_swad_05", []),

	("arena_block_j_a", 0, "arena_block_j_a", "bo_arena_block_j_a", []),

	("arena_underway_a", 0, "arena_underway_a", "bo_arena_underway_a", []),

	("arena_circle_a", 0, "arena_circle_a", "bo_arena_circle_a", []),

	("rope_bridge_15m", 0, "rope_bridge_15m", "bo_rope_bridge_15m", []),

	("tree_house_a", 0, "tree_house_a", "bo_tree_house_a", []),

	("tree_house_guard_a", 0, "tree_house_guard_a", "bo_tree_house_guard_a", []),

	("tree_house_guard_b", 0, "tree_house_guard_b", "bo_tree_house_guard_b", []),

	("tree_shelter_a", 0, "tree_shelter_a", "bo_tree_shelter_a", []),

	("yellow_fall_leafs_a", 0, "0", "0", 
	[(ti_on_scene_prop_init,
		[
			(particle_system_add_new, "psys_fall_leafs_a")
		])
	]),

	("buttress_2stp_large_a", 0, "buttress_2stp_large_a", "bo_buttress_2stp_large_a", []),

	("buttress_flying_a", 0, "buttress_flying_a", "bo_buttress_flying_a", []),

	("buttress_large_a", 0, "buttress_large_a", "bo_buttress_large_a", []),

	("buttress_simple_a", 0, "buttress_simple_a", "bo_buttress_simple_a", []),

	("bell_tent", sokf_type_barrier, "mongol_house_5", "bo_mongol_house_5", []),

	("bell_tent_inventory", sokf_type_container, "mongol_house_5", "bo_mongol_house_5", []),

	("bell_tent_noinventory", 0, "mongol_house_5", "bo_mongol_house_5", []),

	("command_tent", 0, "mongol_house_6", "bo_mongol_house_6", []),

	("siege_camp_spikes", 0, "spike_group_a", "bo_spike_group_a", []),

	("siege_camp_tower", 0, "belfry_b", "bo_belfry_b", []),

	("siege_camp_bridge", 0, "belfry_platform_b", "bo_belfry_platform_b", []),

	("gutek_window_glow", 0, "torch_a", "0", 
	[(ti_on_scene_prop_init,
		[
			(is_currently_night, 0),
			(set_position_delta, 0, -40, 4),
			(particle_system_add_new, "psys_torch_fire"),
			(particle_system_add_new, "psys_torch_smoke"),
			(particle_system_add_new, "psys_torch_fire_sparks"),
			(set_position_delta, 0, -85, 56),
			(particle_system_add_new, "psys_fire_glow_1"),
			(particle_system_emit, "psys_fire_glow_1", 9000000),
			(play_sound, "snd_torch_loop", 0)
		])
	]),

	("nord_borghovdinghus", 0, "nord_borghovdinghus", "bo_nord_borghovdinghus", []),

	("nord_fyrkathouse", 0, "nord_fyrkathouse", "bo_nord_fyrkathouse", []),

	("nord_longhouse_1", 0, "nord_longhouse_1", "bo_nord_longhouse_1", []),

	("nord_lofotrinterior", 0, "nord_lofotrinterior", "bo_nord_lofotrinterior", []),

	("nord_stable", 0, "nord_stable", "bo_swadia_stable", []),

	("rhodok_gatehouse_a", 0, "rhodok_gatehouse_a", "bo_rhodok_gatehouse_a", []),

	("rhodok_keep_a", 0, "rhodok_keep_a", "bo_rhodok_keep_a", []),

	("rhodok_keep_b", 0, "rhodok_keep_b", "bo_rhodok_keep_b", []),

	("rhodok_tower_a", 0, "rhodok_tower_a", "bo_rhodok_tower_a", []),

	("rhodok_tower_b", 0, "rhodok_tower_b", "bo_rhodok_tower_b", []),

	("rhodok_tower_c", 0, "rhodok_tower_c", "bo_rhodok_tower_c", []),

	("rhodok_tower_d", 0, "rhodok_tower_d", "bo_rhodok_tower_d", []),

	("rhodok_tower_e", 0, "rhodok_tower_e", "bo_rhodok_tower_e", []),

	("rhodok_tower_f", 0, "rhodok_tower_f", "bo_rhodok_tower_f", []),

	("rhodok_tower_g", 0, "rhodok_tower_g", "bo_rhodok_tower_g", []),

	("rhodok_wall_a", 0, "rhodok_wall_a", "bo_rhodok_wall_a", []),

	("rhodok_wall_a_destroyed", 0, "rhodok_wall_a_destroyed", "bo_rhodok_wall_a_destroyed", []),

	("rhodok_wall_b", 0, "rhodok_wall_b", "bo_rhodok_wall_b", []),

	("rhodok_wall_c", 0, "rhodok_wall_c", "bo_rhodok_wall_c", []),

	("rhodok_wall_d", 0, "rhodok_wall_d", "bo_rhodok_wall_d", []),

	("rhodok_wall_d_destroyed", 0, "rhodok_wall_d_destroyed", "bo_rhodok_wall_d_destroyed", []),

	("weirwood", 0, "weirwood", "bo_weirwood", []),

	("weirwood_2", 0, "weirwood_2", "bo_weirwood_2", []),

	("weirwood_3", 0, "weirwood_3", "bo_weirwood_3", []),

	("12_french_tower", 0, "12_french_tower", "bo_12_french_tower", []),

	("12_french_tower_b", 0, "12_french_tower_b", "bo_12_french_tower_b", []),

	("french_battlement_a", 0, "french_battlement_a", "bo_french_battlement_a", []),

	("french_battlement_a_destroyed", 0, "french_battlement_a_destroyed", "bo_french_battlement_a_destroyed", []),

	("french_battlement_b", 0, "french_battlement_b", "bo_french_battlement_b", []),

	("french_battlement_c", 0, "french_battlement_c", "bo_french_battlement_c", []),

	("french_battlement_rea", 0, "french_battlement_rea", "bo_french_battlement_rea", []),

	("french_battlement_rea_destroyed", 0, "french_battlement_rea_destroyed", "bo_french_battlement_rea_destroyed", []),

	("french_corner", 0, "french_corner", "bo_french_corner", []),

	("french_corner_b", 0, "french_corner_b", "bo_french_corner_b", []),

	("french_gatehouse", 0, "french_gatehouse", "bo_french_gatehouse", []),

	("french_keep", 0, "french_keep", "bo_french_keep", []),

	("french_round_tower", 0, "french_round_tower", "bo_french_round_tower", []),

	("french_tower", 0, "french_tower", "bo_french_tower_2", []),

	("rouen_keep", 0, "rouen_keep", "bo_Rouen_keep", []),

	("Lota_Wheat", 0, "Lota_Wheat", "0", []),

	("Lota_Hedge", 0, "Lota_Hedge", "0", []),

	("Lota_Dothraki_Grass", 0, "Lota_Dothraki_Grass", "0", []),

	("Lota_Dothraki_Plants", 0, "Lota_Dothraki_Plants", "0", []),

	("banner_the_seven", 0, "banner_the_seven", "0", []),

	("flag_pole_long_1", 0, "flag_pole_long_1", "0", []),

	("flag_pole_long_2", 0, "flag_pole_long_2", "0", []),

	("flag_pole_long_3", 0, "flag_pole_long_3", "0", []),

	("flag_pole_long_4", 0, "flag_pole_long_4", "0", []),

	("flag_pole_long_5", 0, "flag_pole_long_5", "0", []),

	("ACOK_Spectator_1", 0, "nobleman_spectator_5", "0", []),

	("ACOK_Spectator_2", 0, "ACOK_Spectator_2", "0", []),

	("ACOK_Spectator_3", 0, "ACOK_Spectator_3", "0", []),

	("ACOK_Spectator_4", 0, "nobleman_spectator_4", "0", []),

	("ACOK_Spectator_5", 0, "ACOK_Spectator_5", "0", []),

	("ACOK_Spectator_6", 0, "ACOK_Spectator_6", "0", []),

	("ACOK_Spectator_7", 0, "nobleman_spectator_3", "0", []),

	("ACOK_Spectator_8", 0, "ACOK_Spectator_8", "0", []),

	("ACOK_Spectator_9", 0, "ACOK_Spectator_9", "0", []),

	("ACOK_Spectator_10", 0, "nobleman_spectator_2", "0", []),

	("ACOK_Spectator_11", 0, "ACOK_Spectator_11", "0", []),

	("ACOK_Spectator_12", 0, "ACOK_Spectator_12", "0", []),

	("ACOK_Spectator_new_1", 0, "nobleman_spectator_1", "0", []),

	("ACOK_Spectator_new_2", 0, "nobleman_spectator_2", "0", []),

	("ACOK_Spectator_new_3", 0, "nobleman_spectator_3", "0", []),

	("ACOK_Spectator_new_4", 0, "nobleman_spectator_4", "0", []),

	("ACOK_Spectator_new_5", 0, "nobleman_spectator_5", "0", []),

	("ACOK_Spectator_new_6", 0, "nobleman_spectator_6", "0", []),

	("ACOK_Spectator_new_7", 0, "nobleman_spectator_7", "0", []),

	("ACOK_Spectator_new_8", 0, "nobleman_spectator_8", "0", []),

	("mp_battlement_framework", 0, "mp_battlement_framework", "bo_mp_battlement_way", []),

	("mp_battlement_way", 0, "mp_battlement_way", "bo_mp_battlement_way", []),

	("mp_burgh_wall", 0, "mp_burgh_wall", "bo_mp_burgh_wall", []),

	("mp_burgh_wall_part_a", 0, "mp_burgh_wall_part_a", "bo_mp_burgh_wall_part_a", []),

	("mp_burgh_wall_part_b", 0, "mp_burgh_wall_part_b", "bo_mp_burgh_wall_part_b", []),

	("mp_compound_Burgh_wall", 0, "mp_compound_Burgh_wall", "bo_mp_compound_Burgh_wall", []),

	("mp_fence", 0, "mp_fence", "bo_mp_fence", []),

	("mp_gate", 0, "mp_gate", "bo_mp_gate", []),

	("mp_mound_a_turf", 0, "mp_mound_a_turf", "bo_mp_mound_a", []),

	("mp_mound_a_path", 0, "mp_mound_a_path", "bo_mp_mound_a", []),

	("mp_mound_b_turf", 0, "mp_mound_b_turf", "bo_mp_mound_b", []),

	("mp_mound_b_path", 0, "mp_mound_b_path", "bo_mp_mound_b", []),

	("mp_stage", 0, "mp_stage", "bo_mp_stage", []),

	("mp_stairs_small", 0, "mp_stairs_small", "bo_mp_stairs_small", []),

	("mp_tools_bowsaw", 0, "mp_tools_bowsaw", "bo_mp_tools_bowsaw", []),

	("mp_wall_a", 0, "mp_wall_a", "bo_mp_wall", []),

	("mp_wall_b", 0, "mp_wall_b", "bo_mp_wall", []),

	("mp_wall_horizontal_a", 0, "mp_wall_horizontal_a", "bo_mp_wall_horizontal", []),

	("mp_wall_horizontal_b", 0, "mp_wall_horizontal_b", "bo_mp_wall_horizontal", []),

	("mp_way", 0, "mp_way", "bo_mp_way", []),

	("mp_way_short", 0, "mp_way_short", "bo_mp_way_short", []),

	("cut_off_head_male", 0, "cut_off_head_male", "bo_cut_off_head_male", []),

	("cut_off_head_female", 0, "cut_off_head_female", "bo_cut_off_head_female", []),

	("tavern", 0, "tavern", "bo_tavern", []),

	("Gold_Coin", 0, "Gold_Coin", "0", []),

	("bell", 0, "bell", "0", []),

	("wall_painting_1", 0, "tapestry_1", "0", []),

	("wall_painting_2", 0, "tapestry_2", "0", []),

	("wall_painting_3", 0, "tapestry_3", "0", []),

	("wall_painting_4", 0, "tapestry_4", "0", []),

	("wall_painting_5", 0, "tapestry_5", "0", []),

	("wall_painting_6", 0, "tapestry_6", "0", []),

	("wall_painting_7", 0, "wall_painting_7", "0", []),

	("wall_painting_8", 0, "wall_painting_8", "0", []),

	("wall_painting_9", 0, "wall_painting_9", "0", []),

	("wall_painting_10", 0, "wall_painting_10", "0", []),

	("new_a_bridge_a", 0, "new_a_bridge_a", "bo_new_a_bridge_a", []),

	("new_a_bridge_b", 0, "new_a_bridge_b", "bo_new_a_bridge_b", []),

	("new_a_bridge_c", 0, "new_a_bridge_c", "bo_new_a_bridge_c", []),

	("new_a_bridge_d", 0, "new_a_bridge_d", "bo_new_a_bridge_d", []),

	("new_a_bridge_e", 0, "new_a_bridge_e", "bo_new_a_bridge_e", []),

	("new_a_bridge_f", 0, "new_a_bridge_f", "bo_new_a_bridge_f", []),

	("new_a_church_a", 0, "new_a_church_a", "bo_new_a_church_a", []),

	("new_a_church_b", 0, "new_a_church_b", "bo_new_a_church_b", []),

	("new_a_church_c", 0, "new_a_church_c", "bo_new_a_church_c", []),

	("new_a_church_d", 0, "new_a_church_a", "bo_new_a_church_d", []),

	("new_a_church_deco_a", 0, "new_a_church_deco_a", "bo_new_a_church_deco_a", []),

	("new_a_church_deco_b", 0, "new_a_church_deco_b", "bo_new_a_church_deco_b", []),

	("pr_castle_keep_a", 0, "pr_castle_keep_a", "bo_pr_castle_keep_a", []),

	("pr_castle_tower_a", 0, "pr_castle_tower_a", "bo_pr_castle_tower_a", []),

	("pr_castle_wall_a", 0, "pr_castle_wall_a", "bo_pr_castle_wall_a", []),

	("pr_church_base", 0, "pr_church_base", "bo_pr_church_base", []),

	("pr_church_stairs", 0, "pr_church_stairs", "bo_pr_church_stairs", []),

	("pr_fake_houses_a", 0, "pr_fake_houses_a", "0", []),

	("pr_farm_house_a", 0, "pr_farm_house_a", "bo_pr_farm_house_a", []),

	("pr_fountain", 0, "pr_fountain", "bo_pr_fountain", []),

	("pr_fountain_water", 0, "pr_fountain_water", "0", []),

	("pr_house_block_a", 0, "pr_house_block_a", "bo_pr_house_block_a", []),

	("pr_house_block_b", 0, "pr_house_block_b", "bo_pr_house_block_b", []),

	("pr_house_block_c", 0, "pr_house_block_c", "bo_pr_house_block_c", []),

	("pr_house_lods_a", 0, "pr_house_lods_a", "0", []),

	("pr_house_passage_a", 0, "pr_house_passage_a", "bo_pr_house_passage_a", []),

	("pr_interior_a", 0, "pr_interior_a", "bo_pr_interior_a", []),

	("pr_new_cozur_red_keep", 0, "pr_new_cozur_red_keep", "bo_pr_it_cathedral", []),

	("pr_it_cathedral", 0, "pr_it_cathedral", "bo_pr_it_cathedral", []),

	("pr_it_cathedral_campanile", 0, "pr_it_cathedral_campanile", "bo_pr_it_cathedral_campanile", []),

	("pr_it_house_a", 0, "pr_it_house_a", "bo_pr_it_house_a", []),

	("pr_it_house_a_2", 0, "pr_it_house_a_2", "bo_pr_it_house_a_2", []),

	("pr_it_house_b", 0, "pr_it_house_b", "bo_pr_it_house_b", []),

	("pr_it_house_b_2", 0, "pr_it_house_b_2", "bo_pr_it_house_b_2", []),

	("pr_it_house_c", 0, "pr_it_house_c", "bo_pr_it_house_c", []),

	("pr_it_house_d", 0, "pr_it_house_d", "bo_pr_it_house_d", []),

	("pr_it_house_e", 0, "pr_it_house_e", "bo_pr_it_house_e", []),

	("pr_it_house_f_new", 0, "pr_it_house_f_new", "bo_pr_it_house_f_new", []),

	("pr_it_house_g", 0, "pr_it_house_g", "bo_pr_it_house_g", []),

	("pr_it_house_h", 0, "pr_it_house_h", "bo_pr_it_house_h", []),

	("pr_it_house_h_2", 0, "pr_it_house_h_2", "bo_pr_it_house_h_2", []),

	("pr_it_house_i", 0, "pr_it_house_i", "bo_pr_it_house_i", []),

	("pr_it_house_j", 0, "pr_it_house_j", "bo_pr_it_house_j", []),

	("pr_it_house_k", 0, "pr_it_house_k", "bo_pr_it_house_k", []),

	("pr_it_house_l", 0, "pr_it_house_l", "bo_pr_it_house_l", []),

	("pr_it_house_m", 0, "pr_it_house_m", "bo_pr_it_house_m", []),

	("pr_it_house_n_int", 0, "pr_it_house_n_int", "bo_pr_it_house_n_int", []),

	("new_tree_a", 0, "new_tree_a", "bo_new_tree_a", []),

	("new_tree_a_double", 0, "new_tree_a_double", "bo_new_tree_a_double", []),

	("new_cypress", 0, "new_cypress", "bo_new_cypress", []),

	("new_cypress2", 0, "new_cypress2", "bo_new_cypress2", []),

	("smaug_skeleton", 0, "smaug_skeleton", "bo_smaug_skeleton", []),

	("a_altar_1", 0, "a_altar_1", "bo_a_altar_1", []),

	("a_temple_columns_1", 0, "a_temple_columns_1", "bo_a_temple_columns_1", []),

	("celtycka_chata", 0, "celtycka_chata", "bo_celtycka_chata", []),

	("arena_2", 0, "arena_2", "bo_arena_2", []),

	("small_arena", 0, "small_arena", "bo_small_arena", []),

	("stonehenge_ruined", 0, "stonehenge_ruined", "bo_stonehenge_ruined", []),

	("stonehenge_ruined_2", 0, "stonehenge_ruined_2", "bo_stonehenge_ruined_2", []),

	("stonehenge_ruined_3", 0, "stonehenge_ruined_3", "bo_stonehenge_ruined_3", []),

	("stonehenge_ruined_3_ice", 0, "stonehenge_ruined_3_ice", "bo_stonehenge_ruined_3_ice", []),

	("tree_pole_old", 0, "tree_pole_old", "bo_tree_pole_old", []),

	("tree_logs_stripped", 0, "tree_logs_stripped", "bo_tree_logs_stripped", []),

	("tree_log_big", 0, "tree_log_big", "bo_tree_log_big", []),

	("tree_log_pile", 0, "tree_log_pile", "bo_tree_log_pile", []),

	("palisade_wood", 0, "palisade_wood", "bo_palisade_wood", []),

	("iceflake", 0, "iceflake", "bo_iceflake", []),

	("iceflake_small", 0, "iceflake_small", "bo_iceflake_small", []),

	("staigue", 0, "staigue", "bo_staigue", []),

	("gold_candle_stick", 0, "gold_candle_stick", "bo_gold_candle_stick", []),

	("gold_candle_stick_large", 0, "gold_candle_stick_large", "bo_gold_candle_stick_large", []),

	("gold_goblet", 0, "gold_goblet", "bo_gold_goblet", []),

	("gold_nugget", 0, "gold_nugget", "bo_gold_nugget", []),

	("statue_greek_goddess", 0, "statue_greek_goddess", "bo_statue_greek_goddess", []),

	("statue_wines", 0, "statue_wines", "bo_statue_wines", []),

	("statue_wines_dead", 0, "statue_wines_dead", "bo_statue_wines_dead", []),

	("titan_of_braavos", 0, "titan_of_braavos", "0", []),

	("elder_statue", 0, "elder_statue", "bo_elder_statue", []),

	("obelisk_1", 0, "obelisk_1", "bo_obelisk_1", []),

	("manticore", 0, "manticore", "bo_manticore", []),

	("manticore_podium", 0, "manticore_podium", "bo_manticore_podium", []),

	("dragon_3", 0, "dragon_3", "bo_dragon_3", []),

	("mermaid", 0, "mermaid", "bo_mermaid", []),

	("tombstone_1", 0, "tombstone_1", "bo_tombstone_1", []),

	("tombstone_2", 0, "tombstone_2", "bo_tombstone_2", []),

	("tombstone_3", 0, "tombstone_3", "bo_tombstone_3", []),

	("tombstone_4", 0, "tombstone_4", "bo_tombstone_4", []),

	("direwolf", 0, "direwolf", "bo_direwolf", []),

	("creepy_tree", 0, "creepy_tree", "bo_creepy_tree", []),

	("creepy_tree_weirwood", 0, "creepy_tree_weirwood", "bo_creepy_tree", []),

	("vase_1_1", 0, "vase_1_1", "bo_vase_1_1", []),

	("vase_1_1_broken", 0, "vase_1_1_broken", "bo_vase_1_1_broken", []),

	("vase_1_2", 0, "vase_1_2", "bo_vase_1_2", []),

	("a_vase_1_2_broken", 0, "a_vase_1_2_broken", "bo_vase_1_2_broken", []),

	("vase_1_3", 0, "vase_1_3", "bo_vase_1_3", []),

	("vase_1_3_broken", 0, "vase_1_3_broken", "bo_vase_1_3_broken", []),

	("vase_1_4", 0, "vase_1_4", "bo_vase_1_4", []),

	("vase_1_4_broken", 0, "vase_1_4_broken", "bo_vase_1_4_broken", []),

	("vase_1_5", 0, "vase_1_5", "bo_vase_1_5", []),

	("vase_1_6", 0, "vase_1_6", "bo_vase_1_6", []),

	("vase_2_1", 0, "vase_2_1", "bo_vase_2_1", []),

	("vase_2_1_broken", 0, "vase_2_1_broken", "bo_vase_2_1_broken", []),

	("vase_2_2", 0, "vase_2_2", "bo_vase_2_2", []),

	("vase_3_1", 0, "vase_3_1", "bo_vase_3_1", []),

	("vase_4_1", 0, "vase_4_1", "bo_vase_4_1", []),

	("rope", 0, "rope", "bo_rope", []),

	("haysack_1", 0, "haysack_1", "bo_haysack_1", []),

	("haysack_2", 0, "haysack_2", "bo_haysack_2", []),

	("haysack_3", 0, "haysack_3", "bo_haysack_3", []),

	("hanging_cloth_1", 0, "hanging_cloth_1", "bo_hanging_cloth_1", []),

	("hanging_cloth_2", 0, "hanging_cloth_2", "bo_hanging_cloth_2", []),

	("hanging_cloth_3", 0, "hanging_cloth_3", "bo_hanging_cloth_3", []),

	("hanging_cloth_4", 0, "hanging_cloth_4", "bo_hanging_cloth_4", []),

	("hanging_cloth_5", 0, "hanging_cloth_5", "bo_hanging_cloth_5", []),

	("impaled_fish_2", 0, "impaled_fish_2", "bo_impaled_fish_2", []),

	("crane_4", 0, "crane_4", "bo_crane_4", []),

	("crane_3", 0, "crane_3", "bo_crane_3", []),

	("gallows", 0, "gallows", "bo_gallows", []),

	("cochon", 0, "cochon", "bo_cochon", []),

	("goat_statue", 0, "goat_statue", "bo_goat_statue", []),

	("lion_statue", 0, "lion_statue", "bo_lion_statue", []),

	("food_blue_cheese", 0, "food_blue_cheese", "bo_food_blue_cheese", []),

	("food_rabbit", 0, "food_rabbit", "bo_food_rabbit", []),

	("food_salmon", 0, "food_salmon", "bo_food_salmon", []),

	("food_oerred", 0, "food_oerred", "bo_food_oerred", []),

	("food_blueberry_tart_whole_1", 0, "food_blueberry_tart_whole_1", "bo_food_blueberry_tart_whole_1", []),

	("food_apple_tart_whole_1", 0, "food_apple_tart_whole_1", "bo_food_apple_tart_whole_1", []),

	("food_apple_tart_whole_2", 0, "food_apple_tart_whole_2", "bo_food_apple_tart_whole_2", []),

	("tribal_hut", 0, "tribal_hut", "bo_tribal_hut", []),

	("tribal_hut_b", 0, "tribal_hut_b", "bo_tribal_hut_b", []),

	("tribal_hut_2", 0, "tribal_hut_2", "bo_tribal_hut_2", []),

	("tribal_hut_3", 0, "tribal_hut_3", "bo_tribal_hut_3", []),

	("tribal_cage_1", 0, "tribal_cage_1", "bo_tribal_cage_1", []),

	("tribal_gate", 0, "tribal_gate", "bo_tribal_gate", []),

	("tribal_vine_rope_1", 0, "tribal_vine_rope_1", "0", []),

	("tribal_vine_rope_2", 0, "tribal_vine_rope_2", "0", []),

	("tribal_vine_rope_3", 0, "tribal_vine_rope_3", "0", []),

	("tribal_vine_ivy_1", 0, "tribal_vine_ivy_1", "0", []),

	("tribal_vine_ivy_2", 0, "tribal_vine_ivy_2", "0", []),

	("tribal_new_shrub_1", 0, "tribal_new_shrub_1", "0", []),

	("tribal_new_shrub_2", 0, "tribal_new_shrub_2", "0", []),

	("tribal_new_shrub_3", 0, "tribal_new_shrub_3", "0", []),

	("tribal_new_shrub_3b", 0, "tribal_new_shrub_3b", "0", []),

	("tribal_new_shrub_3c", 0, "tribal_new_shrub_3c", "0", []),

	("tribal_new_shrub_4", 0, "tribal_new_shrub_4", "0", []),

	("tribal_new_shrub_4b", 0, "tribal_new_shrub_4b", "0", []),

	("tribal_new_shrub_4c", 0, "tribal_new_shrub_4c", "0", []),

	("tribal_new_shrub_5", 0, "tribal_new_shrub_5", "0", []),

	("tribal_new_shrub_5b", 0, "tribal_new_shrub_5b", "0", []),

	("tribal_new_shrub_5c", 0, "tribal_new_shrub_5c", "0", []),

	("tribal_cactus", 0, "cactus", "bo_cactus", []),

	("tribal_bamboo", 0, "bamboo", "0", []),

	("tribal_pumpkin", 0, "pumpkin", "0", []),

	("tribal_new_shrub_1_huge", 0, "tribal_new_shrub_1_huge", "0", []),

	("tribal_new_shrub_3b_huge", 0, "tribal_new_shrub_3b_huge", "0", []),

	("tribal_new_shrub_4_huge", 0, "tribal_new_shrub_4_huge", "0", []),

	("tribal_new_shrub_5_huge", 0, "tribal_new_shrub_5_huge", "0", []),

	("tribal_new_shrub_5b_huge", 0, "tribal_new_shrub_5b_huge", "0", []),

	("tribal_new_shrub_5c_huge", 0, "tribal_new_shrub_5c_huge", "0", []),

	("roman_aqued_a", 0, "roman_aqued_a", "bo_roman_aqued_a", []),

	("roman_aqued_a_turn", 0, "roman_aqued_a_turn", "bo_roman_aqued_a_turn", []),

	("roman_forum_new", 0, "roman_forum_new", "bo_roman_forum_new", []),

	("roman_forum_new_part_a", 0, "roman_forum_new_part_a", "bo_roman_forum_new_part_a", []),

	("roman_forum_new_part_b", 0, "roman_forum_new_part_b", "bo_roman_forum_new_part_b", []),

	("roman_gazebo_new_a", 0, "roman_gazebo_new_a", "bo_roman_gazebo_new_a", []),

	("roman_house_a", 0, "roman_house_a", "bo_roman_house_a", []),

	("roman_house_b", 0, "roman_house_b", "bo_roman_house_b", []),

	("roman_house_c", 0, "roman_house_c", "bo_roman_house_c", []),

	("roman_house_e", 0, "roman_house_e", "bo_roman_house_e", []),

	("roman_house_f", 0, "roman_house_f", "bo_roman_house_f", []),

	("roman_house_g", 0, "roman_house_g", "bo_roman_house_g", []),

	("roman_house_h", 0, "roman_house_h", "bo_roman_house_h", []),

	("roman_market_new", 0, "roman_market_new", "bo_roman_market_new", []),

	("roman_prop_new_a", 0, "roman_prop_new_a", "bo_roman_prop_new_a", []),

	("roman_temple_new_a", 0, "roman_temple_new_a", "bo_roman_temple_new_a", []),

	("roman_temple_new_b", 0, "roman_temple_new_b", "bo_roman_temple_new_b", []),

	("roman_villa_new_a", 0, "roman_villa_new_a", "bo_roman_villa_new_a", []),

	("roman_wall_a", 0, "roman_wall_a", "bo_roman_wall_a", []),

	("roman_wall_a_gate", 0, "roman_wall_a_gate", "bo_roman_wall_a_gate", []),

	("iron_throne", 0, "iron_throne", "bo_iron_throne", []),

	("painted_table", 0, "painted_table", "bo_painted_table", []),

	("iron_throne_2", 0, "iron_throne_2", "bo_iron_throne_2", []),

	("iron_throne_new", 0, "iron_throne_new", "bo_iron_throne_new", []),

	("iron_throne_3", 0, "iron_throne_3", "0", []),

	("iron_throne_4", 0, "iron_throne_4", "0", []),

	("iron_throne_5", 0, "iron_throne_5", "0", []),

	("iron_throne_no_collision", 0, "iron_throne_no_collision", "0", []),

	("storms_end_mountains", 0, "storms_end_mountains", "0", []),

	("aqua_plant", 0, "aqua_plant", "0", []),

	("skeleton_a", 0, "skeleton_b_new", "0", []),

	("skeleton_b", 0, "skeleton_b_new", "0", []),

	("skeleton_c", 0, "skeleton_b_new", "0", []),

	("ado_fantasy_temple", 0, "ado_fantasy_temple", "bo_ado_fantasy_temple", []),

	("ado_fantasy_castle", 0, "ado_fantasy_castle", "bo_ado_fantasy_castle", []),

	("ado_fantasy_tower", 0, "ado_fantasy_tower", "bo_ado_fantasy_tower", []),

	("ado_fantasy_theatre", 0, "ado_fantasy_theatre", "bo_ado_fantasy_theatre", []),

	("ado_fantasy_house_small", 0, "ado_fantasy_house_small", "bo_ado_fantasy_house_small", []),

	("ado_fantasy_wall_small", 0, "ado_fantasy_wall_small", "bo_ado_fantasy_wall_small", []),

	("ado_fantasy_wall_small_corner", 0, "ado_fantasy_wall_small_corner", "bo_ado_fantasy_wall_small_corner", []),

	("ado_fantasy_wall_small_decay", 0, "ado_fantasy_wall_small_decay", "bo_ado_fantasy_wall_small_decay", []),

	("ado_fantasy_wall_small_decay2", 0, "ado_fantasy_wall_small_decay2", "bo_ado_fantasy_wall_small_decay2", []),

	("ado_fantasy_wall_small_gate", 0, "ado_fantasy_wall_small_gate", "bo_ado_fantasy_wall_small_gate", []),

	("ado_fantasy_wall_large", 0, "ado_fantasy_wall_large", "bo_ado_fantasy_wall_large", []),

	("ado_fantasy_wall_large_arrow_slits", 0, "ado_fantasy_wall_large_arrow_slits", "bo_ado_fantasy_wall_large_arrow_slits", []),

	("ado_fantasy_wall_large_destroyed", 0, "ado_fantasy_wall_large_destroyed", "bo_ado_fantasy_wall_large_destroyed", []),

	("ado_fantasy_wall_large_corner", 0, "ado_fantasy_wall_large_corner", "bo_ado_fantasy_wall_large_corner", []),

	("ado_fantasy_wall_large_stairs", 0, "ado_fantasy_wall_large_stairs", "bo_ado_fantasy_wall_large_stairs", []),

	("ado_fantasy_stairs_stone", 0, "ado_fantasy_stairs_stone", "bo_ado_fantasy_stairs_stone", []),

	("ado_fantasy_stairs_stone_steps", 0, "ado_fantasy_stairs_stone_steps", "bo_ado_fantasy_stairs_stone_steps", []),

	("ado_fantasy_wall_large_stairs_left", 0, "ado_fantasy_wall_large_stairs_left", "bo_ado_fantasy_wall_large_stairs_left", []),

	("ado_fantasy_wall_large_stairs_right", 0, "ado_fantasy_wall_large_stairs_right", "bo_ado_fantasy_wall_large_stairs_right", []),

	("ado_fantasy_wall_large_bend", 0, "ado_fantasy_wall_large_bend", "bo_ado_fantasy_wall_large_bend", []),

	("ado_fantasy_rubble", 0, "ado_fantasy_rubble", "bo_ado_fantasy_rubble", []),

	("ado_fantasy_rubble2", 0, "ado_fantasy_rubble2", "bo_ado_fantasy_rubble2", []),

	("ado_fantasy_platform_small_stone", 0, "ado_fantasy_platform_small_stone", "bo_ado_fantasy_platform_small_stone", []),

	("ado_fantasy_wall_large_tower", 0, "ado_fantasy_wall_large_tower", "bo_ado_fantasy_wall_large_tower", []),

	("ado_fantasy_wall_large_tower_turret", 0, "ado_fantasy_wall_large_tower_turret", "bo_ado_fantasy_wall_large_tower_turret", []),

	("ado_fantasy_platform_octagon", 0, "ado_fantasy_platform_octagon", "bo_ado_fantasy_platform_octagon", []),

	("iron_throne_platform", 0, "iron_throne_platform", "bo_iron_throne_platform", []),

	("ado_fantasy_wall_stone_rough", 0, "ado_fantasy_wall_stone_rough", "bo_ado_fantasy_wall_stone_rough", []),

	("ado_fantasy_wall_stone_regular", 0, "ado_fantasy_wall_stone_regular", "bo_ado_fantasy_wall_stone_regular", []),

	("ado_fantasy_wall_stone_regular_pillar", 0, "ado_fantasy_wall_stone_regular_pillar", "bo_ado_fantasy_wall_stone_regular_pillar", []),

	("ado_fantasy_wall_stone_regular_gate", 0, "ado_fantasy_wall_stone_regular_gate", "bo_ado_fantasy_wall_stone_regular_gate", []),

	("ado_fantasy_gatehouse", 0, "ado_fantasy_gatehouse", "bo_ado_fantasy_gatehouse", []),

	("ado_fantasy_beacon_pillar", 0, "ado_fantasy_beacon_pillar", "bo_ado_fantasy_beacon_pillar", []),

	("ado_fantasy_house_long", 0, "ado_fantasy_house_long", "bo_ado_fantasy_house_long", []),

	("ado_fantasy_courtyard_arches", 0, "ado_fantasy_courtyard_arches", "bo_ado_fantasy_courtyard_arches", []),

	("nights_watch_bush", 0, "nights_watch_bush", "0", []),

	("nights_watch_tree_1", 0, "nights_watch_tree_1", "bo_nights_watch_tree_1", []),

	("nights_watch_tree_2", 0, "nights_watch_tree_2", "bo_nights_watch_tree_2", []),

	("nights_watch_tree_3", 0, "nights_watch_tree_3", "bo_nights_watch_tree_3", []),

	("nights_watch_tree_4", 0, "nights_watch_tree_4", "bo_nights_watch_tree_4", []),

	("essos_dungeon_1", 0, "essos_dungeon_1", "bo_essos_dungeon_1", []),

	("essos_cave_1", 0, "essos_cave_1", "bo_essos_cave_1", []),

	("essos_cave_2", 0, "essos_cave_2", "bo_essos_cave_2", []),

	("essos_cave_3", 0, "essos_cave_3", "bo_essos_cave_3", []),

	("essos_cave_4", 0, "essos_cave_4", "bo_essos_cave_4", []),

	("essos_cave_5", 0, "essos_cave_5", "bo_essos_cave_5", []),

	("essos_cave_6", 0, "essos_cave_6", "bo_essos_cave_6", []),

	("essos_cave_7", 0, "essos_cave_7", "bo_essos_cave_7", []),

	("wall_cave_1", 0, "wall_cave_1", "bo_essos_cave_1", []),

	("wall_cave_2", 0, "wall_cave_2", "bo_essos_cave_2", []),

	("wall_cave_3", 0, "wall_cave_3", "bo_essos_cave_3", []),

	("wall_cave_4", 0, "wall_cave_4", "bo_essos_cave_4", []),

	("wall_cave_5", 0, "wall_cave_5", "bo_essos_cave_5", []),

	("wall_cave_6", 0, "wall_cave_6", "bo_essos_cave_6", []),

	("wall_cave_7", 0, "wall_cave_7", "bo_essos_cave_7", []),

	("wall_tunnel_1", 0, "wall_tunnel_1", "bo_wall_tunnel_1", []),

	("wall_tunnel_2", 0, "wall_tunnel_2", "bo_wall_tunnel_2", []),

	("wall_tunnel_3", 0, "wall_tunnel_3", "bo_wall_tunnel_3", []),

	("wall_tunnel_4", 0, "wall_tunnel_4", "bo_wall_tunnel_4", []),

	("wall_tunnel_5", 0, "wall_tunnel_5", "bo_wall_tunnel_5", []),

	("wall_tunnel_6", 0, "wall_tunnel_6", "bo_wall_tunnel_6", []),

	("mummy", 0, "mummy", "0", []),

	("weirwood_throne", 0, "weirwood_throne", "0", []),

	("antlers_on_wood", 0, "antlers_on_wood", "0", []),

	("antlers_on_wood_2", 0, "antlers_on_wood_2", "0", []),

	("duke_throne", 0, "duke_throne", "bo_duke_throne", []),

	("dark_throne", 0, "dark_throne", "bo_dark_throne", []),

	("statue_mourning_woman", 0, "statue_mourning_woman", "bo_statue_mourning_woman", []),

	("statue_harvest", 0, "statue_harvest", "bo_statue_pedestal_3", []),

	("statue_king", 0, "statue_king", "bo_statue_pedestal_2", []),

	("statue_weeping_angel", 0, "statue_weeping_angel", "bo_statue_pedestal_1", []),

	("statue_god_warrior", 0, "statue_god_warrior", "bo_statue_god_warrior", []),

	("statue_pedestal_1", 0, "statue_pedestal_1", "bo_statue_pedestal_1", []),

	("statue_pedestal_2", 0, "statue_pedestal_2", "bo_statue_pedestal_2", []),

	("statue_pedestal_3", 0, "statue_pedestal_3", "bo_statue_pedestal_3", []),

	("rock_bridge_a", 0, "rock_bridge_a", "bo_rock_bridge_a", []),

	("suspension_bridge_a", 0, "suspension_bridge_a", "bo_suspension_bridge_a", []),

	("mine_a", 0, "mine_a", "bo_mine_a", []),

	("statue_lion", 0, "statue_lion", "bo_statue_lion", []),

	("statue_lion_2", 0, "statue_lion_2", "bo_statue_lion_2", []),

	("statue_woman", 0, "statue_woman", "bo_statue_woman", []),

	("coffin", 0, "coffin", "bo_coffin", []),

	("statue_elephant", 0, "statue_elephant", "bo_statue_elephant", []),

	("picture_map_1", 0, "picture_map_1", "0", []),

	("picture_map_2", 0, "picture_map_2", "0", []),

	("picture_map_3", 0, "picture_map_3", "0", []),

	("picture_map_4", 0, "picture_map_4", "0", []),

	("picture_map_5", 0, "picture_map_5", "0", []),

	("picture_map_6", 0, "picture_map_6", "0", []),

	("picture_map_7", 0, "picture_map_7", "0", []),

	("picture_map_8", 0, "picture_map_8", "0", []),

	("picture_map_9", 0, "picture_map_9", "0", []),

	("a_acantilado-05", 0, "acantilado-05", "bo_acantilado-05", []),

	("nordous_gallow", 0, "nordous_gallow", "bo_nordous_gallow", []),

	("nordous_straw_1", 0, "nordous_straw_1", "bo_nordous_straw_1", []),

	("nordous_straw_2", 0, "nordous_straw_2", "bo_nordous_straw_2", []),

	("nordous_straw_3", 0, "nordous_straw_3", "bo_nordous_straw_3", []),

	("straw_a", 0, "nordous_straw_1", "0", []),

	("straw_b", 0, "nordous_straw_2", "0", []),

	("straw_c", 0, "nordous_straw_3", "0", []),

	("ghiscari_pyramid", 0, "ghiscari_pyramid", "0", []),

	("ghiscari_pyramid_complex", 0, "ghiscari_pyramid_complex", "0", []),

	("night_king_stone", 0, "night_king_stone", "bo_night_king_stone", []),

	("dragon_skull", 0, "dragon_skull", "0", []),

	("mad_axe_blood", 0, "mad_axe_blood", "0", []),

	("a_fog_fantasy", 0, "0", "0", 
	[(ti_on_scene_prop_init,
		[
			(particle_system_add_new, "psys_brume")
		])
	]),

	("naggas_rib", 0, "naggas_rib", "bo_naggas_rib", []),

	("oim_trench_set_a", 0, "oim_trench_set_a", "bo_oim_trench_set_a", []),

	("oim_trench_set_b", 0, "oim_trench_set_b", "bo_oim_trench_set_b", []),

	("oim_broken_cart", 0, "oim_broken_cart", "bo_oim_broken_cart", []),

	("oim_broken_barrel", 0, "oim_broken_barrel", "bo_oim_broken_barrel", []),

	("oim_trench_box_set", 0, "oim_trench_box_set", "bo_oim_trench_box_set", []),

	("oim_trench_wood_a", 0, "oim_trench_wood_a", "bo_oim_trench_wood_a", []),

	("oim_trench_wood_b", 0, "oim_trench_wood_b", "bo_oim_trench_wood_b", []),

	("oim_trench_wood_c", 0, "oim_trench_wood_c", "bo_oim_trench_wood_c", []),

	("oim_shelves_1", 0, "oim_shelves_1", "0", []),

	("oim_shelves_2", 0, "oim_shelves_2", "0", []),

	("tunnel_curved", 0, "tunnel_curved", "bo_tunnel_curved", []),

	("tunnel_crossing", 0, "tunnel_crossing", "bo_tunnel_crossing", []),

	("tunnel_support", 0, "tunnel_support", "bo_tunnel_support", []),

	("tunnel_crossing_supports", 0, "tunnel_crossing_supports", "bo_tunnel_crossing_supports", []),

	("tunnel_split", 0, "tunnel_split", "bo_tunnel_split", []),

	("tunnel_split_supports", 0, "tunnel_split_supports", "bo_tunnel_split_supports", []),

	("chasm", 0, "chasm", "bo_chasm", []),

	("tunnel_curved_supports", 0, "tunnel_curved_supports", "bo_tunnel_curved_supports", []),

	("tunnel_short", 0, "tunnel_short", "bo_tunnel_short", []),

	("tunnel_short_supports", 0, "tunnel_short_supports", "bo_tunnel_short_supports", []),

	("tunnel_sloped", 0, "tunnel_sloped", "bo_tunnel_sloped", []),

	("tunnel_sloped_supports", 0, "tunnel_sloped_supports", "bo_tunnel_sloped_supports", []),

	("tunnel_straight", 0, "tunnel_straight", "bo_tunnel_straight", []),

	("tunnel_straight_supports", 0, "tunnel_straight_supports", "bo_tunnel_straight_supports", []),

	("arena_tourney_tent_1", 0, "arena_tourney_tent_1", "bo_arena_tourney_tent_1", []),

	("arena_tourney_tent_2", 0, "arena_tourney_tent_2", "bo_arena_tourney_tent_2", []),

	("arena_merchant_stand_1", 0, "arena_merchant_stand_1", "bo_arena_merchant_stand_1", []),

	("arena_merchant_stand_2", 0, "arena_merchant_stand_2", "bo_arena_merchant_stand_2", []),

	("arena_tourney_stand_1", 0, "arena_tourney_stand_1", "bo_arena_tourney_stand_1", []),

	("arena_tourney_stand_2", 0, "arena_tourney_stand_2", "bo_arena_tourney_stand_2", []),

	("necturus_gold_bars", 0, "necturus_gold_bars", "bo_necturus_gold_bars", []),

	("necturus_banket_chair", 0, "necturus_banket_chair", "bo_necturus_banket_chair", []),

	("necturus_banket_table", 0, "necturus_banket_table", "bo_necturus_banket_table", []),

	("necturus_throne", 0, "necturus_throne", "bo_necturus_throne", []),

	("necturus_knight", 0, "necturus_knight", "bo_necturus_knight", []),

	("necturus_bed_wood", 0, "necturus_bed_wood", "bo_necturus_bed_wood", []),

	("necturus_bath", 0, "necturus_bath", "bo_necturus_bath", []),

	("necturus_alchemy_stove", 0, "necturus_alchemy_stove", "bo_necturus_alchemy_stove", []),

	("necturus_alchemy_table", 0, "necturus_alchemy_table", "bo_necturus_alchemy_table", []),

	("necturus_bookshelf", 0, "necturus_bookshelf", "bo_necturus_bookshelf", []),

	("necturus_bookshelf_clutter", 0, "necturus_bookshelf_clutter", "bo_necturus_bookshelf", []),

	("necturus_cabinet_1", 0, "necturus_cabinet_1", "bo_necturus_cabinet_1", []),

	("necturus_cabinet_2", 0, "necturus_cabinet_2", "bo_necturus_cabinet_2", []),

	("necturus_common_chair", 0, "necturus_common_chair", "bo_necturus_common_chair", []),

	("necturus_dinner_stool", 0, "necturus_dinner_stool", "bo_necturus_dinner_stool", []),

	("necturus_dinner_table", 0, "necturus_dinner_table", "bo_necturus_dinner_table", []),

	("necturus_stool", 0, "necturus_stool", "bo_necturus_stool", []),

	("necturus_table", 0, "necturus_table", "bo_necturus_table", []),

	("necturus_bed_1", 0, "necturus_bed_1", "bo_necturus_bed_1", []),

	("necturus_bed_2", 0, "necturus_bed_2", "bo_necturus_bed_2", []),

	("necturus_bs_anvil", 0, "necturus_bs_anvil", "bo_necturus_bs_anvil", []),

	("necturus_bs_log", 0, "necturus_bs_log", "bo_necturus_bs_log", []),

	("necturus_bs_rack", 0, "necturus_bs_rack", "bo_necturus_bs_rack", []),

	("necturus_bs_rack_clutter", 0, "necturus_bs_rack_clutter", "bo_necturus_bs_rack", []),

	("necturus_bs_stool", 0, "necturus_bs_stool", "bo_necturus_bs_stool", []),

	("necturus_bs_table", 0, "necturus_bs_table", "bo_necturus_bs_table", []),

	("necturus_bs_table_clutter", 0, "necturus_bs_table_clutter", "bo_necturus_bs_table", []),

	("necturus_bs_tools_base", 0, "necturus_bs_tools_base", "bo_necturus_bs_tools_base", []),

	("necturus_bs_tub", 0, "necturus_bs_tub", "bo_necturus_bs_tub", []),

	("necturus_alchemy_shelf", 0, "necturus_alchemy_shelf", "bo_necturus_alchemy_shelf", []),

	("necturus_alchemy_shelf_clutter", 0, "necturus_alchemy_shelf_clutter", "bo_necturus_alchemy_shelf", []),

	("necturus_alchemy_shelves", 0, "necturus_alchemy_shelves", "bo_necturus_alchemy_shelves", []),

	("seastone_chair", 0, "seastone_chair", "bo_seastone_chair", []),

	("necturus_bell", 0, "necturus_bell", "0", []),

	("necturus_gold_coin_single", 0, "necturus_gold_coin_single", "0", []),

	("necturus_gold_coin_pile", 0, "necturus_gold_coin_pile", "0", []),

	("necturus_bear_skin", 0, "necturus_bear_skin", "0", []),

	("necturus_deep_trophy", 0, "necturus_deep_trophy", "0", []),

	("necturus_cup", 0, "necturus_cup", "0", []),

	("necturus_drinking_horn", 0, "necturus_drinking_horn", "0", []),

	("necturus_gratter", 0, "necturus_gratter", "0", []),

	("necturus_pot", 0, "necturus_pot", "0", []),

	("necturus_vase", 0, "necturus_vase", "0", []),

	("necturus_bowl", 0, "necturus_bowl", "0", []),

	("necturus_candle_stick", 0, "necturus_candle_stick", "0", []),

	("necturus_chandelier", 0, "necturus_chandelier", "0", []),

	("necturus_carpet_1", 0, "necturus_carpet_1", "0", []),

	("necturus_carpet_2", 0, "necturus_carpet_2", "0", []),

	("necturus_carpet_3", 0, "necturus_carpet_3", "0", []),

	("necturus_carpet_4", 0, "necturus_carpet_4", "0", []),

	("necturus_carpet_5", 0, "necturus_carpet_5", "0", []),

	("necturus_carpet_6", 0, "necturus_carpet_6", "0", []),

	("necturus_book_1", 0, "necturus_book_1", "0", []),

	("necturus_book_2", 0, "necturus_book_2", "0", []),

	("necturus_book_3", 0, "necturus_book_3", "0", []),

	("necturus_book_4", 0, "necturus_book_4", "0", []),

	("necturus_book_5", 0, "necturus_book_5", "0", []),

	("necturus_inkwell", 0, "necturus_inkwell", "0", []),

	("necturus_journal", 0, "necturus_journal", "0", []),

	("necturus_map", 0, "necturus_map", "0", []),

	("necturus_scroll_1", 0, "necturus_scroll_1", "0", []),

	("necturus_scroll_2", 0, "necturus_scroll_2", "0", []),

	("necturus_scroll_3", 0, "necturus_scroll_3", "0", []),

	("necturus_dinner_fork", 0, "necturus_dinner_fork", "0", []),

	("necturus_dinner_knife", 0, "necturus_dinner_knife", "0", []),

	("necturus_dinner_spoon", 0, "necturus_dinner_spoon", "0", []),

	("necturus_goblet", 0, "necturus_goblet", "0", []),

	("necturus_plate_1", 0, "necturus_plate_1", "0", []),

	("necturus_plate_2", 0, "necturus_plate_2", "0", []),

	("necturus_tankard", 0, "necturus_tankard", "0", []),

	("necturus_bottle_rhum", 0, "necturus_bottle_rhum", "0", []),

	("necturus_bottle_wine", 0, "necturus_bottle_wine", "0", []),

	("necturus_alchemy_bellows", 0, "necturus_alchemy_bellows", "0", []),

	("necturus_alchemy_bulb_1", 0, "necturus_alchemy_bulb_1", "0", []),

	("necturus_alchemy_bulb_2", 0, "necturus_alchemy_bulb_2", "0", []),

	("necturus_alchemy_bulb_3", 0, "necturus_alchemy_bulb_3", "0", []),

	("necturus_alchemy_bulb_4", 0, "necturus_alchemy_bulb_4", "0", []),

	("necturus_alchemy_bulb_5", 0, "necturus_alchemy_bulb_5", "0", []),

	("necturus_alchemy_bulb_6", 0, "necturus_alchemy_bulb_6", "0", []),

	("necturus_alchemy_coal", 0, "necturus_alchemy_coal", "0", []),

	("necturus_alchemy_crystal_1", 0, "necturus_alchemy_crystal_1", "0", []),

	("necturus_alchemy_crystal_2", 0, "necturus_alchemy_crystal_2", "0", []),

	("necturus_alchemy_crystal_3", 0, "necturus_alchemy_crystal_3", "0", []),

	("necturus_alchemy_crystal_ball", 0, "necturus_alchemy_crystal_ball", "0", []),

	("necturus_alchemy_dragon_egg", 0, "necturus_alchemy_dragon_egg", "0", []),

	("necturus_alchemy_forceps", 0, "necturus_alchemy_forceps", "0", []),

	("necturus_alchemy_gold", 0, "necturus_alchemy_gold", "0", []),

	("necturus_alchemy_hook", 0, "necturus_alchemy_hook", "0", []),

	("necturus_alchemy_ladle", 0, "necturus_alchemy_ladle", "0", []),

	("necturus_alchemy_poker", 0, "necturus_alchemy_poker", "0", []),

	("necturus_alchemy_potion_1", 0, "necturus_alchemy_potion_1", "0", []),

	("necturus_alchemy_potion_2", 0, "necturus_alchemy_potion_2", "0", []),

	("necturus_alchemy_potion_3", 0, "necturus_alchemy_potion_3", "0", []),

	("necturus_alchemy_potion_4", 0, "necturus_alchemy_potion_4", "0", []),

	("necturus_alchemy_potion_5", 0, "necturus_alchemy_potion_5", "0", []),

	("necturus_alchemy_pounder", 0, "necturus_alchemy_pounder", "0", []),

	("necturus_alchemy_retort_1", 0, "necturus_alchemy_retort_1", "0", []),

	("necturus_alchemy_retort_2", 0, "necturus_alchemy_retort_2", "0", []),

	("necturus_alchemy_retort_3", 0, "necturus_alchemy_retort_3", "0", []),

	("necturus_alchemy_retort_4", 0, "necturus_alchemy_retort_4", "0", []),

	("necturus_alchemy_retort_5", 0, "necturus_alchemy_retort_5", "0", []),

	("necturus_alchemy_retort_6", 0, "necturus_alchemy_retort_6", "0", []),

	("necturus_alchemy_retort_broken", 0, "necturus_alchemy_retort_broken", "0", []),

	("necturus_alchemy_root_1", 0, "necturus_alchemy_root_1", "0", []),

	("necturus_alchemy_root_2", 0, "necturus_alchemy_root_2", "0", []),

	("necturus_alchemy_scales", 0, "necturus_alchemy_scales", "0", []),

	("necturus_alchemy_scissors", 0, "necturus_alchemy_scissors", "0", []),

	("necturus_alchemy_scraper", 0, "necturus_alchemy_scraper", "0", []),

	("necturus_alchemy_skull", 0, "necturus_alchemy_skull", "0", []),

	("necturus_alchemy_stand", 0, "necturus_alchemy_stand", "0", []),

	("necturus_alchemy_stand_small", 0, "necturus_alchemy_stand_small", "0", []),

	("necturus_alchemy_telescope", 0, "necturus_alchemy_telescope", "0", []),

	("necturus_alchemy_timeglass", 0, "necturus_alchemy_timeglass", "0", []),

	("necturus_alchemy_tube_1", 0, "necturus_alchemy_tube_1", "0", []),

	("necturus_alchemy_tube_2", 0, "necturus_alchemy_tube_2", "0", []),

	("necturus_alchemy_vase_1", 0, "necturus_alchemy_vase_1", "0", []),

	("necturus_alchemy_vase_2", 0, "necturus_alchemy_vase_2", "0", []),

	("necturus_alchemy_vase_2_cover", 0, "necturus_alchemy_vase_2_cover", "0", []),

	("necturus_alchemy_vase_3", 0, "necturus_alchemy_vase_3", "0", []),

	("necturus_alchemy_vase_3_cover", 0, "necturus_alchemy_vase_3_cover", "0", []),

	("necturus_alchemy_vase_4", 0, "necturus_alchemy_vase_4", "0", []),

	("necturus_alchemy_vase_4_cover", 0, "necturus_alchemy_vase_4_cover", "0", []),

	("necturus_alchemy_vase_5", 0, "necturus_alchemy_vase_5", "0", []),

	("necturus_alchemy_vase_5_cover", 0, "necturus_alchemy_vase_5_cover", "0", []),

	("necturus_basket_1", 0, "necturus_basket_1", "0", []),

	("necturus_basket_2", 0, "necturus_basket_2", "0", []),

	("necturus_big_barrel", 0, "necturus_big_barrel", "0", []),

	("necturus_big_box", 0, "necturus_big_box", "0", []),

	("necturus_bird_cage", 0, "necturus_bird_cage", "0", []),

	("necturus_brazier", 0, "necturus_brazier", "0", []),

	("necturus_candle_large", 0, "necturus_candle_large", "0", []),

	("necturus_candle_small", 0, "necturus_candle_small", "0", []),

	("necturus_ceramic_container_1", 0, "necturus_ceramic_container_1", "0", []),

	("necturus_ceramic_container_2", 0, "necturus_ceramic_container_2", "0", []),

	("necturus_oil_lamp_1", 0, "necturus_oil_lamp_1", "0", []),

	("necturus_oil_lamp_2", 0, "necturus_oil_lamp_2", "0", []),

	("necturus_torch", 0, "necturus_torch", "0", []),

	("necturus_sack_1", 0, "necturus_sack_1", "0", []),

	("necturus_sack_2", 0, "necturus_sack_2", "0", []),

	("necturus_sack_3", 0, "necturus_sack_3", "0", []),

	("necturus_small_barrel", 0, "necturus_small_barrel", "0", []),

	("necturus_small_box", 0, "necturus_small_box", "0", []),

	("necturus_picture_1", 0, "necturus_picture_1", "0", []),

	("necturus_picture_2", 0, "necturus_picture_2", "0", []),

	("necturus_big_chest", 0, "necturus_big_chest", "0", []),

	("necturus_captain_chest", 0, "necturus_captain_chest", "0", []),

	("necturus_casket", 0, "necturus_casket", "0", []),

	("necturus_small_chest", 0, "necturus_small_chest", "0", []),

	("necturus_bs_brass_bar", 0, "necturus_bs_brass_bar", "0", []),

	("necturus_bs_copper_bar", 0, "necturus_bs_copper_bar", "0", []),

	("necturus_bs_iron_bar", 0, "necturus_bs_iron_bar", "0", []),

	("necturus_bs_steel_bar", 0, "necturus_bs_steel_bar", "0", []),

	("necturus_bs_brass_rod", 0, "necturus_bs_brass_rod", "0", []),

	("necturus_bs_copper_rod", 0, "necturus_bs_copper_rod", "0", []),

	("necturus_bs_iron_rod", 0, "necturus_bs_iron_rod", "0", []),

	("necturus_bs_steel_rod", 0, "necturus_bs_steel_rod", "0", []),

	("necturus_bs_chain_one", 0, "necturus_bs_chain_one", "0", []),

	("necturus_bs_chains", 0, "necturus_bs_chains", "0", []),

	("necturus_bs_hammer_big", 0, "necturus_bs_hammer_big", "0", []),

	("necturus_bs_hammer_small", 0, "necturus_bs_hammer_small", "0", []),

	("necturus_bs_horseshoe", 0, "necturus_bs_horseshoe", "0", []),

	("necturus_bs_nail", 0, "necturus_bs_nail", "0", []),

	("necturus_bs_plier_medium", 0, "necturus_bs_plier_medium", "0", []),

	("necturus_bs_plier_big", 0, "necturus_bs_plier_big", "0", []),

	("necturus_bs_plier_small", 0, "necturus_bs_plier_small", "0", []),

	("necturus_bs_rasp", 0, "necturus_bs_rasp", "0", []),

	("necturus_bs_vise", 0, "necturus_bs_vise", "0", []),

	("necturus_bowl_full", 0, "necturus_bowl_full", "0", []),

	("necturus_veggi_apple_green", 0, "necturus_veggi_apple_green", "0", []),

	("necturus_veggi_apple_green_half", 0, "necturus_veggi_apple_green_half", "0", []),

	("necturus_veggi_apple_red", 0, "necturus_veggi_apple_red", "0", []),

	("necturus_veggi_apple_yellow", 0, "necturus_veggi_apple_yellow", "0", []),

	("necturus_veggi_beet", 0, "necturus_veggi_beet", "0", []),

	("necturus_veggi_beet_piece", 0, "necturus_veggi_beet_piece", "0", []),

	("necturus_veggi_carrot", 0, "necturus_veggi_carrot", "0", []),

	("necturus_veggi_carrot_piece", 0, "necturus_veggi_carrot_piece", "0", []),

	("necturus_veggi_garlic", 0, "necturus_veggi_garlic", "0", []),

	("necturus_veggi_garlic_single", 0, "necturus_veggi_garlic_single", "0", []),

	("necturus_veggi_grapes", 0, "necturus_veggi_grapes", "0", []),

	("necturus_veggi_lemon", 0, "necturus_veggi_lemon", "0", []),

	("necturus_veggi_lemon_half", 0, "necturus_veggi_lemon_half", "0", []),

	("necturus_veggi_onion_piece", 0, "necturus_veggi_onion_piece", "0", []),

	("necturus_veggi_onion", 0, "necturus_veggi_onion", "0", []),

	("necturus_veggi_peach", 0, "necturus_veggi_peach", "0", []),

	("necturus_veggi_peach_half", 0, "necturus_veggi_peach_half", "0", []),

	("necturus_veggi_pear_green", 0, "necturus_veggi_pear_green", "0", []),

	("necturus_veggi_pear_green_half", 0, "necturus_veggi_pear_green_half", "0", []),

	("necturus_veggi_pear_red", 0, "necturus_veggi_pear_red", "0", []),

	("necturus_veggi_pumpkin", 0, "necturus_veggi_pumpkin", "0", []),

	("necturus_veggi_cabbage", 0, "necturus_veggi_cabbage", "0", []),

	("necturus_veggi_lettuce", 0, "necturus_veggi_lettuce", "0", []),

	("necturus_food_bread_black", 0, "necturus_food_bread_black", "0", []),

	("necturus_food_bread_black_half_b", 0, "necturus_food_bread_black_half_b", "0", []),

	("necturus_food_bread_black_piece_a", 0, "necturus_food_bread_black_piece_a", "0", []),

	("necturus_food_bread_black_cut", 0, "necturus_food_bread_black_cut", "0", []),

	("necturus_food_bread_black_quarters_a", 0, "necturus_food_bread_black_quarters_a", "0", []),

	("necturus_food_bread_white", 0, "necturus_food_bread_white", "0", []),

	("necturus_food_bread_white_half_b", 0, "necturus_food_bread_white_half_b", "0", []),

	("necturus_food_bread_white_piece_b", 0, "necturus_food_bread_white_piece_b", "0", []),

	("necturus_food_bread_white_cut", 0, "necturus_food_bread_white_cut", "0", []),

	("necturus_food_cakes_many", 0, "necturus_food_cakes_many", "0", []),

	("necturus_food_cake_a", 0, "necturus_food_cake_a", "0", []),

	("necturus_food_cheese", 0, "necturus_food_cheese", "0", []),

	("necturus_food_cheese_cut", 0, "necturus_food_cheese_cut", "0", []),

	("necturus_food_cheese_cut_plate", 0, "necturus_food_cheese_cut_plate", "0", []),

	("necturus_food_cheese_piece_a", 0, "necturus_food_cheese_piece_a", "0", []),

	("necturus_food_cheese_piece_b", 0, "necturus_food_cheese_piece_b", "0", []),

	("necturus_food_chicken_leg_many", 0, "necturus_food_chicken_leg_many", "0", []),

	("necturus_food_chicken_leg_many_plate", 0, "necturus_food_chicken_leg_many_plate", "0", []),

	("necturus_food_chicken_leg_a", 0, "necturus_food_chicken_leg_a", "0", []),

	("necturus_food_egg_a", 0, "necturus_food_egg_a", "0", []),

	("necturus_food_egg_many", 0, "necturus_food_egg_many", "0", []),

	("necturus_food_egg_many_plate", 0, "necturus_food_egg_many_plate", "0", []),

	("necturus_food_fried_eggs_a", 0, "necturus_food_fried_eggs_a", "0", []),

	("necturus_food_ham_cut", 0, "necturus_food_ham_cut", "0", []),

	("necturus_food_ham_cut_plate", 0, "necturus_food_ham_cut_plate", "0", []),

	("necturus_food_ham_a", 0, "necturus_food_ham_a", "0", []),

	("necturus_food_ham_piece_a", 0, "necturus_food_ham_piece_a", "0", []),

	("necturus_food_ham_piece_b", 0, "necturus_food_ham_piece_b", "0", []),

	("necturus_food_honey", 0, "necturus_food_honey", "0", []),

	("necturus_food_honey_cap", 0, "necturus_food_honey_cap", "0", []),

	("necturus_food_milk_pincher", 0, "necturus_food_milk_pincher", "0", []),

	("necturus_food_pint", 0, "necturus_food_pint", "0", []),

	("necturus_food_plate_a", 0, "necturus_food_plate_a", "0", []),

	("necturus_food_plate_b", 0, "necturus_food_plate_b", "0", []),

	("necturus_food_plate_c", 0, "necturus_food_plate_c", "0", []),

	("necturus_food_sang", 0, "necturus_food_sang", "0", []),

	("necturus_food_sang_half_a", 0, "necturus_food_sang_half_a", "0", []),

	("necturus_food_sang_cut", 0, "necturus_food_sang_cut", "0", []),

	("necturus_food_sang_cut_plate", 0, "necturus_food_sang_cut_plate", "0", []),

	("necturus_food_sang_piece_a", 0, "necturus_food_sang_piece_a", "0", []),

	("necturus_food_sausage_a", 0, "necturus_food_sausage_a", "0", []),

	("necturus_food_sausage_many", 0, "necturus_food_sausage_many", "0", []),

	("necturus_food_sausage_many_plate", 0, "necturus_food_sausage_many_plate", "0", []),

	("necturus_feast_roast_chicken", 0, "necturus_feast_roast_chicken", "0", []),

	("necturus_feast_caviar_pie", 0, "necturus_feast_caviar_pie", "0", []),

	("necturus_feast_apple_pie", 0, "necturus_feast_apple_pie", "0", []),

	("necturus_feast_roast_swann", 0, "necturus_feast_roast_swann", "0", []),

	("necturus_feast_sturgeon", 0, "necturus_feast_sturgeon", "0", []),

	("necturus_feast_roast_pig", 0, "necturus_feast_roast_pig", "0", []),

	("necturus_feast_oysters", 0, "necturus_feast_oysters", "0", []),

	("necturus_kitchen_big_barrel", 0, "necturus_kitchen_big_barrel", "0", []),

	("necturus_kitchen_big_boiler", 0, "necturus_kitchen_big_boiler", "0", []),

	("necturus_kitchen_boiler_medium", 0, "necturus_kitchen_boiler_medium", "0", []),

	("necturus_kitchen_coffee_maker", 0, "necturus_kitchen_coffee_maker", "0", []),

	("necturus_kitchen_copper_pot", 0, "necturus_kitchen_copper_pot", "0", []),

	("necturus_kitchen_cutting_board", 0, "necturus_kitchen_cutting_board", "0", []),

	("necturus_kitchen_cutting_board_small", 0, "necturus_kitchen_cutting_board_small", "0", []),

	("necturus_kitchen_jar_leaves", 0, "necturus_kitchen_jar_leaves", "0", []),

	("necturus_kitchen_knife_a", 0, "necturus_kitchen_knife_a", "0", []),

	("necturus_kitchen_knife_b", 0, "necturus_kitchen_knife_b", "0", []),

	("necturus_kitchen_knife_c", 0, "necturus_kitchen_knife_c", "0", []),

	("necturus_kitchen_knife_butcher", 0, "necturus_kitchen_knife_butcher", "0", []),

	("necturus_kitchen_ladle_a", 0, "necturus_kitchen_ladle_a", "0", []),

	("necturus_kitchen_ladle_b", 0, "necturus_kitchen_ladle_b", "0", []),

	("necturus_kitchen_ladle_c", 0, "necturus_kitchen_ladle_c", "0", []),

	("necturus_kitchen_ladle_big", 0, "necturus_kitchen_ladle_big", "0", []),

	("necturus_kitchen_meat_fork", 0, "necturus_kitchen_meat_fork", "0", []),

	("necturus_kitchen_oven_tray", 0, "necturus_kitchen_oven_tray", "0", []),

	("necturus_kitchen_pan_big", 0, "necturus_kitchen_pan_big", "0", []),

	("necturus_kitchen_pan_medium", 0, "necturus_kitchen_pan_medium", "0", []),

	("necturus_kitchen_pan_small", 0, "necturus_kitchen_pan_small", "0", []),

	("necturus_kitchen_poker", 0, "necturus_kitchen_poker", "0", []),

	("necturus_kitchen_roasting_jack", 0, "necturus_kitchen_roasting_jack", "0", []),

	("necturus_kitchen_saucepan_combined", 0, "necturus_kitchen_saucepan_combined", "0", []),

	("necturus_kitchen_stewpan_big", 0, "necturus_kitchen_stewpan_big", "0", []),

	("necturus_kitchen_stewpan_medium", 0, "necturus_kitchen_stewpan_medium", "0", []),

	("necturus_kitchen_stirer", 0, "necturus_kitchen_stirer", "0", []),

	("necturus_kitchen_teapot_combined", 0, "necturus_kitchen_teapot_combined", "0", []),

	("necturus_kitchen_water_can_combined", 0, "necturus_kitchen_water_can_combined", "0", []),

	("necturus_kitchen_wood_saucer", 0, "necturus_kitchen_wood_saucer", "0", []),

	("necturus_skeleton_lying_down", 0, "necturus_skeleton_lying_down", "0", []),

	("necturus_skeleton_sitting_down", 0, "necturus_skeleton_sitting_down", "0", []),

	("necturus_skeleton_bone", 0, "necturus_skeleton_bone", "0", []),

	("necturus_skeleton_foot", 0, "necturus_skeleton_foot", "0", []),

	("necturus_skeleton_rib_cage", 0, "necturus_skeleton_rib_cage", "0", []),

]