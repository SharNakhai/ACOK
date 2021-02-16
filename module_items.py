from module_constants import *
from ID_factions import *
from header_items import  *
from header_operations import *
from header_triggers import *

####################################################################################################################
#  Each item record contains the following fields:
#  1) Item id: used for referencing items in other files.
#     The prefix itm_ is automatically added before each item id.
#  2) Item name. Name of item as it'll appear in inventory window
#  3) List of meshes.  Each mesh record is a tuple containing the following fields:
#    3.1) Mesh name.
#    3.2) Modifier bits that this mesh matches.
#     Note that the first mesh record is the default.
#  4) Item flags. See header_items.py for a list of available flags.
#  5) Item capabilities. Used for which animations this item is used with. See header_items.py for a list of available flags.
#  6) Item value.
#  7) Item stats: Bitwise-or of various stats about the item such as:
#      weight, abundance, difficulty, head_armor, body_armor,leg_armor, etc...
#  8) Modifier bits: Modifiers that can be applied to this item.
#  9) [Optional] Triggers: List of simple triggers to be associated with the item.
#  10) [Optional] Factions: List of factions that item can be found as merchandise.
####################################################################################################################

# Some constants for ease of use.
imodbits_none = 0
imodbits_horse_basic = imodbit_swaybacked|imodbit_lame|imodbit_spirited|imodbit_heavy|imodbit_stubborn
imodbits_cloth  = imodbit_tattered | imodbit_ragged | imodbit_sturdy | imodbit_thick | imodbit_hardened
imodbits_armor  = imodbit_rusty | imodbit_battered | imodbit_crude | imodbit_thick | imodbit_reinforced |imodbit_lordly
imodbits_plate  = imodbit_cracked | imodbit_rusty | imodbit_battered | imodbit_crude | imodbit_thick | imodbit_reinforced |imodbit_lordly
imodbits_polearm = imodbit_cracked | imodbit_bent | imodbit_balanced
imodbits_shield  = imodbit_cracked | imodbit_battered |imodbit_thick | imodbit_reinforced
imodbits_sword   = imodbit_rusty | imodbit_chipped | imodbit_balanced |imodbit_tempered
imodbits_sword_high   = imodbit_rusty | imodbit_chipped | imodbit_balanced |imodbit_tempered|imodbit_masterwork
imodbits_axe   = imodbit_rusty | imodbit_chipped | imodbit_heavy
imodbits_mace   = imodbit_rusty | imodbit_chipped | imodbit_heavy
imodbits_pick   = imodbit_rusty | imodbit_chipped | imodbit_balanced | imodbit_heavy
imodbits_bow = imodbit_cracked | imodbit_bent | imodbit_strong |imodbit_masterwork
imodbits_crossbow = imodbit_cracked | imodbit_bent | imodbit_masterwork
imodbits_missile   = imodbit_bent | imodbit_large_bag
imodbits_thrown   = imodbit_bent | imodbit_heavy| imodbit_balanced| imodbit_large_bag
imodbits_thrown_minus_heavy = imodbit_bent | imodbit_balanced| imodbit_large_bag

imodbits_horse_good = imodbit_spirited|imodbit_heavy
imodbits_good   = imodbit_sturdy | imodbit_thick | imodbit_hardened | imodbit_reinforced
imodbits_bad    = imodbit_rusty | imodbit_chipped | imodbit_tattered | imodbit_ragged | imodbit_cracked | imodbit_bent
# Replace winged mace/spiked mace with: Flanged mace / Knobbed mace?
# Fauchard (majowski glaive) 
items = [
	["no_item", "INVALID ITEM", [("invalid_item", imodbits_none)], itp_type_one_handed_wpn|itp_primary|itp_secondary, itc_longsword, 3, thrust_damage(10, blunt)|hit_points(16384)|spd_rtng(103)|abundance(100)|weight(1.5)|swing_damage(16, blunt)|weapon_length(90), imodbits_none],

	["tutorial_spear", "Spear", [("light_spear_1", imodbits_none)], itp_type_polearm|itp_wooden_parry|itp_primary|itp_penalty_with_shield, itcf_carry_spear|itc_spear, 0, thrust_damage(19, pierce)|spd_rtng(80)|abundance(100)|weight(4.5)|weapon_length(158), imodbits_polearm],

	["tutorial_club", "Club", [("tutorial_club", imodbits_none)], itp_type_one_handed_wpn|itp_wooden_attack|itp_wooden_parry|itp_primary, itc_scimitar, 0, thrust_damage(0, pierce)|hit_points(11264)|spd_rtng(95)|abundance(100)|weight(2.5)|swing_damage(11, blunt)|weapon_length(95), imodbits_none],

	["tutorial_battle_axe", "Battle Axe", [("mackie_tomahawk", imodbits_none)], itp_type_two_handed_wpn|itp_wooden_parry|itp_two_handed|itp_primary|itp_bonus_against_shield, itcf_carry_axe_back|itc_nodachi, 0, thrust_damage(0, pierce)|hit_points(27648)|spd_rtng(88)|abundance(100)|weight(5.0)|swing_damage(27, cut)|weapon_length(108), imodbits_axe|imodbits_mace],

	["tutorial_arrows", "Arrows", [("we_pla_arrow", imodbits_none), ("flying_missile", ixmesh_flying_ammo), ("we_pla_quiver", ixmesh_carry)], itp_type_arrows, itcf_carry_quiver_back, 0, thrust_damage(0, pierce)|max_ammo(20)|abundance(80)|weight(3.0)|weapon_length(95), imodbits_missile],

	["tutorial_bolts", "Bolts", [("we_rho_bolt", imodbits_none), ("flying_missile", ixmesh_flying_ammo), ("we_rho_bolt_bag", ixmesh_carry), ("we_rho_bolt_bag_b", imodbit_large_bag|ixmesh_carry)], itp_type_bolts, itcf_carry_quiver_right_vertical, 0, thrust_damage(0, pierce)|max_ammo(18)|abundance(60)|weight(2.25)|weapon_length(55), imodbits_missile, 
	[(ti_on_missile_hit,
		[
			(store_trigger_param_1, ":trigger_param_1"),
			(eq, "$g_report_shot_distance", 1),
			(get_player_agent_no, ":player_agent_no"),
			(try_begin),
				(eq, ":trigger_param_1", ":player_agent_no"),
				(agent_get_position, 2, ":trigger_param_1"),
				(agent_get_horse, ":horse_player_agent_no", ":player_agent_no"),
				(try_begin),
					(gt, ":horse_player_agent_no", -1),
					(position_move_z, 2, 220),
				(else_try),
					(position_move_z, 2, 150),
				(try_end),
				(get_distance_between_positions, ":distance_between_positions_1_2", 1, 2),
				(store_div, reg61, ":distance_between_positions_1_2", 100),
				(store_mod, reg62, ":distance_between_positions_1_2", 100),
				(try_begin),
					(lt, reg62, 10),
					(str_store_string, 1, "@{reg61}.0{reg62}"),
				(else_try),
					(str_store_string, 1, "@{reg61}.{reg62}"),
				(try_end),
				(display_message, "@Shot distance: {s1} meters.", 0x00cccccc),
			(try_end)
		])]
	],

	["tutorial_short_bow", "Short Bow", [("we_swa_bow_practice", imodbits_none), ("we_swa_bow_practice_carry", ixmesh_carry)], itp_type_bow|itp_two_handed|itp_primary, itcf_shoot_bow|itcf_carry_bow_back, 0, thrust_damage(12, pierce)|spd_rtng(98)|abundance(100)|weight(1.0)|shoot_speed(49), imodbits_bow],

	["tutorial_crossbow", "Crossbow", [("we_rho_crossbow", imodbits_none)], itp_type_crossbow|itp_cant_reload_on_horseback|itp_two_handed|itp_primary, itcf_shoot_crossbow|itcf_carry_crossbow_back, 0, thrust_damage(32, pierce)|max_ammo(1)|spd_rtng(42)|abundance(100)|weight(3.0)|shoot_speed(68), imodbits_crossbow],

	["tutorial_throwing_daggers", "Throwing Daggers", [("we_vae_sword_throw_daggers", imodbits_none)], itp_type_thrown|itp_primary, itcf_throw_knife, 0, thrust_damage(16, cut)|max_ammo(14)|spd_rtng(102)|abundance(100)|weight(3.5)|shoot_speed(25), imodbits_missile, 
	[(ti_on_missile_hit,
		[
			(store_trigger_param_1, ":trigger_param_1"),
			(eq, "$g_report_shot_distance", 1),
			(get_player_agent_no, ":player_agent_no"),
			(try_begin),
				(eq, ":trigger_param_1", ":player_agent_no"),
				(agent_get_position, 2, ":trigger_param_1"),
				(agent_get_horse, ":horse_player_agent_no", ":player_agent_no"),
				(try_begin),
					(gt, ":horse_player_agent_no", -1),
					(position_move_z, 2, 220),
				(else_try),
					(position_move_z, 2, 150),
				(try_end),
				(get_distance_between_positions, ":distance_between_positions_1_2", 1, 2),
				(store_div, reg61, ":distance_between_positions_1_2", 100),
				(store_mod, reg62, ":distance_between_positions_1_2", 100),
				(try_begin),
					(lt, reg62, 10),
					(str_store_string, 1, "@{reg61}.0{reg62}"),
				(else_try),
					(str_store_string, 1, "@{reg61}.{reg62}"),
				(try_end),
				(display_message, "@Shot distance: {s1} meters.", 0x00cccccc),
			(try_end)
		])]
	],

	["tutorial_saddle_horse", "Saddle Horse", [("new_hunting_horse", imodbits_none)], itp_type_horse, 0, 0, horse_maneuver(38)|abundance(60)|horse_charge(8)|horse_speed(40)|body_armor(3), imodbit_timid|imodbits_horse_basic],

	["tutorial_shield", "Kite Shield", [("witcher_worn_shield", imodbits_none)], itp_type_shield|itp_wooden_parry, itcf_carry_kite_shield, 118, hit_points(480)|spd_rtng(82)|abundance(100)|weight(2.5)|shield_width(150)|body_armor(1), imodbits_shield],

	["tutorial_staff_no_attack", "Staff", [("we_sar_spear_staff", imodbits_none)], itp_type_polearm|itp_wooden_attack|itp_wooden_parry|itp_primary|itp_penalty_with_shield|itp_fit_to_head|itp_offset_lance, itcf_carry_sword_back|itc_parry_polearm, 9, thrust_damage(0, blunt)|spd_rtng(120)|abundance(100)|weight(3.5)|swing_damage(0, blunt)|weapon_length(115), imodbits_none],

	["tutorial_staff", "Staff", [("we_sar_spear_staff", imodbits_none)], itp_type_polearm|itp_wooden_attack|itp_wooden_parry|itp_primary|itp_penalty_with_shield|itp_fit_to_head|itp_offset_lance, itcf_carry_sword_back|itc_staff, 9, thrust_damage(16, blunt)|hit_points(16384)|spd_rtng(120)|abundance(100)|weight(3.5)|swing_damage(16, blunt)|weapon_length(115), imodbits_none],

	["tutorial_sword", "Sword", [("tutorial_sword", imodbits_none), ("tutorial_sword_scabbard", ixmesh_carry)], itp_type_one_handed_wpn|itp_primary, itcf_carry_sword_left_hip|itcf_show_holster_when_drawn|itc_longsword, 0, thrust_damage(15, pierce)|hit_points(18432)|spd_rtng(100)|abundance(100)|weight(1.5)|swing_damage(18, cut)|weapon_length(102), imodbits_sword],

	["tutorial_axe", "Axe", [("tutorial_axe", imodbits_none)], itp_type_two_handed_wpn|itp_wooden_parry|itp_two_handed|itp_primary|itp_bonus_against_shield, itcf_carry_axe_back|itc_nodachi, 0, thrust_damage(0, pierce)|hit_points(19456)|spd_rtng(91)|abundance(100)|weight(4.0)|swing_damage(19, cut)|weapon_length(108), imodbits_axe|imodbits_mace],

	["tutorial_dagger", "Dagger", [("practice_dagger", imodbits_none)], itp_type_one_handed_wpn|itp_primary|itp_secondary, itc_longsword, 3, thrust_damage(10, blunt)|hit_points(16384)|spd_rtng(103)|abundance(100)|weight(1.5)|swing_damage(16, blunt)|weapon_length(40), imodbits_none],

	["horse_meat", "Horse Meat", [("trade_cattle_meat", imodbits_none)], itp_type_goods|itp_food|itp_consumable, 0, 12, max_ammo(40)|abundance(50)|weight(40.0)|food_quality(30), imodbits_none, [], [fac_kingdom_3]],

	["practice_lance", "Tourney Lance", [("light_spear_1", imodbits_none)], itp_type_polearm|itp_wooden_parry|itp_primary|itp_penalty_with_shield|itp_fit_to_head|itp_offset_lance|itp_covers_head|itp_couchable, itc_staff, 90, thrust_damage(35, pierce)|spd_rtng(96)|abundance(100)|weight(4.0)|swing_damage(0, blunt)|weapon_length(150), imodbits_polearm, [], [fac_kingdom_1, fac_kingdom_8, fac_kingdom_9, fac_kingdom_10, fac_kingdom_20]],

	["practice_axe", "Blunt Tourney Axe", [("mackie_tomahawk", imodbits_none)], itp_type_one_handed_wpn|itp_wooden_parry|itp_primary|itp_bonus_against_shield, itcf_carry_axe_left_hip|itc_scimitar, 500, thrust_damage(0, pierce)|hit_points(28672)|spd_rtng(85)|abundance(100)|weight(2.0)|swing_damage(28, blunt)|weapon_length(70), imodbits_axe|imodbits_mace, [], [fac_kingdom_12, fac_kingdom_13, fac_kingdom_14, fac_kingdom_15, fac_kingdom_16, fac_kingdom_5, fac_kingdom_17, fac_kingdom_18]],

	["practice_dagger", "Blunt Tourney Mace", [("mace_spiral", imodbits_none)], itp_type_one_handed_wpn|itp_wooden_parry|itp_primary|itp_bonus_against_shield|itp_crush_through|itp_can_knock_down, itcf_carry_mace_left_hip|itc_scimitar, 600, thrust_damage(0, pierce)|hit_points(29696)|spd_rtng(80)|abundance(100)|weight(4.0)|swing_damage(29, blunt)|difficulty(12)|weapon_length(70), imodbits_axe|imodbits_mace, [], [fac_kingdom_1, fac_kingdom_2, fac_kingdom_3, fac_kingdom_5, fac_kingdom_8]],

	["practice_staff", "Blunt Tourney Sword", [("medium_tier_sword_2", imodbits_none), ("medium_tier_sword_2_scab", ixmesh_carry)], itp_type_one_handed_wpn|itp_primary, itcf_carry_sword_left_hip|itcf_show_holster_when_drawn|itc_longsword, 1000, thrust_damage(28, pierce)|hit_points(26624)|spd_rtng(100)|abundance(70)|weight(2.0)|swing_damage(26, blunt)|difficulty(10)|weapon_length(95), imodbits_sword_high, [], [fac_kingdom_1, fac_kingdom_8, fac_kingdom_9, fac_kingdom_10, fac_kingdom_20]],

	["practice_sword", "Blunt Tourney Sword", [("medium_tier_sword_2", imodbits_none), ("medium_tier_sword_2_scab", ixmesh_carry)], itp_type_one_handed_wpn|itp_primary, itcf_carry_sword_left_hip|itcf_show_holster_when_drawn|itc_longsword, 1000, thrust_damage(28, pierce)|hit_points(26624)|spd_rtng(100)|abundance(70)|weight(2.0)|swing_damage(26, blunt)|difficulty(10)|weapon_length(95), imodbits_sword_high, [], [fac_kingdom_1, fac_kingdom_8, fac_kingdom_9, fac_kingdom_10, fac_kingdom_20]],

	["practice_sword_heavy", "Blunt Tourney Mace", [("mace_spiral", imodbits_none)], itp_type_one_handed_wpn|itp_wooden_parry|itp_primary|itp_bonus_against_shield|itp_crush_through|itp_can_knock_down, itcf_carry_mace_left_hip|itc_scimitar, 600, thrust_damage(0, pierce)|hit_points(29696)|spd_rtng(80)|abundance(100)|weight(4.0)|swing_damage(29, blunt)|difficulty(12)|weapon_length(70), imodbits_axe|imodbits_mace, [], [fac_kingdom_1, fac_kingdom_2, fac_kingdom_3, fac_kingdom_5, fac_kingdom_8]],

	["practice_arrows", "Blunt Tourney Sword", [("medium_tier_sword_2", imodbits_none), ("medium_tier_sword_2_scab", ixmesh_carry)], itp_type_one_handed_wpn|itp_primary, itcf_carry_sword_left_hip|itcf_show_holster_when_drawn|itc_longsword, 1000, thrust_damage(28, pierce)|hit_points(26624)|spd_rtng(100)|abundance(70)|weight(2.0)|swing_damage(26, blunt)|difficulty(10)|weapon_length(95), imodbits_sword_high, [], [fac_kingdom_1, fac_kingdom_8, fac_kingdom_9, fac_kingdom_10, fac_kingdom_20]],

	["practice_arrows_10_amount", "Blunt Tourney Sword", [("medium_tier_sword_2", imodbits_none), ("medium_tier_sword_2_scab", ixmesh_carry)], itp_type_one_handed_wpn|itp_primary, itcf_carry_sword_left_hip|itcf_show_holster_when_drawn|itc_longsword, 1000, thrust_damage(28, pierce)|hit_points(26624)|spd_rtng(100)|abundance(70)|weight(2.0)|swing_damage(26, blunt)|difficulty(10)|weapon_length(95), imodbits_sword_high, [], [fac_kingdom_1, fac_kingdom_8, fac_kingdom_9, fac_kingdom_10, fac_kingdom_20]],

	["practice_arrows_100_amount", "Blunt Tourney Sword", [("medium_tier_sword_2", imodbits_none), ("medium_tier_sword_2_scab", ixmesh_carry)], itp_type_one_handed_wpn|itp_primary, itcf_carry_sword_left_hip|itcf_show_holster_when_drawn|itc_longsword, 1000, thrust_damage(28, pierce)|hit_points(26624)|spd_rtng(100)|abundance(70)|weight(2.0)|swing_damage(26, blunt)|difficulty(10)|weapon_length(95), imodbits_sword_high, [], [fac_kingdom_1, fac_kingdom_8, fac_kingdom_9, fac_kingdom_10, fac_kingdom_20]],

	["practice_bolts", "Blunt Tourney Sword", [("medium_tier_sword_2", imodbits_none), ("medium_tier_sword_2_scab", ixmesh_carry)], itp_type_one_handed_wpn|itp_primary, itcf_carry_sword_left_hip|itcf_show_holster_when_drawn|itc_longsword, 1000, thrust_damage(28, pierce)|hit_points(26624)|spd_rtng(100)|abundance(70)|weight(2.0)|swing_damage(26, blunt)|difficulty(10)|weapon_length(95), imodbits_sword_high, [], [fac_kingdom_1, fac_kingdom_8, fac_kingdom_9, fac_kingdom_10, fac_kingdom_20]],

	["practice_bolts_9_amount", "Blunt Tourney Mace", [("mace_spiral", imodbits_none)], itp_type_one_handed_wpn|itp_wooden_parry|itp_primary|itp_bonus_against_shield|itp_crush_through|itp_can_knock_down, itcf_carry_mace_left_hip|itc_scimitar, 600, thrust_damage(0, pierce)|hit_points(29696)|spd_rtng(80)|abundance(100)|weight(4.0)|swing_damage(29, blunt)|difficulty(12)|weapon_length(70), imodbits_axe|imodbits_mace, [], [fac_kingdom_1, fac_kingdom_2, fac_kingdom_3, fac_kingdom_5, fac_kingdom_8]],

	["practice_bow", "Tourney Lance", [("light_spear_1", imodbits_none)], itp_type_polearm|itp_wooden_parry|itp_primary|itp_penalty_with_shield|itp_fit_to_head|itp_offset_lance|itp_covers_head|itp_couchable, itc_staff, 90, thrust_damage(35, pierce)|spd_rtng(96)|abundance(100)|weight(4.0)|swing_damage(0, blunt)|weapon_length(150), imodbits_polearm, [], [fac_kingdom_1, fac_kingdom_8, fac_kingdom_9, fac_kingdom_10, fac_kingdom_20]],

	["practice_crossbow", "Tourney Lance", [("light_spear_1", imodbits_none)], itp_type_polearm|itp_wooden_parry|itp_primary|itp_penalty_with_shield|itp_fit_to_head|itp_offset_lance|itp_covers_head|itp_couchable, itc_staff, 90, thrust_damage(35, pierce)|spd_rtng(96)|abundance(100)|weight(4.0)|swing_damage(0, blunt)|weapon_length(150), imodbits_polearm, [], [fac_kingdom_1, fac_kingdom_8, fac_kingdom_9, fac_kingdom_10, fac_kingdom_20]],

	["practice_javelin", "Tourney Lance", [("light_spear_1", imodbits_none)], itp_type_polearm|itp_wooden_parry|itp_primary|itp_penalty_with_shield|itp_fit_to_head|itp_offset_lance|itp_covers_head|itp_couchable, itc_staff, 90, thrust_damage(35, pierce)|spd_rtng(96)|abundance(100)|weight(4.0)|swing_damage(0, blunt)|weapon_length(150), imodbits_polearm, [], [fac_kingdom_1, fac_kingdom_8, fac_kingdom_9, fac_kingdom_10, fac_kingdom_20]],

	["practice_javelin_melee", "Tourney Lance", [("light_spear_1", imodbits_none)], itp_type_polearm|itp_wooden_parry|itp_primary|itp_penalty_with_shield|itp_fit_to_head|itp_offset_lance|itp_covers_head|itp_couchable, itc_staff, 90, thrust_damage(35, pierce)|spd_rtng(96)|abundance(100)|weight(4.0)|swing_damage(0, blunt)|weapon_length(150), imodbits_polearm, [], [fac_kingdom_1, fac_kingdom_8, fac_kingdom_9, fac_kingdom_10, fac_kingdom_20]],

	["practice_throwing_daggers", "Blunt Tourney Mace", [("mace_spiral", imodbits_none)], itp_type_one_handed_wpn|itp_wooden_parry|itp_primary|itp_bonus_against_shield|itp_crush_through|itp_can_knock_down, itcf_carry_mace_left_hip|itc_scimitar, 600, thrust_damage(0, pierce)|hit_points(29696)|spd_rtng(80)|abundance(100)|weight(4.0)|swing_damage(29, blunt)|difficulty(12)|weapon_length(70), imodbits_axe|imodbits_mace, [], [fac_kingdom_1, fac_kingdom_2, fac_kingdom_3, fac_kingdom_5, fac_kingdom_8]],

	["practice_throwing_daggers_100_amount", "Blunt Tourney Mace", [("mace_spiral", imodbits_none)], itp_type_one_handed_wpn|itp_wooden_parry|itp_primary|itp_bonus_against_shield|itp_crush_through|itp_can_knock_down, itcf_carry_mace_left_hip|itc_scimitar, 600, thrust_damage(0, pierce)|hit_points(29696)|spd_rtng(80)|abundance(100)|weight(4.0)|swing_damage(29, blunt)|difficulty(12)|weapon_length(70), imodbits_axe|imodbits_mace, [], [fac_kingdom_1, fac_kingdom_2, fac_kingdom_3, fac_kingdom_5, fac_kingdom_8]],

	["practice_boots", "Practice Boots", [("bo_vae_t3_leather", imodbits_none)], itp_type_foot_armor|itp_attach_armature|itp_attachment_mask|itp_civilian|itp_next_item_as_melee, 0, 11, abundance(60)|weight(1.0)|leg_armor(10), imodbits_cloth],

	["practice_horse", "Practice Horse", [("new_hunting_horse", imodbits_none)], itp_type_horse, 0, 37, horse_maneuver(37)|abundance(100)|horse_charge(14)|horse_speed(40)|body_armor(10), imodbits_none],

	["practice_shield", "Practice Shield", [("witcher_worn_shield", imodbits_none)], itp_type_shield|itp_wooden_parry, itcf_carry_round_shield, 20, hit_points(200)|spd_rtng(100)|abundance(100)|weight(3.5)|shield_width(50)|body_armor(1), imodbits_none],

	["book_tactics", "A Compendium on the Blackfyre Rebellions", [("bk_book_01", imodbits_none)], itp_type_book, 0, 4000, abundance(60)|weight(2.0), imodbits_none],

	["book_persuasion", "The Conquest of Dorne", [("bk_book_01", imodbits_none)], itp_type_book, 0, 5000, abundance(60)|weight(2.0), imodbits_none],

	["book_leadership", "Life of Aegon the Conqueror", [("bk_book_01", imodbits_none)], itp_type_book, 0, 4200, abundance(60)|weight(2.0), imodbits_none],

	["book_intelligence", "Essay on Logic by Grand Maester Gerardys", [("bk_book_01", imodbits_none)], itp_type_book, 0, 2900, abundance(60)|weight(2.0), imodbits_none],

	["book_trade", "A History of the Iron Bank of Braavos", [("bk_book_01", imodbits_none)], itp_type_book, 0, 3100, abundance(60)|weight(2.0), imodbits_none],

	["book_weapon_mastery", "On the Art of Fighting with Swords", [("bk_book_01", imodbits_none)], itp_type_book, 0, 4200, abundance(60)|weight(2.0), imodbits_none],

	["book_engineering", "The War of Volantene Aggression", [("bk_book_01", imodbits_none)], itp_type_book, 0, 4000, abundance(60)|weight(2.0), imodbits_none],

	["book_necronomicon", "The Great Book of Magic", [("bk_book_01", imodbits_none)], itp_type_book, 0, 5000, abundance(60)|weight(2.0), imodbits_none],

	["book_bible", "The Seven-Pointed Star", [("bk_book_01", imodbits_none)], itp_type_book, 0, 4500, abundance(60)|weight(2.0), imodbits_none],

	["book_prisoner_management", "The Diary of Gralmaq mo Eraz", [("bk_book_01", imodbits_none)], itp_type_book, 0, 5000, abundance(60)|weight(2.0), imodbits_none],

	["book_spotting_reference", "Wonders Made by Man", [("bk_book_01", imodbits_none)], itp_type_book, 0, 3500, abundance(60)|weight(2.0), imodbits_none],

	["book_first_aid_reference", "A Short Treatise on the Great Spring Sickness", [("bk_book_01", imodbits_none)], itp_type_book, 0, 3500, abundance(60)|weight(2.0), imodbits_none],

	["book_pathfinding_reference", "Map of the Known World", [("bk_book_01", imodbits_none)], itp_type_book, 0, 3500, abundance(60)|weight(2.0), imodbits_none],

	["book_wound_treatment_reference", "The Book of Healing", [("bk_book_01", imodbits_none)], itp_type_book, 0, 3500, abundance(60)|weight(2.0), imodbits_none],

	["book_training_reference", "On the Unsullied", [("bk_book_01", imodbits_none)], itp_type_book, 0, 3500, abundance(60)|weight(2.0), imodbits_none],

	["book_surgery_reference", "On the Citadel and Surgery", [("bk_book_01", imodbits_none)], itp_type_book, 0, 3500, abundance(60)|weight(2.0), imodbits_none],

	["book_trade_ledger", "Merchant's Ledger", [("book_open", imodbits_none)], itp_type_book, 0, 3500, abundance(60)|weight(2.0), imodbits_none],

	["trade_spice", "Jar of Spices", [("trade_spice", imodbits_none)], itp_type_goods|itp_merchandise|itp_consumable, 0, 880, max_ammo(50)|abundance(25)|weight(40.0), imodbit_fine|imodbit_exquisite],

	["trade_salt", "Bag of Salt", [("trade_salt", imodbits_none)], itp_type_goods|itp_merchandise, 0, 255, abundance(120)|weight(50.0), imodbit_fine],

	["trade_oil", "Jar of Oil", [("trade_oil", imodbits_none)], itp_type_goods|itp_merchandise|itp_consumable, 0, 450, max_ammo(50)|abundance(60)|weight(50.0), imodbit_cheap|imodbit_fine|imodbit_well_made],

	["trade_pottery", "Pottery", [("jug_new", imodbits_none)], itp_type_goods|itp_merchandise, 0, 100, abundance(90)|weight(50.0), imodbit_cracked|imodbit_crude|imodbit_old|imodbit_cheap|imodbit_fine|imodbit_well_made|imodbit_masterwork|imodbit_rough|imodbit_sturdy],

	["trade_raw_flax", "Flax Bundle", [("trade_raw_flax", imodbits_none)], itp_type_goods|itp_merchandise, 0, 150, abundance(90)|weight(40.0), imodbit_fine],

	["trade_linen", "Linen Bundle", [("trade_linen", imodbits_none)], itp_type_goods|itp_merchandise, 0, 250, abundance(90)|weight(40.0), imodbit_cheap|imodbit_fine|imodbit_well_made|imodbit_masterwork|imodbit_tattered|imodbit_ragged|imodbit_rough|imodbit_sturdy],

	["trade_wool", "Bag of Raw Wool", [("trade_wool", imodbits_none)], itp_type_goods|itp_merchandise, 0, 130, abundance(90)|weight(40.0), imodbit_fine],

	["trade_wool_cloth", "Wool Cloth", [("trade_wool_cloth", imodbits_none)], itp_type_goods|itp_merchandise, 0, 250, abundance(90)|weight(40.0), imodbit_cheap|imodbit_fine|imodbit_well_made|imodbit_masterwork|imodbit_tattered|imodbit_ragged|imodbit_rough|imodbit_sturdy],

	["trade_raw_silk", "Raw Silk", [("trade_raw_silk", imodbits_none)], itp_type_goods|itp_merchandise, 0, 600, abundance(90)|weight(30.0), imodbit_fine|imodbit_exquisite],

	["trade_raw_dyes", "Bowl of Dyes", [("trade_raw_dyes", imodbits_none)], itp_type_goods|itp_merchandise, 0, 200, abundance(90)|weight(10.0), imodbit_fine|imodbit_well_made|imodbit_exquisite|imodbit_masterwork],

	["trade_velvet", "Velvet Bundle", [("trade_velvet", imodbits_none)], itp_type_goods|itp_merchandise, 0, 1025, abundance(30)|weight(40.0), imodbit_fine|imodbit_well_made|imodbit_masterwork],

	["trade_iron", "Iron Bar", [("trade_iron", imodbits_none)], itp_type_goods|itp_merchandise, 0, 264, abundance(60)|weight(60.0), imodbit_rusty|imodbit_poor|imodbit_well_made|imodbit_tempered|imodbit_hardened],

	["trade_tools", "Tools", [("trade_tools", imodbits_none)], itp_type_goods|itp_merchandise, 0, 410, abundance(90)|weight(50.0), imodbit_rusty|imodbit_crude|imodbit_old|imodbit_cheap|imodbit_fine|imodbit_well_made|imodbit_masterwork|imodbit_sturdy|imodbit_hardened],

	["trade_raw_leather", "Hides", [("trade_raw_leather", imodbits_none)], itp_type_goods|itp_merchandise, 0, 120, abundance(90)|weight(40.0), imodbit_fine|imodbit_exquisite|imodbit_tattered|imodbit_ragged|imodbit_sturdy|imodbit_thick],

	["trade_leatherwork", "Leatherwork", [("trade_leatherwork", imodbits_none)], itp_type_goods|itp_merchandise, 0, 220, abundance(90)|weight(40.0), imodbit_cheap|imodbit_fine|imodbit_well_made|imodbit_masterwork|imodbit_tattered|imodbit_ragged|imodbit_rough|imodbit_sturdy|imodbit_thick],

	["trade_raw_date_fruit", "Date Fruit", [("trade_raw_date_fruit", imodbits_none)], itp_type_goods|itp_merchandise|itp_food|itp_consumable, 0, 120, max_ammo(10)|abundance(100)|weight(40.0)|food_quality(10), imodbit_cheap|imodbit_fine],

	["trade_furs", "Fur Bundle", [("trade_furs", imodbits_none)], itp_type_goods|itp_merchandise, 0, 391, abundance(90)|weight(40.0), imodbit_cheap|imodbit_fine|imodbit_tattered|imodbit_ragged|imodbit_sturdy|imodbit_thick],

	["trade_wine", "Jar of Wine", [("trade_wine", imodbits_none)], itp_type_goods|itp_merchandise|itp_consumable, 0, 220, max_ammo(50)|abundance(60)|weight(30.0), imodbit_cheap|imodbit_fine|imodbit_well_made|imodbit_strong],

	["trade_ale", "Barrel of Ale", [("trade_ale", imodbits_none)], itp_type_goods|itp_merchandise|itp_consumable, 0, 120, max_ammo(50)|abundance(70)|weight(30.0), imodbit_cheap|imodbit_fine|imodbit_well_made|imodbit_strong],

	["market_gold_chalice", "Gold Chalice", [("market_gold_chalice", imodbits_none)], itp_type_goods|itp_merchandise, 0, 1066, abundance(90)|weight(50.0), imodbit_fine|imodbit_well_made|imodbit_exquisite|imodbit_masterwork],

	["market_lemon_basket", "Basket of Lemons", [("market_lemon_basket", imodbits_none)], itp_type_goods|itp_merchandise|itp_food|itp_consumable, 0, 100, max_ammo(50)|abundance(110)|weight(20.0)|food_quality(40), imodbit_cheap],

	["market_plum_basket", "Basket of Plums", [("market_plum_basket", imodbits_none)], itp_type_goods|itp_merchandise|itp_food|itp_consumable, 0, 80, max_ammo(50)|abundance(110)|weight(20.0)|food_quality(40), imodbit_cheap],

	["market_dornish_wine", "Crate of Dornish Wine", [("market_dornish_wine", imodbits_none)], itp_type_goods|itp_merchandise|itp_consumable, 0, 300, max_ammo(50)|abundance(60)|weight(30.0), imodbit_exquisite|imodbit_strong],

	["market_pear_basket", "Basket of Pears", [("market_pear_basket", imodbits_none)], itp_type_goods|itp_merchandise|itp_food|itp_consumable, 0, 44, max_ammo(50)|abundance(110)|weight(20.0)|food_quality(40), imodbit_cheap],

	["market_apple_basket", "Basket of Apples", [("market_apple_basket", imodbits_none)], itp_type_goods|itp_merchandise|itp_food|itp_consumable, 0, 44, max_ammo(50)|abundance(110)|weight(20.0)|food_quality(40), imodbit_cheap],

	["market_arbor_red", "Jar of Arbor Wine", [("market_arbor_red", imodbits_none)], itp_type_goods|itp_merchandise|itp_consumable, 0, 900, max_ammo(50)|abundance(60)|weight(30.0), imodbit_exquisite|imodbit_strong],

	["market_candles", "Candles", [("market_candles", imodbits_none)], itp_type_goods|itp_merchandise|itp_consumable, 0, 150, max_ammo(50)|abundance(60)|weight(30.0), imodbit_cheap],

	["market_pumpkins", "Pumpkin", [("market_pumpkin", imodbits_none)], itp_type_goods|itp_merchandise|itp_food|itp_consumable, 0, 25, max_ammo(50)|abundance(110)|weight(20.0)|food_quality(40), imodbit_cheap],

	["market_lead", "Lead Ingot", [("market_lead", imodbits_none)], itp_type_goods|itp_merchandise, 0, 154, abundance(60)|weight(60.0), imodbit_rusty|imodbit_poor|imodbit_well_made|imodbit_tempered|imodbit_hardened],

	["market_tin", "Tin Ingot", [("market_tin", imodbits_none)], itp_type_goods|itp_merchandise, 0, 100, abundance(60)|weight(60.0), imodbit_rusty|imodbit_poor|imodbit_well_made|imodbit_tempered|imodbit_hardened],

	["market_coal", "Crate of Coal", [("market_coal", imodbits_none)], itp_type_goods|itp_merchandise, 0, 89, abundance(60)|weight(60.0), imodbit_rusty|imodbit_poor|imodbit_well_made|imodbit_tempered|imodbit_hardened],

	["market_silver_chalice", "Silver Chalice", [("market_silver_chalice", imodbits_none)], itp_type_goods|itp_merchandise, 0, 533, abundance(90)|weight(50.0), imodbit_fine|imodbit_well_made|imodbit_exquisite|imodbit_masterwork],

	["market_pentoshi_wine", "Jar of Pentoshi Wine", [("market_pentoshi_wine", imodbits_none)], itp_type_goods|itp_merchandise, 0, 400, abundance(90)|weight(50.0), imodbit_exquisite|imodbit_strong],

	["market_lyseni_wine", "Jar of Lyseni Wine", [("market_lyseni_wine", imodbits_none)], itp_type_goods|itp_merchandise, 0, 450, abundance(90)|weight(50.0), imodbit_exquisite|imodbit_strong],

	["market_qohorik_carpets", "Qohorik Carpets", [("market_qohorik_carpets", imodbits_none)], itp_type_goods|itp_merchandise, 0, 600, abundance(90)|weight(50.0), imodbit_fine|imodbit_well_made|imodbit_exquisite|imodbit_masterwork],

	["market_bronzewood", "Bronzewood", [("market_bronzewood", imodbits_none)], itp_type_goods|itp_merchandise, 0, 200, abundance(90)|weight(50.0), imodbit_fine],

	["market_myrish_carpets", "Myrish Carpets", [("market_myrish_carpets", imodbits_none)], itp_type_goods|itp_merchandise, 0, 700, abundance(90)|weight(50.0), imodbit_fine|imodbit_well_made|imodbit_exquisite|imodbit_masterwork],

	["market_tyroshi_pear_brandy", "Bottle of Tyroshi Pear Brandy", [("market_tyroshi_pear_brandy", imodbits_none)], itp_type_goods|itp_merchandise, 0, 150, abundance(90)|weight(50.0), imodbit_exquisite|imodbit_strong],

	["market_volantene_wine", "Bottle of Volantene Wine", [("market_volantene_wine", imodbits_none)], itp_type_goods|itp_merchandise, 0, 350, abundance(90)|weight(50.0), imodbit_exquisite|imodbit_strong],

	["market_ironwood", "Ironwood", [("market_ironwood", imodbits_none)], itp_type_goods|itp_merchandise, 0, 300, abundance(90)|weight(50.0), imodbit_fine],

	["market_persimmon_wine", "Bottle of Persimmon Wine", [("market_persimmon_wine", imodbits_none)], itp_type_goods|itp_merchandise, 0, 350, abundance(90)|weight(50.0), imodbit_exquisite|imodbit_strong],

	["market_perfume", "Bottle of Perfume", [("market_perfume", imodbits_none)], itp_type_goods|itp_merchandise, 0, 470, abundance(90)|weight(50.0), imodbit_exquisite|imodbit_strong],

	["trade_smoked_fish", "Smoked Fish", [("trade_smoked_fish", imodbits_none)], itp_type_goods|itp_merchandise|itp_food|itp_consumable, 0, 65, max_ammo(50)|abundance(110)|weight(15.0)|food_quality(50), imodbit_cheap|imodbit_fine|imodbit_well_made|imodbit_exquisite],

	["trade_cheese", "Cheese", [("cheese_b_new", imodbits_none)], itp_type_goods|itp_merchandise|itp_food|itp_consumable, 0, 75, max_ammo(30)|abundance(110)|weight(6.0)|food_quality(40), imodbit_cheap|imodbit_fine|imodbit_well_made|imodbit_exquisite],

	["trade_honey", "Jar of Honey", [("necturus_food_honey", imodbits_none)], itp_type_goods|itp_merchandise|itp_food|itp_consumable, 0, 220, max_ammo(30)|abundance(110)|weight(5.0)|food_quality(40), imodbit_cheap|imodbit_fine|imodbit_exquisite],

	["trade_sausages", "Sausages", [("necturus_food_sausage_many", imodbits_none)], itp_type_goods|itp_merchandise|itp_food|itp_consumable, 0, 85, max_ammo(40)|abundance(110)|weight(10.0)|food_quality(40), imodbit_cheap|imodbit_fine|imodbit_well_made|imodbit_exquisite],

	["trade_cabbages", "Cabbages", [("cabbage_new", imodbits_none)], itp_type_goods|itp_merchandise|itp_food|itp_consumable, 0, 30, max_ammo(50)|abundance(110)|weight(15.0)|food_quality(40), imodbit_cheap|imodbit_fine|imodbit_exquisite],

	["trade_dried_meat", "Dried Meat", [("trade_dried_meat", imodbits_none)], itp_type_goods|itp_merchandise|itp_food|itp_consumable, 0, 85, max_ammo(50)|abundance(100)|weight(15.0)|food_quality(70), imodbit_cheap|imodbit_fine|imodbit_well_made|imodbit_exquisite],

	["trade_apples", "Basket of Fruit", [("apple_basket", imodbits_none)], itp_type_goods|itp_merchandise|itp_food|itp_consumable, 0, 44, max_ammo(50)|abundance(110)|weight(20.0)|food_quality(40), imodbit_cheap|imodbit_fine|imodbit_exquisite],

	["trade_raw_grapes", "Grapes", [("grapes_inventory_new", imodbits_none)], itp_type_goods|itp_merchandise|itp_consumable, 0, 75, max_ammo(10)|abundance(90)|weight(40.0)|head_armor(10), imodbit_cheap|imodbit_fine|imodbit_exquisite],

	["trade_raw_olives", "Olives", [("trade_raw_olives", imodbits_none)], itp_type_goods|itp_merchandise|itp_consumable, 0, 100, max_ammo(10)|abundance(90)|weight(40.0)|head_armor(10), imodbit_cheap|imodbit_fine|imodbit_exquisite],

	["trade_grain", "Bag of Grain", [("trade_grain", imodbits_none)], itp_type_goods|itp_merchandise|itp_consumable, 0, 30, max_ammo(50)|abundance(110)|weight(30.0)|head_armor(40), imodbit_cheap|imodbit_fine|imodbit_exquisite],

	["trade_cattle_meat", "Beef", [("trade_cattle_meat", imodbits_none)], itp_type_goods|itp_merchandise|itp_food|itp_consumable, 0, 80, max_ammo(50)|abundance(100)|weight(20.0)|food_quality(80), imodbits_none],

	["trade_bread", "Bread", [("bread_a_new", imodbits_none)], itp_type_goods|itp_merchandise|itp_food|itp_consumable, 0, 50, max_ammo(50)|abundance(110)|weight(30.0)|food_quality(40), imodbit_cheap|imodbit_fine|imodbit_well_made|imodbit_exquisite],

	["trade_chicken", "Chicken", [("trade_chicken_new", imodbits_none)], itp_type_goods|itp_merchandise|itp_food|itp_consumable, 0, 95, max_ammo(50)|abundance(110)|weight(10.0)|food_quality(40), imodbits_none],

	["trade_pork", "Pork", [("trade_pork_new", imodbits_none)], itp_type_goods|itp_merchandise|itp_food|itp_consumable, 0, 75, max_ammo(50)|abundance(100)|weight(15.0)|food_quality(70), imodbits_none],

	["trade_butter", "Jar of Butter", [("necturus_ceramic_container_2", imodbits_none)], itp_type_goods|itp_merchandise|itp_food|itp_consumable, 0, 150, max_ammo(30)|abundance(110)|weight(6.0)|food_quality(40), imodbit_cheap|imodbit_fine|imodbit_well_made|imodbit_exquisite],

	["trade_dummy01", "Dummy item 1", [("trade_spice", imodbits_none)], itp_type_goods|itp_consumable, 0, 880, max_ammo(50)|abundance(25)|weight(40.0), imodbits_none],

	["trade_dummy02", "Dummy item 2", [("trade_spice", imodbits_none)], itp_type_goods|itp_consumable, 0, 880, max_ammo(50)|abundance(25)|weight(40.0), imodbits_none],

	["trade_dummy03", "Dummy item 3", [("trade_spice", imodbits_none)], itp_type_goods|itp_consumable, 0, 880, max_ammo(50)|abundance(25)|weight(40.0), imodbits_none],

	["trade_dummy04", "Dummy item 4", [("trade_spice", imodbits_none)], itp_type_goods|itp_consumable, 0, 880, max_ammo(50)|abundance(25)|weight(40.0), imodbits_none],

	["trade_dummy05", "Dummy item 5", [("trade_spice", imodbits_none)], itp_type_goods|itp_consumable, 0, 880, max_ammo(50)|abundance(25)|weight(40.0), imodbits_none],

	["trade_dummy06", "Dummy item 6", [("trade_spice", imodbits_none)], itp_type_goods|itp_consumable, 0, 880, max_ammo(50)|abundance(25)|weight(40.0), imodbits_none],

	["trade_dummy07", "Dummy item 7", [("trade_spice", imodbits_none)], itp_type_goods|itp_consumable, 0, 880, max_ammo(50)|abundance(25)|weight(40.0), imodbits_none],

	["trade_dummy08", "Dummy item 8", [("trade_spice", imodbits_none)], itp_type_goods|itp_consumable, 0, 880, max_ammo(50)|abundance(25)|weight(40.0), imodbits_none],

	["trade_dummy09", "Dummy item 9", [("trade_spice", imodbits_none)], itp_type_goods|itp_consumable, 0, 880, max_ammo(50)|abundance(25)|weight(40.0), imodbits_none],

	["trade_dummy10", "Dummy item 10", [("trade_spice", imodbits_none)], itp_type_goods|itp_consumable, 0, 880, max_ammo(50)|abundance(25)|weight(40.0), imodbits_none],

	["trade_dummy11", "Dummy item 11", [("trade_spice", imodbits_none)], itp_type_goods|itp_consumable, 0, 880, max_ammo(50)|abundance(25)|weight(40.0), imodbits_none],

	["trade_dummy12", "Dummy item 12", [("trade_spice", imodbits_none)], itp_type_goods|itp_consumable, 0, 880, max_ammo(50)|abundance(25)|weight(40.0), imodbits_none],

	["trade_dummy13", "Dummy item 13", [("trade_spice", imodbits_none)], itp_type_goods|itp_consumable, 0, 880, max_ammo(50)|abundance(25)|weight(40.0), imodbits_none],

	["trade_dummy14", "Dummy item 14", [("trade_spice", imodbits_none)], itp_type_goods|itp_consumable, 0, 880, max_ammo(50)|abundance(25)|weight(40.0), imodbits_none],

	["trade_dummy15", "Dummy item 15", [("trade_spice", imodbits_none)], itp_type_goods|itp_consumable, 0, 880, max_ammo(50)|abundance(25)|weight(40.0), imodbits_none],

	["trade_dummy16", "Dummy item 16", [("trade_spice", imodbits_none)], itp_type_goods|itp_consumable, 0, 880, max_ammo(50)|abundance(25)|weight(40.0), imodbits_none],

	["trade_dummy17", "Dummy item 17", [("trade_spice", imodbits_none)], itp_type_goods|itp_consumable, 0, 880, max_ammo(50)|abundance(25)|weight(40.0), imodbits_none],

	["trade_dummy18", "Dummy item 18", [("trade_spice", imodbits_none)], itp_type_goods|itp_consumable, 0, 880, max_ammo(50)|abundance(25)|weight(40.0), imodbits_none],

	["trade_dummy19", "Dummy item 19", [("trade_spice", imodbits_none)], itp_type_goods|itp_consumable, 0, 880, max_ammo(50)|abundance(25)|weight(40.0), imodbits_none],

	["trade_dummy20", "Dummy item 20", [("trade_spice", imodbits_none)], itp_type_goods|itp_consumable, 0, 880, max_ammo(50)|abundance(25)|weight(40.0), imodbits_none],

	["dragon_coin", "Gold Dragon", [("dragon_coin", imodbits_none)], itp_type_goods, 0, 1050, abundance(25)|weight(40.0), imodbits_none],

	["dragon_coin_many", "Gold Dragons", [("dragon_coin_many", imodbits_none)], itp_type_goods, 0, 25200, abundance(25)|weight(40.0), imodbits_none],

	["honor", "Gold Honor", [("honor", imodbits_none)], itp_type_goods, 0, 2100, abundance(25)|weight(40.0), imodbits_none],

	["honor_many", "Gold Honors", [("honor_many", imodbits_none)], itp_type_goods, 0, 50400, abundance(25)|weight(40.0), imodbits_none],

	["groat", "Groat", [("honor_many", imodbits_none)], itp_type_goods, 0, 5, abundance(25)|weight(40.0), imodbits_none],

	["groat_many", "Groats", [("honor_many", imodbits_none)], itp_type_goods, 0, 120, abundance(25)|weight(40.0), imodbits_none],

	["lumber", "Lumber", [("timber", imodbits_none)], itp_type_goods|itp_merchandise, 0, 100, abundance(90)|weight(50.0), imodbits_none],

	["ring_1", "Gold Ring", [("ring_1", imodbits_none)], itp_type_goods, 0, 4000, abundance(25)|weight(40.0), imodbits_none],

	["ring_2", "Gold Ring", [("ring_2", imodbits_none)], itp_type_goods, 0, 2000, abundance(25)|weight(40.0), imodbits_none],

	["ring_3", "Gold Ring", [("ring_3", imodbits_none)], itp_type_goods, 0, 4000, abundance(25)|weight(40.0), imodbits_none],

	["ring_4", "Silver Ring", [("ring_4", imodbits_none)], itp_type_goods, 0, 1000, abundance(25)|weight(40.0), imodbits_none],

	["ring_5", "Silver Ring", [("ring_5", imodbits_none)], itp_type_goods, 0, 2000, abundance(25)|weight(40.0), imodbits_none],

	["asshai_saffron", "Saffron", [("trade_spice", imodbits_none)], itp_type_goods, 0, 4000, abundance(25)|weight(40.0), imodbits_none],

	["asshai_myrrh", "Myrrh", [("trade_spice", imodbits_none)], itp_type_goods, 0, 4000, abundance(25)|weight(40.0), imodbits_none],

	["asshai_cinnamon", "Cinnamon", [("trade_spice", imodbits_none)], itp_type_goods, 0, 4000, abundance(25)|weight(40.0), imodbits_none],

	["qarth_saffron", "Saffron", [("trade_spice", imodbits_none)], itp_type_goods, 0, 2500, abundance(25)|weight(40.0), imodbits_none],

	["qarth_pepper", "Pepper", [("trade_spice", imodbits_none)], itp_type_goods, 0, 2500, abundance(25)|weight(40.0), imodbits_none],

	["qarth_cardamom", "Cardamom", [("trade_spice", imodbits_none)], itp_type_goods, 0, 2500, abundance(25)|weight(40.0), imodbits_none],

	["zamettar_nutmeg", "Nutmeg", [("trade_spice", imodbits_none)], itp_type_goods, 0, 4000, abundance(25)|weight(40.0), imodbits_none],

	["zamettar_curry", "Curry", [("trade_spice", imodbits_none)], itp_type_goods, 0, 4000, abundance(25)|weight(40.0), imodbits_none],

	["zamettar_anise", "Anise", [("trade_spice", imodbits_none)], itp_type_goods, 0, 4000, abundance(25)|weight(40.0), imodbits_none],

	["moraq_cloves", "Cloves", [("trade_spice", imodbits_none)], itp_type_goods, 0, 1500, abundance(25)|weight(40.0), imodbits_none],

	["moraq_spiceflower", "Spiceflower", [("trade_spice", imodbits_none)], itp_type_goods, 0, 1500, abundance(25)|weight(40.0), imodbits_none],

	["moraq_persimmon_seeds", "Persimmon Seeds", [("trade_spice", imodbits_none)], itp_type_goods, 0, 1500, abundance(25)|weight(40.0), imodbits_none],

	["mysterious_spices1", "Mysterious Spices", [("trade_spice", imodbits_none)], itp_type_goods, 0, 50, abundance(25)|weight(40.0), imodbits_none],

	["mysterious_spices2", "Mysterious Spices", [("trade_spice", imodbits_none)], itp_type_goods, 0, 50, abundance(25)|weight(40.0), imodbits_none],

	["mysterious_spices3", "Mysterious Spices", [("trade_spice", imodbits_none)], itp_type_goods, 0, 50, abundance(25)|weight(40.0), imodbits_none],

	["mysterious_sword1", "Mysterious Sword", [("final_rusty_sword", imodbits_none)], itp_type_goods, 0, 50, abundance(25)|weight(40.0), imodbits_none],

	["mysterious_sword2", "Mysterious Sword", [("final_rusty_sword", imodbits_none)], itp_type_goods, 0, 50, abundance(25)|weight(40.0), imodbits_none],

	["mysterious_sword3", "Mysterious Sword", [("final_rusty_sword", imodbits_none)], itp_type_goods, 0, 50, abundance(25)|weight(40.0), imodbits_none],

	["credits_book", "Book of Patrons", [("bk_book_01", imodbits_none)], itp_type_goods, 0, 50, abundance(244)|weight(1.0), imodbits_none],

	["clifford_ring", "Ruby Ring", [("ring_2", imodbits_none)], itp_type_goods, 0, 1000, abundance(1)|weight(1.0), imodbits_none],

	["clifford_letter", "Ser Cliffords Letter", [("necturus_scroll_1", imodbits_none)], itp_type_goods, 0, 5, abundance(25)|weight(1.0), imodbits_none],

	["samol_book", "Old Grimoire", [("necturus_book_1", imodbits_none)], itp_type_goods, 0, 1000, abundance(2)|weight(2.0), imodbits_none],

	["samol_horn", "Old Horn", [("necturus_drinking_horn", imodbits_none)], itp_type_goods, 0, 500, abundance(2)|weight(2.0), imodbits_none],

	["varys_npc_5_letter", "Illyrios Letter", [("necturus_scroll_1", imodbits_none)], itp_type_goods, 0, 5, abundance(25)|weight(1.0), imodbits_none],

	["varys_npc_8_letter", "Allards Letter", [("necturus_scroll_1", imodbits_none)], itp_type_goods, 0, 5, abundance(25)|weight(1.0), imodbits_none],

	["harodon_letter", "Garibalds Letter", [("necturus_scroll_1", imodbits_none)], itp_type_goods, 0, 5, abundance(25)|weight(1.0), imodbits_none],

	["illyrios_letter", "Illyrios Letter", [("necturus_scroll_1", imodbits_none)], itp_type_goods, 0, 5, abundance(25)|weight(1.0), imodbits_none],

	["varys_npc_1_letter", "Illyrios Letter", [("necturus_scroll_1", imodbits_none)], itp_type_goods, 0, 5, abundance(25)|weight(1.0), imodbits_none],

	["varys_npc_2_letter", "Rugens Letter", [("necturus_scroll_1", imodbits_none)], itp_type_goods, 0, 5, abundance(25)|weight(1.0), imodbits_none],

	["varys_npc_3_chest", "Illyrios Chest", [("necturus_casket", imodbits_none)], itp_type_goods, 0, 5000, abundance(25)|weight(40.0), imodbits_none],

	["barrel_of_pitch", "Barrel of Pitch", [("necturus_big_barrel", imodbits_none)], itp_type_goods, 0, 50, abundance(25)|weight(16.0), imodbits_none],

	["huge_ruby", "Large Ruby", [("huge_ruby", imodbits_none)], itp_type_goods, 0, 5000, abundance(25)|weight(40.0), imodbits_none],

	["carved_tusk", "Carved Tusk", [("carved_tusk", imodbits_none)], itp_type_goods, 0, 1000, abundance(25)|weight(40.0), imodbits_none],

	["gold_goblet", "Gold Goblet", [("gold_goblet", imodbits_none)], itp_type_goods, 0, 7000, abundance(25)|weight(40.0), imodbits_none],

	["gold_nugget", "Gold Nugget", [("gold_nugget", imodbits_none)], itp_type_goods, 0, 8000, abundance(25)|weight(40.0), imodbits_none],

	["event_rabbit", "Rabbit", [("food_rabbit", imodbits_none)], itp_type_goods|itp_food|itp_consumable, 0, 85, max_ammo(50)|abundance(60)|weight(15.0)|food_quality(70), imodbit_old|imodbit_cheap|imodbit_fine|imodbit_well_made],

	["siege_supply", "Supplies", [("trade_ale", imodbits_none)], itp_type_goods, 0, 96, abundance(70)|weight(40.0), imodbits_none],

	["quest_wine", "Local Wine", [("trade_wine", imodbits_none)], itp_type_goods, 0, 46, max_ammo(50)|abundance(60)|weight(40.0), imodbits_none],

	["quest_ale", "Local Ale", [("trade_ale", imodbits_none)], itp_type_goods, 0, 31, max_ammo(50)|abundance(70)|weight(40.0), imodbits_none],

	["trial_destrier", "Destrier", [("destrier_1", imodbits_none)], itp_type_horse, 0, 4000, hit_points(140)|horse_maneuver(35)|abundance(50)|horse_charge(40)|horse_speed(40)|body_armor(15)|horse_scale(113), imodbit_timid|imodbit_champion|imodbits_horse_basic, [], [fac_kingdom_1, fac_kingdom_2, fac_kingdom_3, fac_kingdom_8, fac_kingdom_9, fac_kingdom_10]],

	["stormlands_destrier", "Destrier", [("destrier_1", imodbits_none)], itp_type_horse, 0, 4000, hit_points(140)|horse_maneuver(40)|abundance(50)|difficulty(3)|horse_charge(50)|horse_speed(40)|body_armor(15)|horse_scale(116), imodbit_timid|imodbit_champion|imodbits_horse_basic, [], [fac_kingdom_1, fac_kingdom_2, fac_kingdom_3, fac_kingdom_8, fac_kingdom_9, fac_kingdom_10]],

	["destrier_1", "Destrier", [("destrier_1", imodbits_none)], itp_type_horse|itp_merchandise, 0, 4000, hit_points(140)|horse_maneuver(35)|abundance(50)|difficulty(3)|horse_charge(40)|horse_speed(40)|body_armor(15)|horse_scale(113), imodbit_timid|imodbit_champion|imodbits_horse_basic, [], [fac_kingdom_1, fac_kingdom_2, fac_kingdom_3, fac_kingdom_8, fac_kingdom_9, fac_kingdom_10]],

	["destrier_2", "Destrier", [("destrier_2", imodbits_none)], itp_type_horse|itp_merchandise, 0, 4000, hit_points(140)|horse_maneuver(35)|abundance(50)|difficulty(3)|horse_charge(40)|horse_speed(40)|body_armor(15)|horse_scale(113), imodbit_timid|imodbit_champion|imodbits_horse_basic, [], [fac_kingdom_1, fac_kingdom_2, fac_kingdom_3, fac_kingdom_8, fac_kingdom_9, fac_kingdom_10]],

	["destrier_3", "Destrier", [("destrier_3", imodbits_none)], itp_type_horse|itp_merchandise, 0, 4000, hit_points(140)|horse_maneuver(35)|abundance(50)|difficulty(3)|horse_charge(40)|horse_speed(40)|body_armor(15)|horse_scale(113), imodbit_timid|imodbit_champion|imodbits_horse_basic, [], [fac_kingdom_1, fac_kingdom_2, fac_kingdom_3, fac_kingdom_8, fac_kingdom_9, fac_kingdom_10]],

	["destrier_4", "Destrier", [("destrier_4", imodbits_none)], itp_type_horse|itp_merchandise, 0, 4000, hit_points(140)|horse_maneuver(35)|abundance(50)|difficulty(3)|horse_charge(40)|horse_speed(40)|body_armor(15)|horse_scale(113), imodbit_timid|imodbit_champion|imodbits_horse_basic, [], [fac_kingdom_1, fac_kingdom_2, fac_kingdom_3, fac_kingdom_8, fac_kingdom_9, fac_kingdom_10]],

	["ho_swa_saddle_black", "Rounsey", [("rounsey_1", imodbits_none)], itp_type_horse|itp_merchandise, 0, 1000, hit_points(120)|horse_maneuver(30)|abundance(60)|horse_charge(10)|horse_speed(36)|horse_scale(108), imodbit_timid|imodbit_meek|imodbit_champion|imodbits_horse_basic],

	["rounsey_2", "Rounsey", [("rounsey_2", imodbits_none)], itp_type_horse|itp_merchandise, 0, 1000, hit_points(120)|horse_maneuver(30)|abundance(60)|horse_charge(10)|horse_speed(36)|horse_scale(108), imodbit_timid|imodbit_meek|imodbit_champion|imodbits_horse_basic],

	["palfrey_1", "Palfrey", [("palfrey_1", imodbits_none)], itp_type_horse|itp_merchandise, 0, 3000, hit_points(140)|horse_maneuver(40)|abundance(60)|difficulty(3)|horse_charge(5)|horse_speed(40)|horse_scale(108), imodbit_timid|imodbit_meek|imodbit_champion|imodbits_horse_basic, [], [fac_kingdom_1, fac_kingdom_3, fac_kingdom_6, fac_kingdom_9, fac_kingdom_10]],

	["palfrey_2", "Palfrey", [("palfrey_2", imodbits_none)], itp_type_horse|itp_merchandise, 0, 3000, hit_points(140)|horse_maneuver(40)|abundance(60)|difficulty(3)|horse_charge(5)|horse_speed(40)|horse_scale(108), imodbit_timid|imodbit_meek|imodbit_champion|imodbits_horse_basic, [], [fac_kingdom_1, fac_kingdom_3, fac_kingdom_6, fac_kingdom_9, fac_kingdom_10]],

	["courser_1", "Courser", [("courser_1", imodbits_none)], itp_type_horse|itp_merchandise, 0, 2000, hit_points(140)|horse_maneuver(40)|abundance(60)|difficulty(2)|horse_charge(20)|horse_speed(40)|body_armor(10)|horse_scale(108), imodbit_timid|imodbit_meek|imodbit_champion|imodbits_horse_basic],

	["courser_2", "Courser", [("courser_2", imodbits_none)], itp_type_horse|itp_merchandise, 0, 2000, hit_points(140)|horse_maneuver(40)|abundance(60)|difficulty(2)|horse_charge(20)|horse_speed(40)|body_armor(10)|horse_scale(108), imodbit_timid|imodbit_meek|imodbit_champion|imodbits_horse_basic],

	["courser_3", "Courser", [("courser_3", imodbits_none)], itp_type_horse|itp_merchandise, 0, 2000, hit_points(140)|horse_maneuver(40)|abundance(60)|difficulty(2)|horse_charge(20)|horse_speed(40)|body_armor(10)|horse_scale(108), imodbit_timid|imodbit_meek|imodbit_champion|imodbits_horse_basic],

	["garron_1", "Garron", [("garron_1", imodbits_none)], itp_type_horse|itp_merchandise, 0, 500, hit_points(140)|horse_maneuver(50)|abundance(60)|difficulty(1)|horse_charge(5)|horse_speed(30)|body_armor(10)|horse_scale(108), imodbit_timid|imodbit_meek|imodbit_champion|imodbits_horse_basic, [], [fac_kingdom_2]],

	["garron_2", "Garron", [("garron_2", imodbits_none)], itp_type_horse|itp_merchandise, 0, 500, hit_points(140)|horse_maneuver(50)|abundance(60)|difficulty(1)|horse_charge(5)|horse_speed(30)|body_armor(10)|horse_scale(108), imodbit_timid|imodbit_meek|imodbit_champion|imodbits_horse_basic, [], [fac_kingdom_2]],

	["horse_light_a", "Dothraki Courser", [("horse_light_a", imodbits_none)], itp_type_horse|itp_merchandise, 0, 2000, hit_points(140)|horse_maneuver(25)|abundance(60)|difficulty(3)|horse_charge(25)|horse_speed(45)|horse_scale(112), imodbit_timid|imodbit_meek|imodbit_champion|imodbits_horse_basic, [], [fac_kingdom_5, fac_kingdom_12, fac_kingdom_13, fac_kingdom_14, fac_kingdom_15, fac_kingdom_16, fac_kingdom_17, fac_kingdom_18]],

	["horse_light_b", "Dothraki Courser", [("horse_light_b", imodbits_none)], itp_type_horse|itp_merchandise, 0, 2000, hit_points(140)|horse_maneuver(25)|abundance(60)|difficulty(3)|horse_charge(25)|horse_speed(45)|horse_scale(112), imodbit_timid|imodbit_meek|imodbit_champion|imodbits_horse_basic, [], [fac_kingdom_5, fac_kingdom_12, fac_kingdom_13, fac_kingdom_14, fac_kingdom_15, fac_kingdom_16, fac_kingdom_17, fac_kingdom_18]],

	["horse_light_c", "Dothraki Courser", [("horse_light_c", imodbits_none)], itp_type_horse|itp_merchandise, 0, 2000, hit_points(140)|horse_maneuver(25)|abundance(60)|difficulty(3)|horse_charge(25)|horse_speed(45)|horse_scale(112), imodbit_timid|imodbit_meek|imodbit_champion|imodbits_horse_basic, [], [fac_kingdom_5, fac_kingdom_12, fac_kingdom_13, fac_kingdom_14, fac_kingdom_15, fac_kingdom_16, fac_kingdom_17, fac_kingdom_18]],

	["andal_destrier", "Andal Destrier", [("andal_destrier", imodbits_none)], itp_type_horse|itp_merchandise, 0, 3000, hit_points(140)|horse_maneuver(35)|abundance(60)|difficulty(3)|horse_charge(40)|horse_speed(40)|body_armor(10)|horse_scale(108), imodbit_timid|imodbit_meek|imodbit_champion|imodbits_horse_basic, [], [fac_kingdom_12, fac_kingdom_17, fac_kingdom_18]],

	["plate_warhorse_1", "Plated Warhorse", [("plate_warhorse_1", imodbits_none)], itp_type_horse|itp_merchandise, 0, 15000, hit_points(150)|horse_maneuver(36)|abundance(2)|difficulty(3)|horse_charge(50)|horse_speed(40)|body_armor(35)|horse_scale(113), imodbit_timid|imodbit_champion|imodbits_horse_basic, [], [fac_kingdom_9, fac_kingdom_10]],

	["plate_warhorse_2", "Plated Warhorse", [("plate_warhorse_2", imodbits_none)], itp_type_horse|itp_merchandise, 0, 15000, hit_points(150)|horse_maneuver(36)|abundance(2)|difficulty(3)|horse_charge(50)|horse_speed(40)|body_armor(35)|horse_scale(113), imodbit_timid|imodbit_champion|imodbits_horse_basic, [], [fac_kingdom_9, fac_kingdom_10]],

	["plate_warhorse_3", "Plated Warhorse", [("plate_warhorse_3", imodbits_none)], itp_type_horse|itp_merchandise, 0, 15000, hit_points(150)|horse_maneuver(36)|abundance(2)|difficulty(3)|horse_charge(50)|horse_speed(40)|body_armor(35)|horse_scale(113), imodbit_timid|imodbit_champion|imodbits_horse_basic, [], [fac_kingdom_9]],

	["andal_cataphract", "Cataphract Warhorse", [("andal_cataphract", imodbits_none)], itp_type_horse|itp_merchandise, 0, 15000, hit_points(150)|horse_maneuver(36)|abundance(2)|difficulty(3)|horse_charge(50)|horse_speed(40)|body_armor(35)|horse_scale(113), imodbit_timid|imodbit_champion|imodbits_horse_basic, [], [fac_kingdom_12, fac_kingdom_13, fac_kingdom_14, fac_kingdom_15, fac_kingdom_16]],

	["chain_mail_horse", "Mailed Destrier", [("chain_mail_horse", imodbits_none)], itp_type_horse|itp_merchandise, 0, 8000, hit_points(150)|horse_maneuver(36)|abundance(10)|difficulty(3)|horse_charge(40)|horse_speed(40)|body_armor(30)|horse_scale(113), imodbit_timid|imodbit_champion|imodbits_horse_basic, [], [fac_kingdom_1, fac_kingdom_2, fac_kingdom_3, fac_kingdom_8, fac_kingdom_9, fac_kingdom_10]],

	["rhoynar_cataphract", "Dothraki Cataphract Warhorse", [("rhoynar_cataphract", imodbits_none)], itp_type_horse, 0, 15000, hit_points(150)|horse_maneuver(36)|abundance(2)|difficulty(3)|horse_charge(50)|horse_speed(42)|body_armor(35)|horse_scale(113), imodbit_timid|imodbit_champion|imodbits_horse_basic, [], [fac_kingdom_12, fac_kingdom_13, fac_kingdom_14, fac_kingdom_15, fac_kingdom_16]],

	["dornish_sand_steed_1", "Dornish Sand Steed", [("dornish_sand_steed_1", imodbits_none)], itp_type_horse|itp_merchandise, 0, 2000, hit_points(140)|horse_maneuver(40)|abundance(60)|difficulty(2)|horse_charge(10)|horse_speed(45)|horse_scale(108), imodbit_timid|imodbit_meek|imodbit_champion|imodbits_horse_basic, [], [fac_kingdom_6]],

	["dornish_sand_steed_2", "Dornish Sand Steed", [("dornish_sand_steed_2", imodbits_none)], itp_type_horse|itp_merchandise, 0, 2000, hit_points(140)|horse_maneuver(40)|abundance(60)|difficulty(2)|horse_charge(10)|horse_speed(45)|horse_scale(108), imodbit_timid|imodbit_meek|imodbit_champion|imodbits_horse_basic, [], [fac_kingdom_6]],

	["donkey", "Donkey", [("donkey", imodbits_none)], itp_type_horse|itp_merchandise, 0, 200, hit_points(60)|horse_maneuver(25)|abundance(70)|horse_charge(10)|horse_speed(25)|horse_scale(98), imodbit_timid|imodbits_horse_basic],

	["ho_nor_mule", "Mule", [("mule", imodbits_none)], itp_type_horse|itp_merchandise, 0, 200, hit_points(60)|horse_maneuver(25)|abundance(70)|horse_charge(10)|horse_speed(25)|horse_scale(98), imodbit_timid|imodbits_horse_basic],

	["ho_sar_camel_bactrian", "Camel", [("camel", imodbits_none)], itp_type_horse|itp_merchandise, 0, 500, hit_points(130)|horse_maneuver(30)|abundance(40)|difficulty(3)|horse_charge(20)|horse_speed(36)|horse_scale(108), imodbits_none, [], [fac_kingdom_16]],

	["we_swa_axe_hatchet", "Hatchet", [("we_swa_axe_hatchet", imodbits_none)], itp_type_one_handed_wpn|itp_merchandise|itp_wooden_parry|itp_primary|itp_secondary, itcf_carry_axe_left_hip|itc_scimitar, 100, thrust_damage(0, pierce)|hit_points(23552)|spd_rtng(65)|abundance(60)|weight(2.0)|swing_damage(23, cut)|difficulty(8)|weapon_length(60), imodbits_axe|imodbits_mace, [], [fac_kingdom_11, fac_kingdom_19]],

	["we_swa_axe_voulge", "Pole Cleaver", [("we_swa_axe_voulge", imodbits_none)], itp_type_two_handed_wpn|itp_merchandise|itp_wooden_parry|itp_two_handed|itp_primary|itp_covers_legs|itp_doesnt_cover_hair|itp_can_penetrate_shield|itp_bonus_against_shield|itp_cant_use_on_horseback, itcf_carry_axe_back|itc_nodachi, 1000, thrust_damage(0, pierce)|hit_points(40960)|spd_rtng(80)|abundance(10)|weight(6.0)|swing_damage(40, cut)|difficulty(13)|weapon_length(119), imodbits_axe|imodbits_mace, [], [fac_kingdom_2]],

	["we_vae_axe_bardiche", "Long Poleaxe", [("we_vae_axe_bardiche", imodbits_none)], itp_type_two_handed_wpn|itp_merchandise|itp_wooden_parry|itp_two_handed|itp_primary|itp_covers_legs|itp_doesnt_cover_hair|itp_can_penetrate_shield|itp_bonus_against_shield|itp_cant_use_on_horseback|itp_unbalanced, itcf_carry_axe_back|itc_nodachi, 1000, thrust_damage(0, pierce)|hit_points(40960)|spd_rtng(80)|abundance(10)|weight(6.0)|swing_damage(40, cut)|difficulty(13)|weapon_length(102), imodbits_axe|imodbits_mace, [], [fac_kingdom_2]],

	["we_vae_blunt_club", "Club", [("tutorial_club", imodbits_none)], itp_type_one_handed_wpn|itp_merchandise|itp_wooden_attack|itp_wooden_parry|itp_primary|itp_bonus_against_shield, itc_scimitar, 25, thrust_damage(0, pierce)|hit_points(15360)|spd_rtng(98)|abundance(60)|weight(2.0)|swing_damage(15, blunt)|weapon_length(70), imodbits_none],

	["we_swa_blunt_club_long", "Long Spiked Club", [("we_swa_blunt_club_long", imodbits_none)], itp_type_two_handed_wpn|itp_merchandise|itp_wooden_parry|itp_two_handed|itp_primary|itp_bonus_against_shield|itp_cant_use_on_horseback|itp_crush_through|itp_can_knock_down, itcf_carry_axe_back|itc_nodachi, 400, thrust_damage(0, blunt)|hit_points(30720)|spd_rtng(70)|abundance(80)|weight(7.0)|swing_damage(30, pierce)|difficulty(12)|weapon_length(126), imodbits_axe|imodbits_mace, [], [fac_kingdom_1, fac_kingdom_8, fac_kingdom_9, fac_kingdom_10, fac_kingdom_20]],

	["we_vae_blunt_maul", "Maul", [("we_vae_blunt_maul", imodbits_none)], itp_type_two_handed_wpn|itp_merchandise|itp_wooden_attack|itp_wooden_parry|itp_two_handed|itp_primary|itp_cant_use_on_horseback|itp_crush_through|itp_unbalanced|itp_can_knock_down, itcf_carry_spear|itc_nodachi, 200, thrust_damage(0, pierce)|hit_points(28672)|spd_rtng(60)|abundance(100)|weight(8.0)|swing_damage(28, blunt)|difficulty(13)|weapon_length(79), imodbits_axe|imodbits_mace, [], [fac_kingdom_2]],

	["we_vae_blunt_sledgehammer", "Sledgehammer", [("we_vae_blunt_sledgehammer", imodbits_none)], itp_type_two_handed_wpn|itp_wooden_attack|itp_wooden_parry|itp_two_handed|itp_primary|itp_cant_use_on_horseback|itp_crush_through|itp_unbalanced|itp_can_knock_down, itcf_carry_spear|itc_nodachi, 200, thrust_damage(0, pierce)|hit_points(30720)|spd_rtng(60)|abundance(100)|weight(8.0)|swing_damage(30, blunt)|difficulty(13)|weapon_length(82), imodbits_axe|imodbits_mace, [], [fac_kingdom_2]],

	["we_swa_spear_glaive_small", "Small Glaive", [("we_swa_spear_glaive_small", imodbits_none)], itp_type_polearm|itp_merchandise|itp_wooden_parry|itp_two_handed|itp_primary|itp_bonus_against_shield|itp_cant_use_on_horseback, itcf_carry_spear|itc_staff, 1000, thrust_damage(32, pierce)|hit_points(40960)|spd_rtng(90)|abundance(10)|weight(6.0)|swing_damage(40, cut)|weapon_length(163), imodbits_polearm, [], [fac_kingdom_1, fac_kingdom_8, fac_kingdom_9, fac_kingdom_10, fac_kingdom_20]],

	["we_swa_spear_glaive", "Glaive", [("we_swa_spear_glaive", imodbits_none)], itp_type_polearm|itp_merchandise|itp_wooden_parry|itp_two_handed|itp_primary|itp_bonus_against_shield|itp_cant_use_on_horseback, itcf_carry_spear|itc_staff, 1100, thrust_damage(34, pierce)|hit_points(43008)|spd_rtng(80)|abundance(10)|weight(6.0)|swing_damage(42, cut)|weapon_length(170), imodbits_polearm, [], [fac_kingdom_1, fac_kingdom_8, fac_kingdom_9, fac_kingdom_10, fac_kingdom_20]],

	["we_swa_spear_bill_english", "Bill", [("fi_bill", imodbits_none)], itp_type_polearm|itp_merchandise|itp_wooden_parry|itp_two_handed|itp_primary|itp_bonus_against_shield|itp_cant_use_on_horseback|itp_crush_through|itp_can_knock_down, itcf_carry_spear|itc_staff, 1200, thrust_damage(32, pierce)|hit_points(45056)|spd_rtng(80)|abundance(10)|weight(6.0)|swing_damage(44, cut)|difficulty(12)|weapon_length(187), imodbits_polearm, [], [fac_kingdom_1, fac_kingdom_8, fac_kingdom_9, fac_kingdom_10, fac_kingdom_20]],

	["we_vae_spear_scythe", "Scythe", [("we_vae_spear_scythe", imodbits_none)], itp_type_polearm|itp_merchandise|itp_wooden_parry|itp_primary|itp_penalty_with_shield|itp_cant_use_on_horseback|itp_fit_to_head|itp_offset_lance, itcf_carry_spear|itc_staff, 43, thrust_damage(14, pierce)|hit_points(19456)|spd_rtng(100)|abundance(60)|weight(4.0)|swing_damage(19, cut)|weapon_length(182), imodbits_polearm, [], [fac_kingdom_1, fac_kingdom_8, fac_kingdom_9, fac_kingdom_10, fac_kingdom_20]],

	["we_vae_spear_scythe_shortened", "Shortened Military Scythe", [("we_vae_spear_scythe_shortened", imodbits_none)], itp_type_two_handed_wpn|itp_merchandise|itp_two_handed|itp_primary|itp_bonus_against_shield|itp_cant_use_on_horseback, itcf_carry_sword_back|itc_nodachi, 1000, thrust_damage(0, pierce)|hit_points(40960)|spd_rtng(85)|abundance(10)|weight(6.0)|swing_damage(40, cut)|difficulty(12)|weapon_length(112), imodbits_sword_high, [], [fac_kingdom_1, fac_kingdom_8, fac_kingdom_9, fac_kingdom_10, fac_kingdom_20]],

	["we_vae_spear_polehammer", "Light Spear", [("spear_a_2m", imodbits_none)], itp_type_polearm|itp_merchandise|itp_wooden_parry|itp_two_handed|itp_primary|itp_covers_legs|itp_doesnt_cover_hair|itp_can_penetrate_shield|itp_bonus_against_shield|itp_can_knock_down, itcf_carry_spear|itc_staff, 200, thrust_damage(33, pierce)|hit_points(25600)|spd_rtng(110)|abundance(60)|weight(4.0)|swing_damage(25, cut)|weapon_length(200), imodbits_none],

	["we_khe_spear_staff", "Light Spear", [("spear_1_45m", imodbits_none)], itp_type_polearm|itp_merchandise|itp_wooden_attack|itp_wooden_parry|itp_primary|itp_covers_legs|itp_doesnt_cover_hair|itp_can_penetrate_shield|itp_bonus_against_shield|itp_can_knock_down, itcf_carry_spear|itc_staff, 200, thrust_damage(33, pierce)|hit_points(25600)|spd_rtng(110)|abundance(80)|weight(4.0)|swing_damage(25, cut)|weapon_length(145), imodbits_none],

	["we_khe_spear_bamboolong", "Light Spear", [("spear_1_44m", imodbits_none)], itp_type_polearm|itp_merchandise|itp_wooden_parry|itp_primary|itp_covers_legs|itp_doesnt_cover_hair|itp_can_penetrate_shield|itp_bonus_against_shield|itp_can_knock_down, itcf_carry_spear|itc_staff, 200, thrust_damage(33, pierce)|hit_points(25600)|spd_rtng(110)|abundance(60)|weight(4.0)|swing_damage(25, cut)|weapon_length(144), imodbits_none],

	["we_khe_spear_nagita", "Light Spear", [("spear_1_22m", imodbits_none)], itp_type_polearm|itp_merchandise|itp_wooden_parry|itp_two_handed|itp_primary|itp_covers_legs|itp_doesnt_cover_hair|itp_can_penetrate_shield|itp_bonus_against_shield|itp_can_knock_down, itcf_carry_spear|itc_staff, 200, thrust_damage(33, pierce)|hit_points(25600)|spd_rtng(110)|abundance(80)|weight(4.0)|swing_damage(25, cut)|weapon_length(122), imodbits_none, [], [fac_kingdom_1, fac_kingdom_8, fac_kingdom_9, fac_kingdom_10, fac_kingdom_20]],

	["we_khe_spear_haftedblade", "Light Spear", [("spear_2m", imodbits_none)], itp_type_polearm|itp_merchandise|itp_wooden_parry|itp_primary|itp_covers_legs|itp_doesnt_cover_hair|itp_can_penetrate_shield|itp_bonus_against_shield|itp_can_knock_down, itcf_carry_spear|itc_staff, 200, thrust_damage(33, pierce)|hit_points(25600)|spd_rtng(110)|abundance(60)|weight(4.0)|swing_damage(25, cut)|weapon_length(200), imodbits_none, [], [fac_kingdom_1, fac_kingdom_8, fac_kingdom_9, fac_kingdom_10, fac_kingdom_20]],

	["heavy_spear_1", "Heavy Spear", [("heavy_spear_1", imodbits_none)], itp_type_polearm|itp_merchandise|itp_wooden_parry|itp_two_handed|itp_primary|itp_covers_legs|itp_doesnt_cover_hair|itp_can_penetrate_shield|itp_bonus_against_shield|itp_can_knock_down, itcf_carry_spear|itc_staff, 500, thrust_damage(30, pierce)|hit_points(25600)|spd_rtng(96)|abundance(60)|weight(4.0)|swing_damage(25, cut)|difficulty(12)|weapon_length(125), imodbits_polearm],

	["heavy_spear_2", "Heavy Spear", [("heavy_spear_2", imodbits_none)], itp_type_polearm|itp_merchandise|itp_wooden_parry|itp_two_handed|itp_primary|itp_covers_legs|itp_doesnt_cover_hair|itp_can_penetrate_shield|itp_bonus_against_shield|itp_can_knock_down, itcf_carry_spear|itc_staff, 500, thrust_damage(30, pierce)|hit_points(25600)|spd_rtng(100)|abundance(60)|weight(4.0)|swing_damage(25, cut)|difficulty(12)|weapon_length(123), imodbits_polearm],

	["heavy_spear_3", "Heavy Spear", [("heavy_spear_3", imodbits_none)], itp_type_polearm|itp_merchandise|itp_wooden_parry|itp_two_handed|itp_primary|itp_covers_legs|itp_doesnt_cover_hair|itp_can_penetrate_shield|itp_bonus_against_shield|itp_can_knock_down, itcf_carry_spear|itc_staff, 500, thrust_damage(30, pierce)|hit_points(27648)|spd_rtng(102)|abundance(60)|weight(4.0)|swing_damage(27, cut)|difficulty(12)|weapon_length(88), imodbits_polearm],

	["dornish_spear_feathers", "Heavy Spear", [("dornish_spear_feathers", imodbits_none)], itp_type_polearm|itp_merchandise|itp_wooden_parry|itp_two_handed|itp_primary|itp_covers_legs|itp_doesnt_cover_hair|itp_can_penetrate_shield|itp_bonus_against_shield|itp_can_knock_down, itcf_carry_spear|itc_staff, 900, thrust_damage(30, pierce)|hit_points(27648)|spd_rtng(110)|abundance(60)|weight(4.0)|swing_damage(27, cut)|difficulty(12)|weapon_length(152), imodbits_polearm, [], [fac_kingdom_6]],

	["dornish_heavy_spear", "Heavy Spear", [("dornish_heavy_spear", imodbits_none)], itp_type_polearm|itp_merchandise|itp_wooden_parry|itp_two_handed|itp_primary|itp_covers_legs|itp_doesnt_cover_hair|itp_can_penetrate_shield|itp_bonus_against_shield|itp_can_knock_down, itcf_carry_spear|itc_staff, 1300, thrust_damage(25, pierce)|hit_points(30720)|spd_rtng(112)|abundance(60)|weight(4.0)|swing_damage(30, cut)|difficulty(12)|weapon_length(178), imodbits_polearm, [], [fac_kingdom_6]],

	["we_rho_spear_fork_pitch", "Pitch Fork", [("we_rho_spear_fork_pitch", imodbits_none)], itp_type_polearm|itp_merchandise|itp_wooden_parry|itp_primary|itp_penalty_with_shield|itp_fit_to_head|itp_offset_lance, itc_staff, 25, thrust_damage(14, pierce)|spd_rtng(100)|abundance(60)|weight(2.0)|swing_damage(0, blunt)|weapon_length(154), imodbits_polearm, [], [fac_kingdom_1, fac_kingdom_8, fac_kingdom_9, fac_kingdom_10, fac_kingdom_20]],

	["we_rho_spear_fork_military", "Military Fork", [("we_rho_spear_fork_military", imodbits_none)], itp_type_polearm|itp_merchandise|itp_wooden_parry|itp_primary|itp_fit_to_head|itp_offset_lance, itc_staff, 100, thrust_damage(20, pierce)|spd_rtng(100)|abundance(80)|weight(3.0)|swing_damage(0, blunt)|weapon_length(135), imodbits_polearm, [], [fac_kingdom_1, fac_kingdom_8, fac_kingdom_9, fac_kingdom_10, fac_kingdom_20]],

	["we_rho_spear_fork_battle", "Battle Fork", [("we_rho_spear_fork_battle", imodbits_none)], itp_type_polearm|itp_merchandise|itp_wooden_parry|itp_primary|itp_fit_to_head|itp_offset_lance, itc_staff, 122, thrust_damage(22, pierce)|spd_rtng(100)|abundance(70)|weight(4.0)|swing_damage(0, blunt)|weapon_length(142), imodbits_polearm, [], [fac_kingdom_1, fac_kingdom_8, fac_kingdom_9, fac_kingdom_10, fac_kingdom_20]],

	["we_sar_spear_staff", "Staff", [("we_sar_spear_staff", imodbits_none)], itp_type_polearm|itp_merchandise|itp_wooden_attack|itp_wooden_parry|itp_primary|itp_penalty_with_shield|itp_cant_use_on_horseback|itp_fit_to_head|itp_offset_lance, itcf_carry_sword_back|itc_staff, 36, thrust_damage(19, blunt)|hit_points(18432)|spd_rtng(100)|abundance(60)|weight(1.0)|swing_damage(18, blunt)|weapon_length(130), imodbits_polearm],

	["we_sar_spear_staff_quarter", "Quarter Staff", [("we_sar_spear_staff_quarter", imodbits_none)], itp_type_polearm|itp_wooden_attack|itp_wooden_parry|itp_primary|itp_cant_use_on_horseback, itcf_carry_sword_back|itc_staff, 60, thrust_damage(20, blunt)|hit_points(20480)|spd_rtng(104)|abundance(60)|weight(2.0)|swing_damage(20, blunt)|weapon_length(140), imodbits_polearm],

	["we_sar_spear_staff_iron", "Iron Staff", [("we_sar_spear_staff_iron", imodbits_none)], itp_type_polearm|itp_primary|itp_cant_use_on_horseback, itcf_carry_sword_back|itc_staff, 202, thrust_damage(23, blunt)|hit_points(23552)|spd_rtng(97)|abundance(60)|weight(3.0)|swing_damage(23, blunt)|weapon_length(140), imodbits_polearm, [], [fac_kingdom_6]],

	["we_sar_spear_lance", "Hooked Glaive", [("guisarme_a", imodbits_none)], itp_type_polearm|itp_merchandise|itp_wooden_parry|itp_primary|itp_bonus_against_shield|itp_penalty_with_shield|itp_cant_use_on_horseback|itp_can_knock_down, itcf_carry_spear|itc_staff, 1200, thrust_damage(30, pierce)|hit_points(45056)|spd_rtng(80)|abundance(10)|weight(6.0)|swing_damage(44, cut)|weapon_length(170), imodbits_polearm, [], [fac_kingdom_1, fac_kingdom_8, fac_kingdom_9, fac_kingdom_10, fac_kingdom_20]],

	["we_vae_sword_sickle", "Sickle", [("we_vae_sword_sickle", imodbits_none)], itp_type_one_handed_wpn|itp_no_parry|itp_merchandise|itp_primary|itp_secondary, itc_cleaver, 9, thrust_damage(0, pierce)|hit_points(10240)|spd_rtng(99)|abundance(60)|weight(1.0)|swing_damage(10, cut)|weapon_length(40), imodbits_none, [], [fac_kingdom_1, fac_kingdom_8, fac_kingdom_9, fac_kingdom_10, fac_kingdom_20]],

	["we_vae_sword_cleaver_military", "Military Cleaver", [("we_vae_sword_cleaver_military", imodbits_none)], itp_type_two_handed_wpn|itp_merchandise|itp_two_handed|itp_primary|itp_bonus_against_shield|itp_cant_use_on_horseback, itcf_carry_sword_back|itc_nodachi, 1200, thrust_damage(0, pierce)|hit_points(40960)|spd_rtng(85)|abundance(10)|weight(6.0)|swing_damage(40, cut)|difficulty(13)|weapon_length(115), imodbits_sword_high, [], [fac_kingdom_2]],

	["we_swa_sword_clamshell_claymore", "Long Sword", [("Faradon_handandahalf", imodbits_none)], itp_type_two_handed_wpn|itp_merchandise|itp_two_handed|itp_primary|itp_penalty_with_shield, itcf_thrust_twohanded|itcf_carry_sword_back|itc_dagger|itc_nodachi, 1200, thrust_damage(43, pierce)|hit_points(40960)|spd_rtng(90)|abundance(10)|weight(6.0)|swing_damage(40, cut)|difficulty(12)|weapon_length(104), imodbits_sword_high, [], [fac_kingdom_1, fac_kingdom_8, fac_kingdom_9, fac_kingdom_10, fac_kingdom_20]],

	["we_swa_sword_twohanded_claymore", "Great Sword", [("Faradon_twohanded1", imodbits_none)], itp_type_two_handed_wpn|itp_merchandise|itp_two_handed|itp_primary|itp_cant_use_on_horseback, itcf_carry_sword_back|itc_greatsword, 1200, thrust_damage(43, pierce)|hit_points(40960)|spd_rtng(90)|abundance(10)|weight(6.0)|swing_damage(40, cut)|difficulty(12)|weapon_length(122), imodbits_sword_high, [], [fac_kingdom_1, fac_kingdom_8, fac_kingdom_9, fac_kingdom_10, fac_kingdom_20]],

	["gregors_great_sword", "Gregors Great Sword", [("Faradon_twohanded1", imodbits_none)], itp_type_one_handed_wpn|itp_unique|itp_primary|itp_covers_legs|itp_doesnt_cover_hair|itp_can_penetrate_shield|itp_bonus_against_shield|itp_crush_through|itp_can_knock_down|itp_extra_penetration, itcf_carry_sword_back|itc_longsword, 2200, thrust_damage(45, pierce)|hit_points(46080)|spd_rtng(110)|abundance(10)|weight(6.0)|swing_damage(45, cut)|difficulty(12)|weapon_length(122), imodbits_sword, [], [fac_kingdom_1, fac_kingdom_8, fac_kingdom_9, fac_kingdom_10, fac_kingdom_20]],

	["we_vae_sword_cleaverwar", "War Cleaver", [("we_vae_sword_cleaverwar", imodbits_none)], itp_type_two_handed_wpn|itp_merchandise|itp_two_handed|itp_primary|itp_bonus_against_shield|itp_cant_use_on_horseback|itp_crush_through, itcf_carry_sword_back|itc_nodachi, 1100, hit_points(43008)|spd_rtng(85)|abundance(10)|weight(6.0)|swing_damage(42, cut)|difficulty(13)|weapon_length(120), imodbits_sword_high, [], [fac_kingdom_2]],

	["we_khe_sword_sabre", "Great Sword", [("Faradon_twohanded2", imodbits_none)], itp_type_two_handed_wpn|itp_merchandise|itp_two_handed|itp_primary|itp_cant_use_on_horseback, itcf_carry_sword_back|itc_nodachi, 1200, thrust_damage(43, pierce)|hit_points(40960)|spd_rtng(90)|abundance(10)|weight(6.0)|swing_damage(40, cut)|difficulty(12)|weapon_length(122), imodbits_sword_high, [], [fac_kingdom_1, fac_kingdom_8, fac_kingdom_9, fac_kingdom_10, fac_kingdom_20]],

	["we_nor_sword_danish_great", "Great Sword", [("we_nor_sword_danish_great", imodbits_none)], itp_type_two_handed_wpn|itp_merchandise|itp_two_handed|itp_primary|itp_cant_use_on_horseback, itcf_carry_sword_back|itc_greatsword, 1200, thrust_damage(43, pierce)|hit_points(40960)|spd_rtng(90)|abundance(1)|weight(6.0)|swing_damage(40, cut)|difficulty(12)|weapon_length(114), imodbits_sword_high, [], [fac_kingdom_1, fac_kingdom_8, fac_kingdom_9, fac_kingdom_10, fac_kingdom_20]],

	["we_rho_sword_great", "Great Sword", [("flamberge", imodbits_none)], itp_type_polearm|itp_merchandise|itp_two_handed|itp_primary|itp_covers_legs|itp_doesnt_cover_hair|itp_can_penetrate_shield|itp_bonus_against_shield|itp_cant_use_on_horseback|itp_can_knock_down, itcf_carry_sword_back|itc_greatsword, 2000, thrust_damage(36, pierce)|hit_points(46080)|spd_rtng(85)|abundance(10)|weight(7.0)|swing_damage(45, cut)|difficulty(13)|weapon_length(143), imodbits_none, [], [fac_kingdom_2]],

	["we_pla_sword_great_four", "Halberd", [("fi_halberd_3", imodbits_none)], itp_type_polearm|itp_merchandise|itp_two_handed|itp_primary|itp_bonus_against_shield|itp_cant_use_on_horseback|itp_crush_through|itp_can_knock_down, itcf_carry_spear|itc_poleaxe, 1400, thrust_damage(34, pierce)|hit_points(43008)|spd_rtng(80)|abundance(10)|weight(7.0)|swing_damage(42, cut)|difficulty(12)|weapon_length(148), imodbits_sword_high, [], [fac_kingdom_1, fac_kingdom_8, fac_kingdom_9, fac_kingdom_10, fac_kingdom_20]],

	["fi_halberd_2", "Halberd", [("fi_halberd_2", imodbits_none)], itp_type_polearm|itp_merchandise|itp_two_handed|itp_primary|itp_bonus_against_shield|itp_cant_use_on_horseback|itp_crush_through|itp_can_knock_down, itcf_carry_spear|itc_poleaxe, 1400, thrust_damage(34, pierce)|hit_points(43008)|spd_rtng(80)|abundance(10)|weight(7.0)|swing_damage(42, cut)|difficulty(12)|weapon_length(148), imodbits_sword_high, [], [fac_kingdom_1, fac_kingdom_8, fac_kingdom_9, fac_kingdom_10, fac_kingdom_20]],

	["fi_halberd_1", "Halberd", [("fi_halberd_1", imodbits_none)], itp_type_polearm|itp_merchandise|itp_two_handed|itp_primary|itp_bonus_against_shield|itp_cant_use_on_horseback|itp_crush_through|itp_can_knock_down, itcf_carry_spear|itc_poleaxe, 1400, thrust_damage(34, pierce)|hit_points(43008)|spd_rtng(80)|abundance(10)|weight(7.0)|swing_damage(42, cut)|difficulty(12)|weapon_length(148), imodbits_sword_high, [], [fac_kingdom_1, fac_kingdom_8, fac_kingdom_9, fac_kingdom_10, fac_kingdom_20]],

	["normal_arrows", "Arrows", [("we_nor_arrow_bodkin", imodbits_none), ("flying_missile", ixmesh_flying_ammo), ("we_vae_quiver_sharp", ixmesh_carry)], itp_type_arrows|itp_merchandise, itcf_carry_quiver_back_right, 100, thrust_damage(2, pierce)|max_ammo(22)|abundance(60)|weight(3.0)|weapon_length(91), imodbits_missile],

	["arrow_f_big", "Heavy Arrows", [("arrow_f_big", imodbits_none), ("flying_missile", ixmesh_flying_ammo), ("arrow_f_big_quiver", ixmesh_carry)], itp_type_arrows|itp_merchandise, itcf_carry_quiver_back_right, 300, thrust_damage(5, pierce)|max_ammo(22)|abundance(60)|weight(3.0)|weapon_length(91), imodbits_missile],

	["arrow_f_piece", "Piercing Arrows", [("arrow_f_piece", imodbits_none), ("flying_missile", ixmesh_flying_ammo), ("arrow_f_piece_quiver", ixmesh_carry)], itp_type_arrows|itp_merchandise, itcf_carry_quiver_back_right, 500, thrust_damage(6, pierce)|max_ammo(22)|abundance(60)|weight(3.0)|weapon_length(91), imodbits_missile],

	["arrow_f_slash", "Heavy Arrows", [("arrow_f_slash", imodbits_none), ("flying_missile", ixmesh_flying_ammo), ("arrow_f_slash_quiver", ixmesh_carry)], itp_type_arrows|itp_merchandise, itcf_carry_quiver_back_right, 300, thrust_damage(5, pierce)|max_ammo(22)|abundance(60)|weight(3.0)|weapon_length(91), imodbits_missile],

	["arrow_f_standard", "Wildling Arrows", [("arrow_f_standard", imodbits_none), ("flying_missile", ixmesh_flying_ammo), ("arrow_f_standard_quiver", ixmesh_carry)], itp_type_arrows|itp_merchandise, itcf_carry_quiver_back_right, 100, thrust_damage(2, pierce)|max_ammo(22)|abundance(60)|weight(3.0)|weapon_length(91), imodbits_missile, [], [fac_kingdom_21]],

	["arrow_f_dornish", "Dornish Arrows", [("arrow_f_dornish", imodbits_none), ("flying_missile", ixmesh_flying_ammo), ("arrow_f_dornish_quiver", ixmesh_carry)], itp_type_arrows|itp_merchandise, itcf_carry_quiver_back_right, 200, thrust_damage(4, pierce)|max_ammo(22)|abundance(60)|weight(3.0)|weapon_length(91), imodbits_missile, [], [fac_kingdom_6]],

	["arrow_f_dothraki", "Dothraki Arrows", [("arrow_f_dothraki", imodbits_none), ("flying_missile", ixmesh_flying_ammo), ("arrow_f_dothraki_quiver", ixmesh_carry)], itp_type_arrows|itp_merchandise, itcf_carry_quiver_back, 500, thrust_damage(6, pierce)|max_ammo(22)|abundance(60)|weight(3.0)|weapon_length(91), imodbits_missile, [], [fac_kingdom_5, fac_kingdom_12, fac_kingdom_13, fac_kingdom_14, fac_kingdom_15, fac_kingdom_16, fac_kingdom_17]],

	["bolt_f_simple", "Bolts", [("bolt_f_simple", imodbits_none), ("flying_missile", ixmesh_flying_ammo), ("bolt_f_simple_bag", ixmesh_carry), ("bolt_f_simple_bag", imodbit_large_bag|ixmesh_carry)], itp_type_bolts|itp_default_ammo|itp_merchandise|itp_covers_legs|itp_doesnt_cover_hair|itp_can_penetrate_shield, itcf_carry_quiver_right_vertical, 200, thrust_damage(6, pierce)|max_ammo(30)|abundance(60)|weight(2.25)|weapon_length(63), imodbits_missile, [], [fac_kingdom_1, fac_kingdom_3, fac_kingdom_8, fac_kingdom_9, fac_kingdom_10]],

	["bolt_f_heavy", "Piercing Bolts", [("bolt_f_heavy", imodbits_none), ("flying_missile", ixmesh_flying_ammo), ("bolt_f_heavy_bag", ixmesh_carry), ("bolt_f_heavy_bag", imodbit_large_bag|ixmesh_carry)], itp_type_bolts|itp_default_ammo|itp_merchandise|itp_covers_legs|itp_doesnt_cover_hair|itp_can_penetrate_shield, itcf_carry_quiver_right_vertical, 800, thrust_damage(14, pierce)|max_ammo(30)|abundance(60)|weight(2.25)|weapon_length(63), imodbits_missile, [], [fac_kingdom_1, fac_kingdom_3, fac_kingdom_8, fac_kingdom_9, fac_kingdom_10]],

	["bolt_f_slash", "Heavy Bolts", [("bolt_f_slash", imodbits_none), ("flying_missile", ixmesh_flying_ammo), ("bolt_f_slash_bag", ixmesh_carry), ("bolt_f_slash_bag", imodbit_large_bag|ixmesh_carry)], itp_type_bolts|itp_default_ammo|itp_merchandise|itp_covers_legs|itp_doesnt_cover_hair|itp_can_penetrate_shield, itcf_carry_quiver_right_vertical, 600, thrust_damage(12, pierce)|max_ammo(30)|abundance(60)|weight(2.25)|weapon_length(63), imodbits_missile, [], [fac_kingdom_1, fac_kingdom_3, fac_kingdom_8, fac_kingdom_9, fac_kingdom_10]],

	["bolt_f_crippling", "Crippling Bolts", [("bolt_f_crippling", imodbits_none), ("flying_missile", ixmesh_flying_ammo), ("bolt_f_crippling_bag", ixmesh_carry), ("bolt_f_crippling_bag", imodbit_large_bag|ixmesh_carry)], itp_type_bolts|itp_default_ammo|itp_merchandise|itp_covers_legs|itp_doesnt_cover_hair|itp_can_penetrate_shield, itcf_carry_quiver_right_vertical, 400, thrust_damage(8, pierce)|max_ammo(30)|abundance(60)|weight(2.25)|weapon_length(63), imodbits_missile, [], [fac_kingdom_1, fac_kingdom_3, fac_kingdom_8, fac_kingdom_9, fac_kingdom_10]],

	["bolt_f_piercing", "Piercing Bolts", [("bolt_f_piercing", imodbits_none), ("flying_missile", ixmesh_flying_ammo), ("bolt_f_piercing_bag", ixmesh_carry), ("bolt_f_piercing_bag", imodbit_large_bag|ixmesh_carry)], itp_type_bolts|itp_default_ammo|itp_merchandise|itp_covers_legs|itp_doesnt_cover_hair|itp_can_penetrate_shield, itcf_carry_quiver_right_vertical, 800, thrust_damage(14, pierce)|max_ammo(30)|abundance(60)|weight(2.25)|weapon_length(63), imodbits_missile, [], [fac_kingdom_1, fac_kingdom_3, fac_kingdom_8, fac_kingdom_9, fac_kingdom_10]],

	["bolt_f_myrish", "Myrish Bolts", [("bolt_f_myrish", imodbits_none), ("flying_missile", ixmesh_flying_ammo), ("bolt_f_myrish_bag", ixmesh_carry), ("bolt_f_myrish_bag", imodbit_large_bag|ixmesh_carry)], itp_type_bolts|itp_default_ammo|itp_merchandise|itp_covers_legs|itp_doesnt_cover_hair|itp_can_penetrate_shield, itcf_carry_quiver_right_vertical, 1000, thrust_damage(16, pierce)|max_ammo(30)|abundance(60)|weight(2.25)|weapon_length(63), imodbits_missile, [], [fac_kingdom_14]],

	["bow_f_hunting_bow", "Hunting Bow", [("bow_f_hunting_bow", imodbits_none), ("bow_f_hunting_bow_carry", ixmesh_carry)], itp_type_bow|itp_merchandise|itp_two_handed|itp_primary, itcf_shoot_bow|itcf_carry_bow_back, 200, thrust_damage(18, pierce)|spd_rtng(90)|abundance(80)|weight(1.0)|accuracy(70)|difficulty(1)|shoot_speed(52), imodbits_bow],

	["bow_f_simple", "Short Bow", [("bow_f_simple", imodbits_none), ("bow_f_simple_carry", ixmesh_carry)], itp_type_bow|itp_merchandise|itp_two_handed|itp_primary, itcf_shoot_bow|itcf_carry_bow_back, 300, thrust_damage(21, pierce)|spd_rtng(95)|abundance(80)|weight(1.0)|accuracy(80)|difficulty(1)|shoot_speed(60), imodbits_bow],

	["bow_f_longbow_1", "Longbow", [("bow_f_longbow_1", imodbits_none), ("bow_f_longbow_1_carry", ixmesh_carry)], itp_type_bow|itp_merchandise|itp_two_handed|itp_primary|itp_cant_use_on_horseback, itcf_shoot_bow|itcf_carry_bow_back, 500, thrust_damage(32, pierce)|spd_rtng(75)|abundance(80)|weight(1.0)|accuracy(90)|difficulty(3)|shoot_speed(90), imodbits_bow, [], [fac_kingdom_1, fac_kingdom_2, fac_kingdom_3, fac_kingdom_8, fac_kingdom_9, fac_kingdom_10, fac_kingdom_11]],

	["bow_f_longbow_2", "Flatbow", [("bow_f_longbow_2", imodbits_none), ("bow_f_longbow_2_carry", ixmesh_carry)], itp_type_bow|itp_merchandise|itp_two_handed|itp_primary|itp_cant_use_on_horseback, itcf_shoot_bow|itcf_carry_bow_back, 800, thrust_damage(32, pierce)|spd_rtng(80)|abundance(80)|weight(1.0)|accuracy(90)|difficulty(3)|shoot_speed(90), imodbits_bow, [], [fac_kingdom_1, fac_kingdom_2, fac_kingdom_3, fac_kingdom_8, fac_kingdom_9, fac_kingdom_10, fac_kingdom_11]],

	["bow_f_dothraki", "Recurved Bow", [("bow_f_dothraki", imodbits_none), ("bow_f_dothraki_carry", ixmesh_carry)], itp_type_bow|itp_merchandise|itp_two_handed|itp_primary, itcf_shoot_bow|itcf_carry_bow_back, 600, thrust_damage(25, pierce)|spd_rtng(95)|abundance(80)|weight(1.0)|accuracy(95)|difficulty(2)|shoot_speed(80), imodbits_bow, [], [fac_kingdom_4, fac_kingdom_5, fac_kingdom_12, fac_kingdom_13, fac_kingdom_14, fac_kingdom_15, fac_kingdom_16, fac_kingdom_17, fac_kingdom_18]],

	["bow_f_dornish", "Recurved Bow", [("bow_f_dornish", imodbits_none), ("bow_f_dornish_carry", ixmesh_carry)], itp_type_bow|itp_merchandise|itp_two_handed|itp_primary, itcf_shoot_bow|itcf_carry_bow_back, 600, thrust_damage(25, pierce)|spd_rtng(95)|abundance(80)|weight(1.0)|accuracy(95)|difficulty(2)|shoot_speed(80), imodbits_bow, [], [fac_kingdom_6]],

	["bow_f_decorated_bow", "Decorated Longbow", [("bow_f_decorated_bow", imodbits_none), ("bow_f_decorated_bow_carry", ixmesh_carry)], itp_type_bow|itp_merchandise|itp_two_handed|itp_primary|itp_cant_use_on_horseback, itcf_shoot_bow|itcf_carry_bow_back, 900, thrust_damage(34, pierce)|spd_rtng(80)|abundance(80)|weight(1.0)|accuracy(95)|difficulty(3)|shoot_speed(95), imodbits_bow, [], [fac_kingdom_1, fac_kingdom_2, fac_kingdom_3, fac_kingdom_8, fac_kingdom_9, fac_kingdom_10, fac_kingdom_11]],

	["crossbow_f_simple_1", "Hunting Crossbow", [("crossbow_f_simple_1", imodbits_none)], itp_type_crossbow|itp_merchandise|itp_two_handed|itp_primary, itcf_shoot_crossbow|itcf_carry_crossbow_back, 300, thrust_damage(25, pierce)|max_ammo(1)|spd_rtng(50)|abundance(120)|weight(2.25)|accuracy(90)|shoot_speed(75), imodbits_crossbow, [], [fac_kingdom_1, fac_kingdom_3, fac_kingdom_5, fac_kingdom_8, fac_kingdom_9, fac_kingdom_10, fac_kingdom_4]],

	["crossbow_f_simple_2", "Light Crossbow", [("crossbow_f_simple_2", imodbits_none)], itp_type_crossbow|itp_merchandise|itp_two_handed|itp_primary, itcf_shoot_crossbow|itcf_carry_crossbow_back, 600, thrust_damage(30, pierce)|max_ammo(1)|spd_rtng(50)|abundance(120)|weight(2.25)|accuracy(95)|shoot_speed(80), imodbits_crossbow, [], [fac_kingdom_1, fac_kingdom_3, fac_kingdom_5, fac_kingdom_8, fac_kingdom_9, fac_kingdom_10, fac_kingdom_4]],

	["crossbow_f_medium", "Crossbow", [("crossbow_f_medium", imodbits_none)], itp_type_crossbow|itp_merchandise|itp_cant_reload_on_horseback|itp_two_handed|itp_primary, itcf_shoot_crossbow|itcf_carry_crossbow_back, 800, thrust_damage(40, pierce)|max_ammo(1)|spd_rtng(50)|abundance(120)|weight(2.25)|accuracy(95)|shoot_speed(90), imodbits_crossbow, [], [fac_kingdom_1, fac_kingdom_3, fac_kingdom_5, fac_kingdom_8, fac_kingdom_9, fac_kingdom_10, fac_kingdom_4]],

	["crossbow_f_heavy", "Heavy Crossbow", [("crossbow_f_heavy", imodbits_none)], itp_type_crossbow|itp_merchandise|itp_cant_reload_on_horseback|itp_two_handed|itp_primary, itcf_shoot_crossbow|itcf_carry_crossbow_back, 1200, thrust_damage(50, pierce)|max_ammo(1)|spd_rtng(45)|abundance(120)|weight(2.25)|accuracy(95)|shoot_speed(99), imodbits_crossbow, [], [fac_kingdom_1, fac_kingdom_3, fac_kingdom_5, fac_kingdom_8, fac_kingdom_9, fac_kingdom_10, fac_kingdom_4]],

	["crossbow_f_myrish", "Myrish Crossbow", [("crossbow_f_myrish", imodbits_none)], itp_type_crossbow|itp_merchandise|itp_cant_reload_on_horseback|itp_two_handed|itp_primary, itcf_shoot_crossbow|itcf_carry_crossbow_back, 1600, thrust_damage(58, pierce)|max_ammo(1)|spd_rtng(45)|abundance(120)|weight(2.25)|accuracy(99)|shoot_speed(99), imodbits_crossbow, [], [fac_kingdom_14]],

	["we_khe_throw_stone", "Stones", [("we_khe_throw_stone", imodbits_none)], itp_type_thrown|itp_primary, itcf_throw_stone, 1, thrust_damage(14, blunt)|max_ammo(6)|spd_rtng(97)|abundance(100)|weight(4.0)|weapon_length(8)|shoot_speed(30), imodbit_large_bag, [], [fac_kingdom_1]],

	["we_sar_spear_javelin", "Javelins", [("we_sar_spear_javelin", imodbits_none), ("we_sar_spear_javelin_quiver", ixmesh_carry)], itp_type_thrown|itp_merchandise|itp_primary|itp_civilian|itp_next_item_as_melee, itcf_throw_javelin|itcf_carry_quiver_back|itcf_show_holster_when_drawn, 800, thrust_damage(47, pierce)|max_ammo(4)|spd_rtng(91)|abundance(100)|weight(5.0)|difficulty(4)|weapon_length(75)|shoot_speed(25), imodbits_thrown, [], [fac_kingdom_12, fac_kingdom_13, fac_kingdom_14, fac_kingdom_15, fac_kingdom_16, fac_kingdom_5, fac_kingdom_17, fac_kingdom_18]],

	["we_sar_spear_javelin_melee", "Short Spear", [("we_sar_spear_javelin", imodbits_none)], itp_type_polearm|itp_wooden_parry|itp_primary, itcf_carry_spear|itc_staff, 400, thrust_damage(22, pierce)|hit_points(18432)|spd_rtng(100)|abundance(100)|weight(3.0)|swing_damage(18, cut)|weapon_length(75), imodbits_polearm, [], [fac_kingdom_11, fac_kingdom_19]],

	["we_sar_spear_throwing_spears", "Throwing Spears", [("we_sar_spear_throwing_spears", imodbits_none), ("we_sar_spear_throwing_spears_bag", ixmesh_carry)], itp_type_thrown|itp_merchandise|itp_primary|itp_civilian|itp_next_item_as_melee, itcf_throw_javelin|itcf_carry_quiver_back|itcf_show_holster_when_drawn, 900, thrust_damage(45, pierce)|max_ammo(4)|spd_rtng(87)|abundance(100)|weight(4.0)|difficulty(2)|weapon_length(65)|shoot_speed(22), imodbits_thrown, [], [fac_kingdom_12, fac_kingdom_13, fac_kingdom_14, fac_kingdom_15, fac_kingdom_16, fac_kingdom_5, fac_kingdom_17, fac_kingdom_18]],

	["we_sar_spear_throwing_spear_melee", "Short Spear", [("we_sar_spear_throwing_spears", imodbits_none), ("we_sar_spear_throwing_spears_bag", ixmesh_carry)], itp_type_polearm|itp_wooden_parry|itp_primary, itc_staff, 400, thrust_damage(22, pierce)|hit_points(18432)|spd_rtng(100)|abundance(100)|weight(3.0)|swing_damage(18, cut)|difficulty(1)|weapon_length(75), imodbits_thrown, [], [fac_kingdom_11, fac_kingdom_19]],

	["we_sar_spear_jarid", "Jarids", [("we_sar_spear_jarid", imodbits_none), ("we_sar_spear_jarid_quiver", ixmesh_carry)], itp_type_thrown|itp_merchandise|itp_primary|itp_civilian|itp_next_item_as_melee, itcf_throw_javelin|itcf_carry_quiver_back|itcf_show_holster_when_drawn, 800, thrust_damage(42, pierce)|max_ammo(3)|spd_rtng(89)|abundance(100)|weight(4.0)|difficulty(2)|weapon_length(65)|shoot_speed(24), imodbits_thrown, [], [fac_kingdom_12, fac_kingdom_13, fac_kingdom_14, fac_kingdom_15, fac_kingdom_16, fac_kingdom_5, fac_kingdom_17, fac_kingdom_18]],

	["we_sar_spear_jarid_melee", "Short Spear", [("we_sar_spear_jarid", imodbits_none), ("we_sar_spear_jarid_quiver", ixmesh_carry)], itp_type_polearm|itp_wooden_parry|itp_primary, itcf_carry_spear|itc_staff, 400, thrust_damage(22, pierce)|hit_points(18432)|spd_rtng(100)|abundance(100)|weight(3.0)|swing_damage(18, cut)|difficulty(2)|weapon_length(65), imodbits_thrown, [], [fac_kingdom_11, fac_kingdom_19]],

	["ar_vae_t7_elite_b", "Heavy Lamellar Plate Armor", [("ar_vae_t7_elite_b", imodbits_none)], itp_type_body_armor|itp_covers_legs|itp_doesnt_cover_hair|itp_can_penetrate_shield, 0, 6000, abundance(10)|weight(25.0)|leg_armor(8)|difficulty(14)|body_armor(54), imodbits_plate, [], [fac_kingdom_17, fac_kingdom_5]],

	["ar_khe_t2_armor_a", "Fur Armor", [("ar_khe_t2_armor_a", imodbits_none)], itp_type_body_armor|itp_covers_legs|itp_doesnt_cover_hair|itp_can_penetrate_shield, 0, 150, abundance(60)|weight(8.0)|leg_armor(5)|body_armor(20), imodbits_cloth, [], [fac_kingdom_2]],

	["ar_khe_t6_tunic_a", "Heavy Dornish Armor", [("ar_khe_t6_tunic_a", imodbits_none)], itp_type_body_armor|itp_merchandise|itp_covers_legs|itp_doesnt_cover_hair|itp_can_penetrate_shield, 0, 8000, abundance(50)|weight(20.0)|leg_armor(11)|difficulty(12)|body_armor(42), imodbits_plate, [], [fac_kingdom_6]],

	["ar_nor_t7_vikingbyrnie_a", "Decorated Chain Mail Hauberk", [("ar_nor_t7_vikingbyrnie_a", imodbits_none)], itp_type_body_armor|itp_merchandise|itp_covers_legs|itp_doesnt_cover_hair|itp_can_penetrate_shield, 0, 5000, abundance(40)|weight(20.0)|leg_armor(7)|difficulty(12)|body_armor(40), imodbits_armor, [], [fac_kingdom_11, fac_kingdom_19]],

	["ar_rho_ban_highlander_a", "Clansmans Outfit", [("ar_rho_ban_highlander_a", imodbits_none)], itp_type_body_armor|itp_covers_legs|itp_doesnt_cover_hair|itp_can_penetrate_shield, 0, 200, abundance(10)|weight(8.0)|leg_armor(6)|body_armor(15), imodbits_cloth, [], [fac_kingdom_5]],

	["ar_rho_t4_highlander_a", "Clansmans Lamellar Armor", [("ar_rho_t4_highlander_a", imodbits_none)], itp_type_body_armor|itp_covers_legs|itp_doesnt_cover_hair|itp_can_penetrate_shield, 0, 500, abundance(70)|weight(16.0)|leg_armor(5)|difficulty(10)|body_armor(25), imodbits_armor, [], [fac_kingdom_5]],

	["ar_pla_t6_heraldic_a", "Heraldic Heavy Plate Armor", [("ar_pla_t6_heraldic_a", imodbits_none)], itp_type_body_armor|itp_merchandise|itp_covers_legs|itp_doesnt_cover_hair|itp_can_penetrate_shield, 0, 9000, abundance(40)|weight(25.0)|leg_armor(10)|difficulty(12)|body_armor(54), imodbits_plate, 
	[(ti_on_init_item,
		[
			(store_trigger_param_1, ":trigger_param_1"),
			(store_trigger_param_2, ":trigger_param_2"),
			(call_script, "script_shield_item_set_banner", "tableau_ar_pla_t6_heraldic", ":trigger_param_1", ":trigger_param_2")
		])]
	, [fac_kingdom_10]],

	["ar_swa_shi_linen", "Brown Robe", [("ar_pla_pri_monkrobe", imodbits_none)], itp_type_body_armor|itp_merchandise|itp_covers_legs|itp_doesnt_cover_hair|itp_can_penetrate_shield|itp_civilian|itp_next_item_as_melee, 0, 6, abundance(60)|weight(3.0)|leg_armor(1)|body_armor(3), imodbits_cloth, [], [fac_kingdom_1, fac_kingdom_8, fac_kingdom_9, fac_kingdom_10, fac_kingdom_20]],

	["ar_swa_tun_tabard", "Expensive Tunic", [("ar_pla_mer_surgeon", imodbits_none)], itp_type_body_armor|itp_covers_legs|itp_doesnt_cover_hair|itp_can_penetrate_shield|itp_civilian|itp_next_item_as_melee, 0, 100, abundance(60)|weight(3.0)|leg_armor(2)|body_armor(10), imodbits_cloth, [], [fac_kingdom_1, fac_kingdom_8, fac_kingdom_9, fac_kingdom_10, fac_kingdom_20]],

	["brown_robe", "Brown Robe", [("ar_pla_pri_monkrobe", imodbits_none)], itp_type_body_armor|itp_merchandise|itp_covers_legs|itp_doesnt_cover_hair|itp_can_penetrate_shield, 0, 6, abundance(60)|weight(3.0)|leg_armor(1)|body_armor(3), imodbits_cloth, [], [fac_kingdom_1, fac_kingdom_8, fac_kingdom_9, fac_kingdom_10, fac_kingdom_20]],

	["ar_pla_pri_pilgrimdisguise", "Disguise", [("archer_a", imodbits_none)], itp_type_body_armor|itp_covers_legs|itp_doesnt_cover_hair|itp_can_penetrate_shield|itp_civilian|itp_next_item_as_melee, 0, 100, abundance(80)|weight(2.0)|leg_armor(10)|body_armor(10), imodbits_cloth, [], [fac_kingdom_1, fac_kingdom_8, fac_kingdom_9, fac_kingdom_10, fac_kingdom_20]],

	["dress_general_bride", "Bride Dress", [("bride_style_dress", imodbits_none)], itp_type_body_armor|itp_covers_legs|itp_doesnt_cover_hair|itp_can_penetrate_shield|itp_civilian|itp_next_item_as_melee, 0, 500, abundance(60)|weight(3.0)|leg_armor(10)|body_armor(10), imodbits_cloth],

	["bo_gen_t0_bride_shoes", "Bride Shoes", [("bo_vae_t2_shoes", imodbits_none)], itp_type_foot_armor|itp_attach_armature|itp_attachment_mask|itp_civilian|itp_next_item_as_melee, 0, 30, abundance(60)|weight(1.0)|leg_armor(8), imodbits_cloth],

	["bo_swa_t4_sandal", "Plated Sandals", [("full_shoe_4", imodbits_none)], itp_type_foot_armor|itp_attach_armature|itp_attachment_mask|itp_merchandise, 0, 800, abundance(70)|weight(3.0)|leg_armor(20), imodbits_cloth, [], [fac_kingdom_1, fac_kingdom_8, fac_kingdom_9, fac_kingdom_10, fac_kingdom_20]],

	["bo_swa_t6_mail", "Plated Mail Boots", [("full_plate_boots_2", imodbits_none)], itp_type_foot_armor|itp_attach_armature|itp_attachment_mask|itp_merchandise, 0, 800, abundance(50)|weight(3.0)|leg_armor(20)|difficulty(12), imodbits_armor, [], [fac_kingdom_1, fac_kingdom_8, fac_kingdom_9, fac_kingdom_10, fac_kingdom_20]],

	["bo_vae_t2_shoes", "Shoes", [("bo_vae_t2_shoes", imodbits_none)], itp_type_foot_armor|itp_attach_armature|itp_attachment_mask|itp_merchandise|itp_civilian|itp_next_item_as_melee, 0, 50, abundance(60)|weight(1.0)|leg_armor(5), imodbits_cloth],

	["bo_vae_t3_leather", "Leather Boots", [("bo_vae_t3_leather", imodbits_none)], itp_type_foot_armor|itp_attach_armature|itp_attachment_mask|itp_merchandise|itp_civilian|itp_next_item_as_melee, 0, 200, abundance(80)|weight(1.0)|leg_armor(14), imodbits_cloth],

	["bo_vae_t4_shoes", "Leather Plated Shoes", [("bo_vae_t4_shoes", imodbits_none)], itp_type_foot_armor|itp_attach_armature|itp_attachment_mask|itp_merchandise, 0, 800, abundance(70)|weight(1.0)|leg_armor(20), imodbits_cloth],

	["bo_khe_t0_sandal", "Mail Boots", [("full_chain_boot_1", imodbits_none)], itp_type_foot_armor|itp_attach_armature|itp_attachment_mask|itp_merchandise, 0, 1000, abundance(80)|weight(3.0)|leg_armor(26), imodbits_armor],

	["bo_khe_t2_boots", "Leather Boots", [("full_leatherboot_1", imodbits_none)], itp_type_foot_armor|itp_attach_armature|itp_attachment_mask|itp_merchandise|itp_civilian|itp_next_item_as_melee, 0, 200, abundance(60)|weight(3.0)|leg_armor(14), imodbits_cloth],

	["bo_khe_t4_sandal", "Leather Boots", [("full_leatherboot_2", imodbits_none)], itp_type_foot_armor|itp_attach_armature|itp_attachment_mask|itp_merchandise|itp_civilian|itp_next_item_as_melee, 0, 200, abundance(70)|weight(3.0)|leg_armor(14), imodbits_cloth, [], [fac_kingdom_1, fac_kingdom_8, fac_kingdom_9, fac_kingdom_10, fac_kingdom_20]],

	["bo_khe_t6_mail", "Plated Leather Boots", [("full_leatherboot_3", imodbits_none)], itp_type_foot_armor|itp_attach_armature|itp_attachment_mask|itp_merchandise, 0, 800, abundance(50)|weight(1.0)|leg_armor(20), imodbits_none, [], [fac_kingdom_3]],

	["bo_nor_t2_shoes", "Leather Boots", [("full_leatherboot_4", imodbits_none)], itp_type_foot_armor|itp_attach_armature|itp_attachment_mask|itp_merchandise|itp_civilian|itp_next_item_as_melee, 0, 200, abundance(60)|weight(1.0)|leg_armor(14), imodbits_cloth],

	["bo_rho_t3_highlander", "Fur Boots", [("bo_rho_t3_highlander", imodbits_none)], itp_type_foot_armor|itp_attach_armature|itp_attachment_mask|itp_merchandise|itp_civilian|itp_next_item_as_melee, 0, 100, abundance(80)|weight(1.25)|leg_armor(10), imodbits_cloth, [], [fac_kingdom_5]],

	["bo_rho_t4_greaves", "Splinted Greaves", [("bo_rho_t4_greaves", imodbits_none)], itp_type_foot_armor|itp_attach_armature|itp_attachment_mask|itp_merchandise, 0, 1000, abundance(70)|weight(3.0)|leg_armor(32), imodbits_cloth, [], [fac_kingdom_11, fac_kingdom_19]],

	["bo_rho_t5_greaves", "Splinted Mail Greaves", [("bo_rho_t5_greaves", imodbits_none)], itp_type_foot_armor|itp_attach_armature|itp_attachment_mask|itp_merchandise, 0, 1000, abundance(60)|weight(3.0)|leg_armor(32), imodbits_armor, [], [fac_kingdom_11, fac_kingdom_19]],

	["bo_sar_t4_camel", "Woolen Hoses", [("full_shoe_1", imodbits_none)], itp_type_foot_armor|itp_attach_armature|itp_attachment_mask, 0, 50, abundance(70)|weight(1.0)|leg_armor(5), imodbits_cloth],

	["bo_sar_t6_mail", "Shoes", [("full_shoe_2", imodbits_none)], itp_type_foot_armor|itp_attach_armature|itp_attachment_mask, 0, 50, abundance(50)|weight(3.0)|leg_armor(5), imodbits_armor],

	["bo_sar_t7_greaves", "Shoes", [("full_shoe_3", imodbits_none)], itp_type_foot_armor|itp_attach_armature|itp_attachment_mask, 0, 50, abundance(40)|weight(3.0)|leg_armor(5), imodbits_armor],

	["bo_pla_str_samurai", "Shoes", [("full_shoe_5", imodbits_none)], itp_type_foot_armor|itp_attach_armature|itp_attachment_mask, 0, 50, abundance(10)|weight(3.0)|leg_armor(5), imodbits_cloth],

	["bo_pla_t1_priest", "Leather Boots", [("full_leatherboot_5", imodbits_none)], itp_type_foot_armor|itp_attach_armature|itp_attachment_mask|itp_merchandise|itp_civilian|itp_next_item_as_melee, 0, 200, abundance(60)|weight(1.0)|leg_armor(14), imodbits_cloth],

	["bo_pla_t2_ankle", "Leather Boots", [("full_leatherboot_6", imodbits_none)], itp_type_foot_armor|itp_attach_armature|itp_attachment_mask|itp_civilian|itp_next_item_as_melee, 0, 100, abundance(60)|weight(1.0)|leg_armor(14), imodbits_cloth],

	["bo_pla_t5_highlander", "Mail Boots", [("bo_pla_t5_highlander", imodbits_none)], itp_type_foot_armor|itp_attach_armature|itp_attachment_mask|itp_merchandise, 0, 800, abundance(60)|weight(3.0)|leg_armor(26), imodbits_armor, [], [fac_kingdom_2, fac_kingdom_3]],

	["bo_pla_t7_greaves", "Plate Boots", [("full_plate_boots_1", imodbits_none)], itp_type_foot_armor|itp_attach_armature|itp_attachment_mask, 0, 2000, abundance(40)|weight(3.0)|leg_armor(40)|difficulty(12), imodbits_armor, [], [fac_kingdom_1, fac_kingdom_8, fac_kingdom_9, fac_kingdom_10, fac_kingdom_20]],

	["ga_swa_a4_plate", "Plate Mittens", [("ga_swa_a4_plate_L", imodbits_none)], itp_type_hand_armor|itp_merchandise, 0, 1000, abundance(20)|weight(2.0)|difficulty(12)|body_armor(12), imodbits_armor, [], [fac_kingdom_1, fac_kingdom_8, fac_kingdom_9, fac_kingdom_10, fac_kingdom_20]],

	["ga_swa_a6_plate", "Plate Gauntlets", [("full_glove1_L", imodbits_none)], itp_type_hand_armor|itp_merchandise, 0, 1000, abundance(20)|weight(2.0)|difficulty(12)|body_armor(12), imodbits_armor, [], [fac_kingdom_1, fac_kingdom_8, fac_kingdom_9, fac_kingdom_10, fac_kingdom_20]],

	["ga_vae_a5_mail", "Mail Gauntlets", [("full_glove3_L", imodbits_none)], itp_type_hand_armor|itp_merchandise, 0, 400, abundance(60)|weight(2.0)|body_armor(10), imodbits_armor],

	["ga_vae_a6_black", "Iron Gauntlets", [("ga_vae_a6_black_L", imodbits_none)], itp_type_hand_armor|itp_merchandise, 0, 1000, abundance(20)|weight(2.0)|difficulty(12)|body_armor(12), imodbits_armor, [], [fac_kingdom_9, fac_kingdom_10]],

	["ga_khe_a5_armor", "Lamellar Gloves", [("full_glove5_L", imodbits_none)], itp_type_hand_armor, 0, 400, abundance(60)|weight(1.0)|body_armor(10), imodbits_armor, [], [fac_kingdom_12, fac_kingdom_13, fac_kingdom_14, fac_kingdom_15, fac_kingdom_16, fac_kingdom_17, fac_kingdom_5, fac_kingdom_18]],

	["ga_khe_a6_lamellar", "Lamellar Gloves", [("full_glove6_L", imodbits_none)], itp_type_hand_armor, 0, 400, abundance(40)|weight(1.0)|body_armor(10), imodbits_armor, [], [fac_kingdom_12, fac_kingdom_13, fac_kingdom_14, fac_kingdom_15, fac_kingdom_16, fac_kingdom_17, fac_kingdom_5, fac_kingdom_18]],

	["ga_rho_a2_leather", "Leather Gloves", [("full_glove4_L", imodbits_none)], itp_type_hand_armor|itp_merchandise, 0, 100, abundance(60)|weight(1.0)|body_armor(5), imodbits_cloth],

	["ga_rho_a5_bnw", "Decorated Plate Gauntlets", [("ga_rho_a5_bnw_L", imodbits_none)], itp_type_hand_armor, 0, 1300, abundance(20)|weight(2.0)|difficulty(12)|body_armor(12), imodbits_armor, [], [fac_kingdom_4]],

	["ga_rho_a6_hourglass", "Iron Gauntlets", [("ga_rho_a6_hourglass_L", imodbits_none)], itp_type_hand_armor|itp_merchandise, 0, 1000, abundance(20)|weight(2.0)|difficulty(12)|body_armor(12), imodbits_armor, [], [fac_kingdom_9, fac_kingdom_10]],

	["ga_pla_a5_iron", "Plate Gauntlets", [("full_glove2_L", imodbits_none)], itp_type_hand_armor, 0, 1000, abundance(20)|weight(2.0)|difficulty(12)|body_armor(12), imodbits_armor, [], [fac_kingdom_1, fac_kingdom_8, fac_kingdom_9, fac_kingdom_10, fac_kingdom_20]],

	["he_gen_lad_bride_crown", "Wimple Top", [("he_nor_lad_common_a", imodbits_none)], itp_type_head_armor|itp_civilian|itp_next_item_as_melee|itp_fit_to_head|itp_offset_lance, 0, 3, abundance(60)|weight(1.0)|head_armor(2), imodbits_cloth, [], [fac_kingdom_4]],

	["he_swa_lad_common_a", "White Headcloth", [("he_swa_lad_common_a", imodbits_none)], itp_type_head_armor|itp_civilian|itp_next_item_as_melee, 0, 5, abundance(60)|weight(1.0)|head_armor(3), imodbits_cloth, [], [fac_kingdom_1]],

	["he_swa_t1_common_a", "Common Hood", [("he_swa_t1_common_a", imodbits_none)], itp_type_head_armor|itp_civilian|itp_next_item_as_melee, 0, 5, abundance(60)|weight(1.0)|head_armor(3), imodbits_cloth, [], [fac_kingdom_1, fac_kingdom_8, fac_kingdom_9, fac_kingdom_10, fac_kingdom_20]],

	["he_swa_t1_noble_a", "Arming Cap", [("he_swa_t1_noble_a", imodbits_none)], itp_type_head_armor|itp_civilian|itp_next_item_as_melee, 0, 7, abundance(40)|weight(1.0)|head_armor(4), imodbits_cloth, [], [fac_kingdom_1, fac_kingdom_8, fac_kingdom_9, fac_kingdom_10, fac_kingdom_20]],

	["he_vae_lad_lady_a", "Barbette", [("he_vae_lad_lady_a", imodbits_none)], itp_type_head_armor|itp_civilian|itp_next_item_as_melee|itp_fit_to_head|itp_offset_lance, 0, 180, abundance(40)|weight(1.0)|head_armor(3), imodbits_cloth, [], [fac_kingdom_2]],

	["he_vae_t1_common_a", "Felt Hat", [("he_vae_t1_common_a", imodbits_none)], itp_type_head_armor|itp_merchandise|itp_civilian|itp_next_item_as_melee, 0, 7, abundance(60)|weight(1.0)|head_armor(4), imodbits_cloth, [], [fac_kingdom_1, fac_kingdom_8, fac_kingdom_9, fac_kingdom_10, fac_kingdom_20]],

	["he_khe_lad_common_a", "Leather Cap", [("he_khe_lad_common_a", imodbits_none)], itp_type_head_armor|itp_merchandise|itp_civilian|itp_next_item_as_melee, 0, 100, abundance(60)|weight(1.0)|head_armor(5), imodbits_cloth, [], [fac_kingdom_3]],

	["he_nor_t1_common_a", "Woolen Cap", [("he_nor_t1_common_a", imodbits_none)], itp_type_head_armor|itp_merchandise|itp_civilian|itp_next_item_as_melee, 0, 3, abundance(60)|weight(1.0)|head_armor(2), imodbits_cloth, [], [fac_kingdom_1, fac_kingdom_8, fac_kingdom_9, fac_kingdom_10, fac_kingdom_20]],

	["he_pla_pri_noel", "Boar Helmet", [("BL_boarhelmet", imodbits_none)], itp_type_head_armor|itp_civilian|itp_next_item_as_melee|itp_fit_to_head|itp_offset_lance, 0, 100, abundance(10)|weight(4.0)|head_armor(20), imodbits_none, [], [fac_player_faction]],

	["he_swa_t2_coif_a", "Padded Coif", [("he_swa_t2_coif_a", imodbits_none)], itp_type_head_armor|itp_merchandise, 0, 16, abundance(60)|weight(1.0)|head_armor(8), imodbits_cloth, [], [fac_kingdom_1, fac_kingdom_8, fac_kingdom_9, fac_kingdom_10, fac_kingdom_20]],

	["he_swa_t3_helmet_a", "Goat Helmet", [("goat_cap", imodbits_none)], itp_type_head_armor, 0, 100, abundance(80)|weight(3.0)|head_armor(15), imodbits_none, [], [fac_kingdom_1]],

	["he_swa_t4_bascinet_a", "Straw Hat", [("straw_hat_new_bry", imodbits_none)], itp_type_head_armor|itp_merchandise, 0, 5, abundance(70)|weight(1.0)|head_armor(1), imodbits_none, [], [fac_kingdom_1, fac_kingdom_10]],

	["he_vae_t6_warhelmet_a", "Felt Hat", [("felt_hat_coif", imodbits_none)], itp_type_head_armor|itp_merchandise, 0, 100, abundance(50)|weight(1.0)|head_armor(5), imodbits_cloth, [], [fac_kingdom_1, fac_kingdom_8, fac_kingdom_9, fac_kingdom_10, fac_kingdom_20]],

	["he_vae_t7_warmask_a", "Great Helmet", [("fi_greathelmet_4", imodbits_none)], itp_type_head_armor|itp_covers_beard, 0, 2000, abundance(20)|weight(6.0)|difficulty(14)|head_armor(45), imodbits_plate, [], [fac_kingdom_1, fac_kingdom_8]],

	["he_vae_t7_warmask_b", "Leather Cap", [("fi_leather_helmet", imodbits_none)], itp_type_head_armor|itp_merchandise, 0, 400, abundance(40)|weight(6.0)|head_armor(20), imodbits_cloth],

	["he_khe_t2_steppe_a", "Leather Fur Cap", [("he_khe_t2_steppe_a", imodbits_none)], itp_type_head_armor|itp_merchandise, 0, 50, abundance(60)|weight(1.0)|head_armor(8), imodbits_cloth, [], [fac_kingdom_3]],

	["he_khe_t3_steppe_a", "Leather Helmet", [("he_khe_t3_steppe_a", imodbits_none)], itp_type_head_armor|itp_merchandise, 0, 48, abundance(80)|weight(1.0)|head_armor(18), imodbits_cloth, [], [fac_kingdom_3]],

	["he_khe_t4_war_a", "Hounskull Helmet", [("hounskull", imodbits_none)], itp_type_head_armor|itp_merchandise, 0, 2000, abundance(10)|weight(6.0)|difficulty(13)|head_armor(45), imodbits_plate, [], [fac_kingdom_9, fac_kingdom_10, fac_kingdom_20]],

	["he_khe_t5_neck_a", "Great Helmet", [("fi_greathelmet_3", imodbits_none)], itp_type_head_armor|itp_merchandise, 0, 2000, abundance(10)|weight(6.0)|difficulty(14)|head_armor(45), imodbits_plate, [], [fac_kingdom_1, fac_kingdom_8]],

	["he_nor_t2_spangen_a", "Nasal Helmet", [("fi_ironborn_helmet_1", imodbits_none)], itp_type_head_armor|itp_merchandise, 0, 1400, abundance(20)|weight(4.0)|difficulty(12)|head_armor(30), imodbits_armor, [], [fac_kingdom_11, fac_kingdom_19]],

	["he_nor_t3_valsgarde_a", "Nasal Helmet", [("fi_ironborn_helmet_2", imodbits_none)], itp_type_head_armor|itp_merchandise, 0, 1400, abundance(20)|weight(4.0)|difficulty(12)|head_armor(33), imodbits_armor, [], [fac_kingdom_11, fac_kingdom_19]],

	["he_nor_t5_valsgarde_a", "Nasal Helmet", [("fi_lannister_helmet", imodbits_none)], itp_type_head_armor|itp_merchandise, 0, 1400, abundance(20)|weight(4.0)|difficulty(12)|head_armor(37), imodbits_armor, [], [fac_kingdom_11, fac_kingdom_19]],

	["he_rho_t2_beret_a", "Leather Cap", [("he_rho_t2_beret_a", imodbits_none)], itp_type_head_armor|itp_merchandise, 0, 18, abundance(60)|weight(1.0)|head_armor(9), imodbits_cloth, [], [fac_kingdom_1, fac_kingdom_2, fac_kingdom_3, fac_kingdom_5, fac_kingdom_8, fac_kingdom_9, fac_kingdom_10, fac_kingdom_11]],

	["he_rho_t5_kettle_a", "Nasal Helmet", [("fi_nasal_helmet_1", imodbits_none)], itp_type_head_armor|itp_merchandise, 0, 1400, abundance(10)|weight(4.0)|difficulty(12)|head_armor(35), imodbits_armor, [], [fac_kingdom_1, fac_kingdom_2, fac_kingdom_3, fac_kingdom_5, fac_kingdom_8, fac_kingdom_9]],

	["he_pla_t7_gerulfingen", "Armet", [("fi_armet_1", imodbits_none)], itp_type_head_armor|itp_merchandise|itp_covers_beard, 0, 2000, abundance(5)|weight(6.0)|difficulty(14)|head_armor(45), imodbits_plate, [], [fac_kingdom_10]],

	["he_pla_t7_crusader_a", "Sallet", [("milanese_sallet", imodbits_none)], itp_type_head_armor|itp_merchandise|itp_covers_head|itp_couchable, 0, 2000, abundance(5)|weight(4.0)|difficulty(13)|head_armor(45), imodbits_plate, [], [fac_kingdom_1]],

	["he_pla_t7_crusader_b", "Armet", [("fi_armet_2", imodbits_none)], itp_type_head_armor|itp_merchandise|itp_covers_head|itp_couchable, 0, 2000, abundance(5)|weight(6.0)|difficulty(14)|head_armor(45), imodbits_plate, [], [fac_kingdom_10]],

	["sh_swa_rou_bandit_a", "Clansmans Shield", [("sh_swa_rou_bandit_a", imodbits_none)], itp_type_shield|itp_wooden_parry, itcf_carry_round_shield, 100, hit_points(200)|spd_rtng(100)|abundance(10)|weight(5.0)|shield_width(30)|body_armor(5), imodbits_shield, [], [fac_kingdom_1]],

	["sh_swa_hea_plain", "Heater Shield", [("tableau_shield_heater_1", imodbits_none)], itp_type_shield|itp_merchandise|itp_wooden_parry, itcf_carry_kite_shield, 74, hit_points(210)|spd_rtng(93)|abundance(100)|weight(2.5)|shield_width(36)|shield_height(70)|body_armor(10), imodbits_shield, 
	[(ti_on_init_item,
		[
			(store_trigger_param_1, ":trigger_param_1"),
			(store_trigger_param_2, ":trigger_param_2"),
			(call_script, "script_shield_item_set_banner", "tableau_heater_shield_1", ":trigger_param_1", ":trigger_param_2")
		])]
	, [fac_kingdom_3]],

	["sh_swa_kit_horseman", "Kite Shield", [("tableau_shield_kite_4", imodbits_none)], itp_type_shield|itp_merchandise|itp_wooden_parry, itcf_carry_kite_shield, 205, hit_points(165)|spd_rtng(103)|abundance(100)|weight(2.0)|shield_width(30)|shield_height(50)|body_armor(5), imodbits_shield, 
	[(ti_on_init_item,
		[
			(store_trigger_param_1, ":trigger_param_1"),
			(store_trigger_param_2, ":trigger_param_2"),
			(call_script, "script_shield_item_set_banner", "tableau_kite_shield_4", ":trigger_param_1", ":trigger_param_2")
		])]
	, [fac_kingdom_9, fac_kingdom_10]],

	["sh_swa_hea_horseman", "Heater Shield", [("tableau_shield_heater_2", imodbits_none)], itp_type_shield|itp_merchandise|itp_wooden_parry, itcf_carry_kite_shield, 229, hit_points(160)|spd_rtng(103)|abundance(100)|weight(2.0)|shield_width(30)|shield_height(50)|body_armor(10), imodbits_shield, 
	[(ti_on_init_item,
		[
			(store_trigger_param_1, ":trigger_param_1"),
			(store_trigger_param_2, ":trigger_param_2"),
			(call_script, "script_shield_item_set_banner", "tableau_heater_shield_2", ":trigger_param_1", ":trigger_param_2")
		])]
	, [fac_kingdom_9, fac_kingdom_10]],

	["sh_vae_kit_old", "Old Kite Shield", [("tableau_shield_kite_1", imodbits_none)], itp_type_shield|itp_merchandise|itp_wooden_parry, itcf_carry_kite_shield, 33, hit_points(165)|spd_rtng(96)|abundance(100)|weight(2.0)|shield_width(36)|shield_height(70)|body_armor(2), imodbits_shield, 
	[(ti_on_init_item,
		[
			(store_trigger_param_1, ":trigger_param_1"),
			(store_trigger_param_2, ":trigger_param_2"),
			(call_script, "script_shield_item_set_banner", "tableau_kite_shield_1", ":trigger_param_1", ":trigger_param_2")
		])]
	, [fac_kingdom_1, fac_kingdom_2, fac_kingdom_8]],

	["sh_vae_kit_plain", "Kite Shield", [("tableau_shield_kite_3", imodbits_none)], itp_type_shield|itp_merchandise|itp_wooden_parry, itcf_carry_kite_shield, 70, hit_points(215)|spd_rtng(93)|abundance(100)|weight(2.5)|shield_width(36)|shield_height(70)|body_armor(5), imodbits_shield, 
	[(ti_on_init_item,
		[
			(store_trigger_param_1, ":trigger_param_1"),
			(store_trigger_param_2, ":trigger_param_2"),
			(call_script, "script_shield_item_set_banner", "tableau_kite_shield_3", ":trigger_param_1", ":trigger_param_2")
		])]
	, [fac_kingdom_1, fac_kingdom_2, fac_kingdom_8]],

	["sh_vae_kit_heavy", "Kite Shield", [("tableau_shield_kite_2", imodbits_none)], itp_type_shield|itp_merchandise|itp_wooden_parry, itcf_carry_kite_shield, 156, hit_points(265)|spd_rtng(90)|abundance(100)|weight(3.0)|shield_width(36)|shield_height(70)|body_armor(10), imodbits_shield, 
	[(ti_on_init_item,
		[
			(store_trigger_param_1, ":trigger_param_1"),
			(store_trigger_param_2, ":trigger_param_2"),
			(call_script, "script_shield_item_set_banner", "tableau_kite_shield_2", ":trigger_param_1", ":trigger_param_2")
		])]
	, [fac_kingdom_1, fac_kingdom_2, fac_kingdom_8]],

	["sh_khe_rou_old", "Old Round Shield", [("tableau_shield_round_5", imodbits_none)], itp_type_shield|itp_merchandise|itp_wooden_parry, itcf_carry_round_shield, 40, hit_points(160)|spd_rtng(93)|abundance(60)|weight(4.0)|shield_width(50)|body_armor(2), imodbits_shield, 
	[(ti_on_init_item,
		[
			(store_trigger_param_1, ":trigger_param_1"),
			(store_trigger_param_2, ":trigger_param_2"),
			(call_script, "script_shield_item_set_banner", "tableau_round_shield_5", ":trigger_param_1", ":trigger_param_2")
		])]
	, [fac_kingdom_19]],

	["sh_khe_rou_plain", "Plain Round Shield", [("tableau_shield_round_3", imodbits_none)], itp_type_shield|itp_merchandise|itp_wooden_parry, itcf_carry_round_shield, 150, hit_points(180)|spd_rtng(90)|abundance(85)|weight(4.0)|shield_width(50)|body_armor(5), imodbits_shield, 
	[(ti_on_init_item,
		[
			(store_trigger_param_1, ":trigger_param_1"),
			(store_trigger_param_2, ":trigger_param_2"),
			(call_script, "script_shield_item_set_banner", "tableau_round_shield_3", ":trigger_param_1", ":trigger_param_2")
		])]
	, [fac_kingdom_19]],

	["sh_khe_rou_round", "Round Shield", [("tableau_shield_round_2", imodbits_none)], itp_type_shield|itp_merchandise|itp_wooden_parry, itcf_carry_round_shield, 200, hit_points(180)|spd_rtng(87)|abundance(70)|weight(4.0)|shield_width(50)|body_armor(10), imodbits_shield, 
	[(ti_on_init_item,
		[
			(store_trigger_param_1, ":trigger_param_1"),
			(store_trigger_param_2, ":trigger_param_2"),
			(call_script, "script_shield_item_set_banner", "tableau_round_shield_2", ":trigger_param_1", ":trigger_param_2")
		])]
	, [fac_kingdom_19]],

	["sh_khe_rou_heavy", "Heavy Round Shield", [("tableau_shield_round_1", imodbits_none)], itp_type_shield|itp_merchandise|itp_wooden_parry, itcf_carry_round_shield, 250, hit_points(200)|spd_rtng(84)|abundance(55)|weight(4.0)|shield_width(50)|body_armor(15), imodbits_shield, 
	[(ti_on_init_item,
		[
			(store_trigger_param_1, ":trigger_param_1"),
			(store_trigger_param_2, ":trigger_param_2"),
			(call_script, "script_shield_item_set_banner", "tableau_round_shield_1", ":trigger_param_1", ":trigger_param_2")
		])]
	, [fac_kingdom_19]],

	["sh_sar_rou_plain", "Plain Round Shield", [("tableau_shield_small_round_3", imodbits_none)], itp_type_shield|itp_merchandise|itp_wooden_parry, itcf_carry_round_shield, 100, hit_points(150)|spd_rtng(105)|abundance(85)|weight(3.0)|shield_width(40)|body_armor(2), imodbits_shield, 
	[(ti_on_init_item,
		[
			(store_trigger_param_1, ":trigger_param_1"),
			(store_trigger_param_2, ":trigger_param_2"),
			(call_script, "script_shield_item_set_banner", "tableau_small_round_shield_3", ":trigger_param_1", ":trigger_param_2")
		])]
	, [fac_kingdom_6, fac_kingdom_5, fac_kingdom_12, fac_kingdom_13, fac_kingdom_14, fac_kingdom_15, fac_kingdom_16, fac_kingdom_17, fac_kingdom_18]],

	["sh_sar_rou_round", "Round Shield", [("tableau_shield_small_round_1", imodbits_none)], itp_type_shield|itp_merchandise|itp_wooden_parry, itcf_carry_round_shield, 110, hit_points(180)|spd_rtng(103)|abundance(70)|weight(3.0)|shield_width(40)|body_armor(5), imodbits_shield, 
	[(ti_on_init_item,
		[
			(store_trigger_param_1, ":trigger_param_1"),
			(store_trigger_param_2, ":trigger_param_2"),
			(call_script, "script_shield_item_set_banner", "tableau_small_round_shield_1", ":trigger_param_1", ":trigger_param_2")
		])]
	, [fac_kingdom_6, fac_kingdom_5, fac_kingdom_12, fac_kingdom_13, fac_kingdom_14, fac_kingdom_15, fac_kingdom_16, fac_kingdom_17, fac_kingdom_18]],

	["sh_sar_rou_elite", "Heavy Round Shield", [("tableau_shield_small_round_2", imodbits_none)], itp_type_shield|itp_merchandise, itcf_carry_round_shield, 300, hit_points(180)|spd_rtng(100)|abundance(40)|weight(3.0)|shield_width(40)|body_armor(10), imodbits_shield, 
	[(ti_on_init_item,
		[
			(store_trigger_param_1, ":trigger_param_1"),
			(store_trigger_param_2, ":trigger_param_2"),
			(call_script, "script_shield_item_set_banner", "tableau_small_round_shield_2", ":trigger_param_1", ":trigger_param_2")
		])]
	, [fac_kingdom_6, fac_kingdom_5, fac_kingdom_12, fac_kingdom_13, fac_kingdom_14, fac_kingdom_15, fac_kingdom_16, fac_kingdom_17, fac_kingdom_18]],

	["sh_sar_rou_mamluk", "Elite Round Shield", [("tableau_shield_round_4", imodbits_none)], itp_type_shield|itp_merchandise, itcf_carry_round_shield, 450, hit_points(200)|spd_rtng(81)|abundance(40)|weight(4.0)|shield_width(50)|body_armor(15), imodbits_shield, 
	[(ti_on_init_item,
		[
			(store_trigger_param_1, ":trigger_param_1"),
			(store_trigger_param_2, ":trigger_param_2"),
			(call_script, "script_shield_item_set_banner", "tableau_round_shield_4", ":trigger_param_1", ":trigger_param_2")
		])]
	, [fac_kingdom_6, fac_kingdom_5, fac_kingdom_12, fac_kingdom_13, fac_kingdom_14, fac_kingdom_15, fac_kingdom_16, fac_kingdom_17, fac_kingdom_18]],

	["sh_pla_pav_plain", "Plain Pavise", [("tableau_shield_pavise_2", imodbits_none)], itp_type_shield|itp_merchandise|itp_wooden_parry|itp_cant_use_on_horseback, itcf_carry_board_shield, 200, hit_points(200)|spd_rtng(85)|abundance(85)|weight(7.0)|shield_width(43)|shield_height(100)|body_armor(15), imodbits_shield, 
	[(ti_on_init_item,
		[
			(store_trigger_param_1, ":trigger_param_1"),
			(store_trigger_param_2, ":trigger_param_2"),
			(call_script, "script_shield_item_set_banner", "tableau_pavise_shield_2", ":trigger_param_1", ":trigger_param_2")
		])]
	, [fac_kingdom_1, fac_kingdom_9, fac_kingdom_10]],

	["sh_pla_pav_heavy", "Heavy Pavise", [("tableau_shield_pavise_1", imodbits_none)], itp_type_shield|itp_merchandise|itp_wooden_parry|itp_cant_use_on_horseback, itcf_carry_board_shield, 350, hit_points(220)|spd_rtng(78)|abundance(70)|weight(7.0)|shield_width(43)|shield_height(100)|body_armor(15), imodbits_shield, 
	[(ti_on_init_item,
		[
			(store_trigger_param_1, ":trigger_param_1"),
			(store_trigger_param_2, ":trigger_param_2"),
			(call_script, "script_shield_item_set_banner", "tableau_pavise_shield_1", ":trigger_param_1", ":trigger_param_2")
		])]
	, [fac_kingdom_1, fac_kingdom_9, fac_kingdom_10]],

	["sh_nor_rou_small_b", "Round Shield", [("sh_nor_rou_small_b", imodbits_none)], itp_type_shield|itp_merchandise|itp_wooden_parry, itcf_carry_round_shield, 100, hit_points(150)|spd_rtng(87)|abundance(60)|weight(4.0)|shield_width(40)|body_armor(5), imodbits_shield, [], [fac_kingdom_11]],

	["sh_nor_rou_medium_b", "Round Shield", [("sh_nor_rou_medium_b", imodbits_none)], itp_type_shield|itp_merchandise|itp_wooden_parry, itcf_carry_round_shield, 100, hit_points(150)|spd_rtng(84)|abundance(85)|weight(4.0)|shield_width(50)|body_armor(5), imodbits_shield, [], [fac_kingdom_11]],

	["sh_nor_rou_large_b", "Round Shield", [("sh_nor_rou_large_b", imodbits_none)], itp_type_shield|itp_merchandise|itp_wooden_parry, itcf_carry_round_shield, 100, hit_points(150)|spd_rtng(81)|abundance(55)|weight(4.0)|shield_width(60)|body_armor(5), imodbits_shield, [], [fac_kingdom_11]],

	["sh_rho_rou_bandit_a", "Clansmans Shield", [("sh_rho_rou_bandit_a", imodbits_none)], itp_type_shield|itp_wooden_parry, itcf_carry_round_shield, 150, hit_points(150)|spd_rtng(100)|abundance(100)|weight(4.0)|shield_width(30)|body_armor(5), imodbits_shield, [], [fac_kingdom_5]],

	["heraldic_cuir_bouilli", "Heraldic Heavy Leather Armor", [("cuir_bouilli_a", imodbits_none)], itp_type_body_armor|itp_merchandise|itp_covers_legs|itp_doesnt_cover_hair|itp_can_penetrate_shield, 0, 8000, abundance(60)|weight(25.0)|leg_armor(15)|difficulty(8)|body_armor(45), imodbits_armor, 
	[(ti_on_init_item,
		[
			(store_trigger_param_1, ":trigger_param_1"),
			(store_trigger_param_2, ":trigger_param_2"),
			(call_script, "script_shield_item_set_banner", "tableau_heraldic_cuir_bouilli", ":trigger_param_1", ":trigger_param_2")
		])]
	, [fac_kingdom_19]],

	["cor_herald", "Heraldic Heavy Plate Armor", [("cor_herald", imodbits_none)], itp_type_body_armor|itp_merchandise|itp_covers_legs|itp_doesnt_cover_hair|itp_can_penetrate_shield, 0, 9000, abundance(40)|weight(25.0)|leg_armor(13)|difficulty(14)|body_armor(54), imodbits_plate, 
	[(ti_on_init_item,
		[
			(store_trigger_param_1, ":trigger_param_1"),
			(store_trigger_param_2, ":trigger_param_2"),
			(call_script, "script_shield_item_set_banner", "tableau_cor_herald", ":trigger_param_1", ":trigger_param_2")
		])]
	, [fac_kingdom_10]],

	["heraldic_cozur_1", "Heraldic Chain Mail Hauberk", [("fi_chain_mail_hauberk_heraldic_3", imodbits_none)], itp_type_body_armor|itp_merchandise|itp_covers_legs|itp_doesnt_cover_hair|itp_can_penetrate_shield, 0, 4500, abundance(40)|weight(20.0)|leg_armor(14)|difficulty(12)|body_armor(40), imodbits_armor, 
	[(ti_on_init_item,
		[
			(store_trigger_param_1, ":trigger_param_1"),
			(store_trigger_param_2, ":trigger_param_2"),
			(call_script, "script_shield_item_set_banner", "tableau_heraldic_armor_a", ":trigger_param_1", ":trigger_param_2")
		])]
	, [fac_kingdom_8]],

	["heraldic_cozur_2", "Heraldic Chain Mail Hauberk", [("sellsword_armor_1", imodbits_none)], itp_type_body_armor|itp_merchandise|itp_covers_legs|itp_doesnt_cover_hair|itp_can_penetrate_shield, 0, 4500, abundance(40)|weight(20.0)|leg_armor(14)|difficulty(12)|body_armor(40), imodbits_armor, 
	[(ti_on_init_item,
		[
			(store_trigger_param_1, ":trigger_param_1"),
			(store_trigger_param_2, ":trigger_param_2"),
			(call_script, "script_shield_item_set_banner", "tableau_heraldic_armor_d", ":trigger_param_1", ":trigger_param_2")
		])]
	, [fac_kingdom_1, fac_kingdom_8]],

	["brigandine_b_heraldic", "Heraldic Chain Mail Hauberk", [("sellsword_armor_2", imodbits_none)], itp_type_body_armor|itp_merchandise|itp_covers_legs|itp_doesnt_cover_hair|itp_can_penetrate_shield, 0, 4500, abundance(50)|weight(25.0)|leg_armor(14)|difficulty(14)|body_armor(40), imodbits_armor, 
	[(ti_on_init_item,
		[
			(store_trigger_param_1, ":trigger_param_1"),
			(store_trigger_param_2, ":trigger_param_2"),
			(call_script, "script_shield_item_set_banner", "tableau_brigandine_b_heraldic_new", ":trigger_param_1", ":trigger_param_2")
		])]
	, [fac_kingdom_9]],

	["heraldic_tunic_new", "Heraldic Chain Mail Hauberk", [("sellsword_armor_4", imodbits_none)], itp_type_body_armor|itp_merchandise|itp_covers_legs|itp_doesnt_cover_hair|itp_can_penetrate_shield, 0, 4500, abundance(50)|weight(25.0)|leg_armor(14)|difficulty(14)|body_armor(40), imodbits_armor, 
	[(ti_on_init_item,
		[
			(store_trigger_param_1, ":trigger_param_1"),
			(store_trigger_param_2, ":trigger_param_2"),
			(call_script, "script_shield_item_set_banner", "tableau_heraldic_short_tunic_new", ":trigger_param_1", ":trigger_param_2")
		])]
	, [fac_kingdom_1, fac_kingdom_2, fac_kingdom_3, fac_kingdom_8, fac_kingdom_9, fac_kingdom_10]],

	["frenchpepperpot2", "Top Helmet with Faceplate", [("frenchpepperpot2", imodbits_none)], itp_type_head_armor|itp_merchandise|itp_fit_to_head|itp_offset_lance|itp_covers_beard, 0, 1800, abundance(10)|weight(4.0)|difficulty(12)|head_armor(37), imodbits_plate, [], [fac_kingdom_1, fac_kingdom_8]],

	["frenchpepperpot3", "Top Helmet with Faceplate", [("frenchpepperpot3", imodbits_none)], itp_type_head_armor|itp_merchandise|itp_fit_to_head|itp_offset_lance|itp_covers_beard, 0, 1800, abundance(10)|weight(4.0)|difficulty(12)|head_armor(37), imodbits_plate, [], [fac_kingdom_1, fac_kingdom_8]],

	["munitionshelm2", "Helmet with Faceplate", [("munitionshelm2", imodbits_none)], itp_type_head_armor|itp_merchandise|itp_fit_to_head|itp_offset_lance|itp_covers_beard, 0, 1800, abundance(10)|weight(4.0)|difficulty(12)|head_armor(37), imodbits_plate, [], [fac_kingdom_1, fac_kingdom_8]],

	["conichelm", "Conical Helmet", [("conichelm", imodbits_none)], itp_type_head_armor|itp_merchandise|itp_fit_to_head|itp_offset_lance|itp_covers_beard, 0, 1100, abundance(10)|weight(4.0)|difficulty(12)|head_armor(33), imodbits_plate, [], [fac_kingdom_12, fac_kingdom_17]],

	["pepperpothelm1", "Top Helmet with Faceplate", [("pepperpothelm1", imodbits_none)], itp_type_head_armor|itp_merchandise|itp_fit_to_head|itp_offset_lance|itp_covers_beard, 0, 1800, abundance(10)|weight(4.0)|difficulty(12)|head_armor(37), imodbits_plate, [], [fac_kingdom_1, fac_kingdom_8]],

	["normanpepperpot", "Conical Helmet with Faceplate", [("normanpepperpot", imodbits_none)], itp_type_head_armor|itp_merchandise|itp_fit_to_head|itp_offset_lance|itp_covers_beard, 0, 1800, abundance(10)|weight(4.0)|difficulty(12)|head_armor(37), imodbits_plate, [], [fac_kingdom_1, fac_kingdom_8]],

	["munitionshelm1", "Helmet with Faceplate", [("munitionshelm1", imodbits_none)], itp_type_head_armor|itp_merchandise|itp_fit_to_head|itp_offset_lance|itp_covers_beard, 0, 1800, abundance(10)|weight(4.0)|difficulty(12)|head_armor(37), imodbits_plate, [], [fac_kingdom_1, fac_kingdom_8]],

	["crownedhelm", "Nasal Helmet with Crown", [("crownedhelm", imodbits_none)], itp_type_head_armor|itp_fit_to_head|itp_offset_lance, 0, 1300, abundance(50)|weight(4.0)|difficulty(12)|head_armor(37), imodbits_plate, [], [fac_kingdom_3]],

	["frenchpepperpot", "Top Helmet with Faceplate", [("frenchpepperpot", imodbits_none)], itp_type_head_armor|itp_merchandise|itp_fit_to_head|itp_offset_lance|itp_covers_beard, 0, 1800, abundance(10)|weight(4.0)|difficulty(12)|head_armor(37), imodbits_plate, [], [fac_kingdom_1, fac_kingdom_8]],

	["flattophelmet", "Top Helmet", [("flattophelmet", imodbits_none)], itp_type_head_armor|itp_merchandise|itp_fit_to_head|itp_offset_lance|itp_covers_beard, 0, 1800, abundance(10)|weight(4.0)|difficulty(12)|head_armor(37), imodbits_plate, [], [fac_kingdom_8]],

	["chionite_hat_b", "Woolen Cap", [("chionite_hat_b", imodbits_none)], itp_type_head_armor|itp_merchandise|itp_fit_to_head|itp_offset_lance, 0, 30, abundance(50)|weight(1.0)|head_armor(3), imodbits_none, [], [fac_kingdom_1, fac_kingdom_3, fac_kingdom_5, fac_kingdom_8]],

	["clansman_cloth_1", "Clansmans Tunic", [("Clansman_Cloth_1", imodbits_none)], itp_type_body_armor|itp_covers_legs|itp_doesnt_cover_hair|itp_can_penetrate_shield, 0, 100, abundance(55)|weight(5.0)|leg_armor(5)|body_armor(10), imodbits_cloth, [], [fac_kingdom_1, fac_kingdom_8, fac_kingdom_9, fac_kingdom_10, fac_kingdom_20]],

	["clansman_cloth_2", "Clansmans Tunic", [("Clansman_Cloth_2", imodbits_none)], itp_type_body_armor|itp_covers_legs|itp_doesnt_cover_hair|itp_can_penetrate_shield, 0, 100, abundance(55)|weight(5.0)|leg_armor(5)|body_armor(10), imodbits_cloth, [], [fac_kingdom_1, fac_kingdom_8, fac_kingdom_9, fac_kingdom_10, fac_kingdom_20]],

	["clansman_cloth_3", "Clansmans Tunic", [("Clansman_Cloth_3", imodbits_none)], itp_type_body_armor|itp_covers_legs|itp_doesnt_cover_hair|itp_can_penetrate_shield, 0, 100, abundance(55)|weight(5.0)|leg_armor(5)|body_armor(10), imodbits_cloth, [], [fac_kingdom_1, fac_kingdom_8, fac_kingdom_9, fac_kingdom_10, fac_kingdom_20]],

	["clansman_lamellar_1", "Clansmans Lamellar Armor", [("Clansman_Lamellar_1", imodbits_none)], itp_type_body_armor|itp_covers_legs|itp_doesnt_cover_hair|itp_can_penetrate_shield, 0, 100, abundance(55)|weight(15.0)|leg_armor(5)|body_armor(25), imodbits_cloth, [], [fac_kingdom_1, fac_kingdom_8, fac_kingdom_9, fac_kingdom_10, fac_kingdom_20]],

	["clansman_lamellar_2", "Clansmans Lamellar Armor", [("Clansman_Lamellar_2", imodbits_none)], itp_type_body_armor|itp_covers_legs|itp_doesnt_cover_hair|itp_can_penetrate_shield, 0, 100, abundance(55)|weight(15.0)|leg_armor(5)|body_armor(25), imodbits_cloth, [], [fac_kingdom_1, fac_kingdom_8, fac_kingdom_9, fac_kingdom_10, fac_kingdom_20]],

	["clansman_fur_armor_1", "Clansmans Heavy Fur Armor", [("Clansman_Fur_Armor_1", imodbits_none)], itp_type_body_armor|itp_covers_legs|itp_doesnt_cover_hair|itp_can_penetrate_shield, 0, 100, abundance(55)|weight(20.0)|leg_armor(4)|body_armor(26), imodbits_cloth, [], [fac_kingdom_1, fac_kingdom_8, fac_kingdom_9, fac_kingdom_10, fac_kingdom_20]],

	["clansman_fur_armor_2", "Clansmans Heavy Fur Armor", [("Clansman_Fur_Armor_2", imodbits_none)], itp_type_body_armor|itp_covers_legs|itp_doesnt_cover_hair|itp_can_penetrate_shield, 0, 100, abundance(55)|weight(20.0)|leg_armor(4)|body_armor(26), imodbits_cloth, [], [fac_kingdom_1, fac_kingdom_8, fac_kingdom_9, fac_kingdom_10, fac_kingdom_20]],

	["bigod_spurs", "Plate Boots", [("full_plate_boots_5", imodbits_none)], itp_type_foot_armor|itp_attach_armature|itp_attachment_mask|itp_merchandise, 0, 2000, abundance(70)|weight(3.0)|leg_armor(40)|difficulty(12), imodbits_armor, [], [fac_kingdom_1, fac_kingdom_8, fac_kingdom_9, fac_kingdom_10, fac_kingdom_20]],

	["brienne_spurs", "Plate Boots", [("full_plate_boots_6", imodbits_none)], itp_type_foot_armor|itp_attach_armature|itp_attachment_mask|itp_merchandise, 0, 2000, abundance(70)|weight(4.0)|leg_armor(40)|difficulty(12), imodbits_armor, [], [fac_kingdom_1, fac_kingdom_8, fac_kingdom_9, fac_kingdom_10, fac_kingdom_20]],

	["henryv_helm", "Aegon Targaryens Crowned Great Helmet", [("henryv_helm", imodbits_none)], itp_type_head_armor|itp_covers_beard, 0, 1500, abundance(40)|weight(6.0)|difficulty(14)|head_armor(45), imodbits_none, [], [fac_kingdom_1]],

	["longshanks_helm", "Crowned Great Helmet", [("longshanks_helm", imodbits_none)], itp_type_head_armor|itp_covers_beard, 0, 1500, abundance(40)|weight(6.0)|difficulty(14)|head_armor(45), imodbits_none, [], [fac_kingdom_1]],

	["byz_helmet_a", "Nasal Helmet", [("fi_nasal_helmet_2", imodbits_none)], itp_type_head_armor|itp_merchandise, 0, 1100, abundance(20)|weight(4.0)|difficulty(12)|head_armor(29), imodbits_armor],

	["archer_a", "Peasants Tunic", [("archer_a", imodbits_none)], itp_type_body_armor|itp_merchandise|itp_covers_legs|itp_doesnt_cover_hair|itp_can_penetrate_shield|itp_civilian|itp_next_item_as_melee, 0, 50, abundance(55)|weight(2.0)|leg_armor(1)|body_armor(5), imodbits_cloth],

	["militia_tunic_a", "Peasants Tunic", [("militia_tunic_a", imodbits_none)], itp_type_body_armor|itp_merchandise|itp_covers_legs|itp_doesnt_cover_hair|itp_can_penetrate_shield, 0, 50, abundance(55)|weight(2.0)|leg_armor(1)|body_armor(5), imodbits_cloth],

	["peasant_b", "Peasants Tunic", [("peasant_b", imodbits_none)], itp_type_body_armor|itp_merchandise|itp_covers_legs|itp_doesnt_cover_hair|itp_can_penetrate_shield, 0, 50, abundance(55)|weight(2.0)|leg_armor(1)|body_armor(5), imodbits_cloth],

	["peasant_c", "Peasants Tunic", [("peasant_c", imodbits_none)], itp_type_body_armor|itp_merchandise|itp_covers_legs|itp_doesnt_cover_hair|itp_can_penetrate_shield, 0, 50, abundance(55)|weight(2.0)|leg_armor(1)|body_armor(5), imodbits_cloth],

	["peasant_man_b", "Peasants Tunic", [("peasant_man_b", imodbits_none)], itp_type_body_armor|itp_merchandise|itp_covers_legs|itp_doesnt_cover_hair|itp_can_penetrate_shield, 0, 50, abundance(55)|weight(2.0)|leg_armor(1)|body_armor(5), imodbits_cloth],

	["peasant_outfit_a", "Peasants Tunic", [("peasant_outfit_a", imodbits_none)], itp_type_body_armor|itp_merchandise|itp_covers_legs|itp_doesnt_cover_hair|itp_can_penetrate_shield, 0, 50, abundance(55)|weight(2.0)|leg_armor(1)|body_armor(5), imodbits_cloth],

	["flattop_a", "Top Helmet", [("fi_top_helmet", imodbits_none)], itp_type_head_armor|itp_merchandise|itp_fit_to_head|itp_offset_lance, 0, 1500, abundance(10)|weight(4.0)|difficulty(12)|head_armor(35), imodbits_armor, [], [fac_kingdom_3, fac_kingdom_5]],

	["varangian_helmet", "Cataphract Helmet", [("fi_cataphract_helmet_1", imodbits_none)], itp_type_head_armor|itp_merchandise|itp_fit_to_head|itp_offset_lance|itp_covers_beard, 0, 2000, abundance(10)|weight(4.0)|difficulty(12)|head_armor(37), imodbits_plate, [], [fac_kingdom_12, fac_kingdom_13, fac_kingdom_14, fac_kingdom_15, fac_kingdom_16, fac_kingdom_17, fac_kingdom_5, fac_kingdom_18]],

	["andalusianskirmisher_armor", "Heavy Leather Jerkin", [("cozur_leather_armor_b", imodbits_none)], itp_type_body_armor|itp_merchandise|itp_covers_legs|itp_doesnt_cover_hair|itp_can_penetrate_shield, 0, 400, abundance(55)|weight(15.0)|leg_armor(15)|body_armor(25), imodbits_cloth],

	["gaelic_mail_shirt_a", "Chain Mail Hauberk", [("gaelic_mail_shirt_a", imodbits_none)], itp_type_body_armor|itp_covers_legs|itp_doesnt_cover_hair|itp_can_penetrate_shield, 0, 1500, abundance(20)|weight(15.0)|leg_armor(15)|difficulty(12)|body_armor(35), imodbits_armor, [], [fac_kingdom_19]],

	["galloglass_padded", "Chain Mail Hauberk", [("galloglass_padded", imodbits_none)], itp_type_body_armor|itp_merchandise|itp_covers_legs|itp_doesnt_cover_hair|itp_can_penetrate_shield, 0, 2500, abundance(20)|weight(15.0)|leg_armor(15)|difficulty(12)|body_armor(35), imodbits_armor, [], [fac_kingdom_1, fac_kingdom_3, fac_kingdom_8]],

	["lit_segmented_helmet", "Great Helmet", [("fi_greathelmet_2", imodbits_none)], itp_type_head_armor|itp_merchandise|itp_fit_to_head|itp_offset_lance|itp_covers_beard, 0, 2000, abundance(10)|weight(4.0)|difficulty(14)|head_armor(45), imodbits_plate, [], [fac_kingdom_1, fac_kingdom_8]],

	["liv_tunic_a", "Faith Militant Tunic", [("liv_tunic_a", imodbits_none)], itp_type_body_armor|itp_covers_legs|itp_doesnt_cover_hair|itp_can_penetrate_shield, 0, 200, abundance(55)|weight(5.0)|leg_armor(5)|body_armor(8), imodbits_cloth, [], [fac_kingdom_1, fac_kingdom_3, fac_kingdom_5, fac_kingdom_8]],

	["teu_postulant", "Chain Mail Hauberk", [("teu_postulant", imodbits_none)], itp_type_body_armor|itp_covers_legs|itp_doesnt_cover_hair|itp_can_penetrate_shield, 0, 2800, abundance(20)|weight(15.0)|leg_armor(15)|difficulty(11)|body_armor(25), imodbits_armor, [], [fac_kingdom_5]],

	["mackie_dagger", "Valyrian Dagger", [("mackie_dagger", imodbits_none), ("mackie_dagger_scabbard", ixmesh_carry)], itp_type_one_handed_wpn|itp_no_parry|itp_primary|itp_secondary, itcf_carry_dagger_front_left|itcf_show_holster_when_drawn|itc_dagger, 5000, thrust_damage(25, pierce)|hit_points(21504)|spd_rtng(108)|abundance(60)|weight(1.0)|swing_damage(21, cut)|weapon_length(40), imodbits_none, [], [fac_kingdom_11, fac_kingdom_19]],

	["mackie_bearded_axe", "Two-Handed Axe", [("mackie_bearded_axe", imodbits_none)], itp_type_two_handed_wpn|itp_merchandise|itp_wooden_parry|itp_two_handed|itp_primary|itp_covers_legs|itp_doesnt_cover_hair|itp_can_penetrate_shield|itp_bonus_against_shield|itp_cant_use_on_horseback, itcf_carry_axe_back|itc_nodachi, 800, thrust_damage(0, pierce)|hit_points(37888)|spd_rtng(85)|abundance(5)|weight(6.0)|swing_damage(37, cut)|difficulty(12)|weapon_length(100), imodbits_axe|imodbits_mace, [], [fac_kingdom_11, fac_kingdom_19]],

	["mackie_beefsplitter01", "Peasants Beefsplitter", [("mackie_beefsplitter01", imodbits_none)], itp_type_two_handed_wpn|itp_wooden_parry|itp_two_handed|itp_primary|itp_bonus_against_shield|itp_cant_use_on_horseback, itcf_carry_axe_back|itc_nodachi, 100, thrust_damage(0, pierce)|hit_points(25600)|spd_rtng(65)|abundance(10)|weight(10.0)|swing_damage(25, cut)|difficulty(12)|weapon_length(74), imodbits_axe|imodbits_mace, [], [fac_kingdom_11, fac_kingdom_19]],

	["mackie_beefsplitter02", "Peasants Beefsplitter", [("mackie_beefsplitter02", imodbits_none)], itp_type_two_handed_wpn|itp_wooden_parry|itp_two_handed|itp_primary|itp_bonus_against_shield|itp_cant_use_on_horseback, itcf_carry_axe_back|itc_nodachi, 100, thrust_damage(0, pierce)|hit_points(26624)|spd_rtng(65)|abundance(10)|weight(10.0)|swing_damage(26, cut)|difficulty(12)|weapon_length(74), imodbits_axe|imodbits_mace, [], [fac_kingdom_11, fac_kingdom_19]],

	["mackie_celtic_axe", "Two-Handed Axe", [("mackie_celtic_axe", imodbits_none)], itp_type_two_handed_wpn|itp_merchandise|itp_wooden_parry|itp_two_handed|itp_primary|itp_covers_legs|itp_doesnt_cover_hair|itp_can_penetrate_shield|itp_bonus_against_shield|itp_cant_use_on_horseback, itcf_carry_axe_back|itc_nodachi, 1400, thrust_damage(0, pierce)|hit_points(45056)|spd_rtng(85)|abundance(10)|weight(6.0)|swing_damage(44, cut)|difficulty(12)|weapon_length(96), imodbits_none, [], [fac_kingdom_11, fac_kingdom_19]],

	["mackie_tomahawk", "One-Handed Axe", [("mackie_tomahawk", imodbits_none)], itp_type_one_handed_wpn|itp_merchandise|itp_wooden_parry|itp_primary|itp_secondary, itcf_carry_axe_left_hip|itc_scimitar, 500, thrust_damage(0, pierce)|hit_points(30720)|spd_rtng(100)|abundance(5)|weight(2.0)|swing_damage(30, cut)|difficulty(8)|weapon_length(61), imodbits_axe|imodbits_mace, [], [fac_kingdom_11, fac_kingdom_19]],

	["mackie_varangian_axe", "One-Handed Axe", [("mackie_varangian_axe", imodbits_none)], itp_type_one_handed_wpn|itp_merchandise|itp_wooden_parry|itp_primary|itp_secondary, itcf_carry_axe_left_hip|itc_scimitar, 500, thrust_damage(0, pierce)|hit_points(30720)|spd_rtng(100)|abundance(50)|weight(2.0)|swing_damage(30, cut)|difficulty(8)|weapon_length(71), imodbits_axe|imodbits_mace, [], [fac_kingdom_12, fac_kingdom_18]],

	["mackie_voulge", "Voulge", [("mackie_voulge", imodbits_none)], itp_type_polearm|itp_merchandise|itp_wooden_parry|itp_two_handed|itp_primary|itp_bonus_against_shield|itp_cant_use_on_horseback|itp_crush_through|itp_can_knock_down, itcf_carry_spear|itc_staff, 1000, thrust_damage(32, pierce)|hit_points(45056)|spd_rtng(80)|abundance(10)|weight(6.0)|swing_damage(44, cut)|difficulty(12)|weapon_length(170), imodbits_polearm, [], [fac_kingdom_2, fac_kingdom_3, fac_kingdom_5]],

	["mackie_godenak", "War Cleaver", [("mackie_godenak", imodbits_none)], itp_type_two_handed_wpn|itp_merchandise|itp_two_handed|itp_primary|itp_bonus_against_shield|itp_cant_use_on_horseback|itp_crush_through, itcf_carry_sword_back|itc_nodachi, 1200, hit_points(43008)|spd_rtng(85)|abundance(10)|weight(6.0)|swing_damage(42, cut)|difficulty(13)|weapon_length(74), imodbits_sword_high, [], [fac_kingdom_2]],

	["mackie_morning_star_long", "Long Hafted Spiked Mace", [("mackie_morning_star_long", imodbits_none)], itp_type_two_handed_wpn|itp_merchandise|itp_wooden_parry|itp_two_handed|itp_primary|itp_covers_legs|itp_doesnt_cover_hair|itp_can_penetrate_shield|itp_bonus_against_shield|itp_cant_use_on_horseback|itp_crush_through|itp_can_knock_down, itcf_carry_axe_back|itc_nodachi, 1000, thrust_damage(0, pierce)|hit_points(40960)|spd_rtng(85)|abundance(5)|weight(6.0)|swing_damage(40, pierce)|difficulty(12)|weapon_length(100), imodbits_axe|imodbits_mace, [], [fac_kingdom_1]],

	["coif", "Mail Coif", [("fi_chain_mail_coif", imodbits_none)], itp_type_head_armor|itp_merchandise|itp_fit_to_head|itp_offset_lance, 0, 1000, abundance(50)|weight(4.0)|difficulty(10)|head_armor(33), imodbits_plate],

	["kettlehatfacebyrnie", "Kettle Hat", [("fi_kettle_hat_1", imodbits_none)], itp_type_head_armor|itp_merchandise|itp_fit_to_head|itp_offset_lance, 0, 1300, abundance(10)|weight(4.0)|difficulty(10)|head_armor(35), imodbits_plate, [], [fac_kingdom_1, fac_kingdom_3, fac_kingdom_8, fac_kingdom_9, fac_kingdom_10]],

	["kettlehat2", "Kettle Hat", [("fi_kettle_hat_3", imodbits_none)], itp_type_head_armor|itp_merchandise|itp_fit_to_head|itp_offset_lance, 0, 1300, abundance(10)|weight(4.0)|difficulty(10)|head_armor(35), imodbits_plate, [], [fac_kingdom_1, fac_kingdom_3, fac_kingdom_8, fac_kingdom_9, fac_kingdom_10]],

	["col1_kettlehat1", "Bascinet", [("fi_bascinet_1", imodbits_none)], itp_type_head_armor|itp_fit_to_head|itp_offset_lance|itp_covers_beard, 0, 1300, abundance(10)|weight(4.0)|difficulty(10)|head_armor(35), imodbits_plate, [], [fac_kingdom_1, fac_kingdom_3, fac_kingdom_8, fac_kingdom_9, fac_kingdom_10]],

	["col1_kettlehat2", "Bascinet", [("fi_bascinet_2", imodbits_none)], itp_type_head_armor|itp_fit_to_head|itp_offset_lance|itp_covers_beard, 0, 1300, abundance(10)|weight(4.0)|difficulty(10)|head_armor(35), imodbits_plate, [], [fac_kingdom_1, fac_kingdom_3, fac_kingdom_8, fac_kingdom_9, fac_kingdom_10]],

	["byzantion", "Pointy Kettle Hat", [("byzantion", imodbits_none)], itp_type_head_armor|itp_merchandise|itp_fit_to_head|itp_offset_lance|itp_covers_beard, 0, 1300, abundance(10)|weight(4.0)|difficulty(10)|head_armor(35), imodbits_plate, [], [fac_kingdom_4, fac_kingdom_12, fac_kingdom_17, fac_kingdom_5, fac_kingdom_18]],

	["col1_byzantion", "Pointy Kettle Hat", [("col1_byzantion", imodbits_none)], itp_type_head_armor|itp_merchandise|itp_fit_to_head|itp_offset_lance|itp_covers_beard, 0, 1300, abundance(20)|weight(4.0)|difficulty(10)|head_armor(35), imodbits_plate, [], [fac_kingdom_4, fac_kingdom_12, fac_kingdom_17, fac_kingdom_5, fac_kingdom_18]],

	["aketon", "Aketon", [("aketon", imodbits_none)], itp_type_body_armor|itp_covers_legs|itp_doesnt_cover_hair|itp_can_penetrate_shield, 0, 200, abundance(55)|weight(5.0)|leg_armor(4)|body_armor(16), imodbits_cloth],

	["nomad_cap_b_new", "Leather Cap", [("nomad_cap_b_new", imodbits_none)], itp_type_head_armor|itp_merchandise, 0, 18, abundance(60)|weight(1.0)|head_armor(9), imodbits_cloth, [], [fac_kingdom_1, fac_kingdom_2, fac_kingdom_3, fac_kingdom_5, fac_kingdom_8, fac_kingdom_9, fac_kingdom_10, fac_kingdom_11]],

	["black_khergit_armor_new", "Fur Armor", [("black_khergit_armor_new", imodbits_none)], itp_type_body_armor|itp_covers_legs|itp_doesnt_cover_hair|itp_can_penetrate_shield, 0, 150, abundance(60)|weight(8.0)|leg_armor(5)|body_armor(20), imodbits_cloth, [], [fac_kingdom_2]],

	["black_nomad_armor_new", "Fur Armor", [("black_nomad_armor_new", imodbits_none)], itp_type_body_armor|itp_covers_legs|itp_doesnt_cover_hair|itp_can_penetrate_shield, 0, 150, abundance(60)|weight(8.0)|leg_armor(5)|body_armor(20), imodbits_cloth, [], [fac_kingdom_2]],

	["brass_shield2", "Round Bronze Shield", [("brass_shield2", imodbits_none)], itp_type_shield, itcf_carry_round_shield, 500, hit_points(250)|spd_rtng(90)|abundance(60)|weight(4.0)|shield_width(65)|difficulty(2)|body_armor(15), imodbits_shield, [], [fac_kingdom_16]],

	["dec_steel_shield", "Round Silver Shield", [("dec_steel_shield", imodbits_none)], itp_type_shield|itp_merchandise, itcf_carry_round_shield, 500, hit_points(250)|spd_rtng(90)|abundance(60)|weight(4.0)|shield_width(57)|difficulty(2)|body_armor(15), imodbits_shield, [], [fac_kingdom_16]],

	["brass_mamluk_armor", "Heavy Plate Armor", [("ar_sar_t7_fullplate_a", imodbits_none)], itp_type_body_armor|itp_covers_legs|itp_doesnt_cover_hair|itp_can_penetrate_shield, 0, 6000, abundance(20)|weight(25.0)|leg_armor(18)|difficulty(14)|body_armor(54), imodbits_plate, [], [fac_kingdom_13, fac_kingdom_14, fac_kingdom_15, fac_kingdom_16]],

	["mercenary_lamellar", "Expensive Lamellar Armor", [("mercenary_lamellar", imodbits_none)], itp_type_body_armor|itp_covers_legs|itp_doesnt_cover_hair|itp_can_penetrate_shield, 0, 4000, abundance(20)|weight(16.0)|leg_armor(4)|difficulty(12)|body_armor(37), imodbits_armor, [], [fac_kingdom_11, fac_kingdom_19]],

	["mercenary_surcoat", "Surcoat over Mail", [("mercenary_surcoat", imodbits_none)], itp_type_body_armor|itp_covers_legs|itp_doesnt_cover_hair|itp_can_penetrate_shield, 0, 5000, abundance(20)|weight(16.0)|leg_armor(15)|difficulty(12)|body_armor(44), imodbits_armor, [], [fac_kingdom_11, fac_kingdom_19]],

	["mercenary_hauberk", "Chain Mail Hauberk", [("mercenary_hauberk", imodbits_none)], itp_type_body_armor|itp_covers_legs|itp_doesnt_cover_hair|itp_can_penetrate_shield, 0, 4000, abundance(20)|weight(16.0)|leg_armor(4)|difficulty(12)|body_armor(37), imodbits_armor, [], [fac_kingdom_11, fac_kingdom_19]],

	["surcoat_braavosi", "Surcoat over Mail", [("surcoat_braavosi", imodbits_none)], itp_type_body_armor|itp_merchandise|itp_covers_legs|itp_doesnt_cover_hair|itp_can_penetrate_shield, 0, 5000, abundance(100)|weight(18.0)|leg_armor(14)|difficulty(12)|body_armor(40), imodbits_armor, [], [fac_kingdom_4]],

	["surcoat_lorathi", "Surcoat over Mail", [("surcoat_lorathi", imodbits_none)], itp_type_body_armor|itp_covers_legs|itp_doesnt_cover_hair|itp_can_penetrate_shield, 0, 5000, abundance(100)|weight(18.0)|leg_armor(14)|difficulty(12)|body_armor(40), imodbits_armor, [], [fac_kingdom_18]],

	["surcoat_tyrosh", "Surcoat over Mail", [("surcoat_tyrosh", imodbits_none)], itp_type_body_armor|itp_covers_legs|itp_doesnt_cover_hair|itp_can_penetrate_shield, 0, 5000, abundance(100)|weight(18.0)|leg_armor(14)|difficulty(12)|body_armor(40), imodbits_armor, [], [fac_kingdom_4]],

	["surcoat_lys", "Surcoat over Mail", [("surcoat_lys", imodbits_none)], itp_type_body_armor|itp_covers_legs|itp_doesnt_cover_hair|itp_can_penetrate_shield, 0, 5000, abundance(100)|weight(18.0)|leg_armor(14)|difficulty(12)|body_armor(40), imodbits_armor, [], [fac_kingdom_15]],

	["militia_tunic_a2", "Peasants Tunic with Cloak", [("militia_tunic_a2", imodbits_none)], itp_type_body_armor|itp_merchandise|itp_covers_legs|itp_doesnt_cover_hair|itp_can_penetrate_shield|itp_civilian|itp_next_item_as_melee, 0, 10, abundance(55)|weight(2.0)|leg_armor(1)|body_armor(4), imodbits_none],

	["peasant_b2", "Peasants Tunic with Cloak", [("peasant_b2", imodbits_none)], itp_type_body_armor|itp_merchandise|itp_covers_legs|itp_doesnt_cover_hair|itp_can_penetrate_shield|itp_civilian|itp_next_item_as_melee, 0, 10, abundance(55)|weight(2.0)|leg_armor(1)|body_armor(4), imodbits_none],

	["peasant_c2", "Peasants Tunic with Cloak", [("peasant_c2", imodbits_none)], itp_type_body_armor|itp_merchandise|itp_covers_legs|itp_doesnt_cover_hair|itp_can_penetrate_shield|itp_civilian|itp_next_item_as_melee, 0, 10, abundance(55)|weight(2.0)|leg_armor(1)|body_armor(4), imodbits_none],

	["peasant_outfit_a2", "Peasants Tunic with Cloak", [("peasant_outfit_a2", imodbits_none)], itp_type_body_armor|itp_merchandise|itp_covers_legs|itp_doesnt_cover_hair|itp_can_penetrate_shield|itp_civilian|itp_next_item_as_melee, 0, 10, abundance(55)|weight(2.0)|leg_armor(1)|body_armor(4), imodbits_none],

	["norman_short_hauberk", "Chain Mail Hauberk", [("norman_short_hauberk", imodbits_none)], itp_type_body_armor|itp_merchandise|itp_covers_legs|itp_doesnt_cover_hair|itp_can_penetrate_shield, 0, 4000, abundance(20)|weight(15.0)|leg_armor(8)|difficulty(12)|body_armor(37), imodbits_armor, [], [fac_kingdom_11, fac_kingdom_3, fac_kingdom_8, fac_kingdom_9, fac_kingdom_10, fac_kingdom_11, fac_kingdom_19]],

	["rough_padded_leather", "Padded Tunic", [("rough_padded_leather", imodbits_none)], itp_type_body_armor|itp_merchandise|itp_covers_legs|itp_doesnt_cover_hair|itp_can_penetrate_shield, 0, 200, abundance(55)|weight(2.0)|leg_armor(1)|body_armor(15), imodbits_cloth],

	["surcoat_over_mail_swadian_f", "Leather Surcoat over Mail", [("surcoat_over_mail_swadian_f", imodbits_none)], itp_type_body_armor|itp_merchandise|itp_covers_legs|itp_doesnt_cover_hair|itp_can_penetrate_shield, 0, 4500, abundance(60)|weight(18.0)|leg_armor(15)|difficulty(12)|body_armor(44), imodbits_armor, [], [fac_kingdom_1, fac_kingdom_3, fac_kingdom_5, fac_kingdom_8, fac_kingdom_9, fac_kingdom_10]],

	["rathos_fluted_helmet", "Fluted Helmet", [("rathos_fluted_helmet", imodbits_none)], itp_type_head_armor|itp_merchandise|itp_fit_to_head|itp_offset_lance, 0, 800, abundance(20)|weight(4.0)|difficulty(12)|head_armor(30), imodbits_armor, [], [fac_kingdom_1, fac_kingdom_3, fac_kingdom_5, fac_kingdom_8, fac_kingdom_9, fac_kingdom_10]],

	["inv_nikolskoe_helm", "Cataphract Helmet", [("inv_nikolskoe_helm", imodbits_none)], itp_type_head_armor|itp_merchandise|itp_fit_to_head|itp_offset_lance|itp_covers_beard, 0, 2000, abundance(20)|weight(4.0)|difficulty(10)|head_armor(40), imodbits_plate, [], [fac_kingdom_12, fac_kingdom_13, fac_kingdom_14, fac_kingdom_15, fac_kingdom_16, fac_kingdom_17, fac_kingdom_5, fac_kingdom_18]],

	["kolchuga", "Chain Mail Hauberk", [("kolchuga", imodbits_none)], itp_type_body_armor|itp_merchandise|itp_covers_legs|itp_doesnt_cover_hair|itp_can_penetrate_shield, 0, 4500, abundance(20)|weight(20.0)|leg_armor(8)|difficulty(12)|body_armor(37), imodbits_armor, [], [fac_kingdom_2, fac_kingdom_11, fac_kingdom_19]],

	["rus_cap", "Coif", [("rus_cap", imodbits_none)], itp_type_head_armor|itp_merchandise|itp_fit_to_head|itp_offset_lance, 0, 50, abundance(50)|weight(1.0)|head_armor(5), imodbits_cloth, [], [fac_kingdom_2, fac_kingdom_3, fac_kingdom_5, fac_kingdom_11]],

	["rus_fur_hat", "Braavosi Fur Hat", [("rus_fur_hat", imodbits_none)], itp_type_head_armor|itp_fit_to_head|itp_offset_lance, 0, 50, abundance(50)|weight(1.0)|head_armor(5), imodbits_cloth, [], [fac_kingdom_2, fac_kingdom_3, fac_kingdom_5, fac_kingdom_11]],

	["langsax", "Long Knife", [("langsax", imodbits_none), ("langsax_scab", ixmesh_carry)], itp_type_one_handed_wpn|itp_no_parry|itp_merchandise|itp_primary|itp_secondary, itcf_carry_dagger_front_left|itcf_show_holster_when_drawn|itc_dagger, 400, thrust_damage(25, pierce)|hit_points(15360)|spd_rtng(115)|abundance(60)|weight(2.0)|swing_damage(15, cut)|weapon_length(65), imodbits_sword_high, [], [fac_kingdom_11, fac_kingdom_19]],

	["saxon_cap", "Coif", [("saxon_cap", imodbits_none)], itp_type_head_armor|itp_merchandise|itp_fit_to_head|itp_offset_lance, 0, 50, abundance(50)|weight(1.0)|head_armor(5), imodbits_cloth, [], [fac_kingdom_2, fac_kingdom_3, fac_kingdom_5, fac_kingdom_11]],

	["saxon_tunic_a", "Peasants Tunic", [("saxon_tunic_a", imodbits_none)], itp_type_body_armor|itp_merchandise|itp_covers_legs|itp_doesnt_cover_hair|itp_can_penetrate_shield, 0, 50, abundance(55)|weight(2.0)|leg_armor(1)|body_armor(5), imodbits_cloth, [], [fac_kingdom_11, fac_kingdom_19]],

	["crossbearer_cap", "Septons Coif", [("crossbearer_cap", imodbits_none)], itp_type_head_armor|itp_civilian|itp_next_item_as_melee|itp_fit_to_head|itp_offset_lance, 0, 50, abundance(50)|weight(1.0)|head_armor(5), imodbits_cloth, [], [fac_kingdom_2, fac_kingdom_3, fac_kingdom_5, fac_kingdom_11]],

	["crossbearer", "Septons Robe", [("crossbearer", imodbits_none)], itp_type_body_armor|itp_covers_legs|itp_doesnt_cover_hair|itp_can_penetrate_shield|itp_civilian|itp_next_item_as_melee, 0, 50, abundance(55)|weight(2.0)|leg_armor(1)|body_armor(5), imodbits_cloth, [], [fac_kingdom_11, fac_kingdom_19]],

	["red_priest", "Red Priests Robe", [("red_priest", imodbits_none)], itp_type_body_armor|itp_covers_legs|itp_doesnt_cover_hair|itp_can_penetrate_shield|itp_civilian|itp_next_item_as_melee, 0, 50, abundance(55)|weight(2.0)|leg_armor(1)|body_armor(5), imodbits_cloth, [], [fac_kingdom_11, fac_kingdom_19]],

	["sonyer_saracen_2", "Bascinet", [("fi_bascinet_3", imodbits_none)], itp_type_head_armor|itp_merchandise|itp_fit_to_head|itp_offset_lance, 0, 1500, abundance(10)|weight(4.0)|difficulty(12)|head_armor(35), imodbits_armor, [], [fac_kingdom_1, fac_kingdom_3, fac_kingdom_5, fac_kingdom_8, fac_kingdom_9, fac_kingdom_10]],

	["leather_vest_brn", "Leather Vest", [("leather_vest_brn", imodbits_none)], itp_type_body_armor|itp_merchandise|itp_covers_legs|itp_doesnt_cover_hair|itp_can_penetrate_shield, 0, 200, abundance(55)|weight(5.0)|leg_armor(10)|body_armor(5), imodbits_cloth],

	["gambeson_trans", "Gambeson", [("gambeson_trans", imodbits_none)], itp_type_body_armor|itp_merchandise|itp_covers_legs|itp_doesnt_cover_hair|itp_can_penetrate_shield, 0, 200, abundance(55)|weight(5.0)|leg_armor(4)|body_armor(16), imodbits_cloth],

	["onion_top_bascinet", "Hounskull Helmet", [("fi_hounskul", imodbits_none)], itp_type_head_armor|itp_merchandise, 0, 2000, abundance(20)|weight(5.0)|difficulty(12)|head_armor(45), imodbits_plate, [], [fac_kingdom_1, fac_kingdom_3, fac_kingdom_5, fac_kingdom_8, fac_kingdom_9, fac_kingdom_10]],

	["battered_plainhelm", "Old Nasal Helmet", [("battered_plainhelm", imodbits_none)], itp_type_head_armor|itp_merchandise|itp_fit_to_head|itp_offset_lance, 0, 500, abundance(60)|weight(4.0)|difficulty(10)|head_armor(22), imodbits_armor, [], [fac_kingdom_1, fac_kingdom_2, fac_kingdom_3, fac_kingdom_5, fac_kingdom_8, fac_kingdom_9]],

	["wight_berserker_1", "Wights Body", [("wight_berserker_1", imodbits_none)], itp_type_body_armor|itp_unique|itp_covers_legs|itp_doesnt_cover_hair|itp_can_penetrate_shield, 0, 500, abundance(40)|weight(5.0)|leg_armor(30)|body_armor(60), imodbits_cloth, [], [fac_kingdom_4, fac_kingdom_12]],

	["wight_berserker_2", "Wights Body", [("wight_berserker_2", imodbits_none)], itp_type_body_armor|itp_unique|itp_covers_legs|itp_doesnt_cover_hair|itp_can_penetrate_shield, 0, 500, abundance(40)|weight(5.0)|leg_armor(30)|body_armor(60), imodbits_cloth, [], [fac_kingdom_4, fac_kingdom_12]],

	["wight_berserker_3", "Wights Body", [("wight_berserker_3", imodbits_none)], itp_type_body_armor|itp_unique|itp_covers_legs|itp_doesnt_cover_hair|itp_can_penetrate_shield, 0, 500, abundance(40)|weight(5.0)|leg_armor(30)|body_armor(60), imodbits_cloth, [], [fac_kingdom_4, fac_kingdom_12]],

	["wight_fur_armor_1", "Leather Armor", [("wight_fur_armor_1", imodbits_none)], itp_type_body_armor|itp_unique|itp_covers_legs|itp_doesnt_cover_hair|itp_can_penetrate_shield, 0, 500, abundance(40)|weight(5.0)|leg_armor(20)|body_armor(60), imodbits_cloth, [], [fac_kingdom_4, fac_kingdom_12]],

	["wight_fur_armor_2", "Heavy Fur Armor", [("wight_fur_armor_2", imodbits_none)], itp_type_body_armor|itp_unique|itp_covers_legs|itp_doesnt_cover_hair|itp_can_penetrate_shield, 0, 500, abundance(40)|weight(5.0)|leg_armor(30)|body_armor(60), imodbits_cloth, [], [fac_kingdom_4, fac_kingdom_12]],

	["wight_face_1_1", "Wight Head", [("wight_face_1_1", imodbits_none)], itp_type_head_armor|itp_unique|itp_fit_to_head|itp_offset_lance|itp_covers_head|itp_couchable, 0, 500, abundance(60)|weight(4.0)|difficulty(10)|head_armor(60), imodbits_armor, [], [fac_kingdom_11, fac_kingdom_19]],

	["wight_face_1_2", "Wight Head", [("wight_face_1_2", imodbits_none)], itp_type_head_armor|itp_unique|itp_fit_to_head|itp_offset_lance|itp_covers_head|itp_couchable, 0, 500, abundance(60)|weight(4.0)|difficulty(10)|head_armor(60), imodbits_armor, [], [fac_kingdom_11, fac_kingdom_19]],

	["wight_face_1_3", "Wight Head", [("wight_face_1_3", imodbits_none)], itp_type_head_armor|itp_unique|itp_fit_to_head|itp_offset_lance|itp_covers_head|itp_couchable, 0, 500, abundance(60)|weight(4.0)|difficulty(10)|head_armor(60), imodbits_armor, [], [fac_kingdom_11, fac_kingdom_19]],

	["wight_face_2_1", "Wight Head", [("wight_face_2_1", imodbits_none)], itp_type_head_armor|itp_unique|itp_fit_to_head|itp_offset_lance|itp_covers_head|itp_couchable, 0, 500, abundance(60)|weight(4.0)|difficulty(10)|head_armor(60), imodbits_armor, [], [fac_kingdom_11, fac_kingdom_19]],

	["wight_face_2_2", "Wight Head", [("wight_face_2_2", imodbits_none)], itp_type_head_armor|itp_unique|itp_fit_to_head|itp_offset_lance|itp_covers_head|itp_couchable, 0, 500, abundance(60)|weight(4.0)|difficulty(10)|head_armor(60), imodbits_armor, [], [fac_kingdom_11, fac_kingdom_19]],

	["wight_face_2_3", "Wight Head", [("wight_face_2_3", imodbits_none)], itp_type_head_armor|itp_unique|itp_fit_to_head|itp_offset_lance|itp_covers_head|itp_couchable, 0, 500, abundance(60)|weight(4.0)|difficulty(10)|head_armor(60), imodbits_armor, [], [fac_kingdom_11, fac_kingdom_19]],

	["wight_face_helmet_1", "Wight Helmet", [("wight_face_helmet_1", imodbits_none)], itp_type_head_armor|itp_unique|itp_fit_to_head|itp_offset_lance|itp_covers_head|itp_couchable, 0, 500, abundance(60)|weight(4.0)|difficulty(10)|head_armor(60), imodbits_armor, [], [fac_kingdom_11, fac_kingdom_19]],

	["wight_face_helmet_2", "Wight Hat", [("wight_face_helmet_2", imodbits_none)], itp_type_head_armor|itp_unique|itp_fit_to_head|itp_offset_lance|itp_covers_head|itp_couchable, 0, 500, abundance(60)|weight(4.0)|difficulty(10)|head_armor(60), imodbits_armor, [], [fac_kingdom_11, fac_kingdom_19]],

	["wight_face_helmet_3", "Wight Hat", [("wight_face_helmet_3", imodbits_none)], itp_type_head_armor|itp_unique|itp_fit_to_head|itp_offset_lance|itp_covers_head|itp_couchable, 0, 500, abundance(60)|weight(4.0)|difficulty(10)|head_armor(60), imodbits_armor, [], [fac_kingdom_11, fac_kingdom_19]],

	["wight_face_helmet_4", "Wight Hat", [("wight_face_helmet_4", imodbits_none)], itp_type_head_armor|itp_unique|itp_fit_to_head|itp_offset_lance|itp_covers_head|itp_couchable, 0, 500, abundance(60)|weight(4.0)|difficulty(10)|head_armor(60), imodbits_armor, [], [fac_kingdom_11, fac_kingdom_19]],

	["mace_knobbed", "War Mace", [("mace_knobbed", imodbits_none)], itp_type_one_handed_wpn|itp_merchandise|itp_wooden_parry|itp_primary|itp_bonus_against_shield, itcf_carry_mace_left_hip|itc_scimitar, 900, thrust_damage(0, pierce)|hit_points(25600)|spd_rtng(95)|abundance(100)|weight(4.0)|swing_damage(25, blunt)|difficulty(12)|weapon_length(62), imodbits_axe|imodbits_mace, [], [fac_kingdom_1, fac_kingdom_2, fac_kingdom_3, fac_kingdom_5, fac_kingdom_8]],

	["mace_spiral", "War Mace", [("mace_spiral", imodbits_none)], itp_type_one_handed_wpn|itp_merchandise|itp_wooden_parry|itp_primary|itp_bonus_against_shield, itcf_carry_mace_left_hip|itc_scimitar, 900, thrust_damage(0, pierce)|hit_points(25600)|spd_rtng(95)|abundance(100)|weight(4.0)|swing_damage(25, blunt)|difficulty(12)|weapon_length(62), imodbits_axe|imodbits_mace, [], [fac_kingdom_1, fac_kingdom_2, fac_kingdom_3, fac_kingdom_5, fac_kingdom_8]],

	["mackie_morning_star", "Spiked Mace", [("Faradon_IberianMace", imodbits_none)], itp_type_one_handed_wpn|itp_merchandise|itp_wooden_parry|itp_primary|itp_bonus_against_shield, itcf_carry_mace_left_hip|itc_scimitar, 900, thrust_damage(0, pierce)|hit_points(27648)|spd_rtng(95)|abundance(100)|weight(4.0)|swing_damage(27, pierce)|difficulty(12)|weapon_length(70), imodbits_axe|imodbits_mace, [], [fac_kingdom_1, fac_kingdom_2, fac_kingdom_3, fac_kingdom_5, fac_kingdom_8]],

	["kataphraktoi_2", "Leather Jerkin", [("cozur_ragged_leather_jerkin", imodbits_none)], itp_type_body_armor|itp_merchandise|itp_covers_legs|itp_doesnt_cover_hair|itp_can_penetrate_shield, 0, 150, abundance(20)|weight(20.0)|body_armor(17), imodbits_cloth],

	["kataphraktoi_3", "Heavy Lamellar Armor", [("cozur_lamellar_armor_d", imodbits_none)], itp_type_body_armor|itp_merchandise|itp_covers_legs|itp_doesnt_cover_hair|itp_can_penetrate_shield, 0, 6000, abundance(5)|weight(20.0)|leg_armor(7)|difficulty(12)|body_armor(46), imodbits_armor, [], [fac_kingdom_12, fac_kingdom_13, fac_kingdom_14, fac_kingdom_15, fac_kingdom_16, fac_kingdom_17, fac_kingdom_5, fac_kingdom_18]],

	["kataphraktoi_4", "Coat of Plates", [("cozur_coat_of_plates_a", imodbits_none)], itp_type_body_armor|itp_merchandise|itp_covers_legs|itp_doesnt_cover_hair|itp_can_penetrate_shield, 0, 1500, abundance(5)|weight(20.0)|leg_armor(15)|difficulty(12)|body_armor(33), imodbits_armor, [], [fac_kingdom_3]],

	["kataphraktoi_5", "Coat of Plates", [("cozur_coat_of_plates_red", imodbits_none)], itp_type_body_armor|itp_merchandise|itp_covers_legs|itp_doesnt_cover_hair|itp_can_penetrate_shield, 0, 1500, abundance(20)|weight(20.0)|leg_armor(15)|difficulty(12)|body_armor(33), imodbits_armor, [], [fac_kingdom_8]],

	["shortsword1", "Short Sword", [("shortsword1", imodbits_none), ("shortsword1_scab", ixmesh_carry)], itp_type_one_handed_wpn|itp_primary|itp_civilian|itp_next_item_as_melee, itcf_carry_sword_left_hip|itcf_show_holster_when_drawn|itc_longsword, 600, thrust_damage(28, pierce)|hit_points(20480)|spd_rtng(110)|abundance(10)|weight(2.0)|swing_damage(20, cut)|difficulty(10)|weapon_length(61), imodbits_none, [], [fac_kingdom_2, fac_kingdom_11, fac_kingdom_19]],

	["rus_mail_cozur", "Chain Mail Hauberk", [("drz_mail_shirt", imodbits_none)], itp_type_body_armor|itp_covers_legs|itp_doesnt_cover_hair|itp_can_penetrate_shield, 0, 4000, abundance(20)|weight(16.0)|leg_armor(15)|difficulty(12)|body_armor(37), imodbits_armor, [], [fac_kingdom_11, fac_kingdom_19]],

	["sh_rho_pav_deploy_a", "Heavy Lamellar Armor", [("drz_elite_lamellar_armor", imodbits_none)], itp_type_body_armor|itp_merchandise|itp_covers_legs|itp_doesnt_cover_hair|itp_can_penetrate_shield, 0, 9000, abundance(20)|weight(25.0)|leg_armor(12)|difficulty(14)|body_armor(46), imodbits_armor, [], [fac_kingdom_12, fac_kingdom_13, fac_kingdom_14, fac_kingdom_15, fac_kingdom_16, fac_kingdom_17, fac_kingdom_5, fac_kingdom_18]],

	["sh_rho_pav_deploy_b", "Heavy Plate Armor", [("hawkwood", imodbits_none)], itp_type_body_armor|itp_covers_legs|itp_doesnt_cover_hair|itp_can_penetrate_shield, 0, 9000, abundance(5)|weight(25.0)|leg_armor(10)|difficulty(14)|body_armor(54), imodbits_plate, [], [fac_kingdom_1, fac_kingdom_3, fac_kingdom_5, fac_kingdom_8, fac_kingdom_9, fac_kingdom_10]],

	["sh_rho_pav_deploy_e", "Plate Boots", [("full_plate_boots_3", imodbits_none)], itp_type_foot_armor|itp_attach_armature|itp_attachment_mask|itp_merchandise, 0, 2000, abundance(60)|weight(1.0)|leg_armor(40)|difficulty(12), imodbits_cloth, [], [fac_kingdom_1, fac_kingdom_5]],

	["sh_rho_pav_deploy_f", "Plate Boots", [("full_plate_boots_4", imodbits_none)], itp_type_foot_armor|itp_attach_armature|itp_attachment_mask|itp_merchandise, 0, 2000, abundance(60)|weight(1.0)|leg_armor(40)|difficulty(12), imodbits_cloth, [], [fac_kingdom_1, fac_kingdom_5]],

	["fi_tourney_helmet_2", "Decorated Tournament Helmet", [("fi_tourney_helmet_2", imodbits_none)], itp_type_head_armor|itp_unique|itp_covers_head|itp_couchable|itp_covers_beard, 0, 2500, abundance(10)|weight(6.0)|difficulty(13)|head_armor(45), imodbits_plate, [], [fac_kingdom_9, fac_kingdom_10]],

	["fi_hood_1", "Cloth Hood", [("fi_hood_1", imodbits_none)], itp_type_head_armor|itp_merchandise, 0, 100, abundance(80)|weight(1.0)|head_armor(5), imodbits_cloth, [], [fac_kingdom_1, fac_kingdom_2, fac_kingdom_3, fac_kingdom_4, fac_kingdom_5, fac_kingdom_8, fac_kingdom_9, fac_kingdom_11]],

	["fi_hood_4", "Leather Hood", [("fi_hood_4", imodbits_none)], itp_type_head_armor|itp_merchandise, 0, 100, abundance(80)|weight(1.0)|head_armor(5), imodbits_cloth, [], [fac_kingdom_1, fac_kingdom_2, fac_kingdom_3, fac_kingdom_4, fac_kingdom_5, fac_kingdom_8, fac_kingdom_9, fac_kingdom_11]],

	["fi_sallet_1", "Visored Sallet", [("fi_sallet_1", imodbits_none)], itp_type_head_armor|itp_merchandise, 0, 1500, abundance(10)|weight(4.0)|difficulty(12)|head_armor(34), imodbits_plate, [], [fac_kingdom_1, fac_kingdom_3, fac_kingdom_4, fac_kingdom_8, fac_kingdom_9, fac_kingdom_10]],

	["fi_sallet_2", "Visored Sallet", [("fi_sallet_2", imodbits_none)], itp_type_head_armor|itp_merchandise, 0, 1500, abundance(10)|weight(4.0)|difficulty(12)|head_armor(34), imodbits_plate, [], [fac_kingdom_1, fac_kingdom_3, fac_kingdom_4, fac_kingdom_8, fac_kingdom_9, fac_kingdom_10]],

	["fi_sallet_3", "Open Sallet", [("fi_sallet_3", imodbits_none)], itp_type_head_armor|itp_merchandise, 0, 1000, abundance(10)|weight(4.0)|difficulty(12)|head_armor(33), imodbits_plate, [], [fac_kingdom_2, fac_kingdom_4]],

	["fi_great_bascinet", "Great Bascinet", [("fi_great_bascinet", imodbits_none)], itp_type_head_armor|itp_merchandise, 0, 2000, abundance(10)|weight(6.0)|difficulty(13)|head_armor(45), imodbits_plate, [], [fac_kingdom_9, fac_kingdom_10]],

	["fi_pigface", "Pigface Klapvisor", [("fi_pigface", imodbits_none)], itp_type_head_armor|itp_merchandise, 0, 2000, abundance(10)|weight(6.0)|difficulty(13)|head_armor(45), imodbits_plate, [], [fac_kingdom_1, fac_kingdom_8, fac_kingdom_9, fac_kingdom_10]],

	["fi_cataphract_helmet_2", "Cataphract Helmet", [("fi_cataphract_helmet_1", imodbits_none)], itp_type_head_armor|itp_merchandise|itp_fit_to_head|itp_offset_lance|itp_covers_beard, 0, 2000, abundance(10)|weight(4.0)|difficulty(12)|head_armor(37), imodbits_plate, [], [fac_kingdom_12, fac_kingdom_13, fac_kingdom_14, fac_kingdom_15, fac_kingdom_16, fac_kingdom_17, fac_kingdom_5, fac_kingdom_18]],

	["cool_dagger", "Dagger", [("norman_dagger", imodbits_none), ("norman_dagger_scab", ixmesh_carry)], itp_type_one_handed_wpn|itp_no_parry|itp_primary|itp_secondary, itcf_carry_dagger_front_left|itcf_show_holster_when_drawn|itc_dagger, 100, thrust_damage(25, pierce)|hit_points(9216)|spd_rtng(108)|abundance(60)|weight(1.0)|swing_damage(9, cut)|weapon_length(40), imodbits_none],

	["cool_dagger_2", "Dagger", [("norman_dagger", imodbits_none), ("norman_dagger_scab", ixmesh_carry)], itp_type_one_handed_wpn|itp_no_parry|itp_primary|itp_secondary, itcf_carry_dagger_front_left|itcf_show_holster_when_drawn|itc_dagger, 100, thrust_damage(25, pierce)|hit_points(9216)|spd_rtng(108)|abundance(60)|weight(1.0)|swing_damage(9, cut)|weapon_length(40), imodbits_none],

	["cool_dagger_3", "Dagger", [("vikingr_seax", imodbits_none), ("vikingr_seax_scab", ixmesh_carry)], itp_type_one_handed_wpn|itp_no_parry|itp_primary|itp_secondary, itcf_carry_dagger_front_left|itcf_show_holster_when_drawn|itc_dagger, 100, thrust_damage(25, pierce)|hit_points(9216)|spd_rtng(108)|abundance(60)|weight(1.0)|swing_damage(9, cut)|weapon_length(40), imodbits_none],

	["cool_dagger_4", "Dagger", [("saxon_seax", imodbits_none), ("saxon_seax_scab", ixmesh_carry)], itp_type_one_handed_wpn|itp_no_parry|itp_primary|itp_secondary, itcf_carry_dagger_front_left|itcf_show_holster_when_drawn|itc_dagger, 100, thrust_damage(25, pierce)|hit_points(9216)|spd_rtng(108)|abundance(60)|weight(1.0)|swing_damage(9, cut)|weapon_length(40), imodbits_none],

	["ilyns_leather_armor", "Ilyns Leather Armor", [("cozur_ragged_leather_jerkin", imodbits_none)], itp_type_body_armor|itp_covers_legs|itp_doesnt_cover_hair|itp_can_penetrate_shield|itp_civilian|itp_next_item_as_melee, 0, 100, abundance(55)|weight(5.0)|leg_armor(5)|body_armor(5), imodbits_cloth, [], [fac_kingdom_13, fac_kingdom_14, fac_kingdom_15, fac_kingdom_16]],

	["kingsguard_armor", "Kingsguard Armor", [("westerland_kingsguard", imodbits_none)], itp_type_body_armor|itp_covers_legs|itp_doesnt_cover_hair|itp_can_penetrate_shield|itp_civilian|itp_next_item_as_melee, 0, 100, abundance(55)|weight(5.0)|leg_armor(5)|body_armor(5), imodbits_cloth, [], [fac_kingdom_13, fac_kingdom_14, fac_kingdom_15, fac_kingdom_16]],

	["stormlands_sellsword_armor_1", "Chain Mail Hauberk", [("sellsword_armor_1", imodbits_none)], itp_type_body_armor|itp_merchandise|itp_covers_legs|itp_doesnt_cover_hair|itp_can_penetrate_shield, 0, 3500, abundance(20)|weight(20.0)|leg_armor(5)|difficulty(12)|body_armor(37), imodbits_armor, [], [fac_kingdom_1]],

	["dragonstone_sellsword_armor_2", "Chain Mail Hauberk", [("sellsword_armor_2", imodbits_none)], itp_type_body_armor|itp_merchandise|itp_covers_legs|itp_doesnt_cover_hair|itp_can_penetrate_shield, 0, 3500, abundance(20)|weight(20.0)|leg_armor(5)|difficulty(12)|body_armor(37), imodbits_armor, [], [fac_kingdom_8]],

	["sellsword_armor_4", "Chain Mail Hauberk", [("sellsword_armor_4", imodbits_none)], itp_type_body_armor|itp_merchandise|itp_covers_legs|itp_doesnt_cover_hair|itp_can_penetrate_shield, 0, 3500, abundance(20)|weight(20.0)|leg_armor(5)|difficulty(12)|body_armor(37), imodbits_armor, [], [fac_kingdom_1, fac_kingdom_3, fac_kingdom_6, fac_kingdom_8, fac_kingdom_9, fac_kingdom_10]],

	["fi_chain_mail_hauberk", "Chain Mail Hauberk", [("fi_chain_mail_hauberk", imodbits_none)], itp_type_body_armor|itp_merchandise|itp_covers_legs|itp_doesnt_cover_hair|itp_can_penetrate_shield, 0, 3500, abundance(20)|weight(20.0)|leg_armor(5)|difficulty(12)|body_armor(37), imodbits_armor, [], [fac_kingdom_1, fac_kingdom_8]],

	["shagwells_armor", "Chain Mail Hauberk", [("fi_chain_mail_hauberk_heraldic_1", imodbits_none)], itp_type_body_armor|itp_covers_legs|itp_doesnt_cover_hair|itp_can_penetrate_shield, 0, 3000, abundance(20)|weight(20.0)|leg_armor(5)|difficulty(12)|body_armor(37), imodbits_armor, [], [fac_kingdom_13]],

	["sellsword_armor_3", "Heavy Plate Armor", [("sellsword_armor_3", imodbits_none)], itp_type_body_armor|itp_merchandise|itp_covers_legs|itp_doesnt_cover_hair|itp_can_penetrate_shield, 0, 9000, abundance(5)|weight(20.0)|leg_armor(10)|difficulty(14)|body_armor(54), imodbits_plate, [], [fac_kingdom_1, fac_kingdom_3, fac_kingdom_8, fac_kingdom_9, fac_kingdom_10]],

	["vale_sellsword_armor_5", "Heavy Plate Armor", [("sellsword_armor_5", imodbits_none)], itp_type_body_armor|itp_covers_legs|itp_doesnt_cover_hair|itp_can_penetrate_shield, 0, 9000, abundance(5)|weight(20.0)|leg_armor(10)|difficulty(14)|body_armor(54), imodbits_plate, [], [fac_kingdom_13]],

	["sellsword_plate_armor_3", "Heavy Plate Armor", [("sellsword_plate_armor_3", imodbits_none)], itp_type_body_armor|itp_merchandise|itp_covers_legs|itp_doesnt_cover_hair|itp_can_penetrate_shield, 0, 9000, abundance(5)|weight(20.0)|leg_armor(15)|difficulty(14)|body_armor(54), imodbits_plate, [], [fac_kingdom_1, fac_kingdom_3, fac_kingdom_8, fac_kingdom_9, fac_kingdom_10]],

	["full_plate_armor_1", "Heavy Plate Armor", [("full_plate_armor_1", imodbits_none)], itp_type_body_armor|itp_merchandise|itp_covers_legs|itp_doesnt_cover_hair|itp_can_penetrate_shield, 0, 9000, abundance(5)|weight(20.0)|leg_armor(15)|difficulty(14)|body_armor(54), imodbits_plate, [], [fac_kingdom_1, fac_kingdom_3, fac_kingdom_8, fac_kingdom_9, fac_kingdom_10]],

	["full_plate_armor_2", "Heavy Plate Armor", [("full_plate_armor_2", imodbits_none)], itp_type_body_armor|itp_merchandise|itp_covers_legs|itp_doesnt_cover_hair|itp_can_penetrate_shield, 0, 9000, abundance(5)|weight(20.0)|leg_armor(15)|difficulty(14)|body_armor(54), imodbits_plate, [], [fac_kingdom_1, fac_kingdom_3, fac_kingdom_8, fac_kingdom_9, fac_kingdom_10]],

	["full_plate_armor_3", "Heavy Plate Armor", [("full_plate_armor_3", imodbits_none)], itp_type_body_armor|itp_merchandise|itp_covers_legs|itp_doesnt_cover_hair|itp_can_penetrate_shield, 0, 9000, abundance(5)|weight(20.0)|leg_armor(15)|difficulty(14)|body_armor(54), imodbits_plate, [], [fac_kingdom_1, fac_kingdom_3, fac_kingdom_8, fac_kingdom_9, fac_kingdom_10]],

	["fi_chain_mail_jerkin", "Heavy Plate Armor", [("fi_chain_mail_jerkin", imodbits_none)], itp_type_body_armor|itp_merchandise|itp_covers_legs|itp_doesnt_cover_hair|itp_can_penetrate_shield, 0, 9000, abundance(5)|weight(20.0)|leg_armor(10)|difficulty(14)|body_armor(54), imodbits_plate, [], [fac_kingdom_1, fac_kingdom_3, fac_kingdom_8, fac_kingdom_9, fac_kingdom_10]],

	["fi_massive_plate_armor", "Heavy Plate Armor", [("fi_massive_plate_armor", imodbits_none)], itp_type_body_armor|itp_covers_legs|itp_doesnt_cover_hair|itp_can_penetrate_shield|itp_civilian|itp_next_item_as_melee, 0, 9000, abundance(5)|weight(20.0)|leg_armor(20)|difficulty(14)|body_armor(60), imodbits_plate, [], [fac_kingdom_10]],

	["fi_arryn_plate_armor_1", "Heavy Plate Armor", [("fi_arryn_plate_armor_1", imodbits_none)], itp_type_body_armor|itp_merchandise|itp_covers_legs|itp_doesnt_cover_hair|itp_can_penetrate_shield, 0, 9000, abundance(5)|weight(20.0)|leg_armor(15)|difficulty(14)|body_armor(54), imodbits_plate, [], [fac_kingdom_3]],

	["fi_dorne_plate_armor_1", "Heavy Plate Armor", [("fi_dorne_plate_armor_1", imodbits_none)], itp_type_body_armor|itp_merchandise|itp_covers_legs|itp_doesnt_cover_hair|itp_can_penetrate_shield, 0, 9000, abundance(5)|weight(20.0)|leg_armor(15)|difficulty(14)|body_armor(54), imodbits_plate, [], [fac_kingdom_9]],

	["fi_dorne_plate_armor_2", "Heavy Plate Armor", [("fi_dorne_plate_armor_2", imodbits_none)], itp_type_body_armor|itp_merchandise|itp_covers_legs|itp_doesnt_cover_hair|itp_can_penetrate_shield, 0, 9000, abundance(5)|weight(20.0)|leg_armor(15)|difficulty(14)|body_armor(54), imodbits_plate, [], [fac_kingdom_9]],

	["fi_reach_plate_armor_1", "Heavy Plate Armor", [("fi_reach_plate_armor_1", imodbits_none)], itp_type_body_armor|itp_merchandise|itp_covers_legs|itp_doesnt_cover_hair|itp_can_penetrate_shield, 0, 9000, abundance(5)|weight(20.0)|leg_armor(15)|difficulty(14)|body_armor(54), imodbits_plate, [], [fac_kingdom_10]],

	["fi_reach_plate_armor_2", "Heavy Plate Armor", [("fi_reach_plate_armor_2", imodbits_none)], itp_type_body_armor|itp_merchandise|itp_covers_legs|itp_doesnt_cover_hair|itp_can_penetrate_shield, 0, 9000, abundance(5)|weight(20.0)|leg_armor(15)|difficulty(14)|body_armor(54), imodbits_plate, [], [fac_kingdom_10]],

	["fi_reach_plate_armor_3", "Heavy Plate Armor", [("fi_reach_plate_armor_3", imodbits_none)], itp_type_body_armor|itp_merchandise|itp_covers_legs|itp_doesnt_cover_hair|itp_can_penetrate_shield, 0, 9000, abundance(5)|weight(20.0)|leg_armor(15)|difficulty(14)|body_armor(54), imodbits_plate, [], [fac_kingdom_10]],

	["fi_westerlands_plate_armor_1", "Heavy Plate Armor", [("fi_westerlands_plate_armor_1", imodbits_none)], itp_type_body_armor|itp_covers_legs|itp_doesnt_cover_hair|itp_can_penetrate_shield, 0, 9000, abundance(5)|weight(20.0)|leg_armor(15)|difficulty(14)|body_armor(54), imodbits_plate],

	["fi_stripped_leather_jerkin", "Leather Jerkin", [("fi_stripped_leather_jerkin", imodbits_none)], itp_type_body_armor|itp_covers_legs|itp_doesnt_cover_hair|itp_can_penetrate_shield, 0, 300, abundance(55)|weight(5.0)|body_armor(20), imodbits_cloth, [], [fac_kingdom_1, fac_kingdom_3, fac_kingdom_8]],

	["fi_leather_jerkin_2", "Leather Jerkin", [("fi_leather_jerkin_2", imodbits_none)], itp_type_body_armor|itp_covers_legs|itp_doesnt_cover_hair|itp_can_penetrate_shield, 0, 200, abundance(55)|weight(5.0)|body_armor(18), imodbits_cloth, [], [fac_kingdom_1, fac_kingdom_3, fac_kingdom_8]],

	["fi_leather_jerkin", "Heavy Leather Jerkin", [("fi_leather_jerkin", imodbits_none)], itp_type_body_armor|itp_merchandise|itp_covers_legs|itp_doesnt_cover_hair|itp_can_penetrate_shield, 0, 600, abundance(55)|weight(5.0)|leg_armor(3)|body_armor(28), imodbits_cloth, [], [fac_kingdom_10]],

	["fi_green_leather_armor", "Kingswood Leather Jerkin", [("fi_green_leather_armor", imodbits_none)], itp_type_body_armor|itp_covers_legs|itp_doesnt_cover_hair|itp_can_penetrate_shield, 0, 150, abundance(55)|weight(5.0)|body_armor(12), imodbits_cloth, [], [fac_kingdom_1, fac_kingdom_3, fac_kingdom_9, fac_kingdom_10]],

	["stormland_light", "Gambeson", [("stormland_light", imodbits_none)], itp_type_body_armor|itp_covers_legs|itp_doesnt_cover_hair|itp_can_penetrate_shield, 0, 300, abundance(50)|weight(5.0)|leg_armor(6)|body_armor(22), imodbits_cloth, [], [fac_kingdom_1]],

	["sellsword_light", "Leather Jerkin", [("sellsword_light", imodbits_none)], itp_type_body_armor|itp_merchandise|itp_covers_legs|itp_doesnt_cover_hair|itp_can_penetrate_shield, 0, 200, abundance(50)|weight(5.0)|leg_armor(3)|body_armor(18), imodbits_cloth, [], [fac_kingdom_3, fac_kingdom_8]],

	["westerland_goldcloak", "Gold Cloaks Chain Mail Hauberk", [("westerland_goldcloak", imodbits_none)], itp_type_body_armor|itp_covers_legs|itp_doesnt_cover_hair|itp_can_penetrate_shield, 0, 3000, abundance(50)|weight(20.0)|leg_armor(10)|difficulty(12)|body_armor(36), imodbits_armor, [], [fac_kingdom_1]],

	["westerland_goldcloak_cloaked", "Gold Cloaks Chain Mail Hauberk", [("westerland_goldcloak_cloaked", imodbits_none)], itp_type_body_armor|itp_covers_legs|itp_doesnt_cover_hair|itp_can_penetrate_shield, 0, 3000, abundance(50)|weight(20.0)|leg_armor(10)|difficulty(12)|body_armor(36), imodbits_armor, [], [fac_kingdom_1]],

	["westerland_hound", "Chain Mail Hauberk", [("westerland_hound", imodbits_none)], itp_type_body_armor|itp_merchandise|itp_covers_legs|itp_doesnt_cover_hair|itp_can_penetrate_shield, 0, 3800, abundance(20)|weight(20.0)|leg_armor(10)|difficulty(12)|body_armor(37), imodbits_armor, [], [fac_kingdom_1, fac_kingdom_3, fac_kingdom_8, fac_kingdom_9, fac_kingdom_10]],

	["nightswatch_a", "Leather Jerkin", [("nightswatch_a", imodbits_none)], itp_type_body_armor|itp_merchandise|itp_covers_legs|itp_doesnt_cover_hair|itp_can_penetrate_shield, 0, 200, abundance(50)|weight(5.0)|leg_armor(4)|body_armor(14), imodbits_cloth, [], [fac_kingdom_1, fac_kingdom_3, fac_kingdom_5, fac_kingdom_8, fac_kingdom_9, fac_kingdom_10]],

	["nightswatch_b", "Leather Jerkin", [("nightswatch_b", imodbits_none)], itp_type_body_armor|itp_merchandise|itp_covers_legs|itp_doesnt_cover_hair|itp_can_penetrate_shield, 0, 200, abundance(50)|weight(5.0)|leg_armor(4)|body_armor(14), imodbits_cloth, [], [fac_kingdom_1, fac_kingdom_3, fac_kingdom_5, fac_kingdom_8, fac_kingdom_9, fac_kingdom_10]],

	["nightswatch_c", "Reinforced Leather Jerkin", [("nightswatch_c", imodbits_none)], itp_type_body_armor|itp_merchandise|itp_covers_legs|itp_doesnt_cover_hair|itp_can_penetrate_shield, 0, 400, abundance(50)|weight(5.0)|leg_armor(8)|body_armor(25), imodbits_none, [], [fac_kingdom_1, fac_kingdom_3, fac_kingdom_5, fac_kingdom_8, fac_kingdom_9, fac_kingdom_10]],

	["nightswatch_d", "Lamellar Armor", [("nightswatch_d", imodbits_none)], itp_type_body_armor|itp_merchandise|itp_covers_legs|itp_doesnt_cover_hair|itp_can_penetrate_shield, 0, 2000, abundance(50)|weight(20.0)|leg_armor(10)|difficulty(12)|body_armor(33), imodbits_none, [], [fac_kingdom_8, fac_kingdom_9]],

	["north_archer", "Leather Gambeson", [("north_archer", imodbits_none)], itp_type_body_armor|itp_merchandise|itp_covers_legs|itp_doesnt_cover_hair|itp_can_penetrate_shield, 0, 300, abundance(50)|weight(5.0)|leg_armor(10)|body_armor(22), imodbits_cloth, [], [fac_kingdom_11, fac_kingdom_19]],

	["north_hunter", "Leather Jerkin", [("north_hunter", imodbits_none)], itp_type_body_armor|itp_merchandise|itp_covers_legs|itp_doesnt_cover_hair|itp_can_penetrate_shield, 0, 1000, abundance(50)|weight(5.0)|leg_armor(10)|difficulty(10)|body_armor(26), imodbits_cloth, [], [fac_kingdom_11, fac_kingdom_19]],

	["north_heavycav", "Heavy Leather Armor", [("north_heavycav", imodbits_none)], itp_type_body_armor|itp_merchandise|itp_covers_legs|itp_doesnt_cover_hair|itp_can_penetrate_shield, 0, 2500, abundance(20)|weight(20.0)|leg_armor(10)|difficulty(12)|body_armor(35), imodbits_none, [], [fac_kingdom_3, fac_kingdom_8]],

	["riverlands_light", "Leather Scale Jerkin", [("riverlands_light", imodbits_none)], itp_type_body_armor|itp_merchandise|itp_covers_legs|itp_doesnt_cover_hair|itp_can_penetrate_shield, 0, 600, abundance(50)|weight(5.0)|leg_armor(7)|body_armor(22), imodbits_none, [], [fac_kingdom_1, fac_kingdom_3, fac_kingdom_2, fac_kingdom_8]],

	["riverlands_freyheavy", "Leather Jerkin", [("riverlands_freyheavy", imodbits_none)], itp_type_body_armor|itp_merchandise|itp_covers_legs|itp_doesnt_cover_hair|itp_can_penetrate_shield, 0, 240, abundance(50)|weight(5.0)|leg_armor(10)|body_armor(14), imodbits_cloth, [], [fac_kingdom_8, fac_kingdom_9]],

	["riverlands_freylight", "Leather Jerkin", [("riverlands_freylight", imodbits_none)], itp_type_body_armor|itp_merchandise|itp_covers_legs|itp_doesnt_cover_hair|itp_can_penetrate_shield, 0, 250, abundance(50)|weight(5.0)|leg_armor(10)|body_armor(23), imodbits_cloth, [], [fac_kingdom_3]],

	["riverlands_freylight_shoulders", "Leather Jerkin", [("riverlands_freylight_shoulders", imodbits_none)], itp_type_body_armor|itp_merchandise|itp_covers_legs|itp_doesnt_cover_hair|itp_can_penetrate_shield, 0, 400, abundance(50)|weight(5.0)|leg_armor(10)|body_armor(26), imodbits_none, [], [fac_kingdom_3]],

	["vale_heavy", "Light Plate Armor", [("vale_heavy", imodbits_none)], itp_type_body_armor|itp_merchandise|itp_covers_legs|itp_doesnt_cover_hair|itp_can_penetrate_shield, 0, 4000, abundance(5)|weight(20.0)|leg_armor(5)|body_armor(40), imodbits_armor, [], [fac_kingdom_3]],

	["vale_heavy_neck", "Light Plate Armor", [("vale_heavy_neck", imodbits_none)], itp_type_body_armor|itp_merchandise|itp_covers_legs|itp_doesnt_cover_hair|itp_can_penetrate_shield, 0, 4000, abundance(5)|weight(20.0)|leg_armor(5)|body_armor(40)|head_armor(5), imodbits_armor, [], [fac_kingdom_3]],

	["sellsword_jerkin", "Leather Jerkin", [("sellsword_jerkin", imodbits_none)], itp_type_body_armor|itp_merchandise|itp_covers_legs|itp_doesnt_cover_hair|itp_can_penetrate_shield, 0, 200, abundance(50)|weight(5.0)|leg_armor(10)|body_armor(18), imodbits_cloth, [], [fac_kingdom_1, fac_kingdom_3, fac_kingdom_2, fac_kingdom_8]],

	["sellsword_jerkin_neck", "Leather Jerkin", [("sellsword_jerkin_neck", imodbits_none)], itp_type_body_armor|itp_merchandise|itp_covers_legs|itp_doesnt_cover_hair|itp_can_penetrate_shield, 0, 350, abundance(50)|weight(5.0)|leg_armor(10)|body_armor(10)|head_armor(5), imodbits_none, [], [fac_kingdom_1, fac_kingdom_3, fac_kingdom_2, fac_kingdom_8]],

	["north_bolton_standard", "Chain Mail Hauberk", [("north_bolton_standard", imodbits_none)], itp_type_body_armor|itp_merchandise|itp_covers_legs|itp_doesnt_cover_hair|itp_can_penetrate_shield, 0, 3500, abundance(20)|weight(20.0)|leg_armor(5)|difficulty(12)|body_armor(37), imodbits_armor, [], [fac_kingdom_2]],

	["north_bolton_heavy", "Plated Chain Mail Hauberk", [("north_bolton_heavy", imodbits_none)], itp_type_body_armor|itp_merchandise|itp_covers_legs|itp_doesnt_cover_hair|itp_can_penetrate_shield, 0, 4500, abundance(20)|weight(20.0)|leg_armor(15)|difficulty(14)|body_armor(43), imodbits_armor, [], [fac_kingdom_2]],

	["north_bolton_standard_cloaked", "Chain Mail Hauberk", [("north_bolton_standard_cloaked", imodbits_none)], itp_type_body_armor|itp_merchandise|itp_covers_legs|itp_doesnt_cover_hair|itp_can_penetrate_shield, 0, 3500, abundance(20)|weight(20.0)|leg_armor(5)|difficulty(12)|body_armor(37), imodbits_armor, [], [fac_kingdom_2]],

	["north_bolton_lord", "Boltons Plated Chain Mail Hauberk", [("north_bolton_lord", imodbits_none)], itp_type_body_armor|itp_always_loot|itp_covers_legs|itp_doesnt_cover_hair|itp_can_penetrate_shield, 0, 4500, abundance(20)|weight(20.0)|leg_armor(10)|difficulty(14)|body_armor(42), imodbits_armor, [], [fac_kingdom_1]],

	["north_bolton_lord_cloaked", "Boltons Chain Mail Hauberk", [("north_bolton_lord_cloaked", imodbits_none)], itp_type_body_armor|itp_covers_legs|itp_doesnt_cover_hair|itp_can_penetrate_shield, 0, 3500, abundance(20)|weight(20.0)|leg_armor(6)|difficulty(12)|body_armor(37), imodbits_armor, [], [fac_kingdom_1]],

	["north_karstark_01", "Chain Mail Hauberk", [("north_karstark_01", imodbits_none)], itp_type_body_armor|itp_merchandise|itp_covers_legs|itp_doesnt_cover_hair|itp_can_penetrate_shield, 0, 3800, abundance(20)|weight(20.0)|leg_armor(10)|difficulty(12)|body_armor(37), imodbits_armor, [], [fac_kingdom_2, fac_kingdom_3]],

	["north_karstark_01_heavy", "Plated Chain Mail Hauberk", [("north_karstark_01_heavy", imodbits_none)], itp_type_body_armor|itp_merchandise|itp_covers_legs|itp_doesnt_cover_hair|itp_can_penetrate_shield, 0, 4200, abundance(20)|weight(20.0)|leg_armor(10)|difficulty(12)|body_armor(41), imodbits_armor, [], [fac_kingdom_2, fac_kingdom_3]],

	["north_karstark_01_cloaked", "Chain Mail Hauberk", [("north_karstark_01_cloaked", imodbits_none)], itp_type_body_armor|itp_merchandise|itp_covers_legs|itp_doesnt_cover_hair|itp_can_penetrate_shield, 0, 4000, abundance(20)|weight(20.0)|leg_armor(10)|difficulty(12)|body_armor(37), imodbits_armor, [], [fac_kingdom_2, fac_kingdom_3]],

	["north_karstark_02", "Chain Mail Hauberk", [("north_karstark_02", imodbits_none)], itp_type_body_armor|itp_merchandise|itp_covers_legs|itp_doesnt_cover_hair|itp_can_penetrate_shield, 0, 4200, abundance(20)|weight(20.0)|leg_armor(18)|difficulty(12)|body_armor(37), imodbits_armor, [], [fac_kingdom_2]],

	["north_light_01", "Leather Jerkin", [("north_light_01", imodbits_none)], itp_type_body_armor|itp_merchandise|itp_covers_legs|itp_doesnt_cover_hair|itp_can_penetrate_shield, 0, 200, abundance(50)|weight(5.0)|leg_armor(10)|body_armor(10), imodbits_cloth, [], [fac_kingdom_2, fac_kingdom_3]],

	["north_light_01_cloaked", "Leather Jerkin", [("north_light_01_cloaked", imodbits_none)], itp_type_body_armor|itp_merchandise|itp_covers_legs|itp_doesnt_cover_hair|itp_can_penetrate_shield, 0, 200, abundance(50)|weight(5.0)|leg_armor(10)|body_armor(10), imodbits_cloth, [], [fac_kingdom_2, fac_kingdom_3]],

	["north_light_02", "Chain Mail Hauberk", [("north_light_02", imodbits_none)], itp_type_body_armor|itp_merchandise|itp_covers_legs|itp_doesnt_cover_hair|itp_can_penetrate_shield, 0, 3800, abundance(20)|weight(20.0)|leg_armor(5)|difficulty(12)|body_armor(37), imodbits_armor, [], [fac_kingdom_2, fac_kingdom_3]],

	["north_stark_captain_heavy", "Plated Chain Mail Hauberk", [("north_stark_captain_heavy", imodbits_none)], itp_type_body_armor|itp_merchandise|itp_covers_legs|itp_doesnt_cover_hair|itp_can_penetrate_shield, 0, 4000, abundance(20)|weight(20.0)|leg_armor(10)|difficulty(12)|body_armor(42), imodbits_armor, [], [fac_kingdom_2]],

	["north_stark_captain", "Chain Mail Hauberk", [("north_stark_captain", imodbits_none)], itp_type_body_armor|itp_merchandise|itp_covers_legs|itp_doesnt_cover_hair|itp_can_penetrate_shield, 0, 3800, abundance(20)|weight(20.0)|leg_armor(10)|difficulty(12)|body_armor(37), imodbits_armor, [], [fac_kingdom_2]],

	["north_stark_captain_cloaked", "Chain Mail Hauberk", [("north_stark_captain_cloaked", imodbits_none)], itp_type_body_armor|itp_merchandise|itp_covers_legs|itp_doesnt_cover_hair|itp_can_penetrate_shield, 0, 3800, abundance(20)|weight(20.0)|leg_armor(10)|difficulty(12)|body_armor(37), imodbits_armor, [], [fac_kingdom_2]],

	["north_stark_knight", "Heavy Leather Jerkin", [("north_stark_knight", imodbits_none)], itp_type_body_armor|itp_merchandise|itp_covers_legs|itp_doesnt_cover_hair|itp_can_penetrate_shield, 0, 1000, abundance(20)|weight(10.0)|leg_armor(10)|body_armor(34)|head_armor(5), imodbits_cloth, [], [fac_kingdom_2]],

	["north_stark_heavy_knight", "Heavy Plated Leather Jerkin", [("north_stark_heavy_knight", imodbits_none)], itp_type_body_armor|itp_merchandise|itp_covers_legs|itp_doesnt_cover_hair|itp_can_penetrate_shield, 0, 2500, abundance(20)|weight(20.0)|leg_armor(10)|difficulty(14)|body_armor(37)|head_armor(5), imodbits_plate, [], [fac_kingdom_2]],

	["north_stark_lord", "Heavy Plated Leather Jerkin", [("north_stark_lord", imodbits_none)], itp_type_body_armor|itp_merchandise|itp_covers_legs|itp_doesnt_cover_hair|itp_can_penetrate_shield, 0, 2000, abundance(20)|weight(20.0)|leg_armor(13)|difficulty(14)|body_armor(40)|head_armor(6), imodbits_cloth, [], [fac_kingdom_2]],

	["north_stark_standard", "Heavy Leather Jerkin", [("north_stark_standard", imodbits_none)], itp_type_body_armor|itp_merchandise|itp_covers_legs|itp_doesnt_cover_hair|itp_can_penetrate_shield, 0, 500, abundance(50)|weight(10.0)|leg_armor(10)|body_armor(26)|head_armor(3), imodbits_cloth, [], [fac_kingdom_2]],

	["north_stark_guardsman", "Heavy Leather Jerkin", [("north_stark_guardsman", imodbits_none)], itp_type_body_armor|itp_merchandise|itp_covers_legs|itp_doesnt_cover_hair|itp_can_penetrate_shield, 0, 500, abundance(20)|weight(10.0)|leg_armor(10)|body_armor(26), imodbits_cloth, [], [fac_kingdom_2]],

	["north_umbar", "Umbers Heavy Leather Jerkin", [("north_umbar", imodbits_none)], itp_type_body_armor|itp_always_loot|itp_covers_legs|itp_doesnt_cover_hair|itp_can_penetrate_shield, 0, 1000, abundance(50)|weight(10.0)|leg_armor(10)|difficulty(12)|body_armor(36)|head_armor(6), imodbits_cloth, [], [fac_kingdom_1]],

	["north_umbar_cloaked", "Umbers Heavy Leather Jerkin", [("north_umbar_cloaked", imodbits_none)], itp_type_body_armor|itp_covers_legs|itp_doesnt_cover_hair|itp_can_penetrate_shield, 0, 600, abundance(50)|weight(10.0)|leg_armor(10)|body_armor(30), imodbits_cloth, [], [fac_kingdom_1]],

	["reach_loras", "Heavy Plate Armor", [("reach_loras", imodbits_none)], itp_type_body_armor|itp_covers_legs|itp_doesnt_cover_hair|itp_can_penetrate_shield, 0, 9000, abundance(5)|weight(20.0)|leg_armor(15)|difficulty(14)|body_armor(54), imodbits_plate, [], [fac_kingdom_10]],

	["reach_loras2", "Heavy Plate Armor", [("reach_loras2", imodbits_none)], itp_type_body_armor|itp_covers_legs|itp_doesnt_cover_hair|itp_can_penetrate_shield, 0, 9000, abundance(5)|weight(20.0)|leg_armor(15)|difficulty(14)|body_armor(54), imodbits_plate, [], [fac_kingdom_10]],

	["riverlands_blackfish", "Chain Mail Hauberk", [("riverlands_blackfish", imodbits_none)], itp_type_body_armor|itp_merchandise|itp_covers_legs|itp_doesnt_cover_hair|itp_can_penetrate_shield, 0, 4000, abundance(20)|weight(20.0)|leg_armor(10)|difficulty(12)|body_armor(35), imodbits_armor, [], [fac_kingdom_2]],

	["riverlands_edmure", "Edmures Chain Mail Hauberk", [("riverlands_edmure", imodbits_none)], itp_type_body_armor|itp_always_loot|itp_covers_legs|itp_doesnt_cover_hair|itp_can_penetrate_shield, 0, 2000, abundance(50)|weight(20.0)|leg_armor(10)|difficulty(12)|body_armor(35), imodbits_armor, [], [fac_kingdom_1]],

	["riverlands_frey_01", "Leather Jerkin", [("riverlands_frey_01", imodbits_none)], itp_type_body_armor|itp_merchandise|itp_covers_legs|itp_doesnt_cover_hair|itp_can_penetrate_shield, 0, 300, abundance(50)|weight(5.0)|leg_armor(6)|body_armor(22), imodbits_cloth, [], [fac_kingdom_2]],

	["riverlands_frey_01_neck", "Heavy Leather Jerkin", [("riverlands_frey_01_neck", imodbits_none)], itp_type_body_armor|itp_merchandise|itp_covers_legs|itp_doesnt_cover_hair|itp_can_penetrate_shield, 0, 500, abundance(50)|weight(5.0)|leg_armor(6)|body_armor(22)|head_armor(4), imodbits_cloth, [], [fac_kingdom_2]],

	["riverlands_frey_02", "Leather Jerkin", [("riverlands_frey_02", imodbits_none)], itp_type_body_armor|itp_merchandise|itp_covers_legs|itp_doesnt_cover_hair|itp_can_penetrate_shield, 0, 200, abundance(50)|weight(5.0)|leg_armor(6)|body_armor(22), imodbits_cloth, [], [fac_kingdom_2]],

	["riverlands_frey_02_neck", "Heavy Leather Jerkin", [("riverlands_frey_02_neck", imodbits_none)], itp_type_body_armor|itp_merchandise|itp_covers_legs|itp_doesnt_cover_hair|itp_can_penetrate_shield, 0, 500, abundance(50)|weight(5.0)|leg_armor(10)|body_armor(22)|head_armor(4), imodbits_cloth, [], [fac_kingdom_2]],

	["riverlands_heavy_no_shoulders", "Chain Mail Hauberk", [("riverlands_heavy_no_shoulders", imodbits_none)], itp_type_body_armor|itp_merchandise|itp_covers_legs|itp_doesnt_cover_hair|itp_can_penetrate_shield, 0, 3800, abundance(20)|weight(20.0)|leg_armor(10)|difficulty(12)|body_armor(37), imodbits_armor, [], [fac_kingdom_2]],

	["riverlands_heavy", "Chain Mail Hauberk", [("riverlands_heavy", imodbits_none)], itp_type_body_armor|itp_merchandise|itp_covers_legs|itp_doesnt_cover_hair|itp_can_penetrate_shield, 0, 3800, abundance(20)|weight(20.0)|leg_armor(10)|difficulty(12)|body_armor(37), imodbits_armor, [], [fac_kingdom_2]],

	["riverlands_heavy_neck", "Heavy Chain Mail Hauberk", [("riverlands_heavy_neck", imodbits_none)], itp_type_body_armor|itp_merchandise|itp_covers_legs|itp_doesnt_cover_hair|itp_can_penetrate_shield, 0, 4000, abundance(20)|weight(20.0)|leg_armor(10)|difficulty(12)|body_armor(37)|head_armor(5), imodbits_armor, [], [fac_kingdom_2]],

	["riverlands_standard_01", "Heavy Leather Jerkin", [("riverlands_standard_01", imodbits_none)], itp_type_body_armor|itp_merchandise|itp_covers_legs|itp_doesnt_cover_hair|itp_can_penetrate_shield, 0, 600, abundance(20)|weight(5.0)|leg_armor(11)|body_armor(27), imodbits_cloth, [], [fac_kingdom_2]],

	["stormlands_brienne", "Heavy Plate Armor", [("stormlands_brienne", imodbits_none)], itp_type_body_armor|itp_covers_legs|itp_doesnt_cover_hair|itp_can_penetrate_shield, 0, 9000, abundance(5)|weight(20.0)|leg_armor(5)|difficulty(14)|body_armor(54), imodbits_plate, [], [fac_kingdom_1]],

	["stormlands_brienne2", "Heavy Plate Armor", [("stormlands_brienne2", imodbits_none)], itp_type_body_armor|itp_covers_legs|itp_doesnt_cover_hair|itp_can_penetrate_shield, 0, 9000, abundance(5)|weight(20.0)|leg_armor(5)|difficulty(14)|body_armor(54), imodbits_plate, [], [fac_kingdom_1]],

	["stormlands_renly", "Renlys Reinforced Gambeson", [("stormlands_renly", imodbits_none)], itp_type_body_armor|itp_always_loot|itp_covers_legs|itp_doesnt_cover_hair|itp_can_penetrate_shield, 0, 5000, abundance(50)|weight(20.0)|leg_armor(13)|difficulty(12)|body_armor(35), imodbits_armor, [], [fac_kingdom_1]],

	["westerlands_heavy", "Light Plate Armor", [("westerlands_heavy", imodbits_none)], itp_type_body_armor|itp_merchandise|itp_covers_legs|itp_doesnt_cover_hair|itp_can_penetrate_shield, 0, 4000, abundance(20)|weight(20.0)|leg_armor(3)|difficulty(12)|body_armor(37), imodbits_armor, [], [fac_kingdom_9]],

	["westerlands_heavy_lord", "Tywins Heavy Plate Armor", [("westerlands_heavy_lord", imodbits_none)], itp_type_body_armor|itp_covers_legs|itp_doesnt_cover_hair|itp_can_penetrate_shield, 0, 9000, abundance(5)|weight(20.0)|leg_armor(3)|difficulty(14)|body_armor(54), imodbits_plate, [], [fac_kingdom_1]],

	["westerlands_heavy_standard", "Light Plate Armor", [("westerlands_heavy_standard", imodbits_none)], itp_type_body_armor|itp_merchandise|itp_covers_legs|itp_doesnt_cover_hair|itp_can_penetrate_shield, 0, 4000, abundance(20)|weight(20.0)|leg_armor(10)|difficulty(12)|body_armor(40), imodbits_armor, [], [fac_kingdom_9]],

	["westerlands_hound", "Light Plate Armor", [("westerlands_hound", imodbits_none)], itp_type_body_armor|itp_merchandise|itp_covers_legs|itp_doesnt_cover_hair|itp_can_penetrate_shield, 0, 4200, abundance(20)|weight(20.0)|leg_armor(10)|difficulty(14)|body_armor(40), imodbits_armor, [], [fac_kingdom_1, fac_kingdom_3, fac_kingdom_5, fac_kingdom_8, fac_kingdom_9, fac_kingdom_10]],

	["westerlands_king", "Heavy Plate Armor", [("westerlands_king", imodbits_none)], itp_type_body_armor|itp_always_loot|itp_covers_legs|itp_doesnt_cover_hair|itp_can_penetrate_shield, 0, 9000, abundance(5)|weight(20.0)|leg_armor(8)|difficulty(14)|body_armor(46), imodbits_plate, [], [fac_kingdom_1]],

	["westerlands_lord_1", "Light Plate Armor", [("westerlands_lord_1", imodbits_none)], itp_type_body_armor|itp_merchandise|itp_covers_legs|itp_doesnt_cover_hair|itp_can_penetrate_shield, 0, 4000, abundance(20)|weight(20.0)|leg_armor(10)|difficulty(12)|body_armor(40), imodbits_armor, [], [fac_kingdom_9]],

	["westerlands_lord_2", "Light Plate Armor", [("westerlands_lord_2", imodbits_none)], itp_type_body_armor|itp_merchandise|itp_covers_legs|itp_doesnt_cover_hair|itp_can_penetrate_shield, 0, 4000, abundance(20)|weight(20.0)|leg_armor(10)|difficulty(12)|body_armor(40), imodbits_armor, [], [fac_kingdom_9]],

	["westerlands_light_01", "Leather Jerkin", [("westerlands_light_01", imodbits_none)], itp_type_body_armor|itp_merchandise|itp_covers_legs|itp_doesnt_cover_hair|itp_can_penetrate_shield, 0, 350, abundance(50)|weight(5.0)|body_armor(24), imodbits_cloth, [], [fac_kingdom_9]],

	["westerlands_light_02", "Leather Jerkin", [("westerlands_light_02", imodbits_none)], itp_type_body_armor|itp_merchandise|itp_covers_legs|itp_doesnt_cover_hair|itp_can_penetrate_shield, 0, 350, abundance(50)|weight(5.0)|body_armor(24), imodbits_cloth, [], [fac_kingdom_9]],

	["westerlands_polliver_01", "Heavy Plated Leather Jerkin", [("westerlands_polliver_01", imodbits_none)], itp_type_body_armor|itp_merchandise|itp_covers_legs|itp_doesnt_cover_hair|itp_can_penetrate_shield, 0, 1500, abundance(20)|weight(20.0)|leg_armor(10)|difficulty(12)|body_armor(37), imodbits_cloth, [], [fac_kingdom_9]],

	["westerlands_polliver_02", "Heavy Leather Jerkin", [("westerlands_polliver_02", imodbits_none)], itp_type_body_armor|itp_merchandise|itp_covers_legs|itp_doesnt_cover_hair|itp_can_penetrate_shield, 0, 1000, abundance(20)|weight(10.0)|leg_armor(10)|difficulty(12)|body_armor(35), imodbits_cloth, [], [fac_kingdom_9]],

	["dragonstone_stannis", "Chain Mail Hauberk", [("dragonstone_stannis", imodbits_none)], itp_type_body_armor|itp_always_loot|itp_covers_legs|itp_doesnt_cover_hair|itp_can_penetrate_shield, 0, 4400, abundance(20)|weight(20.0)|leg_armor(10)|difficulty(12)|body_armor(40), imodbits_armor, [], [fac_kingdom_1]],

	["westerland_helm", "Lannister Helmet", [("westerland_helm", imodbits_none)], itp_type_head_armor|itp_fit_to_head|itp_offset_lance, 0, 1400, abundance(20)|weight(4.0)|difficulty(10)|head_armor(33), imodbits_plate, [], [fac_kingdom_1, fac_kingdom_2, fac_kingdom_3, fac_kingdom_5, fac_kingdom_8]],

	["goldcloak_helm", "Gold Cloak Helmet", [("goldcloak_helm", imodbits_none)], itp_type_head_armor|itp_fit_to_head|itp_offset_lance, 0, 1000, abundance(50)|weight(4.0)|difficulty(10)|head_armor(33), imodbits_plate, [], [fac_kingdom_1, fac_kingdom_2, fac_kingdom_3, fac_kingdom_5, fac_kingdom_8]],

	["kingsguard_helm", "Kingsguard Helmet", [("kingsguard_helm", imodbits_none)], itp_type_head_armor|itp_civilian|itp_next_item_as_melee|itp_fit_to_head|itp_offset_lance, 0, 10, abundance(50)|weight(4.0)|difficulty(10)|head_armor(33), imodbits_none, [], [fac_kingdom_1, fac_kingdom_2, fac_kingdom_3, fac_kingdom_5, fac_kingdom_8]],

	["armor_baratheon", "Heavy Plate Armor", [("Armor_Baratheon", imodbits_none)], itp_type_body_armor|itp_merchandise|itp_covers_legs|itp_doesnt_cover_hair|itp_can_penetrate_shield, 0, 9000, abundance(5)|weight(25.0)|leg_armor(15)|difficulty(14)|body_armor(54), imodbits_armor, [], [fac_kingdom_8]],

	["bnw_armour_slashed", "Light Plate Armor", [("bnw_armour_slashed", imodbits_none)], itp_type_body_armor|itp_merchandise|itp_covers_legs|itp_doesnt_cover_hair|itp_can_penetrate_shield, 0, 3000, abundance(50)|weight(20.0)|difficulty(12)|body_armor(35), imodbits_armor, [], [fac_kingdom_4]],

	["bnw_armour_slashed_full", "Light Plate Armor", [("bnw_armour_slashed_full", imodbits_none)], itp_type_body_armor|itp_merchandise|itp_covers_legs|itp_doesnt_cover_hair|itp_can_penetrate_shield, 0, 4300, abundance(20)|weight(50.0)|leg_armor(6)|difficulty(12)|body_armor(35), imodbits_armor, [], [fac_kingdom_4]],

	["bnw_armour_stripes", "Light Plate Armor", [("bnw_armour_stripes", imodbits_none)], itp_type_body_armor|itp_merchandise|itp_covers_legs|itp_doesnt_cover_hair|itp_can_penetrate_shield, 0, 3000, abundance(50)|weight(20.0)|difficulty(12)|body_armor(35), imodbits_armor, [], [fac_kingdom_4]],

	["bnw_armour_stripes_full", "Light Plate Armor", [("bnw_armour_stripes_full", imodbits_none)], itp_type_body_armor|itp_merchandise|itp_covers_legs|itp_doesnt_cover_hair|itp_can_penetrate_shield, 0, 4300, abundance(20)|weight(50.0)|leg_armor(6)|difficulty(12)|body_armor(35), imodbits_armor, [], [fac_kingdom_4]],

	["pollivers_armor", "Pollivers Armor", [("westerlands_polliver_01", imodbits_none)], itp_type_body_armor|itp_covers_legs|itp_doesnt_cover_hair|itp_can_penetrate_shield|itp_civilian|itp_next_item_as_melee, 0, 100, abundance(55)|weight(5.0)|leg_armor(5)|body_armor(5), imodbits_cloth, [], [fac_kingdom_13, fac_kingdom_14, fac_kingdom_15, fac_kingdom_16]],

	["chiswycks_armor", "Chiswycks Armor", [("westerlands_light_01", imodbits_none)], itp_type_body_armor|itp_covers_legs|itp_doesnt_cover_hair|itp_can_penetrate_shield|itp_civilian|itp_next_item_as_melee, 0, 100, abundance(55)|weight(5.0)|leg_armor(5)|body_armor(5), imodbits_cloth, [], [fac_kingdom_13, fac_kingdom_14, fac_kingdom_15, fac_kingdom_16]],

	["dunsens_armor", "Dunsens Armor", [("westerlands_light_02", imodbits_none)], itp_type_body_armor|itp_covers_legs|itp_doesnt_cover_hair|itp_can_penetrate_shield|itp_civilian|itp_next_item_as_melee, 0, 100, abundance(55)|weight(5.0)|leg_armor(5)|body_armor(5), imodbits_cloth, [], [fac_kingdom_13, fac_kingdom_14, fac_kingdom_15, fac_kingdom_16]],

	["raffords_armor", "Raffords Armor", [("riverlands_freyheavy", imodbits_none)], itp_type_body_armor|itp_covers_legs|itp_doesnt_cover_hair|itp_can_penetrate_shield|itp_civilian|itp_next_item_as_melee, 0, 100, abundance(55)|weight(5.0)|leg_armor(5)|body_armor(5), imodbits_cloth, [], [fac_kingdom_13, fac_kingdom_14, fac_kingdom_15, fac_kingdom_16]],

	["ticklers_armor", "Ticklers Armor", [("sellsword_jerkin", imodbits_none)], itp_type_body_armor|itp_covers_legs|itp_doesnt_cover_hair|itp_can_penetrate_shield|itp_civilian|itp_next_item_as_melee, 0, 100, abundance(55)|weight(5.0)|leg_armor(5)|body_armor(5), imodbits_cloth, [], [fac_kingdom_13, fac_kingdom_14, fac_kingdom_15, fac_kingdom_16]],

	["coldbringer", "Coldbringer", [("fi_decorated_mace_2", imodbits_none)], itp_type_two_handed_wpn|itp_two_handed|itp_primary|itp_bonus_against_shield|itp_cant_use_on_horseback|itp_crush_through|itp_can_knock_down, itcf_carry_axe_back|itc_nodachi, 20000, thrust_damage(0, pierce)|hit_points(50176)|spd_rtng(70)|abundance(100)|weight(4.0)|swing_damage(49, blunt)|difficulty(12)|weapon_length(95), imodbits_none, [], [fac_kingdom_1, fac_kingdom_2, fac_kingdom_3, fac_kingdom_5, fac_kingdom_8]],

	["fi_lowlander_sword", "Great Sword", [("fi_lowlander_sword", imodbits_none)], itp_type_two_handed_wpn|itp_two_handed|itp_primary|itp_covers_legs|itp_doesnt_cover_hair|itp_can_penetrate_shield|itp_bonus_against_shield|itp_cant_use_on_horseback|itp_can_knock_down, itcf_carry_sword_back|itc_greatsword, 2000, thrust_damage(45, pierce)|hit_points(40960)|spd_rtng(90)|abundance(80)|weight(6.0)|swing_damage(40, cut)|difficulty(12)|weapon_length(113), imodbits_none, [], [fac_kingdom_1, fac_kingdom_8, fac_kingdom_9, fac_kingdom_10, fac_kingdom_20]],

	["ssh_huscarl_armour", "Victarions Heavy Plate Armor", [("ssh_huscarl_armour", imodbits_none)], itp_type_body_armor|itp_covers_legs|itp_doesnt_cover_hair|itp_can_penetrate_shield, 0, 6000, abundance(40)|weight(58.0)|leg_armor(18)|difficulty(14)|body_armor(54), imodbits_none, [], [fac_kingdom_10]],

	["kraken_mask", "Kraken Helmet", [("kraken_mask", imodbits_none)], itp_type_head_armor|itp_fit_to_head|itp_offset_lance|itp_covers_beard, 0, 2000, abundance(50)|weight(1.0)|difficulty(12)|head_armor(40), imodbits_plate, [], [fac_kingdom_12, fac_kingdom_17, fac_kingdom_5, fac_kingdom_18]],

	["xenoargh_round_shield01", "Round Wooden Shield", [("xenoargh_round_shield01", imodbits_none)], itp_type_shield|itp_merchandise|itp_wooden_parry, itcf_carry_round_shield, 200, hit_points(160)|spd_rtng(87)|abundance(60)|weight(5.0)|shield_width(76)|body_armor(5), imodbits_none],

	["west_man_at_arms_armor", "Heavy Plate Armor", [("west_man_at_arms_armor", imodbits_none)], itp_type_body_armor|itp_merchandise|itp_covers_legs|itp_doesnt_cover_hair|itp_can_penetrate_shield, 0, 8000, abundance(5)|weight(25.0)|leg_armor(15)|difficulty(14)|body_armor(54), imodbits_plate, [], [fac_kingdom_20]],

	["goplon1", "Round Bronze Shield", [("goplon1", imodbits_none)], itp_type_shield|itp_merchandise, itcf_carry_round_shield, 500, hit_points(250)|spd_rtng(87)|abundance(60)|weight(5.0)|shield_width(78)|difficulty(2)|body_armor(15), imodbits_none, [], [fac_kingdom_16]],

	["mackie_strange_sword", "Curved Great Sword", [("mackie_strange_sword", imodbits_none)], itp_type_two_handed_wpn|itp_merchandise|itp_two_handed|itp_primary|itp_bonus_against_shield|itp_cant_use_on_horseback, itcf_carry_sword_back|itc_nodachi, 2000, hit_points(45056)|spd_rtng(100)|abundance(20)|weight(7.0)|swing_damage(44, cut)|difficulty(15)|weapon_length(104), imodbits_sword, [], [fac_kingdom_13, fac_kingdom_14, fac_kingdom_15, fac_kingdom_16]],

	["arakh", "Arakh", [("arakh", imodbits_none)], itp_type_two_handed_wpn|itp_merchandise|itp_two_handed|itp_primary, itcf_carry_sword_back|itc_nodachi, 1500, hit_points(36864)|spd_rtng(100)|abundance(30)|weight(5.0)|swing_damage(36, cut)|difficulty(10)|weapon_length(78), imodbits_none, [], [fac_kingdom_13, fac_kingdom_14, fac_kingdom_15, fac_kingdom_16, fac_kingdom_17, fac_kingdom_5]],

	["short_arakh", "Arakh", [("short_arakh", imodbits_none)], itp_type_one_handed_wpn|itp_merchandise|itp_primary, itcf_carry_sword_left_hip|itc_scimitar, 800, hit_points(28672)|spd_rtng(115)|abundance(20)|weight(3.0)|swing_damage(28, cut)|difficulty(10)|weapon_length(52), imodbits_none, [], [fac_kingdom_13, fac_kingdom_14, fac_kingdom_15, fac_kingdom_16, fac_kingdom_17, fac_kingdom_5]],

	["tyrions_armor", "Tyrions Armor", [("westerlands_light_02", imodbits_none)], itp_type_body_armor|itp_covers_legs|itp_doesnt_cover_hair|itp_can_penetrate_shield|itp_civilian|itp_next_item_as_melee, 0, 2, abundance(50)|weight(5.0)|body_armor(2), imodbits_cloth, [], [fac_kingdom_3, fac_kingdom_8]],

	["joffreys_armor", "Joffreys Armor", [("westerlands_king", imodbits_none)], itp_type_body_armor|itp_covers_legs|itp_doesnt_cover_hair|itp_can_penetrate_shield|itp_civilian|itp_next_item_as_melee, 0, 2, abundance(50)|weight(5.0)|body_armor(2), imodbits_cloth, [], [fac_kingdom_3, fac_kingdom_8]],

	["witcher_heater_7", "Heater Shield", [("witcher_heater_7", imodbits_none)], itp_type_shield|itp_wooden_parry, itcf_carry_kite_shield, 250, hit_points(200)|spd_rtng(76)|abundance(60)|weight(4.0)|shield_width(50)|shield_height(64)|body_armor(5), imodbits_shield, [], [fac_kingdom_1, fac_kingdom_3, fac_kingdom_8, fac_kingdom_9, fac_kingdom_10]],

	["nw_heater_shield", "Heater Shield", [("nw_heater_shield", imodbits_none)], itp_type_shield|itp_wooden_parry, itcf_carry_kite_shield, 250, hit_points(200)|spd_rtng(76)|abundance(60)|weight(4.0)|shield_width(50)|shield_height(64)|body_armor(5), imodbits_shield, [], [fac_kingdom_12, fac_kingdom_17, fac_kingdom_5, fac_kingdom_18]],

	["witcher_worn_shield", "Round Wooden Shield", [("witcher_worn_shield", imodbits_none)], itp_type_shield|itp_wooden_parry, itcf_carry_round_shield, 200, hit_points(130)|spd_rtng(87)|abundance(60)|weight(5.0)|shield_width(50)|body_armor(2), imodbits_none],

	["xenoargh_shield_kite01_06", "Kite Shield", [("xenoargh_shield_kite01_06", imodbits_none)], itp_type_shield|itp_merchandise|itp_wooden_parry, itcf_carry_kite_shield, 300, hit_points(200)|spd_rtng(76)|abundance(60)|weight(4.0)|shield_width(36)|shield_height(70)|body_armor(10), imodbits_shield, [], [fac_kingdom_1, fac_kingdom_2, fac_kingdom_8]],

	["xenoargh_tableau_shield_heater_1", "Heater Shield", [("xenoargh_tableau_shield_heater_1", imodbits_none)], itp_type_shield|itp_merchandise|itp_wooden_parry, itcf_carry_kite_shield, 300, hit_points(200)|spd_rtng(76)|abundance(60)|weight(4.0)|shield_width(36)|shield_height(70)|body_armor(10), imodbits_shield, [], [fac_kingdom_3]],

	["golden_company_shield", "Kite Shield", [("golden_company_shield", imodbits_none)], itp_type_shield|itp_wooden_parry, itcf_carry_kite_shield, 300, hit_points(200)|spd_rtng(76)|abundance(60)|weight(4.0)|shield_width(36)|shield_height(70)|body_armor(10), imodbits_shield, [], [fac_kingdom_1, fac_kingdom_2, fac_kingdom_8]],

	["xenoargh_shield_pavise_1", "Pavise", [("xenoargh_shield_pavise_1", imodbits_none)], itp_type_shield|itp_merchandise|itp_wooden_parry|itp_cant_use_on_horseback, itcf_carry_board_shield, 380, hit_points(220)|spd_rtng(76)|abundance(60)|weight(4.0)|shield_width(43)|shield_height(100)|body_armor(15), imodbits_shield, [], [fac_kingdom_1, fac_kingdom_9, fac_kingdom_10]],

	["xenoargh_shield_pavise_2", "Pavise", [("xenoargh_shield_pavise_2", imodbits_none)], itp_type_shield|itp_merchandise|itp_wooden_parry|itp_cant_use_on_horseback, itcf_carry_board_shield, 380, hit_points(220)|spd_rtng(76)|abundance(60)|weight(4.0)|shield_width(43)|shield_height(100)|body_armor(15), imodbits_shield, [], [fac_kingdom_1, fac_kingdom_9, fac_kingdom_10]],

	["xenoargh_round_shield02", "Round Wooden Shield", [("xenoargh_round_shield02", imodbits_none)], itp_type_shield|itp_merchandise|itp_wooden_parry, itcf_carry_round_shield, 200, hit_points(180)|spd_rtng(87)|abundance(60)|weight(5.0)|shield_width(76)|body_armor(5), imodbits_none],

	["xenoargh_round_shield03_06", "Round Leather Shield", [("xenoargh_round_shield03_06", imodbits_none)], itp_type_shield|itp_merchandise|itp_wooden_parry, itcf_carry_round_shield, 200, hit_points(180)|spd_rtng(87)|abundance(60)|weight(5.0)|shield_width(76)|body_armor(5), imodbits_none],

	["stark_shield", "Round Steel Shield", [("stark_shield", imodbits_none)], itp_type_shield, itcf_carry_round_shield, 500, hit_points(250)|spd_rtng(87)|abundance(60)|weight(5.0)|shield_width(65)|difficulty(2)|body_armor(15), imodbits_none],

	["alen_cargylls_hauberk", "Alen Cargylls Surcoat", [("surcoat_new_cargyll", imodbits_none)], itp_type_body_armor|itp_covers_legs|itp_doesnt_cover_hair|itp_can_penetrate_shield, 0, 500, abundance(55)|weight(20.0)|leg_armor(5)|difficulty(12)|body_armor(35), imodbits_none, [], [fac_kingdom_12, fac_kingdom_17, fac_kingdom_5, fac_kingdom_18]],

	["wide_toga_1", "Toga", [("kuauik_mace_style_3", imodbits_none)], itp_type_body_armor|itp_covers_legs|itp_doesnt_cover_hair|itp_can_penetrate_shield|itp_civilian|itp_next_item_as_melee, 0, 2, abundance(50)|weight(5.0)|body_armor(2), imodbits_cloth, [], [fac_kingdom_3, fac_kingdom_8]],

	["reznak_robe_1", "Ghiscari Dress", [("reznak_robe_1", imodbits_none)], itp_type_body_armor|itp_covers_legs|itp_doesnt_cover_hair|itp_can_penetrate_shield|itp_civilian|itp_next_item_as_melee, 0, 2, abundance(50)|weight(5.0)|body_armor(2), imodbits_cloth, [], [fac_kingdom_3, fac_kingdom_8]],

	["grazdan_robe_1", "Ghiscari Dress", [("grazdan_robe_1", imodbits_none)], itp_type_body_armor|itp_covers_legs|itp_doesnt_cover_hair|itp_can_penetrate_shield|itp_civilian|itp_next_item_as_melee, 0, 2, abundance(50)|weight(5.0)|body_armor(2), imodbits_cloth, [], [fac_kingdom_3, fac_kingdom_8]],

	["hizdahr_robe_1", "Ghiscari Dress", [("hizdahr_robe_1", imodbits_none)], itp_type_body_armor|itp_covers_legs|itp_doesnt_cover_hair|itp_can_penetrate_shield|itp_civilian|itp_next_item_as_melee, 0, 2, abundance(50)|weight(5.0)|body_armor(2), imodbits_cloth, [], [fac_kingdom_3, fac_kingdom_8]],

	["galazza_robe_1", "Ghiscari Dress", [("galazza_robe_1", imodbits_none)], itp_type_body_armor|itp_covers_legs|itp_doesnt_cover_hair|itp_can_penetrate_shield|itp_civilian|itp_next_item_as_melee, 0, 2, abundance(50)|weight(5.0)|body_armor(2), imodbits_cloth, [], [fac_kingdom_3, fac_kingdom_8]],

	["yunkai_robe_1", "Ghiscari Dress", [("yunkai_robe_1", imodbits_none)], itp_type_body_armor|itp_covers_legs|itp_doesnt_cover_hair|itp_can_penetrate_shield|itp_civilian|itp_next_item_as_melee, 0, 2, abundance(50)|weight(5.0)|body_armor(2), imodbits_cloth, [], [fac_kingdom_3, fac_kingdom_8]],

	["yunkai_robe_2", "Ghiscari Dress", [("yunkai_robe_2", imodbits_none)], itp_type_body_armor|itp_covers_legs|itp_doesnt_cover_hair|itp_can_penetrate_shield|itp_civilian|itp_next_item_as_melee, 0, 2, abundance(50)|weight(5.0)|body_armor(2), imodbits_cloth, [], [fac_kingdom_3, fac_kingdom_8]],

	["kuauik_vale_style_1", "Ghiscari Tunic", [("kuauik_vale_style_1", imodbits_none)], itp_type_body_armor|itp_covers_legs|itp_doesnt_cover_hair|itp_can_penetrate_shield|itp_civilian|itp_next_item_as_melee, 0, 2, abundance(50)|weight(5.0)|body_armor(2), imodbits_cloth, [], [fac_kingdom_3, fac_kingdom_8]],

	["kuauik_mace_style_1", "Ghiscari Tunic", [("kuauik_mace_style_1", imodbits_none)], itp_type_body_armor|itp_covers_legs|itp_doesnt_cover_hair|itp_can_penetrate_shield|itp_civilian|itp_next_item_as_melee, 0, 2, abundance(50)|weight(5.0)|body_armor(2), imodbits_cloth, [], [fac_kingdom_3, fac_kingdom_8]],

	["kuauik_mace_style_2", "Ghiscari Tunic", [("kuauik_mace_style_2", imodbits_none)], itp_type_body_armor|itp_covers_legs|itp_doesnt_cover_hair|itp_can_penetrate_shield|itp_civilian|itp_next_item_as_melee, 0, 2, abundance(50)|weight(5.0)|body_armor(2), imodbits_cloth, [], [fac_kingdom_3, fac_kingdom_8]],

	["kuauik_mace_style_3", "Ghiscari Tunic", [("kuauik_mace_style_3", imodbits_none)], itp_type_body_armor|itp_covers_legs|itp_doesnt_cover_hair|itp_can_penetrate_shield|itp_civilian|itp_next_item_as_melee, 0, 2, abundance(50)|weight(5.0)|body_armor(2), imodbits_cloth, [], [fac_kingdom_3, fac_kingdom_8]],

	["kingsguard_armor_quest", "Kingsguard Heavy Armor", [("westerland_kingsguard", imodbits_none)], itp_type_body_armor|itp_covers_legs|itp_doesnt_cover_hair|itp_can_penetrate_shield, 0, 3000, abundance(55)|weight(20.0)|leg_armor(5)|difficulty(12)|body_armor(37), imodbits_none, [], [fac_kingdom_12, fac_kingdom_17, fac_kingdom_5, fac_kingdom_18]],

	["kingsguard_helm_quest", "Kingsguard Helmet", [("kingsguard_helm", imodbits_none)], itp_type_head_armor|itp_fit_to_head|itp_offset_lance, 0, 1000, abundance(50)|weight(4.0)|difficulty(10)|head_armor(33), imodbits_none, [], [fac_kingdom_4]],

	["nord_dress_common_b", "Peasants Dress", [("nord_dress_common_b", imodbits_none)], itp_type_body_armor|itp_covers_legs|itp_doesnt_cover_hair|itp_can_penetrate_shield|itp_civilian|itp_next_item_as_melee, 0, 50, abundance(55)|weight(2.0)|leg_armor(1)|body_armor(5), imodbits_cloth],

	["rhodok_dress_common_b", "Peasants Dress", [("rhodok_dress_common_b", imodbits_none)], itp_type_body_armor|itp_covers_legs|itp_doesnt_cover_hair|itp_can_penetrate_shield|itp_civilian|itp_next_item_as_melee, 0, 50, abundance(55)|weight(2.0)|leg_armor(1)|body_armor(5), imodbits_cloth],

	["sarranid_dress_common_a", "Peasants Dress", [("sarranid_dress_common_a", imodbits_none)], itp_type_body_armor|itp_covers_legs|itp_doesnt_cover_hair|itp_can_penetrate_shield|itp_civilian|itp_next_item_as_melee, 0, 50, abundance(55)|weight(2.0)|leg_armor(1)|body_armor(5), imodbits_cloth],

	["sarranid_dress_common_b", "Peasants Dress", [("sarranid_dress_common_b", imodbits_none)], itp_type_body_armor|itp_covers_legs|itp_doesnt_cover_hair|itp_can_penetrate_shield|itp_civilian|itp_next_item_as_melee, 0, 50, abundance(55)|weight(2.0)|leg_armor(1)|body_armor(5), imodbits_cloth],

	["aemonds_helmet", "Aemond Targaryens Hounskull Helmet", [("aemonds_helmet", imodbits_none)], itp_type_head_armor, 0, 2000, abundance(20)|weight(5.0)|difficulty(14)|head_armor(24), imodbits_none, [], [fac_kingdom_1, fac_kingdom_3, fac_kingdom_5, fac_kingdom_8, fac_kingdom_9, fac_kingdom_10]],

	["aemonds_boots", "Aemond Targaryens Plate Boots", [("aemonds_boots", imodbits_none)], itp_type_foot_armor|itp_attach_armature|itp_attachment_mask, 0, 2000, abundance(40)|weight(3.0)|leg_armor(20)|difficulty(14), imodbits_none, [], [fac_kingdom_1, fac_kingdom_8, fac_kingdom_9, fac_kingdom_10, fac_kingdom_20]],

	["aemonds_armor", "Aemond Targaryens Heavy Plate Armor", [("aemonds_armor", imodbits_none)], itp_type_body_armor|itp_covers_legs|itp_doesnt_cover_hair|itp_can_penetrate_shield|itp_civilian|itp_next_item_as_melee, 0, 3000, abundance(10)|weight(4.0)|leg_armor(8)|difficulty(14)|body_armor(33), imodbits_cloth, [], [fac_kingdom_12, fac_kingdom_13, fac_kingdom_14, fac_kingdom_15, fac_kingdom_16, fac_kingdom_17, fac_kingdom_5, fac_kingdom_18]],

	["fi_estoc", "Braavosi Long Sword", [("fi_estoc", imodbits_none)], itp_type_two_handed_wpn|itp_two_handed|itp_primary, itcf_thrust_twohanded|itcf_carry_sword_back|itc_dagger|itc_nodachi, 1000, thrust_damage(44, pierce)|hit_points(30720)|spd_rtng(110)|abundance(10)|weight(6.0)|swing_damage(30, cut)|difficulty(12)|weapon_length(118), imodbits_none, [], [fac_kingdom_1, fac_kingdom_8, fac_kingdom_9, fac_kingdom_10, fac_kingdom_20]],

	["hoggox", "One-Handed Axe", [("hoggox", imodbits_none)], itp_type_one_handed_wpn|itp_merchandise|itp_wooden_parry|itp_primary|itp_secondary, itcf_carry_axe_left_hip|itc_scimitar, 500, thrust_damage(0, pierce)|hit_points(30720)|spd_rtng(100)|abundance(10)|weight(2.0)|swing_damage(30, cut)|difficulty(8)|weapon_length(48), imodbits_axe|imodbits_mace],

	["slim_axe", "One-Handed Axe", [("slim_axe", imodbits_none)], itp_type_one_handed_wpn|itp_merchandise|itp_wooden_parry|itp_primary|itp_secondary, itcf_carry_axe_left_hip|itc_scimitar, 300, thrust_damage(0, pierce)|hit_points(27648)|spd_rtng(105)|abundance(10)|weight(2.0)|swing_damage(27, cut)|difficulty(8)|weapon_length(61), imodbits_axe|imodbits_mace],

	["heavy_cutting_axe", "One-Handed Axe", [("heavy_cutting_axe", imodbits_none)], itp_type_one_handed_wpn|itp_merchandise|itp_wooden_parry|itp_primary|itp_secondary, itcf_carry_axe_left_hip|itc_scimitar, 600, thrust_damage(0, pierce)|hit_points(32768)|spd_rtng(100)|abundance(10)|weight(2.0)|swing_damage(32, cut)|difficulty(8)|weapon_length(48), imodbits_axe|imodbits_mace],

	["axe_e", "One-Handed Axe", [("axe_e", imodbits_none)], itp_type_one_handed_wpn|itp_merchandise|itp_wooden_parry|itp_primary|itp_secondary, itcf_carry_axe_left_hip|itc_scimitar, 600, thrust_damage(0, pierce)|hit_points(32768)|spd_rtng(100)|abundance(10)|weight(2.0)|swing_damage(32, cut)|difficulty(8)|weapon_length(48), imodbits_axe|imodbits_mace],

	["axe_f", "One-Handed Axe", [("axe_f", imodbits_none)], itp_type_one_handed_wpn|itp_merchandise|itp_wooden_parry|itp_primary|itp_secondary, itcf_carry_axe_left_hip|itc_scimitar, 600, thrust_damage(0, pierce)|hit_points(32768)|spd_rtng(100)|abundance(10)|weight(2.0)|swing_damage(32, cut)|difficulty(8)|weapon_length(52), imodbits_axe|imodbits_mace],

	["winters_frying_pan", "Frying Pan", [("winters_frying_pan", imodbits_none)], itp_type_one_handed_wpn|itp_no_parry|itp_primary|itp_secondary, itc_scimitar, 10, thrust_damage(0, pierce)|hit_points(7168)|spd_rtng(100)|abundance(50)|weight(2.0)|swing_damage(7, blunt)|difficulty(8)|weapon_length(30), imodbits_axe|imodbits_mace],

	["bearded_axe", "One-Handed Axe", [("bearded_axe", imodbits_none)], itp_type_one_handed_wpn|itp_merchandise|itp_wooden_parry|itp_primary|itp_secondary, itcf_carry_axe_left_hip|itc_scimitar, 500, thrust_damage(0, pierce)|hit_points(30720)|spd_rtng(100)|abundance(10)|weight(2.0)|swing_damage(30, cut)|difficulty(8)|weapon_length(52), imodbits_axe|imodbits_mace],

	["long_danox", "Two-Handed Axe", [("long_danox", imodbits_none)], itp_type_two_handed_wpn|itp_merchandise|itp_wooden_parry|itp_two_handed|itp_primary|itp_covers_legs|itp_doesnt_cover_hair|itp_can_penetrate_shield|itp_bonus_against_shield|itp_cant_use_on_horseback, itcf_carry_axe_back|itc_nodachi, 800, thrust_damage(0, pierce)|hit_points(37888)|spd_rtng(85)|abundance(1)|weight(6.0)|swing_damage(37, cut)|difficulty(12)|weapon_length(109), imodbits_axe|imodbits_mace, [], [fac_kingdom_2, fac_kingdom_3, fac_kingdom_5, fac_kingdom_11, fac_kingdom_19]],

	["fi_broad_axe", "Two-Handed Axe", [("fi_broad_axe", imodbits_none)], itp_type_two_handed_wpn|itp_wooden_parry|itp_two_handed|itp_primary|itp_covers_legs|itp_doesnt_cover_hair|itp_can_penetrate_shield|itp_bonus_against_shield|itp_cant_use_on_horseback|itp_crush_through, itcf_carry_axe_back|itc_nodachi, 1000, thrust_damage(0, pierce)|hit_points(40960)|spd_rtng(75)|abundance(5)|weight(6.0)|swing_damage(40, cut)|difficulty(12)|weapon_length(78), imodbits_axe|imodbits_mace],

	["fi_claymore", "Great Sword", [("fi_claymore", imodbits_none)], itp_type_two_handed_wpn|itp_two_handed|itp_primary|itp_covers_legs|itp_doesnt_cover_hair|itp_can_penetrate_shield|itp_bonus_against_shield|itp_cant_use_on_horseback|itp_can_knock_down, itcf_carry_sword_back|itc_greatsword, 1300, thrust_damage(44, pierce)|hit_points(43008)|spd_rtng(90)|abundance(10)|weight(6.0)|swing_damage(42, cut)|difficulty(12)|weapon_length(126), imodbits_none, [], [fac_kingdom_1, fac_kingdom_8, fac_kingdom_9, fac_kingdom_10, fac_kingdom_20]],

	["sar_helmet1", "Top Helmet", [("sar_helmet1", imodbits_none)], itp_type_head_armor|itp_merchandise|itp_fit_to_head|itp_offset_lance, 0, 1000, abundance(10)|weight(4.0)|head_armor(25), imodbits_plate, [], [fac_kingdom_12, fac_kingdom_13, fac_kingdom_14, fac_kingdom_15, fac_kingdom_16, fac_kingdom_17, fac_kingdom_5, fac_kingdom_18]],

	["sar_helmet2", "Top Helmet", [("sar_helmet2", imodbits_none)], itp_type_head_armor|itp_merchandise|itp_fit_to_head|itp_offset_lance, 0, 1000, abundance(10)|weight(4.0)|head_armor(25), imodbits_plate, [], [fac_kingdom_12, fac_kingdom_13, fac_kingdom_14, fac_kingdom_15, fac_kingdom_16, fac_kingdom_17, fac_kingdom_5, fac_kingdom_18]],

	["tuareg_helmet", "Top Helmet", [("tuareg_helmet", imodbits_none)], itp_type_head_armor|itp_merchandise|itp_fit_to_head|itp_offset_lance, 0, 1000, abundance(10)|weight(4.0)|difficulty(12)|head_armor(25), imodbits_plate, [], [fac_kingdom_12, fac_kingdom_13, fac_kingdom_14, fac_kingdom_15, fac_kingdom_16, fac_kingdom_17, fac_kingdom_5, fac_kingdom_18]],

	["tuareg", "Headcloth", [("tuareg", imodbits_none)], itp_type_head_armor|itp_merchandise|itp_fit_to_head|itp_offset_lance, 0, 200, abundance(10)|weight(4.0)|head_armor(13), imodbits_plate, [], [fac_kingdom_12, fac_kingdom_13, fac_kingdom_14, fac_kingdom_15, fac_kingdom_16, fac_kingdom_17, fac_kingdom_5, fac_kingdom_18]],

	["tuareg_open", "Headcloth", [("tuareg_open", imodbits_none)], itp_type_head_armor|itp_merchandise|itp_fit_to_head|itp_offset_lance, 0, 200, abundance(10)|weight(4.0)|head_armor(13), imodbits_plate, [], [fac_kingdom_12, fac_kingdom_13, fac_kingdom_14, fac_kingdom_15, fac_kingdom_16, fac_kingdom_17, fac_kingdom_5, fac_kingdom_18]],

	["dunland_antleraxe", "One-Handed Antler Axe", [("dunland_antleraxe", imodbits_none)], itp_type_one_handed_wpn|itp_merchandise|itp_wooden_parry|itp_primary|itp_secondary, itcf_carry_axe_left_hip|itc_scimitar, 100, thrust_damage(0, pierce)|hit_points(18432)|spd_rtng(95)|abundance(20)|weight(2.0)|swing_damage(18, cut)|difficulty(8)|weapon_length(61), imodbits_axe|imodbits_mace, [], [fac_kingdom_21]],

	["dunland_spear", "Bone Spear", [("dunland_spear", imodbits_none)], itp_type_polearm|itp_merchandise|itp_wooden_parry|itp_two_handed|itp_primary|itp_covers_legs|itp_doesnt_cover_hair|itp_can_penetrate_shield|itp_bonus_against_shield|itp_crush_through|itp_can_knock_down, itcf_carry_spear|itc_staff, 100, thrust_damage(23, pierce)|hit_points(15360)|spd_rtng(125)|abundance(20)|weight(4.0)|swing_damage(15, cut)|weapon_length(130), imodbits_polearm, [], [fac_kingdom_21]],

	["dunland_pike", "Sharpened Stake", [("dunland_pike", imodbits_none)], itp_type_polearm|itp_merchandise|itp_wooden_parry|itp_two_handed|itp_primary|itp_covers_head|itp_couchable, itcf_carry_spear|itc_staff, 100, thrust_damage(20, pierce)|hit_points(15360)|spd_rtng(110)|abundance(20)|weight(4.0)|swing_damage(15, cut)|weapon_length(196), imodbits_polearm, [], [fac_kingdom_21]],

	["wildling_heavy_armor_1", "Heavy Fur Armor", [("wildling_heavy_armor_1", imodbits_none)], itp_type_body_armor|itp_merchandise|itp_covers_legs|itp_doesnt_cover_hair|itp_can_penetrate_shield, 0, 500, abundance(20)|weight(5.0)|leg_armor(15)|body_armor(30), imodbits_cloth, [], [fac_kingdom_21]],

	["wildling_heavy_armor_2", "Heavy Fur Armor", [("wildling_heavy_armor_2", imodbits_none)], itp_type_body_armor|itp_merchandise|itp_covers_legs|itp_doesnt_cover_hair|itp_can_penetrate_shield, 0, 500, abundance(20)|weight(5.0)|leg_armor(15)|body_armor(30), imodbits_cloth, [], [fac_kingdom_21]],

	["wildling_heavy_armor_3", "Heavy Fur Armor", [("wildling_heavy_armor_3", imodbits_none)], itp_type_body_armor|itp_merchandise|itp_covers_legs|itp_doesnt_cover_hair|itp_can_penetrate_shield, 0, 500, abundance(20)|weight(5.0)|leg_armor(15)|body_armor(30), imodbits_cloth, [], [fac_kingdom_21]],

	["wildling_leather_vest_1", "Leather Vest", [("wildling_leather_vest_1", imodbits_none)], itp_type_body_armor|itp_merchandise|itp_covers_legs|itp_doesnt_cover_hair|itp_can_penetrate_shield, 0, 500, abundance(20)|weight(5.0)|leg_armor(15)|body_armor(35), imodbits_cloth, [], [fac_kingdom_21]],

	["wildling_leather_vest_2", "Leather Vest", [("wildling_leather_vest_2", imodbits_none)], itp_type_body_armor|itp_merchandise|itp_covers_legs|itp_doesnt_cover_hair|itp_can_penetrate_shield, 0, 500, abundance(20)|weight(5.0)|leg_armor(15)|body_armor(35), imodbits_cloth, [], [fac_kingdom_21]],

	["wildling_noble_cloth", "Wildling Chiefs Tunic", [("wildling_noble_cloth", imodbits_none)], itp_type_body_armor|itp_covers_legs|itp_doesnt_cover_hair|itp_can_penetrate_shield, 0, 500, abundance(20)|weight(5.0)|leg_armor(20)|body_armor(35), imodbits_cloth, [], [fac_kingdom_21]],

	["bw_wildling_cloth_tunic_1", "Tunic", [("bw_wildling_cloth_tunic_1", imodbits_none)], itp_type_body_armor|itp_merchandise|itp_covers_legs|itp_doesnt_cover_hair|itp_can_penetrate_shield, 0, 500, abundance(20)|weight(5.0)|leg_armor(5)|body_armor(9), imodbits_cloth, [], [fac_kingdom_21]],

	["bw_wildling_cloth_tunic_2", "Tunic", [("bw_wildling_cloth_tunic_2", imodbits_none)], itp_type_body_armor|itp_merchandise|itp_covers_legs|itp_doesnt_cover_hair|itp_can_penetrate_shield, 0, 500, abundance(20)|weight(5.0)|leg_armor(5)|body_armor(9), imodbits_cloth, [], [fac_kingdom_21]],

	["bw_wildling_cloth_tunic_3", "Tunic", [("bw_wildling_cloth_tunic_3", imodbits_none)], itp_type_body_armor|itp_merchandise|itp_covers_legs|itp_doesnt_cover_hair|itp_can_penetrate_shield, 0, 500, abundance(20)|weight(5.0)|leg_armor(5)|body_armor(9), imodbits_cloth, [], [fac_kingdom_21]],

	["bw_wildling_leather_tunic_1", "Leather Tunic", [("bw_wildling_leather_tunic_1", imodbits_none)], itp_type_body_armor|itp_merchandise|itp_covers_legs|itp_doesnt_cover_hair|itp_can_penetrate_shield, 0, 500, abundance(20)|weight(5.0)|leg_armor(11)|body_armor(22)|head_armor(5), imodbits_cloth, [], [fac_kingdom_21]],

	["bw_wildling_leather_tunic_2", "Leather Tunic", [("bw_wildling_leather_tunic_2", imodbits_none)], itp_type_body_armor|itp_merchandise|itp_covers_legs|itp_doesnt_cover_hair|itp_can_penetrate_shield, 0, 500, abundance(20)|weight(5.0)|leg_armor(11)|body_armor(22)|head_armor(5), imodbits_cloth, [], [fac_kingdom_21]],

	["bw_wildling_leather_tunic_3", "Leather Tunic", [("bw_wildling_leather_tunic_3", imodbits_none)], itp_type_body_armor|itp_merchandise|itp_covers_legs|itp_doesnt_cover_hair|itp_can_penetrate_shield, 0, 500, abundance(20)|weight(5.0)|leg_armor(11)|body_armor(22)|head_armor(5), imodbits_cloth, [], [fac_kingdom_21]],

	["bw_wildling_leather_tunic_4", "Leather Tunic", [("bw_wildling_leather_tunic_4", imodbits_none)], itp_type_body_armor|itp_merchandise|itp_covers_legs|itp_doesnt_cover_hair|itp_can_penetrate_shield, 0, 500, abundance(20)|weight(5.0)|leg_armor(11)|body_armor(22)|head_armor(5), imodbits_cloth, [], [fac_kingdom_21]],

	["bw_wildling_leather_tunic_5", "Leather Tunic", [("bw_wildling_leather_tunic_5", imodbits_none)], itp_type_body_armor|itp_merchandise|itp_covers_legs|itp_doesnt_cover_hair|itp_can_penetrate_shield, 0, 500, abundance(20)|weight(5.0)|leg_armor(11)|body_armor(22)|head_armor(5), imodbits_cloth, [], [fac_kingdom_21]],

	["bw_wildling_leather_tunic_6", "Leather Tunic", [("bw_wildling_leather_tunic_6", imodbits_none)], itp_type_body_armor|itp_merchandise|itp_covers_legs|itp_doesnt_cover_hair|itp_can_penetrate_shield, 0, 500, abundance(20)|weight(5.0)|leg_armor(11)|body_armor(22)|head_armor(5), imodbits_cloth, [], [fac_kingdom_21]],

	["kuyak_a", "Tormunds Plated Fur Armor", [("kuyak_a", imodbits_none)], itp_type_body_armor|itp_unique|itp_covers_legs|itp_doesnt_cover_hair|itp_can_penetrate_shield, 0, 3000, abundance(40)|weight(20.0)|leg_armor(5)|difficulty(12)|body_armor(40), imodbits_armor, [], [fac_kingdom_21]],

	["kuyak_b", "Wildling Chiefs Plated Fur Armor", [("kuyak_b", imodbits_none)], itp_type_body_armor|itp_covers_legs|itp_doesnt_cover_hair|itp_can_penetrate_shield, 0, 3000, abundance(40)|weight(20.0)|leg_armor(4)|difficulty(12)|body_armor(40), imodbits_armor, [], [fac_kingdom_21]],

	["coat_of_plates4", "Heavy Fur Armor", [("coat_of_plates4", imodbits_none)], itp_type_body_armor|itp_merchandise|itp_covers_legs|itp_doesnt_cover_hair|itp_can_penetrate_shield, 0, 500, abundance(20)|weight(5.0)|leg_armor(15)|body_armor(30), imodbits_cloth, [], [fac_kingdom_21]],

	["coat_of_plates5", "Heavy Fur Armor", [("wildling_quilted_tunic", imodbits_none)], itp_type_body_armor|itp_merchandise|itp_covers_legs|itp_doesnt_cover_hair|itp_can_penetrate_shield, 0, 500, abundance(20)|weight(5.0)|leg_armor(15)|body_armor(30), imodbits_cloth, [], [fac_kingdom_21]],

	["coat_of_plates6m", "Heavy Fur Armor", [("wildling_fur_tunic", imodbits_none)], itp_type_body_armor|itp_merchandise|itp_covers_legs|itp_doesnt_cover_hair|itp_can_penetrate_shield, 0, 500, abundance(20)|weight(5.0)|leg_armor(15)|body_armor(30), imodbits_cloth, [], [fac_kingdom_21]],

	["raider_hauberk", "Chain Mail Hauberk", [("Clansman_Lamellar_1", imodbits_none)], itp_type_body_armor|itp_merchandise|itp_covers_legs|itp_doesnt_cover_hair|itp_can_penetrate_shield, 0, 1500, abundance(10)|weight(20.0)|leg_armor(5)|difficulty(12)|body_armor(28), imodbits_armor, [], [fac_kingdom_21]],

	["raider_hauberk2", "Chain Mail Hauberk", [("Clansman_Fur_Armor_1", imodbits_none)], itp_type_body_armor|itp_merchandise|itp_covers_legs|itp_doesnt_cover_hair|itp_can_penetrate_shield, 0, 1500, abundance(40)|weight(20.0)|leg_armor(5)|difficulty(12)|body_armor(28), imodbits_armor, [], [fac_kingdom_21]],

	["raider_hauberk3", "Chain Mail Hauberk", [("raider_hauberk3", imodbits_none)], itp_type_body_armor|itp_merchandise|itp_covers_legs|itp_doesnt_cover_hair|itp_can_penetrate_shield, 0, 1500, abundance(40)|weight(20.0)|leg_armor(5)|difficulty(12)|body_armor(28), imodbits_armor, [], [fac_kingdom_21]],

	["briton_helm", "Wildling Chiefs Nasal Helmet", [("briton_helm", imodbits_none)], itp_type_head_armor|itp_unique|itp_fit_to_head|itp_offset_lance, 0, 2000, abundance(10)|weight(4.0)|difficulty(12)|head_armor(33), imodbits_plate, [], [fac_kingdom_21]],

	["dux_ridge_helm", "Tormunds Nasal Helmet", [("dux_ridge_helm", imodbits_none)], itp_type_head_armor|itp_unique|itp_fit_to_head|itp_offset_lance, 0, 2000, abundance(10)|weight(4.0)|difficulty(12)|head_armor(37), imodbits_none, [], [fac_kingdom_21]],

	["valsgarde1", "Nasal Helmet", [("BL_02_Valsgarde01BOAR", imodbits_none)], itp_type_head_armor|itp_merchandise|itp_fit_to_head|itp_offset_lance|itp_covers_beard, 0, 2000, abundance(10)|weight(4.0)|difficulty(12)|head_armor(33), imodbits_cloth, [], [fac_kingdom_21]],

	["valsgarde2", "Nasal Helmet", [("BL_02_Valsgarde02", imodbits_none)], itp_type_head_armor|itp_merchandise|itp_fit_to_head|itp_offset_lance, 0, 2000, abundance(10)|weight(4.0)|difficulty(12)|head_armor(30), imodbits_cloth, [], [fac_kingdom_21]],

	["valsgarde3", "Nasal Helmet", [("BL_04_Valsgarde01", imodbits_none)], itp_type_head_armor|itp_merchandise|itp_fit_to_head|itp_offset_lance|itp_covers_beard, 0, 2000, abundance(10)|weight(4.0)|difficulty(12)|head_armor(33), imodbits_cloth, [], [fac_kingdom_21]],

	["valsgarde4", "Nasal Helmet", [("BL_04_Valsgarde02", imodbits_none)], itp_type_head_armor|itp_merchandise|itp_fit_to_head|itp_offset_lance, 0, 2000, abundance(10)|weight(4.0)|difficulty(12)|head_armor(30), imodbits_cloth, [], [fac_kingdom_21]],

	["wildling_square_shield_1", "Wildlings Square Shield", [("wildling_square_shield_1", imodbits_none)], itp_type_shield|itp_merchandise|itp_wooden_parry, itcf_carry_round_shield, 200, hit_points(180)|spd_rtng(87)|abundance(60)|weight(5.0)|shield_width(44)|shield_height(70)|body_armor(2), imodbits_none, [], [fac_kingdom_21]],

	["wildling_square_shield_2", "Wildlings Square Shield", [("wildling_square_shield_2", imodbits_none)], itp_type_shield|itp_merchandise|itp_wooden_parry, itcf_carry_round_shield, 200, hit_points(180)|spd_rtng(87)|abundance(60)|weight(5.0)|shield_width(44)|shield_height(70)|body_armor(2), imodbits_none, [], [fac_kingdom_21]],

	["wildling_square_shield_3", "Wildlings Square Shield", [("wildling_square_shield_3", imodbits_none)], itp_type_shield|itp_merchandise|itp_wooden_parry, itcf_carry_round_shield, 200, hit_points(180)|spd_rtng(87)|abundance(60)|weight(5.0)|shield_width(44)|shield_height(70)|body_armor(2), imodbits_none, [], [fac_kingdom_21]],

	["wildling_square_shield_4", "Wildlings Square Shield", [("wildling_square_shield_4", imodbits_none)], itp_type_shield|itp_merchandise|itp_wooden_parry, itcf_carry_round_shield, 200, hit_points(180)|spd_rtng(87)|abundance(60)|weight(5.0)|shield_width(44)|shield_height(70)|body_armor(2), imodbits_none, [], [fac_kingdom_21]],

	["wildling_square_shield_5", "Wildlings Square Shield", [("wildling_square_shield_5", imodbits_none)], itp_type_shield|itp_merchandise|itp_wooden_parry, itcf_carry_round_shield, 200, hit_points(180)|spd_rtng(87)|abundance(60)|weight(5.0)|shield_width(44)|shield_height(70)|body_armor(2), imodbits_none, [], [fac_kingdom_21]],

	["wildling_square_shield_9", "Wildlings Square Shield", [("wildling_square_shield_9", imodbits_none)], itp_type_shield|itp_merchandise|itp_wooden_parry, itcf_carry_round_shield, 200, hit_points(180)|spd_rtng(87)|abundance(60)|weight(5.0)|shield_width(44)|shield_height(70)|body_armor(2), imodbits_none, [], [fac_kingdom_21]],

	["wildling_square_shield_12", "Wildlings Square Shield", [("wildling_square_shield_12", imodbits_none)], itp_type_shield|itp_merchandise|itp_wooden_parry, itcf_carry_round_shield, 200, hit_points(180)|spd_rtng(87)|abundance(60)|weight(5.0)|shield_width(44)|shield_height(70)|body_armor(2), imodbits_none, [], [fac_kingdom_21]],

	["xenoargh_round_shield05_plain", "Round Wooden Shield", [("xenoargh_round_shield05_plain", imodbits_none)], itp_type_shield|itp_merchandise|itp_wooden_parry, itcf_carry_round_shield, 200, hit_points(180)|spd_rtng(87)|abundance(60)|weight(5.0)|shield_width(70)|shield_height(70)|body_armor(2), imodbits_none, [], [fac_kingdom_1, fac_kingdom_2, fac_kingdom_3, fac_kingdom_8, fac_kingdom_9, fac_kingdom_10, fac_kingdom_11, fac_kingdom_19]],

	["bw_wildling_cloth_tunic_1_noble", "Tunic", [("bw_wildling_cloth_tunic_1", imodbits_none)], itp_type_body_armor|itp_covers_legs|itp_doesnt_cover_hair|itp_can_penetrate_shield|itp_civilian|itp_next_item_as_melee, 0, 500, abundance(20)|weight(5.0)|leg_armor(5)|body_armor(9), imodbits_cloth, [], [fac_kingdom_21]],

	["bw_wildling_cloth_tunic_2_noble", "Tunic", [("bw_wildling_cloth_tunic_2", imodbits_none)], itp_type_body_armor|itp_covers_legs|itp_doesnt_cover_hair|itp_can_penetrate_shield|itp_civilian|itp_next_item_as_melee, 0, 500, abundance(20)|weight(5.0)|leg_armor(5)|body_armor(9), imodbits_cloth, [], [fac_kingdom_21]],

	["bw_wildling_cloth_tunic_3_noble", "Tunic", [("bw_wildling_cloth_tunic_3", imodbits_none)], itp_type_body_armor|itp_covers_legs|itp_doesnt_cover_hair|itp_can_penetrate_shield|itp_civilian|itp_next_item_as_melee, 0, 500, abundance(20)|weight(5.0)|leg_armor(5)|body_armor(9), imodbits_cloth, [], [fac_kingdom_21]],

	["bw_wildling_leather_tunic_1_noble", "Leather Tunic", [("bw_wildling_leather_tunic_1", imodbits_none)], itp_type_body_armor|itp_covers_legs|itp_doesnt_cover_hair|itp_can_penetrate_shield|itp_civilian|itp_next_item_as_melee, 0, 500, abundance(20)|weight(5.0)|leg_armor(11)|body_armor(22)|head_armor(5), imodbits_cloth, [], [fac_kingdom_21]],

	["bw_wildling_leather_tunic_2_noble", "Leather Tunic", [("bw_wildling_leather_tunic_2", imodbits_none)], itp_type_body_armor|itp_covers_legs|itp_doesnt_cover_hair|itp_can_penetrate_shield|itp_civilian|itp_next_item_as_melee, 0, 500, abundance(20)|weight(5.0)|leg_armor(11)|body_armor(22)|head_armor(5), imodbits_cloth, [], [fac_kingdom_21]],

	["bw_wildling_leather_tunic_3_noble", "Leather Tunic", [("bw_wildling_leather_tunic_3", imodbits_none)], itp_type_body_armor|itp_covers_legs|itp_doesnt_cover_hair|itp_can_penetrate_shield|itp_civilian|itp_next_item_as_melee, 0, 500, abundance(20)|weight(5.0)|leg_armor(11)|body_armor(22)|head_armor(5), imodbits_cloth, [], [fac_kingdom_21]],

	["bw_wildling_leather_tunic_4_noble", "Leather Tunic", [("bw_wildling_leather_tunic_4", imodbits_none)], itp_type_body_armor|itp_covers_legs|itp_doesnt_cover_hair|itp_can_penetrate_shield|itp_civilian|itp_next_item_as_melee, 0, 500, abundance(20)|weight(5.0)|leg_armor(11)|body_armor(22)|head_armor(5), imodbits_cloth, [], [fac_kingdom_21]],

	["bw_wildling_leather_tunic_5_noble", "Leather Tunic", [("bw_wildling_leather_tunic_5", imodbits_none)], itp_type_body_armor|itp_covers_legs|itp_doesnt_cover_hair|itp_can_penetrate_shield|itp_civilian|itp_next_item_as_melee, 0, 500, abundance(20)|weight(5.0)|leg_armor(11)|body_armor(22)|head_armor(5), imodbits_cloth, [], [fac_kingdom_21]],

	["bw_wildling_leather_tunic_6_noble", "Leather Tunic", [("bw_wildling_leather_tunic_6", imodbits_none)], itp_type_body_armor|itp_covers_legs|itp_doesnt_cover_hair|itp_can_penetrate_shield|itp_civilian|itp_next_item_as_melee, 0, 500, abundance(20)|weight(5.0)|leg_armor(11)|body_armor(22)|head_armor(5), imodbits_cloth, [], [fac_kingdom_21]],

	["we_swa_arrow_gromite", "Steel Arrows", [("strela2", imodbits_none), ("flying_missile", ixmesh_flying_ammo), ("kolchan2", ixmesh_carry)], itp_type_arrows|itp_merchandise, itcf_carry_quiver_back_right, 700, thrust_damage(8, pierce)|max_ammo(22)|abundance(60)|weight(3.0)|weapon_length(91), imodbits_missile, [], [fac_kingdom_16]],

	["ar_nor_shi_skjortira", "Dothraki Outfit", [("berserker_1", imodbits_none)], itp_type_body_armor|itp_unique|itp_covers_legs|itp_doesnt_cover_hair|itp_can_penetrate_shield|itp_civilian|itp_next_item_as_melee, 0, 100, abundance(60)|weight(2.0)|leg_armor(10), imodbits_cloth, [], [fac_kingdom_22]],

	["ar_nor_tun_blue", "Dothraki Outfit", [("berserker_2", imodbits_none)], itp_type_body_armor|itp_unique|itp_covers_legs|itp_doesnt_cover_hair|itp_can_penetrate_shield|itp_civilian|itp_next_item_as_melee, 0, 100, abundance(60)|weight(4.0)|leg_armor(10), imodbits_cloth, [], [fac_kingdom_22]],

	["dothraki_lamellar", "Dothraki Lamellar Armor", [("kuauik_dothraki_mail", imodbits_none)], itp_type_body_armor|itp_covers_legs|itp_doesnt_cover_hair|itp_can_penetrate_shield|itp_civilian|itp_next_item_as_melee, 0, 700, abundance(60)|weight(2.0)|body_armor(27), imodbits_cloth, [], [fac_kingdom_22]],

	["brego_nord_helmet", "Nasal Helmet", [("brego_nord_helmet", imodbits_none)], itp_type_head_armor|itp_fit_to_head|itp_offset_lance, 0, 2000, abundance(10)|weight(4.0)|difficulty(12)|head_armor(27), imodbits_cloth, [], [fac_kingdom_21]],

	["dothraki_hair_1", "Dothraki Braid", [("dothraki_hair_1", imodbits_none)], itp_type_head_armor|itp_unique|itp_civilian|itp_next_item_as_melee|itp_covers_beard, 0, 9, abundance(60)|weight(1.0)|head_armor(2), imodbits_none, [], [fac_kingdom_3]],

	["dothraki_hair_2", "Dothraki Braid", [("dothraki_hair_2", imodbits_none)], itp_type_head_armor|itp_unique|itp_civilian|itp_next_item_as_melee|itp_covers_beard, 0, 9, abundance(60)|weight(1.0)|head_armor(2), imodbits_none, [], [fac_kingdom_3]],

	["dothraki_hair_3", "Dothraki Braid", [("dothraki_hair_3", imodbits_none)], itp_type_head_armor|itp_unique|itp_civilian|itp_next_item_as_melee|itp_covers_beard, 0, 9, abundance(60)|weight(1.0)|head_armor(2), imodbits_none, [], [fac_kingdom_3]],

	["dothraki_hair_4", "Dothraki Braid", [("dothraki_hair_4", imodbits_none)], itp_type_head_armor|itp_unique|itp_civilian|itp_next_item_as_melee|itp_covers_beard, 0, 9, abundance(60)|weight(1.0)|head_armor(2), imodbits_none, [], [fac_kingdom_3]],

	["dothraki_hair_5", "Dothraki Braid", [("dothraki_hair_5", imodbits_none)], itp_type_head_armor|itp_unique|itp_civilian|itp_next_item_as_melee|itp_covers_beard, 0, 9, abundance(60)|weight(1.0)|head_armor(2), imodbits_none, [], [fac_kingdom_3]],

	["dothraki_hair_6", "Dothraki Braid", [("dothraki_hair_6", imodbits_none)], itp_type_head_armor|itp_unique|itp_civilian|itp_next_item_as_melee|itp_covers_beard, 0, 9, abundance(60)|weight(1.0)|head_armor(2), imodbits_none, [], [fac_kingdom_3]],

	["otk_shlem", "The Weepers Helmet", [("otk_shlem", imodbits_none)], itp_type_head_armor|itp_fit_to_head|itp_offset_lance|itp_covers_beard, 0, 2000, abundance(10)|weight(4.0)|difficulty(12)|head_armor(30), imodbits_cloth, [], [fac_kingdom_21]],

	["otk_axe", "One-Handed Axe", [("otk_axe", imodbits_none)], itp_type_one_handed_wpn|itp_wooden_parry|itp_primary|itp_secondary, itcf_carry_axe_left_hip|itc_scimitar, 600, thrust_damage(0, pierce)|hit_points(32768)|spd_rtng(100)|abundance(10)|weight(2.0)|swing_damage(32, cut)|difficulty(8)|weapon_length(61), imodbits_axe|imodbits_mace],

	["mackie_machete", "Dothraki Cleaver", [("mackie_machete", imodbits_none)], itp_type_one_handed_wpn|itp_primary, itcf_carry_sword_left_hip|itc_scimitar, 700, hit_points(28672)|spd_rtng(105)|abundance(20)|weight(5.0)|swing_damage(28, cut)|difficulty(10)|weapon_length(100), imodbits_none, [], [fac_kingdom_13, fac_kingdom_14, fac_kingdom_15, fac_kingdom_16, fac_kingdom_17, fac_kingdom_5]],

	["mackie_meat_cleaver_1", "Meat Cleaver", [("mackie_meat_cleaver_1", imodbits_none)], itp_type_one_handed_wpn|itp_no_parry|itp_primary, itcf_carry_dagger_front_left|itc_dagger, 100, thrust_damage(0, pierce)|hit_points(15360)|spd_rtng(80)|abundance(100)|weight(1.0)|swing_damage(15, cut)|weapon_length(43), imodbits_none],

	["mackie_meat_cleaver_2", "Meat Cleaver", [("mackie_meat_cleaver_2", imodbits_none)], itp_type_one_handed_wpn|itp_no_parry|itp_primary, itcf_carry_dagger_front_left|itc_dagger, 100, thrust_damage(0, pierce)|hit_points(15360)|spd_rtng(80)|abundance(100)|weight(1.0)|swing_damage(15, cut)|weapon_length(43), imodbits_none],

	["mackie_meat_cleaver_3", "Meat Cleaver", [("mackie_meat_cleaver_3", imodbits_none)], itp_type_one_handed_wpn|itp_no_parry|itp_primary, itcf_carry_dagger_front_left|itc_dagger, 100, thrust_damage(0, pierce)|hit_points(15360)|spd_rtng(80)|abundance(100)|weight(1.0)|swing_damage(15, cut)|weapon_length(43), imodbits_none],

	["new_nightswatch_1", "Leather Jerkin", [("new_nightswatch_1", imodbits_none)], itp_type_body_armor|itp_covers_legs|itp_doesnt_cover_hair|itp_can_penetrate_shield|itp_civilian|itp_next_item_as_melee, 0, 300, abundance(10)|weight(10.0)|leg_armor(5)|body_armor(24), imodbits_cloth, [], [fac_kingdom_21]],

	["new_nightswatch_1_cloak", "Leather Jerkin", [("new_nightswatch_1_cloak", imodbits_none)], itp_type_body_armor|itp_covers_legs|itp_doesnt_cover_hair|itp_can_penetrate_shield|itp_civilian|itp_next_item_as_melee, 0, 500, abundance(10)|weight(10.0)|leg_armor(5)|body_armor(24), imodbits_cloth, [], [fac_kingdom_21]],

	["new_nightswatch_2", "Leather Jerkin", [("new_nightswatch_2", imodbits_none)], itp_type_body_armor|itp_covers_legs|itp_doesnt_cover_hair|itp_can_penetrate_shield|itp_civilian|itp_next_item_as_melee, 0, 300, abundance(10)|weight(10.0)|leg_armor(5)|body_armor(24), imodbits_cloth, [], [fac_kingdom_21]],

	["new_nightswatch_2_cloak", "Leather Jerkin", [("new_nightswatch_2_cloak", imodbits_none)], itp_type_body_armor|itp_covers_legs|itp_doesnt_cover_hair|itp_can_penetrate_shield|itp_civilian|itp_next_item_as_melee, 0, 500, abundance(10)|weight(10.0)|leg_armor(5)|body_armor(24), imodbits_cloth, [], [fac_kingdom_21]],

	["new_nightswatch_3", "Chain Mail Hauberk", [("new_nightswatch_3", imodbits_none)], itp_type_body_armor|itp_covers_legs|itp_doesnt_cover_hair|itp_can_penetrate_shield|itp_civilian|itp_next_item_as_melee, 0, 1500, abundance(10)|weight(20.0)|leg_armor(5)|difficulty(12)|body_armor(37), imodbits_armor, [], [fac_kingdom_21]],

	["new_nightswatch_3_cloak", "Chain Mail Hauberk", [("new_nightswatch_3_cloak", imodbits_none)], itp_type_body_armor|itp_covers_legs|itp_doesnt_cover_hair|itp_can_penetrate_shield|itp_civilian|itp_next_item_as_melee, 0, 1500, abundance(10)|weight(20.0)|leg_armor(5)|difficulty(12)|body_armor(37), imodbits_armor, [], [fac_kingdom_21]],

	["new_nightswatch_4", "Lamellar Armor", [("new_nightswatch_4", imodbits_none)], itp_type_body_armor|itp_covers_legs|itp_doesnt_cover_hair|itp_can_penetrate_shield|itp_civilian|itp_next_item_as_melee, 0, 2500, abundance(10)|weight(20.0)|leg_armor(5)|difficulty(12)|body_armor(40), imodbits_armor, [], [fac_kingdom_21]],

	["new_nightswatch_4_cloak", "Lamellar Armor", [("new_nightswatch_4_cloak", imodbits_none)], itp_type_body_armor|itp_covers_legs|itp_doesnt_cover_hair|itp_can_penetrate_shield|itp_civilian|itp_next_item_as_melee, 0, 2500, abundance(10)|weight(20.0)|leg_armor(5)|difficulty(12)|body_armor(40), imodbits_armor, [], [fac_kingdom_21]],

	["new_nightswatch_5", "Light Plate Armor", [("new_nightswatch_5", imodbits_none)], itp_type_body_armor|itp_covers_legs|itp_doesnt_cover_hair|itp_can_penetrate_shield|itp_civilian|itp_next_item_as_melee, 0, 3500, abundance(10)|weight(20.0)|leg_armor(18)|difficulty(12)|body_armor(40), imodbits_armor, [], [fac_kingdom_21]],

	["new_nightswatch_5_cloak", "Light Plate Armor", [("new_nightswatch_5_cloak", imodbits_none)], itp_type_body_armor|itp_covers_legs|itp_doesnt_cover_hair|itp_can_penetrate_shield|itp_civilian|itp_next_item_as_melee, 0, 3500, abundance(10)|weight(20.0)|leg_armor(18)|difficulty(12)|body_armor(40), imodbits_armor, [], [fac_kingdom_21]],

	["new_nightswatch_mance_rayder", "Chain Mail Hauberk", [("new_nightswatch_mance_rayder", imodbits_none)], itp_type_body_armor|itp_covers_legs|itp_doesnt_cover_hair|itp_can_penetrate_shield|itp_civilian|itp_next_item_as_melee, 0, 3500, abundance(10)|weight(20.0)|leg_armor(3)|difficulty(12)|body_armor(40), imodbits_armor, [], [fac_kingdom_21]],

	["aemons_robe", "Maesters Robe", [("aemons_robe", imodbits_none)], itp_type_body_armor|itp_covers_legs|itp_doesnt_cover_hair|itp_can_penetrate_shield|itp_civilian|itp_next_item_as_melee, 0, 50, abundance(10)|weight(5.0)|leg_armor(3)|difficulty(12)|body_armor(8), imodbits_armor, [], [fac_kingdom_21]],

	["dedal_kufel", "Kufel", [("dedal_kufelL", imodbits_none)], itp_type_hand_armor, 0, 0, abundance(100)|weight(1.0), imodbits_none],

	["dedal_lutnia", "Lutnia", [("dedal_lutniaL", imodbits_none)], itp_type_hand_armor, 0, 0, abundance(100)|weight(1.0), imodbits_none],

	["dedal_lira", "Lira", [("dedal_liraL", imodbits_none)], itp_type_hand_armor, 0, 0, abundance(100)|weight(1.0), imodbits_none],

	["awl_pike_a", "Pike", [("awl_pike_a", imodbits_none)], itp_type_polearm|itp_merchandise|itp_wooden_parry|itp_two_handed|itp_primary|itp_cant_use_on_horseback, itcf_carry_spear|itc_staff, 400, thrust_damage(35, pierce)|hit_points(25600)|spd_rtng(105)|abundance(20)|weight(4.0)|swing_damage(25, cut)|weapon_length(183), imodbits_polearm, [], [fac_kingdom_2, fac_kingdom_5, fac_kingdom_9, fac_kingdom_10]],

	["awl_pike_b", "Pike", [("awl_pike_b", imodbits_none)], itp_type_polearm|itp_merchandise|itp_wooden_parry|itp_two_handed|itp_primary|itp_cant_use_on_horseback, itcf_carry_spear|itc_staff, 400, thrust_damage(35, pierce)|hit_points(25600)|spd_rtng(105)|abundance(20)|weight(4.0)|swing_damage(25, cut)|weapon_length(161), imodbits_polearm, [], [fac_kingdom_2, fac_kingdom_5, fac_kingdom_9, fac_kingdom_10]],

	["dornish_cataphract_helmet", "Full Helmet", [("dornish_cataphract_helmet", imodbits_none)], itp_type_head_armor|itp_merchandise|itp_fit_to_head|itp_offset_lance|itp_covers_beard, 0, 2000, abundance(10)|weight(4.0)|difficulty(12)|head_armor(37), imodbits_armor, [], [fac_kingdom_6]],

	["dornish_chain_fur_1", "Nasal Helmet", [("dornish_chain_fur_1", imodbits_none)], itp_type_head_armor|itp_merchandise|itp_fit_to_head|itp_offset_lance, 0, 500, abundance(10)|weight(4.0)|difficulty(12)|head_armor(24), imodbits_armor, [], [fac_kingdom_6]],

	["dornish_chain_fur_2", "Nasal Helmet", [("dornish_chain_fur_2", imodbits_none)], itp_type_head_armor|itp_merchandise|itp_fit_to_head|itp_offset_lance, 0, 500, abundance(10)|weight(4.0)|difficulty(12)|head_armor(24), imodbits_armor, [], [fac_kingdom_6]],

	["dornish_chain_fur_3", "Nasal Helmet", [("dornish_chain_fur_3", imodbits_none)], itp_type_head_armor|itp_merchandise|itp_fit_to_head|itp_offset_lance, 0, 500, abundance(10)|weight(4.0)|difficulty(12)|head_armor(24), imodbits_armor, [], [fac_kingdom_6]],

	["dornish_turban", "Headcloth", [("dornish_turban", imodbits_none)], itp_type_head_armor|itp_merchandise|itp_fit_to_head|itp_offset_lance|itp_covers_beard, 0, 200, abundance(10)|weight(4.0)|head_armor(13), imodbits_armor, [], [fac_kingdom_6]],

	["dornish_open_turban", "Headcloth", [("dornish_open_turban", imodbits_none)], itp_type_head_armor|itp_merchandise|itp_fit_to_head|itp_offset_lance, 0, 200, abundance(10)|weight(4.0)|head_armor(13), imodbits_armor, [], [fac_kingdom_6]],

	["dornish_turban_helmet_mail", "Conical Helmet", [("dornish_turban_helmet_mail", imodbits_none)], itp_type_head_armor|itp_merchandise|itp_fit_to_head|itp_offset_lance, 0, 1000, abundance(10)|weight(4.0)|difficulty(12)|head_armor(30), imodbits_armor, [], [fac_kingdom_6]],

	["dornish_leather_helmet", "Leather Cap", [("dornish_leather_helmet", imodbits_none)], itp_type_head_armor|itp_merchandise|itp_fit_to_head|itp_offset_lance, 0, 400, abundance(10)|weight(4.0)|head_armor(15), imodbits_cloth, [], [fac_kingdom_6]],

	["dornish_chain_mail_1", "Conical Helmet", [("dornish_chain_mail_1", imodbits_none)], itp_type_head_armor|itp_merchandise|itp_fit_to_head|itp_offset_lance, 0, 1000, abundance(10)|weight(4.0)|difficulty(12)|head_armor(30), imodbits_armor, [], [fac_kingdom_6]],

	["dornish_chain_mail_2", "Nasal Helmet", [("dornish_chain_mail_2", imodbits_none)], itp_type_head_armor|itp_merchandise|itp_fit_to_head|itp_offset_lance, 0, 1400, abundance(10)|weight(4.0)|difficulty(12)|head_armor(34), imodbits_armor, [], [fac_kingdom_6]],

	["dornish_chain_mail_3", "Nasal Helmet", [("dornish_chain_mail_3", imodbits_none)], itp_type_head_armor|itp_merchandise|itp_fit_to_head|itp_offset_lance, 0, 1400, abundance(10)|weight(4.0)|difficulty(12)|head_armor(34), imodbits_armor, [], [fac_kingdom_6]],

	["dornish_turban_helmet_2", "Conical Helmet", [("dornish_turban_helmet_2", imodbits_none)], itp_type_head_armor|itp_merchandise|itp_fit_to_head|itp_offset_lance, 0, 1000, abundance(10)|weight(4.0)|difficulty(12)|head_armor(30), imodbits_armor, [], [fac_kingdom_6]],

	["dornish_turban_helmet_1", "Conical Helmet", [("dornish_turban_helmet_1", imodbits_none)], itp_type_head_armor|itp_merchandise|itp_fit_to_head|itp_offset_lance|itp_covers_beard, 0, 1000, abundance(10)|weight(4.0)|difficulty(12)|head_armor(30), imodbits_armor, [], [fac_kingdom_6]],

	["dornish_lamellar", "Lamellar Vest", [("dornish_lamellar", imodbits_none)], itp_type_body_armor|itp_merchandise|itp_covers_legs|itp_doesnt_cover_hair|itp_can_penetrate_shield, 0, 1500, abundance(50)|weight(20.0)|difficulty(12)|body_armor(30), imodbits_armor, [], [fac_kingdom_6]],

	["dornish_scale", "Scale Hauberk", [("dornish_scale", imodbits_none)], itp_type_body_armor|itp_merchandise|itp_covers_legs|itp_doesnt_cover_hair|itp_can_penetrate_shield, 0, 3000, abundance(50)|weight(20.0)|difficulty(12)|body_armor(37), imodbits_armor, [], [fac_kingdom_6]],

	["dornish_cavrobe_1", "Chain Mail Hauberk", [("dornish_cavrobe_1", imodbits_none)], itp_type_body_armor|itp_merchandise|itp_covers_legs|itp_doesnt_cover_hair|itp_can_penetrate_shield, 0, 4000, abundance(50)|weight(20.0)|leg_armor(8)|difficulty(12)|body_armor(40), imodbits_armor, [], [fac_kingdom_6]],

	["dornish_chain_mail_shirt_3", "Chain Mail Hauberk", [("dornish_chain_mail_shirt_3", imodbits_none)], itp_type_body_armor|itp_merchandise|itp_covers_legs|itp_doesnt_cover_hair|itp_can_penetrate_shield, 0, 4000, abundance(50)|weight(20.0)|leg_armor(6)|difficulty(12)|body_armor(37), imodbits_armor, [], [fac_kingdom_6]],

	["dornish_heavy_lamellar", "Heavy Lamellar Armor", [("dornish_heavy_lamellar", imodbits_none)], itp_type_body_armor|itp_merchandise|itp_covers_legs|itp_doesnt_cover_hair|itp_can_penetrate_shield, 0, 6000, abundance(10)|weight(20.0)|difficulty(12)|body_armor(44), imodbits_armor, [], [fac_kingdom_6]],

	["dornish_leather_robe", "Leather Jerkin", [("dornish_leather_robe", imodbits_none)], itp_type_body_armor|itp_merchandise|itp_covers_legs|itp_doesnt_cover_hair|itp_can_penetrate_shield, 0, 600, abundance(50)|weight(10.0)|leg_armor(5)|body_armor(27), imodbits_cloth, [], [fac_kingdom_6]],

	["dornish_skirmisher", "Padded Tunic", [("dornish_skirmisher", imodbits_none)], itp_type_body_armor|itp_merchandise|itp_covers_legs|itp_doesnt_cover_hair|itp_can_penetrate_shield, 0, 300, abundance(50)|weight(5.0)|leg_armor(5)|body_armor(15), imodbits_cloth, [], [fac_kingdom_6]],

	["broken_bottle", "Broken Bottle", [("broken_bottle", imodbits_none)], itp_type_one_handed_wpn|itp_no_parry|itp_primary|itp_secondary, itcf_carry_dagger_front_left|itc_dagger, 1, thrust_damage(10, pierce)|hit_points(14336)|spd_rtng(110)|abundance(100)|weight(0.5)|swing_damage(14, cut)|weapon_length(20), imodbits_none],

	["kuauik_padded_leather", "Leather Jerkin", [("kuauik_padded_leather", imodbits_none)], itp_type_body_armor|itp_merchandise|itp_covers_legs|itp_doesnt_cover_hair|itp_can_penetrate_shield, 0, 150, abundance(100)|weight(10.0)|body_armor(17), imodbits_cloth, [], [fac_kingdom_1, fac_kingdom_3, fac_kingdom_5, fac_kingdom_8, fac_kingdom_9, fac_kingdom_10]],

	["kuauik_peasant_1", "Peasants Tunic", [("kuauik_peasant_1", imodbits_none)], itp_type_body_armor|itp_merchandise|itp_covers_legs|itp_doesnt_cover_hair|itp_can_penetrate_shield, 0, 50, abundance(100)|weight(2.0)|leg_armor(1)|body_armor(5), imodbits_cloth],

	["kuauik_peasant_2", "Peasants Tunic", [("kuauik_peasant_2", imodbits_none)], itp_type_body_armor|itp_merchandise|itp_covers_legs|itp_doesnt_cover_hair|itp_can_penetrate_shield, 0, 50, abundance(100)|weight(2.0)|leg_armor(1)|body_armor(5), imodbits_cloth],

	["kuauik_studded_leather_1", "Studded Leather Jerkin", [("kuauik_studded_leather_1", imodbits_none)], itp_type_body_armor|itp_merchandise|itp_covers_legs|itp_doesnt_cover_hair|itp_can_penetrate_shield, 0, 900, abundance(100)|weight(10.0)|leg_armor(5)|body_armor(30), imodbits_cloth, [], [fac_kingdom_1, fac_kingdom_8]],

	["kuauik_studded_leather_2", "Studded Leather Jerkin", [("kuauik_studded_leather_2", imodbits_none)], itp_type_body_armor|itp_merchandise|itp_covers_legs|itp_doesnt_cover_hair|itp_can_penetrate_shield, 0, 900, abundance(100)|weight(10.0)|leg_armor(5)|body_armor(30), imodbits_cloth, [], [fac_kingdom_1, fac_kingdom_8]],

	["kuauik_welsh_archer_1", "Studded Leather Jerkin", [("kuauik_welsh_archer_1", imodbits_none)], itp_type_body_armor|itp_merchandise|itp_covers_legs|itp_doesnt_cover_hair|itp_can_penetrate_shield, 0, 500, abundance(100)|weight(10.0)|leg_armor(5)|body_armor(25), imodbits_cloth, [], [fac_kingdom_1, fac_kingdom_8]],

	["kuauik_welsh_archer_2", "Studded Leather Jerkin", [("kuauik_welsh_archer_2", imodbits_none)], itp_type_body_armor|itp_merchandise|itp_covers_legs|itp_doesnt_cover_hair|itp_can_penetrate_shield, 0, 500, abundance(100)|weight(10.0)|leg_armor(5)|body_armor(25), imodbits_cloth, [], [fac_kingdom_1, fac_kingdom_8]],

	["kuauik_leather_tunic", "Leather Jerkin", [("kuauik_leather_tunic", imodbits_none)], itp_type_body_armor|itp_merchandise|itp_covers_legs|itp_doesnt_cover_hair|itp_can_penetrate_shield, 0, 400, abundance(100)|weight(10.0)|body_armor(22), imodbits_cloth, [], [fac_kingdom_12, fac_kingdom_13, fac_kingdom_14, fac_kingdom_15, fac_kingdom_16, fac_kingdom_17, fac_kingdom_18]],

	["kuauik_dornish_leather_tunic_1", "Leather Jerkin", [("kuauik_dornish_leather_tunic_1", imodbits_none)], itp_type_body_armor|itp_merchandise|itp_covers_legs|itp_doesnt_cover_hair|itp_can_penetrate_shield, 0, 150, abundance(100)|weight(10.0)|body_armor(17), imodbits_cloth, [], [fac_kingdom_6]],

	["kuauik_dornish_leather_tunic_2", "Leather Jerkin", [("kuauik_dornish_leather_tunic_2", imodbits_none)], itp_type_body_armor|itp_merchandise|itp_covers_legs|itp_doesnt_cover_hair|itp_can_penetrate_shield, 0, 150, abundance(100)|weight(10.0)|body_armor(17), imodbits_cloth, [], [fac_kingdom_6]],

	["kuauik_dornish_studded_leather", "Studded Leather Jerkin", [("kuauik_dornish_studded_leather", imodbits_none)], itp_type_body_armor|itp_merchandise|itp_covers_legs|itp_doesnt_cover_hair|itp_can_penetrate_shield, 0, 500, abundance(100)|weight(10.0)|leg_armor(5)|body_armor(22), imodbits_cloth, [], [fac_kingdom_6]],

	["kuauik_dornish_chain_mail", "Chain Mail Hauberk", [("kuauik_dornish_chain_mail", imodbits_none)], itp_type_body_armor|itp_merchandise|itp_covers_legs|itp_doesnt_cover_hair|itp_can_penetrate_shield, 0, 4000, abundance(100)|weight(20.0)|leg_armor(5)|difficulty(12)|body_armor(37), imodbits_armor, [], [fac_kingdom_6]],

	["kuauik_gambeson", "Gambeson", [("kuauik_gambeson", imodbits_none)], itp_type_body_armor|itp_merchandise|itp_covers_legs|itp_doesnt_cover_hair|itp_can_penetrate_shield, 0, 300, abundance(100)|weight(10.0)|leg_armor(6)|body_armor(22), imodbits_cloth, [], [fac_kingdom_1, fac_kingdom_3, fac_kingdom_10]],

	["kuauik_bulgar_armor", "Lamellar Armor", [("kuauik_bulgar_armor", imodbits_none)], itp_type_body_armor|itp_merchandise|itp_covers_legs|itp_doesnt_cover_hair|itp_can_penetrate_shield, 0, 3500, abundance(100)|weight(20.0)|leg_armor(5)|difficulty(12)|body_armor(37), imodbits_armor, [], [fac_kingdom_12, fac_kingdom_13, fac_kingdom_14, fac_kingdom_15, fac_kingdom_16, fac_kingdom_17, fac_kingdom_5, fac_kingdom_18]],

	["kuauik_bulgar_leather_armor", "Leather Jerkin", [("kuauik_bulgar_leather_armor", imodbits_none)], itp_type_body_armor|itp_merchandise|itp_covers_legs|itp_doesnt_cover_hair|itp_can_penetrate_shield, 0, 150, abundance(100)|weight(10.0)|body_armor(17), imodbits_cloth, [], [fac_kingdom_12, fac_kingdom_13, fac_kingdom_14, fac_kingdom_15, fac_kingdom_16, fac_kingdom_17, fac_kingdom_5, fac_kingdom_18]],

	["kuauik_byz_footman_1", "Chain Mail Hauberk", [("kuauik_byz_footman_1", imodbits_none)], itp_type_body_armor|itp_merchandise|itp_covers_legs|itp_doesnt_cover_hair|itp_can_penetrate_shield, 0, 4000, abundance(100)|weight(20.0)|leg_armor(5)|difficulty(12)|body_armor(37), imodbits_armor, [], [fac_kingdom_12, fac_kingdom_13, fac_kingdom_14, fac_kingdom_15, fac_kingdom_16, fac_kingdom_17, fac_kingdom_5, fac_kingdom_18]],

	["kuauik_byz_guard", "Lamellar Armor", [("kuauik_byz_guard", imodbits_none)], itp_type_body_armor|itp_merchandise|itp_covers_legs|itp_doesnt_cover_hair|itp_can_penetrate_shield, 0, 4000, abundance(100)|weight(20.0)|leg_armor(5)|difficulty(12)|body_armor(37), imodbits_armor, [], [fac_kingdom_12, fac_kingdom_13, fac_kingdom_14, fac_kingdom_15, fac_kingdom_16, fac_kingdom_17, fac_kingdom_5, fac_kingdom_18]],

	["kuauik_byz_leather", "Leather Jerkin", [("kuauik_byz_leather", imodbits_none)], itp_type_body_armor|itp_merchandise|itp_covers_legs|itp_doesnt_cover_hair|itp_can_penetrate_shield, 0, 500, abundance(100)|weight(10.0)|body_armor(22), imodbits_cloth, [], [fac_kingdom_12, fac_kingdom_13, fac_kingdom_14, fac_kingdom_15, fac_kingdom_16, fac_kingdom_17, fac_kingdom_5, fac_kingdom_18]],

	["kuauik_padded_cloth", "Chain Mail Hauberk", [("kuauik_padded_cloth", imodbits_none)], itp_type_body_armor|itp_merchandise|itp_covers_legs|itp_doesnt_cover_hair|itp_can_penetrate_shield, 0, 4000, abundance(100)|weight(20.0)|difficulty(12)|body_armor(37), imodbits_armor, [], [fac_kingdom_12, fac_kingdom_13, fac_kingdom_14, fac_kingdom_15, fac_kingdom_16, fac_kingdom_17, fac_kingdom_5, fac_kingdom_18]],

	["kuauik_varangian_a", "Lamellar Armor", [("kuauik_varangian_a", imodbits_none)], itp_type_body_armor|itp_merchandise|itp_covers_legs|itp_doesnt_cover_hair|itp_can_penetrate_shield, 0, 4000, abundance(100)|weight(20.0)|leg_armor(5)|difficulty(12)|body_armor(37), imodbits_armor, [], [fac_kingdom_12, fac_kingdom_13, fac_kingdom_14, fac_kingdom_15, fac_kingdom_16, fac_kingdom_17, fac_kingdom_5, fac_kingdom_18]],

	["kuauik_norvos_guard", "Leather Jerkin", [("kuauik_norvos_guard", imodbits_none)], itp_type_body_armor|itp_merchandise|itp_covers_legs|itp_doesnt_cover_hair|itp_can_penetrate_shield, 0, 500, abundance(100)|weight(10.0)|body_armor(20), imodbits_cloth, [], [fac_kingdom_17, fac_kingdom_5]],

	["kuauik_pentos_guard", "Lamellar Armor", [("kuauik_pentos_guard", imodbits_none)], itp_type_body_armor|itp_merchandise|itp_covers_legs|itp_doesnt_cover_hair|itp_can_penetrate_shield, 0, 4000, abundance(100)|weight(20.0)|leg_armor(5)|difficulty(12)|body_armor(40), imodbits_armor, [], [fac_kingdom_12]],

	["kuauik_volantis_guard", "Lamellar Armor", [("kuauik_volantis_guard", imodbits_none)], itp_type_body_armor|itp_merchandise|itp_covers_legs|itp_doesnt_cover_hair|itp_can_penetrate_shield, 0, 4000, abundance(100)|weight(20.0)|leg_armor(5)|difficulty(12)|body_armor(40), imodbits_armor, [], [fac_kingdom_16]],

	["kuauik_myr_guard", "Lamellar Armor", [("kuauik_myr_guard", imodbits_none)], itp_type_body_armor|itp_merchandise|itp_covers_legs|itp_doesnt_cover_hair|itp_can_penetrate_shield, 0, 4000, abundance(100)|weight(20.0)|leg_armor(4)|difficulty(12)|body_armor(37), imodbits_armor, [], [fac_kingdom_14]],

	["kuauik_surcoat_1", "Surcoat over Mail", [("kuauik_surcoat_1", imodbits_none)], itp_type_body_armor|itp_covers_legs|itp_doesnt_cover_hair|itp_can_penetrate_shield, 0, 5000, abundance(100)|weight(18.0)|leg_armor(14)|difficulty(12)|body_armor(40), imodbits_armor, [], [fac_kingdom_18]],

	["kuauik_surcoat_2", "Surcoat over Mail", [("kuauik_surcoat_2", imodbits_none)], itp_type_body_armor|itp_covers_legs|itp_doesnt_cover_hair|itp_can_penetrate_shield, 0, 5000, abundance(100)|weight(18.0)|leg_armor(14)|difficulty(12)|body_armor(40), imodbits_armor, [], [fac_kingdom_13]],

	["kuauik_surcoat_3", "Surcoat over Mail", [("kuauik_surcoat_3", imodbits_none)], itp_type_body_armor|itp_covers_legs|itp_doesnt_cover_hair|itp_can_penetrate_shield, 0, 5000, abundance(100)|weight(18.0)|leg_armor(14)|difficulty(12)|body_armor(40), imodbits_armor, [], [fac_kingdom_13]],

	["kuauik_surcoat_4", "Surcoat over Mail", [("kuauik_surcoat_4", imodbits_none)], itp_type_body_armor|itp_covers_legs|itp_doesnt_cover_hair|itp_can_penetrate_shield, 0, 5000, abundance(100)|weight(18.0)|leg_armor(14)|difficulty(12)|body_armor(40), imodbits_armor, [], [fac_kingdom_18]],

	["kuauik_surcoat_5", "Surcoat over Mail", [("kuauik_surcoat_5", imodbits_none)], itp_type_body_armor|itp_covers_legs|itp_doesnt_cover_hair|itp_can_penetrate_shield, 0, 5000, abundance(100)|weight(18.0)|leg_armor(14)|difficulty(12)|body_armor(40), imodbits_armor, [], [fac_kingdom_18]],

	["kuauik_surcoat_6", "Surcoat over Mail", [("kuauik_surcoat_6", imodbits_none)], itp_type_body_armor|itp_covers_legs|itp_doesnt_cover_hair|itp_can_penetrate_shield, 0, 5000, abundance(100)|weight(18.0)|leg_armor(14)|difficulty(12)|body_armor(40), imodbits_armor, [], [fac_kingdom_17, fac_kingdom_5]],

	["kuauik_surcoat_7", "Jasper Rivers Surcoat over Mail", [("kuauik_surcoat_7", imodbits_none)], itp_type_body_armor|itp_covers_legs|itp_doesnt_cover_hair|itp_can_penetrate_shield, 0, 5000, abundance(100)|weight(18.0)|leg_armor(14)|difficulty(12)|body_armor(35), imodbits_none, [], [fac_kingdom_17, fac_kingdom_5]],

	["kuauik_surcoat_8", "Surcoat over Mail", [("kuauik_surcoat_8", imodbits_none)], itp_type_body_armor|itp_covers_legs|itp_doesnt_cover_hair|itp_can_penetrate_shield, 0, 5000, abundance(100)|weight(18.0)|leg_armor(14)|difficulty(12)|body_armor(40), imodbits_armor, [], [fac_kingdom_12]],

	["kuauik_surcoat_9", "Surcoat over Mail", [("kuauik_surcoat_9", imodbits_none)], itp_type_body_armor|itp_covers_legs|itp_doesnt_cover_hair|itp_can_penetrate_shield, 0, 5000, abundance(100)|weight(18.0)|leg_armor(14)|difficulty(12)|body_armor(40), imodbits_armor, [], [fac_kingdom_12]],

	["kuauik_surcoat_10", "Surcoat over Mail", [("kuauik_surcoat_10", imodbits_none)], itp_type_body_armor|itp_covers_legs|itp_doesnt_cover_hair|itp_can_penetrate_shield, 0, 5000, abundance(100)|weight(18.0)|leg_armor(14)|difficulty(12)|body_armor(40), imodbits_armor, [], [fac_kingdom_17, fac_kingdom_5]],

	["kuauik_surcoat_11", "Surcoat over Mail", [("kuauik_surcoat_11", imodbits_none)], itp_type_body_armor|itp_covers_legs|itp_doesnt_cover_hair|itp_can_penetrate_shield, 0, 5000, abundance(100)|weight(18.0)|leg_armor(14)|difficulty(12)|body_armor(40), imodbits_armor, [], [fac_kingdom_9]],

	["surcoat_targaryen", "Surcoat over Mail", [("surcoat_targaryen", imodbits_none)], itp_type_body_armor|itp_covers_legs|itp_doesnt_cover_hair|itp_can_penetrate_shield, 0, 5000, abundance(100)|weight(18.0)|leg_armor(14)|difficulty(12)|body_armor(40), imodbits_armor, [], [fac_kingdom_18]],

	["surcoat_golden_company", "Surcoat over Mail", [("surcoat_golden_company", imodbits_none)], itp_type_body_armor|itp_covers_legs|itp_doesnt_cover_hair|itp_can_penetrate_shield, 0, 5000, abundance(100)|weight(18.0)|leg_armor(14)|difficulty(12)|body_armor(40), imodbits_armor, [], [fac_kingdom_18]],

	["tournament_yellow_surcoat", "Surcoat over Mail", [("tournament_yellow_surcoat", imodbits_none)], itp_type_body_armor|itp_covers_legs|itp_doesnt_cover_hair|itp_can_penetrate_shield, 0, 5000, abundance(60)|weight(18.0)|leg_armor(15)|body_armor(40)|head_armor(10), imodbits_armor, [], [fac_kingdom_1, fac_kingdom_3, fac_kingdom_5, fac_kingdom_8, fac_kingdom_9, fac_kingdom_10]],

	["tournament_white_surcoat", "Surcoat over Mail", [("tournament_white_surcoat", imodbits_none)], itp_type_body_armor|itp_covers_legs|itp_doesnt_cover_hair|itp_can_penetrate_shield, 0, 5000, abundance(60)|weight(18.0)|leg_armor(15)|body_armor(40)|head_armor(10), imodbits_armor, [], [fac_kingdom_1, fac_kingdom_3, fac_kingdom_5, fac_kingdom_8, fac_kingdom_9, fac_kingdom_10]],

	["tournament_red_surcoat", "Surcoat over Mail", [("tournament_red_surcoat", imodbits_none)], itp_type_body_armor|itp_covers_legs|itp_doesnt_cover_hair|itp_can_penetrate_shield, 0, 5000, abundance(60)|weight(18.0)|leg_armor(15)|body_armor(40)|head_armor(10), imodbits_armor, [], [fac_kingdom_1, fac_kingdom_3, fac_kingdom_5, fac_kingdom_8, fac_kingdom_9, fac_kingdom_10]],

	["tournament_surcoat_blue", "Surcoat over Mail", [("tournament_surcoat_blue", imodbits_none)], itp_type_body_armor|itp_covers_legs|itp_doesnt_cover_hair|itp_can_penetrate_shield, 0, 5000, abundance(60)|weight(18.0)|leg_armor(15)|body_armor(40)|head_armor(10), imodbits_armor, [], [fac_kingdom_1, fac_kingdom_3, fac_kingdom_5, fac_kingdom_8, fac_kingdom_9, fac_kingdom_10]],

	["surcoat_new_lannister", "Surcoat over Mail", [("surcoat_new_lannister", imodbits_none)], itp_type_body_armor|itp_covers_legs|itp_doesnt_cover_hair|itp_can_penetrate_shield, 0, 5000, abundance(100)|weight(18.0)|leg_armor(14)|difficulty(12)|body_armor(40), imodbits_armor, [], [fac_kingdom_9]],

	["surcoat_new_morrigen", "Surcoat over Mail", [("surcoat_new_morrigen", imodbits_none)], itp_type_body_armor|itp_covers_legs|itp_doesnt_cover_hair|itp_can_penetrate_shield, 0, 5000, abundance(100)|weight(18.0)|leg_armor(14)|difficulty(12)|body_armor(40), imodbits_armor, [], [fac_kingdom_9]],

	["surcoat_new_florent", "Surcoat over Mail", [("surcoat_new_florent", imodbits_none)], itp_type_body_armor|itp_covers_legs|itp_doesnt_cover_hair|itp_can_penetrate_shield, 0, 5000, abundance(100)|weight(18.0)|leg_armor(14)|difficulty(12)|body_armor(40), imodbits_armor, [], [fac_kingdom_9]],

	["surcoat_new_tarth", "Surcoat over Mail", [("surcoat_new_tarth", imodbits_none)], itp_type_body_armor|itp_covers_legs|itp_doesnt_cover_hair|itp_can_penetrate_shield, 0, 5000, abundance(100)|weight(18.0)|leg_armor(14)|difficulty(12)|body_armor(40), imodbits_armor, [], [fac_kingdom_9]],

	["surcoat_longbow_hall", "Surcoat over Mail", [("surcoat_longbow_hall", imodbits_none)], itp_type_body_armor|itp_covers_legs|itp_doesnt_cover_hair|itp_can_penetrate_shield, 0, 5000, abundance(100)|weight(18.0)|leg_armor(14)|difficulty(12)|body_armor(40), imodbits_armor, [], [fac_kingdom_9]],

	["surcoat_white_harbor", "Surcoat over Mail", [("surcoat_white_harbor", imodbits_none)], itp_type_body_armor|itp_covers_legs|itp_doesnt_cover_hair|itp_can_penetrate_shield, 0, 5000, abundance(100)|weight(18.0)|leg_armor(14)|difficulty(12)|body_armor(40), imodbits_armor, [], [fac_kingdom_9]],

	["surcoat_driftmark", "Surcoat over Mail", [("surcoat_driftmark", imodbits_none)], itp_type_body_armor|itp_covers_legs|itp_doesnt_cover_hair|itp_can_penetrate_shield, 0, 5000, abundance(100)|weight(18.0)|leg_armor(14)|difficulty(12)|body_armor(40), imodbits_armor, [], [fac_kingdom_9]],

	["surcoat_massey", "Surcoat over Mail", [("surcoat_massey", imodbits_none)], itp_type_body_armor|itp_covers_legs|itp_doesnt_cover_hair|itp_can_penetrate_shield, 0, 5000, abundance(100)|weight(18.0)|leg_armor(14)|difficulty(12)|body_armor(40), imodbits_armor, [], [fac_kingdom_9]],

	["surcoat_qorgyle", "Surcoat over Mail", [("surcoat_qorgyle", imodbits_none)], itp_type_body_armor|itp_covers_legs|itp_doesnt_cover_hair|itp_can_penetrate_shield, 0, 5000, abundance(100)|weight(18.0)|leg_armor(14)|difficulty(12)|body_armor(40), imodbits_armor, [], [fac_kingdom_9]],

	["surcoat_oldtown", "Surcoat over Mail", [("surcoat_oldtown", imodbits_none)], itp_type_body_armor|itp_covers_legs|itp_doesnt_cover_hair|itp_can_penetrate_shield, 0, 5000, abundance(100)|weight(18.0)|leg_armor(14)|difficulty(12)|body_armor(40), imodbits_armor, [], [fac_kingdom_9]],

	["surcoat_hellholt", "Surcoat over Mail", [("surcoat_hellholt", imodbits_none)], itp_type_body_armor|itp_covers_legs|itp_doesnt_cover_hair|itp_can_penetrate_shield, 0, 5000, abundance(100)|weight(18.0)|leg_armor(14)|difficulty(12)|body_armor(40), imodbits_armor, [], [fac_kingdom_9]],

	["trial_surcoat", "Tolletts Surcoat over Mail", [("kuauik_surcoat_8", imodbits_none)], itp_type_body_armor|itp_covers_legs|itp_doesnt_cover_hair|itp_can_penetrate_shield, 0, 5000, abundance(60)|weight(18.0)|leg_armor(7)|body_armor(27), imodbits_armor, [], [fac_kingdom_1, fac_kingdom_3, fac_kingdom_5, fac_kingdom_8, fac_kingdom_9, fac_kingdom_10]],

	["trial_shield", "Tolletts Kite Shield", [("witcher_kite_12", imodbits_none)], itp_type_shield|itp_wooden_parry, itcf_carry_kite_shield, 300, hit_points(200)|spd_rtng(76)|abundance(60)|weight(4.0)|shield_width(36)|shield_height(70)|body_armor(2), imodbits_shield, [], [fac_kingdom_12, fac_kingdom_17, fac_kingdom_5, fac_kingdom_18]],

	["trial_boots", "Splinted Mail Greaves", [("bo_rho_t5_greaves", imodbits_none)], itp_type_foot_armor|itp_attach_armature|itp_attachment_mask, 0, 1000, abundance(60)|weight(3.0)|leg_armor(20), imodbits_armor, [], [fac_kingdom_11, fac_kingdom_19]],

	["trial_gloves", "Mail Gauntlets", [("full_glove3_L", imodbits_none)], itp_type_hand_armor, 0, 400, abundance(60)|weight(2.0)|body_armor(5), imodbits_armor],

	["trial_helm", "Helmet with Faceplate", [("munitionshelm2", imodbits_none)], itp_type_head_armor|itp_fit_to_head|itp_offset_lance|itp_covers_beard, 0, 1800, abundance(10)|weight(4.0)|head_armor(32), imodbits_plate, [], [fac_kingdom_1, fac_kingdom_8]],

	["trial_sword", "Arming Sword", [("medium_tier_sword_2", imodbits_none), ("medium_tier_sword_2_scab", ixmesh_carry)], itp_type_one_handed_wpn|itp_primary, itcf_carry_sword_left_hip|itcf_show_holster_when_drawn|itc_longsword, 800, thrust_damage(32, pierce)|hit_points(29696)|spd_rtng(100)|abundance(10)|weight(2.0)|swing_damage(29, cut)|weapon_length(87), imodbits_sword_high],

	["brawl_senlac", "Arming Sword", [("medium_tier_sword_2", imodbits_none), ("medium_tier_sword_2_scab", ixmesh_carry)], itp_type_one_handed_wpn|itp_primary, itcf_carry_sword_left_hip|itcf_show_holster_when_drawn|itc_longsword, 800, thrust_damage(32, pierce)|hit_points(29696)|spd_rtng(100)|abundance(10)|weight(2.0)|swing_damage(29, cut)|weapon_length(87), imodbits_sword_high],

	["we_nor_axe_throw_light", "Throwing Axes", [("axe_e", imodbits_none)], itp_type_thrown|itp_merchandise|itp_primary|itp_civilian|itp_next_item_as_melee, itcf_throw_axe, 100, thrust_damage(31, cut)|max_ammo(5)|spd_rtng(99)|abundance(10)|weight(5.0)|difficulty(1)|weapon_length(53)|shoot_speed(18), imodbits_thrown_minus_heavy, [], [fac_kingdom_11]],

	["we_nor_axe_throw_light_melee", "Throwing Axe", [("axe_e", imodbits_none)], itp_type_one_handed_wpn|itp_primary|itp_bonus_against_shield, itc_scimitar, 100, hit_points(23552)|spd_rtng(99)|abundance(10)|weight(1.0)|swing_damage(23, cut)|difficulty(1)|weapon_length(53), imodbits_thrown_minus_heavy, [], [fac_kingdom_11]],

	["robert_baratheons_helmet", "Robert Baratheons Great Helmet", [("robert_baratheons_helmet", imodbits_none)], itp_type_head_armor|itp_covers_head|itp_couchable|itp_covers_beard, 0, 1500, abundance(40)|weight(6.0)|difficulty(14)|head_armor(45), imodbits_none, [], [fac_kingdom_1]],

	["fi_tourney_helmet_1", "Decorated Tournament Helmet", [("fi_tourney_helmet_1", imodbits_none)], itp_type_head_armor|itp_unique|itp_covers_head|itp_couchable|itp_covers_beard, 0, 2500, abundance(40)|weight(6.0)|difficulty(14)|head_armor(45), imodbits_none, [], [fac_kingdom_1]],

	["fi_greathelmet_1", "Decorated Tournament Helmet", [("fi_greathelmet_1", imodbits_none)], itp_type_head_armor|itp_unique|itp_covers_head|itp_couchable|itp_covers_beard, 0, 2500, abundance(40)|weight(6.0)|difficulty(14)|head_armor(45), imodbits_none, [], [fac_kingdom_1]],

	["fi_armet_2", "Decorated Tournament Helmet", [("fi_armet_2", imodbits_none)], itp_type_head_armor|itp_unique|itp_covers_head|itp_couchable|itp_covers_beard, 0, 2500, abundance(40)|weight(6.0)|difficulty(14)|head_armor(45), imodbits_none, [], [fac_kingdom_1]],

	["crown_sallet", "Sallet with Crown", [("crown_sallet", imodbits_none)], itp_type_head_armor|itp_fit_to_head|itp_offset_lance, 0, 1300, abundance(50)|weight(4.0)|difficulty(12)|head_armor(37), imodbits_none, [], [fac_kingdom_3]],

	["crown_coif", "Mail Coif with Crown", [("crown_coif", imodbits_none)], itp_type_head_armor|itp_fit_to_head|itp_offset_lance, 0, 1300, abundance(50)|weight(4.0)|difficulty(12)|head_armor(37), imodbits_none, [], [fac_kingdom_3]],

	["nord_coat_of_plates", "Heavy Leather Armor", [("nord_coat_of_plates", imodbits_none)], itp_type_body_armor|itp_merchandise|itp_covers_legs|itp_doesnt_cover_hair|itp_can_penetrate_shield, 0, 6000, abundance(40)|weight(25.0)|leg_armor(18)|difficulty(14)|body_armor(45), imodbits_armor, [], [fac_kingdom_11]],

	["nord_coat_of_plates_pelt", "Heavy Leather Armor", [("nord_coat_of_plates_pelt", imodbits_none)], itp_type_body_armor|itp_merchandise|itp_covers_legs|itp_doesnt_cover_hair|itp_can_penetrate_shield, 0, 6000, abundance(40)|weight(25.0)|leg_armor(18)|difficulty(14)|body_armor(45), imodbits_armor, [], [fac_kingdom_11]],

	["fi_lance", "Tourney Lance", [("fi_lance", imodbits_none)], itp_type_polearm|itp_merchandise|itp_wooden_parry|itp_primary|itp_penalty_with_shield|itp_fit_to_head|itp_offset_lance|itp_covers_head|itp_couchable, itc_staff, 700, thrust_damage(35, pierce)|spd_rtng(96)|abundance(40)|weight(5.0)|swing_damage(0, blunt)|weapon_length(250), imodbits_none, [], [fac_kingdom_1, fac_kingdom_3, fac_kingdom_8, fac_kingdom_9, fac_kingdom_10]],

	["bb_rus_pike", "War Lance", [("bb_rus_pike", imodbits_none)], itp_type_polearm|itp_merchandise|itp_wooden_parry|itp_primary|itp_penalty_with_shield|itp_fit_to_head|itp_offset_lance|itp_covers_head|itp_couchable, itc_staff, 700, thrust_damage(35, pierce)|spd_rtng(96)|abundance(100)|weight(5.0)|swing_damage(0, blunt)|weapon_length(248), imodbits_none],

	["sipahi_jawshan", "Heavy Plate Armor", [("sipahi_jawshan", imodbits_none)], itp_type_body_armor|itp_merchandise|itp_covers_legs|itp_doesnt_cover_hair|itp_can_penetrate_shield, 0, 9000, abundance(5)|weight(20.0)|leg_armor(12)|difficulty(14)|body_armor(54), imodbits_plate, [], [fac_kingdom_12, fac_kingdom_13, fac_kingdom_14, fac_kingdom_15, fac_kingdom_16, fac_kingdom_17, fac_kingdom_18]],

	["peltastos_armor", "Gambeson", [("peltastos_armor", imodbits_none)], itp_type_body_armor|itp_merchandise|itp_covers_legs|itp_doesnt_cover_hair|itp_can_penetrate_shield, 0, 200, abundance(5)|weight(5.0)|leg_armor(4)|body_armor(16), imodbits_cloth, [], [fac_kingdom_12, fac_kingdom_13, fac_kingdom_14, fac_kingdom_15, fac_kingdom_16, fac_kingdom_17, fac_kingdom_18]],

	["mongolian_helmet", "Top Helmet", [("mongolian_helmet", imodbits_none)], itp_type_head_armor|itp_merchandise, 0, 1400, abundance(10)|weight(4.0)|difficulty(12)|head_armor(33), imodbits_armor, [], [fac_kingdom_12, fac_kingdom_13, fac_kingdom_14, fac_kingdom_15, fac_kingdom_16, fac_kingdom_17, fac_kingdom_18]],

	["jack_boots_unsullied", "Unsullied Shoes", [("jack_boots_unsullied", imodbits_none)], itp_type_foot_armor|itp_attach_armature|itp_attachment_mask|itp_civilian|itp_next_item_as_melee, 0, 50, abundance(60)|weight(1.0)|leg_armor(7), imodbits_cloth],

	["jack_armour_unsullied", "Unsullied Tunic", [("jack_armour_unsullied", imodbits_none)], itp_type_body_armor|itp_covers_legs|itp_doesnt_cover_hair|itp_can_penetrate_shield|itp_civilian|itp_next_item_as_melee, 0, 1000, abundance(5)|weight(20.0)|leg_armor(8)|body_armor(37), imodbits_cloth, [], [fac_kingdom_12, fac_kingdom_13, fac_kingdom_14, fac_kingdom_15, fac_kingdom_16, fac_kingdom_17, fac_kingdom_18]],

	["jack_helmet_unsullied", "Unsullied Helmet", [("jack_helmet_unsullied", imodbits_none)], itp_type_head_armor|itp_civilian|itp_next_item_as_melee, 0, 800, abundance(10)|weight(4.0)|head_armor(33), imodbits_armor, [], [fac_kingdom_12, fac_kingdom_13, fac_kingdom_14, fac_kingdom_15, fac_kingdom_16, fac_kingdom_17, fac_kingdom_18]],

	["jack_helmet_burgonet", "Burgonet", [("jack_helmet_burgonet", imodbits_none)], itp_type_head_armor|itp_merchandise, 0, 1400, abundance(10)|weight(4.0)|difficulty(12)|head_armor(33), imodbits_armor, [], [fac_kingdom_1]],

	["jack_helmet_burgonet_iron", "Burgonet", [("jack_helmet_burgonet_iron", imodbits_none)], itp_type_head_armor|itp_merchandise, 0, 1400, abundance(10)|weight(4.0)|difficulty(12)|head_armor(33), imodbits_armor, [], [fac_kingdom_8]],

	["unsullied_shield", "Unsullied Shield", [("unsullied_shield", imodbits_none)], itp_type_shield|itp_wooden_parry|itp_civilian|itp_next_item_as_melee, itcf_carry_round_shield, 300, hit_points(200)|spd_rtng(87)|abundance(60)|weight(4.0)|shield_width(65)|body_armor(5), imodbits_none, [], [fac_kingdom_11]],

	["pretender_vezenkor", "Expensive Lamellar Armor", [("rathos_lamellar_armor_2", imodbits_none)], itp_type_body_armor|itp_covers_legs|itp_doesnt_cover_hair|itp_can_penetrate_shield|itp_civilian|itp_next_item_as_melee, 0, 4000, abundance(20)|weight(16.0)|leg_armor(15)|difficulty(12)|body_armor(37), imodbits_armor, [], [fac_kingdom_11, fac_kingdom_19]],

	["pretender_yara", "Chain Mail Hauberk", [("drz_mail_shirt", imodbits_none)], itp_type_body_armor|itp_covers_legs|itp_doesnt_cover_hair|itp_can_penetrate_shield|itp_civilian|itp_next_item_as_melee, 0, 4000, abundance(20)|weight(16.0)|leg_armor(15)|difficulty(12)|body_armor(37), imodbits_armor, [], [fac_kingdom_11, fac_kingdom_19]],

	["pretender_laros", "Surcoat over Mail", [("tournament_white_surcoat", imodbits_none)], itp_type_body_armor|itp_covers_legs|itp_doesnt_cover_hair|itp_can_penetrate_shield|itp_civilian|itp_next_item_as_melee, 0, 4000, abundance(20)|weight(16.0)|leg_armor(15)|difficulty(12)|body_armor(37), imodbits_armor, [], [fac_kingdom_11, fac_kingdom_19]],

	["pretender_assadora", "Lamellar Armor", [("kuauik_dothraki_mail", imodbits_none)], itp_type_body_armor|itp_covers_legs|itp_doesnt_cover_hair|itp_can_penetrate_shield|itp_civilian|itp_next_item_as_melee, 0, 2000, abundance(20)|weight(16.0)|leg_armor(15)|difficulty(12)|body_armor(20), imodbits_armor, [], [fac_kingdom_11, fac_kingdom_19]],

	["pretender_sarella", "Surcoat over Mail", [("tournament_red_surcoat", imodbits_none)], itp_type_body_armor|itp_covers_legs|itp_doesnt_cover_hair|itp_can_penetrate_shield|itp_civilian|itp_next_item_as_melee, 0, 4000, abundance(20)|weight(16.0)|leg_armor(15)|difficulty(12)|body_armor(37), imodbits_armor, [], [fac_kingdom_11, fac_kingdom_19]],

	["pretender_shiera", "Expensive Lamellar Armor", [("rathos_lamellar_armor_1", imodbits_none)], itp_type_body_armor|itp_covers_legs|itp_doesnt_cover_hair|itp_can_penetrate_shield|itp_civilian|itp_next_item_as_melee, 0, 4000, abundance(20)|weight(16.0)|leg_armor(15)|difficulty(12)|body_armor(37), imodbits_armor, [], [fac_kingdom_11, fac_kingdom_19]],

	["rathos_lamellar_armor_2", "Expensive Lamellar Armor", [("rathos_lamellar_armor_2", imodbits_none)], itp_type_body_armor|itp_covers_legs|itp_doesnt_cover_hair|itp_can_penetrate_shield, 0, 4000, abundance(20)|weight(16.0)|leg_armor(15)|difficulty(12)|body_armor(37), imodbits_armor, [], [fac_kingdom_11, fac_kingdom_19]],

	["low_tier_sword_1", "Arming Sword", [("low_tier_sword_1", imodbits_none), ("low_tier_sword_1_scab", ixmesh_carry)], itp_type_one_handed_wpn|itp_merchandise|itp_primary, itcf_carry_sword_left_hip|itcf_show_holster_when_drawn|itc_longsword, 500, thrust_damage(27, pierce)|hit_points(25600)|spd_rtng(100)|abundance(10)|weight(2.0)|swing_damage(25, cut)|difficulty(12)|weapon_length(76), imodbits_sword_high],

	["medium_tier_sword_1", "Arming Sword", [("medium_tier_sword_1", imodbits_none), ("medium_tier_sword_1_scab", ixmesh_carry)], itp_type_one_handed_wpn|itp_merchandise|itp_primary, itcf_carry_sword_left_hip|itcf_show_holster_when_drawn|itc_longsword, 1000, thrust_damage(32, pierce)|hit_points(29696)|spd_rtng(100)|abundance(10)|weight(2.0)|swing_damage(29, cut)|difficulty(12)|weapon_length(96), imodbits_sword_high],

	["medium_tier_sword_2", "Arming Sword", [("medium_tier_sword_2", imodbits_none), ("medium_tier_sword_2_scab", ixmesh_carry)], itp_type_one_handed_wpn|itp_merchandise|itp_primary, itcf_carry_sword_left_hip|itcf_show_holster_when_drawn|itc_longsword, 1000, thrust_damage(32, pierce)|hit_points(29696)|spd_rtng(100)|abundance(10)|weight(2.0)|swing_damage(29, cut)|difficulty(12)|weapon_length(94), imodbits_sword_high],

	["medium_tier_sword_3", "Arming Sword", [("medium_tier_sword_3", imodbits_none), ("medium_tier_sword_3_scab", ixmesh_carry)], itp_type_one_handed_wpn|itp_merchandise|itp_primary, itcf_carry_sword_left_hip|itcf_show_holster_when_drawn|itc_longsword, 1000, thrust_damage(32, pierce)|hit_points(29696)|spd_rtng(100)|abundance(10)|weight(2.0)|swing_damage(29, cut)|difficulty(12)|weapon_length(86), imodbits_sword_high],

	["high_tier_sword_1", "Castle-Forged Arming Sword", [("high_tier_sword_1", imodbits_none), ("high_tier_sword_1_scab", ixmesh_carry)], itp_type_one_handed_wpn|itp_merchandise|itp_primary, itcf_carry_sword_left_hip|itcf_show_holster_when_drawn|itc_longsword, 1500, thrust_damage(34, pierce)|hit_points(32768)|spd_rtng(105)|abundance(10)|weight(2.0)|swing_damage(32, cut)|difficulty(12)|weapon_length(94), imodbits_sword_high, [], [fac_kingdom_1, fac_kingdom_2, fac_kingdom_3, fac_kingdom_6, fac_kingdom_8, fac_kingdom_9, fac_kingdom_10, fac_kingdom_11, fac_kingdom_19]],

	["high_tier_sword_2", "Castle-Forged Arming Sword", [("high_tier_sword_2", imodbits_none), ("high_tier_sword_2_scab", ixmesh_carry)], itp_type_one_handed_wpn|itp_merchandise|itp_primary, itcf_carry_sword_left_hip|itcf_show_holster_when_drawn|itc_longsword, 1500, thrust_damage(34, pierce)|hit_points(32768)|spd_rtng(105)|abundance(10)|weight(2.0)|swing_damage(32, cut)|difficulty(12)|weapon_length(85), imodbits_sword_high, [], [fac_kingdom_1, fac_kingdom_2, fac_kingdom_3, fac_kingdom_6, fac_kingdom_8, fac_kingdom_9, fac_kingdom_10, fac_kingdom_11, fac_kingdom_19]],

	["low_tier_saber_1", "Curved Sword", [("low_tier_saber_1", imodbits_none), ("low_tier_saber_1_scab", ixmesh_carry)], itp_type_one_handed_wpn|itp_merchandise|itp_primary, itcf_carry_sword_left_hip|itcf_show_holster_when_drawn|itc_scimitar, 500, hit_points(22528)|spd_rtng(106)|abundance(100)|weight(1.5)|swing_damage(22, cut)|weapon_length(95), imodbits_sword_high, [], [fac_kingdom_6]],

	["medium_tier_saber_1", "Curved Sword", [("medium_tier_saber_1", imodbits_none), ("medium_tier_saber_1_scab", ixmesh_carry)], itp_type_one_handed_wpn|itp_merchandise|itp_primary, itcf_carry_sword_left_hip|itcf_show_holster_when_drawn|itc_scimitar, 900, hit_points(25600)|spd_rtng(108)|abundance(100)|weight(1.5)|swing_damage(25, cut)|weapon_length(87), imodbits_sword_high, [], [fac_kingdom_6]],

	["high_tier_saber_1", "Castle-Forged Curved Sword", [("high_tier_saber_1", imodbits_none), ("high_tier_saber_1_scab", ixmesh_carry)], itp_type_one_handed_wpn|itp_merchandise|itp_primary, itcf_carry_sword_left_hip|itcf_show_holster_when_drawn|itc_scimitar, 1100, hit_points(32768)|spd_rtng(110)|abundance(100)|weight(1.5)|swing_damage(32, cut)|weapon_length(88), imodbits_sword_high, [], [fac_kingdom_6]],

	["high_tier_saber_2", "Castle-Forged Curved Sword", [("high_tier_saber_2", imodbits_none), ("high_tier_saber_2_scab", ixmesh_carry)], itp_type_one_handed_wpn|itp_merchandise|itp_primary, itcf_carry_sword_left_hip|itcf_show_holster_when_drawn|itc_scimitar, 1100, hit_points(32768)|spd_rtng(110)|abundance(100)|weight(1.5)|swing_damage(32, cut)|weapon_length(95), imodbits_sword_high, [], [fac_kingdom_6]],

	["we_rho_sword_rondeldagger", "Short Sword", [("Faradon_onehanded", imodbits_none)], itp_type_one_handed_wpn|itp_primary|itp_secondary, itcf_carry_sword_left_hip|itc_longsword, 600, thrust_damage(28, pierce)|hit_points(20480)|spd_rtng(110)|abundance(10)|weight(2.0)|swing_damage(20, cut)|difficulty(10)|weapon_length(80), imodbits_sword_high, [], [fac_kingdom_4, fac_kingdom_12, fac_kingdom_13, fac_kingdom_14, fac_kingdom_15, fac_kingdom_16, fac_kingdom_18]],

	["sword_rusty_a", "Rusty Sword", [("low_tier_sword_3", imodbits_none), ("low_tier_sword_3_scab", ixmesh_carry)], itp_type_one_handed_wpn|itp_merchandise|itp_primary, itcf_carry_sword_left_hip|itcf_show_holster_when_drawn|itc_longsword, 200, thrust_damage(20, pierce)|hit_points(18432)|spd_rtng(90)|abundance(10)|weight(2.0)|swing_damage(18, cut)|difficulty(10)|weapon_length(93), imodbits_none, [], [fac_kingdom_2, fac_kingdom_11, fac_kingdom_19]],

	["loki_sword", "Old Arming Sword", [("low_tier_sword_3", imodbits_none)], itp_type_one_handed_wpn|itp_primary|itp_secondary, itcf_carry_sword_left_hip|itc_longsword, 200, thrust_damage(23, pierce)|hit_points(23552)|spd_rtng(100)|abundance(30)|weight(2.0)|swing_damage(23, cut)|difficulty(10)|weapon_length(92), imodbits_none, [], [fac_kingdom_4, fac_kingdom_12, fac_kingdom_17, fac_kingdom_5, fac_kingdom_18]],

	["orphanmaker", "Orphan-Maker", [("valyrian_blade_orphan_maker", imodbits_none), ("valyrian_blade_orphan_maker_scab", ixmesh_carry)], itp_type_one_handed_wpn|itp_primary|itp_covers_legs|itp_doesnt_cover_hair|itp_can_penetrate_shield|itp_bonus_against_shield, itcf_carry_sword_left_hip|itcf_show_holster_when_drawn|itc_longsword, 20000, thrust_damage(39, pierce)|hit_points(37888)|spd_rtng(115)|abundance(30)|weight(2.0)|swing_damage(37, cut)|difficulty(12)|weapon_length(100), imodbits_none, [], [fac_kingdom_11, fac_kingdom_19]],

	["sword_repent", "Dark Sister", [("valyrian_blade_dark_sister", imodbits_none), ("valyrian_blade_dark_sister_scab", ixmesh_carry)], itp_type_one_handed_wpn|itp_primary|itp_covers_legs|itp_doesnt_cover_hair|itp_can_penetrate_shield|itp_bonus_against_shield, itcf_carry_sword_left_hip|itcf_show_holster_when_drawn|itc_longsword, 20000, thrust_damage(39, pierce)|hit_points(37888)|spd_rtng(115)|abundance(30)|weight(2.0)|swing_damage(37, cut)|difficulty(12)|weapon_length(94), imodbits_none, [], [fac_kingdom_11, fac_kingdom_19]],

	["dragonstone_mailed", "Chain Mail Hauberk", [("dragonstone_mailed", imodbits_none)], itp_type_body_armor|itp_merchandise|itp_covers_legs|itp_doesnt_cover_hair|itp_can_penetrate_shield, 0, 4000, abundance(55)|weight(20.0)|leg_armor(15)|difficulty(12)|body_armor(37), imodbits_armor, [], [fac_kingdom_8]],

	["dragonstone_plate2", "Light Plate Armor", [("dragonstone_plate2", imodbits_none)], itp_type_body_armor|itp_merchandise|itp_covers_legs|itp_doesnt_cover_hair|itp_can_penetrate_shield, 0, 4500, abundance(55)|weight(20.0)|leg_armor(15)|difficulty(12)|body_armor(40), imodbits_armor, [], [fac_kingdom_8]],

	["dragonstone_lord", "Light Plate Armor", [("dragonstone_lord", imodbits_none)], itp_type_body_armor|itp_merchandise|itp_covers_legs|itp_doesnt_cover_hair|itp_can_penetrate_shield, 0, 4500, abundance(55)|weight(20.0)|leg_armor(15)|difficulty(12)|body_armor(40), imodbits_armor, [], [fac_kingdom_8]],

	["dragonstone_padded1", "Padded Robe", [("dragonstone_padded1", imodbits_none)], itp_type_body_armor|itp_merchandise|itp_covers_legs|itp_doesnt_cover_hair|itp_can_penetrate_shield, 0, 200, abundance(55)|weight(5.0)|leg_armor(4)|body_armor(16), imodbits_cloth, [], [fac_kingdom_8]],

	["dragonstone_padded2", "Padded Robe", [("dragonstone_padded2", imodbits_none)], itp_type_body_armor|itp_merchandise|itp_covers_legs|itp_doesnt_cover_hair|itp_can_penetrate_shield, 0, 200, abundance(55)|weight(5.0)|leg_armor(4)|body_armor(16), imodbits_cloth, [], [fac_kingdom_8]],

	["dragonstone_court_davos", "Padded Robe", [("dragonstone_court_davos", imodbits_none)], itp_type_body_armor|itp_covers_legs|itp_doesnt_cover_hair|itp_can_penetrate_shield|itp_civilian|itp_next_item_as_melee, 0, 200, abundance(5)|weight(5.0)|leg_armor(4)|body_armor(16), imodbits_cloth, [], [fac_kingdom_8]],

	["dragonstone_court_matthos", "Padded Robe", [("dragonstone_court_matthos", imodbits_none)], itp_type_body_armor|itp_covers_legs|itp_doesnt_cover_hair|itp_can_penetrate_shield|itp_civilian|itp_next_item_as_melee, 0, 200, abundance(5)|weight(5.0)|leg_armor(4)|body_armor(16), imodbits_cloth, [], [fac_kingdom_8]],

	["dragonstone_gendry", "Padded Robe", [("dragonstone_gendry", imodbits_none)], itp_type_body_armor|itp_merchandise|itp_covers_legs|itp_doesnt_cover_hair|itp_can_penetrate_shield, 0, 200, abundance(5)|weight(5.0)|leg_armor(4)|body_armor(16), imodbits_cloth, [], [fac_kingdom_8]],

	["dragonstone_court_gendry", "Padded Robe", [("dragonstone_gendry", imodbits_none)], itp_type_body_armor|itp_covers_legs|itp_doesnt_cover_hair|itp_can_penetrate_shield|itp_civilian|itp_next_item_as_melee, 0, 200, abundance(5)|weight(5.0)|leg_armor(4)|body_armor(16), imodbits_cloth, [], [fac_kingdom_8]],

	["dragonstone_archer_helm", "Coif", [("dragonstone_archer_helm", imodbits_none)], itp_type_head_armor|itp_merchandise, 0, 100, abundance(10)|weight(2.0)|head_armor(6), imodbits_cloth, [], [fac_kingdom_8]],

	["dragonstone_davos_battle", "Padded Robe", [("dragonstone_davos_battle", imodbits_none)], itp_type_body_armor|itp_merchandise|itp_covers_legs|itp_doesnt_cover_hair|itp_can_penetrate_shield, 0, 200, abundance(5)|weight(5.0)|leg_armor(11)|body_armor(28), imodbits_cloth, [], [fac_kingdom_8]],

	["dragonstone_matthos_battle", "Padded Robe", [("dragonstone_matthos_battle", imodbits_none)], itp_type_body_armor|itp_merchandise|itp_covers_legs|itp_doesnt_cover_hair|itp_can_penetrate_shield, 0, 200, abundance(5)|weight(5.0)|leg_armor(11)|body_armor(28), imodbits_cloth, [], [fac_kingdom_8]],

	["dragonstone_archer_helm_burgonet", "Burgonet", [("dragonstone_archer_helm_burgonet", imodbits_none)], itp_type_head_armor|itp_merchandise, 0, 1400, abundance(10)|weight(4.0)|difficulty(12)|head_armor(33), imodbits_armor, [], [fac_kingdom_8]],

	["mackie_falchion01", "Falchion", [("mackie_falchion01", imodbits_none)], itp_type_one_handed_wpn|itp_primary|itp_bonus_against_shield, itcf_carry_sword_left_hip|itc_scimitar, 700, hit_points(25600)|spd_rtng(110)|abundance(100)|weight(1.5)|swing_damage(25, cut)|weapon_length(74), imodbits_sword_high, [], [fac_kingdom_6]],

	["mackie_falchion03", "Falchion", [("falchion_1", imodbits_none)], itp_type_one_handed_wpn|itp_primary|itp_bonus_against_shield, itcf_carry_sword_left_hip|itc_scimitar, 700, hit_points(25600)|spd_rtng(110)|abundance(100)|weight(1.5)|swing_damage(25, cut)|weapon_length(71), imodbits_sword_high, [], [fac_kingdom_6]],

	["mackie_cutlass", "Falchion", [("falchion_2", imodbits_none)], itp_type_one_handed_wpn|itp_primary|itp_bonus_against_shield, itcf_carry_sword_left_hip|itc_scimitar, 700, hit_points(25600)|spd_rtng(110)|abundance(100)|weight(1.5)|swing_damage(25, cut)|weapon_length(74), imodbits_sword_high, [], [fac_kingdom_6]],

	["stormlands_hammer_event", "War Hammer", [("fi_small_hammer", imodbits_none)], itp_type_one_handed_wpn|itp_wooden_parry|itp_primary|itp_bonus_against_shield|itp_crush_through, itcf_carry_mace_left_hip|itc_scimitar, 1000, thrust_damage(0, pierce)|hit_points(30720)|spd_rtng(100)|abundance(100)|weight(4.0)|swing_damage(30, blunt)|difficulty(12)|weapon_length(44), imodbits_axe|imodbits_mace, [], [fac_kingdom_1]],

	["stormlands_hammer", "War Hammer", [("fi_small_hammer", imodbits_none)], itp_type_one_handed_wpn|itp_merchandise|itp_wooden_parry|itp_primary|itp_bonus_against_shield|itp_crush_through, itcf_carry_mace_left_hip|itc_scimitar, 1000, thrust_damage(0, pierce)|hit_points(26624)|spd_rtng(100)|abundance(100)|weight(4.0)|swing_damage(26, blunt)|difficulty(12)|weapon_length(44), imodbits_axe|imodbits_mace, [], [fac_kingdom_1]],

	["stormlands_two_handed_hammer", "Two-Handed War Hammer", [("fi_pole_hammer", imodbits_none)], itp_type_two_handed_wpn|itp_merchandise|itp_wooden_parry|itp_two_handed|itp_primary|itp_bonus_against_shield|itp_cant_use_on_horseback|itp_crush_through|itp_can_knock_down, itcf_carry_axe_back|itc_nodachi, 1000, thrust_damage(0, blunt)|hit_points(40960)|spd_rtng(70)|abundance(80)|weight(7.0)|swing_damage(40, blunt)|difficulty(12)|weapon_length(100), imodbits_axe|imodbits_mace, [], [fac_kingdom_1]],

	["sellsword_club", "Studded Club", [("Faradon_LargeClub", imodbits_none)], itp_type_one_handed_wpn|itp_merchandise|itp_wooden_parry|itp_primary|itp_bonus_against_shield, itc_scimitar, 300, thrust_damage(0, pierce)|hit_points(20480)|spd_rtng(100)|abundance(100)|weight(4.0)|swing_damage(20, blunt)|difficulty(12)|weapon_length(91), imodbits_axe|imodbits_mace, [], [fac_kingdom_16]],

	["sellsword_iron_club", "Iron Club", [("Faradon_IronClub", imodbits_none)], itp_type_one_handed_wpn|itp_merchandise|itp_wooden_parry|itp_primary|itp_bonus_against_shield, itc_scimitar, 500, thrust_damage(0, pierce)|hit_points(24576)|spd_rtng(100)|abundance(100)|weight(4.0)|swing_damage(24, blunt)|difficulty(12)|weapon_length(96), imodbits_axe|imodbits_mace, [], [fac_kingdom_16]],

	["necturus_item_buckler_1", "Buckler", [("necturus_item_buckler_1", imodbits_none)], itp_type_shield|itp_wooden_parry, itcf_carry_round_shield, 500, hit_points(250)|spd_rtng(87)|abundance(60)|weight(5.0)|shield_width(66)|difficulty(2)|body_armor(15), imodbits_none, [], [fac_kingdom_4, fac_kingdom_5, fac_kingdom_12, fac_kingdom_13, fac_kingdom_14, fac_kingdom_15, fac_kingdom_16, fac_kingdom_17, fac_kingdom_18]],

	["necturus_item_buckler_2", "Buckler", [("necturus_item_buckler_2", imodbits_none)], itp_type_shield|itp_wooden_parry, itcf_carry_round_shield, 500, hit_points(250)|spd_rtng(87)|abundance(60)|weight(5.0)|shield_width(67)|difficulty(2)|body_armor(15), imodbits_none, [], [fac_kingdom_4, fac_kingdom_5, fac_kingdom_12, fac_kingdom_13, fac_kingdom_14, fac_kingdom_15, fac_kingdom_16, fac_kingdom_17, fac_kingdom_18]],

	["necturus_item_buckler_3", "Buckler", [("necturus_item_buckler_3", imodbits_none)], itp_type_shield|itp_wooden_parry, itcf_carry_round_shield, 500, hit_points(250)|spd_rtng(87)|abundance(60)|weight(5.0)|shield_width(67)|difficulty(2)|body_armor(15), imodbits_none, [], [fac_kingdom_4, fac_kingdom_5, fac_kingdom_12, fac_kingdom_13, fac_kingdom_14, fac_kingdom_15, fac_kingdom_16, fac_kingdom_17, fac_kingdom_18]],

	["ar_sar_t7_fullplate_a", "Clansman Noblemans Tunic", [("ar_rho_mer_highlandergreen", imodbits_none)], itp_type_body_armor|itp_covers_legs|itp_doesnt_cover_hair|itp_can_penetrate_shield, 0, 50, abundance(40)|weight(4.0)|leg_armor(1)|difficulty(4)|body_armor(2), imodbits_cloth, [], [fac_kingdom_13, fac_kingdom_15, fac_kingdom_16]],

	["ar_rho_shi_capegreen", "Clansman Noblemans Tunic", [("ar_pla_mer_highlanderbrown", imodbits_none)], itp_type_body_armor|itp_covers_legs|itp_doesnt_cover_hair|itp_can_penetrate_shield|itp_civilian|itp_next_item_as_melee, 0, 50, abundance(60)|weight(4.0)|leg_armor(2)|body_armor(2), imodbits_cloth, [], [fac_kingdom_1, fac_kingdom_8, fac_kingdom_9, fac_kingdom_10, fac_kingdom_20]],

	["he_vae_t1_noble_a", "Noblemans Top Hat", [("he_vae_t1_noble_a", imodbits_none)], itp_type_head_armor|itp_civilian|itp_next_item_as_melee, 0, 3, abundance(40)|weight(1.0)|head_armor(2), imodbits_none, [], [fac_kingdom_2]],

	["he_pla_pri_priestcoif", "Noblemans Coif", [("he_pla_pri_priestcoif", imodbits_none)], itp_type_head_armor|itp_civilian|itp_next_item_as_melee, 0, 10, abundance(10)|weight(1.0)|head_armor(5), imodbits_none, [], [fac_player_faction]],

	["vale_lord_1", "Braavosi Noblemans Tunic", [("braavosi_cloak_black", imodbits_none)], itp_type_body_armor|itp_covers_legs|itp_doesnt_cover_hair|itp_can_penetrate_shield|itp_civilian|itp_next_item_as_melee, 0, 10, abundance(55)|weight(4.0)|leg_armor(1)|body_armor(4), imodbits_none, [], [fac_kingdom_1]],

	["vale_lord_2", "Braavosi Noblemans Tunic", [("braavosi_cloak_red", imodbits_none)], itp_type_body_armor|itp_covers_legs|itp_doesnt_cover_hair|itp_can_penetrate_shield|itp_civilian|itp_next_item_as_melee, 0, 10, abundance(55)|weight(4.0)|leg_armor(1)|body_armor(4), imodbits_none, [], [fac_kingdom_1]],

	["fat_wyman_style", "Fat Noblemans Tunic", [("fat_wyman_style", imodbits_none)], itp_type_body_armor|itp_covers_legs|itp_doesnt_cover_hair|itp_can_penetrate_shield|itp_civilian|itp_next_item_as_melee, 0, 10, abundance(55)|weight(4.0)|leg_armor(1)|body_armor(4), imodbits_none, [], [fac_kingdom_1]],

	["heraldic_padded_cloth", "Noblemans Heraldic Gambeson", [("noblemans_gambeson_2", imodbits_none)], itp_type_body_armor|itp_covers_legs|itp_doesnt_cover_hair|itp_can_penetrate_shield|itp_civilian|itp_next_item_as_melee, 0, 300, abundance(40)|weight(6.0)|leg_armor(5)|body_armor(15), imodbits_cloth, 
	[(ti_on_init_item,
		[
			(store_trigger_param_1, ":trigger_param_1"),
			(store_trigger_param_2, ":trigger_param_2"),
			(call_script, "script_shield_item_set_banner", "tableau_heraldic_padded_cloth", ":trigger_param_1", ":trigger_param_2")
		])]
	, [fac_kingdom_1, fac_kingdom_2, fac_kingdom_3, fac_kingdom_8, fac_kingdom_9, fac_kingdom_10]],

	["noblemans_leather_tunic_1", "Noblemans Leather Tunic", [("noblemans_leather_tunic_1", imodbits_none)], itp_type_body_armor|itp_covers_legs|itp_doesnt_cover_hair|itp_can_penetrate_shield|itp_civilian|itp_next_item_as_melee, 0, 10, abundance(55)|weight(4.0)|leg_armor(1)|body_armor(4), imodbits_none, [], [fac_kingdom_1]],

	["noblemans_leather_tunic_2", "Noblemans Leather Tunic", [("noblemans_leather_tunic_2", imodbits_none)], itp_type_body_armor|itp_covers_legs|itp_doesnt_cover_hair|itp_can_penetrate_shield|itp_civilian|itp_next_item_as_melee, 0, 10, abundance(55)|weight(4.0)|leg_armor(1)|body_armor(4), imodbits_none, [], [fac_kingdom_1]],

	["noblemans_leather_tunic_3", "Noblemans Leather Tunic", [("noblemans_leather_tunic_3", imodbits_none)], itp_type_body_armor|itp_covers_legs|itp_doesnt_cover_hair|itp_can_penetrate_shield|itp_civilian|itp_next_item_as_melee, 0, 10, abundance(55)|weight(4.0)|leg_armor(1)|body_armor(4), imodbits_none, [], [fac_kingdom_1]],

	["noblemans_leather_tunic_4", "Noblemans Leather Tunic", [("noblemans_leather_tunic_4", imodbits_none)], itp_type_body_armor|itp_covers_legs|itp_doesnt_cover_hair|itp_can_penetrate_shield|itp_civilian|itp_next_item_as_melee, 0, 10, abundance(55)|weight(4.0)|leg_armor(1)|body_armor(4), imodbits_none, [], [fac_kingdom_1]],

	["noblemans_leather_tunic_5", "Noblemans Leather Tunic", [("noblemans_leather_tunic_5", imodbits_none)], itp_type_body_armor|itp_covers_legs|itp_doesnt_cover_hair|itp_can_penetrate_shield|itp_civilian|itp_next_item_as_melee, 0, 10, abundance(55)|weight(4.0)|leg_armor(1)|body_armor(4), imodbits_none, [], [fac_kingdom_1]],

	["noblemans_gambeson_1", "Noblemans Gambeson", [("noblemans_gambeson_1", imodbits_none)], itp_type_body_armor|itp_covers_legs|itp_doesnt_cover_hair|itp_can_penetrate_shield|itp_civilian|itp_next_item_as_melee, 0, 10, abundance(55)|weight(4.0)|leg_armor(1)|body_armor(4), imodbits_none, [], [fac_kingdom_1]],

	["noblemans_gambeson_2", "Noblemans Gambeson", [("noblemans_gambeson_2", imodbits_none)], itp_type_body_armor|itp_covers_legs|itp_doesnt_cover_hair|itp_can_penetrate_shield|itp_civilian|itp_next_item_as_melee, 0, 10, abundance(55)|weight(4.0)|leg_armor(1)|body_armor(4), imodbits_none, [], [fac_kingdom_1]],

	["noblemans_gambeson_3", "Noblemans Gambeson", [("noblemans_gambeson_3", imodbits_none)], itp_type_body_armor|itp_covers_legs|itp_doesnt_cover_hair|itp_can_penetrate_shield|itp_civilian|itp_next_item_as_melee, 0, 10, abundance(55)|weight(4.0)|leg_armor(1)|body_armor(4), imodbits_none, [], [fac_kingdom_1]],

	["noblemans_tunic_4", "Noblemans Tunic", [("noblemans_tunic_4", imodbits_none)], itp_type_body_armor|itp_covers_legs|itp_doesnt_cover_hair|itp_can_penetrate_shield|itp_civilian|itp_next_item_as_melee, 0, 10, abundance(55)|weight(4.0)|leg_armor(1)|body_armor(4), imodbits_none, [], [fac_kingdom_1]],

	["noblemans_tunic_5", "Noblemans Tunic", [("noblemans_tunic_5", imodbits_none)], itp_type_body_armor|itp_covers_legs|itp_doesnt_cover_hair|itp_can_penetrate_shield|itp_civilian|itp_next_item_as_melee, 0, 10, abundance(55)|weight(4.0)|leg_armor(1)|body_armor(4), imodbits_none, [], [fac_kingdom_1]],

	["noblemans_tunic_6", "Noblemans Tunic", [("noblemans_tunic_6", imodbits_none)], itp_type_body_armor|itp_covers_legs|itp_doesnt_cover_hair|itp_can_penetrate_shield|itp_civilian|itp_next_item_as_melee, 0, 10, abundance(55)|weight(4.0)|leg_armor(1)|body_armor(4), imodbits_none, [], [fac_kingdom_1]],

	["noblemans_tunic_7", "Davos' Tunic", [("dragonstone_court_davos", imodbits_none)], itp_type_body_armor|itp_covers_legs|itp_doesnt_cover_hair|itp_can_penetrate_shield|itp_civilian|itp_next_item_as_melee, 0, 10, abundance(55)|weight(4.0)|leg_armor(1)|body_armor(4), imodbits_none, [], [fac_kingdom_1]],

	["noblemans_tunic_8", "Noblemans Tunic", [("dragonstone_court_matthos", imodbits_none)], itp_type_body_armor|itp_covers_legs|itp_doesnt_cover_hair|itp_can_penetrate_shield|itp_civilian|itp_next_item_as_melee, 0, 10, abundance(55)|weight(4.0)|leg_armor(1)|body_armor(4), imodbits_none, [], [fac_kingdom_1]],

	["noblemans_aketon", "Noblemans Aketon", [("noblemans_aketon", imodbits_none)], itp_type_body_armor|itp_covers_legs|itp_doesnt_cover_hair|itp_can_penetrate_shield|itp_civilian|itp_next_item_as_melee, 0, 10, abundance(55)|weight(4.0)|leg_armor(1)|body_armor(4), imodbits_none, [], [fac_kingdom_1]],

	["noblemans_kaftan", "Noblemans Kaftan", [("noblemans_kaftan", imodbits_none)], itp_type_body_armor|itp_covers_legs|itp_doesnt_cover_hair|itp_can_penetrate_shield|itp_civilian|itp_next_item_as_melee, 0, 10, abundance(55)|weight(4.0)|leg_armor(1)|body_armor(4), imodbits_none, [], [fac_kingdom_1]],

	["kuauik_norvoshi_style_1", "Noblemans Kaftan", [("kuauik_norvoshi_style_1", imodbits_none)], itp_type_body_armor|itp_covers_legs|itp_doesnt_cover_hair|itp_can_penetrate_shield|itp_civilian|itp_next_item_as_melee, 0, 10, abundance(55)|weight(4.0)|leg_armor(1)|body_armor(4), imodbits_none, [], [fac_kingdom_1]],

	["pentoshi_style_1", "Noblemans Kaftan", [("pentoshi_style_1", imodbits_none)], itp_type_body_armor|itp_covers_legs|itp_doesnt_cover_hair|itp_can_penetrate_shield|itp_civilian|itp_next_item_as_melee, 0, 10, abundance(55)|weight(4.0)|leg_armor(1)|body_armor(4), imodbits_none, [], [fac_kingdom_1]],

	["kuauik_volantis_style_1", "Noblemans Robe", [("kuauik_volantis_style_1", imodbits_none)], itp_type_body_armor|itp_covers_legs|itp_doesnt_cover_hair|itp_can_penetrate_shield|itp_civilian|itp_next_item_as_melee, 0, 10, abundance(55)|weight(4.0)|leg_armor(1)|body_armor(4), imodbits_none, [], [fac_kingdom_1]],

	["kuauik_volantis_style_2", "Noblemans Robe", [("kuauik_volantis_style_2", imodbits_none)], itp_type_body_armor|itp_covers_legs|itp_doesnt_cover_hair|itp_can_penetrate_shield|itp_civilian|itp_next_item_as_melee, 0, 10, abundance(55)|weight(4.0)|leg_armor(1)|body_armor(4), imodbits_none, [], [fac_kingdom_1]],

	["kuauik_volantis_style_3", "Noblemans Robe", [("kuauik_volantis_style_3", imodbits_none)], itp_type_body_armor|itp_covers_legs|itp_doesnt_cover_hair|itp_can_penetrate_shield|itp_civilian|itp_next_item_as_melee, 0, 10, abundance(55)|weight(4.0)|leg_armor(1)|body_armor(4), imodbits_none, [], [fac_kingdom_1]],

	["kuauik_volantis_style_4", "Noblemans Robe", [("kuauik_volantis_style_4", imodbits_none)], itp_type_body_armor|itp_covers_legs|itp_doesnt_cover_hair|itp_can_penetrate_shield|itp_civilian|itp_next_item_as_melee, 0, 10, abundance(55)|weight(4.0)|leg_armor(1)|body_armor(4), imodbits_none, [], [fac_kingdom_1]],

	["kuauik_volantis_style_5", "Noblemans Robe", [("kuauik_volantis_style_5", imodbits_none)], itp_type_body_armor|itp_covers_legs|itp_doesnt_cover_hair|itp_can_penetrate_shield|itp_civilian|itp_next_item_as_melee, 0, 10, abundance(55)|weight(4.0)|leg_armor(1)|body_armor(4), imodbits_none, [], [fac_kingdom_1]],

	["andal_nobleman_coat_1", "Andal Noblemans Robe", [("andal_nobleman_coat_1", imodbits_none)], itp_type_body_armor|itp_covers_legs|itp_doesnt_cover_hair|itp_can_penetrate_shield|itp_civilian|itp_next_item_as_melee, 0, 10, abundance(55)|weight(4.0)|leg_armor(1)|body_armor(4), imodbits_none, [], [fac_kingdom_1]],

	["nobleman_f_outfit_rugged_1", "Noblemans Rugged Robe", [("nobleman_f_outfit_rugged_1", imodbits_none)], itp_type_body_armor|itp_covers_legs|itp_doesnt_cover_hair|itp_can_penetrate_shield|itp_civilian|itp_next_item_as_melee, 0, 10, abundance(55)|weight(4.0)|leg_armor(1)|body_armor(4), imodbits_none, [], [fac_kingdom_1]],

	["nobleman_f_outfit_rugged_2", "Noblemans Rugged Robe", [("nobleman_f_outfit_rugged_2", imodbits_none)], itp_type_body_armor|itp_covers_legs|itp_doesnt_cover_hair|itp_can_penetrate_shield|itp_civilian|itp_next_item_as_melee, 0, 10, abundance(55)|weight(4.0)|leg_armor(1)|body_armor(4), imodbits_none, [], [fac_kingdom_1]],

	["nobleman_f_outfit_rugged_3", "Noblemans Rugged Robe", [("nobleman_f_outfit_rugged_3", imodbits_none)], itp_type_body_armor|itp_covers_legs|itp_doesnt_cover_hair|itp_can_penetrate_shield|itp_civilian|itp_next_item_as_melee, 0, 10, abundance(55)|weight(4.0)|leg_armor(1)|body_armor(4), imodbits_none, [], [fac_kingdom_1]],

	["nobleman_f_outfit_robeish_1", "Noblemans Robe", [("nobleman_f_outfit_robeish_1", imodbits_none)], itp_type_body_armor|itp_covers_legs|itp_doesnt_cover_hair|itp_can_penetrate_shield|itp_civilian|itp_next_item_as_melee, 0, 10, abundance(55)|weight(4.0)|leg_armor(1)|body_armor(4), imodbits_none, [], [fac_kingdom_1]],

	["nobleman_f_outfit_robeish_2", "Noblemans Robe", [("nobleman_f_outfit_robeish_2", imodbits_none)], itp_type_body_armor|itp_covers_legs|itp_doesnt_cover_hair|itp_can_penetrate_shield|itp_civilian|itp_next_item_as_melee, 0, 10, abundance(55)|weight(4.0)|leg_armor(1)|body_armor(4), imodbits_none, [], [fac_kingdom_1]],

	["nobleman_f_outfit_vale_1", "Noblemans Doublet", [("nobleman_f_outfit_vale_1", imodbits_none)], itp_type_body_armor|itp_covers_legs|itp_doesnt_cover_hair|itp_can_penetrate_shield|itp_civilian|itp_next_item_as_melee, 0, 10, abundance(55)|weight(4.0)|leg_armor(1)|body_armor(4), imodbits_none, [], [fac_kingdom_1]],

	["nobleman_f_outfit_vale_2", "Noblemans Doublet", [("nobleman_f_outfit_vale_2", imodbits_none)], itp_type_body_armor|itp_covers_legs|itp_doesnt_cover_hair|itp_can_penetrate_shield|itp_civilian|itp_next_item_as_melee, 0, 10, abundance(55)|weight(4.0)|leg_armor(1)|body_armor(4), imodbits_none, [], [fac_kingdom_1]],

	["nobleman_f_outfit_reach_1", "Noblemans Doublet", [("nobleman_f_outfit_reach_1", imodbits_none)], itp_type_body_armor|itp_covers_legs|itp_doesnt_cover_hair|itp_can_penetrate_shield|itp_civilian|itp_next_item_as_melee, 0, 10, abundance(55)|weight(4.0)|leg_armor(1)|body_armor(4), imodbits_none, [], [fac_kingdom_1]],

	["nobleman_f_outfit_reach_2", "Noblemans Doublet", [("nobleman_f_outfit_reach_2", imodbits_none)], itp_type_body_armor|itp_covers_legs|itp_doesnt_cover_hair|itp_can_penetrate_shield|itp_civilian|itp_next_item_as_melee, 0, 10, abundance(55)|weight(4.0)|leg_armor(1)|body_armor(4), imodbits_none, [], [fac_kingdom_1]],

	["nobleman_f_outfit_reach_3", "Noblemans Doublet", [("nobleman_f_outfit_reach_3", imodbits_none)], itp_type_body_armor|itp_covers_legs|itp_doesnt_cover_hair|itp_can_penetrate_shield|itp_civilian|itp_next_item_as_melee, 0, 10, abundance(55)|weight(4.0)|leg_armor(1)|body_armor(4), imodbits_none, [], [fac_kingdom_1]],

	["nobleman_f_sealord", "Noblemans Doublet", [("nobleman_f_sealord", imodbits_none)], itp_type_body_armor|itp_covers_legs|itp_doesnt_cover_hair|itp_can_penetrate_shield|itp_civilian|itp_next_item_as_melee, 0, 10, abundance(55)|weight(4.0)|leg_armor(1)|body_armor(4), imodbits_none, [], [fac_kingdom_1]],

	["nobleman_f_outfit_1", "Noblemans Doublet", [("nobleman_f_outfit_1", imodbits_none)], itp_type_body_armor|itp_covers_legs|itp_doesnt_cover_hair|itp_can_penetrate_shield|itp_civilian|itp_next_item_as_melee, 0, 10, abundance(55)|weight(4.0)|leg_armor(1)|body_armor(4), imodbits_none, [], [fac_kingdom_1]],

	["nobleman_f_outfit_2", "Noblemans Doublet", [("nobleman_f_outfit_2", imodbits_none)], itp_type_body_armor|itp_covers_legs|itp_doesnt_cover_hair|itp_can_penetrate_shield|itp_civilian|itp_next_item_as_melee, 0, 10, abundance(55)|weight(4.0)|leg_armor(1)|body_armor(4), imodbits_none, [], [fac_kingdom_1]],

	["nobleman_f_outfit_3", "Noblemans Doublet", [("nobleman_f_outfit_3", imodbits_none)], itp_type_body_armor|itp_covers_legs|itp_doesnt_cover_hair|itp_can_penetrate_shield|itp_civilian|itp_next_item_as_melee, 0, 10, abundance(55)|weight(4.0)|leg_armor(1)|body_armor(4), imodbits_none, [], [fac_kingdom_1]],

	["nobleman_f_outfit_4", "Noblemans Doublet", [("nobleman_f_outfit_4", imodbits_none)], itp_type_body_armor|itp_covers_legs|itp_doesnt_cover_hair|itp_can_penetrate_shield|itp_civilian|itp_next_item_as_melee, 0, 10, abundance(55)|weight(4.0)|leg_armor(1)|body_armor(4), imodbits_none, [], [fac_kingdom_1]],

	["nobleman_f_outfit_5", "Noblemans Doublet", [("nobleman_f_outfit_5", imodbits_none)], itp_type_body_armor|itp_covers_legs|itp_doesnt_cover_hair|itp_can_penetrate_shield|itp_civilian|itp_next_item_as_melee, 0, 10, abundance(55)|weight(4.0)|leg_armor(1)|body_armor(4), imodbits_none, [], [fac_kingdom_1]],

	["nobleman_f_outfit_6", "Noblemans Doublet", [("nobleman_f_outfit_6", imodbits_none)], itp_type_body_armor|itp_covers_legs|itp_doesnt_cover_hair|itp_can_penetrate_shield|itp_civilian|itp_next_item_as_melee, 0, 10, abundance(55)|weight(4.0)|leg_armor(1)|body_armor(4), imodbits_none, [], [fac_kingdom_1]],

	["nobleman_f_outfit_7", "Noblemans Doublet", [("nobleman_f_outfit_7", imodbits_none)], itp_type_body_armor|itp_covers_legs|itp_doesnt_cover_hair|itp_can_penetrate_shield|itp_civilian|itp_next_item_as_melee, 0, 10, abundance(55)|weight(4.0)|leg_armor(1)|body_armor(4), imodbits_none, [], [fac_kingdom_1]],

	["nobleman_f_outfit_8", "Noblemans Doublet", [("nobleman_f_outfit_8", imodbits_none)], itp_type_body_armor|itp_covers_legs|itp_doesnt_cover_hair|itp_can_penetrate_shield|itp_civilian|itp_next_item_as_melee, 0, 10, abundance(55)|weight(4.0)|leg_armor(1)|body_armor(4), imodbits_none, [], [fac_kingdom_1]],

	["nobleman_f_outfit_9", "Noblemans Doublet", [("nobleman_f_outfit_9", imodbits_none)], itp_type_body_armor|itp_covers_legs|itp_doesnt_cover_hair|itp_can_penetrate_shield|itp_civilian|itp_next_item_as_melee, 0, 10, abundance(55)|weight(4.0)|leg_armor(1)|body_armor(4), imodbits_none, [], [fac_kingdom_1]],

	["nobleman_f_outfit_10", "Noblemans Doublet", [("nobleman_f_outfit_10", imodbits_none)], itp_type_body_armor|itp_covers_legs|itp_doesnt_cover_hair|itp_can_penetrate_shield|itp_civilian|itp_next_item_as_melee, 0, 10, abundance(55)|weight(4.0)|leg_armor(1)|body_armor(4), imodbits_none, [], [fac_kingdom_1]],

	["nobleman_f_outfit_11", "Noblemans Doublet", [("nobleman_f_outfit_11", imodbits_none)], itp_type_body_armor|itp_covers_legs|itp_doesnt_cover_hair|itp_can_penetrate_shield|itp_civilian|itp_next_item_as_melee, 0, 10, abundance(55)|weight(4.0)|leg_armor(1)|body_armor(4), imodbits_none, [], [fac_kingdom_1]],

	["nobleman_f_outfit_12", "Noblemans Doublet", [("nobleman_f_outfit_12", imodbits_none)], itp_type_body_armor|itp_covers_legs|itp_doesnt_cover_hair|itp_can_penetrate_shield|itp_civilian|itp_next_item_as_melee, 0, 10, abundance(55)|weight(4.0)|leg_armor(1)|body_armor(4), imodbits_none, [], [fac_kingdom_1]],

	["nobleman_f_outfit_13", "Noblemans Doublet", [("nobleman_f_outfit_13", imodbits_none)], itp_type_body_armor|itp_covers_legs|itp_doesnt_cover_hair|itp_can_penetrate_shield|itp_civilian|itp_next_item_as_melee, 0, 10, abundance(55)|weight(4.0)|leg_armor(1)|body_armor(4), imodbits_none, [], [fac_kingdom_1]],

	["nobleman_f_outfit_14", "Noblemans Doublet", [("nobleman_f_outfit_14", imodbits_none)], itp_type_body_armor|itp_covers_legs|itp_doesnt_cover_hair|itp_can_penetrate_shield|itp_civilian|itp_next_item_as_melee, 0, 10, abundance(55)|weight(4.0)|leg_armor(1)|body_armor(4), imodbits_none, [], [fac_kingdom_1]],

	["helmet_f_black_1", "Noblemans Hat", [("helmet_f_black_1", imodbits_none)], itp_type_head_armor|itp_civilian|itp_next_item_as_melee, 0, 3, abundance(40)|weight(1.0)|head_armor(2), imodbits_none, [], [fac_kingdom_2]],

	["helmet_f_black_2", "Noblemans Hat", [("helmet_f_black_2", imodbits_none)], itp_type_head_armor|itp_civilian|itp_next_item_as_melee, 0, 3, abundance(40)|weight(1.0)|head_armor(2), imodbits_none, [], [fac_kingdom_2]],

	["helmet_f_black_3", "Noblemans Hat", [("helmet_f_black_3", imodbits_none)], itp_type_head_armor|itp_civilian|itp_next_item_as_melee, 0, 3, abundance(40)|weight(1.0)|head_armor(2), imodbits_none, [], [fac_kingdom_2]],

	["helmet_f_black_4", "Noblemans Hat", [("helmet_f_black_4", imodbits_none)], itp_type_head_armor|itp_civilian|itp_next_item_as_melee, 0, 3, abundance(40)|weight(1.0)|head_armor(2), imodbits_none, [], [fac_kingdom_2]],

	["helmet_f_black_5", "Noblemans Hat", [("helmet_f_black_5", imodbits_none)], itp_type_head_armor|itp_civilian|itp_next_item_as_melee, 0, 3, abundance(40)|weight(1.0)|head_armor(2), imodbits_none, [], [fac_kingdom_2]],

	["helmet_f_black_6", "Noblemans Hat", [("helmet_f_black_6", imodbits_none)], itp_type_head_armor|itp_civilian|itp_next_item_as_melee, 0, 3, abundance(40)|weight(1.0)|head_armor(2), imodbits_none, [], [fac_kingdom_2]],

	["helmet_f_red_1", "Noblemans Hat", [("helmet_f_red_1", imodbits_none)], itp_type_head_armor|itp_civilian|itp_next_item_as_melee, 0, 3, abundance(40)|weight(1.0)|head_armor(2), imodbits_none, [], [fac_kingdom_2]],

	["helmet_f_leather_1", "Noblemans Hat", [("helmet_f_leather_1", imodbits_none)], itp_type_head_armor|itp_civilian|itp_next_item_as_melee, 0, 3, abundance(40)|weight(1.0)|head_armor(2), imodbits_none, [], [fac_kingdom_2]],

	["helmet_f_leather_2", "Noblemans Hat", [("helmet_f_leather_2", imodbits_none)], itp_type_head_armor|itp_civilian|itp_next_item_as_melee, 0, 3, abundance(40)|weight(1.0)|head_armor(2), imodbits_none, [], [fac_kingdom_2]],

	["helmet_f_leather_3", "Noblemans Hat", [("helmet_f_leather_3", imodbits_none)], itp_type_head_armor|itp_civilian|itp_next_item_as_melee, 0, 3, abundance(40)|weight(1.0)|head_armor(2), imodbits_none, [], [fac_kingdom_2]],

	["helmet_f_leather_4", "Noblemans Hat", [("helmet_f_leather_4", imodbits_none)], itp_type_head_armor|itp_civilian|itp_next_item_as_melee, 0, 3, abundance(40)|weight(1.0)|head_armor(2), imodbits_none, [], [fac_kingdom_2]],

	["helmet_f_leather_5", "Noblemans Hat", [("helmet_f_leather_5", imodbits_none)], itp_type_head_armor|itp_civilian|itp_next_item_as_melee, 0, 3, abundance(40)|weight(1.0)|head_armor(2), imodbits_none, [], [fac_kingdom_2]],

	["helmet_f_leather_6", "Noblemans Hat", [("helmet_f_leather_6", imodbits_none)], itp_type_head_armor|itp_civilian|itp_next_item_as_melee, 0, 3, abundance(40)|weight(1.0)|head_armor(2), imodbits_none, [], [fac_kingdom_2]],

	["nobleman_f_shoes_1", "Leather Shoes", [("nobleman_f_shoes_1", imodbits_none)], itp_type_foot_armor|itp_attach_armature|itp_attachment_mask|itp_civilian|itp_next_item_as_melee, 0, 200, abundance(80)|weight(1.0)|leg_armor(14), imodbits_cloth],

	["nobleman_f_shoes_2", "Leather Shoes", [("nobleman_f_shoes_2", imodbits_none)], itp_type_foot_armor|itp_attach_armature|itp_attachment_mask|itp_civilian|itp_next_item_as_melee, 0, 200, abundance(80)|weight(1.0)|leg_armor(14), imodbits_cloth],

	["nobleman_f_shoes_3", "Leather Shoes", [("nobleman_f_shoes_3", imodbits_none)], itp_type_foot_armor|itp_attach_armature|itp_attachment_mask|itp_civilian|itp_next_item_as_melee, 0, 200, abundance(80)|weight(1.0)|leg_armor(14), imodbits_cloth],

	["nobleman_f_shoes_4", "Leather Shoes", [("nobleman_f_shoes_4", imodbits_none)], itp_type_foot_armor|itp_attach_armature|itp_attachment_mask|itp_civilian|itp_next_item_as_melee, 0, 200, abundance(80)|weight(1.0)|leg_armor(14), imodbits_cloth],

	["nobleman_f_shoes_5", "Leather Shoes", [("nobleman_f_shoes_5", imodbits_none)], itp_type_foot_armor|itp_attach_armature|itp_attachment_mask|itp_civilian|itp_next_item_as_melee, 0, 200, abundance(80)|weight(1.0)|leg_armor(14), imodbits_cloth],

	["nobleman_f_shoes_6", "Leather Shoes", [("nobleman_f_shoes_6", imodbits_none)], itp_type_foot_armor|itp_attach_armature|itp_attachment_mask|itp_civilian|itp_next_item_as_melee, 0, 200, abundance(80)|weight(1.0)|leg_armor(14), imodbits_cloth],

	["lysa_style_2", "Northerner Court Dress", [("lysa_style_2", imodbits_none)], itp_type_body_armor|itp_covers_legs|itp_doesnt_cover_hair|itp_can_penetrate_shield|itp_civilian|itp_next_item_as_melee, 0, 50, abundance(55)|weight(2.0)|leg_armor(1)|body_armor(5), imodbits_cloth],

	["lysa_style_3", "Northerner Court Dress", [("lysa_style_3", imodbits_none)], itp_type_body_armor|itp_covers_legs|itp_doesnt_cover_hair|itp_can_penetrate_shield|itp_civilian|itp_next_item_as_melee, 0, 50, abundance(55)|weight(2.0)|leg_armor(1)|body_armor(5), imodbits_cloth],

	["lysa_style_4", "Northerner Court Dress", [("lysa_style_4", imodbits_none)], itp_type_body_armor|itp_covers_legs|itp_doesnt_cover_hair|itp_can_penetrate_shield|itp_civilian|itp_next_item_as_melee, 0, 50, abundance(55)|weight(2.0)|leg_armor(1)|body_armor(5), imodbits_cloth],

	["lysa_style_5", "Lysas Court Dress", [("lysa_style_5", imodbits_none)], itp_type_body_armor|itp_covers_legs|itp_doesnt_cover_hair|itp_can_penetrate_shield|itp_civilian|itp_next_item_as_melee, 0, 50, abundance(55)|weight(2.0)|leg_armor(1)|body_armor(5), imodbits_cloth],

	["barkeeper_1", "Peasants Dress", [("barkeeper_1", imodbits_none)], itp_type_body_armor|itp_covers_legs|itp_doesnt_cover_hair|itp_can_penetrate_shield|itp_civilian|itp_next_item_as_melee, 0, 50, abundance(55)|weight(2.0)|leg_armor(1)|body_armor(5), imodbits_cloth],

	["sansa_style_1", "Southrons Court Dress", [("sansa_style_1", imodbits_none)], itp_type_body_armor|itp_covers_legs|itp_doesnt_cover_hair|itp_can_penetrate_shield|itp_civilian|itp_next_item_as_melee, 0, 50, abundance(55)|weight(2.0)|leg_armor(1)|body_armor(5), imodbits_cloth],

	["sansa_style_2", "Southrons Court Dress", [("sansa_style_2", imodbits_none)], itp_type_body_armor|itp_covers_legs|itp_doesnt_cover_hair|itp_can_penetrate_shield|itp_civilian|itp_next_item_as_melee, 0, 50, abundance(55)|weight(2.0)|leg_armor(1)|body_armor(5), imodbits_cloth],

	["sansa_style_3", "Southrons Court Dress", [("sansa_style_3", imodbits_none)], itp_type_body_armor|itp_covers_legs|itp_doesnt_cover_hair|itp_can_penetrate_shield|itp_civilian|itp_next_item_as_melee, 0, 50, abundance(55)|weight(2.0)|leg_armor(1)|body_armor(5), imodbits_cloth],

	["sansa_style_4", "Southrons Court Dress", [("sansa_style_4", imodbits_none)], itp_type_body_armor|itp_covers_legs|itp_doesnt_cover_hair|itp_can_penetrate_shield|itp_civilian|itp_next_item_as_melee, 0, 50, abundance(55)|weight(2.0)|leg_armor(1)|body_armor(5), imodbits_cloth],

	["sansa_style_5", "Southrons Court Dress", [("sansa_style_5", imodbits_none)], itp_type_body_armor|itp_covers_legs|itp_doesnt_cover_hair|itp_can_penetrate_shield|itp_civilian|itp_next_item_as_melee, 0, 50, abundance(55)|weight(2.0)|leg_armor(1)|body_armor(5), imodbits_cloth],

	["sansa_style_6", "Southrons Court Dress", [("sansa_style_6", imodbits_none)], itp_type_body_armor|itp_covers_legs|itp_doesnt_cover_hair|itp_can_penetrate_shield|itp_civilian|itp_next_item_as_melee, 0, 50, abundance(55)|weight(2.0)|leg_armor(1)|body_armor(5), imodbits_cloth],

	["sansa_style_7", "Sansas Court Dress", [("sansa_style_7", imodbits_none)], itp_type_body_armor|itp_covers_legs|itp_doesnt_cover_hair|itp_can_penetrate_shield|itp_civilian|itp_next_item_as_melee, 0, 50, abundance(55)|weight(2.0)|leg_armor(1)|body_armor(5), imodbits_cloth],

	["dornish_1", "Dornish Court Dress", [("dornish_1", imodbits_none)], itp_type_body_armor|itp_covers_legs|itp_doesnt_cover_hair|itp_can_penetrate_shield|itp_civilian|itp_next_item_as_melee, 0, 50, abundance(55)|weight(2.0)|leg_armor(1)|body_armor(5), imodbits_cloth],

	["dornish_2", "Dornish Court Dress", [("dornish_2", imodbits_none)], itp_type_body_armor|itp_covers_legs|itp_doesnt_cover_hair|itp_can_penetrate_shield|itp_civilian|itp_next_item_as_melee, 0, 50, abundance(55)|weight(2.0)|leg_armor(1)|body_armor(5), imodbits_cloth],

	["dornish_3", "Dornish Court Dress", [("dornish_3", imodbits_none)], itp_type_body_armor|itp_covers_legs|itp_doesnt_cover_hair|itp_can_penetrate_shield|itp_civilian|itp_next_item_as_melee, 0, 50, abundance(55)|weight(2.0)|leg_armor(1)|body_armor(5), imodbits_cloth],

	["dornish_4", "Dornish Court Dress", [("dornish_4", imodbits_none)], itp_type_body_armor|itp_covers_legs|itp_doesnt_cover_hair|itp_can_penetrate_shield|itp_civilian|itp_next_item_as_melee, 0, 50, abundance(55)|weight(2.0)|leg_armor(1)|body_armor(5), imodbits_cloth],

	["dornish_5", "Dornish Court Dress", [("dornish_5", imodbits_none)], itp_type_body_armor|itp_covers_legs|itp_doesnt_cover_hair|itp_can_penetrate_shield|itp_civilian|itp_next_item_as_melee, 0, 50, abundance(55)|weight(2.0)|leg_armor(1)|body_armor(5), imodbits_cloth],

	["cersei_style_1", "Southron Court Dress", [("cersei_style_1", imodbits_none)], itp_type_body_armor|itp_covers_legs|itp_doesnt_cover_hair|itp_can_penetrate_shield|itp_civilian|itp_next_item_as_melee, 0, 50, abundance(55)|weight(2.0)|leg_armor(1)|body_armor(5), imodbits_cloth],

	["cersei_style_2", "Southron Court Dress", [("cersei_style_2", imodbits_none)], itp_type_body_armor|itp_covers_legs|itp_doesnt_cover_hair|itp_can_penetrate_shield|itp_civilian|itp_next_item_as_melee, 0, 50, abundance(55)|weight(2.0)|leg_armor(1)|body_armor(5), imodbits_cloth],

	["cersei_style_3", "Southron Court Dress", [("cersei_style_3", imodbits_none)], itp_type_body_armor|itp_covers_legs|itp_doesnt_cover_hair|itp_can_penetrate_shield|itp_civilian|itp_next_item_as_melee, 0, 50, abundance(55)|weight(2.0)|leg_armor(1)|body_armor(5), imodbits_cloth],

	["cersei_style_4", "Cerseis Court Dress", [("cersei_style_4", imodbits_none)], itp_type_body_armor|itp_covers_legs|itp_doesnt_cover_hair|itp_can_penetrate_shield|itp_civilian|itp_next_item_as_melee, 0, 50, abundance(55)|weight(2.0)|leg_armor(1)|body_armor(5), imodbits_cloth],

	["margaery_style_1", "Southron Court Dress", [("margaery_style_1", imodbits_none)], itp_type_body_armor|itp_covers_legs|itp_doesnt_cover_hair|itp_can_penetrate_shield|itp_civilian|itp_next_item_as_melee, 0, 50, abundance(55)|weight(2.0)|leg_armor(1)|body_armor(5), imodbits_cloth],

	["margaery_style_2", "Southron Court Dress", [("margaery_style_2", imodbits_none)], itp_type_body_armor|itp_covers_legs|itp_doesnt_cover_hair|itp_can_penetrate_shield|itp_civilian|itp_next_item_as_melee, 0, 50, abundance(55)|weight(2.0)|leg_armor(1)|body_armor(5), imodbits_cloth],

	["margaery_style_3", "Southron Court Dress", [("margaery_style_3", imodbits_none)], itp_type_body_armor|itp_covers_legs|itp_doesnt_cover_hair|itp_can_penetrate_shield|itp_civilian|itp_next_item_as_melee, 0, 50, abundance(55)|weight(2.0)|leg_armor(1)|body_armor(5), imodbits_cloth],

	["margaery_style_4", "Margaerys Court Dress", [("margaery_style_4", imodbits_none)], itp_type_body_armor|itp_covers_legs|itp_doesnt_cover_hair|itp_can_penetrate_shield|itp_civilian|itp_next_item_as_melee, 0, 50, abundance(55)|weight(2.0)|leg_armor(1)|body_armor(5), imodbits_cloth],

	["margaery_style_5", "Southron Court Dress", [("margaery_style_5", imodbits_none)], itp_type_body_armor|itp_covers_legs|itp_doesnt_cover_hair|itp_can_penetrate_shield|itp_civilian|itp_next_item_as_melee, 0, 50, abundance(55)|weight(2.0)|leg_armor(1)|body_armor(5), imodbits_cloth],

	["margaery_style_6", "Southron Court Dress", [("margaery_style_6", imodbits_none)], itp_type_body_armor|itp_covers_legs|itp_doesnt_cover_hair|itp_can_penetrate_shield|itp_civilian|itp_next_item_as_melee, 0, 50, abundance(55)|weight(2.0)|leg_armor(1)|body_armor(5), imodbits_cloth],

	["ga_swa_a2_leather", "BUGGED ITEM", [("witcher_worn_shield", imodbits_none)], itp_type_shield|itp_wooden_parry, itcf_carry_round_shield, 200, hit_points(180)|spd_rtng(87)|abundance(60)|weight(5.0)|shield_width(40)|body_armor(2), imodbits_none, [], [fac_kingdom_13, fac_kingdom_14, fac_kingdom_15]],

	["we_vae_bow_hunting", "BUGGED ITEM", [("witcher_worn_shield", imodbits_none)], itp_type_shield|itp_wooden_parry, itcf_carry_round_shield, 200, hit_points(180)|spd_rtng(87)|abundance(60)|weight(5.0)|shield_width(40)|body_armor(2), imodbits_none, [], [fac_kingdom_13, fac_kingdom_14, fac_kingdom_15]],

	["we_khe_bow_red", "BUGGED ITEM", [("witcher_worn_shield", imodbits_none)], itp_type_shield|itp_wooden_parry, itcf_carry_round_shield, 200, hit_points(180)|spd_rtng(87)|abundance(60)|weight(5.0)|shield_width(40)|body_armor(2), imodbits_none, [], [fac_kingdom_13, fac_kingdom_14, fac_kingdom_15]],

	["arena_shield_red", "BUGGED ITEM", [("witcher_worn_shield", imodbits_none)], itp_type_shield|itp_wooden_parry, itcf_carry_round_shield, 200, hit_points(180)|spd_rtng(87)|abundance(60)|weight(5.0)|shield_width(40)|body_armor(2), imodbits_none, [], [fac_kingdom_13, fac_kingdom_14, fac_kingdom_15]],

	["arena_lance", "BUGGED ITEM", [("witcher_worn_shield", imodbits_none)], itp_type_shield|itp_wooden_parry, itcf_carry_round_shield, 200, hit_points(180)|spd_rtng(87)|abundance(60)|weight(5.0)|shield_width(40)|body_armor(2), imodbits_none, [], [fac_kingdom_13, fac_kingdom_14, fac_kingdom_15]],

	["ar_swa_ban_scale_a", "BUGGED ITEM", [("witcher_worn_shield", imodbits_none)], itp_type_shield|itp_wooden_parry, itcf_carry_round_shield, 200, hit_points(180)|spd_rtng(87)|abundance(60)|weight(5.0)|shield_width(40)|body_armor(2), imodbits_none, [], [fac_kingdom_13, fac_kingdom_14, fac_kingdom_15]],

	["grenade_fragments", "Wildfire Pot Fragments", [("xeno_bullet", imodbits_none), ("xenoargh_grenade_fragment", ixmesh_flying_ammo), ("bolt_bag_c", ixmesh_carry), ("xeno_bolts_and_bullets", ixmesh_inventory)], itp_type_bolts|itp_covers_legs|itp_doesnt_cover_hair|itp_can_penetrate_shield|itp_bonus_against_shield|itp_no_pick_up_from_ground, itcf_carry_quiver_right_vertical, 2000, thrust_damage(1, pierce)|max_ammo(30)|abundance(90)|weight(2.25)|weapon_length(150), imodbits_none, 
	[(ti_on_missile_hit,
		[
			(copy_position, 63, 1),
			(position_get_z, ":position_z_63", 63),
			(set_fixed_point_multiplier, 100),
			(try_begin),
				(gt, ":position_z_63", -50),
				(particle_system_burst, "psys_bullet_dust", 63, 1),
			(else_try),
				(gt, ":position_z_63", -300),
				(position_set_z, 63, -50),
				(particle_system_burst, "psys_water_hit_a", 63, 8),
				(particle_system_burst, "psys_water_hit_b", 63, 4),
			(try_end)
		])]
	],

	["player_grenade", "Pot of Wildfire", [("wildfire_potion", imodbits_none), ("wildfire_potion", ixmesh_flying_ammo), ("wildfire_potion", ixmesh_inventory)], itp_type_thrown|itp_primary|itp_remove_item_on_use|itp_no_pick_up_from_ground, itcf_throw_stone, 4500, thrust_damage(70, pierce)|max_ammo(3)|spd_rtng(70)|abundance(100)|weight(5.0)|accuracy(75)|weapon_length(100)|shoot_speed(30), imodbits_none, 
	[(ti_on_missile_hit,
		[
			(copy_position, 63, 1),
			(position_get_distance_to_ground_level, ":position_distance_to_ground_level_63", 63),
			(try_begin),
				(lt, ":position_distance_to_ground_level_63", 0),
				(position_set_z_to_ground_level, 63),
				(position_move_z, 63, 200),
			(try_end),
			(this_or_next|multiplayer_is_dedicated_server),
			(this_or_next|multiplayer_is_server),
			(neg|game_in_multiplayer_mode),
			(store_trigger_param_1, reg1),
			(try_for_range, ":unused", 1, 31),
				(copy_position, 2, 63),
				(store_random_in_range, ":random_in_range_1_361", 1, 361),
				(position_rotate_x, 2, ":random_in_range_1_361"),
				(store_random_in_range, ":random_in_range_1_361_2", 1, 361),
				(position_rotate_y, 2, ":random_in_range_1_361_2"),
				(store_random_in_range, ":random_in_range_1_361_3", 1, 361),
				(position_rotate_z, 2, ":random_in_range_1_361_3"),
				(add_missile, reg1, 2, 1500, "itm_crossbow_f_simple_1", 0, "itm_grenade_fragments", 0),
			(try_end),
			(particle_system_burst, "psys_explosion_dirt", 63, 200),
			(particle_system_burst, "psys_explosive_explosion_sparks_a", 63, 35),
			(particle_system_burst, "psys_explosive_explosion_sparks_b", 63, 35),
			(play_sound_at_position, "snd_wildfire_explosion", 63),
			(play_sound_at_position, "snd_wildfire_scream", 63)
		])]
	],

	["gold_cloak_grenade", "Pot of Wildfire", [("wildfire_potion", imodbits_none), ("wildfire_potion", ixmesh_flying_ammo), ("wildfire_potion", ixmesh_inventory)], itp_type_thrown|itp_primary|itp_no_pick_up_from_ground, itcf_throw_stone, 4500, thrust_damage(50, pierce)|max_ammo(2)|spd_rtng(70)|abundance(100)|weight(5.0)|accuracy(75)|weapon_length(100)|shoot_speed(70), imodbits_none, 
	[(ti_on_missile_hit,
		[
			(copy_position, 63, 1),
			(position_get_distance_to_ground_level, ":position_distance_to_ground_level_63", 63),
			(try_begin),
				(lt, ":position_distance_to_ground_level_63", 0),
				(position_set_z_to_ground_level, 63),
				(position_move_z, 63, 200),
			(try_end),
			(this_or_next|multiplayer_is_dedicated_server),
			(this_or_next|multiplayer_is_server),
			(neg|game_in_multiplayer_mode),
			(store_trigger_param_1, reg1),
			(try_for_range, ":unused", 1, 17),
				(copy_position, 2, 63),
				(store_random_in_range, ":random_in_range_1_361", 1, 361),
				(position_rotate_x, 2, ":random_in_range_1_361"),
				(store_random_in_range, ":random_in_range_1_361_2", 1, 361),
				(position_rotate_y, 2, ":random_in_range_1_361_2"),
				(store_random_in_range, ":random_in_range_1_361_3", 1, 361),
				(position_rotate_z, 2, ":random_in_range_1_361_3"),
				(add_missile, reg1, 2, 1500, "itm_crossbow_f_simple_1", 0, "itm_grenade_fragments", 0),
			(try_end),
			(particle_system_burst, "psys_explosion_dirt", 63, 200),
			(particle_system_burst, "psys_explosive_explosion_sparks_a", 63, 35),
			(particle_system_burst, "psys_explosive_explosion_sparks_b", 63, 35),
			(play_sound_at_position, "snd_wildfire_explosion", 63),
			(play_sound_at_position, "snd_wildfire_scream", 63)
		])]
	],

	["items_end", "Items End", [("practice_shield", imodbits_none)], 0, 0, 1, abundance(100), imodbits_none],

]