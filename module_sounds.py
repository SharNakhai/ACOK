from header_sounds import *

sounds = [
	("click", sf_2d|sf_vol_1, ["min_click.wav"]),

	("tutorial_1", sf_2d|sf_vol_7, ["min_tutorial_1.wav"]),

	("tutorial_2", sf_2d|sf_vol_7, ["min_tutorial_2.wav"]),

	("gong", sf_2d|sf_priority_9|sf_vol_9, ["min_gong.wav"]),

	("quest_taken", sf_2d|sf_priority_9|sf_vol_10, ["min_quest_taken.wav"]),

	("quest_completed", sf_2d|sf_priority_9|sf_vol_7, ["min_quest_completed.wav"]),

	("quest_succeeded", sf_2d|sf_priority_9|sf_vol_7, ["min_quest_succeeded.wav"]),

	("quest_concluded", sf_2d|sf_priority_9|sf_vol_7, ["min_quest_concluded.wav"]),

	("quest_failed", sf_2d|sf_priority_9|sf_vol_7, ["min_quest_failed.wav"]),

	("quest_cancelled", sf_2d|sf_priority_9|sf_vol_7, ["min_quest_cancelled_01.wav"]),

	("rain", sf_2d|sf_looping|sf_priority_10|sf_vol_4, ["min_rain.wav"]),

	("money_received", sf_2d|sf_priority_10|sf_vol_6, ["min_money_received.wav"]),

	("money_paid", sf_2d|sf_priority_10|sf_vol_10, ["min_money_paid.wav"]),

	("sword_clash_1", 0, ["min_sword_clank_metal_01.wav", "min_sword_clank_metal_02.wav", "min_sword_clank_metal_03.wav", "min_sword_clank_metal_04.wav", "min_sword_clank_metal_05.wav", "min_sword_clank_metal_06.wav", "min_sword_clank_metal_07.wav", "min_sword_clank_metal_08.wav"]),

	("sword_clash_2", 0, ["min_sword_clank_metal_05.wav"]),

	("sword_clash_3", 0, ["min_sword_clank_metal_07.wav"]),

	("sword_swing", sf_priority_2|sf_vol_8, ["min_sword_swing_01.wav"]),

	("footstep_grass", sf_priority_1|sf_vol_4, ["min_footstep_grass_light_01.wav", "min_footstep_grass_light_02.wav", "min_footstep_grass_light_03.wav", "min_footstep_grass_light_04.wav"]),

	("footstep_wood", sf_priority_1|sf_vol_6, ["min_footstep_wood_light_01.wav", "min_footstep_wood_light_02.wav", "min_footstep_wood_light_03.wav", "min_footstep_wood_light_04.wav"]),

	("footstep_water", sf_priority_3|sf_vol_7, ["min_footstep_water_01.wav", "min_footstep_water_02.wav", "min_footstep_water_03.wav", "min_footstep_water_04.wav"]),

	("footstep_horse", sf_priority_3|sf_vol_15, ["min_footstep_horse_03b.wav", "min_footstep_horse_03f.wav", "min_footstep_horse_04b.wav", "min_footstep_horse_04f.wav"]),

	("footstep_horse_1b", sf_priority_3|sf_vol_15, ["min_footstep_horse_03b.wav", "min_footstep_horse_03f.wav", "min_footstep_horse_04b.wav", "min_footstep_horse_04f.wav"]),

	("footstep_horse_1f", sf_priority_3|sf_vol_15, ["min_footstep_horse_01b.wav", "min_footstep_horse_01f.wav", "min_footstep_horse_02b.wav", "min_footstep_horse_02f.wav"]),

	("footstep_horse_2b", sf_priority_3|sf_vol_15, ["min_footstep_horse_01b.wav"]),

	("footstep_horse_2f", sf_priority_3|sf_vol_15, ["min_footstep_horse_01f.wav"]),

	("footstep_horse_3b", sf_priority_3|sf_vol_15, ["min_footstep_horse_02b.wav"]),

	("footstep_horse_3f", sf_priority_3|sf_vol_15, ["min_footstep_horse_02f.wav"]),

	("footstep_horse_4b", sf_priority_3|sf_vol_15, ["min_footstep_horse_03b.wav"]),

	("footstep_horse_4f", sf_priority_3|sf_vol_15, ["min_footstep_horse_03f.wav"]),

	("footstep_horse_5b", sf_priority_3|sf_vol_15, ["min_footstep_horse_04b.wav"]),

	("footstep_horse_5f", sf_priority_3|sf_vol_15, ["min_footstep_horse_04f.wav"]),

	("jump_begin", sf_priority_9|sf_vol_7, ["min_jump_light_b_01.wav"]),

	("jump_end", sf_priority_9|sf_vol_5, ["min_jump_light_e_01.wav"]),

	("jump_begin_water", sf_priority_9|sf_vol_9, ["min_jump_water_b_01.wav"]),

	("jump_end_water", sf_priority_9|sf_vol_8, ["min_jump_water_e_01.wav"]),

	("horse_jump_begin", sf_priority_9|sf_vol_10, ["min_horse_jump_b_01.wav"]),

	("horse_jump_end", sf_priority_9|sf_vol_10, ["min_horse_jump_e_01.wav"]),

	("horse_jump_begin_water", sf_priority_9|sf_vol_10, ["min_horse_jump_water_b_01.wav"]),

	("horse_jump_end_water", sf_priority_9|sf_vol_10, ["min_horse_jump_water_e_01.wav"]),

	("release_bow", sf_vol_8, ["min_bow_shoot_01.wav"]),

	("release_crossbow", sf_vol_7, ["min_crossbow_shoot_01.wav"]),

	("throw_javelin", sf_vol_5, ["min_throw_javelin_01.wav"]),

	("throw_axe", sf_vol_7, ["min_throw_axe_01.wav"]),

	("throw_knife", sf_vol_5, ["min_throw_knife_01.wav"]),

	("throw_stone", sf_vol_5, ["min_throw_stone_01.wav"]),

	("reload_crossbow", sf_vol_3, ["min_pull_crossbow_string_01.wav"]),

	("reload_crossbow_continue", sf_vol_6, ["min_crossbow_load_01.wav"]),

	("pull_bow", sf_vol_6, ["min_pull_bow_string_01.wav"]),

	("pull_arrow", sf_vol_5, ["min_draw_arrow_01.wav"]),

	("arrow_pass_by", 0, ["min_arrow_pass_01.wav", "min_arrow_pass_02.wav", "min_arrow_pass_03.wav", "min_arrow_pass_04.wav"]),

	("bolt_pass_by", 0, ["min_bolt_pass_01.wav"]),

	("javelin_pass_by", 0, ["min_javelin_pass_by_01.wav", "min_javelin_pass_by_02.wav"]),

	("stone_pass_by", sf_vol_9, ["min_stone_pass_01.wav"]),

	("axe_pass_by", 0, ["min_axe_pass_by_01.wav"]),

	("knife_pass_by", 0, ["min_knife_pass_01.wav"]),

	("bullet_pass_by", 0, ["min_bullet_pass_01.wav"]),

	("incoming_arrow_hit_ground", sf_priority_7|sf_vol_7, ["min_arrow_ground_01.wav", "min_arrow_ground_02.wav", "min_arrow_ground_03.wav"]),

	("incoming_bolt_hit_ground", sf_priority_7|sf_vol_7, ["min_bolt_ground_01.wav", "min_bolt_ground_02.wav", "min_bolt_ground_03.wav"]),

	("incoming_javelin_hit_ground", sf_priority_7|sf_vol_7, ["min_javelin_ground_01.wav"]),

	("incoming_stone_hit_ground", sf_priority_7|sf_vol_7, ["min_stone_ground_01.wav"]),

	("incoming_axe_hit_ground", sf_priority_7|sf_vol_7, ["min_axe_ground_01.wav"]),

	("incoming_knife_hit_ground", sf_priority_7|sf_vol_7, ["min_knife_ground_01.wav"]),

	("incoming_bullet_hit_ground", sf_priority_7|sf_vol_7, ["min_bullet_ground_01.wav"]),

	("outgoing_arrow_hit_ground", sf_priority_7|sf_vol_7, ["min_arrow_ground_09.wav", "min_arrow_ground_10.wav", "min_arrow_ground_11.wav"]),

	("outgoing_bolt_hit_ground", sf_priority_7|sf_vol_7, ["min_bolt_ground_09.wav", "min_bolt_ground_10.wav", "min_bolt_ground_11.wav"]),

	("outgoing_javelin_hit_ground", sf_priority_7|sf_vol_10, ["min_javelin_ground_09.wav"]),

	("outgoing_stone_hit_ground", sf_priority_7|sf_vol_7, ["min_stone_ground_03.wav"]),

	("outgoing_axe_hit_ground", sf_priority_7|sf_vol_7, ["min_axe_ground_03.wav"]),

	("outgoing_knife_hit_ground", sf_priority_7|sf_vol_7, ["min_knife_ground_03.wav"]),

	("outgoing_bullet_hit_ground", sf_priority_7|sf_vol_7, ["min_bullet_ground_06.wav"]),

	("draw_sword", sf_priority_4, ["min_draw_sword_01.wav"]),

	("put_back_sword", sf_priority_4, ["min_put_away_sword_01.wav"]),

	("draw_greatsword", sf_priority_4, ["min_draw_greatsword_01.wav"]),

	("put_back_greatsword", sf_priority_4, ["min_put_away_greatsword_01.wav"]),

	("draw_axe", sf_priority_4, ["min_draw_axe_01.wav"]),

	("put_back_axe", sf_priority_4, ["min_put_away_axe_01.wav"]),

	("draw_greataxe", sf_priority_4, ["min_draw_greataxe_01.wav"]),

	("put_back_greataxe", sf_priority_4, ["min_put_away_greataxe_01.wav"]),

	("draw_spear", sf_priority_4, ["min_draw_spear_01.wav"]),

	("put_back_spear", sf_priority_4, ["min_put_away_spear_01.wav"]),

	("draw_crossbow", sf_priority_4|sf_vol_6, ["min_draw_crossbow_01.wav"]),

	("put_back_crossbow", sf_priority_4, ["min_put_away_crossbow_01.wav"]),

	("draw_revolver", sf_priority_4, ["min_draw_from_holster.wav"]),

	("put_back_revolver", sf_priority_4, ["min_put_back_to_holster.wav"]),

	("draw_dagger", sf_priority_4, ["min_draw_dagger_01.wav"]),

	("put_back_dagger", sf_priority_4, ["min_put_away_dagger_01.wav"]),

	("draw_bow", sf_priority_4, ["min_draw_bow_01.wav"]),

	("put_back_bow", sf_priority_4, ["min_put_away_bow_01.wav"]),

	("draw_shield", sf_priority_4|sf_vol_7, ["min_draw_shield_01.wav"]),

	("put_back_shield", sf_priority_4|sf_vol_7, ["min_put_away_shield_01.wav"]),

	("draw_other", sf_priority_4, ["min_draw_weapon_01.wav"]),

	("put_back_other", sf_priority_4, ["min_put_away_weapon_01.wav"]),

	("body_fall_small", sf_priority_6|sf_vol_10, ["min_body_fall_small_01.wav", "min_body_fall_small_02.wav"]),

	("body_fall_big", sf_priority_6|sf_vol_10, ["min_body_fall_large_01.wav", "min_body_fall_large_02.wav"]),

	("horse_body_fall_begin", sf_priority_7|sf_vol_10, ["min_horse_fall_b_01.wav", "min_horse_fall_b_02.wav"]),

	("horse_body_fall_end", sf_priority_7|sf_vol_10, ["min_horse_fall_e_01.wav", "min_horse_fall_e_02.wav"]),

	("hit_wood_wood", sf_priority_7|sf_vol_10, ["min_hit_wood_wood_01.wav", "min_hit_wood_wood_02.wav", "min_hit_wood_wood_03.wav", "min_hit_wood_wood_04.wav", "min_hit_wood_wood_05.wav", "min_hit_wood_wood_06.wav", "min_hit_wood_wood_07.wav"]),

	("hit_metal_metal", sf_priority_7|sf_vol_10, ["min_hit_metal_metal_01.wav", "min_hit_metal_metal_02.wav", "min_hit_metal_metal_03.wav", "min_hit_metal_metal_04.wav", "min_hit_metal_metal_05.wav", "min_hit_metal_metal_06.wav", "min_hit_metal_metal_07.wav", "min_hit_metal_metal_08.wav", "min_hit_metal_metal_09.wav", "min_hit_metal_metal_10.wav"]),

	("hit_wood_metal", sf_priority_7|sf_vol_10, ["min_hit_wood_metal_01.wav", "min_hit_wood_metal_02.wav", "min_hit_wood_metal_03.wav"]),

	("shield_hit_wood_wood", sf_priority_7|sf_vol_10, ["min_shield_hit_wood_wood_01.wav", "min_shield_hit_wood_wood_02.wav", "min_shield_hit_wood_wood_03.wav"]),

	("shield_hit_metal_metal", sf_priority_7|sf_vol_10, ["min_shield_hit_metal_metal_01.wav", "min_shield_hit_metal_metal_02.wav", "min_shield_hit_metal_metal_03.wav", "min_shield_hit_metal_metal_04.wav"]),

	("shield_hit_wood_metal", sf_priority_7|sf_vol_10, ["min_shield_hit_wood_metal_01.wav", "min_shield_hit_wood_metal_02.wav", "min_shield_hit_wood_metal_03.wav", "min_shield_hit_wood_metal_04.wav"]),

	("shield_hit_metal_wood", sf_priority_7|sf_vol_10, ["min_shield_hit_metal_wood_01.wav", "min_shield_hit_metal_wood_02.wav", "min_shield_hit_metal_wood_03.wav", "min_shield_hit_metal_wood_04.wav"]),

	("shield_broken", sf_priority_9, ["min_shield_break_01.wav"]),

	("man_hit", sf_priority_2|sf_vol_10, ["min_man_grunt_pain_01.wav", "min_man_grunt_pain_02.wav", "min_man_grunt_pain_03.wav", "min_man_grunt_pain_04.wav", "min_man_grunt_pain_05.wav", "min_man_grunt_pain_06.wav", "min_man_grunt_pain_07.wav", "min_man_grunt_pain_08.wav", "min_man_grunt_pain_09.wav", "min_man_grunt_pain_10.wav", "min_man_grunt_pain_11.wav", "min_man_grunt_pain_12.wav", "min_man_grunt_pain_13.wav", "min_man_grunt_pain_14.wav", "min_man_grunt_pain_15.wav", "min_man_grunt_pain_16.wav", "min_man_grunt_pain_17.wav", "min_man_grunt_pain_18.wav", "min_man_grunt_pain_19.wav", "min_man_grunt_pain_20.wav"]),

	("man_die", sf_priority_10|sf_vol_10, ["min_man_die_01.wav", "min_man_die_02.wav", "min_man_die_03.wav", "min_man_die_04.wav", "min_man_die_05.wav", "min_man_die_06.wav", "min_man_die_07.wav", "min_man_die_08.wav", "min_man_die_09.wav", "min_man_die_10.wav", "min_man_die_11.wav", "min_man_die_12.wav", "min_man_die_13.wav", "min_man_die_14.wav"]),

	("woman_hit", sf_priority_3, ["min_woman_hit_01.wav", "min_woman_hit_02.wav", "min_woman_hit_03.wav", "min_woman_hit_04.wav", "min_woman_hit_05.wav", "min_woman_hit_06.wav", "min_woman_hit_07.wav", "min_woman_hit_08.wav", "min_woman_hit_09.wav", "min_woman_hit_10.wav"]),

	("woman_die", sf_priority_10, ["min_woman_die_01.wav"]),

	("woman_yell", sf_priority_10|sf_vol_10, ["min_woman_yell_01.wav", "min_woman_yell_02.wav"]),

	("hide", 0, ["min_hide.wav"]),

	("unhide", 0, ["min_unhide.wav"]),

	("neigh", 0, ["min_horse_exterior_whinny_01.wav", "min_horse_exterior_whinny_02.wav", "min_horse_exterior_whinny_03.wav", "min_horse_exterior_whinny_04.wav", "min_horse_exterior_whinny_05.wav", "min_horse_exterior_whinny_06.wav"]),

	("gallop", sf_vol_3, ["min_gallop_01.wav", "min_gallop_02.wav", "min_gallop_03.wav"]),

	("battle", sf_vol_4, ["min_battle.wav"]),

	("arrow_hit_body", sf_priority_4, ["min_missile_flesh_01.wav", "min_missile_flesh_02.wav", "min_missile_flesh_03.wav"]),

	("metal_hit_low_armor_low_damage", sf_priority_5|sf_vol_9, ["min_metal_low_low_01.wav", "min_metal_low_low_02.wav", "min_metal_low_low_03.wav"]),

	("metal_hit_low_armor_high_damage", sf_priority_5|sf_vol_9, ["min_metal_low_high_01.wav", "min_metal_low_high_02.wav", "min_metal_low_high_03.wav"]),

	("metal_hit_high_armor_low_damage", sf_priority_5|sf_vol_9, ["min_metal_high_low_01.wav", "min_metal_high_low_02.wav", "min_metal_high_low_03.wav"]),

	("metal_hit_high_armor_high_damage", sf_priority_5|sf_vol_9, ["min_metal_high_high_01.wav", "min_metal_high_high_02.wav", "min_metal_high_high_03.wav"]),

	("wooden_hit_low_armor_low_damage", sf_priority_5|sf_vol_9, ["min_blunt_low_low_01.wav", "min_blunt_low_low_02.wav", "min_blunt_low_low_03.wav"]),

	("wooden_hit_low_armor_high_damage", sf_priority_5|sf_vol_9, ["min_blunt_low_high_01.wav", "min_blunt_low_high_02.wav", "min_blunt_low_high_03.wav"]),

	("wooden_hit_high_armor_low_damage", sf_priority_5|sf_vol_9, ["min_blunt_high_low_01.wav", "min_blunt_high_low_02.wav", "min_blunt_high_low_03.wav"]),

	("wooden_hit_high_armor_high_damage", sf_priority_5|sf_vol_9, ["min_blunt_high_high_01.wav", "min_blunt_high_high_02.wav", "min_blunt_high_high_03.wav"]),

	("mp_arrow_hit_target", sf_2d|sf_priority_10|sf_vol_9, ["min_mp_arrow_hit_target.wav"]),

	("blunt_hit", sf_priority_5|sf_vol_10, ["min_blunt_hit_01.wav", "min_blunt_hit_02.wav", "min_blunt_hit_03.wav"]),

	("player_hit_by_arrow", sf_priority_10|sf_vol_10, ["min_player_hit_by_arrow.wav"]),

	("pistol_shot", sf_priority_10|sf_vol_10, ["min_gun_shoot_01.wav"]),

	("man_grunt", sf_priority_3|sf_vol_4, ["min_man_heavy_grunt_01.wav", "min_man_heavy_grunt_02.wav", "min_man_heavy_grunt_03.wav"]),

	("man_breath_hard", sf_priority_3|sf_vol_8, ["min_man_ugh_01.wav", "min_man_ugh_02.wav", "min_man_ugh_03.wav", "min_man_ugh_04.wav", "min_man_ugh_05.wav", "min_man_ugh_06.wav", "min_man_ugh_07.wav"]),

	("man_stun", sf_priority_3|sf_vol_9, ["min_man_short_grunt_01.wav"]),

	("man_grunt_long", sf_priority_3|sf_vol_8, ["min_man_heavy_grunt_long_01.wav", "min_man_heavy_grunt_long_02.wav", "min_man_heavy_grunt_long_03.wav", "min_man_heavy_grunt_long_04.wav", "min_man_heavy_grunt_long_05.wav", "min_man_heavy_grunt_long_06.wav", "ext_man_heavy_grunt_long_07.wav", "ext_man_heavy_grunt_long_08.wav", "ext_man_heavy_grunt_long_09.wav", "ext_man_heavy_grunt_long_10.wav", "ext_man_heavy_grunt_long_11.wav", "ext_man_heavy_grunt_long_12.wav", "ext_man_heavy_grunt_long_13.wav", "ext_man_heavy_grunt_long_14.wav", "ext_man_heavy_grunt_long_15.wav"]),

	("man_yell", sf_priority_3|sf_vol_7, ["min_man_yell_01.wav", "min_man_yell_02.wav", "min_man_yell_03.wav", "min_man_yell_04.wav", "min_man_yell_05.wav", "min_man_yell_06.wav", "min_man_yell_07.wav", "min_man_yell_08.wav", "min_man_yell_09.wav", "min_man_yell_10.wav", "min_man_yell_11.wav", "min_man_yell_12.wav", "min_man_yell_13.wav", "min_man_yell_14.wav", "min_man_yell_15.wav", "min_man_yell_16.wav", "min_man_yell_17.wav", "min_man_yell_18.wav", "min_man_yell_19.wav"]),

	("man_warcry", sf_priority_6, ["min_man_insult_01.wav", "min_man_insult_02.wav", "min_man_insult_03.wav", "min_man_insult_04.wav", "min_man_insult_05.wav", "min_man_insult_06.wav", "min_man_insult_07.wav"]),

	("encounter_looters", sf_2d|sf_vol_8, ["min_encounter_river_pirates_01.wav", "min_encounter_river_pirates_02.wav", "min_encounter_river_pirates_03.wav", "min_encounter_river_pirates_04.wav", "min_encounter_river_pirates_05.wav"]),

	("encounter_bandits", sf_2d|sf_vol_8, ["min_encounter_bandit_01.wav", "min_encounter_bandit_02.wav", "min_encounter_bandit_03.wav", "min_encounter_bandit_04.wav", "min_encounter_bandit_05.wav", "min_encounter_bandit_06.wav", "min_encounter_bandit_07.wav"]),

	("encounter_farmers", sf_2d|sf_vol_8, ["min_encounter_farmer_01.wav", "min_encounter_farmer_02.wav", "min_encounter_farmer_03.wav", "min_encounter_farmer_04.wav"]),

	("encounter_sea_raiders", sf_2d|sf_vol_8, ["min_encounter_sea_raider_01.wav", "min_encounter_sea_raider_02.wav", "min_encounter_sea_raider_03.wav", "min_encounter_sea_raider_04.wav"]),

	("encounter_steppe_bandits", sf_2d|sf_vol_8, ["min_encounter_steppe_bandit_01.wav", "min_encounter_steppe_bandit_02.wav", "min_encounter_steppe_bandit_03.wav", "min_encounter_steppe_bandit_04.wav", "min_encounter_steppe_bandit_05.wav"]),

	("encounter_nobleman", sf_2d|sf_vol_8, ["min_encounter_nobleman_01.wav"]),

	("encounter_vaegirs_ally", sf_2d|sf_vol_8, ["min_encounter_vaegirs_ally_01.wav", "min_encounter_vaegirs_ally_02.wav"]),

	("encounter_vaegirs_neutral", sf_2d|sf_vol_8, ["min_encounter_vaegirs_neutral_01.wav", "min_encounter_vaegirs_neutral_04.wav", "min_encounter_vaegirs_neutral_06.wav", "min_encounter_vaegirs_neutral_08.wav"]),

	("encounter_vaegirs_enemy", sf_2d|sf_vol_8, ["min_encounter_vaegirs_neutral_02.wav", "min_encounter_vaegirs_neutral_03.wav", "min_encounter_vaegirs_neutral_05.wav", "min_encounter_vaegirs_neutral_07.wav"]),

	("sneak_town_halt", sf_2d, ["min_sneak_halt_01.wav", "min_sneak_halt_02.wav"]),

	("horse_walk", sf_priority_3|sf_vol_10, ["min_horse_walk_01.wav", "min_horse_walk_02.wav", "min_horse_walk_03.wav", "min_horse_walk_04.wav"]),

	("horse_trot", sf_priority_3|sf_vol_10, ["min_horse_trot_01.wav", "min_horse_trot_02.wav", "min_horse_trot_03.wav", "min_horse_trot_04.wav"]),

	("horse_canter", sf_priority_3|sf_vol_13, ["min_horse_canter_01.wav", "min_horse_canter_02.wav", "min_horse_canter_03.wav", "min_horse_canter_04.wav"]),

	("horse_gallop", sf_priority_3|sf_vol_13, ["min_horse_gallop_01.wav", "min_horse_gallop_02.wav", "min_horse_gallop_03.wav", "min_horse_gallop_04.wav"]),

	("horse_breath", sf_priority_11|sf_vol_10, ["min_horse_breath_01.wav", "min_horse_breath_02.wav", "min_horse_breath_03.wav", "min_horse_breath_04.wav"]),

	("horse_snort", sf_priority_5|sf_vol_10, ["min_horse_snort_01.wav", "min_horse_snort_02.wav", "min_horse_snort_03.wav", "min_horse_snort_04.wav", "min_horse_snort_05.wav"]),

	("horse_low_whinny", sf_vol_12, ["min_horse_whinny_01.wav", "min_horse_whinny_02.wav"]),

	("block_fist", 0, ["min_block_fist_01.wav", "min_block_fist_02.wav"]),

	("man_hit_blunt_weak", sf_priority_5|sf_vol_10, ["min_man_hit_01.wav", "min_man_hit_02.wav", "min_man_hit_03.wav", "min_man_hit_04.wav", "min_man_hit_05.wav"]),

	("man_hit_blunt_strong", sf_priority_5|sf_vol_10, ["min_man_hit_08.wav", "min_man_hit_09.wav", "min_man_hit_10.wav", "min_man_hit_11.wav", "min_man_hit_12.wav"]),

	("man_hit_pierce_weak", sf_priority_5|sf_vol_10, ["min_man_hit_15.wav", "min_man_hit_16.wav", "min_man_hit_17.wav", "min_man_hit_18.wav", "min_man_hit_19.wav"]),

	("man_hit_pierce_strong", sf_priority_5|sf_vol_10, ["min_man_hit_22.wav", "min_man_hit_23.wav", "min_man_hit_24.wav", "min_man_hit_25.wav", "min_man_hit_26.wav"]),

	("man_hit_cut_weak", sf_priority_5|sf_vol_10, ["min_man_hit_29.wav", "min_man_hit_30.wav", "min_man_hit_31.wav", "min_man_hit_32.wav", "min_man_hit_33.wav"]),

	("man_hit_cut_strong", sf_priority_5|sf_vol_10, ["min_man_hit_36.wav", "min_man_hit_37.wav", "min_man_hit_38.wav", "min_man_hit_39.wav", "min_man_hit_40.wav"]),

	("man_victory", sf_priority_5|sf_vol_9, ["min_man_victory_01.wav", "min_man_victory_02.wav", "min_man_victory_03.wav", "min_man_victory_04.wav", "min_man_victory_05.wav", "min_man_victory_06.wav", "min_man_victory_07.wav", "min_man_victory_08.wav", "min_man_victory_09.wav", "min_man_victory_10.wav"]),

	("fire_loop", sf_looping|sf_start_at_random_pos|sf_priority_9|sf_vol_4, ["min_Fire_Small_Crackle_Slick_op.wav"]),

	("torch_loop", sf_looping|sf_start_at_random_pos|sf_priority_9|sf_vol_4, ["min_Fire_Torch_Loop3.wav"]),

	("dummy_hit", sf_priority_9, ["min_dummy_hit_01.wav", "min_dummy_hit_02.wav"]),

	("dummy_destroyed", sf_priority_9, ["min_dummy_break_01.wav"]),

	("gourd_destroyed", sf_priority_9, ["min_dummy_break_01.wav"]),

	("cow_moo", sf_2d|sf_priority_9|sf_vol_8, ["min_cow_moo_1.wav"]),

	("cow_slaughter", sf_2d|sf_priority_9|sf_vol_8, ["min_cow_slaughter_01.wav"]),

	("distant_dog_bark", sf_2d|sf_priority_8|sf_vol_8, ["min_d_dog1.wav", "min_d_dog2.wav", "min_d_dog3.wav", "min_d_dog4.wav"]),

	("distant_owl", sf_2d|sf_priority_8|sf_vol_9, ["min_d_owl1.wav", "min_d_owl2.wav", "min_d_owl3.wav"]),

	("distant_chicken", sf_2d|sf_priority_8|sf_vol_8, ["min_d_chicken1.wav", "min_d_chicken2.wav"]),

	("distant_carpenter", sf_2d|sf_priority_8|sf_vol_3, ["min_d_carpenter1.wav", "min_d_saw_short3.wav"]),

	("distant_blacksmith", sf_2d|sf_priority_8|sf_vol_4, ["min_d_blacksmith2.wav"]),

	("scene_lord_of_light", sf_2d|sf_vol_9, ["scene_lord_of_light.wav"]),

	("scene_baratheon_theme", sf_2d|sf_vol_9, ["scene_baratheon_theme.mp3"]),

	("scene_daenerys", sf_2d|sf_vol_9, ["scene_daenerys.mp3"]),

	("scene_jon_and_ygritte", sf_2d|sf_vol_9, ["scene_jon_and_ygritte.mp3"]),

	("scene_main_theme", sf_2d|sf_vol_9, ["scene_main_theme.mp3"]),

	("scene_mhysa", sf_2d|sf_vol_9, ["scene_mhysa.mp3"]),

	("scene_pirates_at_sea", sf_2d|sf_vol_9, ["scene_pirates_at_sea.mp3"]),

	("scene_rains_of_castamere", sf_2d|sf_vol_9, ["scene_rains_of_castamere.mp3"]),

	("scene_sad_baratheon_theme", sf_2d|sf_vol_9, ["scene_sad_baratheon_theme.mp3"]),

	("scene_slavers_bay_1", sf_2d|sf_vol_9, ["scene_slavers_bay_1.mp3"]),

	("scene_slavers_bay_2", sf_2d|sf_vol_9, ["scene_slavers_bay_2.mp3"]),

	("scene_jane_seymour", sf_2d|sf_vol_9, ["scene_jane_seymour.mp3"]),

	("scene_theons_dark_deeds", sf_2d|sf_vol_9, ["scene_theons_dark_deeds.mp3"]),

	("scene_ashford", sf_2d|sf_vol_9, ["scene_ashford.mp3"]),

	("dedal_tavern_lute", sf_looping|sf_priority_6|sf_vol_5, ["dedal_tavern_lute_1.ogg", "dedal_tavern_lute_2.ogg", "dedal_tavern_lute_3.ogg"]),

	("dedal_tavern_lyre", sf_looping|sf_priority_6|sf_vol_6, ["dedal_tavern_lyre_1.ogg", "dedal_tavern_lyre_2.ogg", "dedal_tavern_lyre_3.ogg"]),

	("wildfire_explosion", sf_2d|sf_vol_9, ["wildfire_explosion.wav"]),

	("wildfire_scream", sf_2d|sf_vol_9, ["wildfire_scream.wav"]),

	("arena_ambiance", sf_2d|sf_looping|sf_priority_8|sf_vol_3, ["min_arena_loop1.wav"]),

	("town_ambiance", sf_2d|sf_looping|sf_priority_8|sf_vol_3, ["min_town_loop_3.wav"]),

	("tutorial_fail", sf_2d|sf_vol_7, ["min_cue_failure.wav"]),

	("your_flag_taken", sf_2d|sf_priority_10|sf_vol_10, ["min_your_flag_taken.wav"]),

	("enemy_flag_taken", sf_2d|sf_priority_10|sf_vol_10, ["min_enemy_flag_taken.wav"]),

	("flag_returned", sf_2d|sf_priority_10|sf_vol_10, ["min_your_flag_returned.wav"]),

	("team_scored_a_point", sf_2d|sf_priority_10|sf_vol_10, ["min_you_scored_a_point.wav"]),

	("enemy_scored_a_point", sf_2d|sf_priority_10|sf_vol_10, ["min_enemy_scored_a_point.wav"]),

	("whistle", sf_priority_9, ["min_whistle.wav"]),

]