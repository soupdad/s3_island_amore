####################################################################
## Custom Functions and Classes
####################################################################
init python:
    def pronouns(name):
        '''
        Saves the correct pronouns to generic variables depending on the NPC.
        '''
        women = ["AJ", "Elladine", "Genevieve", "Iona", "Miki", "Lily", "Yasmin"]
        global he_she, him_her, his_her, his_hers

        if name in women:
            he_she = "she"
            him_her = "her"
            his_her = "her"
            his_hers = "hers"
        else:
            he_she = "he"
            him_her = "him"
            his_her = "his"
            his_hers = "his"

    def favorite_li():
        '''
        Returns the love interest that is currently in game that the MC has most often responded positively.
        '''
        rating = 0
        result = ""

        for name in s3_lis:
            if s3_mc.like_mc[name] > rating:
                rating = s3_mc.like_mc[name]
                result = name
        
        return result

    on_screen = []

    def move_character(event, interact=True, **kwargs):
        """
        Function to automatically move characters on and off the screen when they speak.

        The function is added into each character's creation declaration further down in this file.

        Works for 1 or 2 NPCs on screen.

        Declaring new scene:
            Must add below command after declaring new scene or else characters from previous scene will appear.
            on_screen = [] 

        Current Issues:
            Expressions(attributes) of islanders don't change from neutral until the second line of dialog.
                Look into these commands to see if any would help:
                    config.say_attribute_transition
                    config.say_attribute_transition_layer
                    config.say_attribute_transition_callback
                    https://www.reddit.com/r/RenPy/comments/ostkua/layered_images_with_a_transition_problem/
                    https://www.renpy.org/doc/html/config.html#var-config.say_attribute_transition
                    https://www.renpy.org/doc/html/layeredimage.html
            Needs on_screen = [] called after each new scene, not impossible but slightly annoying.
                Not a needed fix.
     
        """
        if not interact:
            return
        
        # Gets speaking character's name.
        character = renpy.get_say_image_tag()
        #attribute = renpy.get_say_attributes()

        # If speaking character already on screen function stops running.
        if renpy.showing(character):
            return
        
        # This is just a safety but it is almost always going to run if the last
        # if statement didn't stop the function.
        if event == "begin":
            # If no characters visible on screen, first character goes in center.
            if len(on_screen) == 0:
                renpy.show(character, [npc_center])
            # If 1 character visible on screen, first character moves to left, second character goes to right.
            elif len(on_screen) == 1:
                renpy.show(on_screen[0], [move_left])
                renpy.show(character, [npc_right])
            # If 2 characters visible on screen, first character to talk gets moved off screen.
            elif len(on_screen) == 2:
                leaving_npc = on_screen.pop(0)
                # Finds if leaving character is on right or left side.
                leaving_npc_bounds = renpy.get_image_bounds(str(leaving_npc))

                renpy.show(leaving_npc, [npc_exit])
                renpy.pause(0.3)
                renpy.hide(leaving_npc)
                
                # If the leaving character was on left then newest speaker goes to left spot.
                # If the leaving character was on right then newest speaker goes to right spot.
                if leaving_npc_bounds[0] < 500:
                    # left
                    renpy.show(character, [npc_left])
                elif leaving_npc_bounds[0] > 700:
                    # right
                    renpy.show(character, [npc_right])

            # Adds newest speaker to list of characters visible on screen.
            on_screen.append(character)

    class MainCharacter:
        '''
        A character that is controlled by the user.

        Still need to run some tests on this and may have to go back to storing in individual variables since I got some errors.

        Attributes:
            current_partner (str) - MC's current partner (or most recent one).
            past_partners (str list) - List of MC's past and current partners.
            current_outfit (str) - Outfit currently being worn. ** Only applicable if MC imgs added to game.
            bff (str) - MC's best friend in game, decided in e1p3. Can be Genevieve, Elladine, Nicky, or Seb.
            job (str) - MC's job, decided in e1p1. Can be Athlete, Scientist, Model, or Musician.
            bisexual (bool) - MC's preference for just men or men and women, decided in e1p2.
            diet (str) - MC's food preference, defined in e2p1. Can be Meat, Vegetarian, or Vegan.
            like_mc (dict) - Names of NPCs linked with numeric represenation of how much they like MC.

            Might be removing these:
            sweet (int) - Numeric representation of NPC's sweet personality trait.
            bold (int) - Numeric representation of NPC's bold personality trait.
            funny (int) - Numeric representation of NPC's funny personality trait.
        '''
        def __init__(self):
            self.current_partner = ""
            self.past_partners = []
            self.current_outfit = ""
            self.bff = ""
            self.job = ""
            self.bisexual = False
            self.diet = ""
            self.like_mc = {"Bill":0, "Camilo":0, "Harry":0, "AJ":0, "Elladine":0, 
            "Iona":0, "Genevieve":0, "Miki":0, "Nicky":0, "Seb":0}

            # maybe remove these?? not sure if they have a point
            self.sweet = 0
            self.bold = 0
            self.funny = 0
        
        def like(self, npc):
            '''
            Adds 1 to like_mc attribute for that particular npc.

            Args:
                npc (str) - Name of NPC, must be lowercase.
            '''
            self.like_mc[npc] += 1
        
        def dislike(self, npc):
            '''
            Subtracts 1 from like_mc attribute for that particular npc.

            Args:
                npc (str) - Name of NPC, must be lowercase.
            '''
            self.like_mc[npc] -= 1


    # This is currently unnecessary but I want to leave in incase if I find a way to use it.
    # I don't want to have to recode all of this.
    # If end up using fav_outfits. Delete current_partner and gender.
    class Npcs:
        def __init__(self, gender):
            """
            Defines attributes and actions of a character that isn't controlled by the user.

            Args:
            gender (str) - The gender of the NPC, either woman or man

            Only Applicable if add MC images to game:
                need to add to args list at top and change below to be = fav_outfits
                fav_outfits (list of strings) - A list of the NPC's favorite MC outfits
            """
            self.fav_outfits = []
            self.current_partner = ""
            self.gender = gender

        def like_mc_outfit(self, mc_current_outfit):
            '''
            Returns true if the NPC likes the outfit MC is wearing.
            Or returns false if NPC doesn't like the outfit MC is wearing.

            ** Only applicable if MC imgs are added to game.

            Args:
                mc_current_outfit (str) - The outfit the MC is currently wearing.
            '''
            if mc_current_outfit in self.fav_outfits:
                return True
            else:
                return False

################################################################################################
#### 
#### Characters
####
#### Includes Text Message, MC, and all NPCs including composite image declarations.
####

## Text Message
define text = Character(window_background = Image("bg_text_message.png", xalign=0.5, yalign=1.0), color = "#ffffff")

####################################################################
## MC
####################################################################
default s3_name = "Filler"
define character.s3_mc = Character("s3_name", dynamic = True, window_background = Image("mc_dialog.png", xalign=0.5, yalign=1.0))
default s3_mc = MainCharacter()
define thought = Character("s3_name", dynamic = True, what_italic = True, window_background = Image("mc_dialog.png", xalign=0.5, yalign=1.0))

####################################################################
## NPCs
####################################################################
# These variables change all NPC's outfits and hair.
# Outfits are titled - swim, evening, and pjs
default outfit = "swim"
default hair = "hair"

# For E3P2 - Bill's Bucket Head
default bucket = "normal"

## AJ
# layeredimage aj:
#     always:
#         "npcs/aj/aj-body.png"
        
#     (0, 0), "npcs/aj/aj-outfit-[outfit].png",
#     (0, 0), "npcs/aj/aj-face-neutral.png",
#     (0, 0), "npcs/aj/aj-hair-[hair].png"


image aj = Composite(
    (965, 1500),
    (0, 0), "npcs/aj/aj-body.png",
    (0, 0), "npcs/aj/aj-outfit-[outfit].png",
    (0, 0), "npcs/aj/aj-face-neutral.png",
    (0, 0), "npcs/aj/aj-hair-[hair].png"
)
image aj angry= Composite(
    (965, 1500),
    (0, 0), "npcs/aj/aj-body.png",
    (0, 0), "npcs/aj/aj-outfit-[outfit].png",
    (0, 0), "npcs/aj/aj-face-angry.png",
    (0, 0), "npcs/aj/aj-hair-[hair].png"
)
image aj awkward= Composite(
    (965, 1500),
    (0, 0), "npcs/aj/aj-body.png",
    (0, 0), "npcs/aj/aj-outfit-[outfit].png",
    (0, 0), "npcs/aj/aj-face-awkward.png",
    (0, 0), "npcs/aj/aj-hair-[hair].png"
)
image aj flirt= Composite(
    (965, 1500),
    (0, 0), "npcs/aj/aj-body.png",
    (0, 0), "npcs/aj/aj-outfit-[outfit].png",
    (0, 0), "npcs/aj/aj-face-flirt.png",
    (0, 0), "npcs/aj/aj-hair-[hair].png"
)
image aj happy= Composite(
    (965, 1500),
    (0, 0), "npcs/aj/aj-body.png",
    (0, 0), "npcs/aj/aj-outfit-[outfit].png",
    (0, 0), "npcs/aj/aj-face-happy.png",
    (0, 0), "npcs/aj/aj-hair-[hair].png"
)
image aj sad= Composite(
    (965, 1500),
    (0, 0), "npcs/aj/aj-body.png",
    (0, 0), "npcs/aj/aj-outfit-[outfit].png",
    (0, 0), "npcs/aj/aj-face-sad.png",
    (0, 0), "npcs/aj/aj-hair-[hair].png"
)
image aj serious= Composite(
    (965, 1500),
    (0, 0), "npcs/aj/aj-body.png",
    (0, 0), "npcs/aj/aj-outfit-[outfit].png",
    (0, 0), "npcs/aj/aj-face-serious.png",
    (0, 0), "npcs/aj/aj-hair-[hair].png"
)
image aj talk= Composite(
    (965, 1500),
    (0, 0), "npcs/aj/aj-body.png",
    (0, 0), "npcs/aj/aj-outfit-[outfit].png",
    (0, 0), "npcs/aj/aj-face-talk.png",
    (0, 0), "npcs/aj/aj-hair-[hair].png"
)
image aj very_happy= Composite(
    (965, 1500),
    (0, 0), "npcs/aj/aj-body.png",
    (0, 0), "npcs/aj/aj-outfit-[outfit].png",
    (0, 0), "npcs/aj/aj-face-very_happy.png",
    (0, 0), "npcs/aj/aj-hair-[hair].png"
)

define character.aj = Character("AJ", image = "aj", callback = move_character, window_background = Image("npc_dialog.png", xalign=0.5, yalign=1.0))
default aj = Npcs("woman")

## Bill
image bill = Composite(
    (965, 1500),
    (0, 0), "npcs/bill/bill-body.png",
    (0, 0), "npcs/bill/bill-outfit-[outfit].png",
    (0, 0), "npcs/bill/bill-face-neutral.png",
    (0, 0), "npcs/bill/bill-hair-[hair].png"
)
image bill angry= Composite(
    (965, 1500),
    (0, 0), "npcs/bill/bill-body.png",
    (0, 0), "npcs/bill/bill-outfit-[outfit].png",
    (0, 0), "npcs/bill/bill-face-angry.png",
    (0, 0), "npcs/bill/bill-hair-[hair].png"
)
image bill awkward= Composite(
    (965, 1500),
    (0, 0), "npcs/bill/bill-body.png",
    (0, 0), "npcs/bill/bill-outfit-[outfit].png",
    (0, 0), "npcs/bill/bill-face-awkward.png",
    (0, 0), "npcs/bill/bill-hair-[hair].png"
)
image bill flirt= Composite(
    (965, 1500),
    (0, 0), "npcs/bill/bill-body.png",
    (0, 0), "npcs/bill/bill-outfit-[outfit].png",
    (0, 0), "npcs/bill/bill-face-flirt.png",
    (0, 0), "npcs/bill/bill-hair-[hair].png"
)
image bill happy= Composite(
    (965, 1500),
    (0, 0), "npcs/bill/bill-body.png",
    (0, 0), "npcs/bill/bill-outfit-[outfit].png",
    (0, 0), "npcs/bill/bill-face-happy.png",
    (0, 0), "npcs/bill/bill-hair-[hair].png"
)
image bill sad= Composite(
    (965, 1500),
    (0, 0), "npcs/bill/bill-body.png",
    (0, 0), "npcs/bill/bill-outfit-[outfit].png",
    (0, 0), "npcs/bill/bill-face-sad.png",
    (0, 0), "npcs/bill/bill-hair-[hair].png"
)
image bill serious= Composite(
    (965, 1500),
    (0, 0), "npcs/bill/bill-body.png",
    (0, 0), "npcs/bill/bill-outfit-[outfit].png",
    (0, 0), "npcs/bill/bill-face-serious.png",
    (0, 0), "npcs/bill/bill-hair-[hair].png"
)
image bill talk= Composite(
    (965, 1500),
    (0, 0), "npcs/bill/bill-body.png",
    (0, 0), "npcs/bill/bill-outfit-[outfit].png",
    (0, 0), "npcs/bill/bill-face-talk.png",
    (0, 0), "npcs/bill/bill-hair-[hair].png"
)
image bill very_happy= Composite(
    (965, 1500),
    (0, 0), "npcs/bill/bill-body.png",
    (0, 0), "npcs/bill/bill-outfit-[outfit].png",
    (0, 0), "npcs/bill/bill-face-very_happy.png",
    (0, 0), "npcs/bill/bill-hair-[hair].png"
)
image bill bucket= Composite(
    (965, 1500),
    (0, 0), "npcs/bill/bill-body.png",
    (0, 0), "npcs/bill/bill-outfit-[outfit].png",
    (0, 0), "npcs/bill/bill-face-very_happy.png",
    (0, 0), "npcs/bill/bill-hair-bucket_[bucket].png"
)

define character.bill = Character("Bill", image = "bill", callback = move_character, window_background = Image("npc_dialog.png", xalign=0.5, yalign=1.0))
default bill = Npcs("man")

## Camilo
image camilo = Composite(
    (965, 1500),
    (0, 0), "npcs/camilo/camilo-body.png",
    (0, 0), "npcs/camilo/camilo-outfit-[outfit].png",
    (0, 0), "npcs/camilo/camilo-face-neutral.png",
    (0, 0), "npcs/camilo/camilo-hair-[hair].png"
)
image camilo angry= Composite(
    (965, 1500),
    (0, 0), "npcs/camilo/camilo-body.png",
    (0, 0), "npcs/camilo/camilo-outfit-[outfit].png",
    (0, 0), "npcs/camilo/camilo-face-angry.png",
    (0, 0), "npcs/camilo/camilo-hair-[hair].png"
)
image camilo awkward= Composite(
    (965, 1500),
    (0, 0), "npcs/camilo/camilo-body.png",
    (0, 0), "npcs/camilo/camilo-outfit-[outfit].png",
    (0, 0), "npcs/camilo/camilo-face-awkward.png",
    (0, 0), "npcs/camilo/camilo-hair-[hair].png"
)
image camilo flirt= Composite(
    (965, 1500),
    (0, 0), "npcs/camilo/camilo-body.png",
    (0, 0), "npcs/camilo/camilo-outfit-[outfit].png",
    (0, 0), "npcs/camilo/camilo-face-flirt.png",
    (0, 0), "npcs/camilo/camilo-hair-[hair].png"
)
image camilo happy= Composite(
    (965, 1500),
    (0, 0), "npcs/camilo/camilo-body.png",
    (0, 0), "npcs/camilo/camilo-outfit-[outfit].png",
    (0, 0), "npcs/camilo/camilo-face-happy.png",
    (0, 0), "npcs/camilo/camilo-hair-[hair].png"
)
image camilo sad= Composite(
    (965, 1500),
    (0, 0), "npcs/camilo/camilo-body.png",
    (0, 0), "npcs/camilo/camilo-outfit-[outfit].png",
    (0, 0), "npcs/camilo/camilo-face-sad.png",
    (0, 0), "npcs/camilo/camilo-hair-[hair].png"
)
image camilo serious= Composite(
    (965, 1500),
    (0, 0), "npcs/camilo/camilo-body.png",
    (0, 0), "npcs/camilo/camilo-outfit-[outfit].png",
    (0, 0), "npcs/camilo/camilo-face-serious.png",
    (0, 0), "npcs/camilo/camilo-hair-[hair].png"
)
image camilo talk= Composite(
    (965, 1500),
    (0, 0), "npcs/camilo/camilo-body.png",
    (0, 0), "npcs/camilo/camilo-outfit-[outfit].png",
    (0, 0), "npcs/camilo/camilo-face-talk.png",
    (0, 0), "npcs/camilo/camilo-hair-[hair].png"
)
image camilo very_happy= Composite(
    (965, 1500),
    (0, 0), "npcs/camilo/camilo-body.png",
    (0, 0), "npcs/camilo/camilo-outfit-[outfit].png",
    (0, 0), "npcs/camilo/camilo-face-very_happy.png",
    (0, 0), "npcs/camilo/camilo-hair-[hair].png"
)

define character.camilo = Character("Camilo", image = "camilo", callback = move_character, window_background = Image("npc_dialog.png", xalign=0.5, yalign=1.0))
default camilo = Npcs("man")

## Ciaran
define character.ciaran = Character("Ciaran", window_background = Image("npc_dialog.png", xalign=0.5, yalign=1.0))
default ciaran = Npcs("man")

## Elladine
image elladine = Composite(
    (965, 1500),
    (0, 0), "npcs/elladine/elladine-body.png",
    (0, 0), "npcs/elladine/elladine-outfit-[outfit].png",
    (0, 0), "npcs/elladine/elladine-face-neutral.png",
    (0, 0), "npcs/elladine/elladine-hair-[hair].png"
)
image elladine angry= Composite(
    (965, 1500),
    (0, 0), "npcs/elladine/elladine-body.png",
    (0, 0), "npcs/elladine/elladine-outfit-[outfit].png",
    (0, 0), "npcs/elladine/elladine-face-angry.png",
    (0, 0), "npcs/elladine/elladine-hair-[hair].png"
)
image elladine awkward= Composite(
    (965, 1500),
    (0, 0), "npcs/elladine/elladine-body.png",
    (0, 0), "npcs/elladine/elladine-outfit-[outfit].png",
    (0, 0), "npcs/elladine/elladine-face-awkward.png",
    (0, 0), "npcs/elladine/elladine-hair-[hair].png"
)
image elladine flirt= Composite(
    (965, 1500),
    (0, 0), "npcs/elladine/elladine-body.png",
    (0, 0), "npcs/elladine/elladine-outfit-[outfit].png",
    (0, 0), "npcs/elladine/elladine-face-flirt.png",
    (0, 0), "npcs/elladine/elladine-hair-[hair].png"
)
image elladine happy= Composite(
    (965, 1500),
    (0, 0), "npcs/elladine/elladine-body.png",
    (0, 0), "npcs/elladine/elladine-outfit-[outfit].png",
    (0, 0), "npcs/elladine/elladine-face-happy.png",
    (0, 0), "npcs/elladine/elladine-hair-[hair].png"
)
image elladine sad= Composite(
    (965, 1500),
    (0, 0), "npcs/elladine/elladine-body.png",
    (0, 0), "npcs/elladine/elladine-outfit-[outfit].png",
    (0, 0), "npcs/elladine/elladine-face-sad.png",
    (0, 0), "npcs/elladine/elladine-hair-[hair].png"
)
image elladine serious= Composite(
    (965, 1500),
    (0, 0), "npcs/elladine/elladine-body.png",
    (0, 0), "npcs/elladine/elladine-outfit-[outfit].png",
    (0, 0), "npcs/elladine/elladine-face-serious.png",
    (0, 0), "npcs/elladine/elladine-hair-[hair].png"
)
image elladine talk= Composite(
    (965, 1500),
    (0, 0), "npcs/elladine/elladine-body.png",
    (0, 0), "npcs/elladine/elladine-outfit-[outfit].png",
    (0, 0), "npcs/elladine/elladine-face-talk.png",
    (0, 0), "npcs/elladine/elladine-hair-[hair].png"
)
image elladine very_happy= Composite(
    (965, 1500),
    (0, 0), "npcs/elladine/elladine-body.png",
    (0, 0), "npcs/elladine/elladine-outfit-[outfit].png",
    (0, 0), "npcs/elladine/elladine-face-very_happy.png",
    (0, 0), "npcs/elladine/elladine-hair-[hair].png"
)

define character.elladine = Character("Elladine", image = "elladine", callback = move_character, window_background = Image("npc_dialog.png", xalign=0.5, yalign=1.0))
default elladine = Npcs("woman")


## Genevieve
image genevieve = Composite(
    (965, 1500),
    (0, 0), "npcs/genevieve/genevieve-body.png",
    (0, 0), "npcs/genevieve/genevieve-outfit-[outfit].png",
    (0, 0), "npcs/genevieve/genevieve-face-neutral.png",
    (0, 0), "npcs/genevieve/genevieve-hair-[hair].png"
)
image genevieve angry= Composite(
    (965, 1500),
    (0, 0), "npcs/genevieve/genevieve-body.png",
    (0, 0), "npcs/genevieve/genevieve-outfit-[outfit].png",
    (0, 0), "npcs/genevieve/genevieve-face-angry.png",
    (0, 0), "npcs/genevieve/genevieve-hair-[hair].png"
)
image genevieve awkward= Composite(
    (965, 1500),
    (0, 0), "npcs/genevieve/genevieve-body.png",
    (0, 0), "npcs/genevieve/genevieve-outfit-[outfit].png",
    (0, 0), "npcs/genevieve/genevieve-face-awkward.png",
    (0, 0), "npcs/genevieve/genevieve-hair-[hair].png"
)
image genevieve flirt= Composite(
    (965, 1500),
    (0, 0), "npcs/genevieve/genevieve-body.png",
    (0, 0), "npcs/genevieve/genevieve-outfit-[outfit].png",
    (0, 0), "npcs/genevieve/genevieve-face-flirt.png",
    (0, 0), "npcs/genevieve/genevieve-hair-[hair].png"
)
image genevieve happy= Composite(
    (965, 1500),
    (0, 0), "npcs/genevieve/genevieve-body.png",
    (0, 0), "npcs/genevieve/genevieve-outfit-[outfit].png",
    (0, 0), "npcs/genevieve/genevieve-face-happy.png",
    (0, 0), "npcs/genevieve/genevieve-hair-[hair].png"
)
image genevieve sad= Composite(
    (965, 1500),
    (0, 0), "npcs/genevieve/genevieve-body.png",
    (0, 0), "npcs/genevieve/genevieve-outfit-[outfit].png",
    (0, 0), "npcs/genevieve/genevieve-face-sad.png",
    (0, 0), "npcs/genevieve/genevieve-hair-[hair].png"
)
image genevieve serious= Composite(
    (965, 1500),
    (0, 0), "npcs/genevieve/genevieve-body.png",
    (0, 0), "npcs/genevieve/genevieve-outfit-[outfit].png",
    (0, 0), "npcs/genevieve/genevieve-face-serious.png",
    (0, 0), "npcs/genevieve/genevieve-hair-[hair].png"
)
image genevieve talk= Composite(
    (965, 1500),
    (0, 0), "npcs/genevieve/genevieve-body.png",
    (0, 0), "npcs/genevieve/genevieve-outfit-[outfit].png",
    (0, 0), "npcs/genevieve/genevieve-face-talk.png",
    (0, 0), "npcs/genevieve/genevieve-hair-[hair].png"
)
image genevieve very_happy= Composite(
    (965, 1500),
    (0, 0), "npcs/genevieve/genevieve-body.png",
    (0, 0), "npcs/genevieve/genevieve-outfit-[outfit].png",
    (0, 0), "npcs/genevieve/genevieve-face-very_happy.png",
    (0, 0), "npcs/genevieve/genevieve-hair-[hair].png"
)

define character.genevieve = Character("Genevieve", image = "genevieve", callback = move_character, window_background = Image("npc_dialog.png", xalign=0.5, yalign=1.0))
default genevieve = Npcs("woman")


## Harry
image harry = Composite(
    (965, 1500),
    (0, 0), "npcs/harry/harry-body.png",
    (0, 0), "npcs/harry/harry-outfit-[outfit].png",
    (0, 0), "npcs/harry/harry-face-neutral.png",
    (0, 0), "npcs/harry/harry-hair-[hair].png"
)
image harry angry= Composite(
    (965, 1500),
    (0, 0), "npcs/harry/harry-body.png",
    (0, 0), "npcs/harry/harry-outfit-[outfit].png",
    (0, 0), "npcs/harry/harry-face-angry.png",
    (0, 0), "npcs/harry/harry-hair-[hair].png"
)
image harry awkward= Composite(
    (965, 1500),
    (0, 0), "npcs/harry/harry-body.png",
    (0, 0), "npcs/harry/harry-outfit-[outfit].png",
    (0, 0), "npcs/harry/harry-face-awkward.png",
    (0, 0), "npcs/harry/harry-hair-[hair].png"
)
image harry flirt= Composite(
    (965, 1500),
    (0, 0), "npcs/harry/harry-body.png",
    (0, 0), "npcs/harry/harry-outfit-[outfit].png",
    (0, 0), "npcs/harry/harry-face-flirt.png",
    (0, 0), "npcs/harry/harry-hair-[hair].png"
)
image harry happy= Composite(
    (965, 1500),
    (0, 0), "npcs/harry/harry-body.png",
    (0, 0), "npcs/harry/harry-outfit-[outfit].png",
    (0, 0), "npcs/harry/harry-face-happy.png",
    (0, 0), "npcs/harry/harry-hair-[hair].png"
)
image harry sad= Composite(
    (965, 1500),
    (0, 0), "npcs/harry/harry-body.png",
    (0, 0), "npcs/harry/harry-outfit-[outfit].png",
    (0, 0), "npcs/harry/harry-face-sad.png",
    (0, 0), "npcs/harry/harry-hair-[hair].png"
)
image harry serious= Composite(
    (965, 1500),
    (0, 0), "npcs/harry/harry-body.png",
    (0, 0), "npcs/harry/harry-outfit-[outfit].png",
    (0, 0), "npcs/harry/harry-face-serious.png",
    (0, 0), "npcs/harry/harry-hair-[hair].png"
)
image harry talk= Composite(
    (965, 1500),
    (0, 0), "npcs/harry/harry-body.png",
    (0, 0), "npcs/harry/harry-outfit-[outfit].png",
    (0, 0), "npcs/harry/harry-face-talk.png",
    (0, 0), "npcs/harry/harry-hair-[hair].png"
)
image harry very_happy= Composite(
    (965, 1500),
    (0, 0), "npcs/harry/harry-body.png",
    (0, 0), "npcs/harry/harry-outfit-[outfit].png",
    (0, 0), "npcs/harry/harry-face-very_happy.png",
    (0, 0), "npcs/harry/harry-hair-[hair].png"
)

define character.harry = Character("Harry", image = "harry", callback = move_character, window_background = Image("npc_dialog.png", xalign=0.5, yalign=1.0))
default harry = Npcs("man")


## Iona
image iona = Composite(
    (965, 1500),
    (0, 0), "npcs/iona/iona-body.png",
    (0, 0), "npcs/iona/iona-outfit-[outfit].png",
    (0, 0), "npcs/iona/iona-face-neutral.png",
    (0, 0), "npcs/iona/iona-hair-[hair].png"
)
image iona angry= Composite(
    (965, 1500),
    (0, 0), "npcs/iona/iona-body.png",
    (0, 0), "npcs/iona/iona-outfit-[outfit].png",
    (0, 0), "npcs/iona/iona-face-angry.png",
    (0, 0), "npcs/iona/iona-hair-[hair].png"
)
image iona awkward= Composite(
    (965, 1500),
    (0, 0), "npcs/iona/iona-body.png",
    (0, 0), "npcs/iona/iona-outfit-[outfit].png",
    (0, 0), "npcs/iona/iona-face-awkward.png",
    (0, 0), "npcs/iona/iona-hair-[hair].png"
)
image iona flirt= Composite(
    (965, 1500),
    (0, 0), "npcs/iona/iona-body.png",
    (0, 0), "npcs/iona/iona-outfit-[outfit].png",
    (0, 0), "npcs/iona/iona-face-flirt.png",
    (0, 0), "npcs/iona/iona-hair-[hair].png"
)
image iona happy= Composite(
    (965, 1500),
    (0, 0), "npcs/iona/iona-body.png",
    (0, 0), "npcs/iona/iona-outfit-[outfit].png",
    (0, 0), "npcs/iona/iona-face-happy.png",
    (0, 0), "npcs/iona/iona-hair-[hair].png"
)
image iona sad= Composite(
    (965, 1500),
    (0, 0), "npcs/iona/iona-body.png",
    (0, 0), "npcs/iona/iona-outfit-[outfit].png",
    (0, 0), "npcs/iona/iona-face-sad.png",
    (0, 0), "npcs/iona/iona-hair-[hair].png"
)
image iona serious= Composite(
    (965, 1500),
    (0, 0), "npcs/iona/iona-body.png",
    (0, 0), "npcs/iona/iona-outfit-[outfit].png",
    (0, 0), "npcs/iona/iona-face-serious.png",
    (0, 0), "npcs/iona/iona-hair-[hair].png"
)
image iona talk= Composite(
    (965, 1500),
    (0, 0), "npcs/iona/iona-body.png",
    (0, 0), "npcs/iona/iona-outfit-[outfit].png",
    (0, 0), "npcs/iona/iona-face-talk.png",
    (0, 0), "npcs/iona/iona-hair-[hair].png"
)
image iona very_happy= Composite(
    (965, 1500),
    (0, 0), "npcs/iona/iona-body.png",
    (0, 0), "npcs/iona/iona-outfit-[outfit].png",
    (0, 0), "npcs/iona/iona-face-very_happy.png",
    (0, 0), "npcs/iona/iona-hair-[hair].png"
)

define character.iona = Character("Iona", image = "iona", callback = move_character, window_background = Image("npc_dialog.png", xalign=0.5, yalign=1.0))
default iona = Npcs("woman")


## Lily
define character.lily = Character("Lily", window_background = Image("npc_dialog.png", xalign=0.5, yalign=1.0))
default lily = Npcs("woman")


## Miki
image miki = Composite(
    (965, 1500),
    (0, 0), "npcs/miki/miki-body.png",
    (0, 0), "npcs/miki/miki-outfit-[outfit].png",
    (0, 0), "npcs/miki/miki-face-neutral.png",
    (0, 0), "npcs/miki/miki-hair-[hair].png"
)
image miki angry= Composite(
    (965, 1500),
    (0, 0), "npcs/miki/miki-body.png",
    (0, 0), "npcs/miki/miki-outfit-[outfit].png",
    (0, 0), "npcs/miki/miki-face-angry.png",
    (0, 0), "npcs/miki/miki-hair-[hair].png"
)
image miki awkward= Composite(
    (965, 1500),
    (0, 0), "npcs/miki/miki-body.png",
    (0, 0), "npcs/miki/miki-outfit-[outfit].png",
    (0, 0), "npcs/miki/miki-face-awkward.png",
    (0, 0), "npcs/miki/miki-hair-[hair].png"
)
image miki flirt= Composite(
    (965, 1500),
    (0, 0), "npcs/miki/miki-body.png",
    (0, 0), "npcs/miki/miki-outfit-[outfit].png",
    (0, 0), "npcs/miki/miki-face-flirt.png",
    (0, 0), "npcs/miki/miki-hair-[hair].png"
)
image miki happy= Composite(
    (965, 1500),
    (0, 0), "npcs/miki/miki-body.png",
    (0, 0), "npcs/miki/miki-outfit-[outfit].png",
    (0, 0), "npcs/miki/miki-face-happy.png",
    (0, 0), "npcs/miki/miki-hair-[hair].png"
)
image miki sad= Composite(
    (965, 1500),
    (0, 0), "npcs/miki/miki-body.png",
    (0, 0), "npcs/miki/miki-outfit-[outfit].png",
    (0, 0), "npcs/miki/miki-face-sad.png",
    (0, 0), "npcs/miki/miki-hair-[hair].png"
)
image miki serious= Composite(
    (965, 1500),
    (0, 0), "npcs/miki/miki-body.png",
    (0, 0), "npcs/miki/miki-outfit-[outfit].png",
    (0, 0), "npcs/miki/miki-face-serious.png",
    (0, 0), "npcs/miki/miki-hair-[hair].png"
)
image miki talk= Composite(
    (965, 1500),
    (0, 0), "npcs/miki/miki-body.png",
    (0, 0), "npcs/miki/miki-outfit-[outfit].png",
    (0, 0), "npcs/miki/miki-face-talk.png",
    (0, 0), "npcs/miki/miki-hair-[hair].png"
)
image miki very_happy= Composite(
    (965, 1500),
    (0, 0), "npcs/miki/miki-body.png",
    (0, 0), "npcs/miki/miki-outfit-[outfit].png",
    (0, 0), "npcs/miki/miki-face-very_happy.png",
    (0, 0), "npcs/miki/miki-hair-[hair].png"
)

define character.miki = Character("Miki", image = "miki", callback = move_character, window_background = Image("npc_dialog.png", xalign=0.5, yalign=1.0))
default miki = Npcs("woman")


## Nicky
image nicky = Composite(
    (965, 1500),
    (0, 0), "npcs/nicky/nicky-body.png",
    (0, 0), "npcs/nicky/nicky-outfit-[outfit].png",
    (0, 0), "npcs/nicky/nicky-face-neutral.png",
    (0, 0), "npcs/nicky/nicky-hair-[hair].png"
)
image nicky angry= Composite(
    (965, 1500),
    (0, 0), "npcs/nicky/nicky-body.png",
    (0, 0), "npcs/nicky/nicky-outfit-[outfit].png",
    (0, 0), "npcs/nicky/nicky-face-angry.png",
    (0, 0), "npcs/nicky/nicky-hair-[hair].png"
)
image nicky awkward= Composite(
    (965, 1500),
    (0, 0), "npcs/nicky/nicky-body.png",
    (0, 0), "npcs/nicky/nicky-outfit-[outfit].png",
    (0, 0), "npcs/nicky/nicky-face-awkward.png",
    (0, 0), "npcs/nicky/nicky-hair-[hair].png"
)
image nicky flirt= Composite(
    (965, 1500),
    (0, 0), "npcs/nicky/nicky-body.png",
    (0, 0), "npcs/nicky/nicky-outfit-[outfit].png",
    (0, 0), "npcs/nicky/nicky-face-flirt.png",
    (0, 0), "npcs/nicky/nicky-hair-[hair].png"
)
image nicky happy= Composite(
    (965, 1500),
    (0, 0), "npcs/nicky/nicky-body.png",
    (0, 0), "npcs/nicky/nicky-outfit-[outfit].png",
    (0, 0), "npcs/nicky/nicky-face-happy.png",
    (0, 0), "npcs/nicky/nicky-hair-[hair].png"
)
image nicky sad= Composite(
    (965, 1500),
    (0, 0), "npcs/nicky/nicky-body.png",
    (0, 0), "npcs/nicky/nicky-outfit-[outfit].png",
    (0, 0), "npcs/nicky/nicky-face-sad.png",
    (0, 0), "npcs/nicky/nicky-hair-[hair].png"
)
image nicky serious= Composite(
    (965, 1500),
    (0, 0), "npcs/nicky/nicky-body.png",
    (0, 0), "npcs/nicky/nicky-outfit-[outfit].png",
    (0, 0), "npcs/nicky/nicky-face-serious.png",
    (0, 0), "npcs/nicky/nicky-hair-[hair].png"
)
image nicky talk= Composite(
    (965, 1500),
    (0, 0), "npcs/nicky/nicky-body.png",
    (0, 0), "npcs/nicky/nicky-outfit-[outfit].png",
    (0, 0), "npcs/nicky/nicky-face-talk.png",
    (0, 0), "npcs/nicky/nicky-hair-[hair].png"
)
image nicky very_happy= Composite(
    (965, 1500),
    (0, 0), "npcs/nicky/nicky-body.png",
    (0, 0), "npcs/nicky/nicky-outfit-[outfit].png",
    (0, 0), "npcs/nicky/nicky-face-very_happy.png",
    (0, 0), "npcs/nicky/nicky-hair-[hair].png"
)

define character.nicky = Character("Nicky", image = "nicky", callback = move_character, window_background = Image("npc_dialog.png", xalign=0.5, yalign=1.0))
default nicky = Npcs("man")


## Rafi
define character.rafi = Character("Rafi", window_background = Image("npc_dialog.png", xalign=0.5, yalign=1.0))
default rafi = Npcs("man")


## Seb
image seb = Composite(
    (965, 1500),
    (0, 0), "npcs/seb/seb-body.png",
    (0, 0), "npcs/seb/seb-outfit-[outfit].png",
    (0, 0), "npcs/seb/seb-face-neutral.png",
    (0, 0), "npcs/seb/seb-hair-[hair].png"
)
image seb angry= Composite(
    (965, 1500),
    (0, 0), "npcs/seb/seb-body.png",
    (0, 0), "npcs/seb/seb-outfit-[outfit].png",
    (0, 0), "npcs/seb/seb-face-angry.png",
    (0, 0), "npcs/seb/seb-hair-[hair].png"
)
image seb awkward= Composite(
    (965, 1500),
    (0, 0), "npcs/seb/seb-body.png",
    (0, 0), "npcs/seb/seb-outfit-[outfit].png",
    (0, 0), "npcs/seb/seb-face-awkward.png",
    (0, 0), "npcs/seb/seb-hair-[hair].png"
)
image seb flirt= Composite(
    (965, 1500),
    (0, 0), "npcs/seb/seb-body.png",
    (0, 0), "npcs/seb/seb-outfit-[outfit].png",
    (0, 0), "npcs/seb/seb-face-flirt.png",
    (0, 0), "npcs/seb/seb-hair-[hair].png"
)
image seb happy= Composite(
    (965, 1500),
    (0, 0), "npcs/seb/seb-body.png",
    (0, 0), "npcs/seb/seb-outfit-[outfit].png",
    (0, 0), "npcs/seb/seb-face-happy.png",
    (0, 0), "npcs/seb/seb-hair-[hair].png"
)
image seb sad= Composite(
    (965, 1500),
    (0, 0), "npcs/seb/seb-body.png",
    (0, 0), "npcs/seb/seb-outfit-[outfit].png",
    (0, 0), "npcs/seb/seb-face-sad.png",
    (0, 0), "npcs/seb/seb-hair-[hair].png"
)
image seb serious= Composite(
    (965, 1500),
    (0, 0), "npcs/seb/seb-body.png",
    (0, 0), "npcs/seb/seb-outfit-[outfit].png",
    (0, 0), "npcs/seb/seb-face-serious.png",
    (0, 0), "npcs/seb/seb-hair-[hair].png"
)
image seb talk= Composite(
    (965, 1500),
    (0, 0), "npcs/seb/seb-body.png",
    (0, 0), "npcs/seb/seb-outfit-[outfit].png",
    (0, 0), "npcs/seb/seb-face-talk.png",
    (0, 0), "npcs/seb/seb-hair-[hair].png"
)
image seb very_happy= Composite(
    (965, 1500),
    (0, 0), "npcs/seb/seb-body.png",
    (0, 0), "npcs/seb/seb-outfit-[outfit].png",
    (0, 0), "npcs/seb/seb-face-very_happy.png",
    (0, 0), "npcs/seb/seb-hair-[hair].png"
)

define character.seb = Character("Seb", image = "seb", callback = move_character, window_background = Image("npc_dialog.png", xalign=0.5, yalign=1.0))
default seb = Npcs("man")


## Tai
define character.tai = Character("Tai", window_background = Image("npc_dialog.png", xalign=0.5, yalign=1.0))
default tai = Npcs("man")


## Yasmin
define character.yasmin = Character("Yasmin", window_background = Image("npc_dialog.png", xalign=0.5, yalign=1.0))
default yasmin = Npcs("woman")