from header_common import *
from header_parties import *
from ID_troops import *
from ID_factions import *
from ID_map_icons import *

pmf_is_prisoner = 0x0001

####################################################################################################################
#  Each party template record contains the following fields:
#  1) Party-template id: used for referencing party-templates in other files.
#     The prefix pt_ is automatically added before each party-template id.
#  2) Party-template name.
#  3) Party flags. See header_parties.py for a list of available flags
#  4) Menu. ID of the menu to use when this party is met. The value 0 uses the default party encounter system.
#  5) Faction
#  6) Personality. See header_parties.py for an explanation of personality flags.
#  7) List of stacks. Each stack record is a tuple that contains the following fields:
#    7.1) Troop-id. 
#    7.2) Minimum number of troops in the stack. 
#    7.3) Maximum number of troops in the stack. 
#    7.4) Member flags(optional). Use pmf_is_prisoner to note that this member is a prisoner.
#     Note: There can be at most 6 stacks.
####################################################################################################################


party_templates = [
	("none", "none", icon_people_gray_knight|pf_label_small, 0, fac_commoners, courage_7|merchant_personality, []),

	("rescued_prisoners", "Rescued Prisoners", icon_people_gray_knight|pf_label_small, 0, fac_commoners, courage_7|merchant_personality, []),

	("enemy", "Enemy", icon_people_gray_knight|pf_label_small, 0, fac_undeads, courage_7|merchant_personality, []),

	("hero_party", "Hero Party", icon_people_player|pf_label_small, 0, fac_commoners, courage_7|merchant_personality, []),

	("village_defenders", "Village Defenders", icon_people_peasant|pf_label_small, 0, fac_commoners, courage_7|merchant_personality, [(trp_mercenary_infantry_1, 10, 40), (trp_mercenary_infantry_2, 0, 8)]),

	("village_defenders_r", "Village Defenders", icon_people_peasant|pf_label_small, 0, fac_commoners, courage_7|merchant_personality, [(trp_mercenary_infantry_1, 10, 40)]),

	("village_defenders_e", "Village Defenders", icon_people_peasant|pf_label_small, 0, fac_commoners, courage_7|merchant_personality, [(trp_mercenary_infantry_1, 10, 40), (trp_mercenary_infantry_2, 0, 8)]),

	("cattle_herd", "Cattle Herd", icon_people_cattle|carries_goods(10)|pf_label_small, 0, fac_neutral, courage_7|merchant_personality, [(trp_cattle, 80, 120)]),

	("nemesis", "Hired Blades", icon_people_axeman|carries_goods(2)|pf_quest_party, 0, fac_neutral, courage_7|merchant_personality, [(trp_mercenary_infantry_1, 6, 18), (trp_mercenary_infantry_1, 9, 27), (trp_mercenary_infantry_1, 9, 18), (trp_mercenary_infantry_1, 9, 18), (trp_mercenary_infantry_1, 6, 18), (trp_mercenary_infantry_1, 3, 12)]),

	("nemesis2", "Hired Blades", icon_people_axeman|pf_quest_party, 0, fac_robber_knights, courage_11|escorted_merchant_personality, [(trp_mercenary_infantry_1, 100, 150), (trp_mercenary_infantry_1, 50, 75)]),

	("looters", "Looters", icon_people_axeman|carries_goods(8)|pf_label_small, 0, fac_outlaws, bandit_personality, [(trp_bandit_n_looter, 6, 45)]),

	("manhunters", "Manhunters", icon_people_gray_knight|pf_label_small, 0, fac_manhunters, soldier_personality, [(trp_bandit_n_manhunter, 18, 40)]),

	("forest_bandits", "Forest Bandits", icon_people_axeman|carries_goods(2)|pf_label_small, 0, fac_outlaws, bandit_personality, [(trp_bandit_n_forest, 8, 52)]),

	("taiga_bandits", "Wildlings", icon_people_axeman|carries_goods(2)|pf_label_small, 0, fac_outlaws, bandit_personality, [(trp_bandit_n_taiga, 10, 25)]),

	("steppe_bandits", "Dothraki Raiders", icon_people_khergit_horseman_b|carries_goods(2)|pf_label_small, 0, fac_outlaws, bandit_personality, [(trp_bandit_n_steppe, 10, 40)]),

	("sea_raiders", "Lyseni Pirates", icon_people_axeman|carries_goods(2)|pf_label_small, 0, fac_outlaws, bandit_personality, [(trp_bandit_n_sea_raider, 10, 50)]),

	("mountain_bandits", "Mountain Bandits", icon_people_axeman|carries_goods(2)|pf_label_small, 0, fac_outlaws, bandit_personality, [(trp_bandit_n_mountain, 5, 60)]),

	("desert_bandits", "Outlaws", icon_people_khergit|carries_goods(2)|pf_label_small, 0, fac_outlaws, bandit_personality, [(trp_bandit_n_desert, 5, 60)]),

	("looters_r", "Looters", icon_people_axeman|carries_goods(8)|pf_label_small, 0, fac_outlaws, bandit_personality, [(trp_bandit_r_looter, 6, 45)]),

	("manhunters_r", "Manhunters", icon_people_gray_knight|pf_label_small, 0, fac_manhunters, soldier_personality, [(trp_bandit_r_manhunter, 18, 40)]),

	("forest_bandits_r", "Forest Bandits", icon_people_axeman|carries_goods(2)|pf_label_small, 0, fac_outlaws, bandit_personality, [(trp_bandit_r_forest, 8, 52)]),

	("taiga_bandits_r", "Tundra Bandits", icon_people_axeman|carries_goods(2)|pf_label_small, 0, fac_outlaws, bandit_personality, [(trp_bandit_r_taiga, 8, 58)]),

	("steppe_bandits_r", "Steppe Bandits", icon_people_khergit|carries_goods(2)|pf_label_small, 0, fac_outlaws, bandit_personality, [(trp_bandit_r_steppe, 8, 58)]),

	("sea_raiders_r", "Sea Raiders", icon_people_axeman|carries_goods(2)|pf_label_small, 0, fac_outlaws, bandit_personality, [(trp_bandit_r_sea_raider, 10, 50)]),

	("mountain_bandits_r", "Mountain Bandits", icon_people_axeman|carries_goods(2)|pf_label_small, 0, fac_outlaws, bandit_personality, [(trp_bandit_r_mountain, 8, 60)]),

	("desert_bandits_r", "Desert Bandits", icon_people_vaegir_knight|carries_goods(2)|pf_label_small, 0, fac_outlaws, bandit_personality, [(trp_bandit_r_desert, 8, 58)]),

	("looters_e", "Looters", icon_people_axeman|carries_goods(2)|pf_label_small, 0, fac_outlaws, bandit_personality, [(trp_bandit_e_looter, 8, 18)]),

	("manhunters_e", "Honorable Men", icon_people_gray_knight|pf_label_small, 0, fac_manhunters, soldier_personality, [(trp_mercenary_horseman_1, 1, 1)]),

	("forest_bandits_e", "Forest Bandits", icon_new_icon_forest_bandit|carries_goods(2)|pf_label_small, 0, fac_outlaws, bandit_personality, [(trp_bandit_e_forest, 5, 12)]),

	("taiga_bandits_e", "Wildlings", icon_new_icon_wildlings|carries_goods(2)|pf_label_small, 0, fac_outlaws, bandit_personality, [(trp_bandit_e_taiga, 1, 1), (trp_bandit_e_taiga1, 3, 6), (trp_bandit_n_taiga, 3, 4), (trp_bandit_e_taiga2, 2, 10), (trp_wildling_spearwife, 2, 4)]),

	("steppe_bandits_e", "Dothraki Raiders", icon_new_icon_dothraki|carries_goods(2)|pf_label_small, 0, fac_outlaws, bandit_personality, [(trp_bandit_e_steppe, 1, 1), (trp_bandit_e_steppe1, 5, 12), (trp_bandit_e_steppe2, 5, 12)]),

	("sea_raiders_e", "Pirates", icon_new_icon_pirates|carries_goods(2)|pf_label_small, 0, fac_outlaws, bandit_personality, [(trp_bandit_e_sea_raider, 1, 1), (trp_bandit_e_sea_raider1, 7, 11), (trp_bandit_e_sea_raider2, 5, 12)]),

	("mountain_bandits_e", "Mountain Bandits", icon_new_icon_mountain_bandit|carries_goods(2)|pf_label_small, 0, fac_outlaws, bandit_personality, [(trp_bandit_e_mountain, 11, 18)]),

	("desert_bandits_e", "Dornish Sandstalkers", icon_people_vaegir_knight|carries_goods(2)|pf_label_small, 0, fac_outlaws, bandit_personality, [(trp_bandit_e_desert, 1, 1), (trp_bandit_e_desert1, 5, 8), (trp_bandit_e_desert2, 4, 8)]),

	("deserters", "Broken Men", icon_new_icon_deserters|carries_goods(2)|pf_label_small, 0, fac_deserters, bandit_personality, []),

	("slaver", "Slavers", icon_people_khergit|carries_goods(2)|pf_label_small, 0, fac_outlaws, bandit_personality, [(trp_bandit_n_slavers, 1, 1), (trp_bandit_n_slavers1, 7, 12), (trp_bandit_n_slavers2, 7, 14)]),

	("escaped_slaves", "Escaped Slaves", icon_people_peasant|carries_goods(2)|pf_label_small, 0, fac_deserters, bandit_personality, [(trp_bandit_n_escapedslave, 2, 4), (trp_bandit_n_escapedslave1, 8, 17)]),

	("clansmen", "Clansmen", icon_new_icon_wildlings|carries_goods(2)|pf_label_small, 0, fac_outlaws, bandit_personality, [(trp_bandit_n_valemen, 2, 4), (trp_bandit_n_valemen1, 4, 12), (trp_bandit_n_valemen2, 4, 12)]),

	("raiders", "Raiders", icon_people_axeman|carries_goods(2)|pf_label_small, 0, fac_outlaws, bandit_personality, [(trp_bandit_n_raiders, 1, 1), (trp_bandit_n_raiders1, 5, 15), (trp_bandit_n_raiders2, 5, 17)]),

	("outlaws", "Outlaws", icon_people_peasant|carries_goods(2)|pf_label_small, 0, fac_outlaws, bandit_personality, [(trp_bandit_n_outlaw, 1, 1), (trp_bandit_e_outlaw1, 5, 12), (trp_bandit_n_outlaw1, 5, 12), (trp_bandit_n_raiders2, 5, 8)]),

	("rhoyne_outlaws", "Rhoyne Outlaws", icon_new_icon_rhoyne_outlaw|carries_goods(2)|pf_label_small, 0, fac_outlaws, bandit_personality, [(trp_bandit_n_pirates, 3, 15), (trp_bandit_n_pirates1, 7, 14)]),

	("crannogmen", "Crannogmen", icon_new_icon_crannogmen|carries_goods(2)|pf_label_small, 0, fac_kingdom_2, bandit_personality, [(trp_crannogmen, 15, 25)]),

	("elite_raiders", "Robber Knights", icon_people_vaegir_knight|carries_goods(4)|pf_label_small, 0, fac_outlaws, bandit_personality, [(trp_bandit_n_raiders, 2, 3), (trp_bandit_n_raiders2, 5, 10), (trp_mercenary_infantry_1, 5, 10), (trp_mercenary_infantry_2, 5, 10)]),

	("elite_wildlings", "Wildling Warband", icon_people_khergit|carries_goods(4)|pf_label_small, 0, fac_outlaws, bandit_personality, [(trp_bandit_e_taiga, 3, 6), (trp_bandit_e_taiga1, 10, 15), (trp_bandit_e_taiga2, 15, 20), (trp_bandit_n_taiga, 12, 15)]),

	("elite_dothraki", "Dothraki Warband", icon_people_khergit|carries_goods(4)|pf_label_small, 0, fac_outlaws, bandit_personality, [(trp_bandit_e_steppe, 3, 4), (trp_bandit_e_steppe1, 14, 18), (trp_bandit_e_steppe2, 12, 20)]),

	("beowulf_warband", "The Brave Companions", icon_people_vaegir_knight|carries_goods(2)|pf_quest_party, 0, fac_beowulf_warband, bandit_personality, [(trp_beowulf_npc_5, 1, 1), (trp_urswyck, 1, 1), (trp_shagwell, 1, 1), (trp_brave_horseman, 14, 18), (trp_brave_swordsman, 20, 40), (trp_brave_archer, 15, 35)]),

	("wildfire_wights", "Wights", icon_people_khergit|pf_quest_party, 0, fac_fac_wights, bandit_personality, [(trp_wildfire_npc_5, 1, 1), (trp_zombie_wight, 18, 28), (trp_wildling_wight, 27, 44)]),

	("new_template", "The Bastard of Bolton", icon_people_vaegir_knight|carries_goods(2)|pf_quest_party, 0, fac_ramsay_snow, bandit_personality, [(trp_ramsay_snow, 1, 1), (trp_reek, 1, 1), (trp_sour_alyn, 1, 1), (trp_bolton_swordsman, 50, 65), (trp_bolton_archer, 36, 53), (trp_bolton_horseman, 42, 57)]),

	("arrians", "The Outlaw of the Crossing", icon_people_axeman|carries_goods(2)|pf_auto_remove_in_town|pf_quest_party, 0, fac_bloodborn, bandit_personality, [(trp_aegon_bloodborn, 1, 1), (trp_bandit_n_outlaw1, 8, 13), (trp_bandit_e_outlaw1, 12, 17), (trp_bandit_n_raiders2, 3, 9)]),

	("clansman_quest", "The Sons of the Mist", icon_people_vaegir_knight|carries_goods(2)|pf_auto_remove_in_town|pf_quest_party, 0, fac_ramsay_snow, bandit_personality, [(trp_clansman_npc_8, 1, 1), (trp_improved_clansman_1, 12, 13), (trp_improved_clansman_2, 14, 18), (trp_improved_clansman_3, 5, 9), (trp_improved_clansman_4, 3, 9)]),

	("cheese_rustlers", "Grain Thieves", icon_new_icon_thieves|carries_goods(2)|pf_quest_party, 0, fac_outlaws, bandit_personality, [(trp_mercenary_infantry_1, 3, 4), (trp_mercenary_infantry_2, 3, 5), (trp_mercenary_archer_1, 3, 7)]),

	("cheese_paladins", "Wine Thieves", icon_new_icon_thieves|carries_goods(2)|pf_quest_party, 0, fac_outlaws, courage_7|merchant_personality, [(trp_mercenary_infantry_1, 3, 5), (trp_mercenary_infantry_2, 3, 5), (trp_mercenary_archer_1, 2, 5), (trp_mercenary_horseman_1, 2, 4)]),

	("scholars", "Noblemen", icon_people_peasant|carries_goods(2)|pf_auto_remove_in_town|pf_quest_party, 0, fac_commoners, courage_11|escorted_merchant_personality, [(trp_scholars, 6, 10)]),

	("bandits_awaiting_ransom2", "Bandits Awaiting Ransom", icon_new_icon_bandits|carries_goods(2)|pf_auto_remove_in_town|pf_quest_party, 0, fac_neutral, bandit_personality, [(trp_bandit_e_bandit, 24, 58), (trp_kidnapped_wife, 1, 1, pmf_is_prisoner)]),

	("smugglers", "Smugglers", icon_new_icon_bandits|carries_goods(2)|pf_default_behavior|pf_quest_party, 0, fac_neutral, courage_7|merchant_personality, [(trp_bandit_e_bandit, 7, 9), (trp_bandit_e_mountain, 5, 10), (trp_bandit_e_forest, 3, 6)]),

	("kidnapped_wife", "Miller's Wife", icon_people_peasant|pf_quest_party, 0, fac_neutral, courage_7|merchant_personality, [(trp_kidnapped_wife, 1, 1)]),

	("merchant_caravan", "Merchant Caravan", icon_people_gray_knight|carries_goods(20)|pf_auto_remove_in_town|pf_quest_party, 0, fac_commoners, courage_11|escorted_merchant_personality, [(trp_caravan_master, 1, 1)]),

	("troublesome_bandits", "Troublesome Outlaws", icon_people_axeman|carries_goods(9)|pf_quest_party, 0, fac_outlaws, bandit_personality, [(trp_bandit_n_bandit, 28, 55)]),

	("bandits_awaiting_ransom", "Outlaws Awaiting Ransom", icon_people_axeman|carries_goods(9)|pf_auto_remove_in_town|pf_quest_party, 0, fac_neutral, bandit_personality, [(trp_bandit_n_bandit, 40, 58), (trp_kidnapped_girl, 1, 1, pmf_is_prisoner)]),

	("merchant_caravan_r", "Merchant Caravan", icon_people_gray_knight|carries_goods(20)|pf_auto_remove_in_town|pf_quest_party, 0, fac_commoners, courage_11|escorted_merchant_personality, [(trp_caravan_master, 1, 1)]),

	("troublesome_bandits_r", "Troublesome Bandits", icon_people_axeman|carries_goods(9)|pf_quest_party, 0, fac_outlaws, bandit_personality, [(trp_bandit_r_bandit, 28, 55)]),

	("bandits_awaiting_ransom_r", "Bandits Awaiting Ransom", icon_people_axeman|carries_goods(9)|pf_auto_remove_in_town|pf_quest_party, 0, fac_neutral, bandit_personality, [(trp_bandit_r_bandit, 40, 58), (trp_kidnapped_girl, 1, 1, pmf_is_prisoner)]),

	("merchant_caravan_e", "Merchant Caravan", icon_people_gray_knight|carries_goods(20)|pf_auto_remove_in_town|pf_quest_party, 0, fac_commoners, courage_11|escorted_merchant_personality, [(trp_caravan_master, 1, 1), (trp_mercenary_infantry_1, 5, 10), (trp_mercenary_infantry_2, 2, 20), (trp_mercenary_archer_1, 1, 10), (trp_mercenary_archer_2, 1, 10)]),

	("troublesome_bandits_e", "Troublesome Outlaws", icon_people_axeman|carries_goods(2)|pf_quest_party, 0, fac_outlaws, bandit_personality, [(trp_bandit_e_desert, 1, 1), (trp_bandit_e_bandit, 15, 25)]),

	("bandits_awaiting_ransom_e", "Outlaws Awaiting Ransom", icon_people_axeman|carries_goods(2)|pf_auto_remove_in_town|pf_quest_party, 0, fac_neutral, bandit_personality, [(trp_bandit_e_bandit, 21, 28), (trp_kidnapped_girl, 1, 1, pmf_is_prisoner)]),

	("kidnapped_girl", "Kidnapped Maiden", icon_people_woman|pf_quest_party, 0, fac_neutral, courage_7|merchant_personality, [(trp_kidnapped_girl, 1, 1)]),

	("village_farmers", "Village Farmers", icon_people_peasant|pf_civilian, 0, fac_innocents, courage_7|merchant_personality, [(trp_mercenary_infantry_1, 5, 20), (trp_mercenary_infantry_1, 3, 16)]),

	("spy_partners", "Unremarkable Travellers", icon_people_gray_knight|carries_goods(10)|pf_default_behavior|pf_quest_party, 0, fac_neutral, courage_7|merchant_personality, [(trp_spy_partner, 1, 1), (trp_mercenary_infantry_1, 2, 8), (trp_mercenary_infantry_1, 2, 8), (trp_mercenary_infantry_1, 1, 4), (trp_mercenary_infantry_1, 0, 2)]),

	("runaway_serfs", "Runaway Farmers", icon_people_peasant|carries_goods(8)|pf_default_behavior|pf_quest_party, 0, fac_neutral, courage_7|merchant_personality, [(trp_mercenary_infantry_1, 5, 20), (trp_mercenary_infantry_1, 3, 16)]),

	("village_farmers_r", "Village Farmers", icon_people_peasant|pf_civilian, 0, fac_innocents, courage_7|merchant_personality, [(trp_mercenary_infantry_1, 5, 20)]),

	("spy_partners_r", "Unremarkable Travellers", icon_people_gray_knight|carries_goods(10)|pf_default_behavior|pf_quest_party, 0, fac_neutral, courage_7|merchant_personality, [(trp_spy_partner, 1, 1), (trp_mercenary_infantry_1, 2, 8)]),

	("runaway_serfs_r", "Runaway Serfs", icon_people_peasant|carries_goods(8)|pf_default_behavior|pf_quest_party, 0, fac_neutral, courage_7|merchant_personality, [(trp_mercenary_infantry_1, 5, 20)]),

	("village_farmers_e", "Village Farmers", icon_people_peasant|pf_civilian, 0, fac_innocents, courage_7|merchant_personality, [(trp_event_peasant_female, 5, 28), (trp_event_peasant, 3, 6)]),

	("spy_partners_e", "Unremarkable Travellers", icon_people_gray_knight|carries_goods(2)|pf_default_behavior|pf_quest_party, 0, fac_neutral, courage_7|merchant_personality, [(trp_spy_partner, 1, 1), (trp_event_peasant_female, 2, 8), (trp_event_peasant, 2, 8), (trp_event_peasant, 1, 4), (trp_event_peasant, 0, 2)]),

	("runaway_serfs_e", "Runaway Farmers", icon_people_peasant|carries_goods(2)|pf_default_behavior|pf_quest_party, 0, fac_neutral, courage_7|merchant_personality, [(trp_event_peasant_female, 5, 20), (trp_event_peasant, 3, 16)]),

	("spy", "Ordinary Townsman", icon_people_gray_knight|carries_goods(2)|pf_default_behavior|pf_quest_party, 0, fac_neutral, courage_7|merchant_personality, [(trp_spy, 1, 1)]),

	("sacrificed_messenger", "Sacrificed Messenger", icon_people_gray_knight|carries_goods(2)|pf_default_behavior|pf_quest_party, 0, fac_neutral, courage_7|merchant_personality, []),

	("forager_party", "Foraging Party", icon_people_gray_knight|carries_goods(2)|pf_show_faction, 0, fac_commoners, courage_7|merchant_personality, []),

	("scout_party", "Scouts", icon_people_gray_knight|carries_goods(2)|pf_show_faction, 0, fac_commoners, bandit_personality, []),

	("patrol_party", "Patrol", icon_people_gray_knight|carries_goods(2)|pf_show_faction, 0, fac_commoners, soldier_personality, []),

	("messenger_party", "Messenger", icon_people_gray_knight|pf_show_faction, 0, fac_commoners, courage_7|merchant_personality, []),

	("raider_party", "Raiders", icon_people_gray_knight|carries_goods(16)|pf_quest_party, 0, fac_commoners, bandit_personality, []),

	("raider_captives", "Raider Captives", icon_people_player|pf_label_small, 0, fac_commoners, aggressiveness_0, [(trp_mercenary_infantry_1, 6, 60, pmf_is_prisoner)]),

	("kingdom_caravan_party", "Caravan", icon_people_mule|carries_goods(25)|pf_show_faction, 0, fac_commoners, courage_7|merchant_personality, [(trp_caravan_master, 1, 1)]),

	("raider_captives_r", "Raider Captives", icon_people_player|pf_label_small, 0, fac_commoners, aggressiveness_0, [(trp_mercenary_infantry_1, 6, 60, pmf_is_prisoner)]),

	("kingdom_caravan_party_r", "Caravan", icon_people_mule|carries_goods(25)|pf_show_faction, 0, fac_commoners, courage_7|merchant_personality, [(trp_caravan_master, 1, 1)]),

	("raider_captives_e", "Raider Captives", icon_people_player|pf_label_small, 0, fac_commoners, aggressiveness_0, [(trp_mercenary_infantry_1, 6, 60, pmf_is_prisoner)]),

	("kingdom_caravan_party_e", "Caravan", icon_people_mule|carries_goods(25)|pf_show_faction, 0, fac_commoners, courage_7|merchant_personality, [(trp_caravan_master, 1, 1), (trp_mercenary_infantry_1, 5, 10), (trp_mercenary_infantry_2, 2, 20), (trp_mercenary_archer_2, 1, 10), (trp_mercenary_archer_1, 1, 10)]),

	("prisoner_train_party", "Prisoner Train", icon_people_gray_knight|carries_goods(5)|pf_show_faction, 0, fac_commoners, courage_7|merchant_personality, []),

	("sea_traders", "Merchant Ship", icon_ship|carries_goods(50)|pf_is_ship|pf_show_faction, 0, fac_commoners, courage_7|merchant_personality, [(trp_caravan_master, 1, 1), (trp_mercenary_infantry_1, 20, 40)]),

	("sea_traders_r", "Merchant Ship", icon_ship|carries_goods(50)|pf_is_ship|pf_show_faction, 0, fac_commoners, courage_7|merchant_personality, [(trp_caravan_master, 1, 1), (trp_mercenary_infantry_1, 20, 40)]),

	("sea_traders_e", "Merchant Ship", icon_ship|carries_goods(50)|pf_is_ship|pf_show_faction, 0, fac_commoners, courage_7|merchant_personality, [(trp_caravan_master, 1, 1), (trp_mercenary_infantry_1, 20, 40), (trp_mercenary_infantry_1, 5, 30), (trp_mercenary_infantry_1, 5, 10), (trp_mercenary_infantry_1, 5, 10)]),

	("ship", "Ship", icon_ship|pf_disabled|pf_is_ship|pf_show_faction|pf_village, 0, fac_commoners, courage_7|merchant_personality, [(trp_sea_captain, 1, 1)]),

	("default_prisoners", "Default Prisoners", icon_people_player|pf_label_small, 0, fac_commoners, aggressiveness_0, [(trp_bandit_n_bandit, 5, 20, pmf_is_prisoner)]),

	("default_prisoners_r", "Default Prisoners", icon_people_player|pf_label_small, 0, fac_commoners, aggressiveness_0, [(trp_bandit_r_bandit, 5, 20, pmf_is_prisoner)]),

	("default_prisoners_e", "Default Prisoners", icon_people_player|pf_label_small, 0, fac_commoners, aggressiveness_0, [(trp_bandit_e_bandit, 5, 20, pmf_is_prisoner)]),

	("routed_warriors", "Routed Enemies", icon_people_vaegir_knight|pf_label_small, 0, fac_commoners, soldier_personality, []),

	("center_reinforcements", "Reinforcements", icon_people_axeman|carries_goods(16)|pf_label_small, 0, fac_commoners, soldier_personality, [(trp_mercenary_infantry_1, 5, 60), (trp_mercenary_infantry_1, 2, 14)]),

	("center_reinforcements_r", "Reinforcements", icon_people_axeman|carries_goods(16)|pf_label_small, 0, fac_commoners, soldier_personality, [(trp_mercenary_infantry_1, 5, 60)]),

	("center_reinforcements_e", "Reinforcements", icon_people_axeman|carries_goods(2)|pf_label_small, 0, fac_commoners, soldier_personality, [(trp_mercenary_infantry_1, 5, 60), (trp_mercenary_infantry_1, 2, 14), (trp_mercenary_infantry_1, 1, 14), (trp_mercenary_infantry_1, 1, 6), (trp_mercenary_infantry_1, 0, 3), (trp_mercenary_infantry_1, 0, 3)]),

	("kingdom_hero_party", "War Party", icon_people_flagbearer_a|pf_default_behavior|pf_show_faction, 0, fac_commoners, soldier_personality, []),

	("kingdom_1_reinforcements_a", "{!}kingdom 1 reinforcements a", icon_people_player|pf_label_small, 0, fac_commoners, aggressiveness_0, [(trp_sarranid_n_cemaat1, 2, 4), (trp_sarranid_n_ajam1, 2, 4), (trp_sarranid_n_cemaat1, 2, 4), (trp_sarranid_n_jebelus1, 2, 4), (trp_sarranid_n_yerliyya1, 2, 4), (trp_sarranid_n_cemaat, 2, 4)]),

	("kingdom_1_reinforcements_b", "{!}kingdom 1 reinforcements b", icon_people_player|pf_label_small, 0, fac_commoners, aggressiveness_0, [(trp_sarranid_n_millet1, 2, 4), (trp_sarranid_n_ajam1, 2, 4), (trp_sarranid_n_cemaat1, 2, 4), (trp_sarranid_n_jebelus1, 2, 4), (trp_sarranid_n_yerliyya1, 2, 4), (trp_sarranid_n_cemaat, 2, 4)]),

	("kingdom_1_reinforcements_c", "{!}kingdom 1 reinforcements c", icon_people_player|pf_label_small, 0, fac_commoners, aggressiveness_0, [(trp_sarranid_n_millet1, 2, 4), (trp_sarranid_n_ajam1, 2, 4), (trp_sarranid_n_cemaat1, 2, 4), (trp_sarranid_n_jebelus1, 2, 4), (trp_sarranid_n_yerliyya1, 2, 4), (trp_sarranid_n_cemaat, 2, 4)]),

	("kingdom_1_reinforcements_d", "{!}kingdom 1 reinforcements d", icon_people_player|pf_label_small, 0, fac_commoners, aggressiveness_0, [(trp_sarranid_n_millet1, 2, 4), (trp_stormlands_troop_1, 2, 4), (trp_sarranid_n_yeniceri1, 2, 4), (trp_sarranid_n_kapikula1, 2, 4), (trp_sarranid_n_uluteci1, 2, 4), (trp_sarranid_n_cemaat1, 2, 4)]),

	("kingdom_1_reinforcements_e", "{!}kingdom 1 reinforcements e", icon_people_player|pf_label_small, 0, fac_commoners, aggressiveness_0, [(trp_sarranid_n_millet1, 2, 4), (trp_sarranid_n_ajam1, 2, 4), (trp_sarranid_n_cemaat1, 2, 4), (trp_sarranid_n_jebelus1, 2, 4), (trp_sarranid_n_yerliyya1, 2, 4), (trp_sarranid_n_cemaat, 2, 4)]),

	("kingdom_1_reinforcements_f", "{!}kingdom 1 reinforcements f", icon_people_player|pf_label_small, 0, fac_commoners, aggressiveness_0, [(trp_sarranid_n_garip1, 2, 4), (trp_stormlands_troop_1, 2, 4), (trp_sarranid_n_yeniceri1, 2, 4), (trp_sarranid_n_kapikula1, 2, 4), (trp_sarranid_n_uluteci1, 2, 4), (trp_sarranid_n_cemaat1, 2, 4)]),

	("kingdom_2_reinforcements_a", "{!}kingdom 2 reinforcements a", icon_people_player|pf_label_small, 0, fac_commoners, aggressiveness_0, [(trp_sarranid_n_millet2, 2, 4), (trp_sarranid_n_ajam2, 2, 4), (trp_sarranid_n_cemaat2, 2, 4), (trp_sarranid_n_jebelus2, 2, 4), (trp_sarranid_n_yerliyya2, 2, 4), (trp_sarranid_n_cemaat1, 2, 4)]),

	("kingdom_2_reinforcements_b", "{!}kingdom 2 reinforcements b", icon_people_player|pf_label_small, 0, fac_commoners, aggressiveness_0, [(trp_sarranid_n_millet2, 2, 4), (trp_sarranid_n_ajam2, 2, 4), (trp_sarranid_n_cemaat2, 2, 4), (trp_sarranid_n_jebelus2, 2, 4), (trp_sarranid_n_yerliyya2, 2, 4), (trp_sarranid_n_cemaat1, 2, 4)]),

	("kingdom_2_reinforcements_c", "{!}kingdom 2 reinforcements c", icon_people_player|pf_label_small, 0, fac_commoners, aggressiveness_0, [(trp_sarranid_n_millet2, 2, 4), (trp_sarranid_n_ajam2, 2, 4), (trp_sarranid_n_cemaat2, 2, 4), (trp_sarranid_n_jebelus2, 2, 4), (trp_sarranid_n_yerliyya2, 2, 4), (trp_sarranid_n_cemaat1, 2, 4)]),

	("kingdom_2_reinforcements_d", "{!}kingdom 2 reinforcements d", icon_people_player|pf_label_small, 0, fac_commoners, aggressiveness_0, [(trp_sarranid_n_garip2, 2, 4), (trp_northern_troop_1, 2, 4), (trp_sarranid_n_yeniceri2, 2, 4), (trp_sarranid_n_kapikula2, 2, 4), (trp_sarranid_n_uluteci2, 2, 4), (trp_sarranid_n_cemaat2, 2, 4)]),

	("kingdom_2_reinforcements_e", "{!}kingdom 2 reinforcements e", icon_people_player|pf_label_small, 0, fac_commoners, aggressiveness_0, [(trp_sarranid_n_millet2, 2, 4), (trp_sarranid_n_ajam2, 2, 4), (trp_sarranid_n_cemaat2, 2, 4), (trp_sarranid_n_jebelus2, 2, 4), (trp_sarranid_n_yerliyya2, 2, 4), (trp_sarranid_n_cemaat2, 2, 4)]),

	("kingdom_2_reinforcements_f", "{!}kingdom 2 reinforcements f", icon_people_player|pf_label_small, 0, fac_commoners, aggressiveness_0, [(trp_sarranid_n_garip2, 2, 4), (trp_northern_troop_1, 2, 4), (trp_sarranid_n_yeniceri2, 2, 4), (trp_sarranid_n_kapikula2, 2, 4), (trp_sarranid_n_uluteci2, 2, 4), (trp_sarranid_n_cemaat2, 2, 4)]),

	("kingdom_3_reinforcements_a", "{!}kingdom 3 reinforcements a", icon_people_player|pf_label_small, 0, fac_commoners, aggressiveness_0, [(trp_sarranid_n_millet3, 2, 4), (trp_sarranid_n_ajam3, 2, 4), (trp_sarranid_n_cemaat3, 2, 4), (trp_sarranid_n_jebelus3, 2, 4), (trp_sarranid_n_yerliyya3, 2, 4), (trp_sarranid_n_cemaat3, 2, 4)]),

	("kingdom_3_reinforcements_b", "{!}kingdom 3 reinforcements b", icon_people_player|pf_label_small, 0, fac_commoners, aggressiveness_0, [(trp_sarranid_n_millet3, 2, 4), (trp_sarranid_n_ajam3, 2, 4), (trp_sarranid_n_cemaat3, 2, 4), (trp_sarranid_n_jebelus3, 2, 4), (trp_sarranid_n_yerliyya3, 2, 4), (trp_sarranid_n_cemaat3, 2, 4)]),

	("kingdom_3_reinforcements_c", "{!}kingdom 3 reinforcements c", icon_people_player|pf_label_small, 0, fac_commoners, aggressiveness_0, [(trp_sarranid_n_millet3, 2, 4), (trp_sarranid_n_ajam3, 2, 4), (trp_sarranid_n_cemaat3, 2, 4), (trp_sarranid_n_jebelus3, 2, 4), (trp_sarranid_n_yerliyya3, 2, 4), (trp_sarranid_n_cemaat3, 2, 4)]),

	("kingdom_3_reinforcements_d", "{!}kingdom 3 reinforcements d", icon_people_player|pf_label_small, 0, fac_commoners, aggressiveness_0, [(trp_sarranid_n_garip3, 2, 4), (trp_vale_troop_1, 2, 4), (trp_sarranid_n_yeniceri3, 2, 4), (trp_sarranid_n_kapikula3, 2, 4), (trp_sarranid_n_uluteci3, 2, 4), (trp_sarranid_n_cemaat3, 2, 4)]),

	("kingdom_3_reinforcements_e", "{!}kingdom 3 reinforcements e", icon_people_player|pf_label_small, 0, fac_commoners, aggressiveness_0, [(trp_sarranid_n_millet3, 2, 4), (trp_sarranid_n_ajam3, 2, 4), (trp_sarranid_n_cemaat3, 2, 4), (trp_sarranid_n_jebelus3, 2, 4), (trp_sarranid_n_yerliyya3, 2, 4), (trp_sarranid_n_cemaat3, 2, 4)]),

	("kingdom_3_reinforcements_f", "{!}kingdom 3 reinforcements f", icon_people_player|pf_label_small, 0, fac_commoners, aggressiveness_0, [(trp_sarranid_n_garip3, 2, 4), (trp_vale_troop_1, 2, 4), (trp_sarranid_n_yeniceri3, 2, 4), (trp_sarranid_n_kapikula3, 2, 4), (trp_sarranid_n_uluteci3, 2, 4), (trp_sarranid_n_cemaat3, 2, 4)]),

	("kingdom_4_reinforcements_a", "{!}kingdom 4 reinforcements a", icon_people_player|pf_label_small, 0, fac_commoners, aggressiveness_0, [(trp_lance_infantry_4, 2, 4), (trp_lance_infantry_3, 2, 4), (trp_lance_infantry_5, 2, 4), (trp_lance_archer_2, 2, 4), (trp_lance_infantry_2, 2, 4), (trp_lance_infantry_1, 2, 4)]),

	("kingdom_4_reinforcements_b", "{!}kingdom 4 reinforcements b", icon_people_player|pf_label_small, 0, fac_commoners, aggressiveness_0, [(trp_lance_infantry_4, 2, 4), (trp_lance_infantry_3, 2, 4), (trp_lance_infantry_5, 2, 4), (trp_lance_archer_2, 2, 4), (trp_lance_infantry_2, 2, 4), (trp_lance_infantry_1, 2, 4)]),

	("kingdom_4_reinforcements_c", "{!}kingdom 4 reinforcements c", icon_people_player|pf_label_small, 0, fac_commoners, aggressiveness_0, [(trp_lance_infantry_4, 2, 4), (trp_lance_infantry_3, 2, 4), (trp_lance_infantry_5, 2, 4), (trp_lance_archer_2, 2, 4), (trp_lance_infantry_2, 2, 4), (trp_lance_infantry_1, 2, 4)]),

	("kingdom_4_reinforcements_d", "{!}kingdom 4 reinforcements d", icon_people_player|pf_label_small, 0, fac_commoners, aggressiveness_0, [(trp_lance_infantry_4, 2, 4), (trp_lance_infantry_3, 2, 4), (trp_lance_infantry_5, 2, 4), (trp_lance_archer_2, 2, 4), (trp_lance_archer_5, 2, 4), (trp_lance_archer_2, 2, 4)]),

	("kingdom_4_reinforcements_e", "{!}kingdom 4 reinforcements e", icon_people_player|pf_label_small, 0, fac_commoners, aggressiveness_0, [(trp_lance_infantry_4, 2, 4), (trp_lance_infantry_3, 2, 4), (trp_lance_infantry_5, 2, 4), (trp_lance_archer_2, 2, 4), (trp_lance_archer_5, 2, 4), (trp_lance_archer_2, 2, 4)]),

	("kingdom_4_reinforcements_f", "{!}kingdom 4 reinforcements f", icon_people_player|pf_label_small, 0, fac_commoners, aggressiveness_0, [(trp_lance_infantry_4, 2, 4), (trp_lance_infantry_3, 2, 4), (trp_lance_infantry_5, 2, 4), (trp_lance_archer_2, 2, 4), (trp_lance_archer_5, 2, 4), (trp_lance_archer_2, 2, 4)]),

	("kingdom_5_reinforcements_a", "{!}kingdom 5 reinforcements a", icon_people_player|pf_label_small, 0, fac_commoners, aggressiveness_0, [(trp_lance_infantry_4, 2, 4), (trp_lance_infantry_3, 2, 4), (trp_lance_infantry_5, 2, 4), (trp_lance_archer_2, 2, 4), (trp_lance_infantry_2, 2, 4), (trp_lance_infantry_1, 2, 4)]),

	("kingdom_5_reinforcements_b", "{!}kingdom 5 reinforcements b", icon_people_player|pf_label_small, 0, fac_commoners, aggressiveness_0, [(trp_lance_infantry_4, 2, 4), (trp_lance_infantry_3, 2, 4), (trp_lance_infantry_5, 2, 4), (trp_lance_archer_2, 2, 4), (trp_lance_infantry_2, 2, 4), (trp_lance_infantry_1, 2, 4)]),

	("kingdom_5_reinforcements_c", "{!}kingdom 5 reinforcements c", icon_people_player|pf_label_small, 0, fac_commoners, aggressiveness_0, [(trp_lance_infantry_4, 2, 4), (trp_lance_infantry_3, 2, 4), (trp_lance_infantry_5, 2, 4), (trp_lance_archer_2, 2, 4), (trp_lance_infantry_2, 2, 4), (trp_lance_infantry_1, 2, 4)]),

	("kingdom_5_reinforcements_d", "{!}kingdom 5 reinforcements d", icon_people_player|pf_label_small, 0, fac_commoners, aggressiveness_0, [(trp_lance_infantry_4, 2, 4), (trp_lance_infantry_3, 2, 4), (trp_lance_infantry_5, 2, 4), (trp_lance_archer_2, 2, 4), (trp_lance_archer_5, 2, 4), (trp_lance_archer_2, 2, 4)]),

	("kingdom_5_reinforcements_e", "{!}kingdom 5 reinforcements e", icon_people_player|pf_label_small, 0, fac_commoners, aggressiveness_0, [(trp_lance_infantry_4, 2, 4), (trp_lance_infantry_3, 2, 4), (trp_lance_infantry_5, 2, 4), (trp_lance_archer_2, 2, 4), (trp_lance_archer_5, 2, 4), (trp_lance_archer_2, 2, 4)]),

	("kingdom_5_reinforcements_f", "{!}kingdom 5 reinforcements f", icon_people_player|pf_label_small, 0, fac_commoners, aggressiveness_0, [(trp_lance_infantry_4, 2, 4), (trp_lance_infantry_3, 2, 4), (trp_lance_infantry_5, 2, 4), (trp_lance_archer_2, 2, 4), (trp_lance_archer_5, 2, 4), (trp_lance_archer_2, 2, 4)]),

	("kingdom_6_reinforcements_a", "{!}kingdom 6 reinforcements a", icon_people_player|pf_label_small, 0, fac_commoners, aggressiveness_0, [(trp_sarranid_n_millet, 2, 4), (trp_sarranid_n_ajam, 2, 4), (trp_sarranid_n_cemaat, 2, 4), (trp_sarranid_n_jebelus, 2, 4), (trp_sarranid_n_yerliyya, 2, 4), (trp_sarranid_n_cemaat, 2, 4)]),

	("kingdom_6_reinforcements_b", "{!}kingdom 6 reinforcements b", icon_people_player|pf_label_small, 0, fac_commoners, aggressiveness_0, [(trp_sarranid_n_millet, 2, 4), (trp_sarranid_n_ajam, 2, 4), (trp_sarranid_n_cemaat, 2, 4), (trp_sarranid_n_jebelus, 2, 4), (trp_sarranid_n_yerliyya, 2, 4), (trp_sarranid_n_cemaat, 2, 4)]),

	("kingdom_6_reinforcements_c", "{!}kingdom 6 reinforcements c", icon_people_player|pf_label_small, 0, fac_commoners, aggressiveness_0, [(trp_sarranid_n_millet, 2, 4), (trp_sarranid_n_ajam, 2, 4), (trp_sarranid_n_cemaat, 2, 4), (trp_sarranid_n_jebelus, 2, 4), (trp_sarranid_n_yerliyya, 2, 4), (trp_sarranid_n_cemaat, 2, 4)]),

	("kingdom_6_reinforcements_d", "{!}kingdom 6 reinforcements d", icon_people_player|pf_label_small, 0, fac_commoners, aggressiveness_0, [(trp_sarranid_n_garip, 2, 4), (trp_dorne_troop_1, 2, 4), (trp_sarranid_n_yeniceri, 2, 4), (trp_sarranid_n_kapikula, 2, 4), (trp_sarranid_n_uluteci, 2, 4), (trp_sarranid_n_cemaat, 2, 4)]),

	("kingdom_6_reinforcements_e", "{!}kingdom 6 reinforcements e", icon_people_player|pf_label_small, 0, fac_commoners, aggressiveness_0, [(trp_sarranid_n_millet, 2, 4), (trp_sarranid_n_ajam, 2, 4), (trp_sarranid_n_cemaat, 2, 4), (trp_sarranid_n_jebelus, 2, 4), (trp_sarranid_n_yerliyya, 2, 4), (trp_sarranid_n_cemaat, 2, 4)]),

	("kingdom_6_reinforcements_f", "{!}kingdom 6 reinforcements f", icon_people_player|pf_label_small, 0, fac_commoners, aggressiveness_0, [(trp_sarranid_n_garip, 2, 4), (trp_dorne_troop_1, 2, 4), (trp_sarranid_n_yeniceri, 2, 4), (trp_sarranid_n_kapikula, 2, 4), (trp_sarranid_n_uluteci, 2, 4), (trp_sarranid_n_cemaat, 2, 4)]),

	("kingdom_7_reinforcements_a", "{!}kingdom 7 reinforcements a", icon_people_player|pf_label_small, 0, fac_commoners, aggressiveness_0, [(trp_sarranid_n_millet21, 2, 4), (trp_sarranid_n_ajam21, 2, 4), (trp_sarranid_n_cemaat21, 2, 4), (trp_sarranid_n_jebelus21, 2, 4), (trp_sarranid_n_yerliyya21, 2, 4), (trp_sarranid_n_cemaat21, 2, 4)]),

	("kingdom_7_reinforcements_b", "{!}kingdom 7 reinforcements b", icon_people_player|pf_label_small, 0, fac_commoners, aggressiveness_0, [(trp_sarranid_n_millet21, 2, 4), (trp_sarranid_n_ajam21, 2, 4), (trp_sarranid_n_cemaat21, 2, 4), (trp_sarranid_n_jebelus21, 2, 4), (trp_sarranid_n_yerliyya21, 2, 4), (trp_sarranid_n_cemaat21, 2, 4)]),

	("kingdom_7_reinforcements_c", "{!}kingdom 7 reinforcements c", icon_people_player|pf_label_small, 0, fac_commoners, aggressiveness_0, [(trp_sarranid_n_millet21, 2, 4), (trp_sarranid_n_ajam21, 2, 4), (trp_sarranid_n_cemaat21, 2, 4), (trp_sarranid_n_jebelus21, 2, 4), (trp_sarranid_n_yerliyya21, 2, 4), (trp_sarranid_n_cemaat21, 2, 4)]),

	("kingdom_7_reinforcements_d", "{!}kingdom 7 reinforcements d", icon_people_player|pf_label_small, 0, fac_commoners, aggressiveness_0, [(trp_sarranid_n_garip21, 2, 4), (trp_sarranid_n_yeniceri21, 2, 4), (trp_sarranid_n_kapikula21, 2, 4), (trp_sarranid_n_uluteci21, 2, 4), (trp_sarranid_n_cemaat21, 2, 4), (trp_sarranid_n_yerliyya21, 2, 4)]),

	("kingdom_7_reinforcements_e", "{!}kingdom 7 reinforcements e", icon_people_player|pf_label_small, 0, fac_commoners, aggressiveness_0, [(trp_sarranid_n_millet21, 2, 4), (trp_sarranid_n_ajam21, 2, 4), (trp_sarranid_n_cemaat21, 2, 4), (trp_sarranid_n_jebelus21, 2, 4), (trp_sarranid_n_yerliyya21, 2, 4), (trp_sarranid_n_cemaat21, 2, 4)]),

	("kingdom_7_reinforcements_f", "{!}kingdom 7 reinforcements f", icon_people_player|pf_label_small, 0, fac_commoners, aggressiveness_0, [(trp_sarranid_n_garip21, 2, 4), (trp_sarranid_n_yeniceri21, 2, 4), (trp_sarranid_n_kapikula21, 2, 4), (trp_sarranid_n_uluteci21, 2, 4), (trp_sarranid_n_cemaat21, 2, 4), (trp_sarranid_n_yerliyya21, 2, 4)]),

	("kingdom_8_reinforcements_a", "{!}kingdom 8 reinforcements a", icon_people_player|pf_label_small, 0, fac_commoners, aggressiveness_0, [(trp_sarranid_n_millet8, 2, 4), (trp_sarranid_n_ajam8, 2, 4), (trp_sarranid_n_cemaat8, 2, 4), (trp_sarranid_n_jebelus8, 2, 4), (trp_sarranid_n_yerliyya8, 2, 4), (trp_sarranid_n_cemaat8, 2, 4)]),

	("kingdom_8_reinforcements_b", "{!}kingdom 8 reinforcements b", icon_people_player|pf_label_small, 0, fac_commoners, aggressiveness_0, [(trp_sarranid_n_millet8, 2, 4), (trp_sarranid_n_ajam8, 2, 4), (trp_sarranid_n_cemaat8, 2, 4), (trp_sarranid_n_jebelus8, 2, 4), (trp_sarranid_n_yerliyya8, 2, 4), (trp_sarranid_n_cemaat8, 2, 4)]),

	("kingdom_8_reinforcements_c", "{!}kingdom 8 reinforcements c", icon_people_player|pf_label_small, 0, fac_commoners, aggressiveness_0, [(trp_sarranid_n_millet8, 2, 4), (trp_sarranid_n_ajam8, 2, 4), (trp_sarranid_n_cemaat8, 2, 4), (trp_sarranid_n_jebelus8, 2, 4), (trp_sarranid_n_yerliyya8, 2, 4), (trp_sarranid_n_cemaat8, 2, 4)]),

	("kingdom_8_reinforcements_d", "{!}kingdom 8 reinforcements d", icon_people_player|pf_label_small, 0, fac_commoners, aggressiveness_0, [(trp_sarranid_n_garip8, 2, 4), (trp_dragonstone_troop_1, 2, 4), (trp_sarranid_n_yeniceri8, 2, 4), (trp_sarranid_n_kapikula8, 2, 4), (trp_sarranid_n_uluteci8, 2, 4), (trp_sarranid_n_cemaat8, 2, 4)]),

	("kingdom_8_reinforcements_e", "{!}kingdom 8 reinforcements e", icon_people_player|pf_label_small, 0, fac_commoners, aggressiveness_0, [(trp_sarranid_n_millet8, 2, 4), (trp_sarranid_n_ajam8, 2, 4), (trp_sarranid_n_cemaat8, 2, 4), (trp_sarranid_n_jebelus8, 2, 4), (trp_sarranid_n_yerliyya8, 2, 4), (trp_sarranid_n_cemaat8, 2, 4)]),

	("kingdom_8_reinforcements_f", "{!}kingdom 8 reinforcements f", icon_people_player|pf_label_small, 0, fac_commoners, aggressiveness_0, [(trp_sarranid_n_garip8, 2, 4), (trp_dragonstone_troop_1, 2, 4), (trp_sarranid_n_yeniceri8, 2, 4), (trp_sarranid_n_kapikula8, 2, 4), (trp_sarranid_n_uluteci8, 2, 4), (trp_sarranid_n_cemaat8, 2, 4)]),

	("kingdom_9_reinforcements_a", "{!}kingdom 9 reinforcements a", icon_people_player|pf_label_small, 0, fac_commoners, aggressiveness_0, [(trp_sarranid_n_cemaat9, 2, 4), (trp_sarranid_n_ajam9, 2, 4), (trp_sarranid_n_cemaat9, 2, 4), (trp_sarranid_n_jebelus9, 2, 4), (trp_sarranid_n_yerliyya9, 2, 4), (trp_sarranid_n_cemaat9, 2, 4)]),

	("kingdom_9_reinforcements_b", "{!}kingdom 9 reinforcements b", icon_people_player|pf_label_small, 0, fac_commoners, aggressiveness_0, [(trp_sarranid_n_millet9, 2, 4), (trp_sarranid_n_ajam9, 2, 4), (trp_sarranid_n_cemaat9, 2, 4), (trp_sarranid_n_jebelus9, 2, 4), (trp_sarranid_n_yerliyya9, 2, 4), (trp_sarranid_n_cemaat9, 2, 4)]),

	("kingdom_9_reinforcements_c", "{!}kingdom 9 reinforcements c", icon_people_player|pf_label_small, 0, fac_commoners, aggressiveness_0, [(trp_sarranid_n_millet9, 2, 4), (trp_sarranid_n_ajam9, 2, 4), (trp_sarranid_n_cemaat9, 2, 4), (trp_sarranid_n_jebelus9, 2, 4), (trp_sarranid_n_yerliyya9, 2, 4), (trp_sarranid_n_cemaat9, 2, 4)]),

	("kingdom_9_reinforcements_d", "{!}kingdom 9 reinforcements d", icon_people_player|pf_label_small, 0, fac_commoners, aggressiveness_0, [(trp_sarranid_n_millet9, 2, 4), (trp_westerlands_troop_1, 2, 4), (trp_sarranid_n_yeniceri9, 2, 4), (trp_sarranid_n_kapikula9, 2, 4), (trp_sarranid_n_uluteci9, 2, 4), (trp_sarranid_n_cemaat9, 2, 4)]),

	("kingdom_9_reinforcements_e", "{!}kingdom 9 reinforcements e", icon_people_player|pf_label_small, 0, fac_commoners, aggressiveness_0, [(trp_sarranid_n_millet9, 2, 4), (trp_sarranid_n_ajam9, 2, 4), (trp_sarranid_n_cemaat9, 2, 4), (trp_sarranid_n_jebelus9, 2, 4), (trp_sarranid_n_yerliyya9, 2, 4), (trp_sarranid_n_cemaat9, 2, 4)]),

	("kingdom_9_reinforcements_f", "{!}kingdom 9 reinforcements f", icon_people_player|pf_label_small, 0, fac_commoners, aggressiveness_0, [(trp_sarranid_n_garip9, 2, 4), (trp_westerlands_troop_1, 2, 4), (trp_sarranid_n_yeniceri9, 2, 4), (trp_sarranid_n_kapikula9, 2, 4), (trp_sarranid_n_uluteci9, 2, 4), (trp_sarranid_n_cemaat9, 2, 4)]),

	("kingdom_10_reinforcements_a", "{!}kingdom 10 reinforcements a", icon_people_player|pf_label_small, 0, fac_commoners, aggressiveness_0, [(trp_sarranid_n_cemaat10, 2, 4), (trp_sarranid_n_ajam10, 2, 4), (trp_sarranid_n_cemaat10, 2, 4), (trp_sarranid_n_jebelus10, 2, 4), (trp_sarranid_n_yerliyya10, 2, 4), (trp_sarranid_n_cemaat10, 2, 4)]),

	("kingdom_10_reinforcements_b", "{!}kingdom 10 reinforcements b", icon_people_player|pf_label_small, 0, fac_commoners, aggressiveness_0, [(trp_sarranid_n_millet10, 2, 4), (trp_sarranid_n_ajam10, 2, 4), (trp_sarranid_n_cemaat10, 2, 4), (trp_sarranid_n_jebelus10, 2, 4), (trp_sarranid_n_yerliyya10, 2, 4), (trp_sarranid_n_cemaat10, 2, 4)]),

	("kingdom_10_reinforcements_c", "{!}kingdom 10 reinforcements c", icon_people_player|pf_label_small, 0, fac_commoners, aggressiveness_0, [(trp_sarranid_n_millet10, 2, 4), (trp_sarranid_n_ajam10, 2, 4), (trp_sarranid_n_cemaat10, 2, 4), (trp_sarranid_n_jebelus10, 2, 4), (trp_sarranid_n_yerliyya10, 2, 4), (trp_sarranid_n_cemaat10, 2, 4)]),

	("kingdom_10_reinforcements_d", "{!}kingdom 10 reinforcements d", icon_people_player|pf_label_small, 0, fac_commoners, aggressiveness_0, [(trp_sarranid_n_millet10, 2, 4), (trp_reach_troop_1, 2, 4), (trp_sarranid_n_yeniceri10, 2, 4), (trp_sarranid_n_kapikula10, 2, 4), (trp_sarranid_n_uluteci10, 2, 4), (trp_sarranid_n_millet10, 2, 4)]),

	("kingdom_10_reinforcements_e", "{!}kingdom 10 reinforcements e", icon_people_player|pf_label_small, 0, fac_commoners, aggressiveness_0, [(trp_sarranid_n_millet10, 2, 4), (trp_sarranid_n_ajam10, 2, 4), (trp_sarranid_n_cemaat10, 2, 4), (trp_sarranid_n_jebelus10, 2, 4), (trp_sarranid_n_yerliyya10, 2, 4), (trp_sarranid_n_cemaat10, 2, 4)]),

	("kingdom_10_reinforcements_f", "{!}kingdom 10 reinforcements f", icon_people_player|pf_label_small, 0, fac_commoners, aggressiveness_0, [(trp_sarranid_n_garip10, 2, 4), (trp_reach_troop_1, 2, 4), (trp_sarranid_n_yeniceri10, 2, 4), (trp_sarranid_n_kapikula10, 2, 4), (trp_sarranid_n_uluteci10, 2, 4), (trp_sarranid_n_millet10, 2, 4)]),

	("kingdom_11_reinforcements_a", "{!}kingdom 4 reinforcements a", icon_people_player|pf_label_small, 0, fac_commoners, aggressiveness_0, [(trp_lance_infantry_4, 2, 4), (trp_lance_infantry_3, 2, 4), (trp_lance_infantry_5, 2, 4), (trp_lance_archer_2, 2, 4), (trp_lance_infantry_2, 2, 4), (trp_lance_infantry_1, 2, 4)]),

	("kingdom_11_reinforcements_b", "{!}kingdom 4 reinforcements b", icon_people_player|pf_label_small, 0, fac_commoners, aggressiveness_0, [(trp_lance_infantry_4, 2, 4), (trp_lance_infantry_3, 2, 4), (trp_lance_infantry_5, 2, 4), (trp_lance_archer_2, 2, 4), (trp_lance_infantry_2, 2, 4), (trp_lance_infantry_1, 2, 4)]),

	("kingdom_11_reinforcements_c", "{!}kingdom 4 reinforcements c", icon_people_player|pf_label_small, 0, fac_commoners, aggressiveness_0, [(trp_lance_infantry_4, 2, 4), (trp_lance_infantry_3, 2, 4), (trp_lance_infantry_5, 2, 4), (trp_lance_archer_2, 2, 4), (trp_lance_infantry_2, 2, 4), (trp_lance_infantry_1, 2, 4)]),

	("kingdom_11_reinforcements_d", "{!}kingdom 4 reinforcements d", icon_people_player|pf_label_small, 0, fac_commoners, aggressiveness_0, [(trp_lance_infantry_4, 2, 4), (trp_lance_infantry_3, 2, 4), (trp_lance_infantry_5, 2, 4), (trp_lance_archer_2, 2, 4), (trp_lance_archer_5, 2, 4), (trp_lance_archer_2, 2, 4)]),

	("kingdom_11_reinforcements_e", "{!}kingdom 4 reinforcements e", icon_people_player|pf_label_small, 0, fac_commoners, aggressiveness_0, [(trp_lance_infantry_4, 2, 4), (trp_lance_infantry_3, 2, 4), (trp_lance_infantry_5, 2, 4), (trp_lance_archer_2, 2, 4), (trp_lance_archer_5, 2, 4), (trp_lance_archer_2, 2, 4)]),

	("kingdom_11_reinforcements_f", "{!}kingdom 4 reinforcements f", icon_people_player|pf_label_small, 0, fac_commoners, aggressiveness_0, [(trp_lance_infantry_4, 2, 4), (trp_lance_infantry_3, 2, 4), (trp_lance_infantry_5, 2, 4), (trp_lance_archer_2, 2, 4), (trp_lance_archer_5, 2, 4), (trp_lance_archer_2, 2, 4)]),

	("kingdom_12_reinforcements_a", "{!}kingdom 4 reinforcements a", icon_people_player|pf_label_small, 0, fac_commoners, aggressiveness_0, [(trp_lance_infantry_4, 2, 4), (trp_lance_infantry_3, 2, 4), (trp_lance_infantry_5, 2, 4), (trp_lance_archer_2, 2, 4), (trp_lance_infantry_2, 2, 4), (trp_lance_infantry_1, 2, 4)]),

	("kingdom_12_reinforcements_b", "{!}kingdom 4 reinforcements b", icon_people_player|pf_label_small, 0, fac_commoners, aggressiveness_0, [(trp_lance_infantry_4, 2, 4), (trp_lance_infantry_3, 2, 4), (trp_lance_infantry_5, 2, 4), (trp_lance_archer_2, 2, 4), (trp_lance_infantry_2, 2, 4), (trp_lance_infantry_1, 2, 4)]),

	("kingdom_12_reinforcements_c", "{!}kingdom 4 reinforcements c", icon_people_player|pf_label_small, 0, fac_commoners, aggressiveness_0, [(trp_lance_infantry_4, 2, 4), (trp_lance_infantry_3, 2, 4), (trp_lance_infantry_5, 2, 4), (trp_lance_archer_2, 2, 4), (trp_lance_infantry_2, 2, 4), (trp_lance_infantry_1, 2, 4)]),

	("kingdom_12_reinforcements_d", "{!}kingdom 4 reinforcements d", icon_people_player|pf_label_small, 0, fac_commoners, aggressiveness_0, [(trp_lance_infantry_4, 2, 4), (trp_lance_infantry_3, 2, 4), (trp_lance_infantry_5, 2, 4), (trp_lance_archer_2, 2, 4), (trp_lance_archer_5, 2, 4), (trp_lance_archer_2, 2, 4)]),

	("kingdom_12_reinforcements_e", "{!}kingdom 4 reinforcements e", icon_people_player|pf_label_small, 0, fac_commoners, aggressiveness_0, [(trp_lance_infantry_4, 2, 4), (trp_lance_infantry_3, 2, 4), (trp_lance_infantry_5, 2, 4), (trp_lance_archer_2, 2, 4), (trp_lance_archer_5, 2, 4), (trp_lance_archer_2, 2, 4)]),

	("kingdom_12_reinforcements_f", "{!}kingdom 4 reinforcements f", icon_people_player|pf_label_small, 0, fac_commoners, aggressiveness_0, [(trp_lance_infantry_4, 2, 4), (trp_lance_infantry_3, 2, 4), (trp_lance_infantry_5, 2, 4), (trp_lance_archer_2, 2, 4), (trp_lance_archer_5, 2, 4), (trp_lance_archer_2, 2, 4)]),

	("kingdom_13_reinforcements_a", "{!}kingdom 4 reinforcements a", icon_people_player|pf_label_small, 0, fac_commoners, aggressiveness_0, [(trp_lance_infantry_4, 2, 4), (trp_lance_infantry_3, 2, 4), (trp_lance_infantry_5, 2, 4), (trp_lance_archer_2, 2, 4), (trp_lance_infantry_2, 2, 4), (trp_lance_infantry_1, 2, 4)]),

	("kingdom_13_reinforcements_b", "{!}kingdom 4 reinforcements b", icon_people_player|pf_label_small, 0, fac_commoners, aggressiveness_0, [(trp_lance_infantry_4, 2, 4), (trp_lance_infantry_3, 2, 4), (trp_lance_infantry_5, 2, 4), (trp_lance_archer_2, 2, 4), (trp_lance_infantry_2, 2, 4), (trp_lance_infantry_1, 2, 4)]),

	("kingdom_13_reinforcements_c", "{!}kingdom 4 reinforcements c", icon_people_player|pf_label_small, 0, fac_commoners, aggressiveness_0, [(trp_lance_infantry_4, 2, 4), (trp_lance_infantry_3, 2, 4), (trp_lance_infantry_5, 2, 4), (trp_lance_archer_2, 2, 4), (trp_lance_infantry_2, 2, 4), (trp_lance_infantry_1, 2, 4)]),

	("kingdom_13_reinforcements_d", "{!}kingdom 4 reinforcements d", icon_people_player|pf_label_small, 0, fac_commoners, aggressiveness_0, [(trp_lance_infantry_4, 2, 4), (trp_lance_infantry_3, 2, 4), (trp_lance_infantry_5, 2, 4), (trp_lance_archer_2, 2, 4), (trp_lance_archer_5, 2, 4), (trp_lance_archer_2, 2, 4)]),

	("kingdom_13_reinforcements_e", "{!}kingdom 4 reinforcements e", icon_people_player|pf_label_small, 0, fac_commoners, aggressiveness_0, [(trp_lance_infantry_4, 2, 4), (trp_lance_infantry_3, 2, 4), (trp_lance_infantry_5, 2, 4), (trp_lance_archer_2, 2, 4), (trp_lance_archer_5, 2, 4), (trp_lance_archer_2, 2, 4)]),

	("kingdom_13_reinforcements_f", "{!}kingdom 4 reinforcements f", icon_people_player|pf_label_small, 0, fac_commoners, aggressiveness_0, [(trp_lance_infantry_4, 2, 4), (trp_lance_infantry_3, 2, 4), (trp_lance_infantry_5, 2, 4), (trp_lance_archer_2, 2, 4), (trp_lance_archer_5, 2, 4), (trp_lance_archer_2, 2, 4)]),

	("kingdom_14_reinforcements_a", "{!}kingdom 4 reinforcements a", icon_people_player|pf_label_small, 0, fac_commoners, aggressiveness_0, [(trp_lance_infantry_4, 2, 4), (trp_lance_infantry_3, 2, 4), (trp_lance_infantry_5, 2, 4), (trp_lance_archer_2, 2, 4), (trp_lance_infantry_2, 2, 4), (trp_lance_infantry_1, 2, 4)]),

	("kingdom_14_reinforcements_b", "{!}kingdom 4 reinforcements b", icon_people_player|pf_label_small, 0, fac_commoners, aggressiveness_0, [(trp_lance_infantry_4, 2, 4), (trp_lance_infantry_3, 2, 4), (trp_lance_infantry_5, 2, 4), (trp_lance_archer_2, 2, 4), (trp_lance_infantry_2, 2, 4), (trp_lance_infantry_1, 2, 4)]),

	("kingdom_14_reinforcements_c", "{!}kingdom 4 reinforcements c", icon_people_player|pf_label_small, 0, fac_commoners, aggressiveness_0, [(trp_lance_infantry_4, 2, 4), (trp_lance_infantry_3, 2, 4), (trp_lance_infantry_5, 2, 4), (trp_lance_archer_2, 2, 4), (trp_lance_infantry_2, 2, 4), (trp_lance_infantry_1, 2, 4)]),

	("kingdom_14_reinforcements_d", "{!}kingdom 4 reinforcements d", icon_people_player|pf_label_small, 0, fac_commoners, aggressiveness_0, [(trp_lance_infantry_4, 2, 4), (trp_lance_infantry_3, 2, 4), (trp_lance_infantry_5, 2, 4), (trp_lance_archer_2, 2, 4), (trp_lance_archer_5, 2, 4), (trp_lance_archer_2, 2, 4)]),

	("kingdom_14_reinforcements_e", "{!}kingdom 4 reinforcements e", icon_people_player|pf_label_small, 0, fac_commoners, aggressiveness_0, [(trp_lance_infantry_4, 2, 4), (trp_lance_infantry_3, 2, 4), (trp_lance_infantry_5, 2, 4), (trp_lance_archer_2, 2, 4), (trp_lance_archer_5, 2, 4), (trp_lance_archer_2, 2, 4)]),

	("kingdom_14_reinforcements_f", "{!}kingdom 4 reinforcements f", icon_people_player|pf_label_small, 0, fac_commoners, aggressiveness_0, [(trp_lance_infantry_4, 2, 4), (trp_lance_infantry_3, 2, 4), (trp_lance_infantry_5, 2, 4), (trp_lance_archer_2, 2, 4), (trp_lance_archer_5, 2, 4), (trp_lance_archer_2, 2, 4)]),

	("kingdom_15_reinforcements_a", "{!}kingdom 4 reinforcements a", icon_people_player|pf_label_small, 0, fac_commoners, aggressiveness_0, [(trp_lance_infantry_4, 2, 4), (trp_lance_infantry_3, 2, 4), (trp_lance_infantry_5, 2, 4), (trp_lance_archer_2, 2, 4), (trp_lance_infantry_2, 2, 4), (trp_lance_infantry_1, 2, 4)]),

	("kingdom_15_reinforcements_b", "{!}kingdom 4 reinforcements b", icon_people_player|pf_label_small, 0, fac_commoners, aggressiveness_0, [(trp_lance_infantry_4, 2, 4), (trp_lance_infantry_3, 2, 4), (trp_lance_infantry_5, 2, 4), (trp_lance_archer_2, 2, 4), (trp_lance_infantry_2, 2, 4), (trp_lance_infantry_1, 2, 4)]),

	("kingdom_15_reinforcements_c", "{!}kingdom 4 reinforcements c", icon_people_player|pf_label_small, 0, fac_commoners, aggressiveness_0, [(trp_lance_infantry_4, 2, 4), (trp_lance_infantry_3, 2, 4), (trp_lance_infantry_5, 2, 4), (trp_lance_archer_2, 2, 4), (trp_lance_infantry_2, 2, 4), (trp_lance_infantry_1, 2, 4)]),

	("kingdom_15_reinforcements_d", "{!}kingdom 4 reinforcements d", icon_people_player|pf_label_small, 0, fac_commoners, aggressiveness_0, [(trp_lance_infantry_4, 2, 4), (trp_lance_infantry_3, 2, 4), (trp_lance_infantry_5, 2, 4), (trp_lance_archer_2, 2, 4), (trp_lance_archer_5, 2, 4), (trp_lance_archer_2, 2, 4)]),

	("kingdom_15_reinforcements_e", "{!}kingdom 4 reinforcements e", icon_people_player|pf_label_small, 0, fac_commoners, aggressiveness_0, [(trp_lance_infantry_4, 2, 4), (trp_lance_infantry_3, 2, 4), (trp_lance_infantry_5, 2, 4), (trp_lance_archer_2, 2, 4), (trp_lance_archer_5, 2, 4), (trp_lance_archer_2, 2, 4)]),

	("kingdom_15_reinforcements_f", "{!}kingdom 4 reinforcements f", icon_people_player|pf_label_small, 0, fac_commoners, aggressiveness_0, [(trp_lance_infantry_4, 2, 4), (trp_lance_infantry_3, 2, 4), (trp_lance_infantry_5, 2, 4), (trp_lance_archer_2, 2, 4), (trp_lance_archer_5, 2, 4), (trp_lance_archer_2, 2, 4)]),

	("kingdom_16_reinforcements_a", "{!}kingdom 4 reinforcements a", icon_people_player|pf_label_small, 0, fac_commoners, aggressiveness_0, [(trp_lance_infantry_4, 2, 4), (trp_lance_infantry_3, 2, 4), (trp_lance_infantry_5, 2, 4), (trp_lance_archer_2, 2, 4), (trp_lance_infantry_2, 2, 4), (trp_lance_infantry_1, 2, 4)]),

	("kingdom_16_reinforcements_b", "{!}kingdom 4 reinforcements b", icon_people_player|pf_label_small, 0, fac_commoners, aggressiveness_0, [(trp_lance_infantry_4, 2, 4), (trp_lance_infantry_3, 2, 4), (trp_lance_infantry_5, 2, 4), (trp_lance_archer_2, 2, 4), (trp_lance_infantry_2, 2, 4), (trp_lance_infantry_1, 2, 4)]),

	("kingdom_16_reinforcements_c", "{!}kingdom 4 reinforcements c", icon_people_player|pf_label_small, 0, fac_commoners, aggressiveness_0, [(trp_lance_infantry_4, 2, 4), (trp_lance_infantry_3, 2, 4), (trp_lance_infantry_5, 2, 4), (trp_lance_archer_2, 2, 4), (trp_lance_infantry_2, 2, 4), (trp_lance_infantry_1, 2, 4)]),

	("kingdom_16_reinforcements_d", "{!}kingdom 4 reinforcements d", icon_people_player|pf_label_small, 0, fac_commoners, aggressiveness_0, [(trp_lance_infantry_4, 2, 4), (trp_lance_infantry_3, 2, 4), (trp_lance_infantry_5, 2, 4), (trp_lance_archer_2, 2, 4), (trp_lance_archer_5, 2, 4), (trp_lance_archer_2, 2, 4)]),

	("kingdom_16_reinforcements_e", "{!}kingdom 4 reinforcements e", icon_people_player|pf_label_small, 0, fac_commoners, aggressiveness_0, [(trp_lance_infantry_4, 2, 4), (trp_lance_infantry_3, 2, 4), (trp_lance_infantry_5, 2, 4), (trp_lance_archer_2, 2, 4), (trp_lance_archer_5, 2, 4), (trp_lance_archer_2, 2, 4)]),

	("kingdom_16_reinforcements_f", "{!}kingdom 4 reinforcements f", icon_people_player|pf_label_small, 0, fac_commoners, aggressiveness_0, [(trp_lance_infantry_4, 2, 4), (trp_lance_infantry_3, 2, 4), (trp_lance_infantry_5, 2, 4), (trp_lance_archer_2, 2, 4), (trp_lance_archer_5, 2, 4), (trp_lance_archer_2, 2, 4)]),

	("kingdom_17_reinforcements_a", "{!}kingdom 4 reinforcements a", icon_people_player|pf_label_small, 0, fac_commoners, aggressiveness_0, [(trp_lance_infantry_4, 2, 4), (trp_lance_infantry_3, 2, 4), (trp_lance_infantry_5, 2, 4), (trp_lance_archer_2, 2, 4), (trp_lance_infantry_2, 2, 4), (trp_lance_infantry_1, 2, 4)]),

	("kingdom_17_reinforcements_b", "{!}kingdom 4 reinforcements b", icon_people_player|pf_label_small, 0, fac_commoners, aggressiveness_0, [(trp_lance_infantry_4, 2, 4), (trp_lance_infantry_3, 2, 4), (trp_lance_infantry_5, 2, 4), (trp_lance_archer_2, 2, 4), (trp_lance_infantry_2, 2, 4), (trp_lance_infantry_1, 2, 4)]),

	("kingdom_17_reinforcements_c", "{!}kingdom 4 reinforcements c", icon_people_player|pf_label_small, 0, fac_commoners, aggressiveness_0, [(trp_lance_infantry_4, 2, 4), (trp_lance_infantry_3, 2, 4), (trp_lance_infantry_5, 2, 4), (trp_lance_archer_2, 2, 4), (trp_lance_infantry_2, 2, 4), (trp_lance_infantry_1, 2, 4)]),

	("kingdom_17_reinforcements_d", "{!}kingdom 4 reinforcements d", icon_people_player|pf_label_small, 0, fac_commoners, aggressiveness_0, [(trp_lance_infantry_4, 2, 4), (trp_lance_infantry_3, 2, 4), (trp_lance_infantry_5, 2, 4), (trp_lance_archer_2, 2, 4), (trp_lance_archer_5, 2, 4), (trp_lance_archer_2, 2, 4)]),

	("kingdom_17_reinforcements_e", "{!}kingdom 4 reinforcements e", icon_people_player|pf_label_small, 0, fac_commoners, aggressiveness_0, [(trp_lance_infantry_4, 2, 4), (trp_lance_infantry_3, 2, 4), (trp_lance_infantry_5, 2, 4), (trp_lance_archer_2, 2, 4), (trp_lance_archer_5, 2, 4), (trp_lance_archer_2, 2, 4)]),

	("kingdom_17_reinforcements_f", "{!}kingdom 4 reinforcements f", icon_people_player|pf_label_small, 0, fac_commoners, aggressiveness_0, [(trp_lance_infantry_4, 2, 4), (trp_lance_infantry_3, 2, 4), (trp_lance_infantry_5, 2, 4), (trp_lance_archer_2, 2, 4), (trp_lance_archer_5, 2, 4), (trp_lance_archer_2, 2, 4)]),

	("kingdom_18_reinforcements_a", "{!}kingdom 4 reinforcements a", icon_people_player|pf_label_small, 0, fac_commoners, aggressiveness_0, [(trp_lance_infantry_4, 2, 4), (trp_lance_infantry_3, 2, 4), (trp_lance_infantry_5, 2, 4), (trp_lance_archer_2, 2, 4), (trp_lance_infantry_2, 2, 4), (trp_lance_infantry_1, 2, 4)]),

	("kingdom_18_reinforcements_b", "{!}kingdom 4 reinforcements b", icon_people_player|pf_label_small, 0, fac_commoners, aggressiveness_0, [(trp_lance_infantry_4, 2, 4), (trp_lance_infantry_3, 2, 4), (trp_lance_infantry_5, 2, 4), (trp_lance_archer_2, 2, 4), (trp_lance_infantry_2, 2, 4), (trp_lance_infantry_1, 2, 4)]),

	("kingdom_18_reinforcements_c", "{!}kingdom 4 reinforcements c", icon_people_player|pf_label_small, 0, fac_commoners, aggressiveness_0, [(trp_lance_infantry_4, 2, 4), (trp_lance_infantry_3, 2, 4), (trp_lance_infantry_5, 2, 4), (trp_lance_archer_2, 2, 4), (trp_lance_infantry_2, 2, 4), (trp_lance_infantry_1, 2, 4)]),

	("kingdom_18_reinforcements_d", "{!}kingdom 4 reinforcements d", icon_people_player|pf_label_small, 0, fac_commoners, aggressiveness_0, [(trp_lance_infantry_4, 2, 4), (trp_lance_infantry_3, 2, 4), (trp_lance_infantry_5, 2, 4), (trp_lance_archer_2, 2, 4), (trp_lance_archer_5, 2, 4), (trp_lance_archer_2, 2, 4)]),

	("kingdom_18_reinforcements_e", "{!}kingdom 4 reinforcements e", icon_people_player|pf_label_small, 0, fac_commoners, aggressiveness_0, [(trp_lance_infantry_4, 2, 4), (trp_lance_infantry_3, 2, 4), (trp_lance_infantry_5, 2, 4), (trp_lance_archer_2, 2, 4), (trp_lance_archer_5, 2, 4), (trp_lance_archer_2, 2, 4)]),

	("kingdom_18_reinforcements_f", "{!}kingdom 4 reinforcements f", icon_people_player|pf_label_small, 0, fac_commoners, aggressiveness_0, [(trp_lance_infantry_4, 2, 4), (trp_lance_infantry_3, 2, 4), (trp_lance_infantry_5, 2, 4), (trp_lance_archer_2, 2, 4), (trp_lance_archer_5, 2, 4), (trp_lance_archer_2, 2, 4)]),

	("kingdom_19_reinforcements_a", "{!}kingdom 19 reinforcements a", icon_people_player|pf_label_small, 0, fac_commoners, aggressiveness_0, [(trp_sarranid_n_millet19, 2, 4), (trp_sarranid_n_ajam19, 2, 4), (trp_sarranid_n_cemaat19, 2, 4), (trp_sarranid_n_jebelus19, 2, 4), (trp_sarranid_n_yerliyya19, 2, 4), (trp_sarranid_n_cemaat19, 2, 4)]),

	("kingdom_19_reinforcements_b", "{!}kingdom 19 reinforcements b", icon_people_player|pf_label_small, 0, fac_commoners, aggressiveness_0, [(trp_sarranid_n_millet19, 2, 4), (trp_sarranid_n_ajam19, 2, 4), (trp_sarranid_n_cemaat19, 2, 4), (trp_sarranid_n_jebelus19, 2, 4), (trp_sarranid_n_yerliyya19, 2, 4), (trp_sarranid_n_cemaat19, 2, 4)]),

	("kingdom_19_reinforcements_c", "{!}kingdom 19 reinforcements c", icon_people_player|pf_label_small, 0, fac_commoners, aggressiveness_0, [(trp_sarranid_n_millet19, 2, 4), (trp_sarranid_n_ajam19, 2, 4), (trp_sarranid_n_cemaat19, 2, 4), (trp_sarranid_n_jebelus19, 2, 4), (trp_sarranid_n_yerliyya19, 2, 4), (trp_sarranid_n_cemaat19, 2, 4)]),

	("kingdom_19_reinforcements_d", "{!}kingdom 19 reinforcements d", icon_people_player|pf_label_small, 0, fac_commoners, aggressiveness_0, [(trp_sarranid_n_garip19, 2, 4), (trp_sarranid_n_yeniceri19, 2, 4), (trp_sarranid_n_kapikula19, 2, 4), (trp_sarranid_n_uluteci19, 2, 4), (trp_sarranid_n_cemaat19, 2, 4), (trp_sarranid_n_kapikula19, 2, 4)]),

	("kingdom_19_reinforcements_e", "{!}kingdom 19 reinforcements e", icon_people_player|pf_label_small, 0, fac_commoners, aggressiveness_0, [(trp_sarranid_n_millet19, 2, 4), (trp_sarranid_n_ajam19, 2, 4), (trp_sarranid_n_cemaat19, 2, 4), (trp_sarranid_n_jebelus19, 2, 4), (trp_sarranid_n_yerliyya19, 2, 4), (trp_sarranid_n_cemaat19, 2, 4)]),

	("kingdom_19_reinforcements_f", "{!}kingdom 19 reinforcements f", icon_people_player|pf_label_small, 0, fac_commoners, aggressiveness_0, [(trp_sarranid_n_garip19, 2, 4), (trp_sarranid_n_yeniceri19, 2, 4), (trp_sarranid_n_kapikula19, 2, 4), (trp_sarranid_n_uluteci19, 2, 4), (trp_sarranid_n_cemaat19, 2, 4), (trp_sarranid_n_kapikula19, 2, 4)]),

	("kingdom_20_reinforcements_a", "{!}kingdom 20 reinforcements a", icon_people_player|pf_label_small, 0, fac_commoners, aggressiveness_0, [(trp_sarranid_n_millet20, 2, 4), (trp_sarranid_n_ajam20, 2, 4), (trp_sarranid_n_cemaat20, 2, 4), (trp_sarranid_n_jebelus20, 2, 4), (trp_sarranid_n_yerliyya20, 2, 4), (trp_sarranid_n_cemaat20, 2, 4)]),

	("kingdom_20_reinforcements_b", "{!}kingdom 20 reinforcements b", icon_people_player|pf_label_small, 0, fac_commoners, aggressiveness_0, [(trp_sarranid_n_millet20, 2, 4), (trp_sarranid_n_ajam20, 2, 4), (trp_sarranid_n_cemaat20, 2, 4), (trp_sarranid_n_jebelus20, 2, 4), (trp_sarranid_n_yerliyya20, 2, 4), (trp_sarranid_n_cemaat20, 2, 4)]),

	("kingdom_20_reinforcements_c", "{!}kingdom 20 reinforcements c", icon_people_player|pf_label_small, 0, fac_commoners, aggressiveness_0, [(trp_sarranid_n_millet20, 2, 4), (trp_sarranid_n_ajam20, 2, 4), (trp_sarranid_n_cemaat20, 2, 4), (trp_sarranid_n_jebelus20, 2, 4), (trp_sarranid_n_yerliyya20, 2, 4), (trp_sarranid_n_cemaat20, 2, 4)]),

	("kingdom_20_reinforcements_d", "{!}kingdom 20 reinforcements d", icon_people_player|pf_label_small, 0, fac_commoners, aggressiveness_0, [(trp_sarranid_n_garip20, 2, 4), (trp_sarranid_n_yeniceri20, 2, 4), (trp_sarranid_n_kapikula20, 2, 4), (trp_sarranid_n_uluteci20, 2, 4), (trp_sarranid_n_cemaat20, 2, 4), (trp_sarranid_n_kapikula20, 2, 4)]),

	("kingdom_20_reinforcements_e", "{!}kingdom 20 reinforcements e", icon_people_player|pf_label_small, 0, fac_commoners, aggressiveness_0, [(trp_sarranid_n_millet20, 2, 4), (trp_sarranid_n_ajam20, 2, 4), (trp_sarranid_n_cemaat20, 2, 4), (trp_sarranid_n_jebelus20, 2, 4), (trp_sarranid_n_yerliyya20, 2, 4), (trp_sarranid_n_cemaat20, 2, 4)]),

	("kingdom_20_reinforcements_f", "{!}kingdom 20 reinforcements f", icon_people_player|pf_label_small, 0, fac_commoners, aggressiveness_0, [(trp_sarranid_n_garip20, 2, 4), (trp_sarranid_n_yeniceri20, 2, 4), (trp_sarranid_n_kapikula20, 2, 4), (trp_sarranid_n_uluteci20, 2, 4), (trp_sarranid_n_cemaat20, 2, 4), (trp_sarranid_n_kapikula20, 2, 4)]),

	("kingdom_21_reinforcements_a", "{!}kingdom 21 reinforcements a", icon_people_player|pf_label_small, 0, fac_commoners, aggressiveness_0, [(trp_sarranid_n_millet22, 2, 4), (trp_sarranid_n_ajam22, 2, 4), (trp_sarranid_n_cemaat22, 2, 4), (trp_sarranid_n_jebelus22, 2, 4), (trp_sarranid_n_yeniceri22, 2, 4), (trp_sarranid_n_kapikula22, 2, 4)]),

	("kingdom_21_reinforcements_b", "{!}kingdom 21 reinforcements b", icon_people_player|pf_label_small, 0, fac_commoners, aggressiveness_0, [(trp_sarranid_n_millet22, 2, 4), (trp_sarranid_n_ajam22, 2, 4), (trp_sarranid_n_cemaat22, 2, 4), (trp_sarranid_n_jebelus22, 2, 4), (trp_sarranid_n_yeniceri22, 2, 4), (trp_sarranid_n_kapikula22, 2, 4)]),

	("kingdom_21_reinforcements_c", "{!}kingdom 21 reinforcements c", icon_people_player|pf_label_small, 0, fac_commoners, aggressiveness_0, [(trp_sarranid_n_uluteci22, 2, 4), (trp_sarranid_n_ajam22, 2, 4), (trp_sarranid_n_cemaat22, 2, 4), (trp_sarranid_n_jebelus22, 2, 4), (trp_sarranid_n_yeniceri22, 2, 4), (trp_sarranid_n_kapikula22, 2, 4)]),

	("kingdom_21_reinforcements_d", "{!}kingdom 21 reinforcements d", icon_people_player|pf_label_small, 0, fac_commoners, aggressiveness_0, [(trp_sarranid_n_uluteci22, 2, 4), (trp_sarranid_n_ajam22, 2, 4), (trp_sarranid_n_cemaat22, 2, 4), (trp_sarranid_n_jebelus22, 2, 4), (trp_sarranid_n_yeniceri22, 2, 4), (trp_sarranid_n_kapikula22, 2, 4)]),

	("kingdom_21_reinforcements_e", "{!}kingdom 21 reinforcements e", icon_people_player|pf_label_small, 0, fac_commoners, aggressiveness_0, [(trp_sarranid_n_uluteci22, 2, 4), (trp_sarranid_n_ajam22, 2, 4), (trp_sarranid_n_cemaat22, 2, 4), (trp_sarranid_n_jebelus22, 2, 4), (trp_sarranid_n_yeniceri22, 2, 4), (trp_sarranid_n_kapikula22, 2, 4)]),

	("kingdom_21_reinforcements_f", "{!}kingdom 21 reinforcements f", icon_people_player|pf_label_small, 0, fac_commoners, aggressiveness_0, [(trp_sarranid_n_uluteci22, 2, 4), (trp_sarranid_n_ajam22, 2, 4), (trp_sarranid_n_cemaat22, 2, 4), (trp_sarranid_n_jebelus22, 2, 4), (trp_sarranid_n_yeniceri22, 2, 4), (trp_sarranid_n_kapikula22, 2, 4)]),

	("kingdom_22_reinforcements_a", "{!}kingdom 22 reinforcements a", icon_people_player|pf_label_small, 0, fac_commoners, aggressiveness_0, [(trp_sarranid_n_millet23, 2, 4), (trp_sarranid_n_ajam23, 2, 4), (trp_sarranid_n_cemaat23, 2, 4), (trp_sarranid_n_jebelus23, 2, 4), (trp_sarranid_n_yeniceri23, 2, 4), (trp_sarranid_n_yeniceri23, 2, 4)]),

	("kingdom_22_reinforcements_b", "{!}kingdom 22 reinforcements b", icon_people_player|pf_label_small, 0, fac_commoners, aggressiveness_0, [(trp_sarranid_n_millet23, 2, 4), (trp_sarranid_n_ajam23, 2, 4), (trp_sarranid_n_cemaat23, 2, 4), (trp_sarranid_n_jebelus23, 2, 4), (trp_sarranid_n_yeniceri23, 2, 4), (trp_sarranid_n_yeniceri23, 2, 4)]),

	("kingdom_22_reinforcements_c", "{!}kingdom 22 reinforcements c", icon_people_player|pf_label_small, 0, fac_commoners, aggressiveness_0, [(trp_sarranid_n_millet23, 2, 4), (trp_sarranid_n_ajam23, 2, 4), (trp_sarranid_n_cemaat23, 2, 4), (trp_sarranid_n_jebelus23, 2, 4), (trp_sarranid_n_yeniceri23, 2, 4), (trp_sarranid_n_yeniceri23, 2, 4)]),

	("kingdom_22_reinforcements_d", "{!}kingdom 22 reinforcements d", icon_people_player|pf_label_small, 0, fac_commoners, aggressiveness_0, [(trp_sarranid_n_millet23, 2, 4), (trp_sarranid_n_ajam23, 2, 4), (trp_sarranid_n_cemaat23, 2, 4), (trp_sarranid_n_jebelus23, 2, 4), (trp_sarranid_n_yeniceri23, 2, 4), (trp_sarranid_n_yeniceri23, 2, 4)]),

	("kingdom_22_reinforcements_e", "{!}kingdom 22 reinforcements e", icon_people_player|pf_label_small, 0, fac_commoners, aggressiveness_0, [(trp_sarranid_n_millet23, 2, 4), (trp_sarranid_n_ajam23, 2, 4), (trp_sarranid_n_cemaat23, 2, 4), (trp_sarranid_n_jebelus23, 2, 4), (trp_sarranid_n_yeniceri23, 2, 4), (trp_sarranid_n_yeniceri23, 2, 4)]),

	("kingdom_22_reinforcements_f", "{!}kingdom 22 reinforcements f", icon_people_player|pf_label_small, 0, fac_commoners, aggressiveness_0, [(trp_sarranid_n_millet23, 2, 4), (trp_sarranid_n_ajam23, 2, 4), (trp_sarranid_n_cemaat23, 2, 4), (trp_sarranid_n_jebelus23, 2, 4), (trp_sarranid_n_yeniceri23, 2, 4), (trp_sarranid_n_yeniceri23, 2, 4)]),

	("kingdom_1_reinforcements_a_r", "{!}kingdom 1 reinforcements a", icon_people_player|pf_label_small, 0, fac_commoners, aggressiveness_0, [(trp_sarranid_n_cemaat1, 2, 4), (trp_sarranid_n_ajam1, 2, 4), (trp_sarranid_n_cemaat1, 2, 4), (trp_sarranid_n_jebelus1, 2, 4), (trp_sarranid_n_yerliyya1, 2, 4), (trp_sarranid_n_cemaat1, 2, 4)]),

	("kingdom_1_reinforcements_b_r", "{!}kingdom 1 reinforcements b", icon_people_player|pf_label_small, 0, fac_commoners, aggressiveness_0, [(trp_sarranid_n_millet1, 2, 4), (trp_stormlands_troop_1, 2, 4), (trp_sarranid_n_yeniceri1, 2, 4), (trp_sarranid_n_kapikula1, 2, 4), (trp_sarranid_n_uluteci1, 2, 4), (trp_sarranid_n_cemaat1, 1, 2)]),

	("kingdom_1_reinforcements_c_r", "{!}kingdom 1 reinforcements c", icon_people_player|pf_label_small, 0, fac_commoners, aggressiveness_0, [(trp_sarranid_n_millet1, 2, 4), (trp_sarranid_n_ajam1, 2, 4), (trp_sarranid_n_cemaat1, 2, 4), (trp_sarranid_n_jebelus1, 2, 4), (trp_sarranid_n_yerliyya1, 2, 4), (trp_sarranid_n_cemaat1, 1, 2)]),

	("kingdom_1_reinforcements_d_r", "{!}kingdom 1 reinforcements d", icon_people_player|pf_label_small, 0, fac_commoners, aggressiveness_0, [(trp_sarranid_n_garip1, 2, 4), (trp_stormlands_troop_1, 2, 4), (trp_sarranid_n_yeniceri1, 2, 4), (trp_sarranid_n_kapikula1, 2, 4), (trp_sarranid_n_uluteci1, 2, 4), (trp_sarranid_n_cemaat1, 1, 2)]),

	("kingdom_1_reinforcements_e_r", "{!}kingdom 1 reinforcements e", icon_people_player|pf_label_small, 0, fac_commoners, aggressiveness_0, [(trp_sarranid_n_millet1, 2, 4), (trp_sarranid_n_ajam1, 2, 4), (trp_sarranid_n_cemaat1, 2, 4), (trp_sarranid_n_jebelus1, 2, 4), (trp_sarranid_n_yerliyya1, 2, 4), (trp_sarranid_n_cemaat1, 1, 2)]),

	("kingdom_1_reinforcements_f_r", "{!}kingdom 1 reinforcements f", icon_people_player|pf_label_small, 0, fac_commoners, aggressiveness_0, [(trp_sarranid_n_garip1, 2, 4), (trp_stormlands_troop_1, 2, 4), (trp_sarranid_n_yeniceri1, 2, 4), (trp_sarranid_n_kapikula1, 2, 4), (trp_sarranid_n_uluteci1, 2, 4), (trp_sarranid_n_cemaat1, 1, 2)]),

	("kingdom_2_reinforcements_a_r", "{!}kingdom 2 reinforcements a", icon_people_player|pf_label_small, 0, fac_commoners, aggressiveness_0, [(trp_sarranid_n_millet2, 2, 4), (trp_sarranid_n_ajam2, 2, 4), (trp_sarranid_n_cemaat2, 2, 4), (trp_sarranid_n_jebelus2, 2, 4), (trp_sarranid_n_yerliyya2, 2, 4), (trp_sarranid_n_cemaat2, 1, 2)]),

	("kingdom_2_reinforcements_b_r", "{!}kingdom 2 reinforcements b", icon_people_player|pf_label_small, 0, fac_commoners, aggressiveness_0, [(trp_sarranid_n_garip2, 2, 4), (trp_northern_troop_1, 2, 4), (trp_sarranid_n_yeniceri2, 2, 4), (trp_sarranid_n_kapikula2, 2, 4), (trp_sarranid_n_uluteci2, 2, 4), (trp_sarranid_n_cemaat2, 1, 2)]),

	("kingdom_2_reinforcements_c_r", "{!}kingdom 2 reinforcements c", icon_people_player|pf_label_small, 0, fac_commoners, aggressiveness_0, [(trp_sarranid_n_millet2, 2, 4), (trp_sarranid_n_ajam2, 2, 4), (trp_sarranid_n_cemaat2, 2, 4), (trp_sarranid_n_jebelus2, 2, 4), (trp_sarranid_n_yerliyya2, 2, 4), (trp_sarranid_n_cemaat2, 1, 2)]),

	("kingdom_2_reinforcements_d_r", "{!}kingdom 2 reinforcements d", icon_people_player|pf_label_small, 0, fac_commoners, aggressiveness_0, [(trp_sarranid_n_garip2, 2, 4), (trp_northern_troop_1, 2, 4), (trp_sarranid_n_yeniceri2, 2, 4), (trp_sarranid_n_kapikula2, 2, 4), (trp_sarranid_n_uluteci2, 2, 4), (trp_sarranid_n_cemaat2, 1, 2)]),

	("kingdom_2_reinforcements_e_r", "{!}kingdom 2 reinforcements e", icon_people_player|pf_label_small, 0, fac_commoners, aggressiveness_0, [(trp_sarranid_n_millet2, 2, 4), (trp_sarranid_n_ajam2, 2, 4), (trp_sarranid_n_cemaat2, 2, 4), (trp_sarranid_n_jebelus2, 2, 4), (trp_sarranid_n_yerliyya2, 2, 4), (trp_sarranid_n_cemaat2, 1, 2)]),

	("kingdom_2_reinforcements_f_r", "{!}kingdom 2 reinforcements f", icon_people_player|pf_label_small, 0, fac_commoners, aggressiveness_0, [(trp_sarranid_n_garip2, 2, 4), (trp_northern_troop_1, 2, 4), (trp_sarranid_n_yeniceri2, 2, 4), (trp_sarranid_n_kapikula2, 2, 4), (trp_sarranid_n_uluteci2, 2, 4), (trp_sarranid_n_cemaat2, 1, 2)]),

	("kingdom_3_reinforcements_a_r", "{!}kingdom 3 reinforcements a", icon_people_player|pf_label_small, 0, fac_commoners, aggressiveness_0, [(trp_sarranid_n_millet3, 2, 4), (trp_sarranid_n_ajam3, 2, 4), (trp_sarranid_n_cemaat3, 2, 4), (trp_sarranid_n_jebelus3, 2, 4), (trp_sarranid_n_yerliyya3, 2, 4), (trp_sarranid_n_cemaat3, 1, 2)]),

	("kingdom_3_reinforcements_b_r", "{!}kingdom 3 reinforcements b", icon_people_player|pf_label_small, 0, fac_commoners, aggressiveness_0, [(trp_sarranid_n_garip3, 2, 4), (trp_vale_troop_1, 2, 4), (trp_sarranid_n_yeniceri3, 2, 4), (trp_sarranid_n_kapikula3, 2, 4), (trp_sarranid_n_uluteci3, 2, 4), (trp_sarranid_n_cemaat3, 1, 2)]),

	("kingdom_3_reinforcements_c_r", "{!}kingdom 3 reinforcements c", icon_people_player|pf_label_small, 0, fac_commoners, aggressiveness_0, [(trp_sarranid_n_millet3, 2, 4), (trp_sarranid_n_ajam3, 2, 4), (trp_sarranid_n_cemaat3, 2, 4), (trp_sarranid_n_jebelus3, 2, 4), (trp_sarranid_n_yerliyya3, 2, 4), (trp_sarranid_n_cemaat3, 1, 2)]),

	("kingdom_3_reinforcements_d_r", "{!}kingdom 3 reinforcements d", icon_people_player|pf_label_small, 0, fac_commoners, aggressiveness_0, [(trp_sarranid_n_garip3, 2, 4), (trp_vale_troop_1, 2, 4), (trp_sarranid_n_yeniceri3, 2, 4), (trp_sarranid_n_kapikula3, 2, 4), (trp_sarranid_n_uluteci3, 2, 4), (trp_sarranid_n_cemaat3, 1, 2)]),

	("kingdom_3_reinforcements_e_r", "{!}kingdom 3 reinforcements e", icon_people_player|pf_label_small, 0, fac_commoners, aggressiveness_0, [(trp_sarranid_n_millet3, 2, 4), (trp_sarranid_n_ajam3, 2, 4), (trp_sarranid_n_cemaat3, 2, 4), (trp_sarranid_n_jebelus3, 2, 4), (trp_sarranid_n_yerliyya3, 2, 4), (trp_sarranid_n_cemaat3, 1, 2)]),

	("kingdom_3_reinforcements_f_r", "{!}kingdom 3 reinforcements f", icon_people_player|pf_label_small, 0, fac_commoners, aggressiveness_0, [(trp_sarranid_n_garip3, 2, 4), (trp_vale_troop_1, 2, 4), (trp_sarranid_n_yeniceri3, 2, 4), (trp_sarranid_n_kapikula3, 2, 4), (trp_sarranid_n_uluteci3, 2, 4), (trp_sarranid_n_cemaat3, 1, 2)]),

	("kingdom_4_reinforcements_a_r", "{!}kingdom 4 reinforcements a", icon_people_player|pf_label_small, 0, fac_commoners, aggressiveness_0, [(trp_lance_infantry_4, 2, 4), (trp_lance_infantry_3, 2, 4), (trp_lance_infantry_5, 2, 4), (trp_lance_archer_2, 2, 4), (trp_lance_infantry_2, 2, 4), (trp_lance_infantry_1, 2, 4)]),

	("kingdom_4_reinforcements_b_r", "{!}kingdom 4 reinforcements b", icon_people_player|pf_label_small, 0, fac_commoners, aggressiveness_0, [(trp_lance_infantry_4, 2, 4), (trp_lance_infantry_3, 2, 4), (trp_lance_infantry_5, 2, 4), (trp_lance_archer_2, 2, 4), (trp_lance_infantry_2, 2, 4), (trp_lance_infantry_1, 2, 4)]),

	("kingdom_4_reinforcements_c_r", "{!}kingdom 4 reinforcements c", icon_people_player|pf_label_small, 0, fac_commoners, aggressiveness_0, [(trp_lance_infantry_4, 2, 4), (trp_lance_infantry_3, 2, 4), (trp_lance_infantry_5, 2, 4), (trp_lance_archer_2, 2, 4), (trp_lance_infantry_2, 2, 4), (trp_lance_infantry_1, 2, 4)]),

	("kingdom_4_reinforcements_d_r", "{!}kingdom 4 reinforcements d", icon_people_player|pf_label_small, 0, fac_commoners, aggressiveness_0, [(trp_lance_infantry_4, 2, 4), (trp_lance_infantry_3, 2, 4), (trp_lance_infantry_5, 2, 4), (trp_lance_archer_2, 2, 4), (trp_lance_archer_5, 2, 4), (trp_lance_archer_2, 2, 4)]),

	("kingdom_4_reinforcements_e_r", "{!}kingdom 4 reinforcements e", icon_people_player|pf_label_small, 0, fac_commoners, aggressiveness_0, [(trp_lance_infantry_4, 2, 4), (trp_lance_infantry_3, 2, 4), (trp_lance_infantry_5, 2, 4), (trp_lance_archer_2, 2, 4), (trp_lance_archer_5, 2, 4), (trp_lance_archer_2, 2, 4)]),

	("kingdom_4_reinforcements_f_r", "{!}kingdom 4 reinforcements f", icon_people_player|pf_label_small, 0, fac_commoners, aggressiveness_0, [(trp_lance_infantry_4, 2, 4), (trp_lance_infantry_3, 2, 4), (trp_lance_infantry_5, 2, 4), (trp_lance_archer_2, 2, 4), (trp_lance_archer_5, 2, 4), (trp_lance_archer_2, 2, 4)]),

	("kingdom_5_reinforcements_a_r", "{!}kingdom 5 reinforcements a", icon_people_player|pf_label_small, 0, fac_commoners, aggressiveness_0, [(trp_lance_infantry_4, 2, 4), (trp_lance_infantry_3, 2, 4), (trp_lance_infantry_5, 2, 4), (trp_lance_archer_2, 2, 4), (trp_lance_infantry_2, 2, 4), (trp_lance_infantry_1, 2, 4)]),

	("kingdom_5_reinforcements_b_r", "{!}kingdom 5 reinforcements b", icon_people_player|pf_label_small, 0, fac_commoners, aggressiveness_0, [(trp_lance_infantry_4, 2, 4), (trp_lance_infantry_3, 2, 4), (trp_lance_infantry_5, 2, 4), (trp_lance_archer_2, 2, 4), (trp_lance_infantry_2, 2, 4), (trp_lance_infantry_1, 2, 4)]),

	("kingdom_5_reinforcements_c_r", "{!}kingdom 5 reinforcements c", icon_people_player|pf_label_small, 0, fac_commoners, aggressiveness_0, [(trp_lance_infantry_4, 2, 4), (trp_lance_infantry_3, 2, 4), (trp_lance_infantry_5, 2, 4), (trp_lance_archer_2, 2, 4), (trp_lance_infantry_2, 2, 4), (trp_lance_infantry_1, 2, 4)]),

	("kingdom_5_reinforcements_d_r", "{!}kingdom 5 reinforcements d", icon_people_player|pf_label_small, 0, fac_commoners, aggressiveness_0, [(trp_lance_infantry_4, 2, 4), (trp_lance_infantry_3, 2, 4), (trp_lance_infantry_5, 2, 4), (trp_lance_archer_2, 2, 4), (trp_lance_archer_5, 2, 4), (trp_lance_archer_2, 2, 4)]),

	("kingdom_5_reinforcements_e_r", "{!}kingdom 5 reinforcements e", icon_people_player|pf_label_small, 0, fac_commoners, aggressiveness_0, [(trp_lance_infantry_4, 2, 4), (trp_lance_infantry_3, 2, 4), (trp_lance_infantry_5, 2, 4), (trp_lance_archer_2, 2, 4), (trp_lance_archer_5, 2, 4), (trp_lance_archer_2, 2, 4)]),

	("kingdom_5_reinforcements_f_r", "{!}kingdom 5 reinforcements f", icon_people_player|pf_label_small, 0, fac_commoners, aggressiveness_0, [(trp_lance_infantry_4, 2, 4), (trp_lance_infantry_3, 2, 4), (trp_lance_infantry_5, 2, 4), (trp_lance_archer_2, 2, 4), (trp_lance_archer_5, 2, 4), (trp_lance_archer_2, 2, 4)]),

	("kingdom_6_reinforcements_a_r", "{!}kingdom 6 reinforcements a", icon_people_player|pf_label_small, 0, fac_commoners, aggressiveness_0, [(trp_sarranid_n_millet, 2, 4), (trp_sarranid_n_ajam, 2, 4), (trp_sarranid_n_cemaat, 2, 4), (trp_sarranid_n_jebelus, 2, 4), (trp_sarranid_n_yerliyya, 2, 4), (trp_sarranid_n_cemaat, 1, 2)]),

	("kingdom_6_reinforcements_b_r", "{!}kingdom 6 reinforcements b", icon_people_player|pf_label_small, 0, fac_commoners, aggressiveness_0, [(trp_sarranid_n_garip, 2, 4), (trp_dorne_troop_1, 2, 4), (trp_sarranid_n_yeniceri, 2, 4), (trp_sarranid_n_kapikula, 2, 4), (trp_sarranid_n_uluteci, 2, 4), (trp_sarranid_n_cemaat, 1, 2)]),

	("kingdom_6_reinforcements_c_r", "{!}kingdom 6 reinforcements c", icon_people_player|pf_label_small, 0, fac_commoners, aggressiveness_0, [(trp_sarranid_n_millet, 2, 4), (trp_sarranid_n_ajam, 2, 4), (trp_sarranid_n_cemaat, 2, 4), (trp_sarranid_n_jebelus, 2, 4), (trp_sarranid_n_yerliyya, 2, 4), (trp_sarranid_n_cemaat, 1, 2)]),

	("kingdom_6_reinforcements_d_r", "{!}kingdom 6 reinforcements d", icon_people_player|pf_label_small, 0, fac_commoners, aggressiveness_0, [(trp_sarranid_n_garip, 2, 4), (trp_dorne_troop_1, 2, 4), (trp_sarranid_n_yeniceri, 2, 4), (trp_sarranid_n_kapikula, 2, 4), (trp_sarranid_n_uluteci, 2, 4), (trp_sarranid_n_cemaat, 1, 2)]),

	("kingdom_6_reinforcements_e_r", "{!}kingdom 6 reinforcements e", icon_people_player|pf_label_small, 0, fac_commoners, aggressiveness_0, [(trp_sarranid_n_millet, 2, 4), (trp_sarranid_n_ajam, 2, 4), (trp_sarranid_n_cemaat, 2, 4), (trp_sarranid_n_jebelus, 2, 4), (trp_sarranid_n_yerliyya, 2, 4), (trp_sarranid_n_cemaat, 1, 2)]),

	("kingdom_6_reinforcements_f_r", "{!}kingdom 6 reinforcements f", icon_people_player|pf_label_small, 0, fac_commoners, aggressiveness_0, [(trp_sarranid_n_garip, 2, 4), (trp_dorne_troop_1, 2, 4), (trp_sarranid_n_yeniceri, 2, 4), (trp_sarranid_n_kapikula, 2, 4), (trp_sarranid_n_uluteci, 2, 4), (trp_sarranid_n_cemaat, 1, 2)]),

	("kingdom_7_reinforcements_a_r", "{!}kingdom 7 reinforcements a", icon_people_player|pf_label_small, 0, fac_commoners, aggressiveness_0, [(trp_sarranid_n_millet21, 2, 4), (trp_sarranid_n_ajam21, 2, 4), (trp_sarranid_n_cemaat21, 2, 4), (trp_sarranid_n_jebelus21, 2, 4), (trp_sarranid_n_yerliyya21, 2, 4), (trp_sarranid_n_cemaat21, 1, 2)]),

	("kingdom_7_reinforcements_b_r", "{!}kingdom 7 reinforcements b", icon_people_player|pf_label_small, 0, fac_commoners, aggressiveness_0, [(trp_sarranid_n_garip21, 2, 4), (trp_sarranid_n_yeniceri21, 2, 4), (trp_sarranid_n_kapikula21, 2, 4), (trp_sarranid_n_uluteci21, 2, 4), (trp_sarranid_n_cemaat21, 2, 4), (trp_sarranid_n_yerliyya21, 1, 2)]),

	("kingdom_7_reinforcements_c_r", "{!}kingdom 7 reinforcements c", icon_people_player|pf_label_small, 0, fac_commoners, aggressiveness_0, [(trp_sarranid_n_millet21, 2, 4), (trp_sarranid_n_ajam21, 2, 4), (trp_sarranid_n_cemaat21, 2, 4), (trp_sarranid_n_jebelus21, 2, 4), (trp_sarranid_n_yerliyya21, 2, 4), (trp_sarranid_n_cemaat21, 1, 2)]),

	("kingdom_7_reinforcements_d_r", "{!}kingdom 7 reinforcements d", icon_people_player|pf_label_small, 0, fac_commoners, aggressiveness_0, [(trp_sarranid_n_garip21, 2, 4), (trp_sarranid_n_yeniceri21, 2, 4), (trp_sarranid_n_kapikula21, 2, 4), (trp_sarranid_n_uluteci21, 2, 4), (trp_sarranid_n_cemaat21, 2, 4), (trp_sarranid_n_yerliyya21, 1, 2)]),

	("kingdom_7_reinforcements_e_r", "{!}kingdom 7 reinforcements e", icon_people_player|pf_label_small, 0, fac_commoners, aggressiveness_0, [(trp_sarranid_n_millet21, 2, 4), (trp_sarranid_n_ajam21, 2, 4), (trp_sarranid_n_cemaat21, 2, 4), (trp_sarranid_n_jebelus21, 2, 4), (trp_sarranid_n_yerliyya21, 2, 4), (trp_sarranid_n_cemaat21, 1, 2)]),

	("kingdom_7_reinforcements_f_r", "{!}kingdom 7 reinforcements f", icon_people_player|pf_label_small, 0, fac_commoners, aggressiveness_0, [(trp_sarranid_n_garip21, 2, 4), (trp_sarranid_n_yeniceri21, 2, 4), (trp_sarranid_n_kapikula21, 2, 4), (trp_sarranid_n_uluteci21, 2, 4), (trp_sarranid_n_cemaat21, 2, 4), (trp_sarranid_n_yerliyya21, 1, 2)]),

	("kingdom_8_reinforcements_a_r", "{!}kingdom 8 reinforcements a", icon_people_player|pf_label_small, 0, fac_commoners, aggressiveness_0, [(trp_sarranid_n_millet8, 2, 4), (trp_sarranid_n_ajam8, 2, 4), (trp_sarranid_n_cemaat8, 2, 4), (trp_sarranid_n_jebelus8, 2, 4), (trp_sarranid_n_yerliyya8, 2, 4), (trp_sarranid_n_cemaat8, 1, 2)]),

	("kingdom_8_reinforcements_b_r", "{!}kingdom 8 reinforcements b", icon_people_player|pf_label_small, 0, fac_commoners, aggressiveness_0, [(trp_sarranid_n_garip8, 2, 4), (trp_dragonstone_troop_1, 2, 4), (trp_sarranid_n_yeniceri8, 2, 4), (trp_sarranid_n_kapikula8, 2, 4), (trp_sarranid_n_uluteci8, 2, 4), (trp_sarranid_n_cemaat8, 1, 2)]),

	("kingdom_8_reinforcements_c_r", "{!}kingdom 8 reinforcements c", icon_people_player|pf_label_small, 0, fac_commoners, aggressiveness_0, [(trp_sarranid_n_millet8, 2, 4), (trp_sarranid_n_ajam8, 2, 4), (trp_sarranid_n_cemaat8, 2, 4), (trp_sarranid_n_jebelus8, 2, 4), (trp_sarranid_n_yerliyya8, 2, 4), (trp_sarranid_n_cemaat8, 1, 2)]),

	("kingdom_8_reinforcements_d_r", "{!}kingdom 8 reinforcements d", icon_people_player|pf_label_small, 0, fac_commoners, aggressiveness_0, [(trp_sarranid_n_garip8, 2, 4), (trp_dragonstone_troop_1, 2, 4), (trp_sarranid_n_yeniceri8, 2, 4), (trp_sarranid_n_kapikula8, 2, 4), (trp_sarranid_n_uluteci8, 2, 4), (trp_sarranid_n_cemaat8, 1, 2)]),

	("kingdom_8_reinforcements_e_r", "{!}kingdom 8 reinforcements e", icon_people_player|pf_label_small, 0, fac_commoners, aggressiveness_0, [(trp_sarranid_n_millet8, 2, 4), (trp_sarranid_n_ajam8, 2, 4), (trp_sarranid_n_cemaat8, 2, 4), (trp_sarranid_n_jebelus8, 2, 4), (trp_sarranid_n_yerliyya8, 2, 4), (trp_sarranid_n_cemaat8, 1, 2)]),

	("kingdom_8_reinforcements_f_r", "{!}kingdom 8 reinforcements f", icon_people_player|pf_label_small, 0, fac_commoners, aggressiveness_0, [(trp_sarranid_n_garip8, 2, 4), (trp_dragonstone_troop_1, 2, 4), (trp_sarranid_n_yeniceri8, 2, 4), (trp_sarranid_n_kapikula8, 2, 4), (trp_sarranid_n_uluteci8, 2, 4), (trp_sarranid_n_cemaat8, 1, 2)]),

	("kingdom_9_reinforcements_a_r", "{!}kingdom 9 reinforcements a", icon_people_player|pf_label_small, 0, fac_commoners, aggressiveness_0, [(trp_sarranid_n_cemaat9, 2, 4), (trp_sarranid_n_ajam9, 2, 4), (trp_sarranid_n_cemaat9, 2, 4), (trp_sarranid_n_jebelus9, 2, 4), (trp_sarranid_n_yerliyya9, 2, 4), (trp_sarranid_n_cemaat9, 1, 2)]),

	("kingdom_9_reinforcements_b_r", "{!}kingdom 9 reinforcements b", icon_people_player|pf_label_small, 0, fac_commoners, aggressiveness_0, [(trp_sarranid_n_millet9, 2, 4), (trp_westerlands_troop_1, 2, 4), (trp_sarranid_n_yeniceri9, 2, 4), (trp_sarranid_n_kapikula9, 2, 4), (trp_sarranid_n_uluteci9, 2, 4), (trp_sarranid_n_cemaat9, 1, 2)]),

	("kingdom_9_reinforcements_c_r", "{!}kingdom 9 reinforcements c", icon_people_player|pf_label_small, 0, fac_commoners, aggressiveness_0, [(trp_sarranid_n_millet9, 2, 4), (trp_sarranid_n_ajam9, 2, 4), (trp_sarranid_n_cemaat9, 2, 4), (trp_sarranid_n_jebelus9, 2, 4), (trp_sarranid_n_yerliyya9, 2, 4), (trp_sarranid_n_cemaat9, 1, 2)]),

	("kingdom_9_reinforcements_d_r", "{!}kingdom 9 reinforcements d", icon_people_player|pf_label_small, 0, fac_commoners, aggressiveness_0, [(trp_sarranid_n_garip9, 2, 4), (trp_westerlands_troop_1, 2, 4), (trp_sarranid_n_yeniceri9, 2, 4), (trp_sarranid_n_kapikula9, 2, 4), (trp_sarranid_n_uluteci9, 2, 4), (trp_sarranid_n_cemaat9, 1, 2)]),

	("kingdom_9_reinforcements_e_r", "{!}kingdom 9 reinforcements e", icon_people_player|pf_label_small, 0, fac_commoners, aggressiveness_0, [(trp_sarranid_n_millet9, 2, 4), (trp_sarranid_n_ajam9, 2, 4), (trp_sarranid_n_cemaat9, 2, 4), (trp_sarranid_n_jebelus9, 2, 4), (trp_sarranid_n_yerliyya9, 2, 4), (trp_sarranid_n_cemaat9, 1, 2)]),

	("kingdom_9_reinforcements_f_r", "{!}kingdom 9 reinforcements f", icon_people_player|pf_label_small, 0, fac_commoners, aggressiveness_0, [(trp_sarranid_n_garip9, 2, 4), (trp_westerlands_troop_1, 2, 4), (trp_sarranid_n_yeniceri9, 2, 4), (trp_sarranid_n_kapikula9, 2, 4), (trp_sarranid_n_uluteci9, 2, 4), (trp_sarranid_n_cemaat9, 1, 2)]),

	("kingdom_10_reinforcements_a_r", "{!}kingdom 10 reinforcements a", icon_people_player|pf_label_small, 0, fac_commoners, aggressiveness_0, [(trp_sarranid_n_cemaat10, 2, 4), (trp_sarranid_n_ajam10, 2, 4), (trp_sarranid_n_cemaat10, 2, 4), (trp_sarranid_n_jebelus10, 2, 4), (trp_sarranid_n_yerliyya10, 2, 4), (trp_sarranid_n_cemaat10, 1, 2)]),

	("kingdom_10_reinforcements_b_r", "{!}kingdom 10 reinforcements b", icon_people_player|pf_label_small, 0, fac_commoners, aggressiveness_0, [(trp_sarranid_n_millet10, 2, 4), (trp_reach_troop_1, 2, 4), (trp_sarranid_n_yeniceri10, 2, 4), (trp_sarranid_n_kapikula10, 2, 4), (trp_sarranid_n_uluteci10, 2, 4), (trp_sarranid_n_millet10, 1, 2)]),

	("kingdom_10_reinforcements_c_r", "{!}kingdom 10 reinforcements c", icon_people_player|pf_label_small, 0, fac_commoners, aggressiveness_0, [(trp_sarranid_n_millet10, 2, 4), (trp_sarranid_n_ajam10, 2, 4), (trp_sarranid_n_cemaat10, 2, 4), (trp_sarranid_n_jebelus10, 2, 4), (trp_sarranid_n_yerliyya10, 2, 4), (trp_sarranid_n_cemaat10, 1, 2)]),

	("kingdom_10_reinforcements_d_r", "{!}kingdom 10 reinforcements d", icon_people_player|pf_label_small, 0, fac_commoners, aggressiveness_0, [(trp_sarranid_n_garip10, 2, 4), (trp_reach_troop_1, 2, 4), (trp_sarranid_n_yeniceri10, 2, 4), (trp_sarranid_n_kapikula10, 2, 4), (trp_sarranid_n_uluteci10, 2, 4), (trp_sarranid_n_millet10, 1, 2)]),

	("kingdom_10_reinforcements_e_r", "{!}kingdom 10 reinforcements e", icon_people_player|pf_label_small, 0, fac_commoners, aggressiveness_0, [(trp_sarranid_n_millet10, 2, 4), (trp_sarranid_n_ajam10, 2, 4), (trp_sarranid_n_cemaat10, 2, 4), (trp_sarranid_n_jebelus10, 2, 4), (trp_sarranid_n_yerliyya10, 2, 4), (trp_sarranid_n_cemaat10, 1, 2)]),

	("kingdom_10_reinforcements_f_r", "{!}kingdom 10 reinforcements f", icon_people_player|pf_label_small, 0, fac_commoners, aggressiveness_0, [(trp_sarranid_n_garip10, 2, 4), (trp_reach_troop_1, 2, 4), (trp_sarranid_n_yeniceri10, 2, 4), (trp_sarranid_n_kapikula10, 2, 4), (trp_sarranid_n_uluteci10, 2, 4), (trp_sarranid_n_millet10, 1, 2)]),

	("kingdom_11_reinforcements_a_r", "{!}kingdom 11 reinforcements a", icon_people_player|pf_label_small, 0, fac_commoners, aggressiveness_0, [(trp_sarranid_n_millet11, 2, 4), (trp_sarranid_n_ajam11, 2, 4), (trp_sarranid_n_cemaat11, 2, 4), (trp_sarranid_n_jebelus11, 2, 4), (trp_sarranid_n_yerliyya11, 2, 4), (trp_sarranid_n_cemaat11, 1, 2)]),

	("kingdom_11_reinforcements_b_r", "{!}kingdom 11 reinforcements b", icon_people_player|pf_label_small, 0, fac_commoners, aggressiveness_0, [(trp_sarranid_n_garip11, 2, 4), (trp_sarranid_n_yeniceri11, 2, 4), (trp_sarranid_n_kapikula11, 2, 4), (trp_sarranid_n_uluteci11, 2, 4), (trp_sarranid_n_uluteci11, 2, 4), (trp_sarranid_n_cemaat11, 1, 2)]),

	("kingdom_11_reinforcements_c_r", "{!}kingdom 11 reinforcements c", icon_people_player|pf_label_small, 0, fac_commoners, aggressiveness_0, [(trp_sarranid_n_millet11, 2, 4), (trp_sarranid_n_ajam11, 2, 4), (trp_sarranid_n_cemaat11, 2, 4), (trp_sarranid_n_jebelus11, 2, 4), (trp_sarranid_n_yerliyya11, 2, 4), (trp_sarranid_n_cemaat11, 1, 2)]),

	("kingdom_11_reinforcements_d_r", "{!}kingdom 11 reinforcements d", icon_people_player|pf_label_small, 0, fac_commoners, aggressiveness_0, [(trp_sarranid_n_garip11, 2, 4), (trp_sarranid_n_yeniceri11, 2, 4), (trp_sarranid_n_kapikula11, 2, 4), (trp_sarranid_n_uluteci11, 2, 4), (trp_sarranid_n_uluteci11, 2, 4), (trp_sarranid_n_cemaat11, 1, 2)]),

	("kingdom_11_reinforcements_e_r", "{!}kingdom 11 reinforcements e", icon_people_player|pf_label_small, 0, fac_commoners, aggressiveness_0, [(trp_sarranid_n_millet11, 2, 4), (trp_sarranid_n_ajam11, 2, 4), (trp_sarranid_n_cemaat11, 2, 4), (trp_sarranid_n_jebelus11, 2, 4), (trp_sarranid_n_yerliyya11, 2, 4), (trp_sarranid_n_cemaat11, 1, 2)]),

	("kingdom_11_reinforcements_f_r", "{!}kingdom 11 reinforcements f", icon_people_player|pf_label_small, 0, fac_commoners, aggressiveness_0, [(trp_sarranid_n_garip11, 2, 4), (trp_sarranid_n_yeniceri11, 2, 4), (trp_sarranid_n_kapikula11, 2, 4), (trp_sarranid_n_uluteci11, 2, 4), (trp_sarranid_n_uluteci11, 2, 4), (trp_sarranid_n_cemaat11, 1, 2)]),

	("kingdom_12_reinforcements_a_r", "{!}kingdom 4 reinforcements a", icon_people_player|pf_label_small, 0, fac_commoners, aggressiveness_0, [(trp_lance_infantry_4, 2, 4), (trp_lance_infantry_3, 2, 4), (trp_lance_infantry_5, 2, 4), (trp_lance_archer_2, 2, 4), (trp_lance_infantry_2, 2, 4), (trp_lance_infantry_1, 2, 4)]),

	("kingdom_12_reinforcements_b_r", "{!}kingdom 4 reinforcements b", icon_people_player|pf_label_small, 0, fac_commoners, aggressiveness_0, [(trp_lance_infantry_4, 2, 4), (trp_lance_infantry_3, 2, 4), (trp_lance_infantry_5, 2, 4), (trp_lance_archer_2, 2, 4), (trp_lance_infantry_2, 2, 4), (trp_lance_infantry_1, 2, 4)]),

	("kingdom_12_reinforcements_c_r", "{!}kingdom 4 reinforcements c", icon_people_player|pf_label_small, 0, fac_commoners, aggressiveness_0, [(trp_lance_infantry_4, 2, 4), (trp_lance_infantry_3, 2, 4), (trp_lance_infantry_5, 2, 4), (trp_lance_archer_2, 2, 4), (trp_lance_infantry_2, 2, 4), (trp_lance_infantry_1, 2, 4)]),

	("kingdom_12_reinforcements_d_r", "{!}kingdom 4 reinforcements d", icon_people_player|pf_label_small, 0, fac_commoners, aggressiveness_0, [(trp_lance_infantry_4, 2, 4), (trp_lance_infantry_3, 2, 4), (trp_lance_infantry_5, 2, 4), (trp_lance_archer_2, 2, 4), (trp_lance_archer_5, 2, 4), (trp_lance_archer_2, 2, 4)]),

	("kingdom_12_reinforcements_e_r", "{!}kingdom 4 reinforcements e", icon_people_player|pf_label_small, 0, fac_commoners, aggressiveness_0, [(trp_lance_infantry_4, 2, 4), (trp_lance_infantry_3, 2, 4), (trp_lance_infantry_5, 2, 4), (trp_lance_archer_2, 2, 4), (trp_lance_archer_5, 2, 4), (trp_lance_archer_2, 2, 4)]),

	("kingdom_12_reinforcements_f_r", "{!}kingdom 4 reinforcements f", icon_people_player|pf_label_small, 0, fac_commoners, aggressiveness_0, [(trp_lance_infantry_4, 2, 4), (trp_lance_infantry_3, 2, 4), (trp_lance_infantry_5, 2, 4), (trp_lance_archer_2, 2, 4), (trp_lance_archer_5, 2, 4), (trp_lance_archer_2, 2, 4)]),

	("kingdom_13_reinforcements_a_r", "{!}kingdom 4 reinforcements a", icon_people_player|pf_label_small, 0, fac_commoners, aggressiveness_0, [(trp_lance_infantry_4, 2, 4), (trp_lance_infantry_3, 2, 4), (trp_lance_infantry_5, 2, 4), (trp_lance_archer_2, 2, 4), (trp_lance_infantry_2, 2, 4), (trp_lance_infantry_1, 2, 4)]),

	("kingdom_13_reinforcements_b_r", "{!}kingdom 4 reinforcements b", icon_people_player|pf_label_small, 0, fac_commoners, aggressiveness_0, [(trp_lance_infantry_4, 2, 4), (trp_lance_infantry_3, 2, 4), (trp_lance_infantry_5, 2, 4), (trp_lance_archer_2, 2, 4), (trp_lance_infantry_2, 2, 4), (trp_lance_infantry_1, 2, 4)]),

	("kingdom_13_reinforcements_c_r", "{!}kingdom 4 reinforcements c", icon_people_player|pf_label_small, 0, fac_commoners, aggressiveness_0, [(trp_lance_infantry_4, 2, 4), (trp_lance_infantry_3, 2, 4), (trp_lance_infantry_5, 2, 4), (trp_lance_archer_2, 2, 4), (trp_lance_infantry_2, 2, 4), (trp_lance_infantry_1, 2, 4)]),

	("kingdom_13_reinforcements_d_r", "{!}kingdom 4 reinforcements d", icon_people_player|pf_label_small, 0, fac_commoners, aggressiveness_0, [(trp_lance_infantry_4, 2, 4), (trp_lance_infantry_3, 2, 4), (trp_lance_infantry_5, 2, 4), (trp_lance_archer_2, 2, 4), (trp_lance_archer_5, 2, 4), (trp_lance_archer_2, 2, 4)]),

	("kingdom_13_reinforcements_e_r", "{!}kingdom 4 reinforcements e", icon_people_player|pf_label_small, 0, fac_commoners, aggressiveness_0, [(trp_lance_infantry_4, 2, 4), (trp_lance_infantry_3, 2, 4), (trp_lance_infantry_5, 2, 4), (trp_lance_archer_2, 2, 4), (trp_lance_archer_5, 2, 4), (trp_lance_archer_2, 2, 4)]),

	("kingdom_13_reinforcements_f_r", "{!}kingdom 4 reinforcements f", icon_people_player|pf_label_small, 0, fac_commoners, aggressiveness_0, [(trp_lance_infantry_4, 2, 4), (trp_lance_infantry_3, 2, 4), (trp_lance_infantry_5, 2, 4), (trp_lance_archer_2, 2, 4), (trp_lance_archer_5, 2, 4), (trp_lance_archer_2, 2, 4)]),

	("kingdom_14_reinforcements_a_r", "{!}kingdom 4 reinforcements a", icon_people_player|pf_label_small, 0, fac_commoners, aggressiveness_0, [(trp_lance_infantry_4, 2, 4), (trp_lance_infantry_3, 2, 4), (trp_lance_infantry_5, 2, 4), (trp_lance_archer_2, 2, 4), (trp_lance_infantry_2, 2, 4), (trp_lance_infantry_1, 2, 4)]),

	("kingdom_14_reinforcements_b_r", "{!}kingdom 4 reinforcements b", icon_people_player|pf_label_small, 0, fac_commoners, aggressiveness_0, [(trp_lance_infantry_4, 2, 4), (trp_lance_infantry_3, 2, 4), (trp_lance_infantry_5, 2, 4), (trp_lance_archer_2, 2, 4), (trp_lance_infantry_2, 2, 4), (trp_lance_infantry_1, 2, 4)]),

	("kingdom_14_reinforcements_c_r", "{!}kingdom 4 reinforcements c", icon_people_player|pf_label_small, 0, fac_commoners, aggressiveness_0, [(trp_lance_infantry_4, 2, 4), (trp_lance_infantry_3, 2, 4), (trp_lance_infantry_5, 2, 4), (trp_lance_archer_2, 2, 4), (trp_lance_infantry_2, 2, 4), (trp_lance_infantry_1, 2, 4)]),

	("kingdom_14_reinforcements_d_r", "{!}kingdom 4 reinforcements d", icon_people_player|pf_label_small, 0, fac_commoners, aggressiveness_0, [(trp_lance_infantry_4, 2, 4), (trp_lance_infantry_3, 2, 4), (trp_lance_infantry_5, 2, 4), (trp_lance_archer_2, 2, 4), (trp_lance_archer_5, 2, 4), (trp_lance_archer_2, 2, 4)]),

	("kingdom_14_reinforcements_e_r", "{!}kingdom 4 reinforcements e", icon_people_player|pf_label_small, 0, fac_commoners, aggressiveness_0, [(trp_lance_infantry_4, 2, 4), (trp_lance_infantry_3, 2, 4), (trp_lance_infantry_5, 2, 4), (trp_lance_archer_2, 2, 4), (trp_lance_archer_5, 2, 4), (trp_lance_archer_2, 2, 4)]),

	("kingdom_14_reinforcements_f_r", "{!}kingdom 4 reinforcements f", icon_people_player|pf_label_small, 0, fac_commoners, aggressiveness_0, [(trp_lance_infantry_4, 2, 4), (trp_lance_infantry_3, 2, 4), (trp_lance_infantry_5, 2, 4), (trp_lance_archer_2, 2, 4), (trp_lance_archer_5, 2, 4), (trp_lance_archer_2, 2, 4)]),

	("kingdom_15_reinforcements_a_r", "{!}kingdom 4 reinforcements a", icon_people_player|pf_label_small, 0, fac_commoners, aggressiveness_0, [(trp_lance_infantry_4, 2, 4), (trp_lance_infantry_3, 2, 4), (trp_lance_infantry_5, 2, 4), (trp_lance_archer_2, 2, 4), (trp_lance_infantry_2, 2, 4), (trp_lance_infantry_1, 2, 4)]),

	("kingdom_15_reinforcements_b_r", "{!}kingdom 4 reinforcements b", icon_people_player|pf_label_small, 0, fac_commoners, aggressiveness_0, [(trp_lance_infantry_4, 2, 4), (trp_lance_infantry_3, 2, 4), (trp_lance_infantry_5, 2, 4), (trp_lance_archer_2, 2, 4), (trp_lance_infantry_2, 2, 4), (trp_lance_infantry_1, 2, 4)]),

	("kingdom_15_reinforcements_c_r", "{!}kingdom 4 reinforcements c", icon_people_player|pf_label_small, 0, fac_commoners, aggressiveness_0, [(trp_lance_infantry_4, 2, 4), (trp_lance_infantry_3, 2, 4), (trp_lance_infantry_5, 2, 4), (trp_lance_archer_2, 2, 4), (trp_lance_infantry_2, 2, 4), (trp_lance_infantry_1, 2, 4)]),

	("kingdom_15_reinforcements_d_r", "{!}kingdom 4 reinforcements d", icon_people_player|pf_label_small, 0, fac_commoners, aggressiveness_0, [(trp_lance_infantry_4, 2, 4), (trp_lance_infantry_3, 2, 4), (trp_lance_infantry_5, 2, 4), (trp_lance_archer_2, 2, 4), (trp_lance_archer_5, 2, 4), (trp_lance_archer_2, 2, 4)]),

	("kingdom_15_reinforcements_e_r", "{!}kingdom 4 reinforcements e", icon_people_player|pf_label_small, 0, fac_commoners, aggressiveness_0, [(trp_lance_infantry_4, 2, 4), (trp_lance_infantry_3, 2, 4), (trp_lance_infantry_5, 2, 4), (trp_lance_archer_2, 2, 4), (trp_lance_archer_5, 2, 4), (trp_lance_archer_2, 2, 4)]),

	("kingdom_15_reinforcements_f_r", "{!}kingdom 4 reinforcements f", icon_people_player|pf_label_small, 0, fac_commoners, aggressiveness_0, [(trp_lance_infantry_4, 2, 4), (trp_lance_infantry_3, 2, 4), (trp_lance_infantry_5, 2, 4), (trp_lance_archer_2, 2, 4), (trp_lance_archer_5, 2, 4), (trp_lance_archer_2, 2, 4)]),

	("kingdom_16_reinforcements_a_r", "{!}kingdom 4 reinforcements a", icon_people_player|pf_label_small, 0, fac_commoners, aggressiveness_0, [(trp_lance_infantry_4, 2, 4), (trp_lance_infantry_3, 2, 4), (trp_lance_infantry_5, 2, 4), (trp_lance_archer_2, 2, 4), (trp_lance_infantry_2, 2, 4), (trp_lance_infantry_1, 2, 4)]),

	("kingdom_16_reinforcements_b_r", "{!}kingdom 4 reinforcements b", icon_people_player|pf_label_small, 0, fac_commoners, aggressiveness_0, [(trp_lance_infantry_4, 2, 4), (trp_lance_infantry_3, 2, 4), (trp_lance_infantry_5, 2, 4), (trp_lance_archer_2, 2, 4), (trp_lance_infantry_2, 2, 4), (trp_lance_infantry_1, 2, 4)]),

	("kingdom_16_reinforcements_c_r", "{!}kingdom 4 reinforcements c", icon_people_player|pf_label_small, 0, fac_commoners, aggressiveness_0, [(trp_lance_infantry_4, 2, 4), (trp_lance_infantry_3, 2, 4), (trp_lance_infantry_5, 2, 4), (trp_lance_archer_2, 2, 4), (trp_lance_infantry_2, 2, 4), (trp_lance_infantry_1, 2, 4)]),

	("kingdom_16_reinforcements_d_r", "{!}kingdom 4 reinforcements d", icon_people_player|pf_label_small, 0, fac_commoners, aggressiveness_0, [(trp_lance_infantry_4, 2, 4), (trp_lance_infantry_3, 2, 4), (trp_lance_infantry_5, 2, 4), (trp_lance_archer_2, 2, 4), (trp_lance_archer_5, 2, 4), (trp_lance_archer_2, 2, 4)]),

	("kingdom_16_reinforcements_e_r", "{!}kingdom 4 reinforcements e", icon_people_player|pf_label_small, 0, fac_commoners, aggressiveness_0, [(trp_lance_infantry_4, 2, 4), (trp_lance_infantry_3, 2, 4), (trp_lance_infantry_5, 2, 4), (trp_lance_archer_2, 2, 4), (trp_lance_archer_5, 2, 4), (trp_lance_archer_2, 2, 4)]),

	("kingdom_16_reinforcements_f_r", "{!}kingdom 4 reinforcements f", icon_people_player|pf_label_small, 0, fac_commoners, aggressiveness_0, [(trp_lance_infantry_4, 2, 4), (trp_lance_infantry_3, 2, 4), (trp_lance_infantry_5, 2, 4), (trp_lance_archer_2, 2, 4), (trp_lance_archer_5, 2, 4), (trp_lance_archer_2, 2, 4)]),

	("kingdom_17_reinforcements_a_r", "{!}kingdom 4 reinforcements a", icon_people_player|pf_label_small, 0, fac_commoners, aggressiveness_0, [(trp_lance_infantry_4, 2, 4), (trp_lance_infantry_3, 2, 4), (trp_lance_infantry_5, 2, 4), (trp_lance_archer_2, 2, 4), (trp_lance_infantry_2, 2, 4), (trp_lance_infantry_1, 2, 4)]),

	("kingdom_17_reinforcements_b_r", "{!}kingdom 4 reinforcements b", icon_people_player|pf_label_small, 0, fac_commoners, aggressiveness_0, [(trp_lance_infantry_4, 2, 4), (trp_lance_infantry_3, 2, 4), (trp_lance_infantry_5, 2, 4), (trp_lance_archer_2, 2, 4), (trp_lance_infantry_2, 2, 4), (trp_lance_infantry_1, 2, 4)]),

	("kingdom_17_reinforcements_c_r", "{!}kingdom 4 reinforcements c", icon_people_player|pf_label_small, 0, fac_commoners, aggressiveness_0, [(trp_lance_infantry_4, 2, 4), (trp_lance_infantry_3, 2, 4), (trp_lance_infantry_5, 2, 4), (trp_lance_archer_2, 2, 4), (trp_lance_infantry_2, 2, 4), (trp_lance_infantry_1, 2, 4)]),

	("kingdom_17_reinforcements_d_r", "{!}kingdom 4 reinforcements d", icon_people_player|pf_label_small, 0, fac_commoners, aggressiveness_0, [(trp_lance_infantry_4, 2, 4), (trp_lance_infantry_3, 2, 4), (trp_lance_infantry_5, 2, 4), (trp_lance_archer_2, 2, 4), (trp_lance_archer_5, 2, 4), (trp_lance_archer_2, 2, 4)]),

	("kingdom_17_reinforcements_e_r", "{!}kingdom 4 reinforcements e", icon_people_player|pf_label_small, 0, fac_commoners, aggressiveness_0, [(trp_lance_infantry_4, 2, 4), (trp_lance_infantry_3, 2, 4), (trp_lance_infantry_5, 2, 4), (trp_lance_archer_2, 2, 4), (trp_lance_archer_5, 2, 4), (trp_lance_archer_2, 2, 4)]),

	("kingdom_17_reinforcements_f_r", "{!}kingdom 4 reinforcements f", icon_people_player|pf_label_small, 0, fac_commoners, aggressiveness_0, [(trp_lance_infantry_4, 2, 4), (trp_lance_infantry_3, 2, 4), (trp_lance_infantry_5, 2, 4), (trp_lance_archer_2, 2, 4), (trp_lance_archer_5, 2, 4), (trp_lance_archer_2, 2, 4)]),

	("kingdom_18_reinforcements_a_r", "{!}kingdom 4 reinforcements a", icon_people_player|pf_label_small, 0, fac_commoners, aggressiveness_0, [(trp_lance_infantry_4, 2, 4), (trp_lance_infantry_3, 2, 4), (trp_lance_infantry_5, 2, 4), (trp_lance_archer_2, 2, 4), (trp_lance_infantry_2, 2, 4), (trp_lance_infantry_1, 2, 4)]),

	("kingdom_18_reinforcements_b_r", "{!}kingdom 4 reinforcements b", icon_people_player|pf_label_small, 0, fac_commoners, aggressiveness_0, [(trp_lance_infantry_4, 2, 4), (trp_lance_infantry_3, 2, 4), (trp_lance_infantry_5, 2, 4), (trp_lance_archer_2, 2, 4), (trp_lance_infantry_2, 2, 4), (trp_lance_infantry_1, 2, 4)]),

	("kingdom_18_reinforcements_c_r", "{!}kingdom 4 reinforcements c", icon_people_player|pf_label_small, 0, fac_commoners, aggressiveness_0, [(trp_lance_infantry_4, 2, 4), (trp_lance_infantry_3, 2, 4), (trp_lance_infantry_5, 2, 4), (trp_lance_archer_2, 2, 4), (trp_lance_infantry_2, 2, 4), (trp_lance_infantry_1, 2, 4)]),

	("kingdom_18_reinforcements_d_r", "{!}kingdom 4 reinforcements d", icon_people_player|pf_label_small, 0, fac_commoners, aggressiveness_0, [(trp_lance_infantry_4, 2, 4), (trp_lance_infantry_3, 2, 4), (trp_lance_infantry_5, 2, 4), (trp_lance_archer_2, 2, 4), (trp_lance_archer_5, 2, 4), (trp_lance_archer_2, 2, 4)]),

	("kingdom_18_reinforcements_e_r", "{!}kingdom 4 reinforcements e", icon_people_player|pf_label_small, 0, fac_commoners, aggressiveness_0, [(trp_lance_infantry_4, 2, 4), (trp_lance_infantry_3, 2, 4), (trp_lance_infantry_5, 2, 4), (trp_lance_archer_2, 2, 4), (trp_lance_archer_5, 2, 4), (trp_lance_archer_2, 2, 4)]),

	("kingdom_18_reinforcements_f_r", "{!}kingdom 4 reinforcements f", icon_people_player|pf_label_small, 0, fac_commoners, aggressiveness_0, [(trp_lance_infantry_4, 2, 4), (trp_lance_infantry_3, 2, 4), (trp_lance_infantry_5, 2, 4), (trp_lance_archer_2, 2, 4), (trp_lance_archer_5, 2, 4), (trp_lance_archer_2, 2, 4)]),

	("kingdom_19_reinforcements_a_r", "{!}kingdom 19 reinforcements a", icon_people_player|pf_label_small, 0, fac_commoners, aggressiveness_0, [(trp_sarranid_n_millet19, 2, 4), (trp_sarranid_n_ajam19, 2, 4), (trp_sarranid_n_cemaat19, 2, 4), (trp_sarranid_n_jebelus19, 2, 4), (trp_sarranid_n_yerliyya19, 2, 4), (trp_sarranid_n_cemaat19, 1, 2)]),

	("kingdom_19_reinforcements_b_r", "{!}kingdom 19 reinforcements b", icon_people_player|pf_label_small, 0, fac_commoners, aggressiveness_0, [(trp_sarranid_n_garip19, 2, 4), (trp_sarranid_n_yeniceri19, 2, 4), (trp_sarranid_n_kapikula19, 2, 4), (trp_sarranid_n_uluteci19, 2, 4), (trp_sarranid_n_cemaat19, 2, 4), (trp_sarranid_n_kapikula19, 1, 2)]),

	("kingdom_19_reinforcements_c_r", "{!}kingdom 19 reinforcements c", icon_people_player|pf_label_small, 0, fac_commoners, aggressiveness_0, [(trp_sarranid_n_millet19, 2, 4), (trp_sarranid_n_ajam19, 2, 4), (trp_sarranid_n_cemaat19, 2, 4), (trp_sarranid_n_jebelus19, 2, 4), (trp_sarranid_n_yerliyya19, 2, 4), (trp_sarranid_n_cemaat19, 1, 2)]),

	("kingdom_19_reinforcements_d_r", "{!}kingdom 19 reinforcements d", icon_people_player|pf_label_small, 0, fac_commoners, aggressiveness_0, [(trp_sarranid_n_garip19, 2, 4), (trp_sarranid_n_yeniceri19, 2, 4), (trp_sarranid_n_kapikula19, 2, 4), (trp_sarranid_n_uluteci19, 2, 4), (trp_sarranid_n_cemaat19, 2, 4), (trp_sarranid_n_kapikula19, 1, 2)]),

	("kingdom_19_reinforcements_e_r", "{!}kingdom 19 reinforcements e", icon_people_player|pf_label_small, 0, fac_commoners, aggressiveness_0, [(trp_sarranid_n_millet19, 2, 4), (trp_sarranid_n_ajam19, 2, 4), (trp_sarranid_n_cemaat19, 2, 4), (trp_sarranid_n_jebelus19, 2, 4), (trp_sarranid_n_yerliyya19, 2, 4), (trp_sarranid_n_cemaat19, 1, 2)]),

	("kingdom_19_reinforcements_f_r", "{!}kingdom 19 reinforcements f", icon_people_player|pf_label_small, 0, fac_commoners, aggressiveness_0, [(trp_sarranid_n_garip19, 2, 4), (trp_sarranid_n_yeniceri19, 2, 4), (trp_sarranid_n_kapikula19, 2, 4), (trp_sarranid_n_uluteci19, 2, 4), (trp_sarranid_n_cemaat19, 2, 4), (trp_sarranid_n_kapikula19, 1, 2)]),

	("kingdom_20_reinforcements_a_r", "{!}kingdom 20 reinforcements a", icon_people_player|pf_label_small, 0, fac_commoners, aggressiveness_0, [(trp_sarranid_n_millet20, 2, 4), (trp_sarranid_n_ajam20, 2, 4), (trp_sarranid_n_cemaat20, 2, 4), (trp_sarranid_n_jebelus20, 2, 4), (trp_sarranid_n_yerliyya20, 2, 4), (trp_sarranid_n_cemaat20, 1, 2)]),

	("kingdom_20_reinforcements_b_r", "{!}kingdom 20 reinforcements b", icon_people_player|pf_label_small, 0, fac_commoners, aggressiveness_0, [(trp_sarranid_n_garip20, 2, 4), (trp_sarranid_n_yeniceri20, 2, 4), (trp_sarranid_n_kapikula20, 2, 4), (trp_sarranid_n_uluteci20, 2, 4), (trp_sarranid_n_cemaat20, 2, 4), (trp_sarranid_n_kapikula20, 1, 2)]),

	("kingdom_20_reinforcements_c_r", "{!}kingdom 20 reinforcements c", icon_people_player|pf_label_small, 0, fac_commoners, aggressiveness_0, [(trp_sarranid_n_millet20, 2, 4), (trp_sarranid_n_ajam20, 2, 4), (trp_sarranid_n_cemaat20, 2, 4), (trp_sarranid_n_jebelus20, 2, 4), (trp_sarranid_n_yerliyya20, 2, 4), (trp_sarranid_n_cemaat20, 1, 2)]),

	("kingdom_20_reinforcements_d_r", "{!}kingdom 20 reinforcements d", icon_people_player|pf_label_small, 0, fac_commoners, aggressiveness_0, [(trp_sarranid_n_garip20, 2, 4), (trp_sarranid_n_yeniceri20, 2, 4), (trp_sarranid_n_kapikula20, 2, 4), (trp_sarranid_n_uluteci20, 2, 4), (trp_sarranid_n_cemaat20, 2, 4), (trp_sarranid_n_kapikula20, 1, 2)]),

	("kingdom_20_reinforcements_e_r", "{!}kingdom 20 reinforcements e", icon_people_player|pf_label_small, 0, fac_commoners, aggressiveness_0, [(trp_sarranid_n_millet20, 2, 4), (trp_sarranid_n_ajam20, 2, 4), (trp_sarranid_n_cemaat20, 2, 4), (trp_sarranid_n_jebelus20, 2, 4), (trp_sarranid_n_yerliyya20, 2, 4), (trp_sarranid_n_cemaat20, 1, 2)]),

	("kingdom_20_reinforcements_f_r", "{!}kingdom 20 reinforcements f", icon_people_player|pf_label_small, 0, fac_commoners, aggressiveness_0, [(trp_sarranid_n_garip20, 2, 4), (trp_sarranid_n_yeniceri20, 2, 4), (trp_sarranid_n_kapikula20, 2, 4), (trp_sarranid_n_uluteci20, 2, 4), (trp_sarranid_n_cemaat20, 2, 4), (trp_sarranid_n_kapikula20, 1, 2)]),

	("kingdom_21_reinforcements_a_r", "{!}kingdom 21 reinforcements a", icon_people_player|pf_label_small, 0, fac_commoners, aggressiveness_0, [(trp_sarranid_n_millet22, 2, 4), (trp_sarranid_n_ajam22, 2, 4), (trp_sarranid_n_cemaat22, 2, 4), (trp_sarranid_n_jebelus22, 2, 4), (trp_sarranid_n_yeniceri22, 2, 4), (trp_sarranid_n_kapikula22, 2, 4)]),

	("kingdom_21_reinforcements_b_r", "{!}kingdom 21 reinforcements b", icon_people_player|pf_label_small, 0, fac_commoners, aggressiveness_0, [(trp_sarranid_n_millet22, 2, 4), (trp_sarranid_n_ajam22, 2, 4), (trp_sarranid_n_cemaat22, 2, 4), (trp_sarranid_n_jebelus22, 2, 4), (trp_sarranid_n_yeniceri22, 2, 4), (trp_sarranid_n_kapikula22, 2, 4)]),

	("kingdom_21_reinforcements_c_r", "{!}kingdom 21 reinforcements c", icon_people_player|pf_label_small, 0, fac_commoners, aggressiveness_0, [(trp_sarranid_n_uluteci22, 2, 4), (trp_sarranid_n_ajam22, 2, 4), (trp_sarranid_n_cemaat22, 2, 4), (trp_sarranid_n_jebelus22, 2, 4), (trp_sarranid_n_yeniceri22, 2, 4), (trp_sarranid_n_kapikula22, 2, 4)]),

	("kingdom_21_reinforcements_d_r", "{!}kingdom 21 reinforcements d", icon_people_player|pf_label_small, 0, fac_commoners, aggressiveness_0, [(trp_sarranid_n_uluteci22, 2, 4), (trp_sarranid_n_ajam22, 2, 4), (trp_sarranid_n_cemaat22, 2, 4), (trp_sarranid_n_jebelus22, 2, 4), (trp_sarranid_n_yeniceri22, 2, 4), (trp_sarranid_n_kapikula22, 2, 4)]),

	("kingdom_21_reinforcements_e_r", "{!}kingdom 21 reinforcements e", icon_people_player|pf_label_small, 0, fac_commoners, aggressiveness_0, [(trp_sarranid_n_uluteci22, 2, 4), (trp_sarranid_n_ajam22, 2, 4), (trp_sarranid_n_cemaat22, 2, 4), (trp_sarranid_n_jebelus22, 2, 4), (trp_sarranid_n_yeniceri22, 2, 4), (trp_sarranid_n_kapikula22, 2, 4)]),

	("kingdom_21_reinforcements_f_r", "{!}kingdom 21 reinforcements f", icon_people_player|pf_label_small, 0, fac_commoners, aggressiveness_0, [(trp_sarranid_n_uluteci22, 2, 4), (trp_sarranid_n_ajam22, 2, 4), (trp_sarranid_n_cemaat22, 2, 4), (trp_sarranid_n_jebelus22, 2, 4), (trp_sarranid_n_yeniceri22, 2, 4), (trp_sarranid_n_kapikula22, 2, 4)]),

	("kingdom_22_reinforcements_a_r", "{!}kingdom 22 reinforcements a", icon_people_player|pf_label_small, 0, fac_commoners, aggressiveness_0, [(trp_sarranid_n_millet23, 2, 4), (trp_sarranid_n_ajam23, 2, 4), (trp_sarranid_n_cemaat23, 2, 4), (trp_sarranid_n_jebelus23, 2, 4), (trp_sarranid_n_yeniceri23, 2, 4), (trp_sarranid_n_yeniceri23, 2, 4)]),

	("kingdom_22_reinforcements_b_r", "{!}kingdom 22 reinforcements b", icon_people_player|pf_label_small, 0, fac_commoners, aggressiveness_0, [(trp_sarranid_n_millet23, 2, 4), (trp_sarranid_n_ajam23, 2, 4), (trp_sarranid_n_cemaat23, 2, 4), (trp_sarranid_n_jebelus23, 2, 4), (trp_sarranid_n_yeniceri23, 2, 4), (trp_sarranid_n_yeniceri23, 2, 4)]),

	("kingdom_22_reinforcements_c_r", "{!}kingdom 22 reinforcements c", icon_people_player|pf_label_small, 0, fac_commoners, aggressiveness_0, [(trp_sarranid_n_millet23, 2, 4), (trp_sarranid_n_ajam23, 2, 4), (trp_sarranid_n_cemaat23, 2, 4), (trp_sarranid_n_jebelus23, 2, 4), (trp_sarranid_n_yeniceri23, 2, 4), (trp_sarranid_n_yeniceri23, 2, 4)]),

	("kingdom_22_reinforcements_d_r", "{!}kingdom 22 reinforcements d", icon_people_player|pf_label_small, 0, fac_commoners, aggressiveness_0, [(trp_sarranid_n_millet23, 2, 4), (trp_sarranid_n_ajam23, 2, 4), (trp_sarranid_n_cemaat23, 2, 4), (trp_sarranid_n_jebelus23, 2, 4), (trp_sarranid_n_yeniceri23, 2, 4), (trp_sarranid_n_yeniceri23, 2, 4)]),

	("kingdom_22_reinforcements_e_r", "{!}kingdom 22 reinforcements e", icon_people_player|pf_label_small, 0, fac_commoners, aggressiveness_0, [(trp_sarranid_n_millet23, 2, 4), (trp_sarranid_n_ajam23, 2, 4), (trp_sarranid_n_cemaat23, 2, 4), (trp_sarranid_n_jebelus23, 2, 4), (trp_sarranid_n_yeniceri23, 2, 4), (trp_sarranid_n_yeniceri23, 2, 4)]),

	("kingdom_22_reinforcements_f_r", "{!}kingdom 22 reinforcements f", icon_people_player|pf_label_small, 0, fac_commoners, aggressiveness_0, [(trp_sarranid_n_millet23, 2, 4), (trp_sarranid_n_ajam23, 2, 4), (trp_sarranid_n_cemaat23, 2, 4), (trp_sarranid_n_jebelus23, 2, 4), (trp_sarranid_n_yeniceri23, 2, 4), (trp_sarranid_n_yeniceri23, 2, 4)]),

	("kingdom_1_reinforcements_a_e", "{!}kingdom 1 reinforcements a", icon_people_player|pf_label_small, 0, fac_commoners, aggressiveness_0, [(trp_sarranid_n_cemaat1, 2, 4), (trp_sarranid_n_ajam1, 2, 4), (trp_sarranid_n_cemaat1, 2, 4), (trp_sarranid_n_jebelus1, 2, 4), (trp_stormlands_halberdier, 2, 4), (trp_sarranid_n_cemaat1, 1, 2)]),

	("kingdom_1_reinforcements_b_e", "{!}kingdom 1 reinforcements b", icon_people_player|pf_label_small, 0, fac_commoners, aggressiveness_0, [(trp_sarranid_n_millet1, 2, 4), (trp_sarranid_n_ajam1, 2, 4), (trp_sarranid_n_cemaat1, 2, 4), (trp_sarranid_n_jebelus1, 2, 4), (trp_stormlands_halberdier, 2, 4), (trp_sarranid_n_cemaat1, 1, 2)]),

	("kingdom_1_reinforcements_c_e", "{!}kingdom 1 reinforcements c", icon_people_player|pf_label_small, 0, fac_commoners, aggressiveness_0, [(trp_sarranid_n_millet1, 2, 4), (trp_sarranid_n_ajam1, 2, 4), (trp_sarranid_n_cemaat1, 2, 4), (trp_sarranid_n_yerliyya1, 2, 4), (trp_sarranid_n_yerliyya1, 2, 4), (trp_sarranid_n_cemaat1, 1, 2)]),

	("kingdom_1_reinforcements_d_e", "{!}kingdom 1 reinforcements d", icon_people_player|pf_label_small, 0, fac_commoners, aggressiveness_0, [(trp_sarranid_n_millet1, 2, 4), (trp_sarranid_n_ajam1, 2, 4), (trp_sarranid_n_yeniceri1, 2, 4), (trp_sarranid_n_kapikula1, 2, 4), (trp_sarranid_n_uluteci1, 2, 4), (trp_sarranid_n_cemaat1, 1, 2)]),

	("kingdom_1_reinforcements_e_e", "{!}kingdom 1 reinforcements e", icon_people_player|pf_label_small, 0, fac_commoners, aggressiveness_0, [(trp_sarranid_n_millet1, 2, 4), (trp_sarranid_n_ajam1, 2, 4), (trp_sarranid_n_cemaat1, 2, 4), (trp_sarranid_n_yerliyya1, 2, 4), (trp_sarranid_n_yerliyya1, 2, 4), (trp_sarranid_n_cemaat1, 1, 2)]),

	("kingdom_1_reinforcements_f_e", "{!}kingdom 1 reinforcements f", icon_people_player|pf_label_small, 0, fac_commoners, aggressiveness_0, [(trp_sarranid_n_garip1, 2, 4), (trp_stormlands_troop_1, 2, 4), (trp_sarranid_n_yeniceri1, 2, 4), (trp_sarranid_n_kapikula1, 2, 4), (trp_sarranid_n_uluteci1, 2, 4), (trp_sarranid_n_cemaat1, 1, 2)]),

	("kingdom_2_reinforcements_a_e", "{!}kingdom 2 reinforcements a", icon_people_player|pf_label_small, 0, fac_commoners, aggressiveness_0, [(trp_sarranid_n_millet2, 2, 4), (trp_sarranid_n_ajam2, 2, 4), (trp_sarranid_n_cemaat2, 2, 4), (trp_sarranid_n_jebelus2, 2, 4), (trp_northern_spearman, 2, 4), (trp_sarranid_n_cemaat2, 1, 2)]),

	("kingdom_2_reinforcements_b_e", "{!}kingdom 2 reinforcements b", icon_people_player|pf_label_small, 0, fac_commoners, aggressiveness_0, [(trp_sarranid_n_millet2, 2, 4), (trp_sarranid_n_ajam2, 2, 4), (trp_sarranid_n_cemaat2, 2, 4), (trp_sarranid_n_jebelus2, 2, 4), (trp_northern_spearman, 2, 4), (trp_sarranid_n_cemaat2, 1, 2)]),

	("kingdom_2_reinforcements_c_e", "{!}kingdom 2 reinforcements c", icon_people_player|pf_label_small, 0, fac_commoners, aggressiveness_0, [(trp_sarranid_n_millet2, 2, 4), (trp_sarranid_n_ajam2, 2, 4), (trp_sarranid_n_cemaat2, 2, 4), (trp_sarranid_n_yerliyya2, 2, 4), (trp_sarranid_n_yerliyya2, 2, 4), (trp_sarranid_n_cemaat2, 1, 2)]),

	("kingdom_2_reinforcements_d_e", "{!}kingdom 2 reinforcements d", icon_people_player|pf_label_small, 0, fac_commoners, aggressiveness_0, [(trp_sarranid_n_garip2, 2, 4), (trp_sarranid_n_ajam2, 2, 4), (trp_sarranid_n_yeniceri2, 2, 4), (trp_sarranid_n_kapikula2, 2, 4), (trp_sarranid_n_uluteci2, 2, 4), (trp_sarranid_n_cemaat2, 1, 2)]),

	("kingdom_2_reinforcements_e_e", "{!}kingdom 2 reinforcements e", icon_people_player|pf_label_small, 0, fac_commoners, aggressiveness_0, [(trp_sarranid_n_millet2, 2, 4), (trp_sarranid_n_ajam2, 2, 4), (trp_sarranid_n_cemaat2, 2, 4), (trp_sarranid_n_yerliyya2, 2, 4), (trp_sarranid_n_yerliyya2, 2, 4), (trp_sarranid_n_cemaat2, 1, 2)]),

	("kingdom_2_reinforcements_f_e", "{!}kingdom 2 reinforcements f", icon_people_player|pf_label_small, 0, fac_commoners, aggressiveness_0, [(trp_sarranid_n_garip2, 2, 4), (trp_northern_troop_1, 2, 4), (trp_sarranid_n_yeniceri2, 2, 4), (trp_sarranid_n_kapikula2, 2, 4), (trp_sarranid_n_uluteci2, 2, 4), (trp_sarranid_n_cemaat2, 1, 2)]),

	("kingdom_3_reinforcements_a_e", "{!}kingdom 3 reinforcements a", icon_people_player|pf_label_small, 0, fac_commoners, aggressiveness_0, [(trp_sarranid_n_millet3, 2, 4), (trp_sarranid_n_ajam3, 2, 4), (trp_sarranid_n_cemaat3, 2, 4), (trp_sarranid_n_jebelus3, 2, 4), (trp_sarranid_n_yerliyya3, 2, 4), (trp_sarranid_n_cemaat3, 1, 2)]),

	("kingdom_3_reinforcements_b_e", "{!}kingdom 3 reinforcements b", icon_people_player|pf_label_small, 0, fac_commoners, aggressiveness_0, [(trp_sarranid_n_millet3, 2, 4), (trp_sarranid_n_ajam3, 2, 4), (trp_sarranid_n_cemaat3, 2, 4), (trp_sarranid_n_jebelus3, 2, 4), (trp_sarranid_n_yerliyya3, 2, 4), (trp_sarranid_n_cemaat3, 1, 2)]),

	("kingdom_3_reinforcements_c_e", "{!}kingdom 3 reinforcements c", icon_people_player|pf_label_small, 0, fac_commoners, aggressiveness_0, [(trp_sarranid_n_millet3, 2, 4), (trp_sarranid_n_ajam3, 2, 4), (trp_sarranid_n_cemaat3, 2, 4), (trp_sarranid_n_yerliyya3, 2, 4), (trp_sarranid_n_yerliyya3, 2, 4), (trp_sarranid_n_cemaat3, 1, 2)]),

	("kingdom_3_reinforcements_d_e", "{!}kingdom 3 reinforcements d", icon_people_player|pf_label_small, 0, fac_commoners, aggressiveness_0, [(trp_sarranid_n_garip3, 2, 4), (trp_sarranid_n_ajam3, 2, 4), (trp_sarranid_n_yeniceri3, 2, 4), (trp_sarranid_n_kapikula3, 2, 4), (trp_sarranid_n_uluteci3, 2, 4), (trp_sarranid_n_cemaat3, 1, 2)]),

	("kingdom_3_reinforcements_e_e", "{!}kingdom 3 reinforcements e", icon_people_player|pf_label_small, 0, fac_commoners, aggressiveness_0, [(trp_sarranid_n_millet3, 2, 4), (trp_sarranid_n_ajam3, 2, 4), (trp_sarranid_n_cemaat3, 2, 4), (trp_sarranid_n_yerliyya3, 2, 4), (trp_sarranid_n_yerliyya3, 2, 4), (trp_sarranid_n_cemaat3, 1, 2)]),

	("kingdom_3_reinforcements_f_e", "{!}kingdom 3 reinforcements f", icon_people_player|pf_label_small, 0, fac_commoners, aggressiveness_0, [(trp_sarranid_n_garip3, 2, 4), (trp_vale_troop_1, 2, 4), (trp_sarranid_n_yeniceri3, 2, 4), (trp_sarranid_n_kapikula3, 2, 4), (trp_sarranid_n_uluteci3, 2, 4), (trp_sarranid_n_cemaat3, 1, 2)]),

	("kingdom_4_reinforcements_a_e", "{!}kingdom 4 reinforcements a", icon_people_player|pf_label_small, 0, fac_commoners, aggressiveness_0, [(trp_lance_infantry_4, 2, 4), (trp_lance_infantry_3, 2, 4), (trp_lance_infantry_5, 2, 4), (trp_lance_archer_2, 2, 4), (trp_lance_infantry_2, 2, 4), (trp_lance_infantry_1, 2, 4)]),

	("kingdom_4_reinforcements_b_e", "{!}kingdom 4 reinforcements b", icon_people_player|pf_label_small, 0, fac_commoners, aggressiveness_0, [(trp_lance_infantry_4, 2, 4), (trp_lance_infantry_3, 2, 4), (trp_lance_infantry_5, 2, 4), (trp_lance_archer_2, 2, 4), (trp_lance_infantry_2, 2, 4), (trp_lance_infantry_1, 2, 4)]),

	("kingdom_4_reinforcements_c_e", "{!}kingdom 4 reinforcements c", icon_people_player|pf_label_small, 0, fac_commoners, aggressiveness_0, [(trp_lance_infantry_4, 2, 4), (trp_lance_infantry_3, 2, 4), (trp_lance_infantry_5, 2, 4), (trp_lance_archer_2, 2, 4), (trp_lance_infantry_2, 2, 4), (trp_lance_infantry_1, 2, 4)]),

	("kingdom_4_reinforcements_d_e", "{!}kingdom 4 reinforcements d", icon_people_player|pf_label_small, 0, fac_commoners, aggressiveness_0, [(trp_lance_infantry_4, 2, 4), (trp_lance_infantry_3, 2, 4), (trp_lance_infantry_5, 2, 4), (trp_lance_archer_2, 2, 4), (trp_lance_archer_5, 2, 4), (trp_lance_archer_2, 2, 4)]),

	("kingdom_4_reinforcements_e_e", "{!}kingdom 4 reinforcements e", icon_people_player|pf_label_small, 0, fac_commoners, aggressiveness_0, [(trp_lance_infantry_4, 2, 4), (trp_lance_infantry_3, 2, 4), (trp_lance_infantry_5, 2, 4), (trp_lance_archer_2, 2, 4), (trp_lance_archer_5, 2, 4), (trp_lance_archer_2, 2, 4)]),

	("kingdom_4_reinforcements_f_e", "{!}kingdom 4 reinforcements f", icon_people_player|pf_label_small, 0, fac_commoners, aggressiveness_0, [(trp_lance_infantry_4, 2, 4), (trp_lance_infantry_3, 2, 4), (trp_lance_infantry_5, 2, 4), (trp_lance_archer_2, 2, 4), (trp_lance_archer_5, 2, 4), (trp_lance_archer_2, 2, 4)]),

	("kingdom_5_reinforcements_a_e", "{!}kingdom 5 reinforcements a", icon_people_player|pf_label_small, 0, fac_commoners, aggressiveness_0, [(trp_lance_infantry_4, 2, 4), (trp_lance_infantry_3, 2, 4), (trp_lance_infantry_5, 2, 4), (trp_lance_archer_2, 2, 4), (trp_lance_infantry_2, 2, 4), (trp_lance_infantry_1, 2, 4)]),

	("kingdom_5_reinforcements_b_e", "{!}kingdom 5 reinforcements b", icon_people_player|pf_label_small, 0, fac_commoners, aggressiveness_0, [(trp_lance_infantry_4, 2, 4), (trp_lance_infantry_3, 2, 4), (trp_lance_infantry_5, 2, 4), (trp_lance_archer_2, 2, 4), (trp_lance_infantry_2, 2, 4), (trp_lance_infantry_1, 2, 4)]),

	("kingdom_5_reinforcements_c_e", "{!}kingdom 5 reinforcements c", icon_people_player|pf_label_small, 0, fac_commoners, aggressiveness_0, [(trp_lance_infantry_4, 2, 4), (trp_lance_infantry_3, 2, 4), (trp_lance_infantry_5, 2, 4), (trp_lance_archer_2, 2, 4), (trp_lance_infantry_2, 2, 4), (trp_lance_infantry_1, 2, 4)]),

	("kingdom_5_reinforcements_d_e", "{!}kingdom 5 reinforcements d", icon_people_player|pf_label_small, 0, fac_commoners, aggressiveness_0, [(trp_lance_infantry_4, 2, 4), (trp_lance_infantry_3, 2, 4), (trp_lance_infantry_5, 2, 4), (trp_lance_archer_2, 2, 4), (trp_lance_archer_5, 2, 4), (trp_lance_archer_2, 2, 4)]),

	("kingdom_5_reinforcements_e_e", "{!}kingdom 5 reinforcements e", icon_people_player|pf_label_small, 0, fac_commoners, aggressiveness_0, [(trp_lance_infantry_4, 2, 4), (trp_lance_infantry_3, 2, 4), (trp_lance_infantry_5, 2, 4), (trp_lance_archer_2, 2, 4), (trp_lance_archer_5, 2, 4), (trp_lance_archer_2, 2, 4)]),

	("kingdom_5_reinforcements_f_e", "{!}kingdom 5 reinforcements f", icon_people_player|pf_label_small, 0, fac_commoners, aggressiveness_0, [(trp_lance_infantry_4, 2, 4), (trp_lance_infantry_3, 2, 4), (trp_lance_infantry_5, 2, 4), (trp_lance_archer_2, 2, 4), (trp_lance_archer_5, 2, 4), (trp_lance_archer_2, 2, 4)]),

	("kingdom_6_reinforcements_a_e", "{!}kingdom 6 reinforcements a", icon_people_player|pf_label_small, 0, fac_commoners, aggressiveness_0, [(trp_sarranid_n_millet, 2, 4), (trp_sarranid_n_ajam, 2, 4), (trp_sarranid_n_cemaat, 2, 4), (trp_sarranid_n_jebelus, 2, 4), (trp_sarranid_n_yerliyya, 2, 4), (trp_sarranid_n_cemaat, 1, 2)]),

	("kingdom_6_reinforcements_b_e", "{!}kingdom 6 reinforcements b", icon_people_player|pf_label_small, 0, fac_commoners, aggressiveness_0, [(trp_sarranid_n_millet, 2, 4), (trp_sarranid_n_ajam, 2, 4), (trp_sarranid_n_cemaat, 2, 4), (trp_sarranid_n_jebelus, 2, 4), (trp_sarranid_n_yerliyya, 2, 4), (trp_sarranid_n_cemaat, 1, 2)]),

	("kingdom_6_reinforcements_c_e", "{!}kingdom 6 reinforcements c", icon_people_player|pf_label_small, 0, fac_commoners, aggressiveness_0, [(trp_sarranid_n_millet, 2, 4), (trp_sarranid_n_ajam, 2, 4), (trp_sarranid_n_cemaat, 2, 4), (trp_sarranid_n_yerliyya, 2, 4), (trp_sarranid_n_yerliyya, 2, 4), (trp_sarranid_n_cemaat, 1, 2)]),

	("kingdom_6_reinforcements_d_e", "{!}kingdom 6 reinforcements d", icon_people_player|pf_label_small, 0, fac_commoners, aggressiveness_0, [(trp_sarranid_n_garip, 2, 4), (trp_sarranid_n_ajam, 2, 4), (trp_sarranid_n_yeniceri, 2, 4), (trp_sarranid_n_kapikula, 2, 4), (trp_sarranid_n_uluteci, 2, 4), (trp_sarranid_n_cemaat, 1, 2)]),

	("kingdom_6_reinforcements_e_e", "{!}kingdom 6 reinforcements e", icon_people_player|pf_label_small, 0, fac_commoners, aggressiveness_0, [(trp_sarranid_n_millet, 2, 4), (trp_sarranid_n_ajam, 2, 4), (trp_sarranid_n_cemaat, 2, 4), (trp_sarranid_n_yerliyya, 2, 4), (trp_sarranid_n_yerliyya, 2, 4), (trp_sarranid_n_cemaat, 1, 2)]),

	("kingdom_6_reinforcements_f_e", "{!}kingdom 6 reinforcements f", icon_people_player|pf_label_small, 0, fac_commoners, aggressiveness_0, [(trp_sarranid_n_garip, 2, 4), (trp_dorne_troop_1, 2, 4), (trp_sarranid_n_yeniceri, 2, 4), (trp_sarranid_n_kapikula, 2, 4), (trp_sarranid_n_uluteci, 2, 4), (trp_sarranid_n_cemaat, 1, 2)]),

	("kingdom_7_reinforcements_a_e", "{!}kingdom 7 reinforcements a", icon_people_player|pf_label_small, 0, fac_commoners, aggressiveness_0, [(trp_sarranid_n_millet21, 2, 4), (trp_sarranid_n_ajam21, 2, 4), (trp_sarranid_n_cemaat21, 2, 4), (trp_sarranid_n_jebelus21, 2, 4), (trp_sarranid_n_yerliyya21, 2, 4), (trp_sarranid_n_cemaat21, 1, 2)]),

	("kingdom_7_reinforcements_b_e", "{!}kingdom 7 reinforcements b", icon_people_player|pf_label_small, 0, fac_commoners, aggressiveness_0, [(trp_sarranid_n_millet21, 2, 4), (trp_sarranid_n_ajam21, 2, 4), (trp_sarranid_n_cemaat21, 2, 4), (trp_sarranid_n_jebelus21, 2, 4), (trp_sarranid_n_yerliyya21, 2, 4), (trp_sarranid_n_cemaat21, 1, 2)]),

	("kingdom_7_reinforcements_c_e", "{!}kingdom 7 reinforcements c", icon_people_player|pf_label_small, 0, fac_commoners, aggressiveness_0, [(trp_sarranid_n_millet21, 2, 4), (trp_sarranid_n_ajam21, 2, 4), (trp_sarranid_n_cemaat21, 2, 4), (trp_sarranid_n_jebelus21, 2, 4), (trp_sarranid_n_yerliyya21, 2, 4), (trp_sarranid_n_cemaat21, 1, 2)]),

	("kingdom_7_reinforcements_d_e", "{!}kingdom 7 reinforcements d", icon_people_player|pf_label_small, 0, fac_commoners, aggressiveness_0, [(trp_sarranid_n_garip21, 2, 4), (trp_sarranid_n_yeniceri21, 2, 4), (trp_sarranid_n_kapikula21, 2, 4), (trp_sarranid_n_uluteci21, 2, 4), (trp_sarranid_n_cemaat21, 2, 4), (trp_sarranid_n_yerliyya21, 1, 2)]),

	("kingdom_7_reinforcements_e_e", "{!}kingdom 7 reinforcements e", icon_people_player|pf_label_small, 0, fac_commoners, aggressiveness_0, [(trp_sarranid_n_millet21, 2, 4), (trp_sarranid_n_ajam21, 2, 4), (trp_sarranid_n_cemaat21, 2, 4), (trp_sarranid_n_jebelus21, 2, 4), (trp_sarranid_n_yerliyya21, 2, 4), (trp_sarranid_n_cemaat21, 1, 2)]),

	("kingdom_7_reinforcements_f_e", "{!}kingdom 7 reinforcements f", icon_people_player|pf_label_small, 0, fac_commoners, aggressiveness_0, [(trp_sarranid_n_garip21, 2, 4), (trp_sarranid_n_yeniceri21, 2, 4), (trp_sarranid_n_kapikula21, 2, 4), (trp_sarranid_n_uluteci21, 2, 4), (trp_sarranid_n_cemaat21, 2, 4), (trp_sarranid_n_yerliyya21, 1, 2)]),

	("kingdom_8_reinforcements_a_e", "{!}kingdom 8 reinforcements a", icon_people_player|pf_label_small, 0, fac_commoners, aggressiveness_0, [(trp_sarranid_n_millet8, 2, 4), (trp_sarranid_n_ajam8, 2, 4), (trp_sarranid_n_cemaat8, 2, 4), (trp_sarranid_n_jebelus8, 2, 4), (trp_sarranid_n_yerliyya8, 2, 4), (trp_sarranid_n_cemaat8, 1, 2)]),

	("kingdom_8_reinforcements_b_e", "{!}kingdom 8 reinforcements b", icon_people_player|pf_label_small, 0, fac_commoners, aggressiveness_0, [(trp_sarranid_n_millet8, 2, 4), (trp_sarranid_n_ajam8, 2, 4), (trp_sarranid_n_cemaat8, 2, 4), (trp_sarranid_n_jebelus8, 2, 4), (trp_sarranid_n_yerliyya8, 2, 4), (trp_sarranid_n_cemaat8, 1, 2)]),

	("kingdom_8_reinforcements_c_e", "{!}kingdom 8 reinforcements c", icon_people_player|pf_label_small, 0, fac_commoners, aggressiveness_0, [(trp_sarranid_n_millet8, 2, 4), (trp_sarranid_n_ajam8, 2, 4), (trp_sarranid_n_cemaat8, 2, 4), (trp_sarranid_n_yerliyya8, 2, 4), (trp_sarranid_n_yerliyya8, 2, 4), (trp_sarranid_n_cemaat8, 1, 2)]),

	("kingdom_8_reinforcements_d_e", "{!}kingdom 8 reinforcements d", icon_people_player|pf_label_small, 0, fac_commoners, aggressiveness_0, [(trp_sarranid_n_garip8, 2, 4), (trp_sarranid_n_ajam8, 2, 4), (trp_sarranid_n_yeniceri8, 2, 4), (trp_sarranid_n_kapikula8, 2, 4), (trp_sarranid_n_uluteci8, 2, 4), (trp_sarranid_n_cemaat8, 1, 2)]),

	("kingdom_8_reinforcements_e_e", "{!}kingdom 8 reinforcements e", icon_people_player|pf_label_small, 0, fac_commoners, aggressiveness_0, [(trp_sarranid_n_millet8, 2, 4), (trp_sarranid_n_ajam8, 2, 4), (trp_sarranid_n_cemaat8, 2, 4), (trp_sarranid_n_yerliyya8, 2, 4), (trp_sarranid_n_yerliyya8, 2, 4), (trp_sarranid_n_cemaat8, 1, 2)]),

	("kingdom_8_reinforcements_f_e", "{!}kingdom 8 reinforcements f", icon_people_player|pf_label_small, 0, fac_commoners, aggressiveness_0, [(trp_sarranid_n_garip8, 2, 4), (trp_dragonstone_troop_1, 2, 4), (trp_sarranid_n_yeniceri8, 2, 4), (trp_sarranid_n_kapikula8, 2, 4), (trp_sarranid_n_uluteci8, 2, 4), (trp_sarranid_n_cemaat8, 1, 2)]),

	("kingdom_9_reinforcements_a_e", "{!}kingdom 9 reinforcements a", icon_people_player|pf_label_small, 0, fac_commoners, aggressiveness_0, [(trp_sarranid_n_cemaat9, 2, 4), (trp_sarranid_n_ajam9, 2, 4), (trp_sarranid_n_cemaat9, 2, 4), (trp_sarranid_n_jebelus9, 2, 4), (trp_sarranid_n_yerliyya9, 2, 4), (trp_sarranid_n_cemaat9, 1, 2)]),

	("kingdom_9_reinforcements_b_e", "{!}kingdom 9 reinforcements b", icon_people_player|pf_label_small, 0, fac_commoners, aggressiveness_0, [(trp_sarranid_n_millet9, 2, 4), (trp_sarranid_n_ajam9, 2, 4), (trp_sarranid_n_cemaat9, 2, 4), (trp_sarranid_n_jebelus9, 2, 4), (trp_sarranid_n_yerliyya9, 2, 4), (trp_sarranid_n_cemaat9, 1, 2)]),

	("kingdom_9_reinforcements_c_e", "{!}kingdom 9 reinforcements c", icon_people_player|pf_label_small, 0, fac_commoners, aggressiveness_0, [(trp_sarranid_n_millet9, 2, 4), (trp_sarranid_n_ajam9, 2, 4), (trp_sarranid_n_cemaat9, 2, 4), (trp_sarranid_n_yerliyya9, 2, 4), (trp_sarranid_n_yerliyya9, 2, 4), (trp_sarranid_n_cemaat9, 1, 2)]),

	("kingdom_9_reinforcements_d_e", "{!}kingdom 9 reinforcements d", icon_people_player|pf_label_small, 0, fac_commoners, aggressiveness_0, [(trp_sarranid_n_millet9, 2, 4), (trp_sarranid_n_ajam9, 2, 4), (trp_sarranid_n_yeniceri9, 2, 4), (trp_sarranid_n_kapikula9, 2, 4), (trp_sarranid_n_uluteci9, 2, 4), (trp_sarranid_n_cemaat9, 1, 2)]),

	("kingdom_9_reinforcements_e_e", "{!}kingdom 9 reinforcements e", icon_people_player|pf_label_small, 0, fac_commoners, aggressiveness_0, [(trp_sarranid_n_millet9, 2, 4), (trp_sarranid_n_ajam9, 2, 4), (trp_sarranid_n_cemaat9, 2, 4), (trp_sarranid_n_yerliyya9, 2, 4), (trp_sarranid_n_yerliyya9, 2, 4), (trp_sarranid_n_cemaat9, 1, 2)]),

	("kingdom_9_reinforcements_f_e", "{!}kingdom 9 reinforcements f", icon_people_player|pf_label_small, 0, fac_commoners, aggressiveness_0, [(trp_sarranid_n_garip9, 2, 4), (trp_westerlands_troop_1, 2, 4), (trp_sarranid_n_yeniceri9, 2, 4), (trp_sarranid_n_kapikula9, 2, 4), (trp_sarranid_n_uluteci9, 2, 4), (trp_sarranid_n_cemaat9, 1, 2)]),

	("kingdom_10_reinforcements_a_e", "{!}kingdom 10 reinforcements a", icon_people_player|pf_label_small, 0, fac_commoners, aggressiveness_0, [(trp_sarranid_n_cemaat10, 2, 4), (trp_sarranid_n_ajam10, 2, 4), (trp_sarranid_n_cemaat10, 2, 4), (trp_sarranid_n_jebelus10, 2, 4), (trp_sarranid_n_yerliyya10, 2, 4), (trp_reach_squire, 1, 2)]),

	("kingdom_10_reinforcements_b_e", "{!}kingdom 10 reinforcements b", icon_people_player|pf_label_small, 0, fac_commoners, aggressiveness_0, [(trp_reach_squire, 2, 4), (trp_sarranid_n_ajam10, 2, 4), (trp_sarranid_n_cemaat10, 2, 4), (trp_sarranid_n_jebelus10, 2, 4), (trp_sarranid_n_yerliyya10, 2, 4), (trp_sarranid_n_cemaat10, 1, 2)]),

	("kingdom_10_reinforcements_c_e", "{!}kingdom 10 reinforcements c", icon_people_player|pf_label_small, 0, fac_commoners, aggressiveness_0, [(trp_sarranid_n_millet10, 2, 4), (trp_sarranid_n_ajam10, 2, 4), (trp_sarranid_n_cemaat10, 2, 4), (trp_sarranid_n_yerliyya10, 2, 4), (trp_sarranid_n_yerliyya10, 2, 4), (trp_sarranid_n_cemaat10, 1, 2)]),

	("kingdom_10_reinforcements_d_e", "{!}kingdom 10 reinforcements d", icon_people_player|pf_label_small, 0, fac_commoners, aggressiveness_0, [(trp_sarranid_n_millet10, 2, 4), (trp_sarranid_n_ajam10, 2, 4), (trp_sarranid_n_yeniceri10, 2, 4), (trp_sarranid_n_kapikula10, 2, 4), (trp_sarranid_n_uluteci10, 2, 4), (trp_sarranid_n_millet10, 1, 2)]),

	("kingdom_10_reinforcements_e_e", "{!}kingdom 10 reinforcements e", icon_people_player|pf_label_small, 0, fac_commoners, aggressiveness_0, [(trp_sarranid_n_millet10, 2, 4), (trp_sarranid_n_ajam10, 2, 4), (trp_sarranid_n_cemaat10, 2, 4), (trp_sarranid_n_yerliyya10, 2, 4), (trp_sarranid_n_yerliyya10, 2, 4), (trp_sarranid_n_cemaat10, 1, 2)]),

	("kingdom_10_reinforcements_f_e", "{!}kingdom 10 reinforcements f", icon_people_player|pf_label_small, 0, fac_commoners, aggressiveness_0, [(trp_sarranid_n_garip10, 2, 4), (trp_reach_troop_1, 2, 4), (trp_sarranid_n_yeniceri10, 2, 4), (trp_sarranid_n_kapikula10, 2, 4), (trp_sarranid_n_uluteci10, 2, 4), (trp_sarranid_n_millet10, 1, 2)]),

	("kingdom_11_reinforcements_a_e", "{!}kingdom 11 reinforcements a", icon_people_player|pf_label_small, 0, fac_commoners, aggressiveness_0, [(trp_sarranid_n_millet11, 2, 4), (trp_sarranid_n_ajam11, 2, 4), (trp_sarranid_n_cemaat11, 2, 4), (trp_sarranid_n_jebelus11, 2, 4), (trp_sarranid_n_yerliyya11, 2, 4), (trp_sarranid_n_cemaat11, 1, 2)]),

	("kingdom_11_reinforcements_b_e", "{!}kingdom 11 reinforcements b", icon_people_player|pf_label_small, 0, fac_commoners, aggressiveness_0, [(trp_sarranid_n_millet11, 2, 4), (trp_sarranid_n_ajam11, 2, 4), (trp_sarranid_n_cemaat11, 2, 4), (trp_sarranid_n_jebelus11, 2, 4), (trp_sarranid_n_yerliyya11, 2, 4), (trp_sarranid_n_cemaat11, 1, 2)]),

	("kingdom_11_reinforcements_c_e", "{!}kingdom 11 reinforcements c", icon_people_player|pf_label_small, 0, fac_commoners, aggressiveness_0, [(trp_sarranid_n_millet11, 2, 4), (trp_sarranid_n_ajam11, 2, 4), (trp_sarranid_n_cemaat11, 2, 4), (trp_sarranid_n_yerliyya11, 2, 4), (trp_sarranid_n_yerliyya11, 2, 4), (trp_sarranid_n_cemaat11, 1, 2)]),

	("kingdom_11_reinforcements_d_e", "{!}kingdom 11 reinforcements d", icon_people_player|pf_label_small, 0, fac_commoners, aggressiveness_0, [(trp_sarranid_n_ajam11, 2, 4), (trp_sarranid_n_yeniceri11, 2, 4), (trp_sarranid_n_kapikula11, 2, 4), (trp_sarranid_n_uluteci11, 2, 4), (trp_sarranid_n_uluteci11, 2, 4), (trp_sarranid_n_cemaat11, 1, 2)]),

	("kingdom_11_reinforcements_e_e", "{!}kingdom 11 reinforcements e", icon_people_player|pf_label_small, 0, fac_commoners, aggressiveness_0, [(trp_sarranid_n_millet11, 2, 4), (trp_sarranid_n_ajam11, 2, 4), (trp_sarranid_n_cemaat11, 2, 4), (trp_sarranid_n_yerliyya11, 2, 4), (trp_sarranid_n_yerliyya11, 2, 4), (trp_sarranid_n_cemaat11, 1, 2)]),

	("kingdom_11_reinforcements_f_e", "{!}kingdom 11 reinforcements f", icon_people_player|pf_label_small, 0, fac_commoners, aggressiveness_0, [(trp_sarranid_n_ajam11, 2, 4), (trp_sarranid_n_yeniceri11, 2, 4), (trp_sarranid_n_kapikula11, 2, 4), (trp_sarranid_n_uluteci11, 2, 4), (trp_sarranid_n_uluteci11, 2, 4), (trp_sarranid_n_cemaat11, 1, 2)]),

	("kingdom_12_reinforcements_a_e", "{!}kingdom 4 reinforcements a", icon_people_player|pf_label_small, 0, fac_commoners, aggressiveness_0, [(trp_lance_infantry_4, 2, 4), (trp_lance_infantry_3, 2, 4), (trp_lance_infantry_5, 2, 4), (trp_lance_archer_2, 2, 4), (trp_lance_infantry_2, 2, 4), (trp_lance_infantry_1, 2, 4)]),

	("kingdom_12_reinforcements_b_e", "{!}kingdom 4 reinforcements b", icon_people_player|pf_label_small, 0, fac_commoners, aggressiveness_0, [(trp_lance_infantry_4, 2, 4), (trp_lance_infantry_3, 2, 4), (trp_lance_infantry_5, 2, 4), (trp_lance_archer_2, 2, 4), (trp_lance_infantry_2, 2, 4), (trp_lance_infantry_1, 2, 4)]),

	("kingdom_12_reinforcements_c_e", "{!}kingdom 4 reinforcements c", icon_people_player|pf_label_small, 0, fac_commoners, aggressiveness_0, [(trp_lance_infantry_4, 2, 4), (trp_lance_infantry_3, 2, 4), (trp_lance_infantry_5, 2, 4), (trp_lance_archer_2, 2, 4), (trp_lance_infantry_2, 2, 4), (trp_lance_infantry_1, 2, 4)]),

	("kingdom_12_reinforcements_d_e", "{!}kingdom 4 reinforcements d", icon_people_player|pf_label_small, 0, fac_commoners, aggressiveness_0, [(trp_lance_infantry_4, 2, 4), (trp_lance_infantry_3, 2, 4), (trp_lance_infantry_5, 2, 4), (trp_lance_archer_2, 2, 4), (trp_lance_archer_5, 2, 4), (trp_lance_archer_2, 2, 4)]),

	("kingdom_12_reinforcements_e_e", "{!}kingdom 4 reinforcements e", icon_people_player|pf_label_small, 0, fac_commoners, aggressiveness_0, [(trp_lance_infantry_4, 2, 4), (trp_lance_infantry_3, 2, 4), (trp_lance_infantry_5, 2, 4), (trp_lance_archer_2, 2, 4), (trp_lance_archer_5, 2, 4), (trp_lance_archer_2, 2, 4)]),

	("kingdom_12_reinforcements_f_e", "{!}kingdom 4 reinforcements f", icon_people_player|pf_label_small, 0, fac_commoners, aggressiveness_0, [(trp_lance_infantry_4, 2, 4), (trp_lance_infantry_3, 2, 4), (trp_lance_infantry_5, 2, 4), (trp_lance_archer_2, 2, 4), (trp_lance_archer_5, 2, 4), (trp_lance_archer_2, 2, 4)]),

	("kingdom_13_reinforcements_a_e", "{!}kingdom 4 reinforcements a", icon_people_player|pf_label_small, 0, fac_commoners, aggressiveness_0, [(trp_lance_infantry_4, 2, 4), (trp_lance_infantry_3, 2, 4), (trp_lance_infantry_5, 2, 4), (trp_lance_archer_2, 2, 4), (trp_lance_infantry_2, 2, 4), (trp_lance_infantry_1, 2, 4)]),

	("kingdom_13_reinforcements_b_e", "{!}kingdom 4 reinforcements b", icon_people_player|pf_label_small, 0, fac_commoners, aggressiveness_0, [(trp_lance_infantry_4, 2, 4), (trp_lance_infantry_3, 2, 4), (trp_lance_infantry_5, 2, 4), (trp_lance_archer_2, 2, 4), (trp_lance_infantry_2, 2, 4), (trp_lance_infantry_1, 2, 4)]),

	("kingdom_13_reinforcements_c_e", "{!}kingdom 4 reinforcements c", icon_people_player|pf_label_small, 0, fac_commoners, aggressiveness_0, [(trp_lance_infantry_4, 2, 4), (trp_lance_infantry_3, 2, 4), (trp_lance_infantry_5, 2, 4), (trp_lance_archer_2, 2, 4), (trp_lance_infantry_2, 2, 4), (trp_lance_infantry_1, 2, 4)]),

	("kingdom_13_reinforcements_d_e", "{!}kingdom 4 reinforcements d", icon_people_player|pf_label_small, 0, fac_commoners, aggressiveness_0, [(trp_lance_infantry_4, 2, 4), (trp_lance_infantry_3, 2, 4), (trp_lance_infantry_5, 2, 4), (trp_lance_archer_2, 2, 4), (trp_lance_archer_5, 2, 4), (trp_lance_archer_2, 2, 4)]),

	("kingdom_13_reinforcements_e_e", "{!}kingdom 4 reinforcements e", icon_people_player|pf_label_small, 0, fac_commoners, aggressiveness_0, [(trp_lance_infantry_4, 2, 4), (trp_lance_infantry_3, 2, 4), (trp_lance_infantry_5, 2, 4), (trp_lance_archer_2, 2, 4), (trp_lance_archer_5, 2, 4), (trp_lance_archer_2, 2, 4)]),

	("kingdom_13_reinforcements_f_e", "{!}kingdom 4 reinforcements f", icon_people_player|pf_label_small, 0, fac_commoners, aggressiveness_0, [(trp_lance_infantry_4, 2, 4), (trp_lance_infantry_3, 2, 4), (trp_lance_infantry_5, 2, 4), (trp_lance_archer_2, 2, 4), (trp_lance_archer_5, 2, 4), (trp_lance_archer_2, 2, 4)]),

	("kingdom_14_reinforcements_a_e", "{!}kingdom 4 reinforcements a", icon_people_player|pf_label_small, 0, fac_commoners, aggressiveness_0, [(trp_port_myrish_crossbowmen, 2, 4), (trp_lance_infantry_3, 2, 4), (trp_lance_infantry_5, 2, 4), (trp_port_myrish_crossbowmen, 2, 4), (trp_lance_infantry_2, 2, 4), (trp_lance_infantry_1, 2, 4)]),

	("kingdom_14_reinforcements_b_e", "{!}kingdom 4 reinforcements b", icon_people_player|pf_label_small, 0, fac_commoners, aggressiveness_0, [(trp_port_myrish_crossbowmen, 2, 4), (trp_lance_infantry_3, 2, 4), (trp_lance_infantry_5, 2, 4), (trp_port_myrish_crossbowmen, 2, 4), (trp_lance_infantry_2, 2, 4), (trp_lance_infantry_1, 2, 4)]),

	("kingdom_14_reinforcements_c_e", "{!}kingdom 4 reinforcements c", icon_people_player|pf_label_small, 0, fac_commoners, aggressiveness_0, [(trp_lance_infantry_4, 2, 4), (trp_lance_infantry_3, 2, 4), (trp_lance_infantry_5, 2, 4), (trp_lance_archer_2, 2, 4), (trp_lance_infantry_2, 2, 4), (trp_lance_infantry_1, 2, 4)]),

	("kingdom_14_reinforcements_d_e", "{!}kingdom 4 reinforcements d", icon_people_player|pf_label_small, 0, fac_commoners, aggressiveness_0, [(trp_lance_infantry_4, 2, 4), (trp_lance_infantry_3, 2, 4), (trp_lance_infantry_5, 2, 4), (trp_lance_archer_2, 2, 4), (trp_lance_archer_5, 2, 4), (trp_lance_archer_2, 2, 4)]),

	("kingdom_14_reinforcements_e_e", "{!}kingdom 4 reinforcements e", icon_people_player|pf_label_small, 0, fac_commoners, aggressiveness_0, [(trp_lance_infantry_4, 2, 4), (trp_lance_infantry_3, 2, 4), (trp_lance_infantry_5, 2, 4), (trp_lance_archer_2, 2, 4), (trp_lance_archer_5, 2, 4), (trp_lance_archer_2, 2, 4)]),

	("kingdom_14_reinforcements_f_e", "{!}kingdom 4 reinforcements f", icon_people_player|pf_label_small, 0, fac_commoners, aggressiveness_0, [(trp_lance_infantry_4, 2, 4), (trp_lance_infantry_3, 2, 4), (trp_lance_infantry_5, 2, 4), (trp_lance_archer_2, 2, 4), (trp_lance_archer_5, 2, 4), (trp_lance_archer_2, 2, 4)]),

	("kingdom_15_reinforcements_a_e", "{!}kingdom 4 reinforcements a", icon_people_player|pf_label_small, 0, fac_commoners, aggressiveness_0, [(trp_lance_infantry_4, 2, 4), (trp_lance_infantry_3, 2, 4), (trp_lance_infantry_5, 2, 4), (trp_lance_archer_2, 2, 4), (trp_lance_infantry_2, 2, 4), (trp_lance_infantry_1, 2, 4)]),

	("kingdom_15_reinforcements_b_e", "{!}kingdom 4 reinforcements b", icon_people_player|pf_label_small, 0, fac_commoners, aggressiveness_0, [(trp_lance_infantry_4, 2, 4), (trp_lance_infantry_3, 2, 4), (trp_lance_infantry_5, 2, 4), (trp_lance_archer_2, 2, 4), (trp_lance_infantry_2, 2, 4), (trp_lance_infantry_1, 2, 4)]),

	("kingdom_15_reinforcements_c_e", "{!}kingdom 4 reinforcements c", icon_people_player|pf_label_small, 0, fac_commoners, aggressiveness_0, [(trp_lance_infantry_4, 2, 4), (trp_lance_infantry_3, 2, 4), (trp_lance_infantry_5, 2, 4), (trp_lance_archer_2, 2, 4), (trp_lance_infantry_2, 2, 4), (trp_lance_infantry_1, 2, 4)]),

	("kingdom_15_reinforcements_d_e", "{!}kingdom 4 reinforcements d", icon_people_player|pf_label_small, 0, fac_commoners, aggressiveness_0, [(trp_lance_infantry_4, 2, 4), (trp_lance_infantry_3, 2, 4), (trp_lance_infantry_5, 2, 4), (trp_lance_archer_2, 2, 4), (trp_lance_archer_5, 2, 4), (trp_lance_archer_2, 2, 4)]),

	("kingdom_15_reinforcements_e_e", "{!}kingdom 4 reinforcements e", icon_people_player|pf_label_small, 0, fac_commoners, aggressiveness_0, [(trp_lance_infantry_4, 2, 4), (trp_lance_infantry_3, 2, 4), (trp_lance_infantry_5, 2, 4), (trp_lance_archer_2, 2, 4), (trp_lance_archer_5, 2, 4), (trp_lance_archer_2, 2, 4)]),

	("kingdom_15_reinforcements_f_e", "{!}kingdom 4 reinforcements f", icon_people_player|pf_label_small, 0, fac_commoners, aggressiveness_0, [(trp_lance_infantry_4, 2, 4), (trp_lance_infantry_3, 2, 4), (trp_lance_infantry_5, 2, 4), (trp_lance_archer_2, 2, 4), (trp_lance_archer_5, 2, 4), (trp_lance_archer_2, 2, 4)]),

	("kingdom_16_reinforcements_a_e", "{!}kingdom 4 reinforcements a", icon_people_player|pf_label_small, 0, fac_commoners, aggressiveness_0, [(trp_lance_infantry_4, 2, 4), (trp_lance_infantry_3, 2, 4), (trp_lance_infantry_5, 2, 4), (trp_lance_archer_2, 2, 4), (trp_lance_infantry_2, 2, 4), (trp_lance_infantry_1, 2, 4)]),

	("kingdom_16_reinforcements_b_e", "{!}kingdom 4 reinforcements b", icon_people_player|pf_label_small, 0, fac_commoners, aggressiveness_0, [(trp_lance_infantry_4, 2, 4), (trp_lance_infantry_3, 2, 4), (trp_lance_infantry_5, 2, 4), (trp_lance_archer_2, 2, 4), (trp_lance_infantry_2, 2, 4), (trp_lance_infantry_1, 2, 4)]),

	("kingdom_16_reinforcements_c_e", "{!}kingdom 4 reinforcements c", icon_people_player|pf_label_small, 0, fac_commoners, aggressiveness_0, [(trp_lance_infantry_4, 2, 4), (trp_lance_infantry_3, 2, 4), (trp_lance_infantry_5, 2, 4), (trp_lance_archer_2, 2, 4), (trp_lance_infantry_2, 2, 4), (trp_lance_infantry_1, 2, 4)]),

	("kingdom_16_reinforcements_d_e", "{!}kingdom 4 reinforcements d", icon_people_player|pf_label_small, 0, fac_commoners, aggressiveness_0, [(trp_lance_infantry_4, 2, 4), (trp_lance_infantry_3, 2, 4), (trp_lance_infantry_5, 2, 4), (trp_lance_archer_2, 2, 4), (trp_lance_archer_5, 2, 4), (trp_lance_archer_2, 2, 4)]),

	("kingdom_16_reinforcements_e_e", "{!}kingdom 4 reinforcements e", icon_people_player|pf_label_small, 0, fac_commoners, aggressiveness_0, [(trp_lance_infantry_4, 2, 4), (trp_lance_infantry_3, 2, 4), (trp_lance_infantry_5, 2, 4), (trp_lance_archer_2, 2, 4), (trp_lance_archer_5, 2, 4), (trp_lance_archer_2, 2, 4)]),

	("kingdom_16_reinforcements_f_e", "{!}kingdom 4 reinforcements f", icon_people_player|pf_label_small, 0, fac_commoners, aggressiveness_0, [(trp_lance_infantry_4, 2, 4), (trp_lance_infantry_3, 2, 4), (trp_lance_infantry_5, 2, 4), (trp_lance_archer_2, 2, 4), (trp_lance_archer_5, 2, 4), (trp_lance_archer_2, 2, 4)]),

	("kingdom_17_reinforcements_a_e", "{!}kingdom 4 reinforcements a", icon_people_player|pf_label_small, 0, fac_commoners, aggressiveness_0, [(trp_lance_infantry_4, 2, 4), (trp_lance_infantry_3, 2, 4), (trp_lance_infantry_5, 2, 4), (trp_lance_archer_2, 2, 4), (trp_lance_infantry_2, 2, 4), (trp_lance_infantry_1, 2, 4)]),

	("kingdom_17_reinforcements_b_e", "{!}kingdom 4 reinforcements b", icon_people_player|pf_label_small, 0, fac_commoners, aggressiveness_0, [(trp_lance_infantry_4, 2, 4), (trp_lance_infantry_3, 2, 4), (trp_lance_infantry_5, 2, 4), (trp_lance_archer_2, 2, 4), (trp_lance_infantry_2, 2, 4), (trp_lance_infantry_1, 2, 4)]),

	("kingdom_17_reinforcements_c_e", "{!}kingdom 4 reinforcements c", icon_people_player|pf_label_small, 0, fac_commoners, aggressiveness_0, [(trp_lance_infantry_4, 2, 4), (trp_lance_infantry_3, 2, 4), (trp_lance_infantry_5, 2, 4), (trp_lance_archer_2, 2, 4), (trp_lance_infantry_2, 2, 4), (trp_lance_infantry_1, 2, 4)]),

	("kingdom_17_reinforcements_d_e", "{!}kingdom 4 reinforcements d", icon_people_player|pf_label_small, 0, fac_commoners, aggressiveness_0, [(trp_lance_infantry_4, 2, 4), (trp_lance_infantry_3, 2, 4), (trp_lance_infantry_5, 2, 4), (trp_lance_archer_2, 2, 4), (trp_lance_archer_5, 2, 4), (trp_lance_archer_2, 2, 4)]),

	("kingdom_17_reinforcements_e_e", "{!}kingdom 4 reinforcements e", icon_people_player|pf_label_small, 0, fac_commoners, aggressiveness_0, [(trp_lance_infantry_4, 2, 4), (trp_lance_infantry_3, 2, 4), (trp_lance_infantry_5, 2, 4), (trp_lance_archer_2, 2, 4), (trp_lance_archer_5, 2, 4), (trp_lance_archer_2, 2, 4)]),

	("kingdom_17_reinforcements_f_e", "{!}kingdom 4 reinforcements f", icon_people_player|pf_label_small, 0, fac_commoners, aggressiveness_0, [(trp_lance_infantry_4, 2, 4), (trp_lance_infantry_3, 2, 4), (trp_lance_infantry_5, 2, 4), (trp_lance_archer_2, 2, 4), (trp_lance_archer_5, 2, 4), (trp_lance_archer_2, 2, 4)]),

	("kingdom_18_reinforcements_a_e", "{!}kingdom 4 reinforcements a", icon_people_player|pf_label_small, 0, fac_commoners, aggressiveness_0, [(trp_lance_infantry_4, 2, 4), (trp_lance_infantry_3, 2, 4), (trp_lance_infantry_5, 2, 4), (trp_lance_archer_2, 2, 4), (trp_lance_infantry_2, 2, 4), (trp_lance_infantry_1, 2, 4)]),

	("kingdom_18_reinforcements_b_e", "{!}kingdom 4 reinforcements b", icon_people_player|pf_label_small, 0, fac_commoners, aggressiveness_0, [(trp_lance_infantry_4, 2, 4), (trp_lance_infantry_3, 2, 4), (trp_lance_infantry_5, 2, 4), (trp_lance_archer_2, 2, 4), (trp_lance_infantry_2, 2, 4), (trp_lance_infantry_1, 2, 4)]),

	("kingdom_18_reinforcements_c_e", "{!}kingdom 4 reinforcements c", icon_people_player|pf_label_small, 0, fac_commoners, aggressiveness_0, [(trp_lance_infantry_4, 2, 4), (trp_lance_infantry_3, 2, 4), (trp_lance_infantry_5, 2, 4), (trp_lance_archer_2, 2, 4), (trp_lance_infantry_2, 2, 4), (trp_lance_infantry_1, 2, 4)]),

	("kingdom_18_reinforcements_d_e", "{!}kingdom 4 reinforcements d", icon_people_player|pf_label_small, 0, fac_commoners, aggressiveness_0, [(trp_lance_infantry_4, 2, 4), (trp_lance_infantry_3, 2, 4), (trp_lance_infantry_5, 2, 4), (trp_lance_archer_2, 2, 4), (trp_lance_archer_5, 2, 4), (trp_lance_archer_2, 2, 4)]),

	("kingdom_18_reinforcements_e_e", "{!}kingdom 4 reinforcements e", icon_people_player|pf_label_small, 0, fac_commoners, aggressiveness_0, [(trp_lance_infantry_4, 2, 4), (trp_lance_infantry_3, 2, 4), (trp_lance_infantry_5, 2, 4), (trp_lance_archer_2, 2, 4), (trp_lance_archer_5, 2, 4), (trp_lance_archer_2, 2, 4)]),

	("kingdom_18_reinforcements_f_e", "{!}kingdom 4 reinforcements f", icon_people_player|pf_label_small, 0, fac_commoners, aggressiveness_0, [(trp_lance_infantry_4, 2, 4), (trp_lance_infantry_3, 2, 4), (trp_lance_infantry_5, 2, 4), (trp_lance_archer_2, 2, 4), (trp_lance_archer_5, 2, 4), (trp_lance_archer_2, 2, 4)]),

	("kingdom_19_reinforcements_a_e", "{!}kingdom 19 reinforcements a", icon_people_player|pf_label_small, 0, fac_commoners, aggressiveness_0, [(trp_sarranid_n_millet19, 2, 4), (trp_sarranid_n_ajam19, 2, 4), (trp_sarranid_n_cemaat19, 2, 4), (trp_sarranid_n_jebelus19, 2, 4), (trp_sarranid_n_yerliyya19, 2, 4), (trp_sarranid_n_cemaat19, 1, 2)]),

	("kingdom_19_reinforcements_b_e", "{!}kingdom 19 reinforcements b", icon_people_player|pf_label_small, 0, fac_commoners, aggressiveness_0, [(trp_sarranid_n_millet19, 2, 4), (trp_sarranid_n_ajam19, 2, 4), (trp_sarranid_n_cemaat19, 2, 4), (trp_sarranid_n_jebelus19, 2, 4), (trp_sarranid_n_yerliyya19, 2, 4), (trp_sarranid_n_cemaat19, 1, 2)]),

	("kingdom_19_reinforcements_c_e", "{!}kingdom 19 reinforcements c", icon_people_player|pf_label_small, 0, fac_commoners, aggressiveness_0, [(trp_sarranid_n_millet19, 2, 4), (trp_sarranid_n_ajam19, 2, 4), (trp_sarranid_n_cemaat19, 2, 4), (trp_sarranid_n_yerliyya19, 2, 4), (trp_sarranid_n_yerliyya19, 2, 4), (trp_sarranid_n_cemaat19, 1, 2)]),

	("kingdom_19_reinforcements_d_e", "{!}kingdom 19 reinforcements d", icon_people_player|pf_label_small, 0, fac_commoners, aggressiveness_0, [(trp_sarranid_n_garip19, 2, 4), (trp_sarranid_n_yeniceri19, 2, 4), (trp_sarranid_n_kapikula19, 2, 4), (trp_sarranid_n_uluteci19, 2, 4), (trp_sarranid_n_cemaat19, 2, 4), (trp_sarranid_n_kapikula19, 1, 2)]),

	("kingdom_19_reinforcements_e_e", "{!}kingdom 19 reinforcements e", icon_people_player|pf_label_small, 0, fac_commoners, aggressiveness_0, [(trp_sarranid_n_millet19, 2, 4), (trp_sarranid_n_ajam19, 2, 4), (trp_sarranid_n_cemaat19, 2, 4), (trp_sarranid_n_yerliyya19, 2, 4), (trp_sarranid_n_yerliyya19, 2, 4), (trp_sarranid_n_cemaat19, 1, 2)]),

	("kingdom_19_reinforcements_f_e", "{!}kingdom 19 reinforcements f", icon_people_player|pf_label_small, 0, fac_commoners, aggressiveness_0, [(trp_sarranid_n_garip19, 2, 4), (trp_sarranid_n_yeniceri19, 2, 4), (trp_sarranid_n_kapikula19, 2, 4), (trp_sarranid_n_uluteci19, 2, 4), (trp_sarranid_n_cemaat19, 2, 4), (trp_sarranid_n_kapikula19, 1, 2)]),

	("kingdom_20_reinforcements_a_e", "{!}kingdom 20 reinforcements a", icon_people_player|pf_label_small, 0, fac_commoners, aggressiveness_0, [(trp_sarranid_n_millet20, 2, 4), (trp_sarranid_n_ajam20, 2, 4), (trp_sarranid_n_cemaat20, 2, 4), (trp_sarranid_n_jebelus20, 2, 4), (trp_sarranid_n_yerliyya20, 2, 4), (trp_sarranid_n_cemaat20, 1, 2)]),

	("kingdom_20_reinforcements_b_e", "{!}kingdom 20 reinforcements b", icon_people_player|pf_label_small, 0, fac_commoners, aggressiveness_0, [(trp_sarranid_n_millet20, 2, 4), (trp_sarranid_n_ajam20, 2, 4), (trp_sarranid_n_cemaat20, 2, 4), (trp_sarranid_n_jebelus20, 2, 4), (trp_sarranid_n_yerliyya20, 2, 4), (trp_sarranid_n_cemaat20, 1, 2)]),

	("kingdom_20_reinforcements_c_e", "{!}kingdom 20 reinforcements c", icon_people_player|pf_label_small, 0, fac_commoners, aggressiveness_0, [(trp_sarranid_n_millet20, 2, 4), (trp_sarranid_n_ajam20, 2, 4), (trp_sarranid_n_cemaat20, 2, 4), (trp_sarranid_n_yerliyya20, 2, 4), (trp_sarranid_n_yerliyya20, 2, 4), (trp_sarranid_n_cemaat20, 1, 2)]),

	("kingdom_20_reinforcements_d_e", "{!}kingdom 20 reinforcements d", icon_people_player|pf_label_small, 0, fac_commoners, aggressiveness_0, [(trp_sarranid_n_garip20, 2, 4), (trp_sarranid_n_yeniceri20, 2, 4), (trp_sarranid_n_kapikula20, 2, 4), (trp_sarranid_n_uluteci20, 2, 4), (trp_sarranid_n_cemaat20, 2, 4), (trp_sarranid_n_kapikula20, 1, 2)]),

	("kingdom_20_reinforcements_e_e", "{!}kingdom 20 reinforcements e", icon_people_player|pf_label_small, 0, fac_commoners, aggressiveness_0, [(trp_sarranid_n_millet20, 2, 4), (trp_sarranid_n_ajam20, 2, 4), (trp_sarranid_n_cemaat20, 2, 4), (trp_sarranid_n_yerliyya20, 2, 4), (trp_sarranid_n_yerliyya20, 2, 4), (trp_sarranid_n_cemaat20, 1, 2)]),

	("kingdom_20_reinforcements_f_e", "{!}kingdom 20 reinforcements f", icon_people_player|pf_label_small, 0, fac_commoners, aggressiveness_0, [(trp_sarranid_n_garip20, 2, 4), (trp_sarranid_n_yeniceri20, 2, 4), (trp_sarranid_n_kapikula20, 2, 4), (trp_sarranid_n_uluteci20, 2, 4), (trp_sarranid_n_cemaat20, 2, 4), (trp_sarranid_n_kapikula20, 1, 2)]),

	("kingdom_21_reinforcements_a_e", "{!}kingdom 21 reinforcements a", icon_people_player|pf_label_small, 0, fac_commoners, aggressiveness_0, [(trp_sarranid_n_millet22, 2, 4), (trp_sarranid_n_ajam22, 2, 4), (trp_sarranid_n_cemaat22, 2, 4), (trp_sarranid_n_cemaat22, 2, 4), (trp_sarranid_n_yeniceri22, 2, 4), (trp_sarranid_n_kapikula22, 2, 4)]),

	("kingdom_21_reinforcements_b_e", "{!}kingdom 21 reinforcements b", icon_people_player|pf_label_small, 0, fac_commoners, aggressiveness_0, [(trp_sarranid_n_millet22, 2, 4), (trp_sarranid_n_ajam22, 2, 4), (trp_sarranid_n_cemaat22, 2, 4), (trp_sarranid_n_cemaat22, 2, 4), (trp_sarranid_n_yeniceri22, 2, 4), (trp_sarranid_n_kapikula22, 2, 4)]),

	("kingdom_21_reinforcements_c_e", "{!}kingdom 21 reinforcements c", icon_people_player|pf_label_small, 0, fac_commoners, aggressiveness_0, [(trp_sarranid_n_uluteci22, 2, 4), (trp_sarranid_n_ajam22, 2, 4), (trp_sarranid_n_cemaat22, 2, 4), (trp_sarranid_n_cemaat22, 2, 4), (trp_sarranid_n_yeniceri22, 2, 4), (trp_sarranid_n_kapikula22, 2, 4)]),

	("kingdom_21_reinforcements_d_e", "{!}kingdom 21 reinforcements d", icon_people_player|pf_label_small, 0, fac_commoners, aggressiveness_0, [(trp_sarranid_n_uluteci22, 2, 4), (trp_sarranid_n_ajam22, 2, 4), (trp_sarranid_n_cemaat22, 2, 4), (trp_sarranid_n_jebelus22, 2, 4), (trp_sarranid_n_yeniceri22, 2, 4), (trp_sarranid_n_kapikula22, 2, 4)]),

	("kingdom_21_reinforcements_e_e", "{!}kingdom 21 reinforcements e", icon_people_player|pf_label_small, 0, fac_commoners, aggressiveness_0, [(trp_sarranid_n_uluteci22, 2, 4), (trp_sarranid_n_ajam22, 2, 4), (trp_sarranid_n_cemaat22, 2, 4), (trp_sarranid_n_jebelus22, 2, 4), (trp_sarranid_n_yeniceri22, 2, 4), (trp_sarranid_n_kapikula22, 2, 4)]),

	("kingdom_21_reinforcements_f_e", "{!}kingdom 21 reinforcements f", icon_people_player|pf_label_small, 0, fac_commoners, aggressiveness_0, [(trp_sarranid_n_uluteci22, 2, 4), (trp_sarranid_n_ajam22, 2, 4), (trp_sarranid_n_cemaat22, 2, 4), (trp_sarranid_n_jebelus22, 2, 4), (trp_sarranid_n_yeniceri22, 2, 4), (trp_sarranid_n_kapikula22, 2, 4)]),

	("kingdom_22_reinforcements_a_e", "{!}kingdom 22 reinforcements a", icon_people_player|pf_label_small, 0, fac_commoners, aggressiveness_0, [(trp_sarranid_n_millet23, 2, 4), (trp_sarranid_n_ajam23, 2, 4), (trp_sarranid_n_cemaat23, 2, 4), (trp_sarranid_n_jebelus23, 2, 4), (trp_sarranid_n_yeniceri23, 2, 4), (trp_sarranid_n_yeniceri23, 2, 4)]),

	("kingdom_22_reinforcements_b_e", "{!}kingdom 22 reinforcements b", icon_people_player|pf_label_small, 0, fac_commoners, aggressiveness_0, [(trp_sarranid_n_millet23, 2, 4), (trp_sarranid_n_ajam23, 2, 4), (trp_sarranid_n_cemaat23, 2, 4), (trp_sarranid_n_jebelus23, 2, 4), (trp_sarranid_n_yeniceri23, 2, 4), (trp_sarranid_n_yeniceri23, 2, 4)]),

	("kingdom_22_reinforcements_c_e", "{!}kingdom 22 reinforcements c", icon_people_player|pf_label_small, 0, fac_commoners, aggressiveness_0, [(trp_sarranid_n_millet23, 2, 4), (trp_sarranid_n_ajam23, 2, 4), (trp_sarranid_n_cemaat23, 2, 4), (trp_sarranid_n_jebelus23, 2, 4), (trp_sarranid_n_yeniceri23, 2, 4), (trp_sarranid_n_yeniceri23, 2, 4)]),

	("kingdom_22_reinforcements_d_e", "{!}kingdom 22 reinforcements d", icon_people_player|pf_label_small, 0, fac_commoners, aggressiveness_0, [(trp_sarranid_n_millet23, 2, 4), (trp_sarranid_n_ajam23, 2, 4), (trp_sarranid_n_cemaat23, 2, 4), (trp_sarranid_n_jebelus23, 2, 4), (trp_sarranid_n_yeniceri23, 2, 4), (trp_sarranid_n_yeniceri23, 2, 4)]),

	("kingdom_22_reinforcements_e_e", "{!}kingdom 22 reinforcements e", icon_people_player|pf_label_small, 0, fac_commoners, aggressiveness_0, [(trp_sarranid_n_millet23, 2, 4), (trp_sarranid_n_ajam23, 2, 4), (trp_sarranid_n_cemaat23, 2, 4), (trp_sarranid_n_jebelus23, 2, 4), (trp_sarranid_n_yeniceri23, 2, 4), (trp_sarranid_n_yeniceri23, 2, 4)]),

	("kingdom_22_reinforcements_f_e", "{!}kingdom 22 reinforcements f", icon_people_player|pf_label_small, 0, fac_commoners, aggressiveness_0, [(trp_sarranid_n_millet23, 2, 4), (trp_sarranid_n_ajam23, 2, 4), (trp_sarranid_n_cemaat23, 2, 4), (trp_sarranid_n_jebelus23, 2, 4), (trp_sarranid_n_yeniceri23, 2, 4), (trp_sarranid_n_yeniceri23, 2, 4)]),

	("golden_company_reinforcements_a", "{!}kingdom 20 reinforcements a", icon_people_player|pf_label_small, 0, fac_commoners, aggressiveness_0, [(trp_mercenary_infantry_1, 2, 4), (trp_golden_company_man_at_arms, 2, 4), (trp_golden_company_man_at_arms, 2, 4), (trp_golden_company_archer, 2, 4), (trp_golden_company_squire, 2, 4), (trp_golden_company_knight, 1, 2)]),

	("golden_company_reinforcements_b", "{!}kingdom 20 reinforcements b", icon_people_player|pf_label_small, 0, fac_commoners, aggressiveness_0, [(trp_mercenary_infantry_2, 2, 4), (trp_golden_company_man_at_arms, 2, 4), (trp_golden_company_man_at_arms, 2, 4), (trp_golden_company_archer, 2, 4), (trp_golden_company_squire, 2, 4), (trp_golden_company_knight, 1, 2)]),

	("golden_company_reinforcements_c", "{!}kingdom 20 reinforcements c", icon_people_player|pf_label_small, 0, fac_commoners, aggressiveness_0, [(trp_mercenary_infantry_3, 2, 4), (trp_golden_company_man_at_arms, 2, 4), (trp_golden_company_man_at_arms, 2, 4), (trp_golden_company_archer, 2, 4), (trp_golden_company_squire, 2, 4), (trp_golden_company_knight, 1, 2)]),

	("golden_company_reinforcements_d", "{!}kingdom 20 reinforcements d", icon_people_player|pf_label_small, 0, fac_commoners, aggressiveness_0, [(trp_mercenary_infantry_1, 2, 4), (trp_golden_company_man_at_arms, 2, 4), (trp_golden_company_man_at_arms, 2, 4), (trp_golden_company_archer, 2, 4), (trp_mercenary_archer_1, 2, 4), (trp_mercenary_archer_1, 1, 2)]),

	("golden_company_reinforcements_e", "{!}kingdom 20 reinforcements e", icon_people_player|pf_label_small, 0, fac_commoners, aggressiveness_0, [(trp_mercenary_infantry_2, 2, 4), (trp_golden_company_man_at_arms, 2, 4), (trp_golden_company_man_at_arms, 2, 4), (trp_golden_company_archer, 2, 4), (trp_mercenary_archer_2, 2, 4), (trp_mercenary_archer_2, 1, 2)]),

	("golden_company_reinforcements_f", "{!}kingdom 20 reinforcements f", icon_people_player|pf_label_small, 0, fac_commoners, aggressiveness_0, [(trp_mercenary_infantry_3, 2, 4), (trp_golden_company_man_at_arms, 2, 4), (trp_golden_company_man_at_arms, 2, 4), (trp_golden_company_archer, 2, 4), (trp_mercenary_archer_3, 2, 4), (trp_mercenary_archer_3, 1, 2)]),
	
	("clegane_reinforcements_a", "{!}kingdom 9 reinforcements a", icon_people_player|pf_label_small, 0, fac_commoners, aggressiveness_0, [(trp_sarranid_n_cemaat9, 2, 4), (trp_sarranid_n_ajam9, 2, 4), (trp_sarranid_n_cemaat9, 2, 4), (trp_sarranid_n_jebelus9, 2, 4), (trp_sarranid_n_yerliyya9, 2, 4), (trp_sarranid_n_cemaat9, 1, 2)]),

	("clegane_reinforcements_b", "{!}kingdom 9 reinforcements b", icon_people_player|pf_label_small, 0, fac_commoners, aggressiveness_0, [(trp_sarranid_n_millet9, 2, 4), (trp_sarranid_n_ajam9, 2, 4), (trp_sarranid_n_cemaat9, 2, 4), (trp_sarranid_n_jebelus9, 2, 4), (trp_sarranid_n_yerliyya9, 2, 4), (trp_sarranid_n_cemaat9, 1, 2)]),

	("clegane_reinforcements_c", "{!}kingdom 9 reinforcements c", icon_people_player|pf_label_small, 0, fac_commoners, aggressiveness_0, [(trp_sarranid_n_millet9, 2, 4), (trp_sarranid_n_ajam9, 2, 4), (trp_sarranid_n_cemaat9, 2, 4), (trp_sarranid_n_yerliyya9, 2, 4), (trp_sarranid_n_yerliyya9, 2, 4), (trp_sarranid_n_cemaat9, 1, 2)]),

	("clegane_reinforcements_d", "{!}kingdom 9 reinforcements d", icon_people_player|pf_label_small, 0, fac_commoners, aggressiveness_0, [(trp_sarranid_n_millet9, 2, 4), (trp_sarranid_n_ajam9, 2, 4), (trp_sarranid_n_yeniceri9, 2, 4), (trp_sarranid_n_kapikula9, 2, 4), (trp_sarranid_n_uluteci9, 2, 4), (trp_sarranid_n_cemaat9, 1, 2)]),

	("clegane_reinforcements_e", "{!}kingdom 9 reinforcements e", icon_people_player|pf_label_small, 0, fac_commoners, aggressiveness_0, [(trp_sarranid_n_millet9, 2, 4), (trp_sarranid_n_ajam9, 2, 4), (trp_sarranid_n_cemaat9, 2, 4), (trp_sarranid_n_yerliyya9, 2, 4), (trp_sarranid_n_yerliyya9, 2, 4), (trp_sarranid_n_cemaat9, 1, 2)]),

	("clegane_reinforcements_f", "{!}kingdom 9 reinforcements f", icon_people_player|pf_label_small, 0, fac_commoners, aggressiveness_0, [(trp_sarranid_n_garip9, 2, 4), (trp_westerlands_troop_1, 2, 4), (trp_sarranid_n_yeniceri9, 2, 4), (trp_sarranid_n_kapikula9, 2, 4), (trp_sarranid_n_uluteci9, 2, 4), (trp_sarranid_n_cemaat9, 1, 2)]),

	("holy_reinforcements_a", "{!}kingdom 9 reinforcements a", icon_people_player|pf_label_small, 0, fac_commoners, aggressiveness_0, [(trp_sarranid_n_cemaat9, 2, 4), (trp_sarranid_n_ajam9, 2, 4), (trp_sarranid_n_cemaat9, 2, 4), (trp_sarranid_n_jebelus9, 2, 4), (trp_sarranid_n_yerliyya9, 2, 4), (trp_sarranid_n_cemaat9, 1, 2)]),

	("holy_reinforcements_b", "{!}kingdom 9 reinforcements b", icon_people_player|pf_label_small, 0, fac_commoners, aggressiveness_0, [(trp_sarranid_n_millet9, 2, 4), (trp_sarranid_n_ajam9, 2, 4), (trp_sarranid_n_cemaat9, 2, 4), (trp_sarranid_n_jebelus9, 2, 4), (trp_sarranid_n_yerliyya9, 2, 4), (trp_sarranid_n_cemaat9, 1, 2)]),

	("holy_reinforcements_c", "{!}kingdom 9 reinforcements c", icon_people_player|pf_label_small, 0, fac_commoners, aggressiveness_0, [(trp_sarranid_n_millet9, 2, 4), (trp_sarranid_n_ajam9, 2, 4), (trp_sarranid_n_cemaat9, 2, 4), (trp_sarranid_n_yerliyya9, 2, 4), (trp_sarranid_n_yerliyya9, 2, 4), (trp_sarranid_n_cemaat9, 1, 2)]),

	("holy_reinforcements_d", "{!}kingdom 9 reinforcements d", icon_people_player|pf_label_small, 0, fac_commoners, aggressiveness_0, [(trp_sarranid_n_millet9, 2, 4), (trp_sarranid_n_ajam9, 2, 4), (trp_sarranid_n_yeniceri9, 2, 4), (trp_sarranid_n_kapikula9, 2, 4), (trp_sarranid_n_uluteci9, 2, 4), (trp_sarranid_n_cemaat9, 1, 2)]),

	("holy_reinforcements_e", "{!}kingdom 9 reinforcements e", icon_people_player|pf_label_small, 0, fac_commoners, aggressiveness_0, [(trp_sarranid_n_millet9, 2, 4), (trp_sarranid_n_ajam9, 2, 4), (trp_sarranid_n_cemaat9, 2, 4), (trp_sarranid_n_yerliyya9, 2, 4), (trp_sarranid_n_yerliyya9, 2, 4), (trp_sarranid_n_cemaat9, 1, 2)]),

	("holy_reinforcements_f", "{!}kingdom 9 reinforcements f", icon_people_player|pf_label_small, 0, fac_commoners, aggressiveness_0, [(trp_sarranid_n_garip9, 2, 4), (trp_westerlands_troop_1, 2, 4), (trp_sarranid_n_yeniceri9, 2, 4), (trp_sarranid_n_kapikula9, 2, 4), (trp_sarranid_n_uluteci9, 2, 4), (trp_sarranid_n_cemaat9, 1, 2)]),

	("crow_reinforcements_a", "{!}kingdom 16 reinforcements a", icon_people_player|pf_label_small, 0, fac_commoners, aggressiveness_0, [(trp_lance_infantry_4, 2, 4), (trp_lance_infantry_3, 2, 4), (trp_lance_infantry_5, 2, 4), (trp_lance_archer_2, 2, 4), (trp_lance_infantry_2, 2, 4), (trp_lance_infantry_1, 2, 4)]),

	("crow_reinforcements_b", "{!}kingdom 16 reinforcements b", icon_people_player|pf_label_small, 0, fac_commoners, aggressiveness_0, [(trp_lance_infantry_4, 2, 4), (trp_lance_infantry_3, 2, 4), (trp_lance_infantry_5, 2, 4), (trp_lance_archer_2, 2, 4), (trp_lance_infantry_2, 2, 4), (trp_lance_infantry_1, 2, 4)]),

	("crow_reinforcements_c", "{!}kingdom 16 reinforcements c", icon_people_player|pf_label_small, 0, fac_commoners, aggressiveness_0, [(trp_lance_infantry_4, 2, 4), (trp_lance_infantry_3, 2, 4), (trp_lance_infantry_5, 2, 4), (trp_lance_archer_2, 2, 4), (trp_lance_infantry_2, 2, 4), (trp_lance_infantry_1, 2, 4)]),

	("crow_reinforcements_d", "{!}kingdom 16 reinforcements d", icon_people_player|pf_label_small, 0, fac_commoners, aggressiveness_0, [(trp_lance_infantry_4, 2, 4), (trp_lance_infantry_3, 2, 4), (trp_lance_infantry_5, 2, 4), (trp_lance_archer_2, 2, 4), (trp_lance_archer_5, 2, 4), (trp_lance_archer_2, 2, 4)]),

	("crow_reinforcements_e", "{!}kingdom 16 reinforcements e", icon_people_player|pf_label_small, 0, fac_commoners, aggressiveness_0, [(trp_lance_infantry_4, 2, 4), (trp_lance_infantry_3, 2, 4), (trp_lance_infantry_5, 2, 4), (trp_lance_archer_2, 2, 4), (trp_lance_archer_5, 2, 4), (trp_lance_archer_2, 2, 4)]),

	("crow_reinforcements_f", "{!}kingdom 16 reinforcements f", icon_people_player|pf_label_small, 0, fac_commoners, aggressiveness_0, [(trp_lance_infantry_4, 2, 4), (trp_lance_infantry_3, 2, 4), (trp_lance_infantry_5, 2, 4), (trp_lance_archer_2, 2, 4), (trp_lance_archer_5, 2, 4), (trp_lance_archer_2, 2, 4)]),

	("horror_reinforcements_a", "{!}kingdom 16 reinforcements a", icon_people_player|pf_label_small, 0, fac_commoners, aggressiveness_0, [(trp_lance_infantry_4, 2, 4), (trp_lance_infantry_3, 2, 4), (trp_lance_infantry_5, 2, 4), (trp_lance_archer_2, 2, 4), (trp_lance_infantry_2, 2, 4), (trp_lance_infantry_1, 2, 4)]),

	("horror_reinforcements_b", "{!}kingdom 16 reinforcements b", icon_people_player|pf_label_small, 0, fac_commoners, aggressiveness_0, [(trp_lance_infantry_4, 2, 4), (trp_lance_infantry_3, 2, 4), (trp_lance_infantry_5, 2, 4), (trp_lance_archer_2, 2, 4), (trp_lance_infantry_2, 2, 4), (trp_lance_infantry_1, 2, 4)]),

	("horror_reinforcements_c", "{!}kingdom 16 reinforcements c", icon_people_player|pf_label_small, 0, fac_commoners, aggressiveness_0, [(trp_lance_infantry_4, 2, 4), (trp_lance_infantry_3, 2, 4), (trp_lance_infantry_5, 2, 4), (trp_lance_archer_2, 2, 4), (trp_lance_infantry_2, 2, 4), (trp_lance_infantry_1, 2, 4)]),

	("horror_reinforcements_d", "{!}kingdom 16 reinforcements d", icon_people_player|pf_label_small, 0, fac_commoners, aggressiveness_0, [(trp_lance_infantry_4, 2, 4), (trp_lance_infantry_3, 2, 4), (trp_lance_infantry_5, 2, 4), (trp_lance_archer_2, 2, 4), (trp_lance_archer_5, 2, 4), (trp_lance_archer_2, 2, 4)]),

	("horror_reinforcements_e", "{!}kingdom 16 reinforcements e", icon_people_player|pf_label_small, 0, fac_commoners, aggressiveness_0, [(trp_lance_infantry_4, 2, 4), (trp_lance_infantry_3, 2, 4), (trp_lance_infantry_5, 2, 4), (trp_lance_archer_2, 2, 4), (trp_lance_archer_5, 2, 4), (trp_lance_archer_2, 2, 4)]),

	("horror_reinforcements_f", "{!}kingdom 16 reinforcements f", icon_people_player|pf_label_small, 0, fac_commoners, aggressiveness_0, [(trp_lance_infantry_4, 2, 4), (trp_lance_infantry_3, 2, 4), (trp_lance_infantry_5, 2, 4), (trp_lance_archer_2, 2, 4), (trp_lance_archer_5, 2, 4), (trp_lance_archer_2, 2, 4)]),

	("triarch_reinforcements_a", "{!}kingdom 16 reinforcements a", icon_people_player|pf_label_small, 0, fac_commoners, aggressiveness_0, [(trp_lance_infantry_4, 2, 4), (trp_lance_infantry_3, 2, 4), (trp_lance_infantry_5, 2, 4), (trp_lance_archer_2, 2, 4), (trp_lance_infantry_2, 2, 4), (trp_lance_infantry_1, 2, 4)]),

	("triarch_reinforcements_b", "{!}kingdom 16 reinforcements b", icon_people_player|pf_label_small, 0, fac_commoners, aggressiveness_0, [(trp_lance_infantry_4, 2, 4), (trp_lance_infantry_3, 2, 4), (trp_lance_infantry_5, 2, 4), (trp_lance_archer_2, 2, 4), (trp_lance_infantry_2, 2, 4), (trp_lance_infantry_1, 2, 4)]),

	("triarch_reinforcements_c", "{!}kingdom 16 reinforcements c", icon_people_player|pf_label_small, 0, fac_commoners, aggressiveness_0, [(trp_lance_infantry_4, 2, 4), (trp_lance_infantry_3, 2, 4), (trp_lance_infantry_5, 2, 4), (trp_lance_archer_2, 2, 4), (trp_lance_infantry_2, 2, 4), (trp_lance_infantry_1, 2, 4)]),

	("triarch_reinforcements_d", "{!}kingdom 16 reinforcements d", icon_people_player|pf_label_small, 0, fac_commoners, aggressiveness_0, [(trp_lance_infantry_4, 2, 4), (trp_lance_infantry_3, 2, 4), (trp_lance_infantry_5, 2, 4), (trp_lance_archer_2, 2, 4), (trp_lance_archer_5, 2, 4), (trp_lance_archer_2, 2, 4)]),

	("triarch_reinforcements_e", "{!}kingdom 16 reinforcements e", icon_people_player|pf_label_small, 0, fac_commoners, aggressiveness_0, [(trp_lance_infantry_4, 2, 4), (trp_lance_infantry_3, 2, 4), (trp_lance_infantry_5, 2, 4), (trp_lance_archer_2, 2, 4), (trp_lance_archer_5, 2, 4), (trp_lance_archer_2, 2, 4)]),

	("triarch_reinforcements_f", "{!}kingdom 16 reinforcements f", icon_people_player|pf_label_small, 0, fac_commoners, aggressiveness_0, [(trp_lance_infantry_4, 2, 4), (trp_lance_infantry_3, 2, 4), (trp_lance_infantry_5, 2, 4), (trp_lance_archer_2, 2, 4), (trp_lance_archer_5, 2, 4), (trp_lance_archer_2, 2, 4)]),

	("lance_reinforcements_a", "{!}kingdom 5 reinforcements a", icon_people_player|pf_label_small, 0, fac_commoners, aggressiveness_0, [(trp_lance_infantry_4, 2, 4), (trp_lance_infantry_3, 2, 4), (trp_lance_infantry_5, 2, 4), (trp_lance_archer_2, 2, 4), (trp_lance_infantry_2, 2, 4), (trp_lance_infantry_1, 2, 4)]),

	("lance_reinforcements_b", "{!}kingdom 5 reinforcements b", icon_people_player|pf_label_small, 0, fac_commoners, aggressiveness_0, [(trp_lance_infantry_4, 2, 4), (trp_lance_infantry_3, 2, 4), (trp_lance_infantry_5, 2, 4), (trp_lance_archer_2, 2, 4), (trp_lance_infantry_2, 2, 4), (trp_lance_infantry_1, 2, 4)]),

	("lance_reinforcements_c", "{!}kingdom 5 reinforcements c", icon_people_player|pf_label_small, 0, fac_commoners, aggressiveness_0, [(trp_lance_infantry_4, 2, 4), (trp_lance_infantry_3, 2, 4), (trp_lance_infantry_5, 2, 4), (trp_lance_archer_2, 2, 4), (trp_lance_infantry_2, 2, 4), (trp_lance_infantry_1, 2, 4)]),

	("lance_reinforcements_d", "{!}kingdom 5 reinforcements d", icon_people_player|pf_label_small, 0, fac_commoners, aggressiveness_0, [(trp_lance_infantry_4, 2, 4), (trp_lance_infantry_3, 2, 4), (trp_lance_infantry_5, 2, 4), (trp_lance_archer_2, 2, 4), (trp_lance_archer_5, 2, 4), (trp_lance_archer_2, 2, 4)]),

	("lance_reinforcements_e", "{!}kingdom 5 reinforcements e", icon_people_player|pf_label_small, 0, fac_commoners, aggressiveness_0, [(trp_lance_infantry_4, 2, 4), (trp_lance_infantry_3, 2, 4), (trp_lance_infantry_5, 2, 4), (trp_lance_archer_2, 2, 4), (trp_lance_archer_5, 2, 4), (trp_lance_archer_2, 2, 4)]),

	("lance_reinforcements_f", "{!}kingdom 5 reinforcements f", icon_people_player|pf_label_small, 0, fac_commoners, aggressiveness_0, [(trp_lance_infantry_4, 2, 4), (trp_lance_infantry_3, 2, 4), (trp_lance_infantry_5, 2, 4), (trp_lance_archer_2, 2, 4), (trp_lance_archer_5, 2, 4), (trp_lance_archer_2, 2, 4)]),

	("maze_reinforcements_a", "{!}kingdom 18 reinforcements a", icon_people_player|pf_label_small, 0, fac_commoners, aggressiveness_0, [(trp_lance_infantry_4, 2, 4), (trp_lance_infantry_3, 2, 4), (trp_lance_infantry_5, 2, 4), (trp_lance_archer_2, 2, 4), (trp_lance_infantry_2, 2, 4), (trp_lance_infantry_1, 2, 4)]),

	("maze_reinforcements_b", "{!}kingdom 18 reinforcements b", icon_people_player|pf_label_small, 0, fac_commoners, aggressiveness_0, [(trp_lance_infantry_4, 2, 4), (trp_lance_infantry_3, 2, 4), (trp_lance_infantry_5, 2, 4), (trp_lance_archer_2, 2, 4), (trp_lance_infantry_2, 2, 4), (trp_lance_infantry_1, 2, 4)]),

	("maze_reinforcements_c", "{!}kingdom 18 reinforcements c", icon_people_player|pf_label_small, 0, fac_commoners, aggressiveness_0, [(trp_lance_infantry_4, 2, 4), (trp_lance_infantry_3, 2, 4), (trp_lance_infantry_5, 2, 4), (trp_lance_archer_2, 2, 4), (trp_lance_infantry_2, 2, 4), (trp_lance_infantry_1, 2, 4)]),

	("maze_reinforcements_d", "{!}kingdom 18 reinforcements d", icon_people_player|pf_label_small, 0, fac_commoners, aggressiveness_0, [(trp_lance_infantry_4, 2, 4), (trp_lance_infantry_3, 2, 4), (trp_lance_infantry_5, 2, 4), (trp_lance_archer_2, 2, 4), (trp_lance_archer_5, 2, 4), (trp_lance_archer_2, 2, 4)]),

	("maze_reinforcements_e", "{!}kingdom 18 reinforcements e", icon_people_player|pf_label_small, 0, fac_commoners, aggressiveness_0, [(trp_lance_infantry_4, 2, 4), (trp_lance_infantry_3, 2, 4), (trp_lance_infantry_5, 2, 4), (trp_lance_archer_2, 2, 4), (trp_lance_archer_5, 2, 4), (trp_lance_archer_2, 2, 4)]),

	("maze_reinforcements_f", "{!}kingdom 18 reinforcements f", icon_people_player|pf_label_small, 0, fac_commoners, aggressiveness_0, [(trp_lance_infantry_4, 2, 4), (trp_lance_infantry_3, 2, 4), (trp_lance_infantry_5, 2, 4), (trp_lance_archer_2, 2, 4), (trp_lance_archer_5, 2, 4), (trp_lance_archer_2, 2, 4)]),

	("ibb_reinforcements_a", "{!}kingdom 18 reinforcements a", icon_people_player|pf_label_small, 0, fac_commoners, aggressiveness_0, [(trp_lance_infantry_4, 2, 4), (trp_lance_infantry_3, 2, 4), (trp_lance_infantry_5, 2, 4), (trp_lance_archer_2, 2, 4), (trp_lance_infantry_2, 2, 4), (trp_lance_infantry_1, 2, 4)]),

	("ibb_reinforcements_b", "{!}kingdom 18 reinforcements b", icon_people_player|pf_label_small, 0, fac_commoners, aggressiveness_0, [(trp_lance_infantry_4, 2, 4), (trp_lance_infantry_3, 2, 4), (trp_lance_infantry_5, 2, 4), (trp_lance_archer_2, 2, 4), (trp_lance_infantry_2, 2, 4), (trp_lance_infantry_1, 2, 4)]),

	("ibb_reinforcements_c", "{!}kingdom 18 reinforcements c", icon_people_player|pf_label_small, 0, fac_commoners, aggressiveness_0, [(trp_lance_infantry_4, 2, 4), (trp_lance_infantry_3, 2, 4), (trp_lance_infantry_5, 2, 4), (trp_lance_archer_2, 2, 4), (trp_lance_infantry_2, 2, 4), (trp_lance_infantry_1, 2, 4)]),

	("ibb_reinforcements_d", "{!}kingdom 18 reinforcements d", icon_people_player|pf_label_small, 0, fac_commoners, aggressiveness_0, [(trp_lance_infantry_4, 2, 4), (trp_lance_infantry_3, 2, 4), (trp_lance_infantry_5, 2, 4), (trp_lance_archer_2, 2, 4), (trp_lance_archer_5, 2, 4), (trp_lance_archer_2, 2, 4)]),

	("ibb_reinforcements_e", "{!}kingdom 18 reinforcements e", icon_people_player|pf_label_small, 0, fac_commoners, aggressiveness_0, [(trp_lance_infantry_4, 2, 4), (trp_lance_infantry_3, 2, 4), (trp_lance_infantry_5, 2, 4), (trp_lance_archer_2, 2, 4), (trp_lance_archer_5, 2, 4), (trp_lance_archer_2, 2, 4)]),

	("ibb_reinforcements_f", "{!}kingdom 18 reinforcements f", icon_people_player|pf_label_small, 0, fac_commoners, aggressiveness_0, [(trp_lance_infantry_4, 2, 4), (trp_lance_infantry_3, 2, 4), (trp_lance_infantry_5, 2, 4), (trp_lance_archer_2, 2, 4), (trp_lance_archer_5, 2, 4), (trp_lance_archer_2, 2, 4)]),

	("titan_reinforcements_a", "{!}kingdom 4 reinforcements a", icon_people_player|pf_label_small, 0, fac_commoners, aggressiveness_0, [(trp_lance_infantry_4, 2, 4), (trp_lance_infantry_3, 2, 4), (trp_lance_infantry_5, 2, 4), (trp_lance_archer_2, 2, 4), (trp_lance_infantry_2, 2, 4), (trp_lance_infantry_1, 2, 4)]),

	("titan_reinforcements_b", "{!}kingdom 4 reinforcements b", icon_people_player|pf_label_small, 0, fac_commoners, aggressiveness_0, [(trp_lance_infantry_4, 2, 4), (trp_lance_infantry_3, 2, 4), (trp_lance_infantry_5, 2, 4), (trp_lance_archer_2, 2, 4), (trp_lance_infantry_2, 2, 4), (trp_lance_infantry_1, 2, 4)]),

	("titan_reinforcements_c", "{!}kingdom 4 reinforcements c", icon_people_player|pf_label_small, 0, fac_commoners, aggressiveness_0, [(trp_lance_infantry_4, 2, 4), (trp_lance_infantry_3, 2, 4), (trp_lance_infantry_5, 2, 4), (trp_lance_archer_2, 2, 4), (trp_lance_infantry_2, 2, 4), (trp_lance_infantry_1, 2, 4)]),

	("titan_reinforcements_d", "{!}kingdom 4 reinforcements d", icon_people_player|pf_label_small, 0, fac_commoners, aggressiveness_0, [(trp_lance_infantry_4, 2, 4), (trp_lance_infantry_3, 2, 4), (trp_lance_infantry_5, 2, 4), (trp_lance_archer_2, 2, 4), (trp_lance_archer_5, 2, 4), (trp_lance_archer_2, 2, 4)]),

	("titan_reinforcements_e", "{!}kingdom 4 reinforcements e", icon_people_player|pf_label_small, 0, fac_commoners, aggressiveness_0, [(trp_lance_infantry_4, 2, 4), (trp_lance_infantry_3, 2, 4), (trp_lance_infantry_5, 2, 4), (trp_lance_archer_2, 2, 4), (trp_lance_archer_5, 2, 4), (trp_lance_archer_2, 2, 4)]),

	("titan_reinforcements_f", "{!}kingdom 4 reinforcements f", icon_people_player|pf_label_small, 0, fac_commoners, aggressiveness_0, [(trp_lance_infantry_4, 2, 4), (trp_lance_infantry_3, 2, 4), (trp_lance_infantry_5, 2, 4), (trp_lance_archer_2, 2, 4), (trp_lance_archer_5, 2, 4), (trp_lance_archer_2, 2, 4)]),

	("norvos_reinforcements_a", "{!}kingdom 17 reinforcements a", icon_people_player|pf_label_small, 0, fac_commoners, aggressiveness_0, [(trp_lance_infantry_4, 2, 4), (trp_lance_infantry_3, 2, 4), (trp_lance_infantry_5, 2, 4), (trp_lance_archer_2, 2, 4), (trp_lance_infantry_2, 2, 4), (trp_lance_infantry_1, 2, 4)]),

	("norvos_reinforcements_b", "{!}kingdom 17 reinforcements b", icon_people_player|pf_label_small, 0, fac_commoners, aggressiveness_0, [(trp_lance_infantry_4, 2, 4), (trp_lance_infantry_3, 2, 4), (trp_lance_infantry_5, 2, 4), (trp_lance_archer_2, 2, 4), (trp_lance_infantry_2, 2, 4), (trp_lance_infantry_1, 2, 4)]),

	("norvos_reinforcements_c", "{!}kingdom 17 reinforcements c", icon_people_player|pf_label_small, 0, fac_commoners, aggressiveness_0, [(trp_lance_infantry_4, 2, 4), (trp_lance_infantry_3, 2, 4), (trp_lance_infantry_5, 2, 4), (trp_lance_archer_2, 2, 4), (trp_lance_infantry_2, 2, 4), (trp_lance_infantry_1, 2, 4)]),

	("norvos_reinforcements_d", "{!}kingdom 17 reinforcements d", icon_people_player|pf_label_small, 0, fac_commoners, aggressiveness_0, [(trp_lance_infantry_4, 2, 4), (trp_lance_infantry_3, 2, 4), (trp_lance_infantry_5, 2, 4), (trp_lance_archer_2, 2, 4), (trp_lance_archer_5, 2, 4), (trp_lance_archer_2, 2, 4)]),

	("norvos_reinforcements_e", "{!}kingdom 17 reinforcements e", icon_people_player|pf_label_small, 0, fac_commoners, aggressiveness_0, [(trp_lance_infantry_4, 2, 4), (trp_lance_infantry_3, 2, 4), (trp_lance_infantry_5, 2, 4), (trp_lance_archer_2, 2, 4), (trp_lance_archer_5, 2, 4), (trp_lance_archer_2, 2, 4)]),

	("norvos_reinforcements_f", "{!}kingdom 17 reinforcements f", icon_people_player|pf_label_small, 0, fac_commoners, aggressiveness_0, [(trp_lance_infantry_4, 2, 4), (trp_lance_infantry_3, 2, 4), (trp_lance_infantry_5, 2, 4), (trp_lance_archer_2, 2, 4), (trp_lance_archer_5, 2, 4), (trp_lance_archer_2, 2, 4)]),

	("rose_reinforcements_a", "{!}kingdom 12 reinforcements a", icon_people_player|pf_label_small, 0, fac_commoners, aggressiveness_0, [(trp_lance_infantry_4, 2, 4), (trp_lance_infantry_3, 2, 4), (trp_lance_infantry_5, 2, 4), (trp_lance_archer_2, 2, 4), (trp_lance_infantry_2, 2, 4), (trp_lance_infantry_1, 2, 4)]),

	("rose_reinforcements_b", "{!}kingdom 12 reinforcements b", icon_people_player|pf_label_small, 0, fac_commoners, aggressiveness_0, [(trp_lance_infantry_4, 2, 4), (trp_lance_infantry_3, 2, 4), (trp_lance_infantry_5, 2, 4), (trp_lance_archer_2, 2, 4), (trp_lance_infantry_2, 2, 4), (trp_lance_infantry_1, 2, 4)]),

	("rose_reinforcements_c", "{!}kingdom 12 reinforcements c", icon_people_player|pf_label_small, 0, fac_commoners, aggressiveness_0, [(trp_lance_infantry_4, 2, 4), (trp_lance_infantry_3, 2, 4), (trp_lance_infantry_5, 2, 4), (trp_lance_archer_2, 2, 4), (trp_lance_infantry_2, 2, 4), (trp_lance_infantry_1, 2, 4)]),

	("rose_reinforcements_d", "{!}kingdom 12 reinforcements d", icon_people_player|pf_label_small, 0, fac_commoners, aggressiveness_0, [(trp_lance_infantry_4, 2, 4), (trp_lance_infantry_3, 2, 4), (trp_lance_infantry_5, 2, 4), (trp_lance_archer_2, 2, 4), (trp_lance_archer_5, 2, 4), (trp_lance_archer_2, 2, 4)]),

	("rose_reinforcements_e", "{!}kingdom 12 reinforcements e", icon_people_player|pf_label_small, 0, fac_commoners, aggressiveness_0, [(trp_lance_infantry_4, 2, 4), (trp_lance_infantry_3, 2, 4), (trp_lance_infantry_5, 2, 4), (trp_lance_archer_2, 2, 4), (trp_lance_archer_5, 2, 4), (trp_lance_archer_2, 2, 4)]),

	("rose_reinforcements_f", "{!}kingdom 12 reinforcements f", icon_people_player|pf_label_small, 0, fac_commoners, aggressiveness_0, [(trp_lance_infantry_4, 2, 4), (trp_lance_infantry_3, 2, 4), (trp_lance_infantry_5, 2, 4), (trp_lance_archer_2, 2, 4), (trp_lance_archer_5, 2, 4), (trp_lance_archer_2, 2, 4)]),

	("dothraki_reinforcements_a", "{!}kingdom 12 reinforcements a", icon_people_player|pf_label_small, 0, fac_commoners, aggressiveness_0, [(trp_lance_infantry_4, 2, 4), (trp_lance_infantry_3, 2, 4), (trp_lance_infantry_5, 2, 4), (trp_lance_archer_2, 2, 4), (trp_lance_infantry_2, 2, 4), (trp_lance_infantry_1, 2, 4)]),

	("dothraki_reinforcements_b", "{!}kingdom 12 reinforcements b", icon_people_player|pf_label_small, 0, fac_commoners, aggressiveness_0, [(trp_lance_infantry_4, 2, 4), (trp_lance_infantry_3, 2, 4), (trp_lance_infantry_5, 2, 4), (trp_lance_archer_2, 2, 4), (trp_lance_infantry_2, 2, 4), (trp_lance_infantry_1, 2, 4)]),

	("dothraki_reinforcements_c", "{!}kingdom 12 reinforcements c", icon_people_player|pf_label_small, 0, fac_commoners, aggressiveness_0, [(trp_lance_infantry_4, 2, 4), (trp_lance_infantry_3, 2, 4), (trp_lance_infantry_5, 2, 4), (trp_lance_archer_2, 2, 4), (trp_lance_infantry_2, 2, 4), (trp_lance_infantry_1, 2, 4)]),

	("dothraki_reinforcements_d", "{!}kingdom 12 reinforcements d", icon_people_player|pf_label_small, 0, fac_commoners, aggressiveness_0, [(trp_lance_infantry_4, 2, 4), (trp_lance_infantry_3, 2, 4), (trp_lance_infantry_5, 2, 4), (trp_lance_archer_2, 2, 4), (trp_lance_archer_5, 2, 4), (trp_lance_archer_2, 2, 4)]),

	("dothraki_reinforcements_e", "{!}kingdom 12 reinforcements e", icon_people_player|pf_label_small, 0, fac_commoners, aggressiveness_0, [(trp_lance_infantry_4, 2, 4), (trp_lance_infantry_3, 2, 4), (trp_lance_infantry_5, 2, 4), (trp_lance_archer_2, 2, 4), (trp_lance_archer_5, 2, 4), (trp_lance_archer_2, 2, 4)]),

	("dothraki_reinforcements_f", "{!}kingdom 12 reinforcements f", icon_people_player|pf_label_small, 0, fac_commoners, aggressiveness_0, [(trp_lance_infantry_4, 2, 4), (trp_lance_infantry_3, 2, 4), (trp_lance_infantry_5, 2, 4), (trp_lance_archer_2, 2, 4), (trp_lance_archer_5, 2, 4), (trp_lance_archer_2, 2, 4)]),

	("summer_reinforcements_a", "{!}kingdom 15 reinforcements a", icon_people_player|pf_label_small, 0, fac_commoners, aggressiveness_0, [(trp_lance_infantry_4, 2, 4), (trp_lance_infantry_3, 2, 4), (trp_lance_infantry_5, 2, 4), (trp_lance_archer_2, 2, 4), (trp_lance_infantry_2, 2, 4), (trp_lance_infantry_1, 2, 4)]),

	("summer_reinforcements_b", "{!}kingdom 15 reinforcements b", icon_people_player|pf_label_small, 0, fac_commoners, aggressiveness_0, [(trp_lance_infantry_4, 2, 4), (trp_lance_infantry_3, 2, 4), (trp_lance_infantry_5, 2, 4), (trp_lance_archer_2, 2, 4), (trp_lance_infantry_2, 2, 4), (trp_lance_infantry_1, 2, 4)]),

	("summer_reinforcements_c", "{!}kingdom 15 reinforcements c", icon_people_player|pf_label_small, 0, fac_commoners, aggressiveness_0, [(trp_lance_infantry_4, 2, 4), (trp_lance_infantry_3, 2, 4), (trp_lance_infantry_5, 2, 4), (trp_lance_archer_2, 2, 4), (trp_lance_infantry_2, 2, 4), (trp_lance_infantry_1, 2, 4)]),

	("summer_reinforcements_d", "{!}kingdom 15 reinforcements d", icon_people_player|pf_label_small, 0, fac_commoners, aggressiveness_0, [(trp_lance_infantry_4, 2, 4), (trp_lance_infantry_3, 2, 4), (trp_lance_infantry_5, 2, 4), (trp_lance_archer_2, 2, 4), (trp_lance_archer_5, 2, 4), (trp_lance_archer_2, 2, 4)]),

	("summer_reinforcements_e", "{!}kingdom 15 reinforcements e", icon_people_player|pf_label_small, 0, fac_commoners, aggressiveness_0, [(trp_lance_infantry_4, 2, 4), (trp_lance_infantry_3, 2, 4), (trp_lance_infantry_5, 2, 4), (trp_lance_archer_2, 2, 4), (trp_lance_archer_5, 2, 4), (trp_lance_archer_2, 2, 4)]),

	("summer_reinforcements_f", "{!}kingdom 15 reinforcements f", icon_people_player|pf_label_small, 0, fac_commoners, aggressiveness_0, [(trp_lance_infantry_4, 2, 4), (trp_lance_infantry_3, 2, 4), (trp_lance_infantry_5, 2, 4), (trp_lance_archer_2, 2, 4), (trp_lance_archer_5, 2, 4), (trp_lance_archer_2, 2, 4)]),

	("maiden_reinforcements_a", "{!}kingdom 15 reinforcements a", icon_people_player|pf_label_small, 0, fac_commoners, aggressiveness_0, [(trp_lance_infantry_4, 2, 4), (trp_lance_infantry_3, 2, 4), (trp_lance_infantry_5, 2, 4), (trp_lance_archer_2, 2, 4), (trp_lance_infantry_2, 2, 4), (trp_lance_infantry_1, 2, 4)]),

	("maiden_reinforcements_b", "{!}kingdom 15 reinforcements b", icon_people_player|pf_label_small, 0, fac_commoners, aggressiveness_0, [(trp_lance_infantry_4, 2, 4), (trp_lance_infantry_3, 2, 4), (trp_lance_infantry_5, 2, 4), (trp_lance_archer_2, 2, 4), (trp_lance_infantry_2, 2, 4), (trp_lance_infantry_1, 2, 4)]),

	("maiden_reinforcements_c", "{!}kingdom 15 reinforcements c", icon_people_player|pf_label_small, 0, fac_commoners, aggressiveness_0, [(trp_lance_infantry_4, 2, 4), (trp_lance_infantry_3, 2, 4), (trp_lance_infantry_5, 2, 4), (trp_lance_archer_2, 2, 4), (trp_lance_infantry_2, 2, 4), (trp_lance_infantry_1, 2, 4)]),

	("maiden_reinforcements_d", "{!}kingdom 15 reinforcements d", icon_people_player|pf_label_small, 0, fac_commoners, aggressiveness_0, [(trp_lance_infantry_4, 2, 4), (trp_lance_infantry_3, 2, 4), (trp_lance_infantry_5, 2, 4), (trp_lance_archer_2, 2, 4), (trp_lance_archer_5, 2, 4), (trp_lance_archer_2, 2, 4)]),

	("maiden_reinforcements_e", "{!}kingdom 15 reinforcements e", icon_people_player|pf_label_small, 0, fac_commoners, aggressiveness_0, [(trp_lance_infantry_4, 2, 4), (trp_lance_infantry_3, 2, 4), (trp_lance_infantry_5, 2, 4), (trp_lance_archer_2, 2, 4), (trp_lance_archer_5, 2, 4), (trp_lance_archer_2, 2, 4)]),

	("maiden_reinforcements_f", "{!}kingdom 15 reinforcements f", icon_people_player|pf_label_small, 0, fac_commoners, aggressiveness_0, [(trp_lance_infantry_4, 2, 4), (trp_lance_infantry_3, 2, 4), (trp_lance_infantry_5, 2, 4), (trp_lance_archer_2, 2, 4), (trp_lance_archer_5, 2, 4), (trp_lance_archer_2, 2, 4)]),

	("stormbreaker_reinforcements_a", "{!}kingdom 13 reinforcements a", icon_people_player|pf_label_small, 0, fac_commoners, aggressiveness_0, [(trp_lance_infantry_4, 2, 4), (trp_lance_infantry_3, 2, 4), (trp_lance_infantry_5, 2, 4), (trp_lance_archer_2, 2, 4), (trp_lance_infantry_2, 2, 4), (trp_lance_infantry_1, 2, 4)]),

	("stormbreaker_reinforcements_b", "{!}kingdom 13 reinforcements b", icon_people_player|pf_label_small, 0, fac_commoners, aggressiveness_0, [(trp_lance_infantry_4, 2, 4), (trp_lance_infantry_3, 2, 4), (trp_lance_infantry_5, 2, 4), (trp_lance_archer_2, 2, 4), (trp_lance_infantry_2, 2, 4), (trp_lance_infantry_1, 2, 4)]),

	("stormbreaker_reinforcements_c", "{!}kingdom 13 reinforcements c", icon_people_player|pf_label_small, 0, fac_commoners, aggressiveness_0, [(trp_lance_infantry_4, 2, 4), (trp_lance_infantry_3, 2, 4), (trp_lance_infantry_5, 2, 4), (trp_lance_archer_2, 2, 4), (trp_lance_infantry_2, 2, 4), (trp_lance_infantry_1, 2, 4)]),

	("stormbreaker_reinforcements_d", "{!}kingdom 13 reinforcements d", icon_people_player|pf_label_small, 0, fac_commoners, aggressiveness_0, [(trp_lance_infantry_4, 2, 4), (trp_lance_infantry_3, 2, 4), (trp_lance_infantry_5, 2, 4), (trp_lance_archer_2, 2, 4), (trp_lance_archer_5, 2, 4), (trp_lance_archer_2, 2, 4)]),

	("stormbreaker_reinforcements_e", "{!}kingdom 13 reinforcements e", icon_people_player|pf_label_small, 0, fac_commoners, aggressiveness_0, [(trp_lance_infantry_4, 2, 4), (trp_lance_infantry_3, 2, 4), (trp_lance_infantry_5, 2, 4), (trp_lance_archer_2, 2, 4), (trp_lance_archer_5, 2, 4), (trp_lance_archer_2, 2, 4)]),

	("stormbreaker_reinforcements_f", "{!}kingdom 13 reinforcements f", icon_people_player|pf_label_small, 0, fac_commoners, aggressiveness_0, [(trp_lance_infantry_4, 2, 4), (trp_lance_infantry_3, 2, 4), (trp_lance_infantry_5, 2, 4), (trp_lance_archer_2, 2, 4), (trp_lance_archer_5, 2, 4), (trp_lance_archer_2, 2, 4)]),

	("corsair_reinforcements_a", "{!}kingdom 13 reinforcements a", icon_people_player|pf_label_small, 0, fac_commoners, aggressiveness_0, [(trp_lance_infantry_4, 2, 4), (trp_lance_infantry_3, 2, 4), (trp_lance_infantry_5, 2, 4), (trp_lance_archer_2, 2, 4), (trp_lance_infantry_2, 2, 4), (trp_lance_infantry_1, 2, 4)]),

	("corsair_reinforcements_b", "{!}kingdom 13 reinforcements b", icon_people_player|pf_label_small, 0, fac_commoners, aggressiveness_0, [(trp_lance_infantry_4, 2, 4), (trp_lance_infantry_3, 2, 4), (trp_lance_infantry_5, 2, 4), (trp_lance_archer_2, 2, 4), (trp_lance_infantry_2, 2, 4), (trp_lance_infantry_1, 2, 4)]),

	("corsair_reinforcements_c", "{!}kingdom 13 reinforcements c", icon_people_player|pf_label_small, 0, fac_commoners, aggressiveness_0, [(trp_lance_infantry_4, 2, 4), (trp_lance_infantry_3, 2, 4), (trp_lance_infantry_5, 2, 4), (trp_lance_archer_2, 2, 4), (trp_lance_infantry_2, 2, 4), (trp_lance_infantry_1, 2, 4)]),

	("corsair_reinforcements_d", "{!}kingdom 13 reinforcements d", icon_people_player|pf_label_small, 0, fac_commoners, aggressiveness_0, [(trp_lance_infantry_4, 2, 4), (trp_lance_infantry_3, 2, 4), (trp_lance_infantry_5, 2, 4), (trp_lance_archer_2, 2, 4), (trp_lance_archer_5, 2, 4), (trp_lance_archer_2, 2, 4)]),

	("corsair_reinforcements_e", "{!}kingdom 13 reinforcements e", icon_people_player|pf_label_small, 0, fac_commoners, aggressiveness_0, [(trp_lance_infantry_4, 2, 4), (trp_lance_infantry_3, 2, 4), (trp_lance_infantry_5, 2, 4), (trp_lance_archer_2, 2, 4), (trp_lance_archer_5, 2, 4), (trp_lance_archer_2, 2, 4)]),

	("corsair_reinforcements_f", "{!}kingdom 13 reinforcements f", icon_people_player|pf_label_small, 0, fac_commoners, aggressiveness_0, [(trp_lance_infantry_4, 2, 4), (trp_lance_infantry_3, 2, 4), (trp_lance_infantry_5, 2, 4), (trp_lance_archer_2, 2, 4), (trp_lance_archer_5, 2, 4), (trp_lance_archer_2, 2, 4)]),

	("thenn_reinforcements_a", "{!}kingdom 21 reinforcements a", icon_people_player|pf_label_small, 0, fac_commoners, aggressiveness_0, [(trp_sarranid_n_millet22, 2, 4), (trp_sarranid_n_ajam22, 2, 4), (trp_sarranid_n_cemaat22, 2, 4), (trp_sarranid_n_cemaat22, 2, 4), (trp_sarranid_n_yeniceri22, 2, 4), (trp_sarranid_n_kapikula22, 2, 4)]),

	("thenn_reinforcements_b", "{!}kingdom 21 reinforcements b", icon_people_player|pf_label_small, 0, fac_commoners, aggressiveness_0, [(trp_sarranid_n_millet22, 2, 4), (trp_sarranid_n_ajam22, 2, 4), (trp_sarranid_n_cemaat22, 2, 4), (trp_sarranid_n_cemaat22, 2, 4), (trp_sarranid_n_yeniceri22, 2, 4), (trp_sarranid_n_kapikula22, 2, 4)]),

	("thenn_reinforcements_c", "{!}kingdom 21 reinforcements c", icon_people_player|pf_label_small, 0, fac_commoners, aggressiveness_0, [(trp_sarranid_n_uluteci22, 2, 4), (trp_sarranid_n_ajam22, 2, 4), (trp_sarranid_n_cemaat22, 2, 4), (trp_sarranid_n_cemaat22, 2, 4), (trp_sarranid_n_yeniceri22, 2, 4), (trp_sarranid_n_kapikula22, 2, 4)]),

	("thenn_reinforcements_d", "{!}kingdom 21 reinforcements d", icon_people_player|pf_label_small, 0, fac_commoners, aggressiveness_0, [(trp_sarranid_n_uluteci22, 2, 4), (trp_sarranid_n_ajam22, 2, 4), (trp_sarranid_n_cemaat22, 2, 4), (trp_sarranid_n_jebelus22, 2, 4), (trp_sarranid_n_yeniceri22, 2, 4), (trp_sarranid_n_kapikula22, 2, 4)]),

	("thenn_reinforcements_e", "{!}kingdom 21 reinforcements e", icon_people_player|pf_label_small, 0, fac_commoners, aggressiveness_0, [(trp_sarranid_n_uluteci22, 2, 4), (trp_sarranid_n_ajam22, 2, 4), (trp_sarranid_n_cemaat22, 2, 4), (trp_sarranid_n_jebelus22, 2, 4), (trp_sarranid_n_yeniceri22, 2, 4), (trp_sarranid_n_kapikula22, 2, 4)]),

	("thenn_reinforcements_f", "{!}kingdom 21 reinforcements f", icon_people_player|pf_label_small, 0, fac_commoners, aggressiveness_0, [(trp_sarranid_n_uluteci22, 2, 4), (trp_sarranid_n_ajam22, 2, 4), (trp_sarranid_n_cemaat22, 2, 4), (trp_sarranid_n_jebelus22, 2, 4), (trp_sarranid_n_yeniceri22, 2, 4), (trp_sarranid_n_kapikula22, 2, 4)]),

	("drumm_reinforcements_a", "{!}kingdom 11 reinforcements a", icon_people_player|pf_label_small, 0, fac_commoners, aggressiveness_0, [(trp_sarranid_n_millet11, 2, 4), (trp_sarranid_n_ajam11, 2, 4), (trp_sarranid_n_cemaat11, 2, 4), (trp_sarranid_n_jebelus11, 2, 4), (trp_sarranid_n_yerliyya11, 2, 4), (trp_sarranid_n_cemaat11, 1, 2)]),

	("drumm_reinforcements_b", "{!}kingdom 11 reinforcements b", icon_people_player|pf_label_small, 0, fac_commoners, aggressiveness_0, [(trp_sarranid_n_millet11, 2, 4), (trp_sarranid_n_ajam11, 2, 4), (trp_sarranid_n_cemaat11, 2, 4), (trp_sarranid_n_jebelus11, 2, 4), (trp_sarranid_n_yerliyya11, 2, 4), (trp_sarranid_n_cemaat11, 1, 2)]),

	("drumm_reinforcements_c", "{!}kingdom 11 reinforcements c", icon_people_player|pf_label_small, 0, fac_commoners, aggressiveness_0, [(trp_sarranid_n_millet11, 2, 4), (trp_sarranid_n_ajam11, 2, 4), (trp_sarranid_n_cemaat11, 2, 4), (trp_sarranid_n_yerliyya11, 2, 4), (trp_sarranid_n_yerliyya11, 2, 4), (trp_sarranid_n_cemaat11, 1, 2)]),

	("drumm_reinforcements_d", "{!}kingdom 11 reinforcements d", icon_people_player|pf_label_small, 0, fac_commoners, aggressiveness_0, [(trp_sarranid_n_ajam11, 2, 4), (trp_sarranid_n_yeniceri11, 2, 4), (trp_sarranid_n_kapikula11, 2, 4), (trp_sarranid_n_uluteci11, 2, 4), (trp_sarranid_n_uluteci11, 2, 4), (trp_sarranid_n_cemaat11, 1, 2)]),

	("drumm_reinforcements_e", "{!}kingdom 11 reinforcements e", icon_people_player|pf_label_small, 0, fac_commoners, aggressiveness_0, [(trp_sarranid_n_millet11, 2, 4), (trp_sarranid_n_ajam11, 2, 4), (trp_sarranid_n_cemaat11, 2, 4), (trp_sarranid_n_yerliyya11, 2, 4), (trp_sarranid_n_yerliyya11, 2, 4), (trp_sarranid_n_cemaat11, 1, 2)]),

	("drumm_reinforcements_f", "{!}kingdom 11 reinforcements f", icon_people_player|pf_label_small, 0, fac_commoners, aggressiveness_0, [(trp_sarranid_n_ajam11, 2, 4), (trp_sarranid_n_yeniceri11, 2, 4), (trp_sarranid_n_kapikula11, 2, 4), (trp_sarranid_n_uluteci11, 2, 4), (trp_sarranid_n_uluteci11, 2, 4), (trp_sarranid_n_cemaat11, 1, 2)]),

	("harlaw_reinforcements_a", "{!}kingdom 11 reinforcements a", icon_people_player|pf_label_small, 0, fac_commoners, aggressiveness_0, [(trp_sarranid_n_millet11, 2, 4), (trp_sarranid_n_ajam11, 2, 4), (trp_sarranid_n_cemaat11, 2, 4), (trp_sarranid_n_jebelus11, 2, 4), (trp_sarranid_n_yerliyya11, 2, 4), (trp_sarranid_n_cemaat11, 1, 2)]),

	("harlaw_reinforcements_b", "{!}kingdom 11 reinforcements b", icon_people_player|pf_label_small, 0, fac_commoners, aggressiveness_0, [(trp_sarranid_n_millet11, 2, 4), (trp_sarranid_n_ajam11, 2, 4), (trp_sarranid_n_cemaat11, 2, 4), (trp_sarranid_n_jebelus11, 2, 4), (trp_sarranid_n_yerliyya11, 2, 4), (trp_sarranid_n_cemaat11, 1, 2)]),

	("harlaw_reinforcements_c", "{!}kingdom 11 reinforcements c", icon_people_player|pf_label_small, 0, fac_commoners, aggressiveness_0, [(trp_sarranid_n_millet11, 2, 4), (trp_sarranid_n_ajam11, 2, 4), (trp_sarranid_n_cemaat11, 2, 4), (trp_sarranid_n_yerliyya11, 2, 4), (trp_sarranid_n_yerliyya11, 2, 4), (trp_sarranid_n_cemaat11, 1, 2)]),

	("harlaw_reinforcements_d", "{!}kingdom 11 reinforcements d", icon_people_player|pf_label_small, 0, fac_commoners, aggressiveness_0, [(trp_sarranid_n_ajam11, 2, 4), (trp_sarranid_n_yeniceri11, 2, 4), (trp_sarranid_n_kapikula11, 2, 4), (trp_sarranid_n_uluteci11, 2, 4), (trp_sarranid_n_uluteci11, 2, 4), (trp_sarranid_n_cemaat11, 1, 2)]),

	("harlaw_reinforcements_e", "{!}kingdom 11 reinforcements e", icon_people_player|pf_label_small, 0, fac_commoners, aggressiveness_0, [(trp_sarranid_n_millet11, 2, 4), (trp_sarranid_n_ajam11, 2, 4), (trp_sarranid_n_cemaat11, 2, 4), (trp_sarranid_n_yerliyya11, 2, 4), (trp_sarranid_n_yerliyya11, 2, 4), (trp_sarranid_n_cemaat11, 1, 2)]),

	("harlaw_reinforcements_f", "{!}kingdom 11 reinforcements f", icon_people_player|pf_label_small, 0, fac_commoners, aggressiveness_0, [(trp_sarranid_n_ajam11, 2, 4), (trp_sarranid_n_yeniceri11, 2, 4), (trp_sarranid_n_kapikula11, 2, 4), (trp_sarranid_n_uluteci11, 2, 4), (trp_sarranid_n_uluteci11, 2, 4), (trp_sarranid_n_cemaat11, 1, 2)]),

	("swann_reinforcements_a", "{!}kingdom 1 reinforcements a", icon_people_player|pf_label_small, 0, fac_commoners, aggressiveness_0, [(trp_sarranid_n_cemaat1, 2, 4), (trp_sarranid_n_ajam1, 2, 4), (trp_sarranid_n_cemaat1, 2, 4), (trp_sarranid_n_jebelus1, 2, 4), (trp_stonehelm_knight, 2, 4), (trp_stonehelm_knight, 1, 2)]),

	("swann_reinforcements_b", "{!}kingdom 1 reinforcements b", icon_people_player|pf_label_small, 0, fac_commoners, aggressiveness_0, [(trp_sarranid_n_millet1, 2, 4), (trp_sarranid_n_ajam1, 2, 4), (trp_sarranid_n_cemaat1, 2, 4), (trp_sarranid_n_jebelus1, 2, 4), (trp_stonehelm_knight, 2, 4), (trp_stonehelm_knight, 1, 2)]),

	("swann_reinforcements_c", "{!}kingdom 1 reinforcements c", icon_people_player|pf_label_small, 0, fac_commoners, aggressiveness_0, [(trp_sarranid_n_millet1, 2, 4), (trp_sarranid_n_ajam1, 2, 4), (trp_sarranid_n_cemaat1, 2, 4), (trp_sarranid_n_jebelus1, 2, 4), (trp_sarranid_n_yerliyya1, 2, 4), (trp_sarranid_n_cemaat1, 1, 2)]),

	("swann_reinforcements_d", "{!}kingdom 1 reinforcements d", icon_people_player|pf_label_small, 0, fac_commoners, aggressiveness_0, [(trp_sarranid_n_millet1, 2, 4), (trp_stormlands_troop_1, 2, 4), (trp_sarranid_n_yeniceri1, 2, 4), (trp_sarranid_n_kapikula1, 2, 4), (trp_sarranid_n_uluteci1, 2, 4), (trp_sarranid_n_cemaat1, 1, 2)]),

	("swann_reinforcements_e", "{!}kingdom 1 reinforcements e", icon_people_player|pf_label_small, 0, fac_commoners, aggressiveness_0, [(trp_sarranid_n_millet1, 2, 4), (trp_sarranid_n_ajam1, 2, 4), (trp_sarranid_n_cemaat1, 2, 4), (trp_sarranid_n_jebelus1, 2, 4), (trp_sarranid_n_yerliyya1, 2, 4), (trp_sarranid_n_cemaat1, 1, 2)]),

	("swann_reinforcements_f", "{!}kingdom 1 reinforcements f", icon_people_player|pf_label_small, 0, fac_commoners, aggressiveness_0, [(trp_sarranid_n_garip1, 2, 4), (trp_stormlands_troop_1, 2, 4), (trp_sarranid_n_yeniceri1, 2, 4), (trp_sarranid_n_kapikula1, 2, 4), (trp_sarranid_n_uluteci1, 2, 4), (trp_sarranid_n_cemaat1, 1, 2)]),

	("caron_reinforcements_a", "{!}kingdom 1 reinforcements a", icon_people_player|pf_label_small, 0, fac_commoners, aggressiveness_0, [(trp_sarranid_n_cemaat1, 2, 4), (trp_sarranid_n_ajam1, 2, 4), (trp_sarranid_n_cemaat1, 2, 4), (trp_sarranid_n_jebelus1, 2, 4), (trp_marcher_longbowman, 2, 4), (trp_marcher_longbowman, 1, 2)]),

	("caron_reinforcements_b", "{!}kingdom 1 reinforcements b", icon_people_player|pf_label_small, 0, fac_commoners, aggressiveness_0, [(trp_sarranid_n_millet1, 2, 4), (trp_sarranid_n_ajam1, 2, 4), (trp_sarranid_n_cemaat1, 2, 4), (trp_sarranid_n_jebelus1, 2, 4), (trp_marcher_longbowman, 2, 4), (trp_marcher_longbowman, 1, 2)]),

	("caron_reinforcements_c", "{!}kingdom 1 reinforcements c", icon_people_player|pf_label_small, 0, fac_commoners, aggressiveness_0, [(trp_sarranid_n_millet1, 2, 4), (trp_sarranid_n_ajam1, 2, 4), (trp_sarranid_n_cemaat1, 2, 4), (trp_sarranid_n_jebelus1, 2, 4), (trp_sarranid_n_yerliyya1, 2, 4), (trp_sarranid_n_cemaat1, 1, 2)]),

	("caron_reinforcements_d", "{!}kingdom 1 reinforcements d", icon_people_player|pf_label_small, 0, fac_commoners, aggressiveness_0, [(trp_sarranid_n_millet1, 2, 4), (trp_stormlands_troop_1, 2, 4), (trp_sarranid_n_yeniceri1, 2, 4), (trp_sarranid_n_kapikula1, 2, 4), (trp_sarranid_n_uluteci1, 2, 4), (trp_sarranid_n_cemaat1, 1, 2)]),

	("caron_reinforcements_e", "{!}kingdom 1 reinforcements e", icon_people_player|pf_label_small, 0, fac_commoners, aggressiveness_0, [(trp_sarranid_n_millet1, 2, 4), (trp_sarranid_n_ajam1, 2, 4), (trp_sarranid_n_cemaat1, 2, 4), (trp_sarranid_n_jebelus1, 2, 4), (trp_sarranid_n_yerliyya1, 2, 4), (trp_sarranid_n_cemaat1, 1, 2)]),

	("caron_reinforcements_f", "{!}kingdom 1 reinforcements f", icon_people_player|pf_label_small, 0, fac_commoners, aggressiveness_0, [(trp_sarranid_n_garip1, 2, 4), (trp_stormlands_troop_1, 2, 4), (trp_sarranid_n_yeniceri1, 2, 4), (trp_sarranid_n_kapikula1, 2, 4), (trp_sarranid_n_uluteci1, 2, 4), (trp_sarranid_n_cemaat1, 1, 2)]),

	("manderly_reinforcements_a", "{!}kingdom 2 reinforcements a", icon_people_player|pf_label_small, 0, fac_commoners, aggressiveness_0, [(trp_sarranid_n_millet2, 2, 4), (trp_sarranid_n_ajam2, 2, 4), (trp_sarranid_n_cemaat2, 2, 4), (trp_white_harbor_knight, 2, 4), (trp_white_harbor_knight, 2, 4), (trp_white_harbor_knight, 1, 2)]),

	("manderly_reinforcements_b", "{!}kingdom 2 reinforcements b", icon_people_player|pf_label_small, 0, fac_commoners, aggressiveness_0, [(trp_sarranid_n_millet2, 2, 4), (trp_sarranid_n_ajam2, 2, 4), (trp_sarranid_n_cemaat2, 2, 4), (trp_sarranid_n_jebelus2, 2, 4), (trp_white_harbor_knight, 2, 4), (trp_white_harbor_knight, 1, 2)]),

	("manderly_reinforcements_c", "{!}kingdom 2 reinforcements c", icon_people_player|pf_label_small, 0, fac_commoners, aggressiveness_0, [(trp_sarranid_n_millet2, 2, 4), (trp_sarranid_n_ajam2, 2, 4), (trp_sarranid_n_cemaat2, 2, 4), (trp_sarranid_n_jebelus2, 2, 4), (trp_sarranid_n_yerliyya2, 2, 4), (trp_sarranid_n_cemaat2, 1, 2)]),

	("manderly_reinforcements_d", "{!}kingdom 2 reinforcements d", icon_people_player|pf_label_small, 0, fac_commoners, aggressiveness_0, [(trp_sarranid_n_garip2, 2, 4), (trp_northern_troop_1, 2, 4), (trp_sarranid_n_yeniceri2, 2, 4), (trp_sarranid_n_kapikula2, 2, 4), (trp_sarranid_n_uluteci2, 2, 4), (trp_sarranid_n_cemaat2, 1, 2)]),

	("manderly_reinforcements_e", "{!}kingdom 2 reinforcements e", icon_people_player|pf_label_small, 0, fac_commoners, aggressiveness_0, [(trp_sarranid_n_millet2, 2, 4), (trp_sarranid_n_ajam2, 2, 4), (trp_sarranid_n_cemaat2, 2, 4), (trp_sarranid_n_jebelus2, 2, 4), (trp_sarranid_n_yerliyya2, 2, 4), (trp_sarranid_n_cemaat2, 1, 2)]),

	("manderly_reinforcements_f", "{!}kingdom 2 reinforcements f", icon_people_player|pf_label_small, 0, fac_commoners, aggressiveness_0, [(trp_sarranid_n_garip2, 2, 4), (trp_northern_troop_1, 2, 4), (trp_sarranid_n_yeniceri2, 2, 4), (trp_sarranid_n_kapikula2, 2, 4), (trp_sarranid_n_uluteci2, 2, 4), (trp_sarranid_n_cemaat2, 1, 2)]),

	("umber_reinforcements_a", "{!}kingdom 2 reinforcements a", icon_people_player|pf_label_small, 0, fac_commoners, aggressiveness_0, [(trp_sarranid_n_millet2, 2, 4), (trp_sarranid_n_ajam2, 2, 4), (trp_sarranid_n_cemaat2, 2, 4), (trp_sarranid_n_jebelus2, 2, 4), (trp_rill_lances, 2, 4), (trp_rill_lances, 1, 2)]),

	("umber_reinforcements_b", "{!}kingdom 2 reinforcements b", icon_people_player|pf_label_small, 0, fac_commoners, aggressiveness_0, [(trp_sarranid_n_millet2, 2, 4), (trp_sarranid_n_ajam2, 2, 4), (trp_sarranid_n_cemaat2, 2, 4), (trp_sarranid_n_jebelus2, 2, 4), (trp_rill_lances, 2, 4), (trp_rill_lances, 1, 2)]),

	("umber_reinforcements_c", "{!}kingdom 2 reinforcements c", icon_people_player|pf_label_small, 0, fac_commoners, aggressiveness_0, [(trp_sarranid_n_millet2, 2, 4), (trp_sarranid_n_ajam2, 2, 4), (trp_sarranid_n_cemaat2, 2, 4), (trp_sarranid_n_jebelus2, 2, 4), (trp_sarranid_n_yerliyya2, 2, 4), (trp_sarranid_n_cemaat2, 1, 2)]),

	("umber_reinforcements_d", "{!}kingdom 2 reinforcements d", icon_people_player|pf_label_small, 0, fac_commoners, aggressiveness_0, [(trp_sarranid_n_garip2, 2, 4), (trp_northern_troop_1, 2, 4), (trp_sarranid_n_yeniceri2, 2, 4), (trp_sarranid_n_kapikula2, 2, 4), (trp_sarranid_n_uluteci2, 2, 4), (trp_sarranid_n_cemaat2, 1, 2)]),

	("umber_reinforcements_e", "{!}kingdom 2 reinforcements e", icon_people_player|pf_label_small, 0, fac_commoners, aggressiveness_0, [(trp_sarranid_n_millet2, 2, 4), (trp_sarranid_n_ajam2, 2, 4), (trp_sarranid_n_cemaat2, 2, 4), (trp_sarranid_n_jebelus2, 2, 4), (trp_sarranid_n_yerliyya2, 2, 4), (trp_sarranid_n_cemaat2, 1, 2)]),

	("umber_reinforcements_f", "{!}kingdom 2 reinforcements f", icon_people_player|pf_label_small, 0, fac_commoners, aggressiveness_0, [(trp_sarranid_n_garip2, 2, 4), (trp_northern_troop_1, 2, 4), (trp_sarranid_n_yeniceri2, 2, 4), (trp_sarranid_n_kapikula2, 2, 4), (trp_sarranid_n_uluteci2, 2, 4), (trp_sarranid_n_cemaat2, 1, 2)]),

	("bolton_reinforcements_a", "{!}kingdom 2 reinforcements a", icon_people_player|pf_label_small, 0, fac_commoners, aggressiveness_0, [(trp_sarranid_n_millet2, 2, 4), (trp_sarranid_n_ajam2, 2, 4), (trp_sarranid_n_cemaat2, 2, 4), (trp_sarranid_n_jebelus2, 2, 4), (trp_rill_lances, 2, 4), (trp_rill_lances, 1, 2)]),

	("bolton_reinforcements_b", "{!}kingdom 2 reinforcements b", icon_people_player|pf_label_small, 0, fac_commoners, aggressiveness_0, [(trp_sarranid_n_millet2, 2, 4), (trp_sarranid_n_ajam2, 2, 4), (trp_sarranid_n_cemaat2, 2, 4), (trp_sarranid_n_jebelus2, 2, 4), (trp_rill_lances, 2, 4), (trp_rill_lances, 1, 2)]),

	("bolton_reinforcements_c", "{!}kingdom 2 reinforcements c", icon_people_player|pf_label_small, 0, fac_commoners, aggressiveness_0, [(trp_sarranid_n_millet2, 2, 4), (trp_sarranid_n_ajam2, 2, 4), (trp_sarranid_n_cemaat2, 2, 4), (trp_sarranid_n_jebelus2, 2, 4), (trp_sarranid_n_yerliyya2, 2, 4), (trp_sarranid_n_cemaat2, 1, 2)]),

	("bolton_reinforcements_d", "{!}kingdom 2 reinforcements d", icon_people_player|pf_label_small, 0, fac_commoners, aggressiveness_0, [(trp_sarranid_n_garip2, 2, 4), (trp_northern_troop_1, 2, 4), (trp_sarranid_n_yeniceri2, 2, 4), (trp_sarranid_n_kapikula2, 2, 4), (trp_sarranid_n_uluteci2, 2, 4), (trp_sarranid_n_cemaat2, 1, 2)]),

	("bolton_reinforcements_e", "{!}kingdom 2 reinforcements e", icon_people_player|pf_label_small, 0, fac_commoners, aggressiveness_0, [(trp_sarranid_n_millet2, 2, 4), (trp_sarranid_n_ajam2, 2, 4), (trp_sarranid_n_cemaat2, 2, 4), (trp_sarranid_n_jebelus2, 2, 4), (trp_sarranid_n_yerliyya2, 2, 4), (trp_sarranid_n_cemaat2, 1, 2)]),

	("bolton_reinforcements_f", "{!}kingdom 2 reinforcements f", icon_people_player|pf_label_small, 0, fac_commoners, aggressiveness_0, [(trp_sarranid_n_garip2, 2, 4), (trp_northern_troop_1, 2, 4), (trp_sarranid_n_yeniceri2, 2, 4), (trp_sarranid_n_kapikula2, 2, 4), (trp_sarranid_n_uluteci2, 2, 4), (trp_sarranid_n_cemaat2, 1, 2)]),

	("stark_reinforcements_a", "{!}kingdom 2 reinforcements a", icon_people_player|pf_label_small, 0, fac_commoners, aggressiveness_0, [(trp_sarranid_n_millet2, 2, 4), (trp_sarranid_n_ajam2, 2, 4), (trp_sarranid_n_cemaat2, 2, 4), (trp_sarranid_n_jebelus2, 2, 4), (trp_rill_lances, 2, 4), (trp_rill_lances, 1, 2)]),

	("stark_reinforcements_b", "{!}kingdom 2 reinforcements b", icon_people_player|pf_label_small, 0, fac_commoners, aggressiveness_0, [(trp_sarranid_n_millet2, 2, 4), (trp_sarranid_n_ajam2, 2, 4), (trp_sarranid_n_cemaat2, 2, 4), (trp_sarranid_n_jebelus2, 2, 4), (trp_rill_lances, 2, 4), (trp_rill_lances, 1, 2)]),

	("stark_reinforcements_c", "{!}kingdom 2 reinforcements c", icon_people_player|pf_label_small, 0, fac_commoners, aggressiveness_0, [(trp_sarranid_n_millet2, 2, 4), (trp_sarranid_n_ajam2, 2, 4), (trp_sarranid_n_cemaat2, 2, 4), (trp_sarranid_n_jebelus2, 2, 4), (trp_sarranid_n_yerliyya2, 2, 4), (trp_sarranid_n_cemaat2, 1, 2)]),

	("stark_reinforcements_d", "{!}kingdom 2 reinforcements d", icon_people_player|pf_label_small, 0, fac_commoners, aggressiveness_0, [(trp_sarranid_n_garip2, 2, 4), (trp_northern_troop_1, 2, 4), (trp_sarranid_n_yeniceri2, 2, 4), (trp_sarranid_n_kapikula2, 2, 4), (trp_sarranid_n_uluteci2, 2, 4), (trp_sarranid_n_cemaat2, 1, 2)]),

	("stark_reinforcements_e", "{!}kingdom 2 reinforcements e", icon_people_player|pf_label_small, 0, fac_commoners, aggressiveness_0, [(trp_sarranid_n_millet2, 2, 4), (trp_sarranid_n_ajam2, 2, 4), (trp_sarranid_n_cemaat2, 2, 4), (trp_sarranid_n_jebelus2, 2, 4), (trp_sarranid_n_yerliyya2, 2, 4), (trp_sarranid_n_cemaat2, 1, 2)]),

	("stark_reinforcements_f", "{!}kingdom 2 reinforcements f", icon_people_player|pf_label_small, 0, fac_commoners, aggressiveness_0, [(trp_sarranid_n_garip2, 2, 4), (trp_northern_troop_1, 2, 4), (trp_sarranid_n_yeniceri2, 2, 4), (trp_sarranid_n_kapikula2, 2, 4), (trp_sarranid_n_uluteci2, 2, 4), (trp_sarranid_n_cemaat2, 1, 2)]),

	("ryswell_reinforcements_a", "{!}kingdom 2 reinforcements a", icon_people_player|pf_label_small, 0, fac_commoners, aggressiveness_0, [(trp_sarranid_n_millet2, 2, 4), (trp_sarranid_n_ajam2, 2, 4), (trp_sarranid_n_cemaat2, 2, 4), (trp_sarranid_n_jebelus2, 2, 4), (trp_rill_lances, 2, 4), (trp_rill_lances, 1, 2)]),

	("ryswell_reinforcements_b", "{!}kingdom 2 reinforcements b", icon_people_player|pf_label_small, 0, fac_commoners, aggressiveness_0, [(trp_sarranid_n_millet2, 2, 4), (trp_sarranid_n_ajam2, 2, 4), (trp_sarranid_n_cemaat2, 2, 4), (trp_sarranid_n_jebelus2, 2, 4), (trp_rill_lances, 2, 4), (trp_rill_lances, 1, 2)]),

	("ryswell_reinforcements_c", "{!}kingdom 2 reinforcements c", icon_people_player|pf_label_small, 0, fac_commoners, aggressiveness_0, [(trp_sarranid_n_millet2, 2, 4), (trp_sarranid_n_ajam2, 2, 4), (trp_sarranid_n_cemaat2, 2, 4), (trp_sarranid_n_jebelus2, 2, 4), (trp_sarranid_n_yerliyya2, 2, 4), (trp_sarranid_n_cemaat2, 1, 2)]),

	("ryswell_reinforcements_d", "{!}kingdom 2 reinforcements d", icon_people_player|pf_label_small, 0, fac_commoners, aggressiveness_0, [(trp_sarranid_n_garip2, 2, 4), (trp_northern_troop_1, 2, 4), (trp_sarranid_n_yeniceri2, 2, 4), (trp_sarranid_n_kapikula2, 2, 4), (trp_sarranid_n_uluteci2, 2, 4), (trp_sarranid_n_cemaat2, 1, 2)]),

	("ryswell_reinforcements_e", "{!}kingdom 2 reinforcements e", icon_people_player|pf_label_small, 0, fac_commoners, aggressiveness_0, [(trp_sarranid_n_millet2, 2, 4), (trp_sarranid_n_ajam2, 2, 4), (trp_sarranid_n_cemaat2, 2, 4), (trp_sarranid_n_jebelus2, 2, 4), (trp_sarranid_n_yerliyya2, 2, 4), (trp_sarranid_n_cemaat2, 1, 2)]),

	("ryswell_reinforcements_f", "{!}kingdom 2 reinforcements f", icon_people_player|pf_label_small, 0, fac_commoners, aggressiveness_0, [(trp_sarranid_n_garip2, 2, 4), (trp_northern_troop_1, 2, 4), (trp_sarranid_n_yeniceri2, 2, 4), (trp_sarranid_n_kapikula2, 2, 4), (trp_sarranid_n_uluteci2, 2, 4), (trp_sarranid_n_cemaat2, 1, 2)]),

	("glover_reinforcements_a", "{!}kingdom 2 reinforcements a", icon_people_player|pf_label_small, 0, fac_commoners, aggressiveness_0, [(trp_port_wolfswood_champion, 2, 4), (trp_sarranid_n_ajam2, 2, 4), (trp_sarranid_n_cemaat2, 2, 4), (trp_sarranid_n_jebelus2, 2, 4), (trp_clan_champion, 2, 4), (trp_clan_champion, 1, 2)]),

	("glover_reinforcements_b", "{!}kingdom 2 reinforcements b", icon_people_player|pf_label_small, 0, fac_commoners, aggressiveness_0, [(trp_port_wolfswood_champion, 2, 4), (trp_sarranid_n_ajam2, 2, 4), (trp_sarranid_n_cemaat2, 2, 4), (trp_sarranid_n_jebelus2, 2, 4), (trp_clan_champion, 2, 4), (trp_clan_champion, 1, 2)]),

	("glover_reinforcements_c", "{!}kingdom 2 reinforcements c", icon_people_player|pf_label_small, 0, fac_commoners, aggressiveness_0, [(trp_port_wolfswood_champion, 2, 4), (trp_sarranid_n_ajam2, 2, 4), (trp_sarranid_n_cemaat2, 2, 4), (trp_sarranid_n_jebelus2, 2, 4), (trp_sarranid_n_yerliyya2, 2, 4), (trp_sarranid_n_cemaat2, 1, 2)]),

	("glover_reinforcements_d", "{!}kingdom 2 reinforcements d", icon_people_player|pf_label_small, 0, fac_commoners, aggressiveness_0, [(trp_port_wolfswood_champion, 2, 4), (trp_northern_troop_1, 2, 4), (trp_sarranid_n_yeniceri2, 2, 4), (trp_sarranid_n_kapikula2, 2, 4), (trp_sarranid_n_uluteci2, 2, 4), (trp_sarranid_n_cemaat2, 1, 2)]),

	("glover_reinforcements_e", "{!}kingdom 2 reinforcements e", icon_people_player|pf_label_small, 0, fac_commoners, aggressiveness_0, [(trp_port_wolfswood_champion, 2, 4), (trp_sarranid_n_ajam2, 2, 4), (trp_sarranid_n_cemaat2, 2, 4), (trp_sarranid_n_jebelus2, 2, 4), (trp_sarranid_n_yerliyya2, 2, 4), (trp_sarranid_n_cemaat2, 1, 2)]),

	("glover_reinforcements_f", "{!}kingdom 2 reinforcements f", icon_people_player|pf_label_small, 0, fac_commoners, aggressiveness_0, [(trp_port_wolfswood_champion, 2, 4), (trp_northern_troop_1, 2, 4), (trp_sarranid_n_yeniceri2, 2, 4), (trp_sarranid_n_kapikula2, 2, 4), (trp_sarranid_n_uluteci2, 2, 4), (trp_sarranid_n_cemaat2, 1, 2)]),

	("blackwood_reinforcements_a", "{!}kingdom 2 reinforcements a", icon_people_player|pf_label_small, 0, fac_commoners, aggressiveness_0, [(trp_sarranid_n_millet2, 2, 4), (trp_sarranid_n_ajam2, 2, 4), (trp_sarranid_n_cemaat2, 2, 4), (trp_sarranid_n_jebelus2, 2, 4), (trp_raventree_archer, 2, 4), (trp_raventree_archer, 1, 2)]),

	("blackwood_reinforcements_b", "{!}kingdom 2 reinforcements b", icon_people_player|pf_label_small, 0, fac_commoners, aggressiveness_0, [(trp_sarranid_n_millet2, 2, 4), (trp_sarranid_n_ajam2, 2, 4), (trp_sarranid_n_cemaat2, 2, 4), (trp_sarranid_n_jebelus2, 2, 4), (trp_raventree_archer, 2, 4), (trp_raventree_archer, 1, 2)]),

	("blackwood_reinforcements_c", "{!}kingdom 2 reinforcements c", icon_people_player|pf_label_small, 0, fac_commoners, aggressiveness_0, [(trp_sarranid_n_millet2, 2, 4), (trp_sarranid_n_ajam2, 2, 4), (trp_sarranid_n_cemaat2, 2, 4), (trp_sarranid_n_jebelus2, 2, 4), (trp_sarranid_n_yerliyya2, 2, 4), (trp_sarranid_n_cemaat2, 1, 2)]),

	("blackwood_reinforcements_d", "{!}kingdom 2 reinforcements d", icon_people_player|pf_label_small, 0, fac_commoners, aggressiveness_0, [(trp_sarranid_n_garip2, 2, 4), (trp_northern_troop_1, 2, 4), (trp_sarranid_n_yeniceri2, 2, 4), (trp_sarranid_n_kapikula2, 2, 4), (trp_sarranid_n_uluteci2, 2, 4), (trp_sarranid_n_cemaat2, 1, 2)]),

	("blackwood_reinforcements_e", "{!}kingdom 2 reinforcements e", icon_people_player|pf_label_small, 0, fac_commoners, aggressiveness_0, [(trp_sarranid_n_millet2, 2, 4), (trp_sarranid_n_ajam2, 2, 4), (trp_sarranid_n_cemaat2, 2, 4), (trp_sarranid_n_jebelus2, 2, 4), (trp_sarranid_n_yerliyya2, 2, 4), (trp_sarranid_n_cemaat2, 1, 2)]),

	("blackwood_reinforcements_f", "{!}kingdom 2 reinforcements f", icon_people_player|pf_label_small, 0, fac_commoners, aggressiveness_0, [(trp_sarranid_n_garip2, 2, 4), (trp_northern_troop_1, 2, 4), (trp_sarranid_n_yeniceri2, 2, 4), (trp_sarranid_n_kapikula2, 2, 4), (trp_sarranid_n_uluteci2, 2, 4), (trp_sarranid_n_cemaat2, 1, 2)]),

	("river_reinforcements_a", "{!}kingdom 2 reinforcements a", icon_people_player|pf_label_small, 0, fac_commoners, aggressiveness_0, [(trp_sarranid_n_millet2, 2, 4), (trp_sarranid_n_ajam2, 2, 4), (trp_sarranid_n_cemaat2, 2, 4), (trp_sarranid_n_jebelus2, 2, 4), (trp_stone_hedge_knight, 2, 4), (trp_stone_hedge_knight, 1, 2)]),

	("river_reinforcements_b", "{!}kingdom 2 reinforcements b", icon_people_player|pf_label_small, 0, fac_commoners, aggressiveness_0, [(trp_sarranid_n_millet2, 2, 4), (trp_sarranid_n_ajam2, 2, 4), (trp_sarranid_n_cemaat2, 2, 4), (trp_sarranid_n_jebelus2, 2, 4), (trp_stone_hedge_knight, 2, 4), (trp_stone_hedge_knight, 1, 2)]),

	("river_reinforcements_c", "{!}kingdom 2 reinforcements c", icon_people_player|pf_label_small, 0, fac_commoners, aggressiveness_0, [(trp_sarranid_n_millet2, 2, 4), (trp_sarranid_n_ajam2, 2, 4), (trp_sarranid_n_cemaat2, 2, 4), (trp_sarranid_n_jebelus2, 2, 4), (trp_sarranid_n_yerliyya2, 2, 4), (trp_sarranid_n_cemaat2, 1, 2)]),

	("river_reinforcements_d", "{!}kingdom 2 reinforcements d", icon_people_player|pf_label_small, 0, fac_commoners, aggressiveness_0, [(trp_sarranid_n_garip2, 2, 4), (trp_northern_troop_1, 2, 4), (trp_sarranid_n_yeniceri2, 2, 4), (trp_sarranid_n_kapikula2, 2, 4), (trp_sarranid_n_uluteci2, 2, 4), (trp_sarranid_n_cemaat2, 1, 2)]),

	("river_reinforcements_e", "{!}kingdom 2 reinforcements e", icon_people_player|pf_label_small, 0, fac_commoners, aggressiveness_0, [(trp_sarranid_n_millet2, 2, 4), (trp_sarranid_n_ajam2, 2, 4), (trp_sarranid_n_cemaat2, 2, 4), (trp_sarranid_n_jebelus2, 2, 4), (trp_sarranid_n_yerliyya2, 2, 4), (trp_sarranid_n_cemaat2, 1, 2)]),

	("river_reinforcements_f", "{!}kingdom 2 reinforcements f", icon_people_player|pf_label_small, 0, fac_commoners, aggressiveness_0, [(trp_sarranid_n_garip2, 2, 4), (trp_northern_troop_1, 2, 4), (trp_sarranid_n_yeniceri2, 2, 4), (trp_sarranid_n_kapikula2, 2, 4), (trp_sarranid_n_uluteci2, 2, 4), (trp_sarranid_n_cemaat2, 1, 2)]),

	("bracken_reinforcements_a", "{!}kingdom 2 reinforcements a", icon_people_player|pf_label_small, 0, fac_commoners, aggressiveness_0, [(trp_sarranid_n_millet2, 2, 4), (trp_sarranid_n_ajam2, 2, 4), (trp_sarranid_n_cemaat2, 2, 4), (trp_sarranid_n_jebelus2, 2, 4), (trp_stone_hedge_knight, 2, 4), (trp_stone_hedge_knight, 1, 2)]),

	("bracken_reinforcements_b", "{!}kingdom 2 reinforcements b", icon_people_player|pf_label_small, 0, fac_commoners, aggressiveness_0, [(trp_sarranid_n_millet2, 2, 4), (trp_sarranid_n_ajam2, 2, 4), (trp_sarranid_n_cemaat2, 2, 4), (trp_sarranid_n_jebelus2, 2, 4), (trp_stone_hedge_knight, 2, 4), (trp_stone_hedge_knight, 1, 2)]),

	("bracken_reinforcements_c", "{!}kingdom 2 reinforcements c", icon_people_player|pf_label_small, 0, fac_commoners, aggressiveness_0, [(trp_sarranid_n_millet2, 2, 4), (trp_sarranid_n_ajam2, 2, 4), (trp_sarranid_n_cemaat2, 2, 4), (trp_sarranid_n_jebelus2, 2, 4), (trp_sarranid_n_yerliyya2, 2, 4), (trp_sarranid_n_cemaat2, 1, 2)]),

	("bracken_reinforcements_d", "{!}kingdom 2 reinforcements d", icon_people_player|pf_label_small, 0, fac_commoners, aggressiveness_0, [(trp_sarranid_n_garip2, 2, 4), (trp_northern_troop_1, 2, 4), (trp_sarranid_n_yeniceri2, 2, 4), (trp_sarranid_n_kapikula2, 2, 4), (trp_sarranid_n_uluteci2, 2, 4), (trp_sarranid_n_cemaat2, 1, 2)]),

	("bracken_reinforcements_e", "{!}kingdom 2 reinforcements e", icon_people_player|pf_label_small, 0, fac_commoners, aggressiveness_0, [(trp_sarranid_n_millet2, 2, 4), (trp_sarranid_n_ajam2, 2, 4), (trp_sarranid_n_cemaat2, 2, 4), (trp_sarranid_n_jebelus2, 2, 4), (trp_sarranid_n_yerliyya2, 2, 4), (trp_sarranid_n_cemaat2, 1, 2)]),

	("bracken_reinforcements_f", "{!}kingdom 2 reinforcements f", icon_people_player|pf_label_small, 0, fac_commoners, aggressiveness_0, [(trp_sarranid_n_garip2, 2, 4), (trp_northern_troop_1, 2, 4), (trp_sarranid_n_yeniceri2, 2, 4), (trp_sarranid_n_kapikula2, 2, 4), (trp_sarranid_n_uluteci2, 2, 4), (trp_sarranid_n_cemaat2, 1, 2)]),

	("frey_reinforcements_a", "{!}kingdom 2 reinforcements a", icon_people_player|pf_label_small, 0, fac_commoners, aggressiveness_0, [(trp_sarranid_n_millet2, 2, 4), (trp_sarranid_n_ajam2, 2, 4), (trp_sarranid_n_cemaat2, 2, 4), (trp_sarranid_n_jebelus2, 2, 4), (trp_crossing_spearman, 2, 4), (trp_crossing_spearman, 1, 2)]),

	("frey_reinforcements_b", "{!}kingdom 2 reinforcements b", icon_people_player|pf_label_small, 0, fac_commoners, aggressiveness_0, [(trp_sarranid_n_millet2, 2, 4), (trp_sarranid_n_ajam2, 2, 4), (trp_sarranid_n_cemaat2, 2, 4), (trp_sarranid_n_jebelus2, 2, 4), (trp_crossing_spearman, 2, 4), (trp_crossing_spearman, 1, 2)]),

	("frey_reinforcements_c", "{!}kingdom 2 reinforcements c", icon_people_player|pf_label_small, 0, fac_commoners, aggressiveness_0, [(trp_sarranid_n_millet2, 2, 4), (trp_sarranid_n_ajam2, 2, 4), (trp_sarranid_n_cemaat2, 2, 4), (trp_sarranid_n_jebelus2, 2, 4), (trp_sarranid_n_yerliyya2, 2, 4), (trp_sarranid_n_cemaat2, 1, 2)]),

	("frey_reinforcements_d", "{!}kingdom 2 reinforcements d", icon_people_player|pf_label_small, 0, fac_commoners, aggressiveness_0, [(trp_sarranid_n_garip2, 2, 4), (trp_northern_troop_1, 2, 4), (trp_sarranid_n_yeniceri2, 2, 4), (trp_sarranid_n_kapikula2, 2, 4), (trp_sarranid_n_uluteci2, 2, 4), (trp_sarranid_n_cemaat2, 1, 2)]),

	("frey_reinforcements_e", "{!}kingdom 2 reinforcements e", icon_people_player|pf_label_small, 0, fac_commoners, aggressiveness_0, [(trp_sarranid_n_millet2, 2, 4), (trp_sarranid_n_ajam2, 2, 4), (trp_sarranid_n_cemaat2, 2, 4), (trp_sarranid_n_jebelus2, 2, 4), (trp_sarranid_n_yerliyya2, 2, 4), (trp_sarranid_n_cemaat2, 1, 2)]),

	("frey_reinforcements_f", "{!}kingdom 2 reinforcements f", icon_people_player|pf_label_small, 0, fac_commoners, aggressiveness_0, [(trp_sarranid_n_garip2, 2, 4), (trp_northern_troop_1, 2, 4), (trp_sarranid_n_yeniceri2, 2, 4), (trp_sarranid_n_kapikula2, 2, 4), (trp_sarranid_n_uluteci2, 2, 4), (trp_sarranid_n_cemaat2, 1, 2)]),

	("royce_reinforcements_a", "{!}kingdom 3 reinforcements a", icon_people_player|pf_label_small, 0, fac_commoners, aggressiveness_0, [(trp_sarranid_n_millet3, 2, 4), (trp_sarranid_n_ajam3, 2, 4), (trp_sarranid_n_cemaat3, 2, 4), (trp_sarranid_n_jebelus3, 2, 4), (trp_runestone_squire, 2, 4), (trp_runestone_squire, 1, 2)]),

	("royce_reinforcements_b", "{!}kingdom 3 reinforcements b", icon_people_player|pf_label_small, 0, fac_commoners, aggressiveness_0, [(trp_sarranid_n_millet3, 2, 4), (trp_sarranid_n_ajam3, 2, 4), (trp_sarranid_n_cemaat3, 2, 4), (trp_sarranid_n_jebelus3, 2, 4), (trp_runestone_squire, 2, 4), (trp_runestone_squire, 1, 2)]),

	("royce_reinforcements_c", "{!}kingdom 3 reinforcements c", icon_people_player|pf_label_small, 0, fac_commoners, aggressiveness_0, [(trp_sarranid_n_millet3, 2, 4), (trp_sarranid_n_ajam3, 2, 4), (trp_sarranid_n_cemaat3, 2, 4), (trp_sarranid_n_jebelus3, 2, 4), (trp_sarranid_n_yerliyya3, 2, 4), (trp_sarranid_n_cemaat3, 1, 2)]),

	("royce_reinforcements_d", "{!}kingdom 3 reinforcements d", icon_people_player|pf_label_small, 0, fac_commoners, aggressiveness_0, [(trp_sarranid_n_garip3, 2, 4), (trp_vale_troop_1, 2, 4), (trp_sarranid_n_yeniceri3, 2, 4), (trp_sarranid_n_kapikula3, 2, 4), (trp_sarranid_n_uluteci3, 2, 4), (trp_sarranid_n_cemaat3, 1, 2)]),

	("royce_reinforcements_e", "{!}kingdom 3 reinforcements e", icon_people_player|pf_label_small, 0, fac_commoners, aggressiveness_0, [(trp_sarranid_n_millet3, 2, 4), (trp_sarranid_n_ajam3, 2, 4), (trp_sarranid_n_cemaat3, 2, 4), (trp_sarranid_n_jebelus3, 2, 4), (trp_sarranid_n_yerliyya3, 2, 4), (trp_sarranid_n_cemaat3, 1, 2)]),

	("royce_reinforcements_f", "{!}kingdom 3 reinforcements f", icon_people_player|pf_label_small, 0, fac_commoners, aggressiveness_0, [(trp_sarranid_n_garip3, 2, 4), (trp_vale_troop_1, 2, 4), (trp_sarranid_n_yeniceri3, 2, 4), (trp_sarranid_n_kapikula3, 2, 4), (trp_sarranid_n_uluteci3, 2, 4), (trp_sarranid_n_cemaat3, 1, 2)]),

	("hunter_reinforcements_a", "{!}kingdom 3 reinforcements a", icon_people_player|pf_label_small, 0, fac_commoners, aggressiveness_0, [(trp_sarranid_n_millet3, 2, 4), (trp_sarranid_n_ajam3, 2, 4), (trp_sarranid_n_cemaat3, 2, 4), (trp_sarranid_n_jebelus3, 2, 4), (trp_longbow_hall_archer, 2, 4), (trp_longbow_hall_archer, 1, 2)]),

	("hunter_reinforcements_b", "{!}kingdom 3 reinforcements b", icon_people_player|pf_label_small, 0, fac_commoners, aggressiveness_0, [(trp_sarranid_n_millet3, 2, 4), (trp_sarranid_n_ajam3, 2, 4), (trp_sarranid_n_cemaat3, 2, 4), (trp_sarranid_n_jebelus3, 2, 4), (trp_longbow_hall_archer, 2, 4), (trp_longbow_hall_archer, 1, 2)]),

	("hunter_reinforcements_c", "{!}kingdom 3 reinforcements c", icon_people_player|pf_label_small, 0, fac_commoners, aggressiveness_0, [(trp_sarranid_n_millet3, 2, 4), (trp_sarranid_n_ajam3, 2, 4), (trp_sarranid_n_cemaat3, 2, 4), (trp_sarranid_n_jebelus3, 2, 4), (trp_sarranid_n_yerliyya3, 2, 4), (trp_sarranid_n_cemaat3, 1, 2)]),

	("hunter_reinforcements_d", "{!}kingdom 3 reinforcements d", icon_people_player|pf_label_small, 0, fac_commoners, aggressiveness_0, [(trp_sarranid_n_garip3, 2, 4), (trp_vale_troop_1, 2, 4), (trp_sarranid_n_yeniceri3, 2, 4), (trp_sarranid_n_kapikula3, 2, 4), (trp_sarranid_n_uluteci3, 2, 4), (trp_sarranid_n_cemaat3, 1, 2)]),

	("hunter_reinforcements_e", "{!}kingdom 3 reinforcements e", icon_people_player|pf_label_small, 0, fac_commoners, aggressiveness_0, [(trp_sarranid_n_millet3, 2, 4), (trp_sarranid_n_ajam3, 2, 4), (trp_sarranid_n_cemaat3, 2, 4), (trp_sarranid_n_jebelus3, 2, 4), (trp_sarranid_n_yerliyya3, 2, 4), (trp_sarranid_n_cemaat3, 1, 2)]),

	("hunter_reinforcements_f", "{!}kingdom 3 reinforcements f", icon_people_player|pf_label_small, 0, fac_commoners, aggressiveness_0, [(trp_sarranid_n_garip3, 2, 4), (trp_vale_troop_1, 2, 4), (trp_sarranid_n_yeniceri3, 2, 4), (trp_sarranid_n_kapikula3, 2, 4), (trp_sarranid_n_uluteci3, 2, 4), (trp_sarranid_n_cemaat3, 1, 2)]),

	("yronwood_reinforcements_a", "{!}kingdom 6 reinforcements a", icon_people_player|pf_label_small, 0, fac_commoners, aggressiveness_0, [(trp_sarranid_n_millet, 2, 4), (trp_sarranid_n_ajam, 2, 4), (trp_sarranid_n_cemaat, 2, 4), (trp_sarranid_n_jebelus, 2, 4), (trp_sarranid_n_yerliyya, 2, 4), (trp_sarranid_n_cemaat, 1, 2)]),

	("yronwood_reinforcements_b", "{!}kingdom 6 reinforcements b", icon_people_player|pf_label_small, 0, fac_commoners, aggressiveness_0, [(trp_sarranid_n_millet, 2, 4), (trp_sarranid_n_ajam, 2, 4), (trp_sarranid_n_cemaat, 2, 4), (trp_sarranid_n_jebelus, 2, 4), (trp_sarranid_n_yerliyya, 2, 4), (trp_sarranid_n_cemaat, 1, 2)]),

	("yronwood_reinforcements_c", "{!}kingdom 6 reinforcements c", icon_people_player|pf_label_small, 0, fac_commoners, aggressiveness_0, [(trp_sarranid_n_millet, 2, 4), (trp_sarranid_n_ajam, 2, 4), (trp_sarranid_n_cemaat, 2, 4), (trp_sarranid_n_yerliyya, 2, 4), (trp_sarranid_n_yerliyya, 2, 4), (trp_sarranid_n_cemaat, 1, 2)]),

	("yronwood_reinforcements_d", "{!}kingdom 6 reinforcements d", icon_people_player|pf_label_small, 0, fac_commoners, aggressiveness_0, [(trp_sarranid_n_garip, 2, 4), (trp_sarranid_n_ajam, 2, 4), (trp_sarranid_n_yeniceri, 2, 4), (trp_sarranid_n_kapikula, 2, 4), (trp_sarranid_n_uluteci, 2, 4), (trp_sarranid_n_cemaat, 1, 2)]),

	("yronwood_reinforcements_e", "{!}kingdom 6 reinforcements e", icon_people_player|pf_label_small, 0, fac_commoners, aggressiveness_0, [(trp_sarranid_n_millet, 2, 4), (trp_sarranid_n_ajam, 2, 4), (trp_sarranid_n_cemaat, 2, 4), (trp_sarranid_n_yerliyya, 2, 4), (trp_sarranid_n_yerliyya, 2, 4), (trp_sarranid_n_cemaat, 1, 2)]),

	("yronwood_reinforcements_f", "{!}kingdom 6 reinforcements f", icon_people_player|pf_label_small, 0, fac_commoners, aggressiveness_0, [(trp_sarranid_n_garip, 2, 4), (trp_dorne_troop_1, 2, 4), (trp_sarranid_n_yeniceri, 2, 4), (trp_sarranid_n_kapikula, 2, 4), (trp_sarranid_n_uluteci, 2, 4), (trp_sarranid_n_cemaat, 1, 2)]),

	("qorgyle_reinforcements_a", "{!}kingdom 6 reinforcements a", icon_people_player|pf_label_small, 0, fac_commoners, aggressiveness_0, [(trp_sarranid_n_millet, 2, 4), (trp_sarranid_n_ajam, 2, 4), (trp_sarranid_n_cemaat, 2, 4), (trp_sarranid_n_jebelus, 2, 4), (trp_sarranid_n_yerliyya, 2, 4), (trp_sarranid_n_cemaat, 1, 2)]),

	("qorgyle_reinforcements_b", "{!}kingdom 6 reinforcements b", icon_people_player|pf_label_small, 0, fac_commoners, aggressiveness_0, [(trp_sarranid_n_millet, 2, 4), (trp_sarranid_n_ajam, 2, 4), (trp_sarranid_n_cemaat, 2, 4), (trp_sarranid_n_jebelus, 2, 4), (trp_sarranid_n_yerliyya, 2, 4), (trp_sarranid_n_cemaat, 1, 2)]),

	("qorgyle_reinforcements_c", "{!}kingdom 6 reinforcements c", icon_people_player|pf_label_small, 0, fac_commoners, aggressiveness_0, [(trp_sarranid_n_millet, 2, 4), (trp_sarranid_n_ajam, 2, 4), (trp_sarranid_n_cemaat, 2, 4), (trp_sarranid_n_yerliyya, 2, 4), (trp_sarranid_n_yerliyya, 2, 4), (trp_sarranid_n_cemaat, 1, 2)]),

	("qorgyle_reinforcements_d", "{!}kingdom 6 reinforcements d", icon_people_player|pf_label_small, 0, fac_commoners, aggressiveness_0, [(trp_sarranid_n_garip, 2, 4), (trp_sarranid_n_ajam, 2, 4), (trp_sarranid_n_yeniceri, 2, 4), (trp_sarranid_n_kapikula, 2, 4), (trp_sarranid_n_uluteci, 2, 4), (trp_sarranid_n_cemaat, 1, 2)]),

	("qorgyle_reinforcements_e", "{!}kingdom 6 reinforcements e", icon_people_player|pf_label_small, 0, fac_commoners, aggressiveness_0, [(trp_sarranid_n_millet, 2, 4), (trp_sarranid_n_ajam, 2, 4), (trp_sarranid_n_cemaat, 2, 4), (trp_sarranid_n_yerliyya, 2, 4), (trp_sarranid_n_yerliyya, 2, 4), (trp_sarranid_n_cemaat, 1, 2)]),

	("qorgyle_reinforcements_f", "{!}kingdom 6 reinforcements f", icon_people_player|pf_label_small, 0, fac_commoners, aggressiveness_0, [(trp_sarranid_n_garip, 2, 4), (trp_dorne_troop_1, 2, 4), (trp_sarranid_n_yeniceri, 2, 4), (trp_sarranid_n_kapikula, 2, 4), (trp_sarranid_n_uluteci, 2, 4), (trp_sarranid_n_cemaat, 1, 2)]),

	("fowler_reinforcements_a", "{!}kingdom 6 reinforcements a", icon_people_player|pf_label_small, 0, fac_commoners, aggressiveness_0, [(trp_sarranid_n_millet, 2, 4), (trp_sarranid_n_ajam, 2, 4), (trp_sarranid_n_cemaat, 2, 4), (trp_sarranid_n_jebelus, 2, 4), (trp_sarranid_n_yerliyya, 2, 4), (trp_sarranid_n_cemaat, 1, 2)]),

	("fowler_reinforcements_b", "{!}kingdom 6 reinforcements b", icon_people_player|pf_label_small, 0, fac_commoners, aggressiveness_0, [(trp_sarranid_n_millet, 2, 4), (trp_sarranid_n_ajam, 2, 4), (trp_sarranid_n_cemaat, 2, 4), (trp_sarranid_n_jebelus, 2, 4), (trp_sarranid_n_yerliyya, 2, 4), (trp_sarranid_n_cemaat, 1, 2)]),

	("fowler_reinforcements_c", "{!}kingdom 6 reinforcements c", icon_people_player|pf_label_small, 0, fac_commoners, aggressiveness_0, [(trp_sarranid_n_millet, 2, 4), (trp_sarranid_n_ajam, 2, 4), (trp_sarranid_n_cemaat, 2, 4), (trp_sarranid_n_yerliyya, 2, 4), (trp_sarranid_n_yerliyya, 2, 4), (trp_sarranid_n_cemaat, 1, 2)]),

	("fowler_reinforcements_d", "{!}kingdom 6 reinforcements d", icon_people_player|pf_label_small, 0, fac_commoners, aggressiveness_0, [(trp_sarranid_n_garip, 2, 4), (trp_sarranid_n_ajam, 2, 4), (trp_sarranid_n_yeniceri, 2, 4), (trp_sarranid_n_kapikula, 2, 4), (trp_sarranid_n_uluteci, 2, 4), (trp_sarranid_n_cemaat, 1, 2)]),

	("fowler_reinforcements_e", "{!}kingdom 6 reinforcements e", icon_people_player|pf_label_small, 0, fac_commoners, aggressiveness_0, [(trp_sarranid_n_millet, 2, 4), (trp_sarranid_n_ajam, 2, 4), (trp_sarranid_n_cemaat, 2, 4), (trp_sarranid_n_yerliyya, 2, 4), (trp_sarranid_n_yerliyya, 2, 4), (trp_sarranid_n_cemaat, 1, 2)]),

	("fowler_reinforcements_f", "{!}kingdom 6 reinforcements f", icon_people_player|pf_label_small, 0, fac_commoners, aggressiveness_0, [(trp_sarranid_n_garip, 2, 4), (trp_dorne_troop_1, 2, 4), (trp_sarranid_n_yeniceri, 2, 4), (trp_sarranid_n_kapikula, 2, 4), (trp_sarranid_n_uluteci, 2, 4), (trp_sarranid_n_cemaat, 1, 2)]),

	("vargo_reinforcements_a", "{!}kingdom 9 reinforcements a", icon_people_player|pf_label_small, 0, fac_commoners, aggressiveness_0, [(trp_sarranid_n_cemaat9, 2, 4), (trp_sarranid_n_ajam9, 2, 4), (trp_sarranid_n_cemaat9, 2, 4), (trp_sarranid_n_jebelus9, 2, 4), (trp_sarranid_n_yerliyya9, 2, 4), (trp_sarranid_n_cemaat9, 1, 2)]),

	("vargo_reinforcements_b", "{!}kingdom 9 reinforcements b", icon_people_player|pf_label_small, 0, fac_commoners, aggressiveness_0, [(trp_sarranid_n_millet9, 2, 4), (trp_sarranid_n_ajam9, 2, 4), (trp_sarranid_n_cemaat9, 2, 4), (trp_sarranid_n_jebelus9, 2, 4), (trp_sarranid_n_yerliyya9, 2, 4), (trp_sarranid_n_cemaat9, 1, 2)]),

	("vargo_reinforcements_c", "{!}kingdom 9 reinforcements c", icon_people_player|pf_label_small, 0, fac_commoners, aggressiveness_0, [(trp_sarranid_n_millet9, 2, 4), (trp_sarranid_n_ajam9, 2, 4), (trp_sarranid_n_cemaat9, 2, 4), (trp_sarranid_n_yerliyya9, 2, 4), (trp_sarranid_n_yerliyya9, 2, 4), (trp_sarranid_n_cemaat9, 1, 2)]),

	("vargo_reinforcements_d", "{!}kingdom 9 reinforcements d", icon_people_player|pf_label_small, 0, fac_commoners, aggressiveness_0, [(trp_sarranid_n_millet9, 2, 4), (trp_sarranid_n_ajam9, 2, 4), (trp_sarranid_n_yeniceri9, 2, 4), (trp_sarranid_n_kapikula9, 2, 4), (trp_sarranid_n_uluteci9, 2, 4), (trp_sarranid_n_cemaat9, 1, 2)]),

	("vargo_reinforcements_e", "{!}kingdom 9 reinforcements e", icon_people_player|pf_label_small, 0, fac_commoners, aggressiveness_0, [(trp_sarranid_n_millet9, 2, 4), (trp_sarranid_n_ajam9, 2, 4), (trp_sarranid_n_cemaat9, 2, 4), (trp_sarranid_n_yerliyya9, 2, 4), (trp_sarranid_n_yerliyya9, 2, 4), (trp_sarranid_n_cemaat9, 1, 2)]),

	("vargo_reinforcements_f", "{!}kingdom 9 reinforcements f", icon_people_player|pf_label_small, 0, fac_commoners, aggressiveness_0, [(trp_sarranid_n_garip9, 2, 4), (trp_westerlands_troop_1, 2, 4), (trp_sarranid_n_yeniceri9, 2, 4), (trp_sarranid_n_kapikula9, 2, 4), (trp_sarranid_n_uluteci9, 2, 4), (trp_sarranid_n_cemaat9, 1, 2)]),

	("sarsfield_reinforcements_a", "{!}kingdom 9 reinforcements a", icon_people_player|pf_label_small, 0, fac_commoners, aggressiveness_0, [(trp_sarranid_n_cemaat9, 2, 4), (trp_sarranid_n_ajam9, 2, 4), (trp_sarranid_n_cemaat9, 2, 4), (trp_sarranid_n_jebelus9, 2, 4), (trp_sarranid_n_yerliyya9, 2, 4), (trp_sarranid_n_cemaat9, 1, 2)]),

	("sarsfield_reinforcements_b", "{!}kingdom 9 reinforcements b", icon_people_player|pf_label_small, 0, fac_commoners, aggressiveness_0, [(trp_sarranid_n_millet9, 2, 4), (trp_sarranid_n_ajam9, 2, 4), (trp_sarranid_n_cemaat9, 2, 4), (trp_sarranid_n_jebelus9, 2, 4), (trp_sarranid_n_yerliyya9, 2, 4), (trp_sarranid_n_cemaat9, 1, 2)]),

	("sarsfield_reinforcements_c", "{!}kingdom 9 reinforcements c", icon_people_player|pf_label_small, 0, fac_commoners, aggressiveness_0, [(trp_sarranid_n_millet9, 2, 4), (trp_sarranid_n_ajam9, 2, 4), (trp_sarranid_n_cemaat9, 2, 4), (trp_sarranid_n_yerliyya9, 2, 4), (trp_sarranid_n_yerliyya9, 2, 4), (trp_sarranid_n_cemaat9, 1, 2)]),

	("sarsfield_reinforcements_d", "{!}kingdom 9 reinforcements d", icon_people_player|pf_label_small, 0, fac_commoners, aggressiveness_0, [(trp_sarranid_n_millet9, 2, 4), (trp_sarranid_n_ajam9, 2, 4), (trp_sarranid_n_yeniceri9, 2, 4), (trp_sarranid_n_kapikula9, 2, 4), (trp_sarranid_n_uluteci9, 2, 4), (trp_sarranid_n_cemaat9, 1, 2)]),

	("sarsfield_reinforcements_e", "{!}kingdom 9 reinforcements e", icon_people_player|pf_label_small, 0, fac_commoners, aggressiveness_0, [(trp_sarranid_n_millet9, 2, 4), (trp_sarranid_n_ajam9, 2, 4), (trp_sarranid_n_cemaat9, 2, 4), (trp_sarranid_n_yerliyya9, 2, 4), (trp_sarranid_n_yerliyya9, 2, 4), (trp_sarranid_n_cemaat9, 1, 2)]),

	("sarsfield_reinforcements_f", "{!}kingdom 9 reinforcements f", icon_people_player|pf_label_small, 0, fac_commoners, aggressiveness_0, [(trp_sarranid_n_garip9, 2, 4), (trp_westerlands_troop_1, 2, 4), (trp_sarranid_n_yeniceri9, 2, 4), (trp_sarranid_n_kapikula9, 2, 4), (trp_sarranid_n_uluteci9, 2, 4), (trp_sarranid_n_cemaat9, 1, 2)]),

	("banefort_reinforcements_a", "{!}kingdom 9 reinforcements a", icon_people_player|pf_label_small, 0, fac_commoners, aggressiveness_0, [(trp_sarranid_n_cemaat9, 2, 4), (trp_sarranid_n_ajam9, 2, 4), (trp_sarranid_n_cemaat9, 2, 4), (trp_sarranid_n_jebelus9, 2, 4), (trp_sarranid_n_yerliyya9, 2, 4), (trp_sarranid_n_cemaat9, 1, 2)]),

	("banefort_reinforcements_b", "{!}kingdom 9 reinforcements b", icon_people_player|pf_label_small, 0, fac_commoners, aggressiveness_0, [(trp_sarranid_n_millet9, 2, 4), (trp_sarranid_n_ajam9, 2, 4), (trp_sarranid_n_cemaat9, 2, 4), (trp_sarranid_n_jebelus9, 2, 4), (trp_sarranid_n_yerliyya9, 2, 4), (trp_sarranid_n_cemaat9, 1, 2)]),

	("banefort_reinforcements_c", "{!}kingdom 9 reinforcements c", icon_people_player|pf_label_small, 0, fac_commoners, aggressiveness_0, [(trp_sarranid_n_millet9, 2, 4), (trp_sarranid_n_ajam9, 2, 4), (trp_sarranid_n_cemaat9, 2, 4), (trp_sarranid_n_yerliyya9, 2, 4), (trp_sarranid_n_yerliyya9, 2, 4), (trp_sarranid_n_cemaat9, 1, 2)]),

	("banefort_reinforcements_d", "{!}kingdom 9 reinforcements d", icon_people_player|pf_label_small, 0, fac_commoners, aggressiveness_0, [(trp_sarranid_n_millet9, 2, 4), (trp_sarranid_n_ajam9, 2, 4), (trp_sarranid_n_yeniceri9, 2, 4), (trp_sarranid_n_kapikula9, 2, 4), (trp_sarranid_n_uluteci9, 2, 4), (trp_sarranid_n_cemaat9, 1, 2)]),

	("banefort_reinforcements_e", "{!}kingdom 9 reinforcements e", icon_people_player|pf_label_small, 0, fac_commoners, aggressiveness_0, [(trp_sarranid_n_millet9, 2, 4), (trp_sarranid_n_ajam9, 2, 4), (trp_sarranid_n_cemaat9, 2, 4), (trp_sarranid_n_yerliyya9, 2, 4), (trp_sarranid_n_yerliyya9, 2, 4), (trp_sarranid_n_cemaat9, 1, 2)]),

	("banefort_reinforcements_f", "{!}kingdom 9 reinforcements f", icon_people_player|pf_label_small, 0, fac_commoners, aggressiveness_0, [(trp_sarranid_n_garip9, 2, 4), (trp_westerlands_troop_1, 2, 4), (trp_sarranid_n_yeniceri9, 2, 4), (trp_sarranid_n_kapikula9, 2, 4), (trp_sarranid_n_uluteci9, 2, 4), (trp_sarranid_n_cemaat9, 1, 2)]),

	("stannis_reinforcements_a", "{!}kingdom 8 reinforcements a", icon_people_player|pf_label_small, 0, fac_commoners, aggressiveness_0, [(trp_sarranid_n_millet8, 2, 4), (trp_sarranid_n_ajam8, 2, 4), (trp_sarranid_n_cemaat8, 2, 4), (trp_driftmark_spearman, 2, 4), (trp_driftmark_spearman, 2, 4), (trp_sarranid_n_cemaat8, 1, 2)]),

	("stannis_reinforcements_b", "{!}kingdom 8 reinforcements b", icon_people_player|pf_label_small, 0, fac_commoners, aggressiveness_0, [(trp_sarranid_n_millet8, 2, 4), (trp_sarranid_n_ajam8, 2, 4), (trp_sarranid_n_cemaat8, 2, 4), (trp_driftmark_spearman, 2, 4), (trp_driftmark_spearman, 2, 4), (trp_sarranid_n_cemaat8, 1, 2)]),

	("stannis_reinforcements_c", "{!}kingdom 8 reinforcements c", icon_people_player|pf_label_small, 0, fac_commoners, aggressiveness_0, [(trp_sarranid_n_millet8, 2, 4), (trp_sarranid_n_ajam8, 2, 4), (trp_sarranid_n_cemaat8, 2, 4), (trp_driftmark_spearman, 2, 4), (trp_driftmark_spearman, 2, 4), (trp_sarranid_n_cemaat8, 1, 2)]),

	("stannis_reinforcements_d", "{!}kingdom 8 reinforcements d", icon_people_player|pf_label_small, 0, fac_commoners, aggressiveness_0, [(trp_sarranid_n_garip8, 2, 4), (trp_dragonstone_troop_1, 2, 4), (trp_sarranid_n_yeniceri8, 2, 4), (trp_sarranid_n_kapikula8, 2, 4), (trp_sarranid_n_uluteci8, 2, 4), (trp_sarranid_n_cemaat8, 1, 2)]),

	("stannis_reinforcements_e", "{!}kingdom 8 reinforcements e", icon_people_player|pf_label_small, 0, fac_commoners, aggressiveness_0, [(trp_sarranid_n_millet8, 2, 4), (trp_sarranid_n_ajam8, 2, 4), (trp_sarranid_n_cemaat8, 2, 4), (trp_sarranid_n_jebelus8, 2, 4), (trp_sarranid_n_yerliyya8, 2, 4), (trp_sarranid_n_cemaat8, 1, 2)]),

	("stannis_reinforcements_f", "{!}kingdom 8 reinforcements f", icon_people_player|pf_label_small, 0, fac_commoners, aggressiveness_0, [(trp_sarranid_n_garip8, 2, 4), (trp_dragonstone_troop_1, 2, 4), (trp_sarranid_n_yeniceri8, 2, 4), (trp_sarranid_n_kapikula8, 2, 4), (trp_sarranid_n_uluteci8, 2, 4), (trp_sarranid_n_cemaat8, 1, 2)]),

	("velaryon_reinforcements_a", "{!}kingdom 8 reinforcements a", icon_people_player|pf_label_small, 0, fac_commoners, aggressiveness_0, [(trp_sarranid_n_millet8, 2, 4), (trp_sarranid_n_ajam8, 2, 4), (trp_sarranid_n_cemaat8, 2, 4), (trp_driftmark_spearman, 2, 4), (trp_driftmark_spearman, 2, 4), (trp_sarranid_n_cemaat8, 1, 2)]),

	("velaryon_reinforcements_b", "{!}kingdom 8 reinforcements b", icon_people_player|pf_label_small, 0, fac_commoners, aggressiveness_0, [(trp_sarranid_n_millet8, 2, 4), (trp_sarranid_n_ajam8, 2, 4), (trp_sarranid_n_cemaat8, 2, 4), (trp_driftmark_spearman, 2, 4), (trp_driftmark_spearman, 2, 4), (trp_sarranid_n_cemaat8, 1, 2)]),

	("velaryon_reinforcements_c", "{!}kingdom 8 reinforcements c", icon_people_player|pf_label_small, 0, fac_commoners, aggressiveness_0, [(trp_sarranid_n_millet8, 2, 4), (trp_sarranid_n_ajam8, 2, 4), (trp_sarranid_n_cemaat8, 2, 4), (trp_driftmark_spearman, 2, 4), (trp_driftmark_spearman, 2, 4), (trp_sarranid_n_cemaat8, 1, 2)]),

	("velaryon_reinforcements_d", "{!}kingdom 8 reinforcements d", icon_people_player|pf_label_small, 0, fac_commoners, aggressiveness_0, [(trp_sarranid_n_garip8, 2, 4), (trp_dragonstone_troop_1, 2, 4), (trp_sarranid_n_yeniceri8, 2, 4), (trp_sarranid_n_kapikula8, 2, 4), (trp_sarranid_n_uluteci8, 2, 4), (trp_sarranid_n_cemaat8, 1, 2)]),

	("velaryon_reinforcements_e", "{!}kingdom 8 reinforcements e", icon_people_player|pf_label_small, 0, fac_commoners, aggressiveness_0, [(trp_sarranid_n_millet8, 2, 4), (trp_sarranid_n_ajam8, 2, 4), (trp_sarranid_n_cemaat8, 2, 4), (trp_sarranid_n_jebelus8, 2, 4), (trp_sarranid_n_yerliyya8, 2, 4), (trp_sarranid_n_cemaat8, 1, 2)]),

	("velaryon_reinforcements_f", "{!}kingdom 8 reinforcements f", icon_people_player|pf_label_small, 0, fac_commoners, aggressiveness_0, [(trp_sarranid_n_garip8, 2, 4), (trp_dragonstone_troop_1, 2, 4), (trp_sarranid_n_yeniceri8, 2, 4), (trp_sarranid_n_kapikula8, 2, 4), (trp_sarranid_n_uluteci8, 2, 4), (trp_sarranid_n_cemaat8, 1, 2)]),

	("saan_reinforcements_a", "{!}kingdom 8 reinforcements a", icon_people_player|pf_label_small, 0, fac_commoners, aggressiveness_0, [(trp_lyseni_pirate, 2, 4), (trp_lyseni_pirate, 2, 4), (trp_lyseni_pirate, 2, 4), (trp_lyseni_pirate, 2, 4), (trp_lyseni_pirate, 2, 4), (trp_lyseni_pirate, 1, 2)]),

	("saan_reinforcements_b", "{!}kingdom 8 reinforcements b", icon_people_player|pf_label_small, 0, fac_commoners, aggressiveness_0, [(trp_lyseni_pirate, 2, 4), (trp_lyseni_pirate, 2, 4), (trp_lyseni_pirate, 2, 4), (trp_lyseni_pirate, 2, 4), (trp_lyseni_pirate, 2, 4), (trp_lyseni_pirate, 1, 2)]),

	("saan_reinforcements_c", "{!}kingdom 8 reinforcements c", icon_people_player|pf_label_small, 0, fac_commoners, aggressiveness_0, [(trp_lyseni_pirate, 2, 4), (trp_lyseni_pirate, 2, 4), (trp_lyseni_pirate, 2, 4), (trp_lyseni_pirate, 2, 4), (trp_lyseni_pirate, 2, 4), (trp_lyseni_pirate, 1, 2)]),

	("saan_reinforcements_d", "{!}kingdom 8 reinforcements d", icon_people_player|pf_label_small, 0, fac_commoners, aggressiveness_0, [(trp_lyseni_pirate, 2, 4), (trp_lyseni_pirate, 2, 4), (trp_lyseni_pirate, 2, 4), (trp_lyseni_pirate, 2, 4), (trp_lyseni_pirate, 2, 4), (trp_lyseni_pirate, 1, 2)]),

	("saan_reinforcements_e", "{!}kingdom 8 reinforcements e", icon_people_player|pf_label_small, 0, fac_commoners, aggressiveness_0, [(trp_lyseni_pirate, 2, 4), (trp_sarranid_n_ajam8, 2, 4), (trp_sarranid_n_cemaat8, 2, 4), (trp_sarranid_n_jebelus8, 2, 4), (trp_sarranid_n_yerliyya8, 2, 4), (trp_sarranid_n_cemaat8, 1, 2)]),

	("saan_reinforcements_f", "{!}kingdom 8 reinforcements f", icon_people_player|pf_label_small, 0, fac_commoners, aggressiveness_0, [(trp_lyseni_pirate, 2, 4), (trp_dragonstone_troop_1, 2, 4), (trp_sarranid_n_yeniceri8, 2, 4), (trp_sarranid_n_kapikula8, 2, 4), (trp_sarranid_n_uluteci8, 2, 4), (trp_sarranid_n_cemaat8, 1, 2)]),

	("lannister_reinforcements_a", "{!}kingdom 9 reinforcements a", icon_people_player|pf_label_small, 0, fac_commoners, aggressiveness_0, [(trp_casterly_rock_man_at_arms, 2, 4), (trp_lannisport_spearman, 2, 4), (trp_sarranid_n_cemaat9, 2, 4), (trp_sarranid_n_jebelus9, 2, 4), (trp_sarranid_n_yerliyya9, 2, 4), (trp_sarranid_n_cemaat9, 1, 2)]),

	("lannister_reinforcements_b", "{!}kingdom 9 reinforcements b", icon_people_player|pf_label_small, 0, fac_commoners, aggressiveness_0, [(trp_casterly_rock_man_at_arms, 2, 4), (trp_lannisport_spearman, 2, 4), (trp_sarranid_n_cemaat9, 2, 4), (trp_sarranid_n_jebelus9, 2, 4), (trp_sarranid_n_yerliyya9, 2, 4), (trp_sarranid_n_cemaat9, 1, 2)]),

	("lannister_reinforcements_c", "{!}kingdom 9 reinforcements c", icon_people_player|pf_label_small, 0, fac_commoners, aggressiveness_0, [(trp_casterly_rock_man_at_arms, 2, 4), (trp_lannisport_spearman, 2, 4), (trp_sarranid_n_cemaat9, 2, 4), (trp_sarranid_n_jebelus9, 2, 4), (trp_sarranid_n_yerliyya9, 2, 4), (trp_sarranid_n_cemaat9, 1, 2)]),

	("lannister_reinforcements_d", "{!}kingdom 9 reinforcements d", icon_people_player|pf_label_small, 0, fac_commoners, aggressiveness_0, [(trp_casterly_rock_man_at_arms, 2, 4), (trp_lannisport_spearman, 2, 4), (trp_sarranid_n_yeniceri9, 2, 4), (trp_sarranid_n_kapikula9, 2, 4), (trp_sarranid_n_uluteci9, 2, 4), (trp_sarranid_n_cemaat9, 1, 2)]),

	("lannister_reinforcements_e", "{!}kingdom 9 reinforcements e", icon_people_player|pf_label_small, 0, fac_commoners, aggressiveness_0, [(trp_casterly_rock_man_at_arms, 2, 4), (trp_lannisport_spearman, 2, 4), (trp_sarranid_n_cemaat9, 2, 4), (trp_sarranid_n_jebelus9, 2, 4), (trp_sarranid_n_yerliyya9, 2, 4), (trp_sarranid_n_cemaat9, 1, 2)]),

	("lannister_reinforcements_f", "{!}kingdom 9 reinforcements f", icon_people_player|pf_label_small, 0, fac_commoners, aggressiveness_0, [(trp_casterly_rock_man_at_arms, 2, 4), (trp_lannisport_spearman, 2, 4), (trp_sarranid_n_yeniceri9, 2, 4), (trp_sarranid_n_kapikula9, 2, 4), (trp_sarranid_n_uluteci9, 2, 4), (trp_sarranid_n_cemaat9, 1, 2)]),

	("redwyne_reinforcements_a", "{!}kingdom 10 reinforcements a", icon_people_player|pf_label_small, 0, fac_commoners, aggressiveness_0, [(trp_oldtown_knight, 2, 4), (trp_sarranid_n_ajam10, 2, 4), (trp_sarranid_n_cemaat10, 2, 4), (trp_sarranid_n_jebelus10, 2, 4), (trp_sarranid_n_yerliyya10, 2, 4), (trp_reach_squire, 1, 2)]),

	("redwyne_reinforcements_b", "{!}kingdom 10 reinforcements b", icon_people_player|pf_label_small, 0, fac_commoners, aggressiveness_0, [(trp_oldtown_knight, 2, 4), (trp_sarranid_n_ajam10, 2, 4), (trp_sarranid_n_cemaat10, 2, 4), (trp_sarranid_n_jebelus10, 2, 4), (trp_sarranid_n_yerliyya10, 2, 4), (trp_sarranid_n_cemaat10, 1, 2)]),

	("redwyne_reinforcements_c", "{!}kingdom 10 reinforcements c", icon_people_player|pf_label_small, 0, fac_commoners, aggressiveness_0, [(trp_oldtown_knight, 2, 4), (trp_sarranid_n_ajam10, 2, 4), (trp_sarranid_n_cemaat10, 2, 4), (trp_sarranid_n_jebelus10, 2, 4), (trp_sarranid_n_yerliyya10, 2, 4), (trp_sarranid_n_cemaat10, 1, 2)]),

	("redwyne_reinforcements_d", "{!}kingdom 10 reinforcements d", icon_people_player|pf_label_small, 0, fac_commoners, aggressiveness_0, [(trp_oldtown_knight, 2, 4), (trp_reach_troop_1, 2, 4), (trp_sarranid_n_yeniceri10, 2, 4), (trp_sarranid_n_kapikula10, 2, 4), (trp_sarranid_n_uluteci10, 2, 4), (trp_sarranid_n_millet10, 1, 2)]),

	("redwyne_reinforcements_e", "{!}kingdom 10 reinforcements e", icon_people_player|pf_label_small, 0, fac_commoners, aggressiveness_0, [(trp_oldtown_knight, 2, 4), (trp_sarranid_n_ajam10, 2, 4), (trp_sarranid_n_cemaat10, 2, 4), (trp_sarranid_n_jebelus10, 2, 4), (trp_sarranid_n_yerliyya10, 2, 4), (trp_sarranid_n_cemaat10, 1, 2)]),

	("redwyne_reinforcements_f", "{!}kingdom 10 reinforcements f", icon_people_player|pf_label_small, 0, fac_commoners, aggressiveness_0, [(trp_oldtown_knight, 2, 4), (trp_reach_troop_1, 2, 4), (trp_sarranid_n_yeniceri10, 2, 4), (trp_sarranid_n_kapikula10, 2, 4), (trp_sarranid_n_uluteci10, 2, 4), (trp_sarranid_n_millet10, 1, 2)]),

	("tyrell_reinforcements_a", "{!}kingdom 10 reinforcements a", icon_people_player|pf_label_small, 0, fac_commoners, aggressiveness_0, [(trp_oldtown_knight, 2, 4), (trp_sarranid_n_ajam10, 2, 4), (trp_sarranid_n_cemaat10, 2, 4), (trp_sarranid_n_jebelus10, 2, 4), (trp_sarranid_n_yerliyya10, 2, 4), (trp_reach_squire, 1, 2)]),

	("tyrell_reinforcements_b", "{!}kingdom 10 reinforcements b", icon_people_player|pf_label_small, 0, fac_commoners, aggressiveness_0, [(trp_oldtown_knight, 2, 4), (trp_sarranid_n_ajam10, 2, 4), (trp_sarranid_n_cemaat10, 2, 4), (trp_sarranid_n_jebelus10, 2, 4), (trp_sarranid_n_yerliyya10, 2, 4), (trp_sarranid_n_cemaat10, 1, 2)]),

	("tyrell_reinforcements_c", "{!}kingdom 10 reinforcements c", icon_people_player|pf_label_small, 0, fac_commoners, aggressiveness_0, [(trp_oldtown_knight, 2, 4), (trp_sarranid_n_ajam10, 2, 4), (trp_sarranid_n_cemaat10, 2, 4), (trp_sarranid_n_jebelus10, 2, 4), (trp_sarranid_n_yerliyya10, 2, 4), (trp_sarranid_n_cemaat10, 1, 2)]),

	("tyrell_reinforcements_d", "{!}kingdom 10 reinforcements d", icon_people_player|pf_label_small, 0, fac_commoners, aggressiveness_0, [(trp_oldtown_knight, 2, 4), (trp_reach_troop_1, 2, 4), (trp_sarranid_n_yeniceri10, 2, 4), (trp_sarranid_n_kapikula10, 2, 4), (trp_sarranid_n_uluteci10, 2, 4), (trp_sarranid_n_millet10, 1, 2)]),

	("tyrell_reinforcements_e", "{!}kingdom 10 reinforcements e", icon_people_player|pf_label_small, 0, fac_commoners, aggressiveness_0, [(trp_oldtown_knight, 2, 4), (trp_sarranid_n_ajam10, 2, 4), (trp_sarranid_n_cemaat10, 2, 4), (trp_sarranid_n_jebelus10, 2, 4), (trp_sarranid_n_yerliyya10, 2, 4), (trp_sarranid_n_cemaat10, 1, 2)]),

	("tyrell_reinforcements_f", "{!}kingdom 10 reinforcements f", icon_people_player|pf_label_small, 0, fac_commoners, aggressiveness_0, [(trp_oldtown_knight, 2, 4), (trp_reach_troop_1, 2, 4), (trp_sarranid_n_yeniceri10, 2, 4), (trp_sarranid_n_kapikula10, 2, 4), (trp_sarranid_n_uluteci10, 2, 4), (trp_sarranid_n_millet10, 1, 2)]),

	("hightower_reinforcements_a", "{!}kingdom 10 reinforcements a", icon_people_player|pf_label_small, 0, fac_commoners, aggressiveness_0, [(trp_oldtown_knight, 2, 4), (trp_sarranid_n_ajam10, 2, 4), (trp_sarranid_n_cemaat10, 2, 4), (trp_sarranid_n_jebelus10, 2, 4), (trp_sarranid_n_yerliyya10, 2, 4), (trp_reach_squire, 1, 2)]),

	("hightower_reinforcements_b", "{!}kingdom 10 reinforcements b", icon_people_player|pf_label_small, 0, fac_commoners, aggressiveness_0, [(trp_oldtown_knight, 2, 4), (trp_sarranid_n_ajam10, 2, 4), (trp_sarranid_n_cemaat10, 2, 4), (trp_sarranid_n_jebelus10, 2, 4), (trp_sarranid_n_yerliyya10, 2, 4), (trp_sarranid_n_cemaat10, 1, 2)]),

	("hightower_reinforcements_c", "{!}kingdom 10 reinforcements c", icon_people_player|pf_label_small, 0, fac_commoners, aggressiveness_0, [(trp_oldtown_knight, 2, 4), (trp_sarranid_n_ajam10, 2, 4), (trp_sarranid_n_cemaat10, 2, 4), (trp_sarranid_n_jebelus10, 2, 4), (trp_sarranid_n_yerliyya10, 2, 4), (trp_sarranid_n_cemaat10, 1, 2)]),

	("hightower_reinforcements_d", "{!}kingdom 10 reinforcements d", icon_people_player|pf_label_small, 0, fac_commoners, aggressiveness_0, [(trp_oldtown_knight, 2, 4), (trp_reach_troop_1, 2, 4), (trp_sarranid_n_yeniceri10, 2, 4), (trp_sarranid_n_kapikula10, 2, 4), (trp_sarranid_n_uluteci10, 2, 4), (trp_sarranid_n_millet10, 1, 2)]),

	("hightower_reinforcements_e", "{!}kingdom 10 reinforcements e", icon_people_player|pf_label_small, 0, fac_commoners, aggressiveness_0, [(trp_oldtown_knight, 2, 4), (trp_sarranid_n_ajam10, 2, 4), (trp_sarranid_n_cemaat10, 2, 4), (trp_sarranid_n_jebelus10, 2, 4), (trp_sarranid_n_yerliyya10, 2, 4), (trp_sarranid_n_cemaat10, 1, 2)]),

	("hightower_reinforcements_f", "{!}kingdom 10 reinforcements f", icon_people_player|pf_label_small, 0, fac_commoners, aggressiveness_0, [(trp_oldtown_knight, 2, 4), (trp_reach_troop_1, 2, 4), (trp_sarranid_n_yeniceri10, 2, 4), (trp_sarranid_n_kapikula10, 2, 4), (trp_sarranid_n_uluteci10, 2, 4), (trp_sarranid_n_millet10, 1, 2)]),

	("celtigar_reinforcements_a", "{!}kingdom 10 reinforcements a", icon_people_player|pf_label_small, 0, fac_commoners, aggressiveness_0, [(trp_port_claw_isle_archer, 2, 4), (trp_sarranid_n_ajam8, 2, 4), (trp_sarranid_n_cemaat8, 2, 4), (trp_sarranid_n_jebelus8, 2, 4), (trp_sarranid_n_yerliyya8, 2, 4), (trp_sarranid_n_ajam8, 1, 2)]),

	("celtigar_reinforcements_b", "{!}kingdom 10 reinforcements b", icon_people_player|pf_label_small, 0, fac_commoners, aggressiveness_0, [(trp_port_claw_isle_archer, 2, 4), (trp_sarranid_n_ajam8, 2, 4), (trp_sarranid_n_cemaat8, 2, 4), (trp_sarranid_n_jebelus8, 2, 4), (trp_sarranid_n_yerliyya8, 2, 4), (trp_sarranid_n_cemaat8, 1, 2)]),

	("celtigar_reinforcements_c", "{!}kingdom 10 reinforcements c", icon_people_player|pf_label_small, 0, fac_commoners, aggressiveness_0, [(trp_port_claw_isle_archer, 2, 4), (trp_sarranid_n_ajam8, 2, 4), (trp_sarranid_n_cemaat8, 2, 4), (trp_sarranid_n_jebelus8, 2, 4), (trp_sarranid_n_yerliyya8, 2, 4), (trp_sarranid_n_cemaat8, 1, 2)]),

	("celtigar_reinforcements_d", "{!}kingdom 10 reinforcements d", icon_people_player|pf_label_small, 0, fac_commoners, aggressiveness_0, [(trp_port_claw_isle_archer, 2, 4), (trp_sarranid_n_ajam8, 2, 4), (trp_sarranid_n_yeniceri8, 2, 4), (trp_sarranid_n_kapikula8, 2, 4), (trp_sarranid_n_uluteci8, 2, 4), (trp_sarranid_n_millet8, 1, 2)]),

	("celtigar_reinforcements_e", "{!}kingdom 10 reinforcements e", icon_people_player|pf_label_small, 0, fac_commoners, aggressiveness_0, [(trp_port_claw_isle_archer, 2, 4), (trp_sarranid_n_ajam8, 2, 4), (trp_sarranid_n_cemaat8, 2, 4), (trp_sarranid_n_jebelus8, 2, 4), (trp_sarranid_n_yerliyya8, 2, 4), (trp_sarranid_n_cemaat8, 1, 2)]),

	("celtigar_reinforcements_f", "{!}kingdom 10 reinforcements f", icon_people_player|pf_label_small, 0, fac_commoners, aggressiveness_0, [(trp_port_claw_isle_archer, 2, 4), (trp_sarranid_n_ajam8, 2, 4), (trp_sarranid_n_yeniceri8, 2, 4), (trp_sarranid_n_kapikula8, 2, 4), (trp_sarranid_n_uluteci8, 2, 4), (trp_sarranid_n_millet8, 1, 2)]),

	("tarth_reinforcements_a", "{!}kingdom 1 reinforcements a", icon_people_player|pf_label_small, 0, fac_commoners, aggressiveness_0, [(trp_sarranid_n_cemaat1, 2, 4), (trp_sarranid_n_ajam1, 2, 4), (trp_sarranid_n_cemaat1, 2, 4), (trp_sarranid_n_jebelus1, 2, 4), (trp_port_tarth_knight, 2, 4), (trp_port_tarth_knight, 1, 2)]),

	("tarth_reinforcements_b", "{!}kingdom 1 reinforcements b", icon_people_player|pf_label_small, 0, fac_commoners, aggressiveness_0, [(trp_sarranid_n_millet1, 2, 4), (trp_sarranid_n_ajam1, 2, 4), (trp_sarranid_n_cemaat1, 2, 4), (trp_sarranid_n_jebelus1, 2, 4), (trp_port_tarth_knight, 2, 4), (trp_port_tarth_knight, 1, 2)]),

	("tarth_reinforcements_c", "{!}kingdom 1 reinforcements c", icon_people_player|pf_label_small, 0, fac_commoners, aggressiveness_0, [(trp_sarranid_n_millet1, 2, 4), (trp_sarranid_n_ajam1, 2, 4), (trp_sarranid_n_cemaat1, 2, 4), (trp_sarranid_n_jebelus1, 2, 4), (trp_sarranid_n_yerliyya1, 2, 4), (trp_sarranid_n_cemaat1, 1, 2)]),

	("tarth_reinforcements_d", "{!}kingdom 1 reinforcements d", icon_people_player|pf_label_small, 0, fac_commoners, aggressiveness_0, [(trp_sarranid_n_millet1, 2, 4), (trp_stormlands_troop_1, 2, 4), (trp_sarranid_n_yeniceri1, 2, 4), (trp_sarranid_n_kapikula1, 2, 4), (trp_sarranid_n_uluteci1, 2, 4), (trp_sarranid_n_cemaat1, 1, 2)]),

	("tarth_reinforcements_e", "{!}kingdom 1 reinforcements e", icon_people_player|pf_label_small, 0, fac_commoners, aggressiveness_0, [(trp_sarranid_n_millet1, 2, 4), (trp_sarranid_n_ajam1, 2, 4), (trp_sarranid_n_cemaat1, 2, 4), (trp_sarranid_n_jebelus1, 2, 4), (trp_sarranid_n_yerliyya1, 2, 4), (trp_sarranid_n_cemaat1, 1, 2)]),

	("tarth_reinforcements_f", "{!}kingdom 1 reinforcements f", icon_people_player|pf_label_small, 0, fac_commoners, aggressiveness_0, [(trp_sarranid_n_garip1, 2, 4), (trp_stormlands_troop_1, 2, 4), (trp_sarranid_n_yeniceri1, 2, 4), (trp_sarranid_n_kapikula1, 2, 4), (trp_sarranid_n_uluteci1, 2, 4), (trp_sarranid_n_cemaat1, 1, 2)]),

	("grafton_reinforcements_a", "{!}kingdom 3 reinforcements a", icon_people_player|pf_label_small, 0, fac_commoners, aggressiveness_0, [(trp_sarranid_n_millet3, 2, 4), (trp_sarranid_n_ajam3, 2, 4), (trp_sarranid_n_cemaat3, 2, 4), (trp_sarranid_n_jebelus3, 2, 4), (trp_port_gulltown_knight, 2, 4), (trp_port_gulltown_knight, 1, 2)]),

	("grafton_reinforcements_b", "{!}kingdom 3 reinforcements b", icon_people_player|pf_label_small, 0, fac_commoners, aggressiveness_0, [(trp_sarranid_n_millet3, 2, 4), (trp_sarranid_n_ajam3, 2, 4), (trp_sarranid_n_cemaat3, 2, 4), (trp_sarranid_n_jebelus3, 2, 4), (trp_port_gulltown_knight, 2, 4), (trp_port_gulltown_knight, 1, 2)]),

	("grafton_reinforcements_c", "{!}kingdom 3 reinforcements c", icon_people_player|pf_label_small, 0, fac_commoners, aggressiveness_0, [(trp_sarranid_n_millet3, 2, 4), (trp_sarranid_n_ajam3, 2, 4), (trp_sarranid_n_cemaat3, 2, 4), (trp_sarranid_n_jebelus3, 2, 4), (trp_sarranid_n_yerliyya3, 2, 4), (trp_sarranid_n_cemaat3, 1, 2)]),

	("grafton_reinforcements_d", "{!}kingdom 3 reinforcements d", icon_people_player|pf_label_small, 0, fac_commoners, aggressiveness_0, [(trp_sarranid_n_garip3, 2, 4), (trp_vale_troop_1, 2, 4), (trp_sarranid_n_yeniceri3, 2, 4), (trp_sarranid_n_kapikula3, 2, 4), (trp_sarranid_n_uluteci3, 2, 4), (trp_sarranid_n_cemaat3, 1, 2)]),

	("grafton_reinforcements_e", "{!}kingdom 3 reinforcements e", icon_people_player|pf_label_small, 0, fac_commoners, aggressiveness_0, [(trp_sarranid_n_millet3, 2, 4), (trp_sarranid_n_ajam3, 2, 4), (trp_sarranid_n_cemaat3, 2, 4), (trp_sarranid_n_jebelus3, 2, 4), (trp_sarranid_n_yerliyya3, 2, 4), (trp_sarranid_n_cemaat3, 1, 2)]),

	("grafton_reinforcements_f", "{!}kingdom 3 reinforcements f", icon_people_player|pf_label_small, 0, fac_commoners, aggressiveness_0, [(trp_sarranid_n_garip3, 2, 4), (trp_vale_troop_1, 2, 4), (trp_sarranid_n_yeniceri3, 2, 4), (trp_sarranid_n_kapikula3, 2, 4), (trp_sarranid_n_uluteci3, 2, 4), (trp_sarranid_n_cemaat3, 1, 2)]),

	("kingswood_reinforcements_a", "{!}kingdom 1 reinforcements a", icon_people_player|pf_label_small, 0, fac_commoners, aggressiveness_0, [(trp_port_kingswood_archers, 2, 4), (trp_sarranid_n_ajam1, 2, 4), (trp_sarranid_n_cemaat1, 2, 4), (trp_sarranid_n_jebelus1, 2, 4), (trp_port_kingswood_archers, 2, 4), (trp_port_kingswood_archers, 1, 2)]),

	("kingswood_reinforcements_b", "{!}kingdom 1 reinforcements b", icon_people_player|pf_label_small, 0, fac_commoners, aggressiveness_0, [(trp_port_kingswood_archers, 2, 4), (trp_sarranid_n_ajam1, 2, 4), (trp_sarranid_n_cemaat1, 2, 4), (trp_sarranid_n_jebelus1, 2, 4), (trp_port_kingswood_archers, 2, 4), (trp_port_kingswood_archers, 1, 2)]),

	("kingswood_reinforcements_c", "{!}kingdom 1 reinforcements c", icon_people_player|pf_label_small, 0, fac_commoners, aggressiveness_0, [(trp_port_kingswood_archers, 2, 4), (trp_sarranid_n_ajam1, 2, 4), (trp_sarranid_n_cemaat1, 2, 4), (trp_sarranid_n_jebelus1, 2, 4), (trp_sarranid_n_yerliyya1, 2, 4), (trp_sarranid_n_cemaat1, 1, 2)]),

	("kingswood_reinforcements_d", "{!}kingdom 1 reinforcements d", icon_people_player|pf_label_small, 0, fac_commoners, aggressiveness_0, [(trp_sarranid_n_millet1, 2, 4), (trp_stormlands_troop_1, 2, 4), (trp_sarranid_n_yeniceri1, 2, 4), (trp_sarranid_n_kapikula1, 2, 4), (trp_sarranid_n_uluteci1, 2, 4), (trp_sarranid_n_cemaat1, 1, 2)]),

	("kingswood_reinforcements_e", "{!}kingdom 1 reinforcements e", icon_people_player|pf_label_small, 0, fac_commoners, aggressiveness_0, [(trp_sarranid_n_millet1, 2, 4), (trp_sarranid_n_ajam1, 2, 4), (trp_sarranid_n_cemaat1, 2, 4), (trp_sarranid_n_jebelus1, 2, 4), (trp_sarranid_n_yerliyya1, 2, 4), (trp_sarranid_n_cemaat1, 1, 2)]),

	("kingswood_reinforcements_f", "{!}kingdom 1 reinforcements f", icon_people_player|pf_label_small, 0, fac_commoners, aggressiveness_0, [(trp_sarranid_n_garip1, 2, 4), (trp_stormlands_troop_1, 2, 4), (trp_sarranid_n_yeniceri1, 2, 4), (trp_sarranid_n_kapikula1, 2, 4), (trp_sarranid_n_uluteci1, 2, 4), (trp_sarranid_n_cemaat1, 1, 2)]),

	("windblown_reinforcements_a", "{!}kingdom 1 reinforcements a", icon_people_player|pf_label_small, 0, fac_commoners, aggressiveness_0, [(trp_windblown_crossbowman, 2, 4), (trp_windblown_infantry, 2, 4), (trp_windblown_infantry, 2, 4), (trp_windblown_pikeman, 2, 4), (trp_windblown_archer, 2, 4), (trp_windblown_lancer, 1, 2)]),

	("windblown_reinforcements_b", "{!}kingdom 1 reinforcements b", icon_people_player|pf_label_small, 0, fac_commoners, aggressiveness_0, [(trp_windblown_crossbowman, 2, 4), (trp_windblown_infantry, 2, 4), (trp_windblown_infantry, 2, 4), (trp_windblown_pikeman, 2, 4), (trp_windblown_archer, 2, 4), (trp_windblown_lancer, 1, 2)]),

	("windblown_reinforcements_c", "{!}kingdom 1 reinforcements c", icon_people_player|pf_label_small, 0, fac_commoners, aggressiveness_0, [(trp_windblown_crossbowman, 2, 4), (trp_windblown_infantry, 2, 4), (trp_windblown_infantry, 2, 4), (trp_windblown_pikeman, 2, 4), (trp_windblown_archer, 2, 4), (trp_windblown_lancer, 1, 2)]),

	("windblown_reinforcements_d", "{!}kingdom 1 reinforcements d", icon_people_player|pf_label_small, 0, fac_commoners, aggressiveness_0, [(trp_windblown_pikeman, 2, 4), (trp_windblown_infantry, 2, 4), (trp_windblown_pikeman, 2, 4), (trp_windblown_archer, 2, 4), (trp_windblown_archer, 2, 4), (trp_windblown_pikeman, 1, 2)]),

	("windblown_reinforcements_e", "{!}kingdom 1 reinforcements e", icon_people_player|pf_label_small, 0, fac_commoners, aggressiveness_0, [(trp_windblown_pikeman, 2, 4), (trp_windblown_infantry, 2, 4), (trp_windblown_pikeman, 2, 4), (trp_windblown_archer, 2, 4), (trp_windblown_archer, 2, 4), (trp_windblown_pikeman, 1, 2)]),

	("windblown_reinforcements_f", "{!}kingdom 1 reinforcements f", icon_people_player|pf_label_small, 0, fac_commoners, aggressiveness_0, [(trp_windblown_pikeman, 2, 4), (trp_windblown_infantry, 2, 4), (trp_windblown_pikeman, 2, 4), (trp_windblown_archer, 2, 4), (trp_windblown_archer, 2, 4), (trp_windblown_pikeman, 1, 2)]),

	("company_cat_reinforcements_a", "{!}kingdom 1 reinforcements a", icon_people_player|pf_label_small, 0, fac_commoners, aggressiveness_0, [(trp_company_of_the_cat_pikeman, 2, 4), (trp_company_of_the_cat_pikeman, 2, 4), (trp_company_of_the_cat_infantry, 2, 4), (trp_company_of_the_cat_infantry, 2, 4), (trp_company_of_the_cat_infantry, 2, 4), (trp_company_of_the_cat_infantry, 1, 2)]),

	("company_cat_reinforcements_b", "{!}kingdom 1 reinforcements b", icon_people_player|pf_label_small, 0, fac_commoners, aggressiveness_0, [(trp_company_of_the_cat_pikeman, 2, 4), (trp_company_of_the_cat_pikeman, 2, 4), (trp_company_of_the_cat_infantry, 2, 4), (trp_company_of_the_cat_infantry, 2, 4), (trp_company_of_the_cat_infantry, 2, 4), (trp_company_of_the_cat_infantry, 1, 2)]),

	("company_cat_reinforcements_c", "{!}kingdom 1 reinforcements c", icon_people_player|pf_label_small, 0, fac_commoners, aggressiveness_0, [(trp_company_of_the_cat_pikeman, 2, 4), (trp_company_of_the_cat_pikeman, 2, 4), (trp_company_of_the_cat_infantry, 2, 4), (trp_company_of_the_cat_infantry, 2, 4), (trp_company_of_the_cat_infantry, 2, 4), (trp_company_of_the_cat_infantry, 1, 2)]),

	("company_cat_reinforcements_d", "{!}kingdom 1 reinforcements d", icon_people_player|pf_label_small, 0, fac_commoners, aggressiveness_0, [(trp_company_of_the_cat_spearman, 2, 4), (trp_company_of_the_cat_spearman, 2, 4), (trp_company_of_the_cat_archer, 2, 4), (trp_company_of_the_cat_archer, 2, 4), (trp_company_of_the_cat_infantry, 2, 4), (trp_company_of_the_cat_infantry, 1, 2)]),

	("company_cat_reinforcements_e", "{!}kingdom 1 reinforcements e", icon_people_player|pf_label_small, 0, fac_commoners, aggressiveness_0, [(trp_company_of_the_cat_spearman, 2, 4), (trp_company_of_the_cat_spearman, 2, 4), (trp_company_of_the_cat_archer, 2, 4), (trp_company_of_the_cat_archer, 2, 4), (trp_company_of_the_cat_infantry, 2, 4), (trp_company_of_the_cat_infantry, 1, 2)]),

	("company_cat_reinforcements_f", "{!}kingdom 1 reinforcements f", icon_people_player|pf_label_small, 0, fac_commoners, aggressiveness_0, [(trp_company_of_the_cat_spearman, 2, 4), (trp_company_of_the_cat_spearman, 2, 4), (trp_company_of_the_cat_archer, 2, 4), (trp_company_of_the_cat_archer, 2, 4), (trp_company_of_the_cat_infantry, 2, 4), (trp_company_of_the_cat_infantry, 1, 2)]),

	("town_16_reinforcements_a", "{!}", icon_people_player|pf_label_small, 0, fac_commoners, aggressiveness_0, [(trp_goldcloak_1, 3, 5), (trp_goldcloak_2, 3, 5), (trp_goldcloak_3, 3, 5), (trp_goldcloak_4, 3, 5), (trp_goldcloak_5, 3, 5), (trp_mercenary_infantry_2, 3, 5)]),

	("town_16_reinforcements_b", "{!}", icon_people_player|pf_label_small, 0, fac_commoners, aggressiveness_0, [(trp_goldcloak_1, 3, 5), (trp_goldcloak_2, 3, 5), (trp_goldcloak_3, 3, 5), (trp_goldcloak_4, 3, 5), (trp_goldcloak_5, 3, 5), (trp_mercenary_infantry_2, 3, 5)]),

	("town_16_reinforcements_c", "{!}", icon_people_player|pf_label_small, 0, fac_commoners, aggressiveness_0, [(trp_goldcloak_1, 3, 5), (trp_goldcloak_2, 3, 5), (trp_goldcloak_3, 3, 5), (trp_goldcloak_4, 3, 5), (trp_goldcloak_5, 3, 5), (trp_mercenary_infantry_3, 3, 5)]),

	("town_16_reinforcements_d", "{!}", icon_people_player|pf_label_small, 0, fac_commoners, aggressiveness_0, [(trp_goldcloak_1, 3, 5), (trp_goldcloak_2, 3, 5), (trp_goldcloak_3, 3, 5), (trp_goldcloak_4, 3, 5), (trp_goldcloak_5, 3, 5), (trp_mercenary_archer_2, 3, 5)]),

	("town_16_reinforcements_e", "{!}", icon_people_player|pf_label_small, 0, fac_commoners, aggressiveness_0, [(trp_goldcloak_1, 3, 5), (trp_goldcloak_2, 3, 5), (trp_goldcloak_3, 3, 5), (trp_goldcloak_4, 3, 5), (trp_goldcloak_5, 3, 5), (trp_mercenary_archer_2, 3, 5)]),

	("town_16_reinforcements_f", "{!}", icon_people_player|pf_label_small, 0, fac_commoners, aggressiveness_0, [(trp_goldcloak_1, 3, 5), (trp_goldcloak_2, 3, 5), (trp_goldcloak_3, 3, 5), (trp_goldcloak_4, 3, 5), (trp_goldcloak_5, 3, 5), (trp_mercenary_archer_3, 3, 5)]),

	("town_17_reinforcements_a", "{!}", icon_people_player|pf_label_small, 0, fac_commoners, aggressiveness_0, [(trp_lance_infantry_4, 3, 5), (trp_lance_infantry_5, 3, 5), (trp_lance_archer_1, 3, 5), (trp_lance_archer_3, 3, 5), (trp_lance_infantry_3, 3, 5), (trp_lance_archer_5, 3, 5)]),

	("town_17_reinforcements_b", "{!}", icon_people_player|pf_label_small, 0, fac_commoners, aggressiveness_0, [(trp_lance_infantry_4, 3, 5), (trp_lance_infantry_5, 3, 5), (trp_lance_archer_1, 3, 5), (trp_lance_archer_3, 3, 5), (trp_lance_infantry_3, 3, 5), (trp_lance_archer_5, 3, 5)]),

	("town_17_reinforcements_c", "{!}", icon_people_player|pf_label_small, 0, fac_commoners, aggressiveness_0, [(trp_lance_infantry_4, 3, 5), (trp_lance_infantry_5, 3, 5), (trp_lance_archer_1, 3, 5), (trp_lance_archer_3, 3, 5), (trp_lance_infantry_3, 3, 5), (trp_lance_archer_5, 3, 5)]),

	("town_17_reinforcements_d", "{!}", icon_people_player|pf_label_small, 0, fac_commoners, aggressiveness_0, [(trp_lance_infantry_4, 3, 5), (trp_lance_infantry_5, 3, 5), (trp_lance_archer_1, 3, 5), (trp_lance_archer_3, 3, 5), (trp_lance_infantry_3, 3, 5), (trp_lance_archer_5, 3, 5)]),

	("town_17_reinforcements_e", "{!}", icon_people_player|pf_label_small, 0, fac_commoners, aggressiveness_0, [(trp_lance_infantry_4, 3, 5), (trp_lance_infantry_5, 3, 5), (trp_lance_archer_1, 3, 5), (trp_lance_archer_3, 3, 5), (trp_lance_infantry_3, 3, 5), (trp_lance_archer_5, 3, 5)]),

	("town_17_reinforcements_f", "{!}", icon_people_player|pf_label_small, 0, fac_commoners, aggressiveness_0, [(trp_lance_infantry_4, 3, 5), (trp_lance_infantry_5, 3, 5), (trp_lance_archer_1, 3, 5), (trp_lance_archer_3, 3, 5), (trp_lance_infantry_3, 3, 5), (trp_lance_archer_5, 3, 5)]),

	("town_40_reinforcements_a", "{!}", icon_people_player|pf_label_small, 0, fac_commoners, aggressiveness_0, [(trp_lance_infantry_4, 3, 5), (trp_lance_infantry_5, 3, 5), (trp_lance_archer_1, 3, 5), (trp_lance_archer_3, 3, 5), (trp_lance_infantry_3, 3, 5), (trp_lance_archer_5, 3, 5)]),

	("town_40_reinforcements_b", "{!}", icon_people_player|pf_label_small, 0, fac_commoners, aggressiveness_0, [(trp_lance_infantry_4, 3, 5), (trp_lance_infantry_5, 3, 5), (trp_lance_archer_1, 3, 5), (trp_lance_archer_3, 3, 5), (trp_lance_infantry_3, 3, 5), (trp_lance_archer_5, 3, 5)]),

	("town_40_reinforcements_c", "{!}", icon_people_player|pf_label_small, 0, fac_commoners, aggressiveness_0, [(trp_lance_infantry_4, 3, 5), (trp_lance_infantry_5, 3, 5), (trp_lance_archer_1, 3, 5), (trp_lance_archer_3, 3, 5), (trp_lance_infantry_3, 3, 5), (trp_lance_archer_5, 3, 5)]),

	("town_40_reinforcements_d", "{!}", icon_people_player|pf_label_small, 0, fac_commoners, aggressiveness_0, [(trp_lance_infantry_4, 3, 5), (trp_lance_infantry_5, 3, 5), (trp_lance_archer_1, 3, 5), (trp_lance_archer_3, 3, 5), (trp_lance_infantry_3, 3, 5), (trp_lance_archer_5, 3, 5)]),

	("town_40_reinforcements_e", "{!}", icon_people_player|pf_label_small, 0, fac_commoners, aggressiveness_0, [(trp_lance_infantry_4, 3, 5), (trp_lance_infantry_5, 3, 5), (trp_lance_archer_1, 3, 5), (trp_lance_archer_3, 3, 5), (trp_lance_infantry_3, 3, 5), (trp_lance_archer_5, 3, 5)]),

	("town_40_reinforcements_f", "{!}", icon_people_player|pf_label_small, 0, fac_commoners, aggressiveness_0, [(trp_lance_infantry_4, 3, 5), (trp_lance_infantry_5, 3, 5), (trp_lance_archer_1, 3, 5), (trp_lance_archer_3, 3, 5), (trp_lance_infantry_3, 3, 5), (trp_lance_archer_5, 3, 5)]),

	("town_51_reinforcements_a", "{!}", icon_people_player|pf_label_small, 0, fac_commoners, aggressiveness_0, [(trp_lance_infantry_4, 3, 5), (trp_lance_infantry_5, 3, 5), (trp_lance_archer_1, 3, 5), (trp_lance_archer_3, 3, 5), (trp_lance_infantry_3, 3, 5), (trp_lance_archer_5, 3, 5)]),

	("town_51_reinforcements_b", "{!}", icon_people_player|pf_label_small, 0, fac_commoners, aggressiveness_0, [(trp_lance_infantry_4, 3, 5), (trp_lance_infantry_5, 3, 5), (trp_lance_archer_1, 3, 5), (trp_lance_archer_3, 3, 5), (trp_lance_infantry_3, 3, 5), (trp_lance_archer_5, 3, 5)]),

	("town_51_reinforcements_c", "{!}", icon_people_player|pf_label_small, 0, fac_commoners, aggressiveness_0, [(trp_lance_infantry_4, 3, 5), (trp_lance_infantry_5, 3, 5), (trp_lance_archer_1, 3, 5), (trp_lance_archer_3, 3, 5), (trp_lance_infantry_3, 3, 5), (trp_lance_archer_5, 3, 5)]),

	("town_51_reinforcements_d", "{!}", icon_people_player|pf_label_small, 0, fac_commoners, aggressiveness_0, [(trp_lance_infantry_4, 3, 5), (trp_lance_infantry_5, 3, 5), (trp_lance_archer_1, 3, 5), (trp_lance_archer_3, 3, 5), (trp_lance_infantry_3, 3, 5), (trp_lance_archer_5, 3, 5)]),

	("town_51_reinforcements_e", "{!}", icon_people_player|pf_label_small, 0, fac_commoners, aggressiveness_0, [(trp_lance_infantry_4, 3, 5), (trp_lance_infantry_5, 3, 5), (trp_lance_archer_1, 3, 5), (trp_lance_archer_3, 3, 5), (trp_lance_infantry_3, 3, 5), (trp_lance_archer_5, 3, 5)]),

	("town_51_reinforcements_f", "{!}", icon_people_player|pf_label_small, 0, fac_commoners, aggressiveness_0, [(trp_lance_infantry_4, 3, 5), (trp_lance_infantry_5, 3, 5), (trp_lance_archer_1, 3, 5), (trp_lance_archer_3, 3, 5), (trp_lance_infantry_3, 3, 5), (trp_lance_archer_5, 3, 5)]),

	("town_47_reinforcements_a", "{!}", icon_people_player|pf_label_small, 0, fac_commoners, aggressiveness_0, [(trp_lance_infantry_4, 3, 5), (trp_lance_infantry_5, 3, 5), (trp_lance_archer_1, 3, 5), (trp_lance_archer_3, 3, 5), (trp_lance_infantry_3, 3, 5), (trp_lance_archer_5, 3, 5)]),

	("town_47_reinforcements_b", "{!}", icon_people_player|pf_label_small, 0, fac_commoners, aggressiveness_0, [(trp_lance_infantry_4, 3, 5), (trp_lance_infantry_5, 3, 5), (trp_lance_archer_1, 3, 5), (trp_lance_archer_3, 3, 5), (trp_lance_infantry_3, 3, 5), (trp_lance_archer_5, 3, 5)]),

	("town_47_reinforcements_c", "{!}", icon_people_player|pf_label_small, 0, fac_commoners, aggressiveness_0, [(trp_lance_infantry_4, 3, 5), (trp_lance_infantry_5, 3, 5), (trp_lance_archer_1, 3, 5), (trp_lance_archer_3, 3, 5), (trp_lance_infantry_3, 3, 5), (trp_lance_archer_5, 3, 5)]),

	("town_47_reinforcements_d", "{!}", icon_people_player|pf_label_small, 0, fac_commoners, aggressiveness_0, [(trp_lance_infantry_4, 3, 5), (trp_lance_infantry_5, 3, 5), (trp_lance_archer_1, 3, 5), (trp_lance_archer_3, 3, 5), (trp_lance_infantry_3, 3, 5), (trp_lance_archer_5, 3, 5)]),

	("town_47_reinforcements_e", "{!}", icon_people_player|pf_label_small, 0, fac_commoners, aggressiveness_0, [(trp_lance_infantry_4, 3, 5), (trp_lance_infantry_5, 3, 5), (trp_lance_archer_1, 3, 5), (trp_lance_archer_3, 3, 5), (trp_lance_infantry_3, 3, 5), (trp_lance_archer_5, 3, 5)]),

	("town_47_reinforcements_f", "{!}", icon_people_player|pf_label_small, 0, fac_commoners, aggressiveness_0, [(trp_lance_infantry_4, 3, 5), (trp_lance_infantry_5, 3, 5), (trp_lance_archer_1, 3, 5), (trp_lance_archer_3, 3, 5), (trp_lance_infantry_3, 3, 5), (trp_lance_archer_5, 3, 5)]),

	("town_45_reinforcements_a", "{!}", icon_people_player|pf_label_small, 0, fac_commoners, aggressiveness_0, [(trp_lance_infantry_4, 3, 5), (trp_lance_infantry_5, 3, 5), (trp_lance_archer_1, 3, 5), (trp_lance_archer_3, 3, 5), (trp_lance_infantry_3, 3, 5), (trp_lance_archer_5, 3, 5)]),

	("town_45_reinforcements_b", "{!}", icon_people_player|pf_label_small, 0, fac_commoners, aggressiveness_0, [(trp_lance_infantry_4, 3, 5), (trp_lance_infantry_5, 3, 5), (trp_lance_archer_1, 3, 5), (trp_lance_archer_3, 3, 5), (trp_lance_infantry_3, 3, 5), (trp_lance_archer_5, 3, 5)]),

	("town_45_reinforcements_c", "{!}", icon_people_player|pf_label_small, 0, fac_commoners, aggressiveness_0, [(trp_lance_infantry_4, 3, 5), (trp_lance_infantry_5, 3, 5), (trp_lance_archer_1, 3, 5), (trp_lance_archer_3, 3, 5), (trp_lance_infantry_3, 3, 5), (trp_lance_archer_5, 3, 5)]),

	("town_45_reinforcements_d", "{!}", icon_people_player|pf_label_small, 0, fac_commoners, aggressiveness_0, [(trp_lance_infantry_4, 3, 5), (trp_lance_infantry_5, 3, 5), (trp_lance_archer_1, 3, 5), (trp_lance_archer_3, 3, 5), (trp_lance_infantry_3, 3, 5), (trp_lance_archer_5, 3, 5)]),

	("town_45_reinforcements_e", "{!}", icon_people_player|pf_label_small, 0, fac_commoners, aggressiveness_0, [(trp_lance_infantry_4, 3, 5), (trp_lance_infantry_5, 3, 5), (trp_lance_archer_1, 3, 5), (trp_lance_archer_3, 3, 5), (trp_lance_infantry_3, 3, 5), (trp_lance_archer_5, 3, 5)]),

	("town_45_reinforcements_f", "{!}", icon_people_player|pf_label_small, 0, fac_commoners, aggressiveness_0, [(trp_lance_infantry_4, 3, 5), (trp_lance_infantry_5, 3, 5), (trp_lance_archer_1, 3, 5), (trp_lance_archer_3, 3, 5), (trp_lance_infantry_3, 3, 5), (trp_lance_archer_5, 3, 5)]),

	("town_46_reinforcements_a", "{!}", icon_people_player|pf_label_small, 0, fac_commoners, aggressiveness_0, [(trp_lance_infantry_4, 3, 5), (trp_lance_infantry_5, 3, 5), (trp_lance_archer_1, 3, 5), (trp_lance_archer_3, 3, 5), (trp_lance_infantry_3, 3, 5), (trp_lance_archer_5, 3, 5)]),

	("town_46_reinforcements_b", "{!}", icon_people_player|pf_label_small, 0, fac_commoners, aggressiveness_0, [(trp_lance_infantry_4, 3, 5), (trp_lance_infantry_5, 3, 5), (trp_lance_archer_1, 3, 5), (trp_lance_archer_3, 3, 5), (trp_lance_infantry_3, 3, 5), (trp_lance_archer_5, 3, 5)]),

	("town_46_reinforcements_c", "{!}", icon_people_player|pf_label_small, 0, fac_commoners, aggressiveness_0, [(trp_lance_infantry_4, 3, 5), (trp_lance_infantry_5, 3, 5), (trp_lance_archer_1, 3, 5), (trp_lance_archer_3, 3, 5), (trp_lance_infantry_3, 3, 5), (trp_lance_archer_5, 3, 5)]),

	("town_46_reinforcements_d", "{!}", icon_people_player|pf_label_small, 0, fac_commoners, aggressiveness_0, [(trp_lance_infantry_4, 3, 5), (trp_lance_infantry_5, 3, 5), (trp_lance_archer_1, 3, 5), (trp_lance_archer_3, 3, 5), (trp_lance_infantry_3, 3, 5), (trp_lance_archer_5, 3, 5)]),

	("town_46_reinforcements_e", "{!}", icon_people_player|pf_label_small, 0, fac_commoners, aggressiveness_0, [(trp_lance_infantry_4, 3, 5), (trp_lance_infantry_5, 3, 5), (trp_lance_archer_1, 3, 5), (trp_lance_archer_3, 3, 5), (trp_lance_infantry_3, 3, 5), (trp_lance_archer_5, 3, 5)]),

	("town_46_reinforcements_f", "{!}", icon_people_player|pf_label_small, 0, fac_commoners, aggressiveness_0, [(trp_lance_infantry_4, 3, 5), (trp_lance_infantry_5, 3, 5), (trp_lance_archer_1, 3, 5), (trp_lance_archer_3, 3, 5), (trp_lance_infantry_3, 3, 5), (trp_lance_archer_5, 3, 5)]),

	("town_44_reinforcements_a", "{!}", icon_people_player|pf_label_small, 0, fac_commoners, aggressiveness_0, [(trp_unsullied, 4, 5), (trp_unsullied, 4, 5), (trp_unsullied, 4, 5), (trp_unsullied, 4, 5), (trp_unsullied, 4, 5), (trp_unsullied, 4, 5)]),

	("town_44_reinforcements_b", "{!}", icon_people_player|pf_label_small, 0, fac_commoners, aggressiveness_0, [(trp_unsullied, 4, 5), (trp_unsullied, 4, 5), (trp_unsullied, 4, 5), (trp_unsullied, 4, 5), (trp_unsullied, 4, 5), (trp_unsullied, 4, 5)]),

	("town_44_reinforcements_c", "{!}", icon_people_player|pf_label_small, 0, fac_commoners, aggressiveness_0, [(trp_unsullied, 4, 5), (trp_unsullied, 4, 5), (trp_unsullied, 4, 5), (trp_unsullied, 4, 5), (trp_unsullied, 4, 5), (trp_unsullied, 4, 5)]),

	("town_44_reinforcements_d", "{!}", icon_people_player|pf_label_small, 0, fac_commoners, aggressiveness_0, [(trp_unsullied, 4, 5), (trp_unsullied, 4, 5), (trp_unsullied, 4, 5), (trp_unsullied, 4, 5), (trp_unsullied, 4, 5), (trp_unsullied, 4, 5)]),

	("town_44_reinforcements_e", "{!}", icon_people_player|pf_label_small, 0, fac_commoners, aggressiveness_0, [(trp_unsullied, 4, 5), (trp_unsullied, 4, 5), (trp_unsullied, 4, 5), (trp_unsullied, 4, 5), (trp_unsullied, 4, 5), (trp_unsullied, 4, 5)]),

	("town_44_reinforcements_f", "{!}", icon_people_player|pf_label_small, 0, fac_commoners, aggressiveness_0, [(trp_mercenary_archer_3, 4, 5), (trp_mercenary_archer_3, 4, 5), (trp_mercenary_archer_3, 4, 5), (trp_mercenary_archer_3, 4, 5), (trp_mercenary_infantry_1, 4, 5), (trp_mercenary_infantry_1, 4, 5)]),

	("town_12_reinforcements_a", "{!}", icon_people_player|pf_label_small, 0, fac_commoners, aggressiveness_0, [(trp_lance_infantry_4, 4, 5), (trp_lance_infantry_5, 4, 5), (trp_lance_archer_1, 4, 5), (trp_lance_archer_3, 4, 5), (trp_lance_infantry_3, 4, 5), (trp_lance_archer_5, 4, 5)]),

	("town_12_reinforcements_b", "{!}", icon_people_player|pf_label_small, 0, fac_commoners, aggressiveness_0, [(trp_lance_infantry_4, 4, 5), (trp_lance_infantry_5, 4, 5), (trp_lance_archer_1, 4, 5), (trp_lance_archer_3, 4, 5), (trp_lance_infantry_3, 4, 5), (trp_lance_archer_5, 4, 5)]),

	("town_12_reinforcements_c", "{!}", icon_people_player|pf_label_small, 0, fac_commoners, aggressiveness_0, [(trp_lance_infantry_4, 4, 5), (trp_lance_infantry_5, 4, 5), (trp_lance_archer_1, 4, 5), (trp_lance_archer_3, 4, 5), (trp_lance_archer_5, 4, 5), (trp_lance_archer_5, 4, 5)]),

	("town_12_reinforcements_d", "{!}", icon_people_player|pf_label_small, 0, fac_commoners, aggressiveness_0, [(trp_lance_infantry_4, 4, 5), (trp_lance_infantry_5, 4, 5), (trp_lance_archer_1, 4, 5), (trp_lance_archer_3, 4, 5), (trp_lance_archer_5, 4, 5), (trp_unsullied, 4, 5)]),

	("town_12_reinforcements_e", "{!}", icon_people_player|pf_label_small, 0, fac_commoners, aggressiveness_0, [(trp_unsullied, 4, 5), (trp_unsullied, 4, 5), (trp_unsullied, 4, 5), (trp_unsullied, 4, 5), (trp_unsullied, 4, 5), (trp_unsullied, 4, 5)]),

	("town_12_reinforcements_f", "{!}", icon_people_player|pf_label_small, 0, fac_commoners, aggressiveness_0, [(trp_mercenary_infantry_1, 4, 5), (trp_mercenary_archer_3, 4, 5), (trp_mercenary_infantry_1, 4, 5), (trp_mercenary_archer_3, 4, 5), (trp_mercenary_infantry_1, 4, 5), (trp_mercenary_infantry_1, 4, 5)]),

	("steppe_bandit_lair", "Steppe Bandit Lair", icon_bandit_lair|carries_goods(2)|pf_is_static|pf_hide_defenders, 0, fac_neutral, bandit_personality, [(trp_bandit_n_steppe, 15, 116)]),

	("taiga_bandit_lair", "Tundra Bandit Lair", icon_bandit_lair|carries_goods(2)|pf_is_static|pf_hide_defenders, 0, fac_neutral, bandit_personality, [(trp_bandit_n_taiga, 15, 116)]),

	("desert_bandit_lair", "Desert Bandit Lair", icon_bandit_lair|carries_goods(2)|pf_is_static|pf_hide_defenders, 0, fac_neutral, bandit_personality, [(trp_bandit_n_desert, 15, 116)]),

	("forest_bandit_lair", "Forest Bandit Camp", icon_bandit_lair|carries_goods(2)|pf_is_static|pf_hide_defenders, 0, fac_neutral, bandit_personality, [(trp_bandit_n_forest, 15, 116)]),

	("mountain_bandit_lair", "Mountain Bandit Hideout", icon_bandit_lair|carries_goods(2)|pf_is_static|pf_hide_defenders, 0, fac_neutral, bandit_personality, [(trp_bandit_n_mountain, 15, 116)]),

	("sea_raider_lair", "Sea Raider Landing", icon_bandit_lair|carries_goods(2)|pf_is_static|pf_hide_defenders, 0, fac_neutral, bandit_personality, [(trp_bandit_n_sea_raider, 15, 100)]),

	("looter_lair", "Kidnappers' Hideout", icon_bandit_lair|carries_goods(2)|pf_is_static|pf_hide_defenders, 0, fac_neutral, bandit_personality, [(trp_bandit_n_looter, 15, 50)]),

	("bandit_lair_templates_end", "{!}bandit lair templates end", icon_people_axeman|carries_goods(2)|pf_is_static, 0, fac_outlaws, bandit_personality, [(trp_bandit_n_sea_raider, 15, 100)]),

	("leaded_looters", "Band of robbers", icon_people_axeman|carries_goods(8)|pf_quest_party, 0, fac_neutral, bandit_personality, [(trp_looter_leader, 1, 1), (trp_bandit_n_looter, 3, 6)]),

	("steppe_bandit_lair_r", "Steppe Bandit Lair", icon_bandit_lair|carries_goods(2)|pf_is_static|pf_hide_defenders, 0, fac_neutral, bandit_personality, [(trp_bandit_r_steppe, 15, 116)]),

	("taiga_bandit_lair_r", "Tundra Bandit Lair", icon_bandit_lair|carries_goods(2)|pf_is_static|pf_hide_defenders, 0, fac_neutral, bandit_personality, [(trp_bandit_r_taiga, 15, 116)]),

	("desert_bandit_lair_r", "Desert Bandit Lair", icon_bandit_lair|carries_goods(2)|pf_is_static|pf_hide_defenders, 0, fac_neutral, bandit_personality, [(trp_bandit_r_desert, 15, 116)]),

	("forest_bandit_lair_r", "Forest Bandit Camp", icon_bandit_lair|carries_goods(2)|pf_is_static|pf_hide_defenders, 0, fac_neutral, bandit_personality, [(trp_bandit_r_forest, 15, 116)]),

	("mountain_bandit_lair_r", "Mountain Bandit Hideout", icon_bandit_lair|carries_goods(2)|pf_is_static|pf_hide_defenders, 0, fac_neutral, bandit_personality, [(trp_bandit_r_mountain, 15, 116)]),

	("sea_raider_lair_r", "Sea Raider Landing", icon_bandit_lair|carries_goods(2)|pf_is_static|pf_hide_defenders, 0, fac_neutral, bandit_personality, [(trp_bandit_r_sea_raider, 15, 100)]),

	("looter_lair_r", "Kidnappers' Hideout", icon_bandit_lair|carries_goods(2)|pf_is_static|pf_hide_defenders, 0, fac_neutral, bandit_personality, [(trp_bandit_r_looter, 15, 50)]),

	("bandit_lair_templates_end_r", "{!}bandit lair templates end", icon_people_axeman|carries_goods(2)|pf_is_static, 0, fac_outlaws, bandit_personality, [(trp_bandit_r_sea_raider, 15, 100)]),

	("leaded_looters_r", "Band of robbers", icon_people_axeman|carries_goods(8)|pf_quest_party, 0, fac_neutral, bandit_personality, [(trp_looter_leader, 1, 1), (trp_bandit_r_looter, 3, 6)]),

	("steppe_bandit_lair_e", "Dothraki Lair", icon_bandit_lair|carries_goods(2)|pf_is_static|pf_hide_defenders, 0, fac_neutral, bandit_personality, [(trp_bandit_e_steppe, 15, 116)]),

	("taiga_bandit_lair_e", "Wildling Lair", icon_bandit_lair|carries_goods(2)|pf_is_static|pf_hide_defenders, 0, fac_neutral, bandit_personality, [(trp_bandit_e_taiga, 15, 116)]),

	("desert_bandit_lair_e", "Outlaw Lair", icon_bandit_lair|carries_goods(2)|pf_is_static|pf_hide_defenders, 0, fac_neutral, bandit_personality, [(trp_bandit_e_desert, 15, 116)]),

	("forest_bandit_lair_e", "Forest Bandit Camp", icon_bandit_lair|carries_goods(2)|pf_is_static|pf_hide_defenders, 0, fac_neutral, bandit_personality, [(trp_bandit_e_forest, 15, 116)]),

	("mountain_bandit_lair_e", "Mountain Bandit Hideout", icon_bandit_lair|carries_goods(2)|pf_is_static|pf_hide_defenders, 0, fac_neutral, bandit_personality, [(trp_bandit_e_mountain, 15, 116)]),

	("sea_raider_lair_e", "Pirate Landing", icon_bandit_lair|carries_goods(2)|pf_is_static|pf_hide_defenders, 0, fac_neutral, bandit_personality, [(trp_bandit_e_sea_raider, 15, 100)]),

	("looter_lair_e", "Kidnappers' Hideout", icon_bandit_lair|carries_goods(2)|pf_is_static|pf_hide_defenders, 0, fac_neutral, bandit_personality, [(trp_bandit_e_looter, 15, 50)]),

	("bandit_lair_templates_end_e", "{!}bandit lair templates end", icon_people_axeman|carries_goods(2)|pf_is_static, 0, fac_outlaws, bandit_personality, [(trp_bandit_e_sea_raider, 15, 100)]),

	("leaded_looters_e", "Band of robbers", icon_people_axeman|carries_goods(8)|pf_quest_party, 0, fac_neutral, bandit_personality, [(trp_looter_leader, 1, 1), (trp_bandit_e_looter, 3, 6)]),

	("dplmc_spouse", "Your spouse", icon_people_woman|pf_show_faction|pf_civilian, 0, fac_neutral, courage_7|merchant_personality, []),

	("dplmc_gift_caravan", "Your Caravan", icon_people_mule|carries_goods(25)|pf_show_faction, 0, fac_commoners, courage_11|escorted_merchant_personality, [(trp_caravan_master, 1, 1)]),

	("dplmc_gift_caravan_r", "Your Caravan", icon_people_mule|carries_goods(25)|pf_show_faction, 0, fac_commoners, courage_11|escorted_merchant_personality, [(trp_caravan_master, 1, 1)]),

	("dplmc_gift_caravan_e", "Your Caravan", icon_people_mule|carries_goods(25)|pf_show_faction, 0, fac_commoners, courage_11|escorted_merchant_personality, [(trp_caravan_master, 1, 1), (trp_mercenary_infantry_1, 4, 32), (trp_mercenary_infantry_2, 1, 10), (trp_mercenary_infantry_3, 0, 4), (trp_mercenary_archer_3, 0, 4)]),

	("dplmc_recruiter", "Recruiter", icon_people_gray_knight|pf_show_faction, 0, fac_neutral, courage_7|merchant_personality, [(trp_dplmc_recruiter, 1, 1)]),

	("entrench", "Entrenchment", icon_camp_entrench_last|pf_is_static|pf_always_visible|pf_no_label, 0, fac_neutral, bandit_personality, []),

	("reinforcements", "Reinforcements", icon_people_axeman|pf_show_faction, 0, fac_commoners, soldier_personality, []),

	("sea_raiders_ships", "Lyseni Pirates", icon_ship|carries_goods(2)|pf_is_ship, 0, fac_outlaws, bandit_personality, [(trp_bandit_n_sea_raider, 45, 85)]),

	("sea_raiders_ships_r", "Lyseni Pirates", icon_ship|carries_goods(2)|pf_is_ship, 0, fac_outlaws, bandit_personality, [(trp_bandit_r_sea_raider, 1, 1)]),

	("sea_raiders_ships_e", "Lyseni Pirates", icon_ship|carries_goods(2)|pf_is_ship, 0, fac_outlaws, bandit_personality, [(trp_bandit_e_sea_raider, 1, 1), (trp_bandit_e_sea_raider1, 30, 70), (trp_bandit_e_sea_raider2, 40, 60)]),

	("elite_dothraki2", "Foraging Party", icon_new_icon_pirates|carries_goods(2)|pf_show_faction, 0, fac_outlaws, bandit_personality, [(trp_mercenary_infantry_3, 3, 4), (trp_mercenary_infantry_1, 12, 18), (trp_mercenary_archer_1, 6, 12)]),

	("elite_dothraki3", "The Brotherhood without Banners", icon_people_vaegir_knight|carries_goods(2)|pf_label_small|pf_dont_attack_civilians, 0, fac_deserters, bandit_personality, [(trp_bandit_e_steppe, 3, 4), (trp_bandit_e_steppe1, 14, 18), (trp_bandit_e_steppe2, 12, 20)]),

	("elite_dothraki4", "Exiled Knights", icon_people_vaegir_knight|carries_goods(4)|pf_label_small, 0, fac_deserters, bandit_personality, [(trp_bandit_e_steppe, 3, 4), (trp_bandit_e_steppe1, 14, 18), (trp_bandit_e_steppe2, 12, 20)]),
	
	("elite_dothraki5", "Foraging Party", icon_people_axeman|carries_goods(2)|pf_label_small, 0, fac_outlaws, bandit_personality, [(trp_bandit_e_steppe, 3, 4), (trp_bandit_e_steppe1, 14, 18), (trp_bandit_e_steppe2, 12, 20)]),
	
	("elite_dothraki6", "Stone Men", icon_people_player|carries_goods(2)|pf_label_small|pf_hide_defenders, 0, fac_outlaws, bandit_personality, [(trp_bandit_e_steppe, 3, 4), (trp_bandit_e_steppe1, 14, 18), (trp_bandit_e_steppe2, 12, 20)]),

	("elite_dothraki7", "Greyscaled Pirates", icon_people_player|carries_goods(4)|pf_label_small|pf_hide_defenders, 0, fac_outlaws, bandit_personality, [(trp_bandit_e_steppe, 3, 4), (trp_bandit_e_steppe1, 14, 18), (trp_bandit_e_steppe2, 12, 20)]),

	("elite_dothraki8", "Sparrows", icon_people_peasant|carries_goods(2)|pf_label_small|pf_show_faction, 0, fac_crannogmen, bandit_personality, [(trp_bandit_e_steppe, 3, 4), (trp_bandit_e_steppe1, 14, 18), (trp_bandit_e_steppe2, 12, 20)]),

	("elite_dothraki9", "Wild Hares", icon_people_vaegir_knight|carries_goods(4)|pf_label_small, 0, fac_kingdom_2, bandit_personality, [(trp_bandit_e_steppe, 3, 4), (trp_bandit_e_steppe1, 14, 18), (trp_bandit_e_steppe2, 12, 20)]),

	("elite_dothraki11", "The Hag's Teeth", icon_new_icon_pirates|carries_goods(4)|pf_label_small, 0, fac_outlaws, bandit_personality, [(trp_bandit_e_steppe, 3, 4), (trp_bandit_e_steppe1, 14, 18), (trp_bandit_e_steppe2, 12, 20)]),

	("elite_dothraki12", "The Baleful Wind", icon_new_icon_pirates|carries_goods(4)|pf_label_small, 0, fac_outlaws, bandit_personality, [(trp_bandit_e_steppe, 3, 4), (trp_bandit_e_steppe1, 14, 18), (trp_bandit_e_steppe2, 12, 20)]),

]