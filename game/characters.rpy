####################################################################
## Custom Functions and Classes
####################################################################
init python:
    on_screen = []

    def npc_exit(name):
        '''
        Manually removes NPC from being visible on screen.

        Currently doesn't work.
        '''
        renpy.show(name, [npc_exit])
        renpy.pause(0.3)
        renpy.hide(name)
        on_screen.remove(name)

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
            "Iona":0, "Genevieve":0, "Miki":0, "Nicky":0, "Seb":0,
            "Yasmin":0, "Ciaran":0, "Tai":0}

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
layeredimage aj:
    always:
        "npcs/aj/aj-body.png"
    
    attribute outfit default:
        "npcs/aj/aj-outfit-[outfit].png"

    group face auto:
        attribute neutral default:
            "npcs/aj/aj-face-neutral.png"
        attribute angry:
            "npcs/aj/aj-face-angry.png"
        attribute awkward:
            "npcs/aj/aj-face-awkward.png"
        attribute flirt:
            "npcs/aj/aj-face-flirt.png"
        attribute happy:
            "npcs/aj/aj-face-happy.png"
        attribute sad:
            "npcs/aj/aj-face-sad.png"
        attribute serious:
            "npcs/aj/aj-face-serious.png"
        attribute talk:
            "npcs/aj/aj-face-talk.png"
        attribute very_happy:
            "npcs/aj/aj-face-very_happy.png"

    attribute hair default:
        "npcs/aj/aj-hair-[hair].png"

define character.aj = Character("AJ", image = "aj", callback = move_character, window_background = Image("npc_dialog.png", xalign=0.5, yalign=1.0))
default aj = Npcs("woman")

## Bill
layeredimage bill:
    always:
        "npcs/bill/bill-body.png"
    
    attribute outfit default:
        "npcs/bill/bill-outfit-[outfit].png"

    group face auto:
        attribute neutral default:
            "npcs/bill/bill-face-neutral.png"
        attribute angry:
            "npcs/bill/bill-face-angry.png"
        attribute awkward:
            "npcs/bill/bill-face-awkward.png"
        attribute flirt:
            "npcs/bill/bill-face-flirt.png"
        attribute happy:
            "npcs/bill/bill-face-happy.png"
        attribute sad:
            "npcs/bill/bill-face-sad.png"
        attribute serious:
            "npcs/bill/bill-face-serious.png"
        attribute talk:
            "npcs/bill/bill-face-talk.png"
        attribute very_happy:
            "npcs/bill/bill-face-very_happy.png"

    group hair auto:
        attribute hair default:
            "npcs/bill/bill-hair-[hair].png"
        attribute bucket:
            "npcs/bill/bill-hair-bucket_[bucket].png"

define character.bill = Character("Bill", image = "bill", callback = move_character, window_background = Image("npc_dialog.png", xalign=0.5, yalign=1.0))
default bill = Npcs("man")

## Camilo
layeredimage camilo:
    always:
        "npcs/camilo/camilo-body.png"
    
    attribute outfit default:
        "npcs/camilo/camilo-outfit-[outfit].png"

    group face auto:
        attribute neutral default:
            "npcs/camilo/camilo-face-neutral.png"
        attribute angry:
            "npcs/camilo/camilo-face-angry.png"
        attribute awkward:
            "npcs/camilo/camilo-face-awkward.png"
        attribute flirt:
            "npcs/camilo/camilo-face-flirt.png"
        attribute happy:
            "npcs/camilo/camilo-face-happy.png"
        attribute sad:
            "npcs/camilo/camilo-face-sad.png"
        attribute serious:
            "npcs/camilo/camilo-face-serious.png"
        attribute talk:
            "npcs/camilo/camilo-face-talk.png"
        attribute very_happy:
            "npcs/camilo/camilo-face-very_happy.png"

    attribute hair default:
        "npcs/camilo/camilo-hair-[hair].png"

define character.camilo = Character("Camilo", image = "camilo", callback = move_character, window_background = Image("npc_dialog.png", xalign=0.5, yalign=1.0))
default camilo = Npcs("man")

## Ciaran
layeredimage ciaran:
    always:
        "npcs/ciaran/ciaran-body.png"
    
    attribute outfit default:
        "npcs/ciaran/ciaran-outfit-[outfit].png"

    group face auto:
        attribute neutral default:
            "npcs/ciaran/ciaran-face-neutral.png"
        attribute angry:
            "npcs/ciaran/ciaran-face-angry.png"
        attribute awkward:
            "npcs/ciaran/ciaran-face-awkward.png"
        attribute flirt:
            "npcs/ciaran/ciaran-face-flirt.png"
        attribute happy:
            "npcs/ciaran/ciaran-face-happy.png"
        attribute sad:
            "npcs/ciaran/ciaran-face-sad.png"
        attribute serious:
            "npcs/ciaran/ciaran-face-serious.png"
        attribute talk:
            "npcs/ciaran/ciaran-face-talk.png"
        attribute very_happy:
            "npcs/ciaran/ciaran-face-very_happy.png"

    attribute hair default:
        "npcs/ciaran/ciaran-hair-[hair].png"

define character.ciaran = Character("Ciaran", image = "ciaran", callback = move_character, window_background = Image("npc_dialog.png", xalign=0.5, yalign=1.0))
default ciaran = Npcs("man")

## Elladine
layeredimage elladine:
    always:
        "npcs/elladine/elladine-body.png"
    
    attribute outfit default:
        "npcs/elladine/elladine-outfit-[outfit].png"

    group face auto:
        attribute neutral default:
            "npcs/elladine/elladine-face-neutral.png"
        attribute angry:
            "npcs/elladine/elladine-face-angry.png"
        attribute awkward:
            "npcs/elladine/elladine-face-awkward.png"
        attribute flirt:
            "npcs/elladine/elladine-face-flirt.png"
        attribute happy:
            "npcs/elladine/elladine-face-happy.png"
        attribute sad:
            "npcs/elladine/elladine-face-sad.png"
        attribute serious:
            "npcs/elladine/elladine-face-serious.png"
        attribute talk:
            "npcs/elladine/elladine-face-talk.png"
        attribute very_happy:
            "npcs/elladine/elladine-face-very_happy.png"

    attribute hair default:
        "npcs/elladine/elladine-hair-[hair].png"

define character.elladine = Character("Elladine", image = "elladine", callback = move_character, window_background = Image("npc_dialog.png", xalign=0.5, yalign=1.0))
default elladine = Npcs("woman")


## Genevieve
layeredimage genevieve:
    always:
        "npcs/genevieve/genevieve-body.png"
    
    attribute outfit default:
        "npcs/genevieve/genevieve-outfit-[outfit].png"

    group face auto:
        attribute neutral default:
            "npcs/genevieve/genevieve-face-neutral.png"
        attribute angry:
            "npcs/genevieve/genevieve-face-angry.png"
        attribute awkward:
            "npcs/genevieve/genevieve-face-awkward.png"
        attribute flirt:
            "npcs/genevieve/genevieve-face-flirt.png"
        attribute happy:
            "npcs/genevieve/genevieve-face-happy.png"
        attribute sad:
            "npcs/genevieve/genevieve-face-sad.png"
        attribute serious:
            "npcs/genevieve/genevieve-face-serious.png"
        attribute talk:
            "npcs/genevieve/genevieve-face-talk.png"
        attribute very_happy:
            "npcs/genevieve/genevieve-face-very_happy.png"

    attribute hair default:
        "npcs/genevieve/genevieve-hair-[hair].png"

define character.genevieve = Character("Genevieve", image = "genevieve", callback = move_character, window_background = Image("npc_dialog.png", xalign=0.5, yalign=1.0))
default genevieve = Npcs("woman")


## Harry
layeredimage harry:
    always:
        "npcs/harry/harry-body.png"
    
    attribute outfit default:
        "npcs/harry/harry-outfit-[outfit].png"

    group face auto:
        attribute neutral default:
            "npcs/harry/harry-face-neutral.png"
        attribute angry:
            "npcs/harry/harry-face-angry.png"
        attribute awkward:
            "npcs/harry/harry-face-awkward.png"
        attribute flirt:
            "npcs/harry/harry-face-flirt.png"
        attribute happy:
            "npcs/harry/harry-face-happy.png"
        attribute sad:
            "npcs/harry/harry-face-sad.png"
        attribute serious:
            "npcs/harry/harry-face-serious.png"
        attribute talk:
            "npcs/harry/harry-face-talk.png"
        attribute very_happy:
            "npcs/harry/harry-face-very_happy.png"

    attribute hair default:
        "npcs/harry/harry-hair-[hair].png"

define character.harry = Character("Harry", image = "harry", callback = move_character, window_background = Image("npc_dialog.png", xalign=0.5, yalign=1.0))
default harry = Npcs("man")


## Iona
layeredimage iona:
    always:
        "npcs/iona/iona-body.png"
    
    attribute outfit default:
        "npcs/iona/iona-outfit-[outfit].png"

    group face auto:
        attribute neutral default:
            "npcs/iona/iona-face-neutral.png"
        attribute angry:
            "npcs/iona/iona-face-angry.png"
        attribute awkward:
            "npcs/iona/iona-face-awkward.png"
        attribute flirt:
            "npcs/iona/iona-face-flirt.png"
        attribute happy:
            "npcs/iona/iona-face-happy.png"
        attribute sad:
            "npcs/iona/iona-face-sad.png"
        attribute serious:
            "npcs/iona/iona-face-serious.png"
        attribute talk:
            "npcs/iona/iona-face-talk.png"
        attribute very_happy:
            "npcs/iona/iona-face-very_happy.png"

    attribute hair default:
        "npcs/iona/iona-hair-[hair].png"

define character.iona = Character("Iona", image = "iona", callback = move_character, window_background = Image("npc_dialog.png", xalign=0.5, yalign=1.0))
default iona = Npcs("woman")


## Lily
define character.lily = Character("Lily", window_background = Image("npc_dialog.png", xalign=0.5, yalign=1.0))
default lily = Npcs("woman")


## Miki
layeredimage miki:
    always:
        "npcs/miki/miki-body.png"
    
    attribute outfit default:
        "npcs/miki/miki-outfit-[outfit].png"

    group face auto:
        attribute neutral default:
            "npcs/miki/miki-face-neutral.png"
        attribute angry:
            "npcs/miki/miki-face-angry.png"
        attribute awkward:
            "npcs/miki/miki-face-awkward.png"
        attribute flirt:
            "npcs/miki/miki-face-flirt.png"
        attribute happy:
            "npcs/miki/miki-face-happy.png"
        attribute sad:
            "npcs/miki/miki-face-sad.png"
        attribute serious:
            "npcs/miki/miki-face-serious.png"
        attribute talk:
            "npcs/miki/miki-face-talk.png"
        attribute very_happy:
            "npcs/miki/miki-face-very_happy.png"

    attribute hair default:
        "npcs/miki/miki-hair-[hair].png"

define character.miki = Character("Miki", image = "miki", callback = move_character, window_background = Image("npc_dialog.png", xalign=0.5, yalign=1.0))
default miki = Npcs("woman")


## Nicky
layeredimage nicky:
    always:
        "npcs/nicky/nicky-body.png"
    
    attribute outfit default:
        "npcs/nicky/nicky-outfit-[outfit].png"

    group face auto:
        attribute neutral default:
            "npcs/nicky/nicky-face-neutral.png"
        attribute angry:
            "npcs/nicky/nicky-face-angry.png"
        attribute awkward:
            "npcs/nicky/nicky-face-awkward.png"
        attribute flirt:
            "npcs/nicky/nicky-face-flirt.png"
        attribute happy:
            "npcs/nicky/nicky-face-happy.png"
        attribute sad:
            "npcs/nicky/nicky-face-sad.png"
        attribute serious:
            "npcs/nicky/nicky-face-serious.png"
        attribute talk:
            "npcs/nicky/nicky-face-talk.png"
        attribute very_happy:
            "npcs/nicky/nicky-face-very_happy.png"

    attribute hair default:
        "npcs/nicky/nicky-hair-[hair].png"

define character.nicky = Character("Nicky", image = "nicky", callback = move_character, window_background = Image("npc_dialog.png", xalign=0.5, yalign=1.0))
default nicky = Npcs("man")


## Rafi
define character.rafi = Character("Rafi", window_background = Image("npc_dialog.png", xalign=0.5, yalign=1.0))
default rafi = Npcs("man")


## Seb
layeredimage seb:
    always:
        "npcs/seb/seb-body.png"
    
    attribute outfit default:
        "npcs/seb/seb-outfit-[outfit].png"

    group face auto:
        attribute neutral default:
            "npcs/seb/seb-face-neutral.png"
        attribute angry:
            "npcs/seb/seb-face-angry.png"
        attribute awkward:
            "npcs/seb/seb-face-awkward.png"
        attribute flirt:
            "npcs/seb/seb-face-flirt.png"
        attribute happy:
            "npcs/seb/seb-face-happy.png"
        attribute sad:
            "npcs/seb/seb-face-sad.png"
        attribute serious:
            "npcs/seb/seb-face-serious.png"
        attribute talk:
            "npcs/seb/seb-face-talk.png"
        attribute very_happy:
            "npcs/seb/seb-face-very_happy.png"

    attribute hair default:
        "npcs/seb/seb-hair-[hair].png"

define character.seb = Character("Seb", image = "seb", callback = move_character, window_background = Image("npc_dialog.png", xalign=0.5, yalign=1.0))
default seb = Npcs("man")


## Tai
layeredimage tai:
    always:
        "npcs/tai/tai-hair-back.png"

    always:
        "npcs/tai/tai-body.png"
    
    attribute outfit default:
        "npcs/tai/tai-outfit-[outfit].png"

    group face auto:
        attribute neutral default:
            "npcs/tai/tai-face-neutral.png"
        attribute angry:
            "npcs/tai/tai-face-angry.png"
        attribute awkward:
            "npcs/tai/tai-face-awkward.png"
        attribute flirt:
            "npcs/tai/tai-face-flirt.png"
        attribute happy:
            "npcs/tai/tai-face-happy.png"
        attribute sad:
            "npcs/tai/tai-face-sad.png"
        attribute serious:
            "npcs/tai/tai-face-serious.png"
        attribute talk:
            "npcs/tai/tai-face-talk.png"
        attribute very_happy:
            "npcs/tai/tai-face-very_happy.png"

    attribute hair default:
        "npcs/tai/tai-hair-[hair].png"

define character.tai = Character("Tai", image = "tai", callback = move_character, window_background = Image("npc_dialog.png", xalign=0.5, yalign=1.0))
default tai = Npcs("man")

default extra = "none"
## Yasmin
layeredimage yasmin:
    always:
        "npcs/yasmin/yasmin-body.png"
    
    attribute outfit default:
        "npcs/yasmin/yasmin-outfit-[outfit].png"

    group face auto:
        attribute neutral default:
            "npcs/yasmin/yasmin-face-neutral.png"
        attribute angry:
            "npcs/yasmin/yasmin-face-angry.png"
        attribute awkward:
            "npcs/yasmin/yasmin-face-awkward.png"
        attribute flirt:
            "npcs/yasmin/yasmin-face-flirt.png"
        attribute happy:
            "npcs/yasmin/yasmin-face-happy.png"
        attribute sad:
            "npcs/yasmin/yasmin-face-sad.png"
        attribute serious:
            "npcs/yasmin/yasmin-face-serious.png"
        attribute talk:
            "npcs/yasmin/yasmin-face-talk.png"
        attribute very_happy:
            "npcs/yasmin/yasmin-face-very_happy.png"

    attribute hair default:
        "npcs/yasmin/yasmin-hair-[hair].png"

    attribute extra default:
        "npcs/yasmin/yasmin-extras-[extra].png"

define character.yasmin = Character("Yasmin", image = "yasmin", callback = move_character, window_background = Image("npc_dialog.png", xalign=0.5, yalign=1.0))
default yasmin = Npcs("woman")