################################################################
## General
################################################################
define config.autosave_on_quit = True

# Coupling Ceremonies:
# Episode 1 Part 1 == ["Bill", "Camilo", "Harry"]
# Episode 3 Part 3 == ["Bill", "Camilo", "Harry", "AJ"]
# Episode 6 Part 3 == ["Yasmin", "Tai", "Ciaran"]

default s3_hints = False
default s3_show_cust_icons = True
default s3_show_character = False
define s3_3rd_girl_options = {"Bill":"Miki", "Camilo":"Iona", "Harry":"Genevieve", "AJ":"Seb"}
default s3_3rd_girl = ""
default s3_character_profile = ""

# lol do i even use this?
default s3_lis = []
default s3_fav_li = ""
default s3_like_aj = False
default s3_like_bill = False
default s3_like_camilo = False
default s3_like_harry = False
default s3_like_tai = False
default s3_like_ciaran = False
default s3_like_yasmin = False
default s3_couples = {"AJ":"", "Elladine":"", "Genevieve":"", "Miki":"", "Iona":"", "Bill":"", "Camilo":"", "Harry":"", "Seb":"", "Nicky":""}

default he_she = ""
default him_her = ""
default his_her = ""

################################################################
## Episode 1
################################################################
## Episode 1, Part 1
# s3e1p1_warning_here_to_win (bool)
default s3e1p1_warning_here_to_win = False
# s3e1p1_feeling_hungry (bool)
default s3e1p1_feeling_hungry = False
# s3e1p1_grab_some_condoms (bool)
default s3e1p1_grab_some_condoms = False
# s3e1p1_took_a_nap (bool)
default s3e1p1_took_a_nap = False
# s3e1p1_strongest_couple ("Miki and Bill" "Iona and Camilo" "Genevieve and Harry")
default s3e1p1_strongest_couple = "None"
# s3e1p1_li_wants_chat_response ("Positive" "Negative")
default s3e1p1_li_wants_chat_response = "None"
# s3e1p1_cheeky_snog (bool)
default s3e1p1_cheeky_snog = False

## Episode 1 Part 2
# s3e1p2_mc_secret ("Thunder" "Rollercoaster" "Dimples" "Fan Fiction")
default s3e1p2_mc_secret = "None"
# s3e1p2_spooned_a_badger ("Camilo" "Bill" "Harry" "Nicky" "Seb")
default s3e1p2_spooned_a_badger = "None"
# s3e1p2_challenge_kiss (bool)
default s3e1p2_challenge_kiss = False
# s3e1p2_caught_having_sex ("Camilo" "Bill" "Harry" "Nicky" "Seb")
default s3e1p2_caught_having_sex = "None"
# s3e1p2_rescue_cat ("Camilo" "Bill" "Harry" "Nicky" "Seb")
default s3e1p2_rescue_cat = "None"
# s3e1p2_asked_girl_out ("Camilo" "Bill" "Harry" "Nicky" "Seb")
default s3e1p2_asked_girl_out = "None"
# s3e1p2_set_fire (bool)
default s3e1p2_set_fire = False
# s3e1p2_camilos_clue (bool)(bill:took job as waitress, camilo/harry: bday striptease)
default s3e1p2_camilos_clue = False
# s3e1p2_ordered_sex_toys (bool)
default s3e1p2_ordered_sex_toys = False
# s3e1p2_talk_to_new_girl (bool)
default s3e1p2_talk_to_new_girl = False

## Episode 1 Part 3
# s3e1p3_prank (bool)
default s3e1p3_prank = False
# s3e1p3_prankee ("AJ", "Bill", "Camilo", "Harry")
default s3e1p3_prankee = "None"

################################################################
## Episode 2
################################################################
## Episode 2 Part 1
# s3e2p1_want_spoon (bool)
default s3e2p1_want_spoon = False 
# s3e2p1_visited = ["Pool", "Bean Bags", "Sun Loungers", "Kitchen"]
default s3e2p1_visited = []
# s3e2p1_bill_lick (bool)
default s3e2p1_bill_lick = False
# s3e2p1_bfast_with_bill (bool)
default s3e2p1_bfast_with_bill = False

## Episode 2 Part 2
# s3e2p2_reject_bill (bool)
default s3e2p2_reject_bill = False
# s3e2p2_reject_camilo (bool)
default s3e2p2_reject_camilo = False
# s3e2p2_reject_harry (bool)
default s3e2p2_reject_harry = False
# s3e2p2_first_date (str)("Bill", "Camilo", "Harry")
default s3e2p2_first_date = ""
default s3e2p2_second_date = ""
default s3e2p2_third_date = ""
# s3e2p2_only_two_dates (bool)
default s3e2p2_only_two_dates = False
# s3e2p2_special_spark (str)("Bill", "Camilo", "Harry", "AJ")
default s3e2p2_special_spark = ""

## Episode 2 Part 3
# s3e2p3_food_seen = [""]
default s3e2p3_food_seen = []
# s3e2p3_food_fight (bool)
default s3e2p3_food_fight = False
# s3e2p3_first_victim (str)("Bill", "Camilo", "Harry", "AJ", "Seb", "Nicky")
default s3e2p3_first_victim = ""
# s3e2p3_second_victim (str)("Bill", "Camilo", "Harry", "AJ", "Seb", "Nicky")
default s3e2p3_second_victim = ""
# s3e2p3_clean_off_with_cam (bool)
default s3e2p3_clean_off_with_cam = False

################################################################
## Episode 3
################################################################
## Episode 3, Part 1
# s3e3p1_visited = ["Pool", "Bean Bags", "Gym"]
default s3e3p1_visited = []
# s3e3p1_bet = (str)("AJ", "Genevieve")
default s3e3p1_bet = ""
# s3e3p1_get_in_pool (bool)
default s3e3p1_get_in_pool = False
# s3e3p1_teach_harry (bool)
default s3e3p1_teach_harry = False
# s3e3p1_harry_bfast (str)
default s3e3p1_harry_bfast = ""
# s3e3p1_arm_wrestle (bool)
default s3e3p1_arm_wrestle = False

## Episode 3, Part 2
# default s3e3p2_visited = ["Lounge", "Bean Bags", "Pool", "Kitchen"]
default s3e3p2_visited = []
# s3e3p2_getting_kissy (bool)
default s3e3p2_getting_kissy = False
# s3e3p2_kiss_count (int)
default s3e3p2_kiss_count = 0
# s3e3p2_kiss_bill (bool)
default s3e3p2_kiss_bill = False
# s3e3p2_kiss_camilo (bool)
default s3e3p2_kiss_camilo = False
# s3e3p2_kiss_harry (bool)
default s3e3p2_kiss_harry = False
# s3e3p2_masseur (str) ["Bill", "AJ", "Harry", "Camilo"]
default s3e3p2_masseur = ""
# s3e3p2_dare_count (int)
default s3e3p2_dare_count = 0
# s3e3p2_completed_dare_count (int)
default s3e3p2_completed_dare_count = 0
# s3e3p2_hypnotise_seb (bool)
default s3e3p2_hypnotise_seb = False
# s3e3p2_interact_camilo (bool)
default s3e3p2_interact_camilo = False
# s3e3p2_draw_on_bucket (bool)
default s3e3p2_draw_on_bucket = False
# s3e3p2_win_challenge (bool)
default s3e3p2_win_challenge = False
# s3e3p2_s3e3p2_ask_question (str) ("AJ", "Bill", "Camilo", "Harry")
default s3e3p2_ask_question = ""

## Episode 3, Part 3
# s3e3p3_go_alone (bool)
default s3e3p3_go_alone = False
# s3e3p3_get_to_know (str) ["Bill", "Camilo", "Harry", "Miki", "Iona", "Genevieve", "Elladine"]
default s3e3p3_get_to_know = ""
# s3e3p3_just_cuddle (bool)
default s3e3p3_just_cuddle = False
# s3e3p3_roof_sex (bool)
default s3e3p3_roof_sex = False
# s3e3p3_get_to_know_current_partner (str) ["Miki", "Iona", "Genevieve", "Elladine", "AJ"]

################################################################
## Episode 4
################################################################
## Episode 4, Part 1
# s3e4p1_kiss_or_cuddle (bool)
default s3e4p1_kiss_or_cuddle = False
# s3e4p1_harry_incident (bool)
default s3e4p1_harry_incident = False
# s3e4p1_invite_gym (str) ["AJ", "Bill", "Camilo", "Harry"]
default s3e4p1_invite_gym = ""
# s3e4p1_massage (bool)
default s3e4p1_massage = False

## Episode 4, Part 2
# s3e4p2_good_tent (bool)
default s3e4p2_good_tent = False
# s3e4p2_give_rock (bool)
default s3e4p2_give_rock = False
# s3e4p2_say_dirty (bool)
default s3e4p2_say_dirty = False
# s3e4p2_decorate_tent (bool)
default s3e4p2_decorate_tent = False

## Episode 4, Part 3
# s3e4p3_wear_shirt (bool)
default s3e4p3_wear_shirt = False
# s3e4p3_supper (str) ["Beans", "Marshmallows", "Soup"]
default s3e4p3_supper = ""
# s3e4p3_drink (str) ["hot chocolate", "fear", "kombucha"]
default s3e4p3_drink = ""
# s3e4p3_stay_up (bool)
default s3e4p3_stay_up = False
# s3e4p3_tent_bits (bool)
default s3e4p3_tent_bits = False

################################################################
## Episode 5
################################################################

## Episode 5, Part 1
# s3e5p1_rummage_suitcases (bool)
default s3e5p1_rummage_suitcases = False

## Episode 5, Part 2
# s3e5p2_committed (bool)
default s3e5p2_committed = False
# s3e5p2_options_open (bool)
default s3e5p2_options_open = False
# s3e5p2_jump_in_water (bool)
default s3e5p2_jump_in_water = False
# s3e5p2_behind_waterfall (bool)
default s3e5p2_behind_waterfall = False
# s3e5p2_waterfall_bits (bool)
default s3e5p2_waterfall_bits = False
# s3e5p2_confess_attraction_yasmin (bool)
default s3e5p2_confess_attraction_yasmin = False
# s3e5p2_confess_attraction_tai (bool)
default s3e5p2_confess_attraction_tai = False
# s3e5p2_confess_attraction_ciaran (bool)
default s3e5p2_confess_attraction_ciaran = False

## Episode 5, Part 3
# s3e5p3_snog (str) ["Bill", "Camilo", "Harry", "Tai", "Ciaran", "AJ", "Yasmin"]
default s3e5p3_snog = ""
# s3e5p3_marry (str) ["Bill", "Camilo", "Harry", "Tai", "Ciaran", "AJ", "Yasmin"]
default s3e5p3_marry = ""
# s3e5p3_pie (str) ["Bill", "Camilo", "Harry", "Tai", "Ciaran", "AJ", "Yasmin"]
default s3e5p3_pie = ""
# s3e5p3_nudes (bool)
default s3e5p3_nudes = True
# s3e5p3_pursue_yasmin (bool)
default s3e5p3_pursue_yasmin = False
# s3e5p3_question (str) ["Tai", "AJ", "Seb"]
default s3e5p3_question = ""
# s3e5p3_yasmin_help (str) ["Tai", "Ciaran"]
default s3e5p3_yasmin_help = ""

################################################################
## Episode 6
################################################################
## Episode 6, Part 1
# s3e6p1_break_up (bool)
default s3e6p1_break_up = True
# s3e6p1_walk (bool)
default s3e6p1_walk = False
# s3e6p1_walking (bool)
default s3e6p1_walking = True

## Episode 6, Part 2
# s3e6p2_task (str) ["Nicky", "Camilo", "Bill", "Harry", "Ciaran Tai", "Seb", "Pool"]
default s3e6p2_task = ""
# s3e6p2_agent_name (str) ["Agent Martinez", "Agent Buckethead", "Agent FuryStone", "Agent Serious Face"]
default s3e6p2_agent_name = ""
# s3e6p2_switched (str) ["Yasmin", "Miki", "Iona", "Elladine", "Genevieve", "AJ"]
default s3e6p2_switched = ""

## Episode 6, Part 3
# s3e6p3_li (str) ["Yasmin", "Tai", "Ciaran"]
default s3e6p3_li = ""
# s3e6p3_good_couple (bool)
default s3e6p3_good_couple = False
# s3e6p3_hug_old_li (bool)
default s3e6p3_hug_old_li = False
# s3e6p3_listen (bool)
default s3e6p3_listen = False
# s3e6p3_other (str) ["Tai", "Ciaran", "Genevieve", "Miki", "Iona", "Seb"]
default s3e6p3_other = ""
# s3e6p3_loyal (bool)
default s3e6p3_loyal = False
# s3e6p3_kiss (bool)
default s3e6p3_kiss = False
# s3e6p3_bits (bool)
default s3e6p3_bits = False

################################################################
## Episode 7
################################################################
## Episode 7, Part 1
# s3e7p1_give_towel (bool)
default s3e7p1_give_towel = False
# s3e7p1_help_camilo (bool)
default s3e7p1_help_camilo = False
# s3e7p1_want_cam (bool)
default s3e7p1_want_cam = False
# s3e7p1_fruit (str) ["banana", "strawberries", "cherries"]
default s3e7p1_fruit = "banana"
# s3e7p1_saved_lipstick (bool)
default s3e7p1_saved_lipstick = False

## Episode 7, Part 2
# s3e7p2_visited (str list) ["lawn", "kitchen", "pool", "beanbags"]
default s3e7p2_visited = []
# s3e7p2_bill_talk (bool)
default s3e7p2_bill_talk = False
# s3e7p2_like_bill (bool)
default s3e7p2_like_bill = False
# s3e7p2_helped_kitchen (bool)
default s3e7p2_helped_kitchen = False
# s3e7p2_ciaran_hot (bool)
default s3e7p2_ciaran_hot = False

## Episode 7, Part 3
# s3e7p3_dump_m (str) ["Camilo", "Bill"]
default s3e7p3_dump_m = ""
# s3e7p3_dump_f (str) ["Iona", "Miki"]
default s3e7p3_dump_f = ""
# s3e7p3_cry (bool)
default s3e7p3_cry = False
# s3e7p3_help_pack (bool)
default s3e7p3_help_pack = False
# s3e7p3_stayed (str) ["Camilo and Iona", "Bill and Miki"]
default s3e7p3_stayed = ""
# s3e7p3_stay_m (str) ["Camilo", "Bill"]
default s3e7p3_stay_m = ""
# s3e7p3_stay_f (str) ["Iona", "Miki"]
default s3e7p3_stay_f = ""

################################################################
## Episode 8
################################################################
## Episode 8, Part 1
# s3e8p1_aj_chat (bool)
default s3e8p1_aj_chat = False
# s3e8p1_keep_distance_aj (bool)
default s3e8p1_keep_distance_aj = False
# s3e8p1_nice (bool)
default s3e8p1_nice = False
# s3e8p1_hope_recoupling (bool)
default s3e8p1_hope_recoupling_yasmin = False

## Episode 8, Part 2
# s3e8p2_glory (bool)
default s3e8p2_glory = False
# s3e8p2_ride_again (bool)
default s3e8p2_ride_again = False

## Episode 8, Part 3
# s3e8p3_bits (bool)
default s3e8p3_bits = False

################################################################
## Episode 9
################################################################
## Episode 9, Part 1
# s3e9p1_shower (bool)
default s3e9p1_shower = False
# s3e9p1_shower_bits (bool)
default s3e9p1_shower_bits = False
# s3e9p1_fate (bool)
default s3e9p1_fate = False
# s3e9p1_bottom_of_heart (bool)
default s3e9p1_bottom_of_heart = False



