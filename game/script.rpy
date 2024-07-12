################################################################
## Transforms
################################################################
# Moves MC onto screen to the left side
# transform mc_left:
#     zoom 1
#     xalign 1.75 yalign 0.05
#     easein 0.2 xalign 0.1

transform mc_move_left:
    anchor(0.5, 0.05)
    easein 0.2 zoom 1 xalign 0 yalign 0.05

# Used for 1 on 1 scenes.
transform mc_left:
    zoom 1.15
    xalign 1.75 yalign 0.05
    easein 0.2 xalign 0.2

# Move MC from current position into "center", used for 1 on 1.
transform mc_move_center:
    anchor(0.5, 0.05)
    easein 0.2 zoom 1.15 xalign 0.2

# Moves MC onto screen into center
transform mc_center:
    zoom 1.15
    xalign 1.75 yalign 0.05
    easein 0.2 xalign 0.5 yalign 0.05

# Moves character from current position to npc_left position.
transform move_left:
    anchor(0.5, 0)
    easein 0.2 zoom 1 xalign 0.5

# Used for 1 on 1 scenes.
transform npc_slight_right:
    zoom 1
    xalign 1.75 yalign 0
    easein 0.2 xalign 0.8

# Moves character from off screen to on screen, left.
transform npc_left:
    zoom 1
    xalign 1.75 yalign 0
    easein 0.2 xalign 0.5

# Moves character from off screen to on screen, right.
transform npc_right:
    zoom 1
    xalign 1.75 yalign 0
    easein 0.2 xalign 0.98

# Moves character from off screen to on screen, center.
transform npc_center:
    zoom 1.15
    xalign 1.75 yalign 0
    easein 0.2 xalign 0.8 yalign 0

# Moves character from current position into npc_center position.
transform move_center:
    anchor(0.5, 0)
    easein 0.2 zoom 1.15 xalign 0.8

# Moves character from current position on screen to off screen.
transform npc_exit:
    easeout 0.2 xalign 1.75

# Slow zoom in on character in center of screen during first introductions.
transform character_profile_zoom:
    zoom 0.7
    xalign 0.5 yalign 0.5
    anchor(0.5, 0.5)
    linear 3 zoom 0.8 yalign 0

# Makes character icons on map get larger on mouse hover.
transform map_icon:
    zoom 0.4
    anchor(0.5, 0.5)
    on hover:
        zoom 0.5
    on idle:
        zoom 0.4

# Adds slow zoom for 4secs for the Day and Part title screen.
transform title:
    anchor(0.5, 0.5)
    linear 4 zoom 1.1

## MC Customizer Icons
# When mouse hovers over icon it zooms in slightly to indicate to user that they can select it.
transform hover_zoom:
    zoom 0.5
    anchor(0.5, 0.5)
    on hover:
        zoom 0.55
    on idle:
        zoom 0.5



################################################################
## Game Start
## Decides what happens when user selects "Start" on Main Menu.
################################################################
label start:

    ########################################
    ### For Testing Only: (Comment Out before Building!)
    # $ s3_mc.current_partner = "Harry"

    # $ s3_li = "Bill"
    # $ s3_mc.past_partners = ["Bill"]
    # $ s3_mc.bff = "Seb"
    # $ s3_mc.job = "Athlete"
    # $ s3_mc.bisexual = False
    # $ s3_mc.diet = "Vegetarian"

    # $ s3_bff = "Seb"
    # $ s3_bff_lower = "seb"
    # $ s3_3rd_girl = "Miki"

    ## For testing if changing partners worked.
    # $ s3_mc.current_partner = "AJ"
    # $ s3_mc.past_partners = ["Harry", "AJ"]

    menu:
        "Want to start a new game at Day 1 or play with the character customizer?"
        "Start New Game":
            jump s3e1p1
        "Character Look Customizer":
            $ randomize_style("look")
            call screen cust_body
        "Character Outfit Customizer":
            $ randomize_style("look")
            menu:
                "What's the style?"
                "Bathing Suits":
                    $ randomize_style("clothes", "swim")
                    call screen cust_outfit("swim")
                "Evening Wear":
                    $ randomize_style("clothes", "evening")
                    call screen cust_outfit("evening")
                "Pjs":
                    $ randomize_style("clothes", "pjs")
                    call screen cust_outfit("pjs")


    return

label cust_confirm:
    # Show character middle of screen
    show s3_mc_image at mc_center
    menu:
        "Is this how I want to look?"
        "Yes, let's go!":
            pass
        "No, I want to change.":
            call screen cust_body()

    return

label cust_confirm_outfit:
    show s3_mc_image at mc_center
    menu:
        "Is this how I want to look?"
        "Yes, let's go!":
            pass
        "No, I want to change.":
            call customize_outfit

    return