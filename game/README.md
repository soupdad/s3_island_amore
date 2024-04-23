# Island Amore /game
This repo is specifically for the recreation of LITG S3.
- Please feel free to adjust and optimize anything I've coded previously. Just make sure that it works before merging anything into main :))

## Folders
- audio - Currently nothing is saved in here. If we add music or voice acting those mp3 or wav files would go here.
- gui - Image files used in the menus.
- images - Image files used during gameplay for backgrounds, characters, and dialog boxes.
    - bgs - Background images.
    - map_icons - NPC's map icons. Will update later with better looking ones, these are just placeholders.
    - npc - Each NPC has folder with their name that stores the different parts of their character's look
        - Also has vertical and horizonal visual naming guides for the different expressions the NPCs can wear.
            - I recommend looking at it when coding expression changes because some of the faces are not intuitive (I tried my best lol).
- tl - Standard language files. This is where files will go if we translate game into other languages.

## Files
- characters
    - All custom declared functions and classes including:
        - Function that controls automatic on screen character movement.
        - MainCharacter and Npc classes.
    - Each NPC character declaration with their corresponding images.
    - MC character declaration.
    - Text message character declaration.
- gameplay_variables
    - The individual variables used in gameplay separated by the episode and part they are used in.
    - Each variable includes what type it is and the possibilities for it.
    - Each variable starts with the season, episode, and part it is used in.
        - Ex. s3e2p2_variable_name
- gui - Default file from RenPy that defines how the menus look.
- options - Default file from RenPy that defines what options are available to the user.
- screens - Default file from RenPy that defines what the different screens look like.
    - Custom Screens - Defined at bottom of this file, seperated by the episode and part they are used in.
- script
    - Transitions defined.
    - Defines what label is called when character selects "Start" on main menu.
        - This is good for testing a specific episode
- e1e2e3
    - Holds the dialog and logic for the first 3 episodes/days of gameplay.
    - Since there are many lines of dialog in each day/episode the gameplay files will hold only 3 days each.
        - So this one is for the first 3 in-game days.