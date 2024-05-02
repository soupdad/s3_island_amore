#########################################################################
## Episode 4, Part 1
#########################################################################
label s3e4p1:
    scene sand with dissolve
    $ on_screen = []

    show screen day_title(4, 1) with Pause(4)
    hide screen day_title with dissolve

    $ outfit = "evening"

    "Last time on Love Island..."
    "The ball was finally back in [s3_name]'s court."

    if s3_mc.past_partners[0] == s3_mc.current_partner:
        "No prizes for guessing who she went for..."
        s3_mc "The person I'd like to couple up with is... [s3_mc.current_partner]."
        "Yes, two days after losing him, she's back with [s3_mc.current_partner]..."
        "It's like watching a ping pong match in slow motion."
    else:
        "And instead of going for [s3_mc.past_partners[0]], she decided to surprise everyone and change things up..."
        s3_mc "The person I'd like to couple up with is... [s3_mc.current_partner]."

    "As expected, there was no end of crying, accusations of broken girl code and..."

    if s3_mc.current_partner == "Bill":
        miki "I really didn't want to cause a scene."
        miki "I don't want you to think I'm in a mood with you or anything. I'm not."
        show miki at npc_exit
        pause .3
        $ renpy.hide("miki")
        $ on_screen = []
    elif s3_mc.current_partner == "Camilo":
        iona "I really didn't want to cause a scene."
        iona "I don't want you to think I'm in a mood with you or anything. I'm not."
        show iona at npc_exit
        pause .3
        $ renpy.hide("iona")
        $ on_screen = []
    elif s3_mc.current_partner == "Harry":
        genevieve "I really didn't want to cause a scene."
        genevieve "I don't want you to think I'm in a mood with you or anything. I'm not."
        show genevieve at npc_exit
        pause .3
        $ renpy.hide("genevieve")
        $ on_screen = []
    elif s3_mc.current_partner == "AJ":
        seb "I really didn't want to cause a scene."
        seb "I don't want you to think I'm in a mood with you or anything. I'm not."
        show aj at npc_exit
        pause .3
        $ renpy.hide("aj")
        $ on_screen = []

    "Wait, what? I must have tuned into the wrong channel. It looked like [s3_3rd_girl_options[s3_mc.current_partner]] was handling it well."
    "Coming up..."
    "One of the boys isn't in the mood for some friendly ribbing..."

    $ outfit = "swim"
    bill "What are you doing, mate?"
    show bill at npc_exit
    pause .3
    $ renpy.hide("bill")

    "And there was me thinking it was just going to be a nice relaxing day by the pool."

    $ pronouns(s3_mc.current_partner)

    scene s3-bedroom-day with dissolve
    $ on_screen = []

    $ outfit = "pjs"

    "All is quiet in the Villa, except for a few soft snores."
    "You wake up wrapped up in [s3_mc.current_partner]'s strong arms."
    "You take a moment to watch [him_her] sleep."
    thought "After all that time being single, it's actually nice to wake up next to someone."

    # CHOICE
    menu:
        thought "[s3_mc.current_partner] looks..."
        "Cute as a button":
            thought "I could stare at [him_her] for hours."
        "Hot like fiyah":
            thought "It's ridiculous. Who looks that hot first thing in the morning?"
        "Funny...":
            thought "[he_she!c] looks totally out of it. I could totally draw on his face..."

    "[s3_mc.current_partner] stirs, opens [his_her] eyes and catches you gazing at [him_her]."

    if s3_mc.current_partner == "Bill":
        bill "Were you watching me sleep?"
    elif s3_mc.current_partner == "Camilo":
        camilo "Were you watching me sleep?"
    elif s3_mc.current_partner == "Harry":
        harry "Were you watching me sleep?"
    elif s3_mc.current_partner == "AJ":
        aj "Were you watching me sleep?"

    # CHOICE
    menu:
        thought "[s3_mc.current_partner] caught me watching [him_her]..."
        "Can you blame me?":
            s3_mc "You're gorgeous. I couldn't help myself."

            if s3_mc.current_partner == "Bill":
                bill "You're not too bad yourself."
            elif s3_mc.current_partner == "Camilo":
                camilo "You're not too bad yourself."
            elif s3_mc.current_partner == "Harry":
                harry "You're not too bad yourself."
            elif s3_mc.current_partner == "AJ":
                aj "You're pretty fit too."
        "You sleep funny":
            $ s3_mc.dislike(s3_mc.current_partner)
            s3_mc "You stick your arms out so wide, you look like a scarecrow."

            if s3_mc.current_partner == "Bill":
                bill "Is that a good thing?"
                s3_mc "It's funny!"
                bill "I'll take your word for it."
                bill "Let's start again."
            elif s3_mc.current_partner == "Camilo":
                camilo "Is that a good thing?"
                s3_mc "It's funny!"
                camilo "I'll take your word for it."
                camilo "Let's start again."
            elif s3_mc.current_partner == "Harry":
                harry "Is that a good thing?"
                s3_mc "It's funny!"
                harry "I'll take your word for it."
                harry "Let's start again."
            elif s3_mc.current_partner == "AJ":
                aj "Is that a good thing?"
                s3_mc "It's funny!"
                aj "I'll take your word for it."
                aj "Let's start again."
        "Who, me?":
            if s3_mc.current_partner == "Bill":
                bill "Yeah you, silly."
                s3_mc "I don't know what you're talking about."
                bill "Aw, you're embarrassed. I thought it was cute."
            elif s3_mc.current_partner == "Camilo":
                camilo "Yeah you, silly."
                s3_mc "I don't know what you're talking about."
                camilo "Aw, you're embarrassed. I thought it was cute."
            elif s3_mc.current_partner == "Harry":
                harry "Yeah you, silly."
                s3_mc "I don't know what you're talking about."
                harry "Aw, you're embarrassed. I thought it was cute."
            elif s3_mc.current_partner == "AJ":
                aj "Yeah you, silly."
                s3_mc "I don't know what you're talking about."
                aj "Aw, you're embarrassed. I thought it was cute."

    "[s3_mc.current_partner] smiles and stretches before wrapping [his_her] arms around you and pulling you closer."

    if s3_mc.current_partner == "Bill":
        bill "Morning."
        "You're so close your noses are almost touching. You can feel the warmth of [s3_mc.current_partner]'s breath."
        bill "This is nice. You and me, all coupled up. I don't think it could get any better."
        s3_mc "I can think of one thing that would make it better..."
        bill "Oh really? And what would that be?"
    elif s3_mc.current_partner == "Camilo":
        camilo "Morning."
        "You're so close your noses are almost touching. You can feel the warmth of [s3_mc.current_partner]'s breath."
        camilo "This is nice. You and me, all coupled up. I don't think it could get any better."
        s3_mc "I can think of one thing that would make it better..."
        camilo "Oh really? And what would that be?"
    elif s3_mc.current_partner == "Harry":
        harry "Morning."
        "You're so close your noses are almost touching. You can feel the warmth of [s3_mc.current_partner]'s breath."
        harry "This is nice. You and me, all coupled up. I don't think it could get any better."
        s3_mc "I can think of one thing that would make it better..."
        harry "Oh really? And what would that be?"
    elif s3_mc.current_partner == "AJ":
        aj "Morning."
        "You're so close your noses are almost touching. You can feel the warmth of [s3_mc.current_partner]'s breath."
        aj "This is nice. You and me, all coupled up. I don't think it could get any better."
        s3_mc "I can think of one thing that would make it better..."
        aj "Oh really? And what would that be?"
    
    # CHOICE
    menu:
        thought "Hmm, what would make this moment even better?"
        "A kiss":
            $ s3e4p1_kiss_or_cuddle = True
            "You lean closer."

            if s3_mc.current_partner == "Bill":
                bill "Oh, you mean..."
            elif s3_mc.current_partner == "Camilo":
                camilo "Oh, you mean..."
            elif s3_mc.current_partner == "Harry":
                harry "Oh, you mean..."
            elif s3_mc.current_partner == "AJ":
                aj "Oh, you mean..."

            "[s3_mc.current_partner] smiles seductively and pulls you closer. [his_her!c] lips press firmly against yours."

            if s3_mc.current_partner == "Bill" or s3_mc.current_partner == "Harry":
                "The kiss starts gently but builds in intensity."
                "His kisses move towards your collar bone, sending tingles down your spine."
            elif s3_mc.current_partner == "AJ" or s3_mc.current_partner == "Camilo":
                "You feel [his_her] tongue trace your lips and then [he_she] gently bites your bottom lip."
                if s3_mc.current_partner == "Camilo":
                    camilo "I could eat you."
                else:
                    aj "I could eat you."
                "[he_she!c] nibbles down your neck, making you giggle."

            "You pull away, a little breathless."
            s3_mc "We're going to wake everyone up."

            if s3_mc.current_partner == "Bill":
                bill "Good. They should be up anyway."
            elif s3_mc.current_partner == "Camilo":
                camilo "Good. They should be up anyway."
            elif s3_mc.current_partner == "Harry":
                harry "Good. They should be up anyway."
            elif s3_mc.current_partner == "AJ":
                aj "Good. They should be up anyway."
        "A cuddle":
            $ s3e4p1_kiss_or_cuddle = True
            "You roll over, facing away from [him_her]. Then start to wiggle backwards until your body is nuzzled into [him_her]."

            if s3_mc.current_partner == "Bill":
                bill "Woah, what are you doing?"
            elif s3_mc.current_partner == "Camilo":
                camilo "Woah, what are you doing?"
            elif s3_mc.current_partner == "Harry":
                harry "Woah, what are you doing?"
            elif s3_mc.current_partner == "AJ":
                aj "Woah, what are you doing?"

            s3_mc "Being the little spoon."
            "You take [s3_mc.current_partner]'s arms and pull them in tight around your waist."
            s3_mc "Morning cuddles are the best."
            "[he_she!c] rests [his_her] chin on your shoulder."
            "You feel [his_her] body envelop yours. It's warm and reassuring."

            if s3_mc.current_partner == "Bill":
                bill "Hmm, I could get used to this."
            elif s3_mc.current_partner == "Camilo":
                camilo "Hmm, I could get used to this."
            elif s3_mc.current_partner == "Harry":
                harry "Hmm, I could get used to this."
            elif s3_mc.current_partner == "AJ":
                aj "Hmm, I could get used to this."
        "A cuppa":
            "You beckon [s3_mc.current_partner] closer with your finger. [he_she!c] smiles and leans in."
            s3_mc "What I'd really love..."

            if s3_mc.current_partner == "Bill":
                bill "Yeah..."
            elif s3_mc.current_partner == "Camilo":
                camilo "Yeah..."
            elif s3_mc.current_partner == "Harry":
                harry "Yeah..."
            elif s3_mc.current_partner == "AJ":
                aj "Yeah..."

            s3_mc "It's a nice, hot, sweet..."
            s3_mc "...cup of tea."

            if s3_mc.current_partner == "Bill":
                bill "Oh. You want a cuppa."
                bill "Actually, I could really go for one too."
            elif s3_mc.current_partner == "Camilo":
                camilo "Oh. You want a cuppa."
                camilo "Actually, I could really go for one too."
            elif s3_mc.current_partner == "Harry":
                harry "Oh. You want a cuppa."
                harry "Actually, I could really go for one too."
            elif s3_mc.current_partner == "AJ":
                aj "Oh. You want a cuppa."
                aj "Actually, I could really go for one too."

    "As Genevieve emerges and switches the lights on, Seb puts a pillow over his head and groans."
    seb "Ugh, turn it off!"
    genevieve "You're awake already! Your body clock says it's time to get up."
    seb "Can I put my body clock on snooze?"
    seb "I just need another hour. I'm knackered."
    nicky "Come on man! Today's the best day ever."

    if s3_mc.current_partner != "AJ":
        "Seb shivers and looks over at AJ who has taken all the sheets."
        seb "You didn't have to wrestle AJ for a sliver of duvet."
        "AJ stirs and Seb takes the opportunity to steal some back."
        aj "Hey!"
        "AJ sits up sleepily."
        aj "Might as well get up then."
        nicky "C'mon, it's the furthest we're going to be from another recoupling."
        s3_mc "Nicky's got a point. That's worth celebrating."
        seb "Fair point."
        "Seb jumps out of the bed and the Islanders cheer."
        seb "Time to seize the day."
        "AJ jumps up with a smile and starts jogging on the spot."
        aj "Yes! That's the Seb I've been waiting for!"
        aj "What do you say? A couple of laps and then we hit the gym?"
        seb "Er, maybe after brekkie. You get a head start and I'll join you."
        "AJ smiles brightly and bounds into the dressing room."
        nicky "You're going to hit the gym?"
        seb "No way. But have you tried to say no to AJ?"
        seb "I just haven't got the energy."
        camilo "The name of Seb's sex tape."
    else:
        "Seb looks over at you and AJ before covering his face with the duvet."
        seb "Unless you missed it, my night didn't end so well."
        s3_mc "C'mon Seb, remember our chat? The Villa's your oyster now!"
        seb "Can't stand oysters. They're like giant bogies in shells."
        
        "[s3e3p3_get_to_know] sits up and throws a pillow at Seb. He smiles."

        if s3e3p3_get_to_know != "Genevieve":
            if s3e3p3_get_to_know == "Miki":
                miki "Wow, a smile. I must have the magic touch."
            elif s3e3p3_get_to_know == "Iona":
                iona "Wow, a smile. I must have the magic touch."
            elif s3e3p3_get_to_know == "Elladine":
                elladine "Wow, a smile. I must have the magic touch."

            "Seb glances in your direction and you give him a wink."
            thought "Was she flirting?"
            thought "I may have actually given Seb some good advice."
        else:
            genevieve "Right, misery guts. I am putting a smile on that face today even if I have to draw it on."
            seb "You won't be able to. I'm notoriously sour faced. Ask my mum."
            genevieve "Well, Seb's mum, prepare to be amazed."
            "A smile touches the corner of his lips and he shoots you a knowing look."
            thought "Viv definitely brings out his softer side."
            thought "They'd make a lovely couple."


    "Camilo jumps out of bed and stretches."
    camilo "Ain't gonna lie, we're all set for a sexy day."
    "Bill claps his hands together with a grin."
    bill "Come on girls, time to get all leathery in the sun."


    if s3_mc.current_partner != "AJ":
        "[s3_3rd_girl_options[s3_mc.current_partner]] chucks a pillow at Bill and it hits him square in the face."
        bill "Someone woke up in a mood."

        if s3_3rd_girl_options[s3_mc.current_partner] == "Miki":
            miki "Actually, I feel great."
            miki "It's nice having the whole bed to yourself."
            miki "Especially after sharing a bed with that human starfish..."
            bill "You could've asked me for more space..."
        elif s3_3rd_girl_options[s3_mc.current_partner] == "Iona":
            iona "Actually, I feel great."
            iona "It's nice having the whole bed to yourself."
            iona "It beats being almost pushed off the bed."
            camilo "I can't help it if I'm a cuddler."
        elif s3_3rd_girl_options[s3_mc.current_partner] == "Genevieve":
            genevieve "Actually, I feel great."
            genevieve "It's nice having the whole bed to yourself."
            genevieve "No more being woken up at the crack of dawn."
            harry "You said you didn't even notice when I got up!"
    else:
        seb "Right, who's getting in the kitchen to cook me up some brekkie?"
        "A flurry of pillows go flying towards Seb."
        seb "Fine. Cereal out the box it is."

    if s3e4p1_kiss_or_cuddle == True:
        if s3_mc.current_partner == "Bill":
            bill "Right, enough chit-chat. I'm off to get this one a morning beverage."
        elif s3_mc.current_partner == "Camilo":
            camilo "Right, enough chit-chat. I'm off to get this one a morning beverage."
        elif s3_mc.current_partner == "Harry":
            harry "Right, enough chit-chat. I'm off to get this one a morning beverage."
        elif s3_mc.current_partner == "AJ":
            aj "Right, enough chit-chat. I'm off to get this one a morning beverage."

        # CHOICE
        menu:
            thought "[s3_mc.current_partner] is going to get me a drink. I want..."
            "A glass of bubbles":
                pass
            "A cuppa":
                pass
            "A matcha latte":
                pass

        if s3_mc.current_partner == "Bill":
            bill "I could probably rustle you up a regular breakfast tea..."
        elif s3_mc.current_partner == "Camilo":
            camilo "I could probably rustle you up a regular breakfast tea..."
        elif s3_mc.current_partner == "Harry":
            harry "I could probably rustle you up a regular breakfast tea..."
        elif s3_mc.current_partner == "AJ":
            aj "I could probably rustle you up a regular breakfast tea..."
    else:
        if s3_mc.current_partner == "Bill":
            bill "You still fancy that tea?"
            s3_mc "Is an elephant heavy?"
            bill "I'll get on it then."
        elif s3_mc.current_partner == "Camilo":
            camilo "You still fancy that tea?"
            s3_mc "Is an elephant heavy?"
            camilo "I'll get on it then."
        elif s3_mc.current_partner == "Harry":
            harry "You still fancy that tea?"
            s3_mc "Is an elephant heavy?"
            harry "I'll get on it then."
        elif s3_mc.current_partner == "AJ":
            aj "You still fancy that tea?"
            s3_mc "Is an elephant heavy?"
            aj "I'll get on it then."

    "You jump out of bed."
    s3_mc "I'm coming with you."
    elladine "Aw, I am loving this. You two are such a couple already. No offence [s3_3rd_girl_options[s3_mc.current_partner]]."

    if s3_3rd_girl_options[s3_mc.current_partner] == "Miki":
        miki "Nah, it's proper cute."
    elif s3_3rd_girl_options[s3_mc.current_partner] == "Iona":
        iona "Nah, it's proper cute."
    elif s3_3rd_girl_options[s3_mc.current_partner] == "Genevieve":
        genevieve "Nah, it's proper cute."
    elif s3_3rd_girl_options[s3_mc.current_partner] == "Seb":
        seb "Nah, it's proper cute."

    s3_mc "I just want to make sure [he_she] gets it just the way I like it."

    if s3_mc.current_partner == "Bill":
        bill "I can make a cuppa."
        bill "My way's foolproof. First you need to..."
    elif s3_mc.current_partner == "Camilo":
        camilo "That's sweet. I like having someone in the kitchen with me."
        camilo "And I wouldn't want to mess up your tea."
    elif s3_mc.current_partner == "Harry":
        harry "I'm from Yorkshire, we practically invented tea."
        s3_mc "Less talk, more tea!"
    elif s3_mc.current_partner == "AJ":
        bill "Make sure you unplug the toaster."
        nicky "I'll alert the fire brigade."
        s3_mc "Very funny."
        aj "That might not be a bad idea."

    s3_mc "But first I'm going to get changed. See you in the kitchen, babe."
    "You bound off towards the dressing room."

    scene s3-dressing-room with dissolve
    $ on_screen = []

    "You quickly check yourself out in the mirror and tousle your hair."

    # CHOICE
    menu:
        thought "I am looking good."
        "Blow yourself a kiss":
            "You blow your reflection a kiss."
            thought "Morning gorgeous."
        "Compliment your fine self":
            thought "Damn girl. You are looking fine. [s3_mc.current_partner] is one lucky Islander."
        "Spray your face with toner":
            "You close your eyes and spray the cool water onto your face."
            thought "So refreshing."

    thought "All I need now is a gorgeous outfit!"
    thought "Something that'll say to [s3_mc.current_partner] 'you just levelled up, hun'."

    # Add back once MC images are added to the game.
    # MC outfit changes to swimwear
    $ outfit = "swim"
    # thought "Meh, this will do I guess."
    # thought "It's tea time!"

    "You get changed into your bathing suit."
    thought "Looks good to me!"
    thought "Yup. This is definitely the ticket."

    scene s3-kitchen-day with dissolve
    $ on_screen = []

    "You never forget your first."
    "Mine was in a bed and breakfast in Dorset."
    "The sun was just coming up..."
    "Gold top milk, two sugar cubes..."
    "What did you lot think I was talking about? Mind in the gutter..."
    "[s3_mc.current_partner] is in the kitchen filling up the kettle."

    # Add back when MC images are added to the game.
    # "[he_she!c] spies you coming towards [him_her]."
    # if s3_mc.current_partner == "Bill":
    #     bill "There's my girl. Ready for your tea?"
    # elif s3_mc.current_partner == "Camilo":
    #     camilo "There's my girl. Ready for your tea?"
    # elif s3_mc.current_partner == "Harry":
    #     harry "There's my girl. Ready for your tea?"
    # elif s3_mc.current_partner == "AJ":
    #     aj "There's my girl. Ready for your tea?"
    # s3_mc "Am I ever."
    # "[he_she!c] spies you coming towards [him_her]."
    # if s3_mc.current_partner == "Bill":
    #     bill "There's my girl, pretty as always."
    # elif s3_mc.current_partner == "Camilo":
    #     camilo "There's my girl, pretty as always."
    # elif s3_mc.current_partner == "Harry":
    #     harry "There's my girl, pretty as always."
    # elif s3_mc.current_partner == "AJ":
    #     aj "There's my girl, pretty as always."
    # s3_mc "You're so sweet."
    # s3_mc "And thirsty."
    # if s3_mc.current_partner == "Bill":
    #     bill "Oh really?"
    #     s3_mc "Where's this brew then?"
    #     bill "Oh, yeah. The tea."
    # elif s3_mc.current_partner == "Camilo":
    #     camilo "Oh really?"
    #     s3_mc "Where's this brew then?"
    #     camilo "Oh, yeah. The tea."
    # elif s3_mc.current_partner == "Harry":
    #     harry "Oh really?"
    #     s3_mc "Where's this brew then?"
    #     harry "Oh, yeah. The tea."
    # elif s3_mc.current_partner == "AJ":
    #     aj "Oh really?"
    #     s3_mc "Where's this brew then?"
    #     aj "Oh, yeah. The tea."

    "[he_she!c] spies you coming towards [him_her] and does a double take."

    if s3_mc.current_partner == "Bill":
        bill "Wow. You are just... wow."
        bill "I want to make you two cups of tea now."
    elif s3_mc.current_partner == "Camilo":
        camilo "Wow. You are just... wow."
        camilo "I want to make you two cups of tea now."
    elif s3_mc.current_partner == "Harry":
        harry "Wow. You are just... wow."
        harry "I want to make you two cups of tea now."
    elif s3_mc.current_partner == "AJ":
        aj "Wow. You are just... wow."
        aj "I want to make you two cups of tea now."

    s3_mc "You're so sweet."
    s3_mc "And thirsty."

    if s3_mc.current_partner == "Bill":
        bill "Oh really?"
        s3_mc "Where's this brew then?"
        bill "Oh, yeah. The tea."
    elif s3_mc.current_partner == "Camilo":
        camilo "Oh really?"
        s3_mc "Where's this brew then?"
        camilo "Oh, yeah. The tea."
    elif s3_mc.current_partner == "Harry":
        harry "Oh really?"
        s3_mc "Where's this brew then?"
        harry "Oh, yeah. The tea."
    elif s3_mc.current_partner == "AJ":
        aj "Oh really?"
        s3_mc "Where's this brew then?"
        aj "Oh, yeah. The tea."

    "[s3_mc.current_partner] grabs two mugs, sugar and the box of teabags. [he_she] puts the kettle on."
    s3_mc "You look so focused."
    aj "I'm trying to impress you aren't I?"

    # CHOICE
    menu:
        thought "[s3_mc.current_partner] wants to impress me..."
        "You don't need to impress me":
            "[s3_mc.current_partner] turns and wraps [his_her] arms around your waist."

            if s3_mc.current_partner == "Bill":
                bill "I know. But I really want to."
                s3_mc "That's really sweet, hun."
                s3_mc "I hope you're this keen to please all the time..."
                bill "You'll find out soon enough."
            elif s3_mc.current_partner == "Camilo":
                camilo "I know. But I really want to."
                s3_mc "That's really sweet, hun."
                s3_mc "I hope you're this keen to please all the time..."
                camilo "You'll find out soon enough."
            elif s3_mc.current_partner == "Harry":
                harry "I know. But I really want to."
                s3_mc "That's really sweet, hun."
                s3_mc "I hope you're this keen to please all the time..."
                harry "You'll find out soon enough."
            elif s3_mc.current_partner == "AJ":
                aj "I know. But I really want to."
                s3_mc "That's really sweet, hun."
                s3_mc "I hope you're this keen to please all the time..."
                aj "You'll find out soon enough."
        "Tea isn't really impressive":
            if s3_mc.current_partner == "Bill":
                bill "Oh. Yeah. I mean, like, as a start."
                s3_mc "If tea's where this all starts, I'm not sure I want to see where it's going."
                bill "Wow, high maintenance, are you?"
                s3_mc "Let's just say it takes a lot to impress me."
                bill "Challenge accepted."
            elif s3_mc.current_partner == "Camilo":
                camilo "Oh. Yeah. I mean, like, as a start."
                s3_mc "If tea's where this all starts, I'm not sure I want to see where it's going."
                camilo "Wow, high maintenance, are you?"
                s3_mc "Let's just say it takes a lot to impress me."
                camilo "Challenge accepted."
            elif s3_mc.current_partner == "Harry":
                harry "Oh. Yeah. I mean, like, as a start."
                s3_mc "If tea's where this all starts, I'm not sure I want to see where it's going."
                harry "Wow, high maintenance, are you?"
                s3_mc "Let's just say it takes a lot to impress me."
                harry "Challenge accepted."
            elif s3_mc.current_partner == "AJ":
                aj "Oh. Yeah. I mean, like, as a start."
                s3_mc "If tea's where this all starts, I'm not sure I want to see where it's going."
                aj "Wow, high maintenance, are you?"
                s3_mc "Let's just say it takes a lot to impress me."
                aj "Challenge accepted."
        "Buy me diamonds!":
            "[s3_mc.current_partner] raises an eyebrow."

            if s3_mc.current_partner == "Bill":
                bill "You want diamonds?"
                s3_mc "Ooh yeah, a big one. Princess cut."
                bill "A diamond ring..."
                s3_mc "Or a necklace. No! Wait! A tiara."
                bill "Let's start with the tea."
            elif s3_mc.current_partner == "Camilo":
                camilo "You want diamonds?"
                s3_mc "Ooh yeah, a big one. Princess cut."
                camilo "A diamond ring..."
                s3_mc "Or a necklace. No! Wait! A tiara."
                camilo "Let's start with the tea."
            elif s3_mc.current_partner == "Harry":
                harry "You want diamonds?"
                s3_mc "Ooh yeah, a big one. Princess cut."
                harry "A diamond ring..."
                s3_mc "Or a necklace. No! Wait! A tiara."
                harry "Let's start with the tea."
            elif s3_mc.current_partner == "AJ":
                aj "You want diamonds?"
                s3_mc "Ooh yeah, a big one. Princess cut."
                aj "A diamond ring..."
                s3_mc "Or a necklace. No! Wait! A tiara."
                aj "Let's start with the tea."

    "The hiss of the kettle interrupts you both. [s3_mc.current_partner] grabs the mugs."
    s3_mc "Now this is where it gets serious."
    s3_mc "You can tell a lot about a person from the way they like their tea."

    if s3_mc.current_partner == "Bill":
        bill "Is that right now?"
        bill "Right, I've got a bit of a confession to make."
        s3_mc "You don't know how to make tea?"
        bill "I'm not that bad! Just, I'm more of a coffee drinker."
        "[he_she!c] pops a teabag in the mug, adds a teaspoon of sugar and gives the cup a stir."
        "After a few moments [he_she] removes the teabag and adds milk."
    elif s3_mc.current_partner == "Camilo":
        camilo "Is that right now?"
        "Camilo grabs the milk and pours a splash into a mug. He adds a teabag and tops it up with hot water."
    elif s3_mc.current_partner == "Harry":
        harry "Is that right now?"
        "Harry pops in a spoon of sugar and a teabag, and fills the mug up halfway with hot water."
        "He then tops it up with milk and takes out the teabag."
        "He takes a sip of the milky drink."
    elif s3_mc.current_partner == "AJ":
        aj "Is that right now?"
        aj "Right, I've got a bit of a confession to make."
        s3_mc "You don't know how to make tea?"
        aj "I'm not that bad! Just, I'm more of a coffee drinker."
        "[he_she!c] pops a teabag in the mug, adds a teaspoon of sugar and gives the cup a stir."
        "After a few moments [he_she] removes the teabag and adds milk."

    # CHOICE
    menu:
        s3_mc "The way you make a cup of tea is..."
        "Poetry in motion":
            $ s3_mc.like(s3_mc.current_partner)
            if s3_mc.current_partner == "Bill":
                bill "It's not rocket science, just a teabag in a mug."
                s3_mc "I'll have mine just the same."
                bill "Coming right up."
            elif s3_mc.current_partner == "Camilo":
                camilo "It's not rocket science, just a teabag in a mug."
                s3_mc "I'll have mine just the same."
                camilo "Coming right up."
            elif s3_mc.current_partner == "Harry":
                harry "It's not rocket science, just a teabag in a mug."
                s3_mc "I'll have mine just the same."
                harry "Coming right up."
            elif s3_mc.current_partner == "AJ":
                aj "It's not rocket science, just a teabag in a mug."
                s3_mc "I'll have mine just the same."
                aj "Coming right up."
            "[s3_mc.current_partner] makes you the tea with a silly smile plastered on [his_her] face."
        "A crime against humani-tea":
            $ s3_mc.dislike(s3_mc.current_partner)
            if s3_mc.current_partner == "Bill":
                bill "What's wrong with how I make it?"
                s3_mc "Two teabags? Four sugars!"
                s3_mc "Let's just say you should stick to coffee, babe."
            elif s3_mc.current_partner == "Camilo":
                camilo "What's wrong with how I make it?"
                s3_mc "Milk first? Ugh."
            elif s3_mc.current_partner == "Harry":
                harry "What's wrong with how I make it?"
                s3_mc "The tea bag was only in the mug for two seconds!"
            elif s3_mc.current_partner == "AJ":
                aj "What's wrong with how I make it?"
                s3_mc "Two teabags? Four sugars!"
                s3_mc "Let's just say you should stick to coffee, babe."    
            s3_mc "I'll make my own."
        "Not very entertaining...":
            if s3_mc.current_partner == "Bill":
                bill "When is watching someone making tea entertaining?"
                s3_mc "Sometimes there's a bit of showmanship."
                bill "Like what? Fireworks and a striptease?"
                s3_mc "That would have been entertaining."
                bill "What are you like."
            elif s3_mc.current_partner == "Camilo":
                camilo "When is watching someone making tea entertaining?"
                s3_mc "Sometimes there's a bit of showmanship."
                camilo "Like what? Fireworks and a striptease?"
                s3_mc "That would have been entertaining."
                camilo "What are you like."
            elif s3_mc.current_partner == "Harry":
                harry "When is watching someone making tea entertaining?"
                s3_mc "Sometimes there's a bit of showmanship."
                harry "Like what? Fireworks and a striptease?"
                s3_mc "That would have been entertaining."
                harry "What are you like."
            elif s3_mc.current_partner == "AJ":
                aj "When is watching someone making tea entertaining?"
                s3_mc "Sometimes there's a bit of showmanship."
                aj "Like what? Fireworks and a striptease?"
                s3_mc "That would have been entertaining."
                aj "What are you like."

            "[s3_mc.current_partner] slides you your tea."

    "You both sip your cuppa."
    "[s3_mc.current_partner] glances at you over the rim of [his_her] mug. You see a smile touch the corner of [his_her] lips."

    if s3_mc.current_partner == "Bill":
        bill "I could get used to starting my day like this."
        bill "Sexy girl in front of me, sipping a steamy beverage..."
    elif s3_mc.current_partner == "Camilo":
        camilo "I could get used to starting my day like this."
        camilo "Sexy girl in front of me, sipping a steamy beverage..."
    elif s3_mc.current_partner == "Harry":
        harry "I could get used to starting my day like this."
        harry "Sexy girl in front of me, sipping a steamy beverage..."
    elif s3_mc.current_partner == "AJ":
        aj "I could get used to starting my day like this."
        aj "Sexy girl in front of me, sipping a steamy beverage..."

    # CHOICE
    menu:
        thought "[s3_mc.current_partner] is flirting with me. I should..."
        "Get a cheeky snog in":
            "You step towards [s3_mc.current_partner] and go in for a kiss."
            "[his_her!c] hands tighten around your waist. The faint taste of tea remains on [his_her] lips."
            if s3_mc.current_partner == "Bill":
                bill "Yeah, I could definitely do this every morning."
            elif s3_mc.current_partner == "Camilo":
                camilo "Yeah, I could definitely do this every morning."
            elif s3_mc.current_partner == "Harry":
                harry "Yeah, I could definitely do this every morning."
            elif s3_mc.current_partner == "AJ":
                aj "Yeah, I could definitely do this every morning."
        "Play it cool":
            "You take a sip of your tea and smile coyly."
            s3_mc "We'll see how it goes."
        "Flirt back":
            s3_mc "This is great, but I can think of at least one thing that could top it."
            "You run your fingers up [s3_mc.current_partner]'s arm and [he_she] bites [his_her] bottom lip."
            if s3_mc.current_partner == "Bill":
                bill "Maybe we can start today again..."
            elif s3_mc.current_partner == "Camilo":
                camilo "Maybe we can start today again..."
            elif s3_mc.current_partner == "Harry":
                harry "Maybe we can start today again..."
            elif s3_mc.current_partner == "AJ":
                aj "Maybe we can start today again..."

    if s3_mc.bff == "Elladine":
        elladine "Hey..."
        elladine "You two weren't cracking on in the kitchen, were you?"
    elif s3_mc.bff == "Genevieve":
        genevieve "Hey..."
        genevieve "You two weren't cracking on in the kitchen, were you?"
    elif s3_mc.bff == "Nicky":
        nicky "Hey..."
        nicky "You two weren't cracking on in the kitchen, were you?"
    elif s3_mc.bff == "Seb":
        seb "Hey..."
        seb "You two weren't cracking on in the kitchen, were you?"

    "[s3_mc.current_partner] scratches the back of [his_her] neck and you carry on drinking your tea."
    s3_mc "Just enjoying some time alone."

    if s3_mc.current_partner == "Bill":
        bill "Having a chat."
    elif s3_mc.current_partner == "Camilo":
        camilo "Having a chat."
    elif s3_mc.current_partner == "Harry":
        harry "Having a chat."
    elif s3_mc.current_partner == "AJ":
        aj "Having a chat."

    if s3_mc.bff == "Elladine":
        elladine "Well, we're over by the loungers for when you two are done doing whatever it is you're doing."
    elif s3_mc.bff == "Genevieve":
        genevieve "Well, we're over by the loungers for when you two are done doing whatever it is you're doing."
    elif s3_mc.bff == "Nicky":
        nicky "Well, we're over by the loungers for when you two are done doing whatever it is you're doing."
    elif s3_mc.bff == "Seb":
        seb "Well, we're over by the loungers for when you two are done doing whatever it is you're doing."

    "[s3_mc.bff] gives you a wink, grabs some fruit and heads out."

    if s3_mc.bff == "Elladine":
        show elladine at npc_exit
    elif s3_mc.bff == "Genevieve":
        show genevieve at npc_exit
    elif s3_mc.bff == "Nicky":
        show nicky at npc_exit
    elif s3_mc.bff == "Seb":
        show seb at npc_exit

    pause .3
    $ renpy.hide(s3_mc.bff.lower())
    $ on_screen.remove(s3_mc.bff.lower())

    s3_mc "Well, it was nice while it lasted."
    "[s3_mc.current_partner] smiles at you warmly. You both make your way to the loungers."

    scene s3-sun-loungers-day with dissolve
    $ on_screen = []

    "You, [s3_mc.current_partner] and the other Islanders are lounging by the pool. Your empty mug sits by your side. Laughter fills the air."

    "Bill's setting the world to rights and he's starting with vegetables."
    bill "And that's why you're better off using a cucumber."
    harry "Mate, I want to agree with you, but it just sounds disgusting."
    camilo "It's a risotto! Who puts cucumber in it?"
    "Well, I'm glad someone cleared that up for me..."
    iona "I don't know, they kinda do look exactly the same."
    bill "Exactly! Only a courgette is fanicer. A cucumber works just as well."
    camilo "Name of Bill's sex tape."
    "The girls giggle and Bill just rolls his eyes."
    iona "If you were going to make a sex tape what would you actually call it?"
    nicky "Easy. True Grit."
    "The Islanders groan and Elladine pulls a face of disgust."
    iona "How is that sexy?"
    nicky "It's not, I just think it's a great movie. Wait, you meant sex tape?"
    elladine "Mine would be something sensual..."
    "She thinks for a moment, then says something in Welsh."
    miki "That's a bit of a mouthful, isn't it?"
    genevieve "Name of Miki's sex tape!"
    "Camilo and Genevieve high five. Miki shakes her head, laughing."
    miki "What about you, [s3_name]? What would you name your naughty video?"
    "The Islanders turn to you."

    # CHOICE
    menu:
        s3_mc "Hmm, my sex tape would be called..."
        "Inspect Her Gadget":
            if s3_mc.current_partner == "Bill":
                bill "You don't have to ask me twice..."
            elif s3_mc.current_partner == "Camilo":
                camilo "You don't have to ask me twice..."
            elif s3_mc.current_partner == "Harry":
                harry "You don't have to ask me twice..."
            elif s3_mc.current_partner == "AJ":
                aj "You don't have to ask me twice..."
            elladine "[s3_name], you're so dirty!"
        "Missionary Impossible":
            camilo "Did you just came up with that?"
            s3_mc "What can I say, I'm a natural."
        "Sin-derella":
            bill "If the shoe fits..."
            s3_mc "Very funny."
        "I wouldn't make one!":
            seb "That's a crap name for a... Oh, I see what you did there."
            if s3_mc.current_partner == "Bill":
                bill "I get it, it's not for everybody."
            elif s3_mc.current_partner == "Camilo":
                camilo "I get it, it's not for everybody."
            elif s3_mc.current_partner == "Harry":
                harry "I get it, it's not for everybody."
            elif s3_mc.current_partner == "AJ":
                aj "I get it, it's not for everybody."
            s3_mc "No judgement guys, just not my thing."
            "[s3_mc.current_partner] smiles and squeezes your hand."

    bill "Fast and Furious would be a good one too. You wouldn't even need to change the name."
    harry "I've actually driven one of those cars."
    iona "From the film? For real? That's so cool."
    harry "Yeah, normally you need special training, but I know my way around a car."
    bill "Yeah, all the way round to the passenger side."
    "The Islanders all laugh, except for Harry who sits up."
    harry "I do, actually. They said I was a natural."
    bill "Yeah, course. Next thing he'll be saying is he was Arnie's stunt double in Expendables 2."
    bill "What did you do after? Go on a date with Zendaya? Regular James Bond this one."
    "The Islanders laugh playfully."
    "Harry frowns, and his jaw tightens. It's clear the vibe has changed."
    thought "Harry doesn't look like he's finding this funny."
    thought "I should decide if I want to be around this conversation."

    # CHOICE
    menu:
        thought "Shall I get involved?"
        "I'll say something":
            $ s3e4p1_harry_incident = True
            # SUB-CHOICE
            menu: 
                thought "Hmm, what shall I say?"
                "Tell Bill to stop":
                    s3_mc "Give it a rest, Bill."
                    bill "What? He was the one who brought it up."
                "Ask if Harry's OK":
                    "You catch Harry's eye and mouth 'Are you OK'?"
                    "He forces a smile and nods."
                    thought "Bill's still talking..."
                "Change the subject":
                    s3_mc "You know what's a good film? Any film with Ryan Gosling."
                    iona "I would. He is so fit."
                    bill "Yeah, Drive was awesome. Did you have a go on that car too, Harry?"

            "Harry folds his arms and lies back down."
            bill "Sorry, mate, I was just playing around. Tell us about the car then."
            "Harry inhales deeply, still frowning."
            harry "No thanks."
            seb "C'mon mate, what was it like? Fast or furious?"
            "Harry shakes his head stubbornly."
            bill "Mate, there's no need to be weird about it, it was just a..."
            "Harry jumps up."
            bill "What are you doing, mate?"
            harry "Everyone needs to stop talking to me."
            "Harry strides towards the pool and dives in."
            s3_mc "Woah!"
            bill "My hair!"
            "You watch as Harry resurfaces. He walks back slowly, looking more relaxed, and lies down on a lounger."

            # SUB-CHOICE
            menu:
                thought "That's one way of ending a discussion..."
                "Lie back and enjoy the sun":
                    bill "I'm not trying to be funny or anything, but what just happened, mate?"
                "Ask what was that about":
                    s3_mc "Hey Harry, what just happened?"
                "Nudge Bill to say something":
                    bill "I'm not trying to be funny or anything, but what just happened, mate?"

            aj "Harry literally just jumped into the..."
            bill "We know what literally happened, AJ."
            harry "I'm sorry. I've always had a short temper. Ever since I was a kid."
            harry "You wouldn't think it, but I was always getting into fights."
            iona "I know plenty of folk who've got anger management issues."
            harry "Yeah, I guess you could call it that. I've been getting therapy for it though."
            harry "I don't lose it with anyone anymore, but sometimes the littlest thing can set me off."
            aj "And so... you jump in the pool?"

            # SUB-CHOICE
            menu:
                thought "Harry jumped into the pool because he was angry..."
                "I don't get it":
                    s3_mc "I mean, why jump in the pool?"
                "I totally get it":
                    s3_mc "It cools you off, right?"
                    harry "Something like that."
                "What happens if there's no pool?":
                    s3_mc "I mean do you just go all Hulk?"

            "Harry exhales."
            harry "It doesn't have to be a pool. Sometimes I just splash my face with water."
            harry "It's something we came up with in therapy."
            genevieve "It's a distraction thing, right?"
            harry "Yeah! Sort of."
            harry "Your body temperature goes up when you get angry, so you're literally cooling yourself down."
            "Harry smiles, then turns back to Bill."
            harry "I know you were kidding. The anger just builds up sometimes. I feel like a right doughnut."
            bill "I didn't mean to upset you, mate. I was genuinely just messing about."
            seb "You're not a doughnut. You've found your own way of coping with a really tricky emotion."
            seb "That's really cool."
            harry "Yeah, therapy helped me out. Big time."
            bill "I'm glad to hear it, mate. I'm sorry again."
            harry "I know. I'm fine now, don't worry about it."
            "Bill gets up and walks over to the pool edge."
            "He grins at Harry and then flops into the pool."
            miki "Bill! My hair! You've soaked me completely!"
            "Harry looks surprised as Bill pulls himself out of the pool and comes to sit by his side."
            harry "What did you go and do that for?"
            bill "You said you felt like a doughnut. That makes two of us now."
            bill "Two wet doughnuts."
            "Harry grins and Bill messes up his hair."

            # SUB-CHOICE
            menu:
                thought "Bill jumped in the pool to make Harry feel better..."
                "That makes no sense":
                    thought "Who even understands these boys?"
                "That was really sweet":
                    thought "He cares about his mates."
                    "Bill catches you looking at him and smiles."
                "Now they're both wet and it's kinda hot":
                    "You bite your bottom lip and stare. Bill and Harry notice."
                    harry "You alright there, [s3_name]?"
                    s3_mc "Er, yeah, fine. I might jump in the pool myself."

            "Another splash rings out. AJ and Camilo have dived into the pool."

        "I'd rather go and grab a snack":
            "You head to the kitchen and pick out a selection of fruit."
            "Bearing a huge bowl, you emerge to see the other Islanders splashing around in the pool."
            "Harry seems to have relaxed."

    aj "[s3_name]! Jump in!"
    camilo "Yeah, it's lovely. Good call Harry."

    # CHOICE
    menu:
        "Should I jump into the pool?"
        "Move out of the way, here comes the cannon ball":
            "You take a running jump towards the pool."
            "You tuck in your limbs and hit the water with an enormous splash."
        "I can't...My hair!":
            genevieve "Well, if you won't I will."
            "Genevieve whoops and jumps into the pool, splashing Miki."

    miki "You have got to be kidding me."
    "You look over and see Harry and Bill grinning."
    miki "Right, I might as well get in now. I'm already wet."
    miki "Wait! That could be the name of my sex tape!"
    camilo "Yes, Miki! You nailed it."
    harry "And that can be the name of yours, Camilo."
    "You climb out of the pool and dry off."
    thought "My shoulders are a bit stiff, I could do with a workout..."
    thought "And it would give me a chance for some good old-fashioned grafting."

    # CHOICE
    menu:
        "Who shall I invite to the gym?"
        "Bill":
            $ s3e4p1_invite_gym = "Bill"
        "Camilo":
            $ s3e4p1_invite_gym = "Camilo"
        "Harry":
            $ s3e4p1_invite_gym = "Harry"
        "AJ":
            $ s3e4p1_invite_gym = "AJ"

    $ pronouns(s3e4p1_invite_gym)

    s3_mc "Hey, [s3e4p1_invite_gym], fancy a workout?"
    "[s3e4p1_invite_gym] gives you a flirty look."

    if s3e4p1_invite_gym == "Bill":
        bill "You know it."
    elif s3e4p1_invite_gym == "Camilo":
        camilo "You know it."
    elif s3e4p1_invite_gym == "Harry":
        harry "You know it."
    elif s3e4p1_invite_gym == "AJ":
        aj "You know it."

    scene s3-gym-day with dissolve
    $ on_screen = []

    thought "Time to work up a sweat!"
    "The breeze caresses your skins as you watch [s3e4p1_invite_gym] straddle the lat pulldown machine."
    thought "I wish I was that machine right now..."

    if s3_mc.job == "Athlete":
        if s3e4p1_invite_gym == "Bill":
            bill "I don't need to explain to you how one of these works..."
        elif s3e4p1_invite_gym == "Camilo":
            camilo "I don't need to explain to you how one of these works..."
        elif s3e4p1_invite_gym == "Harry":
            harry "I don't need to explain to you how one of these works..."
        elif s3e4p1_invite_gym == "AJ":
            aj "I don't need to explain to you how one of these works..."
    else:
        if s3e4p1_invite_gym == "Bill":
            bill "I always love getting my heart going on one of these. How about you?"
        elif s3e4p1_invite_gym == "Camilo":
            camilo "I always love getting my heart going on one of these. How about you?"
        elif s3e4p1_invite_gym == "Harry":
            harry "I always love getting my heart going on one of these. How about you?"
        elif s3e4p1_invite_gym == "AJ":
            aj "I always love getting my heart going on one of these. How about you?"

    # CHOICE
    menu:
        thought "[s3e4p1_invite_gym] wants to know if I train..."
        "Of course I do":
            s3_mc "I love to break a sweat."
            if s3e4p1_invite_gym == "Bill":
                bill "Nothing hotter than someone who trains."
            elif s3e4p1_invite_gym == "Camilo":
                camilo "Nothing hotter than someone who trains."
            elif s3e4p1_invite_gym == "Harry":
                harry "Nothing hotter than someone who trains."
            elif s3e4p1_invite_gym == "AJ":
                aj "Nothing hotter than someone who trains."
        "It's not really my thing":
            if s3e4p1_invite_gym == "Bill":
                bill "Then I'll show you the ropes."
                bill "Er, not that we're doing anything with ropes today."
            elif s3e4p1_invite_gym == "Camilo":
                camilo "Then I'll show you the ropes."
                camilo "Er, not that we're doing anything with ropes today."
            elif s3e4p1_invite_gym == "Harry":
                harry "Then I'll show you the ropes."
                harry "Er, not that we're doing anything with ropes today."
            elif s3e4p1_invite_gym == "AJ":
                aj "Then I'll show you the ropes."
                aj "Er, not that we're doing anything with ropes today."

    if s3e4p1_invite_gym == "Bill":
        bill "I'll get a firm grip on these handles..."
    elif s3e4p1_invite_gym == "Camilo":
        camilo "I'll get a firm grip on these handles..."
    elif s3e4p1_invite_gym == "Harry":
        harry "I'll get a firm grip on these handles..."
    elif s3e4p1_invite_gym == "AJ":
        aj "I'll get a firm grip on these handles..."

    thought "Hmm, that looks pretty heavy..."
    "[he_she!c] pulls down towards [his_her] chest."
    s3_mc "Are you sure that's not too much weight?"

    if s3e4p1_invite_gym == "Bill":
        bill "Hey, don't you worry about me."
    elif s3e4p1_invite_gym == "Camilo":
        camilo "Hey, don't you worry about me."
    elif s3e4p1_invite_gym == "Harry":
        harry "Hey, don't you worry about me."
    elif s3e4p1_invite_gym == "AJ":
        aj "Hey, don't you worry about me."

    "[s3e4p1_invite_gym] pulls and there is little movement. [he_she!c] tries again."
    s3_mc "Are you showing off for me?"

    if s3e4p1_invite_gym == "Bill":
        bill "Maybe a bit..."
        bill "I can do it!"
    elif s3e4p1_invite_gym == "Camilo":
        camilo "Maybe a bit..."
        camilo "I can do it!"
    elif s3e4p1_invite_gym == "Harry":
        harry "Maybe a bit..."
        harry "I can do it!"
    elif s3e4p1_invite_gym == "AJ":
        aj "Maybe a bit..."
        aj "I can do it!"

    "[s3e4p1_invite_gym] tries again to no avail. [he_she!c] stops and has a look at the weight."

    if s3e4p1_invite_gym == "Bill":
        bill "Who was last on this? The Rock?"
    elif s3e4p1_invite_gym == "Camilo":
        camilo "Who was last on this? The Rock?"
    elif s3e4p1_invite_gym == "Harry":
        harry "Who was last on this? The Rock?"
    elif s3e4p1_invite_gym == "AJ":
        aj "Who was last on this? The Rock?"

    if s3_mc.job == "Athlete":
        s3_mc "Me!"
        if s3e4p1_invite_gym == "Bill":
            bill "Woah... you're something else."
        elif s3e4p1_invite_gym == "Camilo":
            camilo "Woah... you're something else."
        elif s3e4p1_invite_gym == "Harry":
            harry "Woah... you're something else."
        elif s3e4p1_invite_gym == "AJ":
            aj "Woah... you're something else."
    else:
        s3_mc "I think it was Iona..."
        if s3e4p1_invite_gym == "Bill":
            bill "Woah. Does she put the pylons up by hand?"
        elif s3e4p1_invite_gym == "Camilo":
            camilo "Woah. Does she put the pylons up by hand?"
        elif s3e4p1_invite_gym == "Harry":
            harry "Woah. Does she put the pylons up by hand?"
        elif s3e4p1_invite_gym == "AJ":
            aj "Woah. Does she put the pylons up by hand?"

    "[s3e4p1_invite_gym] rubs [his_her] shoulder."
    s3_mc "Is your shoulder sore?"

    if s3e4p1_invite_gym == "Bill":
        bill "A little bit."
    elif s3e4p1_invite_gym == "Camilo":
        camilo "A little bit."
    elif s3e4p1_invite_gym == "Harry":
        harry "A little bit."
    elif s3e4p1_invite_gym == "AJ":
        aj "A little bit."

    thought "Poor [s3e4p1_invite_gym]..."
    thought "What if I give [him_her] a proper massage?"

    if s3e3p2_masseur == s3e4p1_invite_gym:
        thought "[he_she!c] gave me an amazing massage yesterday... "
        thought "It would be cute to return the favour."
        thought "Who knows, this time I might be able to get [him_her] to make some noise..."

    thought "They say touch brings you closer..."
    thought "And we could do with some of that."

    # CHOICE
    menu:
        thought "I should..."
        "Offer to give [s3e4p1_invite_gym] a massage":
            $ s3e4p1_massage = True
            $ s3_mc.like(s3e4p1_invite_massage)
            call s3e4p1_massage
        "Take [him_her] to Viv to be checked out":
            s3_mc "If you're sore, Viv should take a look at you."
            if s3e4p1_invite_gym == "Bill":
                bill "Good idea. I don't want to get achey."
            elif s3e4p1_invite_gym == "Camilo":
                camilo "Good idea. I don't want to get achey."
            elif s3e4p1_invite_gym == "Harry":
                harry "Good idea. I don't want to get achey."
            elif s3e4p1_invite_gym == "AJ":
                aj "Good idea. I don't want to get achey."
            "You both stand up and head towards the pool."

    scene sand with dissolve
    $ on_screen = []

    if s3e4p1_massage:
        "Is it hot in here or is it just me?"
        "It's only going to get hotter on the next episode of Love Island..."
    else:
        "Oh [s3_name], [s3e4p1_invite_gym] thought [his_her] luck was in..."
        "Don't worry [s3e4p1_invite_gym]. Things sound like they'll be heating up in the challenge..."
    
    if s3_mc.current_partner == "Bill":
        bill "My rod's so stiff..."
    elif s3_mc.current_partner == "Camilo":
        camilo "My rod's so stiff..."
    elif s3_mc.current_partner == "Harry":
        harry "My rod's so stiff..."
    elif s3_mc.current_partner == "AJ":
        aj "I just can't find the hole!"

    "Sounds like it's going to be a right carry on..."

    jump s3e4p2

label s3e4p1_massage:
    s3_mc "You're really tense. Do you want a massage?"

    if s3e4p1_invite_gym == "Bill":
        bill "You are a mind reader."
    elif s3e4p1_invite_gym == "Camilo":
        camilo "You are a mind reader."
    elif s3e4p1_invite_gym == "Harry":
        harry "You are a mind reader."
    elif s3e4p1_invite_gym == "AJ":
        aj "You are a mind reader."

    "You rub your hands over [s3e4p1_invite_gym]'s shoulders."
    "[he_she!c] lets out a sigh of pleasure."
    aj "Wow, that feels great. Have you done this before?"

    # CHOICE
    menu:
        thought "[s3e4p1_invite_gym] wants to know if I've done this before..."
        "I do it all the time":
            pass
        "Not very often":
            pass
        "I've got the magic touch":
            pass

    aj "Mmm, well, it feels amazing."
    "[he_she!c] stretches luxuriously, looking like a very happy cat."
    "Then [he_she] sighs."

    if s3e4p1_invite_gym == "Bill" and s3e4p1_harry_incident:
        bill "I feel bad about what happened with Harry."
        bill "I was just having a laugh. I didn't know he'd take it so personal."

        # CHOICE
        menu:
            thought "Bill feels bad about what happened with Harry..."
            "Be supportive":
                s3_mc "Hey, you didn't know."
                s3_mc "What matters is you listened, and you took the time to understand."
                bill "You're right."
            "Be critical":
                s3_mc "Just don't do it again."
                bill "He's a top lad. I was just having a laugh."
                bill "Trust me, I won't tease him again. Not now I know."
            "Focus on the massage":
                "You let your hands do the talking. Bill gives a happier sigh."

    if s3e4p1_invite_gym == "Harry" and s3e4p1_harry_incident:
        harry "Sorry about earlier. I'm a bit embarrassed if I'm honest."
        harry "I'm not very good at talking about my feelings."
        "You feel his shoulders tense."
        harry "Just I get so frustrated, and I bottle it all up inside and then before I know it..."
        s3_mc "You need to jump in the pool?"
        "Harry laughs."
        harry "Yeah."

        # CHOICE
        menu:
            thought "Harry's feeling a bit bad about what happened earlier. I'll..."
            "Make him smile":
                s3_mc "You wanna know what I want to know?"
                s3_mc "How is a cucumber anything like a courgette?"
                "Harry wipes his eyes and laughs, properly this time."
            "Reassure him":
                s3_mc "Hey, you're among friends. We understand. Don't overthink this."
                "Harry wipes his eyes and takes a deep breath before turning to face you."
            "Focus on the massage":
                "You let your hands do the talking. Harry wipes his eyes and gives a happier sigh."

    thought "[he_she!c]'s obviously enjoying this a lot!"
    "You carry on kneading [s3e4p1_invite_gym]'s shoulders."

    # CHOICE
    menu:
        thought "I should..."
        "Move into a head massage":
            "You slide your hands up [his_her] neck and as [he_she] moans with pleasure, you work your fingers into [his_her] hair."
        "Slide my hands down to [his_her] lower back":
            "Goosebumpbs appear on [his_her] shoulders as you work your way down [his_her] back."
            "[he_she!c] moans with delight as you work your fingertips into [his_her] hips."
        "Stick to the shoulder":
            "You keep kneading [his_her] shoulders. Your fingers work their way down [his_her] strong arms."
            "You feel [his_her] skin break out in goosebumps as [he_she] exhales deeply."

    s3_mc "Does that feel good?"

    if s3e4p1_invite_gym == "Bill":
        bill "So good."
    elif s3e4p1_invite_gym == "Camilo":
        camilo "So good."
    elif s3e4p1_invite_gym == "Harry":
        harry "So good."
    elif s3e4p1_invite_gym == "AJ":
        aj "So good."

    "[s3e4p1_invite_gym] turns around, a mischievous look in [his_her] eyes."

    if s3e4p1_invite_gym == "Bill":
        bill "If this was some master plan to get me right where you want me, mm..."
        bill "Well done."
        s3_mc "Oh really?"
        bill "You can run your hands all over me, if you want."
    elif s3e4p1_invite_gym == "Camilo":
        camilo "If this was some master plan to get me right where you want me, mm..."
        camilo "Well done."
        s3_mc "Oh really?"
        camilo "You can run your hands all over me, if you want."
    elif s3e4p1_invite_gym == "Harry":
        harry "If this was some master plan to get me right where you want me, mm..."
        harry "Well done."
        s3_mc "Oh really?"
        harry "You can run your hands all over me, if you want."
    elif s3e4p1_invite_gym == "AJ":
        aj "If this was some master plan to get me right where you want me, mm..."
        aj "Well done."
        s3_mc "Oh really?"
        aj "You can run your hands all over me, if you want."

    "You sit close behind [him_her]."

    # CHOICE
    menu:
        "[s3e4p1_invite_gym] says I can do whatever I like..."
        "Stroke [his_her] stomach":
            "You slowly slide your finger tips around [his_her] waist."
            "[his_her!c] skin is warm. You gently drag your nails over [his_her] tight abs."
            "[he_she!c] trembles at your touch."
        "Run my hands over [his_her] legs":
            "You slide your hands along [his_her] muscular thighs, letting your nails drag gently over [his_her] warm skin."
            "[he_she!c] murmurs with pleasure."
        "Kiss [his_her] neck":
            "You lean in close and your lips gently brush [his_her] neck."
            "[he_she!c] murmurs with pleasure as you slowly kiss [his_her] warm skin."

    s3_mc "Feeling better?"
    "[s3e4p1_invite_gym] bites his bottom lip and looks at you hungrily. "

    if s3e4p1_invite_gym == "Bill":
        bill "Like a brand new man."
    elif s3e4p1_invite_gym == "Camilo":
        camilo "Like a brand new man."
    elif s3e4p1_invite_gym == "Harry":
        harry "Like a brand new man."
    elif s3e4p1_invite_gym == "AJ":
        aj "Like a brand new woman."

    "[he_she] leans closer until the tips of your noses touch. [his_her] hands rest firmly on your hips."

    if s3e4p1_invite_gym == "Bill":
        bill "Have I told you how fit you are?"
    elif s3e4p1_invite_gym == "Camilo":
        camilo "Have I told you how fit you are?"
    elif s3e4p1_invite_gym == "Harry":
        harry "Have I told you how fit you are?"
    elif s3e4p1_invite_gym == "AJ":
        aj "Have I told you how fit you are?"
        
    s3_mc "Tell me again..."
    "[he_she] grimaces suddenly."
    s3_mc "You alright?"

    if s3e4p1_invite_gym == "Bill":
        bill "My shoulder's still aching..."
    elif s3e4p1_invite_gym == "Camilo":
        camilo "My shoulder's still aching..."
    elif s3e4p1_invite_gym == "Harry":
        harry "My shoulder's still aching..."
    elif s3e4p1_invite_gym == "AJ":
        aj "My shoulder's still aching..."

    s3_mc "OK, I insist we go and find Genevieve."
    "[s3e4p1_invite_gym] groans."

    if s3e4p1_invite_gym == "Bill":
        bill "OK..."
    elif s3e4p1_invite_gym == "Camilo":
        camilo "OK..."
    elif s3e4p1_invite_gym == "Harry":
        harry "OK..."
    elif s3e4p1_invite_gym == "AJ":
        aj "OK..."

    "You stand up to go. [s3e4p1_invite_gym] coils an arm around your waist and you head over to the pool."


#########################################################################
## Episode 4, Part 2
#########################################################################
label e3e4p2:
    scene sand with dissolve
    $ on_screen = []

    show screen day_title(4, 2) with Pause(4)
    hide screen day_title with dissolve

    "Welcome back to Love Land! The best theme park in this hemisphere."
    "Our feature attraction is [s3_mc.current_partner], The Ride."
    "Which [s3_name] is having a lot of fun on right now."
    "Did I just do that whole bit for the sake of a pun? You're damn right I did."
    "Previously on Love Island..."
    "Things got a little heated when Bill did a Bill..."
    harry "Normally you need a special training, but I know my way around a car."
    bill "Yeah, all the way round to the passenger side."

    show harry at npc_exit
    show bill at npc_exit
    pause .3
    $ renpy.hide("harry")
    $ renpy.hide("bill")
    $ on_screen = []

    "And did we have a special guest in the Villa?"

    if s3e4p1_invite_gym == "Bill":
        bill "Who was last on this machine? The Rock?"
        show bill at npc_exit
        pause .3
        $ renpy.hide("bill")
        $ on_screen.remove("bill")
    elif s3e4p1_invite_gym == "Camilo":
        camilo "Who was last on this machine? The Rock?"
        show camilo at npc_exit
        pause .3
        $ renpy.hide("camilo")
        $ on_screen.remove("camilo")
    elif s3e4p1_invite_gym == "Harry":
        harry "Who was last on this machine? The Rock?"
        show harry at npc_exit
        pause .3
        $ renpy.hide("harry")
        $ on_screen.remove("harry")
    elif s3e4p1_invite_gym == "AJ":
        aj "Who was last on this machine? The Rock?"
        show aj at npc_exit
        pause .3
        $ renpy.hide("aj")
        $ on_screen.remove("aj")

    "Sadly not. But I do have a pet rock to keep me company during the long, dark nights here."
    "I call him 'Rocky' in honour of Bill's favourite film franchise."
    "Coming up!"
    "Iona shouts about her job a lot."

    iona "I rig pylons!"
    show iona at npc_exit
    pause .3
    $ renpy.hide("iona")
    $ on_screen.remove("iona")

    "And innuendos are abound as our Islanders all pitch in for today's in-tents challenge."

    if s3_mc.current_partner == "Bill":
        bill "My rod's so stiff..."
        show bill at npc_exit
        pause .3
        $ renpy.hide("bill")
    elif s3_mc.current_partner == "Camilo":
        camilo "My rod's so stiff..."
        show camilo at npc_exit
        pause .3
        $ renpy.hide("camilo")
    elif s3_mc.current_partner == "Harry":
        harry "My rod's so stiff..."
        show harry at npc_exit
        pause .3
        $ renpy.hide("harry")
    elif s3_mc.current_partner == "AJ":
        aj "I just can't find the hole!"
        show aj at npc_exit
        pause .3
        $ renpy.hide("aj")

    "Strap yourselves in! This is one rollercoaster you don't want to miss."
    "Sun's out, birds are singing, and our Islanders..."
    "...are in the lounge."
    "I don't know why we even flew them out here. Next time we'll send them to Skegness."

    scene s3-lounge with dissolve
    $ on_screen = []

    "You lie sprawled across a sofa, your head resting on [s3_mc.current_partner]'s lap."
    "Iona fans herself with a palm leaf."
    miki "It's nice to get out of the heat for a while."
    camilo "Yeah, bruv. It's an oven out there..."
    iona "It's an oven in here!"

    if s3_mc.current_partner == "Bill":
        bill "Nah, that's just [s3_name].I mean, have you seen how hot she is?"
        s3_mc "[s3_mc.current_partner]!"
        bill "Don't even try and deny it."
    elif s3_mc.current_partner == "Camilo":
        camilo "Nah, that's just [s3_name].I mean, have you seen how hot she is?"
        s3_mc "[s3_mc.current_partner]!"
        camilo "Don't even try and deny it."
    elif s3_mc.current_partner == "Harry":
        harry "Nah, that's just [s3_name].I mean, have you seen how hot she is?"
        s3_mc "[s3_mc.current_partner]!"
        harry "Don't even try and deny it."
    elif s3_mc.current_partner == "AJ":
        aj "Nah, that's just [s3_name].I mean, have you seen how hot she is?"
        s3_mc "[s3_mc.current_partner]!"
        aj "Don't even try and deny it."
    
    iona "Pack it in, you two. I don't think I can take any more."

    # Can add back dialog option once MC images are in game
    # aj "Nah, that's just [s3_name]. I mean, have you seen her outfit today?"
    # s3_mc "You already said that earlier, babe."
    # aj "And?"

    harry "This is nothing. One time, my flat's boiler went on the blink and set itself to forty degrees!"
    harry "My ice lolly melted all over my head..."

    # CHOICE
    menu:
        s3_mc "You think this is hot? I once..."
        "Got stranded in Death Valley":
            s3_mc "Our car broke down in the middle of it. We were stuck there for half a day!"
            bill "Why were you even out there?"
            s3_mc "To sightsee! But like, there's nothing there. Just heat."
            nicky "It's meant to be pretty, tough, right?"
            s3_mc "Sure, if you like beige..."
            bill "That's a solid colour, to be fair."
        "Sat next to Tessa Thompson":
            "AJ lets out a squeal."
            aj "What?"
            aj "I would have been a mess!"
            nicky "She's proper cute, man."
            s3_mc "Even cuter in person."
            aj "I would give anything to just, like, touch her face."
            aj "Not for long or anything. Just like..."
            aj "...boop."
        "Was in a lift with Jason Momoa":
            "Iona's breath catches in her throat."
            iona "Shut up! No way!"
            s3_mc "Yeah way. He's... impressive."
            iona "That's an understatement."
            iona "Ugh, I'd let him blast me with his trident any day."
            genevieve "Oh my gosh, Iona."
        "Looked in a mirror":
            if s3_mc.current_partner == "Bill":
                bill "You're not wrong!"
            elif s3_mc.current_partner == "Camilo":
                camilo "You're not wrong!"
            elif s3_mc.current_partner == "Harry":
                harry "You're not wrong!"
            elif s3_mc.current_partner == "AJ":
                aj "You're not wrong!"
            iona "I love the confidence you have, babe."

    "The others laugh."
    nicky "Tell you what, this one time during a heatwave, an ex's cat hid this box of prawns we'd just bought."
    nicky "The next day we were tearing the place apart looking for what was causing the smell!"
    nicky "She even put my shoes outside."

    # CHOICE
    menu:
        thought "Are we seriously talking about your ex's prawns...?"
        "Can we change the subject?":
            # NEED TO FILL
            "EMPTY"
        "I mean, it's funny, keep going":
            $ s3_mc.like("Nicky")
            s3_mc "It's just weird is all..."
            nicky "Right so, we've looked everywhere. Changed the litter box. Bleached all the drains and all this."
            nicky "And it still honks."
            nicky "We're knackered by now, so we crash down onto the sofa..."
            nicky "... and a prawn slides out from under a cushion."
            s3_mc "What?"
            nicky "The little bugger had hid the box under our sofa cushion."
        "Tell me more about this cat...":
            nicky "He was a proper terror."
            nicky "Adorable. But, like, a demon."
            nicky "This fluffy white thing whose favourite game was jumping on my head from a height..."
            nicky "Turns out he'd hidden the prawns under the sofa cushions."

    nicky "It took two boil washes to stop the fabric smelling like Billingsgate fish market..."
    seb "That's cats for you, man."
    "There's something fishy about that story."
    "But we won't get to the bottom of it now. It's challenge time!"
    miki "Oh, I got a text."
    text "Islanders, please make your way to the lawn for today's challenge. #someassemblyrequired #mightyerections"
    genevieve "I wonder what it is?"
    "Camilo looks out of the window."
    camilo "What're all those bundles on the lawn?"

    scene s3-lawn-day with dissolve
    $ on_screen = []

    "In today's challenge, our girls have to help the lads pitch a tent."
    "No, not like that..."
    "An actual tent."
    "You lot are filthy."
    "All across the lawn are bundles of nylon, tent pegs, and collapsed metal poles."
    s3_mc "I've got a text."
    text "Islanders, it's time to find out how good you are with your hands in today's pitch a tent challenge. The couple with the best tent, as voted by the others, get to decide what everyone eats tonight. #tentlife #grabapole #canvastheneighbourhood"
    harry "Aw, man. I've never put up a proper tent. Even when I got to Glasto, I just use a pop up..."
    seb "Pop ups all the way, man. Tents are a faff."
    genevieve "We always get medical crew tents at festivals. I've never put one up before..."
    iona "Pfft. I rig pylons for a living, which are basically just big tents."
    elladine "They are?"
    iona "Well, no, but they're mostly wires and poles and stuff. This'll be a cinch."
    camilo "This is gonna be a huge pain."
    bill "Just follow the instructions, mate. It's simple."
    aj "Yeah! I used to put tents up in the Brownies all the time. It's really not that hard."

    # CHOICE
    menu:
        thought "Can I put up a tent?"
        "We've got this!":
            if s3_mc.current_partner == "Bill":
                bill "You know it, babe!"
            elif s3_mc.current_partner == "Camilo":
                camilo "I hope that means you're good at this..."
            elif s3_mc.current_partner == "Harry":
                harry "I hope that means you're good at this..."
            elif s3_mc.current_partner == "AJ":
                aj "You know it, babe!"
        "We're doomed":
            if s3_mc.current_partner == "Bill":
                bill "Nah, I believe in you, babe. I'll be here to help, too!"
            elif s3_mc.current_partner == "Camilo":
                camilo "Don't say that! Let's at least give it a go..."
            elif s3_mc.current_partner == "Harry":
                harry "Don't say that! Let's at least give it a go..."
            elif s3_mc.current_partner == "AJ":
                aj "Nah, I believe in you, babe. I'll be here to help, too!"
        "I care more about what we do in the tent...":
            if s3_mc.current_partner == "Bill":
                bill "You and me both..."
            elif s3_mc.current_partner == "Camilo":
                camilo "You and me both..."
            elif s3_mc.current_partner == "Harry":
                harry "You and me both..."
            elif s3_mc.current_partner == "AJ":
                aj "You and me both..."

    elladine "Alright, let's quit the nattering and get on with it then!"
    miki "Woah, Elladine's got a competitive side."
    elladine "It's a task that needs completing. Nicky, grab those poles, we're going to do this right."
    nicky "No problem, babe."
    "He goes over to their bundle and picks it up."
    "Something comes undone, and the poles and small metal rings clatter to the ground."
    nicky "We may now have a problem."

    "You and [s3_mc.current_partner] look down at your unassembled tent."

    if s3_mc.current_partner == "Bill":
        bill "Right then, first things first."
        "[he_she!c] scans through the instructions."
        bill "Seems simple enough."
        bill "We need to thread these rods through the, um, tenty bits."
        s3_mc "The holes?"
        bill "Yeah, tenty bits."
    elif s3_mc.current_partner == "Camilo":
        camilo "Right so... how'd we do this?"
        s3_mc "We've got the instructions right here."
        "He looks at them."
        camilo "I don't get this at all. It's like they're written in another language..."
        s3_mc "They're pictures?"
        camilo "Confusing pictures. But, I think I see what we need to do first..."
        camilo "We need to thread these rods through the, um, tenty bits."
        s3_mc "The holes?"
        camilo "Yeah, tenty bits."
    elif s3_mc.current_partner == "Harry":
        harry "Right so... how'd we do this?"
        s3_mc "We've got the instructions right here."
        "He looks at them."
        harry "I don't get this at all. It's like they're written in another language..."
        s3_mc "They're pictures?"
        harry "Confusing pictures. But, I think I see what we need to do first..."
        harry "We need to thread these rods through the, um, tenty bits."
        s3_mc "The holes?"
        harry "Yeah, tenty bits."
    elif s3_mc.current_partner == "AJ":
        aj "Right then, first things first."
        "[he_she!c] scans through the instructions."
        aj "Seems simple enough."
        aj "We need to thread these rods through the, um, tenty bits."
        s3_mc "The holes?"
        aj "Yeah, tenty bits."

    # CHOICE
    menu:
        thought "We need to thread the poles through the tenty bits..."
        "Do as the instructions say":
            $ s3e4p2_good_tent = True
            "You pick up one of the rods and assemble it, then carefully slide it through one of the tent holes."
            if s3_mc.current_partner == "Bill":
                bill "Nice one. You've done this before."
                "[s3_mc.current_partner] does the same."
                bill "People get themselves in a right mess putting up a tent. I've never understood why. It's pretty straightforward."
            elif s3_mc.current_partner == "Camilo":
                camilo "Wow, you really seem to know what you're doing, babe."
                "He stands and watches you."
                camilo "Keep at it!"
            elif s3_mc.current_partner == "Harry":
                harry "Wow, you really seem to know what you're doing, babe."
                "He stands and watches you."
                harry "Keep at it!"
            elif s3_mc.current_partner == "AJ":
                aj "Nice one. You've done this before."
                "[s3_mc.current_partner] does the same."
                aj "People get themselves in a right mess putting up a tent. I've never understood why. It's pretty straightforward."
        "Do a sexy dance with the pole":
            "You wedge one of the poles into the ground and start to twirl around it, kicking a leg up and arching your back down."
            if s3_mc.current_partner == "Bill":
                bill "This isn't distracting or anything..."
                "As you pull yourself back up, you lean too heavily on the pole. It snaps in half."
                bill "Nice one, babe!"
            elif s3_mc.current_partner == "Camilo":
                camilo "This isn't distracting or anything..."
                "As you pull yourself back up, you lean too heavily on the pole. It snaps in half."
                camilo "Nice one, babe!"
            elif s3_mc.current_partner == "Harry":
                harry "This isn't distracting or anything..."
                "As you pull yourself back up, you lean too heavily on the pole. It snaps in half."
                harry "Nice one, babe!"
            elif s3_mc.current_partner == "AJ":
                aj "This isn't distracting or anything..."
                "As you pull yourself back up, you lean too heavily on the pole. It snaps in half."
                aj "Nice one, babe!"
            s3_mc "Whoops..."
            thought "Maybe not the best idea."
            thought "But who cares? I had fun."
            if s3_mc.current_partner == "Bill":
                bill "Alright, step aside."
            elif s3_mc.current_partner == "Camilo":
                camilo "Alright, step aside."
            elif s3_mc.current_partner == "Harry":
                harry "Alright, step aside."
            elif s3_mc.current_partner == "AJ":
                aj "Alright, step aside."
        "Cocoon yourself in the nylon":
            "You toss your rod aside and scoop up the nylon tent."
            if s3_mc.current_partner == "Bill":
                bill "What are you...?"
                "Before [s3_mc.current_partner] can say anymore, you wrap yourself in the material until only your face is poking out."
                bill "Oh."
                bill "Anyway, you've had your fun..."
                bill "Can I have the tent back?"
                bill "We need to actually put it up."
                s3_mc "But I'm a tent burrito!"
                bill "Aw, you're very cute, but come on. Unwrap yourself."
                "Pouting, you slip out of the fabric."
                bill "We're getting nowhere with this..."
            elif s3_mc.current_partner == "Camilo":
                camilo "What are you...?"
                "Before [s3_mc.current_partner] can say anymore, you wrap yourself in the material until only your face is poking out."
                camilo "Oh."
                camilo "Why doesn't everyone use tents like that?"
                camilo "Stops us having to put them up at least!"
                "He looks around at the others."
                camilo "Although..."
                camilo "We need to actually put it up."
                s3_mc "But I'm a tent burrito!"
                camilo "Aw, you're very cute, but come on. Unwrap yourself."
                "Pouting, you slip out of the fabric."
                camilo "We're getting nowhere with this..."
            elif s3_mc.current_partner == "Harry":
                harry "What are you...?"
                "Before [s3_mc.current_partner] can say anymore, you wrap yourself in the material until only your face is poking out."
                harry "Oh."
                harry "Why doesn't everyone use tents like that?"
                harry "Stops us having to put them up at least!"
                "He looks around at the others."
                harry "Although..."
                harry "We need to actually put it up."
                s3_mc "But I'm a tent burrito!"
                harry "Aw, you're very cute, but come on. Unwrap yourself."
                "Pouting, you slip out of the fabric."
                harry "We're getting nowhere with this..."
            elif s3_mc.current_partner == "AJ":
                aj "What are you...?"
                "Before [s3_mc.current_partner] can say anymore, you wrap yourself in the material until only your face is poking out."
                aj "Oh."
                aj "Anyway, you've had your fun..."
                aj "Can I have the tent back?"
                aj "We need to actually put it up."
                s3_mc "But I'm a tent burrito!"
                aj "Aw, you're very cute, but come on. Unwrap yourself."
                "Pouting, you slip out of the fabric."
                aj "We're getting nowhere with this..."

    if s3_mc.current_partner != "AJ":
        "[s3_mc.current_partner] picks up another pole, but struggles to put it together."

        if s3_mc.current_partner == "Bill":
            bill "My rod's so stiff."
        elif s3_mc.current_partner == "Camilo":
            camilo "My rod's so stiff."
        elif s3_mc.current_partner == "Harry":
            harry "My rod's so stiff."

        # CHOICE
        menu:
            thought "[s3_mc.current_partner] just said his rod is stiff..."
            "Roll your eyes":
                # NEED TO FILL
                "EMPTY - Route: Coupled with any of the available boys."
            "That better be true later":
                if s3_mc.current_partner == "Bill":
                    bill "Oh, don't you worry."
                elif s3_mc.current_partner == "Camilo":
                    camilo "Oh, don't you worry."
                elif s3_mc.current_partner == "Harry":
                    harry "Oh, don't you worry."
            "Give it a good tug":
                if s3_mc.current_partner == "Bill":
                    bill "I'm tugging as hard as I can!"
                    bill "It's not been oiled well enough."
                elif s3_mc.current_partner == "Camilo":
                    camilo "I'm tugging as hard as I can!"
                    camilo "It's not been oiled well enough."
                elif s3_mc.current_partner == "Harry":
                    harry "I'm tugging as hard as I can!"
                    harry "It's not been oiled well enough."
            "Need a hand?":
                if s3_mc.current_partner == "Bill":
                    bill "Yeah. You pull that end while I tug on this one."
                    bill "You should feel when it's about to give..."
                elif s3_mc.current_partner == "Camilo":
                    camilo "Yeah. You pull that end while I tug on this one."
                    camilo "You should feel when it's about to give..."
                elif s3_mc.current_partner == "Harry":
                    harry "Yeah. You pull that end while I tug on this one."
                    harry "You should feel when it's about to give..."

        "Eventually the pole loosens and he threads it into place."
    else:
        "AJ goes to thread the last rod through its eyelet, but keeps losing track of where it is."
        aj "I can't find the hole!"

        # CHOICE
        menu:
            thought "AJ says she can't find the hole..."
            "Roll your eyes":
                # NEED TO FILL
                "EMPTY - Route: Coupled with AJ"
            "That's what she said":
                aj "Who? Has someone else figured out how to do it?"
                "She looks round at the other Islanders."
                s3_mc "Not quite what I meant."
                aj "Oh! I see."
                aj "Good one."
            "Explore it with your fingertips":
                aj "How will that help? I've already..."
                aj "...Oh!"
                aj "Those kind of jokes always go over my head."

        "Eventually, she manages to find the eyelet and slips the rod through it."

    "You look around at the others."
    if s3e4p2_good_tent:
        if s3_mc.current_partner == "Bill" or s3_mc.current_partner == "AJ":
            "You and [s3_mc.current_partner] seem to be smashing it. The others are nowhere near finished."
            thought "We've got this in the bag."
        elif s3_mc.current_partner == "Camilo" or s3_mc.current_partner == "Harry":
            "You and [s3_mc.current_partner]'s is the most complete, with Elladine and Nicky close behind."
            thought "Ours can still be better."
    else:
        "You and [s3_mc.current_partner] are lagging behind the others, who all have their tents up and in pretty good shape."
        "Except Iona's."
        "Iona kneels on the lawn, swaddled in a mass of rope."
        if s3_mc.current_partner != "Camilo":
            camilo "Um, babe, are you OK?"
            "You look over to see Iona's hands tied together in the rope."
            iona "I don't know how this has happened. This stuff's so fiddly."
            "Camilo looks over at her and rolls his eyes, then looks back to the instructions."
            iona "Camilo, babe, as much as I want to be tied up with you, could you maybe help me out."
            camilo "Oh! Sorry. You just seemed like you had it in hand, you know?"
            iona "I do have it! Putting up tents isn't difficult. I've just gotten tangled up somehow."
        else:
            iona "Wait! I've done this the wrong way round..."
            iona "...I think?"
            iona "Or maybe it's fine? I can't tell! How are these instructions so impossible to follow?"
            iona "I rig pylons!"

    "Elladine's voice rings out across the lawn."
    elladine "Nicky, come and hold this corner while I set the pegs."
    nicky "Why?"
    elladine "I don't want the wind to take the tent away. Come quickly!"
    nicky "There's no wind, though?"
    "Just a large gust starts to lift their tent."
    elladine "Quick, hurry!"

    # CHOICE
    menu:
        thought "Next we need to hammer the pegs in..."
        "Hulk out and smash them!":
            s3_mc "[s3_name] smash!"
            "You raise the rubber mallet high in the air before bringing it crashing down onto one of the pegs."
            "It goes straight into the ground without any resistance."
            if s3_mc.current_partner == "Bill":
                bill "Woah..."
            elif s3_mc.current_partner == "Camilo":
                camilo "Woah..."
            elif s3_mc.current_partner == "Harry":
                harry "Woah..."
            elif s3_mc.current_partner == "AJ":
                aj "Woah..."
            "You continue your rampage, you start to hit the ground, or sometimes the tent, and a few pegs are bent under the force."
            if s3_mc.current_partner == "Bill":
                bill "Um, how about I do the rest?"
                s3_mc "No, I've got this!"
                "You don't have this."
                "One of the pegs gives way, and the tent sags sideways."
                s3_mc "Whoops..."
                bill "It's all good, babe. It's kind of like, art now, or something."
            elif s3_mc.current_partner == "Camilo":
                camilo "[s3_mc.current_partner] smash, too!"
                "He joins you in smashing down the pegs. Some bend, but enough seem to survive."
            elif s3_mc.current_partner == "Harry":
                harry "[s3_mc.current_partner] smash, too!"
                "He joins you in smashing down the pegs. Some bend, but enough seem to survive."
            elif s3_mc.current_partner == "AJ":
                aj "Um, how about I do the rest?"
                s3_mc "No, I've got this!"
                "You don't have this."
                "One of the pegs gives way, and the tent sags sideways."
                s3_mc "Whoops..."
                aj "It's all good, babe. It's kind of like, art now, or something."
        "Ask [s3_mc.current_partner] to do it":
            s3_mc "Ugh, babe, this is hard."
            s3_mc "Could, you, like, to the rest?"
            if s3_mc.current_partner == "Bill":
                bill "I..."
            elif s3_mc.current_partner == "Camilo":
                camilo "I..."
            elif s3_mc.current_partner == "Harry":
                harry "I..."
            elif s3_mc.current_partner == "AJ":
                aj "I..."
            s3_mc "Pleeease..."
            if s3_mc.current_partner == "Bill":
                bill "Why can't you do it? "
                s3_mc "My fingers ache."
                s3_mc "It's an actual thing."
                bill "I'll do it for now, but I'm not going to be a pushover for you all the time."
                "[he_she!c] goes around the tent and has it pegged down in no time."
            elif s3_mc.current_partner == "Camilo":
                camilo "And you can't help because...?"
                s3_mc "I just want to watch you use those big muscles of yours."
                camilo "...Fair."
                "He uses his big muscles a bit too effectively. By the time he's done, most of the tent pegs are bent."
                camilo "Oops..."
            elif s3_mc.current_partner == "Harry":
                harry "And you can't help because...?"
                s3_mc "I just want to watch you use those big muscles of yours."
                harry "...Fair."
                "He uses his big muscles a bit too effectively. By the time he's done, most of the tent pegs are bent."
                harry "Oops..."
            elif s3_mc.current_partner == "AJ":
                aj "Why can't you do it? "
                s3_mc "My fingers ache."
                s3_mc "It's an actual thing."
                aj "I'll do it for now, but I'm not going to be a pushover for you all the time."
                "[he_she!c] goes around the tent and has it pegged down in no time."
        "Say something dirty...":
            $ s3e4p2_say_dirty = True
            s3_mc "This tent won't be the only thing getting nailed if I'm lucky..."
            "[s3_mc.current_partner] looks at you confused."
            if s3_mc.current_partner == "Bill":
                bill "I don't get it?"
            elif s3_mc.current_partner == "Camilo":
                camilo "I don't get it?"
            elif s3_mc.current_partner == "Harry":
                harry "I don't get it?"
            elif s3_mc.current_partner == "AJ":
                aj "I don't get it?"
            s3_mc "Oh, don't worry..."
            s3_mc "...you will."

    scene s3-lawn-tents-day with dissolve

    # CHOICE
    menu:
        thought "Right, the pegs are in. Me and [s3_mc.current_partner] put up a tent together!"
        "Pretend to give [him_her] the keys to your first home":
            $ s3_mc.like(s3_mc.current_partner)
            $ s3e4p2_give_rock = True
            s3_mc "Hey, babe..."
            if s3_mc.current_partner == "Bill":
                bill "Yeah?"
            elif s3_mc.current_partner == "Camilo":
                camilo "Yeah?"
            elif s3_mc.current_partner == "Harry":
                harry "Yeah?"
            elif s3_mc.current_partner == "AJ":
                aj "Yeah?"
            "You pick up a small pebble and walk up to [s3_mc.current_partner]."
            s3_mc "Hold out your hand and close your eyes."
            if s3_mc.current_partner == "Bill":
                bill "OK..."
                "[he_she] does what you say. You drop the pebble into [his_her] outstretched palm."
                "[s3_mc.current_partner] frowns and opens their eyes."
                bill "What's this?"
            elif s3_mc.current_partner == "Camilo":
                camilo "OK..."
                "[he_she] does what you say. You drop the pebble into [his_her] outstretched palm."
                "[s3_mc.current_partner] frowns and opens their eyes."
                camilo "What's this?"
            elif s3_mc.current_partner == "Harry":
                harry "OK..."
                "[he_she] does what you say. You drop the pebble into [his_her] outstretched palm."
                "[s3_mc.current_partner] frowns and opens their eyes."
                harry "What's this?"
            elif s3_mc.current_partner == "AJ":
                aj "OK..."
                "[he_she] does what you say. You drop the pebble into [his_her] outstretched palm."
                "[s3_mc.current_partner] frowns and opens their eyes."
                aj "What's this?"
            s3_mc "The keys to our first home..."
            if s3_mc.current_partner == "Bill":
                "Bill looks at the tent."
                bill "Oh, man. We really fluffed it on that mortgage deal, eh?"
                "He turns to you."
                bill "Still, any place with you would be a cracking home..."
            elif s3_mc.current_partner == "Camilo":
                camilo "Woah, you're saying I'm a homeowner already?"
                camilo "It's a bit small to fit my family in as well, though..."
                s3_mc "Huh?"
                camilo "Relax, I'm just joshing you."
            elif s3_mc.current_partner == "Harry":
                harry "Though I always thought my first home would be a little bigger, you know?"
                harry "I guess it at least has a pool."
                harry "But no garage for my sports car."
            elif s3_mc.current_partner == "AJ":
                aj "But it's a tent?"
                s3_mc "It's symbolism, babe!"
                aj "Oooh!"
                aj "That's so sweet!"
        "Tell [him_her] to take his shoes off inside":
            s3_mc "Hey, babe..."
            if s3_mc.current_partner == "Bill":
                bill "Yeah?"
                s3_mc "Don't forget to remove your shoes before you go into the tent."
                "[s3_mc.current_partner] looks down at [his_her] feet."
                bill "I'm not wearing any?"
                s3_mc "Ah, but you might be later, and then you'd get dirt all over our nice tent."
                if s3e4p2_good_tent:
                    bill "I guess we did make it look pretty great..."
                else:
                    bill "Um, have you seen our tent?"
                s3_mc "It's just a pet peeve of mine, OK. I like shoes off in a house."
                bill "It's a tent, but, I guess..."
                bill "...OK."
            elif s3_mc.current_partner == "Camilo":
                camilo "Yeah?"
                s3_mc "Don't forget to remove your shoes before you go into the tent."
                "[s3_mc.current_partner] looks down at [his_her] feet."
                camilo "I'm not wearing any?"
                s3_mc "Ah, but you might be later, and then you'd get dirt all over our nice tent."
                if s3e4p2_good_tent:
                    camilo "I guess we did make it look pretty great..."
                else:
                    camilo "Um, have you seen our tent?"
                s3_mc "It's just a pet peeve of mine, OK. I like shoes off in a house."
                camilo "It's a tent, but, I guess..."
                camilo "...OK."
            elif s3_mc.current_partner == "Harry":
                harry "Yeah?"
                s3_mc "Don't forget to remove your shoes before you go into the tent."
                "[s3_mc.current_partner] looks down at [his_her] feet."
                harry "I'm not wearing any?"
                s3_mc "Ah, but you might be later, and then you'd get dirt all over our nice tent."
                if s3e4p2_good_tent:
                    harry "I guess we did make it look pretty great..."
                else:
                    harry "Um, have you seen our tent?"
                s3_mc "It's just a pet peeve of mine, OK. I like shoes off in a house."
                harry "It's a tent, but, I guess..."
                harry "...OK."
            elif s3_mc.current_partner == "AJ":
                aj "Yeah?"
                s3_mc "Don't forget to remove your shoes before you go into the tent."
                "[s3_mc.current_partner] looks down at [his_her] feet."
                aj "I'm not wearing any?"
                s3_mc "Ah, but you might be later, and then you'd get dirt all over our nice tent."
                if s3e4p2_good_tent:
                    aj "I guess we did make it look pretty great..."
                else:
                    aj "Um, have you seen our tent?"
                s3_mc "It's just a pet peeve of mine, OK. I like shoes off in a house."
                aj "It's a tent, but, I guess..."
                aj "...OK."
        "Whisper in [his_her] ear the naughty things you want to do in it":
            $ s3_mc.like(s3_mc.current_partner)
            s3_mc "Hey, babe..."
            if s3_mc.current_partner == "Bill":
                bill "Yeah?"
            elif s3_mc.current_partner == "Camilo":
                camilo "Yeah?"
            elif s3_mc.current_partner == "Harry":
                harry "Yeah?"
            elif s3_mc.current_partner == "AJ":
                aj "Yeah?"
            s3_mc "Come over here for a second..."
            "[s3_mc.current_partner] walks over. You lean close to [his_her] ear."

            # SUB-CHOICE
            menu:
                s3_mc "When we get into this tent..."
                "I'm going to nibble every inch of you":
                    if s3_mc.current_partner == "Bill":
                        "[s3_mc.current_partner]'s cheeks flush red."
                        bill "That's a lot of me..."
                        bill "Where would you even start?"
                    elif s3_mc.current_partner == "Camilo":
                        "[s3_mc.current_partner] bites [his_her] lip and grins at you."
                        camilo "Every inch, eh? Where would you start?"
                        s3_mc "Wherever you'd want me to..."
                    elif s3_mc.current_partner == "Harry":
                        "[s3_mc.current_partner]'s cheeks flush red."
                        harry "That's a lot of me..."
                        harry "Where would you even start?"
                    elif s3_mc.current_partner == "AJ":
                        "[s3_mc.current_partner] bites [his_her] lip and grins at you."
                        aj "Every inch, eh? Where would you start?"
                        s3_mc "Wherever you'd want me to..."
                "I want you to tie me up with the rope":
                    if s3_mc.current_partner == "Bill":
                        "[s3_mc.current_partner] swallows hard."
                        bill "Oh...? I mean, we have some rope going spare."
                        bill "I just better remember some decent knots."
                    elif s3_mc.current_partner == "Camilo":
                        "A sly grin spreads across [s3_mc.current_partner]'s face."
                        camilo "Oh yeah? I think we have some rope going spare..."
                        camilo "I just better remember some decent knots."
                    elif s3_mc.current_partner == "Harry":
                        "[s3_mc.current_partner] swallows hard."
                        harry "Oh...? I mean, we have some rope going spare."
                        harry "I just better remember some decent knots."
                    elif s3_mc.current_partner == "AJ":
                        "A sly grin spreads across [s3_mc.current_partner]'s face."
                        aj "Oh yeah? I think we have some rope going spare..."
                        aj "I just better remember some decent knots."
                "We're going to get down to some serious canoodling...":
                    if s3_mc.current_partner == "Bill":
                        bill "Canoodling? What does that mean?"
                        bill "I mean, I'm not saying no or anything..."
                        s3_mc "Like, kissing and stuff."
                        bill "Oh, OK!"
                    elif s3_mc.current_partner == "Camilo":
                        # NEED TO FILL
                        "EMPTY - Route: Coupled up with Camilo or AJ"
                    elif s3_mc.current_partner == "Harry":
                        harry "Canoodling? What does that mean?"
                        harry "I mean, I'm not saying no or anything..."
                        s3_mc "Like, kissing and stuff."
                        harry "Oh, OK!"
                    elif s3_mc.current_partner == "AJ":
                        # NEED TO FILL
                        "EMPTY - Route: Coupled up with Camilo or AJ"

    "While the others are still finishing up around you, you stand back and look at your tent."

    if s3e4p2_good_tent:
        s3_mc "Our tent looks amazing!"
        if s3_mc.current_partner == "Bill":
            bill "Yeah, babe. We smashed it."
        elif s3_mc.current_partner == "Camilo":
            camilo "Yeah, babe. We smashed it."
        elif s3_mc.current_partner == "Harry":
            harry "Yeah, babe. We smashed it."
        elif s3_mc.current_partner == "AJ":
            aj "Yeah, babe. We smashed it."
        thought "Hmm, it could be even better..."
        thought "I could go make it super sexy! We'd definitely win the challenge then, and [s3_mc.current_partner] would love it..."
    else:
        s3_mc "Our tent looks really sad."
        if s3_mc.current_partner == "Bill":
            bill "Yeah, we did a rubbish job of it..."
        elif s3_mc.current_partner == "Camilo":
            camilo "Yeah, we did a rubbish job of it..."
        elif s3_mc.current_partner == "Harry":
            harry "Yeah, we did a rubbish job of it..."
        elif s3_mc.current_partner == "AJ":
            aj "Yeah, we did a rubbish job of it..."
        thought "I think I can fix this. If I grab stuff from around the Villa, I can make the tent look amazing!"
        thought "[s3_mc.current_partner] would love it."
    
    # CHOICE
    menu:
        thought "Should I go all out to make this tent look great?"
        "Yeah, make the tent look banging":
            $ s3e4p2_decorate_tent = True
            jump s3e4p2_decorate_tent
        "Nah, it's fine as is...":
            pass

    "All around you, the other Islanders rush about, putting their final touches to their tents."
    "[s3_mc.current_partner] whistles at the tent."
    if s3e4p2_good_tent:
        if s3_mc.current_partner == "Bill":
            bill "Our tent is amazing, babe."
        elif s3_mc.current_partner == "Camilo":
            camilo "Our tent is amazing, babe."
        elif s3_mc.current_partner == "Harry":
            harry "Our tent is amazing, babe."
        elif s3_mc.current_partner == "AJ":
            aj "Our tent is amazing, babe."
    else:
        if s3_mc.current_partner == "Bill":
            bill "I'm not gonna lie. I'm worried about this tent falling down during the night."
        elif s3_mc.current_partner == "Camilo":
            camilo "I'm not gonna lie. I'm worried about this tent falling down during the night."
        elif s3_mc.current_partner == "Harry":
            harry "I'm not gonna lie. I'm worried about this tent falling down during the night."
        elif s3_mc.current_partner == "AJ":
            aj "I'm not gonna lie. I'm worried about this tent falling down during the night."

    "A loud, metallic snap followed by a crash makes the two of you turn around."
    iona "Dammit! How'd that pole snap?"
    genevieve "Do you need help, hun?"
    iona "No!"

    if s3_mc.current_partner != "Camilo":
        camilo "Um, I think we do..."
        
    iona "But..."
    iona "I can riga  pylon! I don't need help with this!"
    nicky "You sure?"
    iona "...Fine. Help, please."
    "The others go over and hold up her tent while she sets about taping together the pole."

    jump s3e4p2_ending

label s3e4p2_decorate_tent:
    s3_mc "I've got an idea!"
    aj "Huh?"
    s3_mc "Just close your eyes, I'm going to do something fun."

    if s3e4p2_give_rock:
        if s3_mc.current_partner == "Bill":
            bill "Again?"
            bill "You're not going to drop more rocks into my hand are you?"
            s3_mc "Just close them and don't open them until I say so! "
            bill "OK..."
        elif s3_mc.current_partner == "Camilo":
            camilo "Again?"
            camilo "You're not going to drop more rocks into my hand are you?"
            s3_mc "Just close them and don't open them until I say so! "
            camilo "OK..."
        elif s3_mc.current_partner == "Harry":
            harry "Again?"
            harry "You're not going to drop more rocks into my hand are you?"
            s3_mc "Just close them and don't open them until I say so! "
            harry "OK..."
        elif s3_mc.current_partner == "AJ":
            aj "Again?"
            aj "You're not going to drop more rocks into my hand are you?"
            s3_mc "Just close them and don't open them until I say so! "
            aj "OK..."

    "[he_she] closes [his_her] eyes."
    "You crawl inside the tent."

    if s3e4p2_good_tent:
        thought "Hmm, it definitely looks better on the outside than on the inside..."
    else:
        thought "As bad on the inside as it is on the outside..."

    thought "Time to fix that!"
    thought "I think the lounge has a plush rug and some fluffy cushions..."
    "You make your way there."

    scene s3-kitchen-day with dissolve
    $ on_screen = []

    "On your way, you spot some fairy lights hanging from the kitchen ceiling."
    thought "They'd give the tent some nice mood lighting..."
    "You start to take down the fairy lights when you hear a voice behind you."

    if s3_mc.bff == "Elladine":
        elladine "Um, [s3_name]...what are you doing?"
    elif s3_mc.bff == "Genevieve":
        genevieve "Um, [s3_name]...what are you doing?"
    elif s3_mc.bff == "Nicky":
        nicky "Um, [s3_name]...what are you doing?"
    elif s3_mc.bff == "Seb":
        seb "Um, [s3_name]...what are you doing?"
    
    # CHOICE
    menu:
        s3_mc "Oh...this?"
        "I need them for sex!":
            # NEED TO FILL
            "EMPTY"
        "I'm making our tent look lush":
            $ s3_mc.like(s3_mc.bff)
            s3_mc "I want to make it look super cosy for [s3_mc.current_partner]."
            if s3_mc.bff == "Elladine":
                elladine "'Cosy', eh?"
            elif s3_mc.bff == "Genevieve":
                genevieve "'Cosy', eh?"
            elif s3_mc.bff == "Nicky":
                nicky "'Cosy', eh?"
            elif s3_mc.bff == "Seb":
                seb "'Cosy', eh?"
        "It isn't what it looks like":
            if s3_mc.bff == "Elladine":
                elladine "Oh really? Because it looks like you're taking a string of fairy lights."
                s3_mc "Hmm... I guess it's exactly how it looks, then."
                s3_mc "I want to use them to make my tent cosier..."
                elladine "'Cosy', eh?"
            elif s3_mc.bff == "Genevieve":
                genevieve "Oh really? Because it looks like you're taking a string of fairy lights."
                s3_mc "Hmm... I guess it's exactly how it looks, then."
                s3_mc "I want to use them to make my tent cosier..."
                genevieve "'Cosy', eh?"
            elif s3_mc.bff == "Nicky":
                nicky "Oh really? Because it looks like you're taking a string of fairy lights."
                s3_mc "Hmm... I guess it's exactly how it looks, then."
                s3_mc "I want to use them to make my tent cosier..."
                nicky "'Cosy', eh?"
            elif s3_mc.bff == "Seb":
                seb "Oh really? Because it looks like you're taking a string of fairy lights."
                s3_mc "Hmm... I guess it's exactly how it looks, then."
                s3_mc "I want to use them to make my tent cosier..."
                seb "'Cosy', eh?"

    if s3_mc.bff == "Elladine":
        elladine "So to achieve the best mood lightning, I suggest you zig-zag these across the top of the tent."
        elladine "Set up mirrors around it, too. That way, they'll catch the light and be a good stand in for candles."
        s3_mc "How do you know this?"
        elladine "I'm an artist, hun. I have an eye for aesthetics, yeah?"
        elladine "And do you not think I know how to get some sexy mood light going?"
    elif s3_mc.bff == "Genevieve":
        genevieve "Oh! You could drape some colourful sheets around them. It'll dim the light and make the tent a funky colour."
        genevieve "I've seen people at festivals do all kinds of fun stuff to decorate their tents."
        genevieve "Do you think we can find a smoke machine lying around here at all?"
        s3_mc "No?"
        genevieve "Shame...what about a bubble one?"
    elif s3_mc.bff == "Nicky":
        nicky "Say no more. I'm all up for helping you score."
        s3_mc "Nicky!"
        nicky "What?"
        s3_mc "You're just so blunt."
        nicky "Only way to be."
    elif s3_mc.bff == "Seb":
        seb "This is weird."
        s3_mc "..."
        seb "But I like weird, so let me help."

    scene s3-lounge with dissolve

    $ pronouns(s3_mc.bff)
    "You and [s3_mc.bff] take down the fairy lights. [he_she!c] then helps you lug some fluffy pillows and the plush rug from the lounge to your tent."

    scene s3-lawn-tents-day with dissolve
    $ on_screen = []

    $ pronouns(s3_mc.current_partner)
    "You pass [s3_mc.current_partner] who still has [his_her] eyes closed."

    if s3_mc.current_partner == "Bill":
        bill "Is that you, babe? Can I open my eyes yet?"
        s3_mc "No! It's still a surprise."
        bill "Aww..."
        show bill at npc_exit
        pause .3
        $ renpy.hide(s3_mc.current_partner.lower())
        $ on_screen.remove(s3_mc.current_partner.lower())
    elif s3_mc.current_partner == "Camilo":
        camilo "Is that you, babe? Can I open my eyes yet?"
        s3_mc "No! It's still a surprise."
        camilo "Aww..."
        show camilo at npc_exit
        pause .3
        $ renpy.hide(s3_mc.current_partner.lower())
        $ on_screen.remove(s3_mc.current_partner.lower())
    elif s3_mc.current_partner == "Harry":
        harry "Is that you, babe? Can I open my eyes yet?"
        s3_mc "No! It's still a surprise."
        harry "Aww..."
        show harry at npc_exit
        pause .3
        $ renpy.hide(s3_mc.current_partner.lower())
        $ on_screen.remove(s3_mc.current_partner.lower())
    elif s3_mc.current_partner == "AJ":
        aj "Is that you, babe? Can I open my eyes yet?"
        s3_mc "No! It's still a surprise."
        aj "Aww..."
        show aj at npc_exit
        pause .3
        $ renpy.hide(s3_mc.current_partner.lower())
        $ on_screen.remove(s3_mc.current_partner.lower())
        
    "Before you know it, you have the nicest tent out of everyone."

    if s3_mc.bff == "Elladine":
        elladine "Woah, now I'm jealous. Can we all just cram in here?"
        s3_mc "Nope!"
        elladine "Hmph, fair."
        "[s3_mc.bff] looks out of the tent towards [s3_mc.current_partner], who's still standing there with closed eyes."
        elladine "Well, looks like it's time for me to leave."
        elladine "You two have some... cosiness to get up to."
        "[s3_mc.bff] winks at you before slipping out of the tent."
        show elladine at npc_exit
        pause .3
        $ renpy.hide(s3_mc.bff.lower())
        $ on_screen.remove(s3_mc.bff.lower())
    elif s3_mc.bff == "Genevieve":
        genevieve "Woah, now I'm jealous. Can we all just cram in here?"
        s3_mc "Nope!"
        genevieve "Hmph, fair."
        "[s3_mc.bff] looks out of the tent towards [s3_mc.current_partner], who's still standing there with closed eyes."
        genevieve "Well, looks like it's time for me to leave."
        genevieve "You two have some... cosiness to get up to."
        "[s3_mc.bff] winks at you before slipping out of the tent."
        show genevieve at npc_exit
        pause .3
        $ renpy.hide(s3_mc.bff.lower())
        $ on_screen.remove(s3_mc.bff.lower())
    elif s3_mc.bff == "Nicky":
        nicky "Woah, now I'm jealous. Can we all just cram in here?"
        s3_mc "Nope!"
        nicky "Hmph, fair."
        "[s3_mc.bff] looks out of the tent towards [s3_mc.current_partner], who's still standing there with closed eyes."
        nicky "Well, looks like it's time for me to leave."
        nicky "You two have some... cosiness to get up to."
        "[s3_mc.bff] winks at you before slipping out of the tent."
        show nicky at npc_exit
        pause .3
        $ renpy.hide(s3_mc.bff.lower())
        $ on_screen.remove(s3_mc.bff.lower())
    elif s3_mc.bff == "Seb":
        seb "Woah, now I'm jealous. Can we all just cram in here?"
        s3_mc "Nope!"
        seb "Hmph, fair."
        "[s3_mc.bff] looks out of the tent towards [s3_mc.current_partner], who's still standing there with closed eyes."
        seb "Well, looks like it's time for me to leave."
        seb "You two have some... cosiness to get up to."
        "[s3_mc.bff] winks at you before slipping out of the tent."
        show seb at npc_exit
        pause .3
        $ renpy.hide(s3_mc.bff.lower())
        $ on_screen.remove(s3_mc.bff.lower())

    s3_mc "Babe! You can come in now."
    "Still covering [his_her] eyes, [s3_mc.current_partner] finds his way into the tent."
    "[he_she!c] kneels in front of the door."
    s3_mc "Alright, open your eyes."

    scene s3-inside-tent-premium-day with dissolve

    "[his_her!c] jaw drops as [he_she] removes [his_her] hand and looks around the tent."

    if s3_mc.current_partner == "Bill":
        bill "What happened to the tent, babe?"
    elif s3_mc.current_partner == "Camilo":
        camilo "What happened to the tent, babe?"
    elif s3_mc.current_partner == "Harry":
        harry "What happened to the tent, babe?"
    elif s3_mc.current_partner == "AJ":
        aj "What happened to the tent, babe?"

    # CHOICE
    menu:
        s3_mc "Oh, the tent?"
        "I thought we'd have a romantic night in":
            s3_mc "And if it meant pinching a bunch of stuff from the Villa, so be it..."
            if s3_mc.current_partner == "Bill":
                bill "I didn't realise you were so sappy!"
                bill "I like it."
            elif s3_mc.current_partner == "Camilo":
                camilo "This is legit one of the most romantic things anyone's ever done for me."
                camilo "Whoever said romance is dead was so wrong."
            elif s3_mc.current_partner == "Harry":
                harry "You've made this tent suddenly feel so much posher."
                harry "The perfect place for some romance..."
            elif s3_mc.current_partner == "AJ":
                aj "I didn't think a tent could be 'sexy'."
                aj "Not that, like, the tent itself is sexy..."
                aj "As in, it creates a mood, kind of thing."
                "She sighs."
                aj "You've done a fab job, babe."
        "You hate it don't you?":
            if s3_mc.current_partner == "Bill":
                bill "Hate it?"
                bill "It's mint, babe!"
            elif s3_mc.current_partner == "Camilo":
                # NEED TO FILL
                "EMPTY - Route: Coupled with Camilo"
            elif s3_mc.current_partner == "Harry":
                # NEED TO FILL
                "EMPTY - Route: Coupled with Harry"
            elif s3_mc.current_partner == "AJ":
                # NEED TO FILL
                "EMPTY - Route: Coupled with AJ"
        "Welcome to my den of sin...":
            if s3_mc.current_partner == "Bill":
                bill "I'd say it's the best den I've ever been in."
                s3_mc "Have you been in many?"
                bill "This is my first. Which makes it the best by default."
                bill "But even if I'd been in many, this would still be the best."
            elif s3_mc.current_partner == "Camilo":
                # NEED TO FILL
                "EMPTY - Route: Coupled with Camilo"
            elif s3_mc.current_partner == "Harry":
                harry "I always wanted a den."
                harry "You know, like a room full of video games and an ultra-wide-screen TV and a popcorn machine."
                s3_mc "Ahem. Focus on the now?"
                harry "Oh yeah, sorry! This tent is amazing."
            elif s3_mc.current_partner == "AJ":
                aj "Agh! I wished I'd known this was going to happen."
                aj "I have this sexy devil Halloween costume back at home which would have been perfect..."

    s3_mc "I'm glad you like it."
    s3_mc "I wanted it to look good for you, babe."
    "[his_her!c] cheeks flush red. For a moment, the only sound you hear is [s3_mc.current_partner]'s gentle breathing..."

    # CHOICE
    menu:
        thought "Should I kiss [s3_mc.current_partner]?"
        "Go in for a kiss":
            "You lean past [s3_mc.current_partner] towards the entrance of the tent and slowly pull and zipper shut."
            if s3_mc.current_partner == "Bill":
                bill "Want to give us some privacy?"
            elif s3_mc.current_partner == "Camilo":
                camilo "Want to give us some privacy?"
            elif s3_mc.current_partner == "Harry":
                harry "Want to give us some privacy?"
            elif s3_mc.current_partner == "AJ":
                aj "Want to give us some privacy?"
            "You don't say anything. Instead, you make your way over to [s3_mc.current_partner] and take hold of [his_her] hand."
            "[he_she!c] moves into your embrace and your lips meet."
            "You gently bite down on [s3_mc.current_partner]'s bottom lip and feel a shudder course through [his_her] body. [he_she] pulls away."
            if s3_mc.current_partner == "Bill":
                bill "I want you..."
            elif s3_mc.current_partner == "Camilo":
                camilo "I want you..."
            elif s3_mc.current_partner == "Harry":
                harry "I want you..."
            elif s3_mc.current_partner == "AJ":
                aj "I want you..."
            s3_mc "..."
        "Give [him_her] a hug":
            "You move across to [s3_mc.current_partner] and wrap your arms around [his_her] waist."
            "[he_she!c] puts [his_her] across your shoulders. As [his_her] arms envelope you, you can feel the warmth of [his_her] body against yours."
            "You're still for a moment, just enjoying the closeness..."
            "You two stay there for a while, under the glow of the fairy lights, just enjoying each other's touch."
            if s3_mc.current_partner == "Bill":
                bill "You're an amazing hugger..."
                s3_mc "And you're so warm!"
                bill "True. I'm pretty hot..."
            elif s3_mc.current_partner == "Camilo":
                camilo "You're an amazing hugger..."
                s3_mc "And you're so warm!"
                camilo "True. I'm pretty hot..."
            elif s3_mc.current_partner == "Harry":
                harry "You're an amazing hugger..."
                s3_mc "And you're so warm!"
                harry "True. I'm pretty hot..."
            elif s3_mc.current_partner == "AJ":
                aj "You're an amazing hugger..."
                s3_mc "And you're so warm!"
                aj "True. I'm pretty hot..."
        "Enjoy the silence":
            "You let out a deep breath and just enjoy the moment for what it is."
            "The sound of gentle wind hitting the side of the tent becomes hypnotic."
            "You're almost about to nod off when..."

    "A crash outside snaps you away from the moment."
    iona "Dammit! How'd that pole snap?"
    genevieve "Do you need help, hun?"
    iona "No!"

    if s3_mc.current_partner != "Camilo":
        camilo "Um, I think we do..."
        iona "But..."

    iona "I'm normally really good at stuff like this..."
    "[s3_mc.current_partner] laughs and turns back to you."

    if s3_mc.current_partner == "Bill":
        bill "Hmm, it's a bit 'busy' outside."
        bill "Maybe later?"
    elif s3_mc.current_partner == "Camilo":
        camilo "Hmm, it's a bit 'busy' outside."
        camilo "Maybe later?"
    elif s3_mc.current_partner == "Harry":
        harry "Hmm, it's a bit 'busy' outside."
        harry "Maybe later?"
    elif s3_mc.current_partner == "AJ":
        aj "Hmm, it's a bit 'busy' outside."
        aj "Maybe later?"

    s3_mc "You'll have to wait and see..."

    scene s3-lawn-tents-day with dissolve
    $ on_screen = []

    "You step out of the tent."
    "You emerge from your tent to find the others holding Iona's tent up while she tapes a snapped pole back together."

    jump s3e4p2_ending

label s3e4p2_ending:
    scene s3-lawn-tents-day with dissolve
    $ on_screen = []

    "While the Islanders are busy putting up Iona's tent, [s3_mc.bff] walks over to you."

    if s3_mc.bff == "Elladine":
        elladine "This challenge has been a thing, eh?"
        s3_mc "Tell me about it."
        elladine "Well, we can't really help Iona. Too many chefs and all that."
        elladine "Guess the best thing we can do is stay out of the way."
    elif s3_mc.bff == "Genevieve":
        elladine "This challenge has been a thing, eh?"
        s3_mc "Tell me about it."
        elladine "Well, we can't really help Iona. Too many chefs and all that."
        elladine "Guess the best thing we can do is stay out of the way."
    elif s3_mc.bff == "Nicky":
        nicky "This challenge has been a thing, eh?"
        s3_mc "Tell me about it."
        nicky "Well, we can't really help Iona. Too many chefs and all that."
        nicky "Guess the best thing we can do is stay out of the way."
    elif s3_mc.bff == "Seb":
        seb "This challenge has been a thing, eh?"
        s3_mc "Tell me about it."
        seb "Well, we can't really help Iona. Too many chefs and all that."
        seb "Guess the best thing we can do is stay out of the way."

    if s3_mc.bff == "Elladine":
        elladine "Hey, [s3_name], could I ask you a quick question?"
        s3_mc "Sure, hun."
        elladine "Do you think I got a bit too much into this challenge?"
        elladine "Like, was I too bossy?"

        # CHOICE
        menu:
            s3_mc "Earlier you..."
            "Were a bit, yeah...":
                # NEED TO FILL
                "EMPTY"
            "Needed to give Nicky a push!":
                # NEED TO FILL
                "EMPTY"
            "Weren't bossy at all":
                "Elladine breathes a small sigh of relief."
                elladine "That's good to hear."

        s3_mc "Why do you ask?"
        "She twiddles her thumbs."
        elladine "One of my exes once said he thought I was too bossy..."
        elladine "I'm fine speaking up for myself! I give instructions in the workshop all the time and I don't worry about it."
        elladine "But then when it comes to romance... I worry Nicky might be put off like my ex was."
        elladine "Maybe I'm being silly..."

        # CHOICE
        menu:
            thought "Elladine says that a guy didn't like her attitude..."
            "Girl, same. It's been an issue for me, too":
                # NEED TO FILL
                "EMPTY"
            "Just for saying what you think?":
                $ s3_mc.like("Elladine")
                elladine "Yeah... I mean the way I say it."
                elladine "Maybe they think I'm unkind? Or want me to change?"
                s3_mc "Woah, hold on!"
                s3_mc "If you were unkind, you wouldn't be this worried about other people, so that's not even on the table."
                s3_mc "And second, never change just so someone can like you!"
                s3_mc "You're great and any guy that's worth it will love you just the way you are."
                "Elladine thinks for a moment."
                elladine "Yeah, you're right!"
                elladine "Thanks, hun."
            "You're not bossy, you're the boss!":
                s3_mc "If people have a problem with you telling it like it is, you just need to remember..."
                s3_mc "...it's them that has the problem!"
                elladine "Well, yeah! But that's easier said than done hun."
                elladine "I will try, though. I don't want to keep driving people away over such a silly thing."
                s3_mc "It's not a silly thing. No one should make you feel you have to change your personality for them to like you!"

        elladine "Thanks for letting me vent..."
        elladine "Enough about me now, what's on your mind?"

        # CHOICE
        menu:
            s3_mc "We should talk about..."
            "The big question. Would you live on Mars?":
                # NEED TO FILL
                "EMPTY"
            "Your biggest hopes and fears":
                elladine "Go big or go home, eh, babe?"
                elladine "Well my biggest hope is to display my art in galleries all around the world."
                elladine "Installations that draw in thousands of people..."
                elladine "I guess my biggest fear is that I don't do the rigging correctly and all of those pieces fall to the ground and shatter..."
                "She lets out a nervous chuckle."
                s3_mc "Is that really it?"
                elladine "Maybe, maybe not."
                elladine "Maybe, I'll tell you properly another time..."
            "This bossy side to you some more":
                elladine "No, hun."
                elladine "Thanks for checking, but I'm good."
                s3_mc "Sure?"
                elladine "Totes sure, you've done your free bit of therapy for the day!"

        "She smiles at you."
        elladine "I really like having these chats with you, hun. It feels like I can leave the rest of the Villa behind for a couple of minutes."

        # CHOICE
        menu:
            thought "I feel..."
            "Completely indifferent to them":
                # NEED TO FILL
                "EMPTY"
            "Like we should just take the money and run":
                # NEED TO FILL
                "EMPTY"
            "The same way about our chats":
                $ s3_mc.like("Elladine")
                elladine "I'm glad to hear it!"
                elladine "They really do make me feel better."

        "She sighs."

    elif s3_mc.bff == "Genevieve":
        genevieve "OK, so..."
        genevieve "I have this thing..."
        genevieve "Like, when you're on a night out, or camping in a field, or you're at a festival..."
        genevieve "Or you're in someone's house with abnormally long corridors and no working light..."
        genevieve "Basically anywhere that, like, might have a toilet in the dark..."
        "She shudders."
        genevieve "Sorry, totally lost my train of thought there."
        genevieve "What was I on about?"
        s3_mc "The thing with toilets in the dark."
        genevieve "Oh, yeah!"
        genevieve "I always try and make sure I have at least one dedicated friend with me who I know will accompany me on the going-to-the-toilet mission."
        genevieve "I call them my Bathroom Babe."
        genevieve "I think out of everyone here, you'd definitely be my main Bathroom Babe."
        genevieve "You just seem like someone I can really count on."

        if s3_mc.current_partner == "Harry":
            "She looks down at her feet."
            genevieve "And I don't want to let something silly like boys get between us."
            genevieve "No matter who Harry ends up with, our friendship is solid."

            # CHOICE
            menu:
                s3_mc "Aw, babe..."
                "This was all so awkward":
                    # NEED TO FILL
                    "EMPTY"
                "Boys smell":
                    # NEED TO FILL
                    "EMPTY"
                "I hope you can forgive me":
                    s3_mc "I stole him from you..."
                    genevieve "Nobody stole anything, and there's nothing to forgive."
                    genevieve "That's literally how it works in here."
                    genevieve "Besides, he wouldn't stop talking about you when we were together."
                    genevieve "And who can blame him? You're amazing."

        genevieve "A true Bathroom Babe."
        genevieve "And that's with a capital 'B' because it's a very important title."

        # CHOICE
        menu:
            thought "Genevieve wants me to be her Bathroom Babe!"
            "Yeah! Let's have a bath together":
                genevieve "Noo, not bathroom bathe."
                genevieve "Bathroom Babe!"
                "She laughs."
                genevieve "Though, now I'm imaging us sat in a bath sky high full of bubbles."
                genevieve "Sipping on wine and having a good soak."
                genevieve "Damn, that would be nice."
            "This is crucial, I hate going to the bathroom alone":
                "Genevieve puts a hand on your shoulder."
                genevieve "Girl."
                genevieve "You don't ever have to worry about that again."
                genevieve "I will go with you."
            "I didn't even know there was a bathroom thing":
                genevieve "Wait, what?"
                genevieve "You haven't used the loo since we got here?"
                s3_mc "Nope!"
                genevieve "That's kinda concerning. I'd speak to a doctor about that."
                genevieve "Oh, wait. I am a doctor."
                genevieve "Well, it's a conflict of interest, because I'm your mate."
                genevieve "Though as your mate, my recommendation is for you to see a doctor about that."
                genevieve "But anyway..."

        genevieve "We'll always stick together when we go to the bathroom at night."
        genevieve "And when we're out of here, we could go to festivals, nights out, and maybe even go on camping trips together!"

    elif s3_mc.bff == "Nicky":
        nicky "Y'know I was thinking about my little sister Rachel again earlier."
        nicky "Thinking about when she was at uni and she did a runner the day before an exam."
        s3_mc "What?"
        nicky "Yeah, she'd found out her boyfriend at the time was cheating on her. And she knew she was going to fail anyway."
        nicky "So she jumped on a bus to Aberdeen to see her ex, and spent the weekend partying with him and his mates."
        nicky "Don't tell anyone.She only told me because she needed to borrow money for the bus home."
        s3_mc "And this is the sister you think I have a lot in common with?"
        nicky "Well, not that stuff, necessarily. I mean, does it sound like the kind of thing you'd do?"

        # CHOICE
        menu:
            thought "Would I drop everything to travel across the country on an impulse?"
            "I would never do that":
                s3_mc "I couldn't be that irresponsible. I don't know if I'd even want to."
                nicky "Yeah, that's probably a good thing."
            "I've totally done that":
                s3_mc "Yeah, that's classic me, to be honest."
                nicky "Ah, I had my suspicions."
            "I'd like to try it someday":
                s3_mc "It's exciting to think about."
                s3_mc "I just haven't ever made that leap before."
                nicky "Well hey, it's never too late to start being spontaneous."

        nicky "You know, I think you'd be a good influence on Rach. I know what I said on our first night here..."
        nicky "How you kind of remind me of her. Just in the way you tend to be surrounded by chaos."
        nicky "And I stand by that, but now we've been here a few days, I wanna make one small disclaimer."
        nicky "You're like Rachel, except you can actually handle the drama going on around you."
        nicky "So even when it's always kicking off, you tend to take it in your stride a lot better."
        nicky "Whereas she's still a bit of a big kid. You're like a more mature version, if that makes sense."

        # CHOICE
        menu:
            thought "Nicky says I'm more like a mature version of his sister..."
            "But I still don't feel properly grown-up":
                s3_mc "Sometimes I look around and realise... I'm an adult now? With a job?!"
                nicky "Have you hit that point yet where people you went to school with start getting married and having kids?"
                s3_mc "Ugh, yes! It's so weird!"
                s3_mc "It feels like just yesterday we were all taking our GCSEs."
                nicky "You'll get used to it."
            "Yeah, I've always been old for my age":
                s3_mc "I think I'm more emotionally mature than most other people my age."
                nicky "Definitely. Though, to be fair, that's not a high bar."
            "Please stop comparing me to your little sister":
                s3_mc "It's weird. Next you're gonna be and helping me with my maths homework."
                nicky "Alright. That was the last time, I promise."

        nicky "Besides, you'll probably be a totally different person by the time you leave here."
        nicky "With everything that's already happened, and more on the horizon, most likely."
        nicky "It could, like, open up whole new parts of yourself you didn't even know about."

        # CHOICE
        menu:
            thought "WIll Love Island change me?"
            "No, I'm already who I want to be":
                # NEED TO FILL
                "EMPTY"
            "Yeah, I'm doing some growing here":
                s3_mc "Yeah, of course. I think this could end up being a turning point in my life."
                s3_mc "Especially if I end up leaving with someone I have real feelings for."
            "Only by making me more famous!":
                s3_mc "It's me who changes the world, not the other way round."
                nicky "Good point."

        s3_mc "What about you? D'you think you're changing by being here?"
        nicky "I hope not. Why would I wanna mess with perfection?"
        s3_mc "Yeah, yeah, okay."

    elif s3_mc.bff == "Seb":
        s3_mc "Oh, hey, by the way."
        s3_mc "How do you think Doom's doing?"
        seb "I'm trying not to think about her too much."
        seb "I know she's in safe hands, but I can't help worrying about her when I do."
        seb "It's weird to think she might've had her kittens already and I wouldn't even know."

        # CHOICE
        menu:
            s3_mc "You might go home to a lot more cats than you left behind..."
            "I wouldn't be looking forward to that":
                # NEED TO FILL
                "EMPTY"
            "Are you sure you're ready to be a dad?":
                "He groans."
                seb "I don't know!"
                seb "It's scary. I really want to do right by them."

                # SUB-CHOICE
                menu:
                    s3_mc "Just remember the most important thing..."
                    "Get them into a good school":
                        pass
                    "Train them to fetch the newspaper":
                        pass
                    "Set up them up on socials":
                        pass
                seb "I will do my best."

            "You're so lucky! Could I adopt one?":
                s3_mc "I'd love to have a new kitten in my life when I leave here."
                seb "Oh, yeah, of course! That's a nice idea."
                seb "Have you had cats before?"

                # CHOICE
                menu:
                    thought "Have I had cats before?"
                    "No, but I'd do my research":
                        pass
                    "Yeah; I've got some experience":
                        pass
                    "So many that it's almost weird":
                        pass
                seb "Cool. I wanna know all Doom's kids are gonna be in safe hands."

        seb "I mean, obviously I'll have to give most of them away, once they're old enough."
        seb "But I'd like to keep one or two around the shop, y'know?"
        seb "To take over Doom's duties someday."
        s3_mc "Have you decided what you're gonna call them?"
        seb "Oh man, I haven't even thought about it."

        # CHOICE
        menu:
            s3_mc "You should name the kittens after..."
            "Your exes":
                # NEED TO FILL
                "EMPTY"
            "Islanders":
                s3_mc "Like, if one of the kittens can explain in detail why it thinks wet food is objectively better than biscuits, you can call it Bill."
                seb "Sure. And 'Harry' can be the kitten with the most relentless ambition in its eyes."
                seb "And 'Genevieve' if one of the kittens turns out to be..."
                seb "No, I can't think of a joke for Genevieve."
            "Music genres":
                s3_mc "You've already got Doom! You could call the kittens Grunge, Sludge, Thrash..."
                seb "Adorable."
                seb "I'm glad we can talk about music."
                seb "I tried to make a joke about shoegaze to AJ the other day, and she thought I was talking about gay people who are into shoes."
                seb "Viv thought it was funny, though."

        "He sighs."
        seb "Viv's just nice. Like it comes naturally to her."
        seb "I wish I knew how she does it."

        # CHOICE
        menu:
            thought "Seb thinks Genevieve is 'nice...'"
            "She's not nice to me":
                # NEED TO FILL
                "EMPTY"
            "Yeah, she's a sweetheart":
                s3_mc "The kind of person who'd wait for your bus with you in the cold type of thing."
                seb "Yeah, exactly."
            "I think you just fancy her":
                "He stares off into space for a while, chewing his lip."
                seb "You might be onto something there."
                seb "It's kinda hard to tell."

        seb "She's the kinda girl I wish I could fall for, y'know? But that wouldn't be very... me."
        s3_mc "You go for bad girls, basically."
        seb "I guess I do."
        seb "Well, hey. If I was good at choosing girlfriends, I wouldn't be here in the first place."
        s3_mc "True."

    "After Iona's tent is finally up, Elladine beams a smile at the rest of you and claps."
    elladine "These tents are amazing!"
    genevieve "It's going to be really hard to choose whose is best!"
    iona "Uh-huh..."
    nicky "Oh, here we go. I've got a text."
    text "Islanders, in your couples, please say who you think has the best tent. You cannot nominate your own. #acontentiousdecision #nothingtoopretentious"
    iona "We can't nominate ourselves?"

    if s3_mc.current_partner != "Camilo":
        camilo "There goes our plan..."
    else:
        iona "Well, there goes my plan..."

    "You look around."

    if s3_mc.current_partner == "Bill":
        bill "Who do you think has the best tent?"
    elif s3_mc.current_partner == "Camilo":
        camilo "Who do you think has the best tent?"
    elif s3_mc.current_partner == "Harry":
        harry "Who do you think has the best tent?"
    elif s3_mc.current_partner == "AJ":
        aj "Who do you think has the best tent?"

    # CHOICE
    menu:
        s3_mc "The best tent is..."
        "[s3_mc.bff]'s one":
            $ s3_mc.like(s3_mc.bff)
            s3_mc "It's clearly the best tent."
            if s3_mc.bff == "Elladine":
                elladine "I couldn't have done it without Nicky's help."
                nicky "Yeah right. You're the organised one."
            elif s3_mc.bff == "Genevieve":
                genevieve "It was tough."
                elladine "I wouldn't have thought so. You just seemed to crack on with it."
                if s3_mc.current_partner != "Harry":
                    harry "That's what Viv's so good at, though."
            elif s3_mc.bff == "Nicky":
                nicky "It literally only exists because Elladine can sort this stuff out so well."
                elladine "Oh, shush. You did loads to help."
            elif s3_mc.bff == "Seb":
                seb "It's kind of you think that."
                if s3_mc.current_partner != "AJ":
                    aj "Stop being so negative! It looks great."
        "Elladine and Nicky's one" if s3_mc.bff != 'Nicky' or s3_mc.bff != 'Elladine':
            $ s3_mc.like("Elladine")
            $ s3_mc.like("Nicky")
            elladine "Thanks, hun!"
            nicky "I'd have been stumped without Elladine, that's for sure."
            elladine "Sorry if I pushed you a bit hard..."
        "Iona and Camilo's one" if s3_mc.current_partner != 'Camilo':
            iona "Um... what?"
            "At that moment, one of the ropes holding her tent up comes loose. Half the tent collapses in on itself."
            camilo "It's kind of you to say that, but it's obvious that we don't have the best tent."
            iona "But you know what? I'll take it."
        "Iona's one" if s3_mc.current_partner == 'Camilo':
            iona "Um... what?"
            "At that moment, one of the ropes holding her tent up comes loose. Half the tent collapses in on itself."
            iona "It's kind of you to say that, babe, but you don't need to make me feel better..."
            iona "But you know what? I'll take it."
        "Our one!":
            if s3_mc.current_partner == "Bill":
                bill "We can't vote for ourselves, babe."
                s3_mc "I don't care. We have the best tent!"
                bill "You're right about that, but..."
                bill "We actually need to vote for someone."
                bill "I think Elladine and Nicky's is the best, personally."
            elif s3_mc.current_partner == "Camilo":
                camilo "We can't vote for ourselves, babe."
                s3_mc "I don't care. We have the best tent!"
                camilo "You're right about that, but..."
                camilo "We actually need to vote for someone."
                camilo "I think Elladine and Nicky's is the best, personally."
            elif s3_mc.current_partner == "Harry":
                harry "We can't vote for ourselves, babe."
                s3_mc "I don't care. We have the best tent!"
                harry "You're right about that, but..."
                harry "We actually need to vote for someone."
                harry "I think Elladine and Nicky's is the best, personally."
            elif s3_mc.current_partner == "AJ":
                aj "We can't vote for ourselves, babe."
                s3_mc "I don't care. We have the best tent!"
                aj "You're right about that, but..."
                aj "We actually need to vote for someone."
                aj "I think Elladine and Nicky's is the best, personally."

    if s3_mc.bff == "Elladine":
        elladine "I think [s3_name] and [s3_mc.current_partner]'s tent is the best! It's got charm."
    elif s3_mc.bff == "Genevieve":
        genevieve "I think [s3_name] and [s3_mc.current_partner]'s tent is the best! It's got charm."
    elif s3_mc.bff == "Nicky":
        nicky "I think [s3_name] and [s3_mc.current_partner]'s tent is the best! It's got charm."
    elif s3_mc.bff == "Seb":
        seb "I think [s3_name] and [s3_mc.current_partner]'s tent is the best! It's got charm."

    if s3_mc.bff != "Nicky" or s3_mc.bff != "Elladine":
        elladine "We agree, too."
    elif s3_mc.bff == "Nicky":
        elladine "Nicky's right."
    elif s3_mc.bff == "Elladine":
        nicky "Yeah, it's got charm."

    "The others look at your tent."

    if s3e4p2_decorate_tent == False and s3e4p2_good_tent == False:
        iona "I'm going to say Elladine and Nicky's gets my vote."
        text "Congrats Elladine and Nicky! The other Islanders have voted your tent as the best. As a reward, you'll get to pick the food for tonight's meal. #foodforthought"
        s3_mc "We didn't win..."
        if s3_mc.current_partner == "Bill":
            bill "You've seen our tent, right?"
        elif s3_mc.current_partner == "Camilo":
            camilo "You've seen our tent, right?"
        elif s3_mc.current_partner == "Harry":
            harry "You've seen our tent, right?"
        elif s3_mc.current_partner == "AJ":
            aj "You've seen our tent, right?"
        "It leans at an odd angle, amongst the rest of the Islanders' tents."
    elif s3e4p2_decorate_tent == True or s3e4p2_good_tent == True:
        iona "Yeah, [s3_name] gets my vote, too."
        miki "And mine!"

        if s3_mc.current_partner == "AJ":
            aj "Mine, too!"

        if s3_mc.current_partner == "Camilo":
            camilo "Agreed."

        if s3_mc.current_partner == "Harry":
            harry "It's definitely the nicest one here."

        if s3_mc.current_partner == "Bill":
            bill "That makes the most sense to me."

        thought "Everyone voted for our tent!"
        "Your phone pings loudly."
        text "Congrats [s3_name] and [s3_mc.current_partner]! The other Islanders have voted your tent as the best. As a reward, you'll get to pick the food for tonight's meal. #foodforthought"
        s3_mc "We won!"

        if s3_mc.current_partner == "Bill":
            bill "Of course! Our tent does look proper good."
        elif s3_mc.current_partner == "Camilo":
            camilo "Of course! Our tent does look proper good."
        elif s3_mc.current_partner == "Harry":
            harry "Of course! Our tent does look proper good."
        elif s3_mc.current_partner == "AJ":
            aj "Of course! Our tent does look proper good."

    "It stands proud amongst the rest of the Islanders' tents. Clearly the best one."
    elladine "Congrats, guys!"
    "You see Miki peek into her tent."
    miki "Hmm, they're still missing something..."
    iona "What?"
    miki "Sleeping bags and things!"

    if s3e4p2_decorate_tent:
        miki "Just like how [s3_name] did with her tent up!"

    nicky "What's the point? It's not like we'll be sleeping here tonight."
    "You pull out your phone."
    text "Islanders, tonight you will be camping out in your tents! #intense #intents"
    nicky "Oh. Well, that answers that."

    # CHOICE
    menu:
        thought "Camping outdoors?"
        "Hell yeah!":
            s3_mc "It's going to be so cosy!"
        "But what about the bugs?":
            if s3_mc.current_partner == "Bill":
                bill "Don't worry about them, babe. Just stay in my arms."
                bill "I'll keep you safe."
            elif s3_mc.current_partner == "Camilo":
                camilo "Don't worry about them, babe. Just stay in my arms."
                camilo "I'll keep you safe."
            elif s3_mc.current_partner == "Harry":
                harry "Don't worry about them, babe. Just stay in my arms."
                harry "I'll keep you safe."
            elif s3_mc.current_partner == "AJ":
                aj "Don't worry about them, babe. Just stay in my arms."
                aj "I'll keep you safe."
        "You can get up to a lot in a tent...":
            if s3_mc.current_partner == "Bill":
                harry "They're a bit cramped, if I'm honest..."
                harry "But I'm still up for this."
            elif s3_mc.current_partner == "Camilo":
                # NEED TO FILL
                "EMPTY - Route: Coupled with Camilo"
            elif s3_mc.current_partner == "Harry":
                harry "They're a bit cramped, if I'm honest..."
                harry "But I'm still up for this."
            elif s3_mc.current_partner == "AJ":
                aj "Yeah! Once me and a friend drained this guy's keg of beer at Reading."
                aj "He had no idea!"
                s3_mc "I was thinking something a little sexier..."
                aj "Oooh..."

    elladine "This is so exciting! I can't wait to camp out tonight. It's been years since I last went camping."

    # CHOICE
    menu:
        s3_mc "Camping is the..."
        "Best way to connect with nature":
            $ s3_mc.like("Miki")
            miki "Camping's one of the reasons I bought my barge."
            miki "I wouldn't want to live in a tent forever, but I knew a normal house wasn't my thing."
            seb "Sounds like a good way to have all your stuff sink to the bottom of a river..."
            miki "Why would it sink?"
            "Seb shrugs."
            seb "Pirates."
            s3_mc "In a Cambridge canal?"
            seb "Canal pirates."
        "Perfect way to ruin a good weekend":
            s3_mc "Why do people want to sleep on the ground?"
            miki "What? It's so peaceful, though!"
            seb "Nah, [s3_name]'s got the right outlook."
            seb "It's called a B&B. I'll take an actual mattress any day."
            miki "Don't you camp for festivals, though?"
            seb "Yeah, but I don't sleep much."
        "Leading cause of tent related injuries":
            bill "Well, yeah? Where else would you get tent related injuries?"
            "The others think."
            aj "In a... tent factory?"
            bill "Oh, that's true. In fact, I bet they're way more dangerous than just camping."
            s3_mc "Yeah, but how many people work in a tent factory versus how many people go camping?"
            bill "Also a good point."
            camilo "This is well hard to answer."
            iona "Then maybe we... don't?"

    elladine "I'm so lost in this conversation..."
    elladine "But I don't care. Let's grab some bedding so we can do all the camping things!"
    elladine "Shame we don't have marshmallows..."

    scene sand with dissolve
    $ on_screen = []

    "And so, with their tents erected, our Islanders are ready for tonight's big camp out."
    "Except for Iona, whose tent skills have made me scared to go near any pylon in Scotland."
    "At least [s3_name] and [s3_mc.current_partner] don't have to worry about their tent!"
    "I've never seen such a sturdy structure, and I once spent two years in Alcatraz."
    "Worst sightseeing tour of my life..."
    "Coming up!"
    "Things get spooky..."

    $ outfit = "evening"

    genevieve "Be gone, shiny demon!"
    show genevieve at npc_exit
    pause .3
    $ renpy.hide("genevieve")
    $ on_screen = []

    "And will the wind be the only thing shaking the tents?"
    
    $ outfit = "pjs"

    if s3_mc.current_partner == "Bill":
        bill "How about it then?"
    elif s3_mc.current_partner == "Camilo":
        camilo "How about it then?"
    elif s3_mc.current_partner == "Harry":
        harry "How about it then?"
    elif s3_mc.current_partner == "AJ":
        aj "How about it then?"

    jump s3e4p3


#########################################################################
## Episode 4, Part 3
#########################################################################
label s3e4p3:
    scene sand with dissolve
    $ on_screen = []
    $ outfit = "swim"

    $ pronouns(s3_mc.current_partner)

    "Previously, our Islanders put their construction skills to the test..."
    aj "I can't find the hole!"
    show aj at npc_exit
    pause .3
    $ renpy.hide("aj")
    $ on_screen.remove("aj")

    "By pitching some tents in the back garden."
    elladine "Run!"
    show elladine at npc_exit
    pause .3
    $ renpy.hide("elladine")
    $ on_screen.remove("elladine")

    "You can't run through a campsite, Elladine!"
    "You can only ran."
    "Why?"
    "Because it's past tents."
    "Prime time content here, folks."
    "Tonight on Love Island..."
    "The Islanders have a big camp out in their erected tents."

    if s3_mc.current_partner == "Bill":
        bill "This is the first time we get to spend the night together..."
        bill "Alone!"
    elif s3_mc.current_partner == "Camilo":
        camilo "This is the first time we get to spend the night together..."
        camilo "Alone!"
    elif s3_mc.current_partner == "Harry":
        harry "This is the first time we get to spend the night together..."
        harry "Alone!"
    elif s3_mc.current_partner == "AJ":
        aj "This is the first time we get to spend the night together..."
        aj "Alone!"
    
    "Need I say more?"

    scene s3-dressing-room with dissolve
    $ on_screen = []

    $ outfit = "pjs"

    "You're in the dressing room trying to find something to wear for tonight's camp out."
    thought "What am I going to wear to sleep outside?"
    "Someone knocks at the door."

    if s3_mc.current_partner == "Bill":
        bill "[s3_name], are you up here?"
    elif s3_mc.current_partner == "Camilo":
        camilo "[s3_name], are you up here?"
    elif s3_mc.current_partner == "Harry":
        harry "[s3_name], are you up here?"
    elif s3_mc.current_partner == "AJ":
        aj "[s3_name], are you up here?"

    s3_mc "I'm in here."
    "[s3_mc.current_partner] shuffles in, closing the door behind [him_her]."
    "[he_she!c]'s holding a top in [his_her] hand."

    if s3_mc.current_partner == "Bill":
        bill "If you want, you can borrow one of my tops to sleep in tonight, like, as an extra layer."
        bill "That's like a cute coupley thing that girls like, right?"
        bill "Steal their boyfriend's clothes."
        s3_mc "Totally."
        bill "I wore this thing the first time I ever plonked a tile on a roof."
        bill "It's kinda my lucky top, I guess."
        bill "I haven't actually worn it yet here."
        bill "But I think it would look cute on you."
    elif s3_mc.current_partner == "Camilo":
        camilo "If you want, you can borrow one of my tops to sleep in tonight, like, as an extra layer."
        camilo "That's like a cute coupley thing that girls like, right?"
        camilo "Steal their boyfriend's clothes."
        s3_mc "Totally."
        camilo "Whenever I go to Jiu Jitsu, I always have this on under my gi."
        s3_mc "That's really sweet."
        s3_mc "But also totally gross."
        camilo "It's been washed!"
        camilo "It's kinda my lucky top, I guess."
        camilo "I haven't actually worn it yet here."
        camilo "But I think it would look cute on you."
    elif s3_mc.current_partner == "Harry":
        harry "If you want, you can borrow one of my tops to sleep in tonight, like, as an extra layer."
        harry "That's like a cute coupley thing that girls like, right?"
        harry "Steal their boyfriend's clothes."
        s3_mc "Totally."
        harry "I always wear this under a shirt when I go for an interview."
        harry "It's kinda my lucky top, I guess."
        harry "I haven't actually worn it yet here."
        harry "But I think it would look cute on you."
    elif s3_mc.current_partner == "AJ":
        aj "If you want, you can borrow one of my tops to sleep in tonight, like, as an extra layer."
        aj "That's like a cute coupley thing that girls like, right?"
        aj "Sharing each other's entire wardrobe is a given when you're with a girl, right?"
        aj "And guys too, to be fair."
        aj "But it's harder to share jeans and stuff."
        s3_mc "I'm gonna steal all your clothes!"  
        aj "I wear this all the time under my hockey gear."
        s3_mc "That's really sweet."
        s3_mc "But also totally gross."
        aj "It's been washed!"
        aj "It's kinda my lucky top, I guess."
        aj "I haven't actually worn it yet here."
        aj "But I think it would look cute on you."

    # CHOICE
    menu:
        thought "[s3_mc.current_partner] wants me to wear his lucky top!"
        "Yeah, I'd love to wear it":
            $ s3_mc.like(s3_mc.current_partner)
            $ s3e4p3_wear_shirt = True

            "[s3_mc.current_partner] smiles and hands it to you."
            if s3_mc.current_partner == "Bill":
                bill "Sweet."
                bill "I'll let you get changed."
            elif s3_mc.current_partner == "Camilo":
                camilo "Sweet."
                camilo "I'll let you get changed."
            elif s3_mc.current_partner == "Harry":
                harry "Sweet."
                harry "I'll let you get changed."
            elif s3_mc.current_partner == "AJ":
                aj "Sweet."
                aj "I'll let you get changed."
            "[he_she!c] looks away as you slip on the top."
            if s3_mc.current_partner == "Bill":
                bill "Perfect!"
                bill "Well, it's a bit baggy..."
                bill "But I find oversized clothes so sexy on a girl."
                bill "I'm never getting that back, am I?"
                s3_mc "Nope."
                bill "Fair enough, gorgeous."
                bill "Let's go down and find the others."
            elif s3_mc.current_partner == "Camilo":
                camilo "Oh, damn."
                camilo "That looks so hot on you."
                camilo "I'm never getting that back, am I?"
                s3_mc "Nope."
                camilo "Fair enough, gorgeous."
                camilo "Let's go down and find the others."
            elif s3_mc.current_partner == "Harry":
                harry "Dang, girl."
                harry "That t-shirt suits you to a T."
                harry "I'm never getting that back, am I?"
                s3_mc "Nope."
                harry "Fair enough, gorgeous."
                harry "Let's go down and find the others."
            elif s3_mc.current_partner == "AJ":
                aj "It looks so cute on you."
                aj "Way cuter than it looks on me!"
                aj "I'm never getting that back, am I?"
                s3_mc "Nope."
                aj "Fair enough, gorgeous."
                aj "Let's go down and find the others."
        "Nah, I'm alright":
            if s3_mc.current_partner == "Bill":
                bill "Aw, are you sure?"
                s3_mc "I prefer my clothes"
                bill "Oh, okay, fair enough!"
            elif s3_mc.current_partner == "Camilo":
                camilo "Aw, are you sure?"
                s3_mc "I prefer my clothes"
                camilo "Oh, okay, fair enough!"
            elif s3_mc.current_partner == "Harry":
                harry "Aw, are you sure?"
                s3_mc "I prefer my clothes"
                harry "Oh, okay, fair enough!"
            elif s3_mc.current_partner == "AJ":
                aj "Aw, are you sure?"
                s3_mc "I prefer my clothes"
                aj "Oh, okay, fair enough!"

    # ADD back once MC has images in game
    # thought "Even if I don't want to wear [his_her] top, I still want to look good for [s3_mc.current_partner]."
    # thought "This'll be our first night together, after all!"
    # MC outfit changes to sleepwear
    # thought "Hmm. Got to leave some things to the imagination, though, right?"
    # B/H/Cam/aj "Not stressing about what to wear to bed, are you, MC?"
    # B/H/Cam/aj "You know I think you look hot regardless."
    # s3_mc "Thanks, babe."

    if s3_mc.current_partner == "Bill":
        bill "Wow, this is going to be the first time, we, like, properly get to spend the night together..."
        bill "Alone!"
    elif s3_mc.current_partner == "Camilo":
        camilo "Wow, this is going to be the first time, we, like, properly get to spend the night together..."
        camilo "Alone!"
    elif s3_mc.current_partner == "Harry":
        harry "Wow, this is going to be the first time, we, like, properly get to spend the night together..."
        harry "Alone!"
    elif s3_mc.current_partner == "AJ":
        aj "Wow, this is going to be the first time, we, like, properly get to spend the night together..."
        aj "Alone!"

    # CHOICE
    menu:
        thought "This is our first night alone together..."
        "I can't wait to get hot and sweaty in the tent":
            if s3_mc.current_partner == "Bill":
                bill "Yeah, we better get loads of blankets to keep warm."
                bill "Oh, wait... did you mean..."
                "You raise an eyebrow."
                bill "Ah, right. Gotcha."
                bill "Well, that can be arranged."
            elif s3_mc.current_partner == "Camilo":
                camilo "I'm literally a human radiator so, yeah."
                camilo "You bet it's going to be hot in there."
                s3_mc "That's not exactly what I..."
                camilo "Oh, you meant..."
                "[he_she!c] raises [his_her] eyebrows."
                camilo "Well, that can be arranged."
            elif s3_mc.current_partner == "Harry":
                harry "Yeah, we better get loads of blankets to keep warm."
                harry "Oh, wait... did you mean..."
                "You raise an eyebrow."
                harry "Ah, right. Gotcha."
                harry "Well, that can be arranged."
            elif s3_mc.current_partner == "AJ":
                aj "I'm literally a human radiator so, yeah."
                aj "You bet it's going to be hot in there."
                s3_mc "That's not exactly what I..."
                aj "Oh, you meant..."
                "[he_she!c] raises [his_her] eyebrows."
                aj "Well, that can be arranged."
        "I'm kinda scared of the dark...":
            if s3_mc.current_partner == "Bill":
                bill "Hey, don't worry about it."
                bill "I'll be there."
                bill "And if anything does happen..."
                "[he_she!c] grabs something from the dresser."
                bill "I'll defend you with this magic hairbrush!"
                s3_mc "Will that help?"
                bill "Absolutely. It works every time."
            elif s3_mc.current_partner == "Camilo":
                camilo "Hey, don't worry about it."
                camilo "I'll be there."
                camilo "And if anything does happen..."
                "[he_she!c] grabs something from the dresser."
                camilo "I'll defend you with this magic hairbrush!"
                s3_mc "Will that help?"
                camilo "Absolutely. It works every time."
            elif s3_mc.current_partner == "Harry":
                harry "Hey, don't worry about it."
                harry "I'll be there."
                harry "And if anything does happen..."
                "[he_she!c] grabs something from the dresser."
                harry "I'll defend you with this magic hairbrush!"
                s3_mc "Will that help?"
                harry "Absolutely. It works every time."
            elif s3_mc.current_partner == "AJ":
                aj "Hey, don't worry about it."
                aj "I'll be there."
                aj "And if anything does happen..."
                "[he_she!c] grabs something from the dresser."
                aj "I'll defend you with this magic hairbrush!"
                s3_mc "Will that help?"
                aj "Absolutely. It works every time."
        "I will miss sleeping in a room full of people":
            if s3_mc.current_partner == "Bill":
                bill "If that's what floats your boat..."
            elif s3_mc.current_partner == "Camilo":
                camilo "If that's what floats your boat..."
            elif s3_mc.current_partner == "Harry":
                harry "If that's what floats your boat..."
            elif s3_mc.current_partner == "AJ":
                aj "If that's what floats your boat..."
            s3_mc "It does."
            s3_mc "I love being surrounded by many, many, sleeping bodies."
            if s3_mc.current_partner == "Bill":
                bill "Well... I'm sure we'll only be spending one night in the tent."
            elif s3_mc.current_partner == "Camilo":
                camilo "Well... I'm sure we'll only be spending one night in the tent."
            elif s3_mc.current_partner == "Harry":
                harry "Well... I'm sure we'll only be spending one night in the tent."
            elif s3_mc.current_partner == "AJ":
                aj "Well... I'm sure we'll only be spending one night in the tent."

    if s3_mc.current_partner == "Bill":
        if s3e4p2_good_tent:
            bill "We'd better go choose what we want to eat at our camp out!"
        else:
            bill "I hope Elladine picks out some good stuff to eat for our camp out..."
    elif s3_mc.current_partner == "Camilo":
        if s3e4p2_good_tent:
            camilo "We'd better go choose what we want to eat at our camp out!"
        else:
            camilo "I hope Elladine picks out some good stuff to eat for our camp out..."
    elif s3_mc.current_partner == "Harry":
        if s3e4p2_good_tent:
            harry "We'd better go choose what we want to eat at our camp out!"
        else:
            harry "I hope Elladine picks out some good stuff to eat for our camp out..."
    elif s3_mc.current_partner == "AJ":
        if s3e4p2_good_tent:
            aj "We'd better go choose what we want to eat at our camp out!"
        else:
            aj "I hope Elladine picks out some good stuff to eat for our camp out..."

    "You both head down to the kitchen."

    scene s3-kitchen-night with dissolve
    $ on_screen = []

    "You head downstairs. Elladine and Nicky are also in the kitchen."

    if s3e4p3_wear_shirt:
        "Elladine points at your top."
        elladine "That's not your top, is it?"
        elladine "I don't recognise it."
        s3_mc "It's [s3_mc.current_partner]'s."
        if s3_mc.current_partner == "Bill":
            bill "I lent it to her."
            "[s3_mc.current_partner] beams at you."
            bill "Looks cute, doesn't it?"
            elladine "So cute."
            nicky "You guys are the cutest."
            bill "We try."
        elif s3_mc.current_partner == "Camilo":
            camilo "I lent it to her."
            "[s3_mc.current_partner] beams at you."
            camilo "Looks cute, doesn't it?"
            elladine "So cute."
            nicky "You guys are the cutest."
            camilo "We try."
        elif s3_mc.current_partner == "Harry":
            harry "I lent it to her."
            "[s3_mc.current_partner] beams at you."
            harry "Looks cute, doesn't it?"
            elladine "So cute."
            nicky "You guys are the cutest."
            harry "We try."
        elif s3_mc.current_partner == "AJ":
            aj "I lent it to her."
            "[s3_mc.current_partner] beams at you."
            aj "Looks cute, doesn't it?"
            elladine "So cute."
            nicky "You guys are the cutest."
            aj "We try."
        "[s3_mc.current_partner] squeezes your hand affectionately."
        nicky "When can we start wearing each other's clothes, babe?"
        elladine "I don't share clothes, babe."
        nicky "Aw."

    if s3e4p2_good_tent or s3e4p2_decorate_tent:
        if s3_mc.current_partner == "Bill":
            bill "So, what food shall we have?"
        elif s3_mc.current_partner == "Camilo":
            camilo "So, what food shall we have?"
        elif s3_mc.current_partner == "Harry":
            harry "So, what food shall we have?"
        elif s3_mc.current_partner == "AJ":
            aj "So, what food shall we have?"

        # CHOICE
        menu:
            thought "What food should we choose for our camp out?"
            "Sausages and beans":
                $ s3e4p3_supper = "Beans"
                if s3_mc.current_partner == "Bill":
                    bill "Yes!"
                    if s3e2p1_bfast_with_bill:
                        $ s3_mc.like("Bill")
                        bill "Like we had on our first sort of breakfast date!"
                        s3_mc "Yeah, just like that!"
                        bill "Sausages and beans are the best part of the fry up."
                elif s3_mc.current_partner == "Camilo":
                    camilo "We can try to cook it over the fire."
                elif s3_mc.current_partner == "Harry":
                    harry "We can try to cook it over the fire."
                elif s3_mc.current_partner == "AJ":
                    aj "We can try to cook it over the fire."
                "[s3_mc.current_partner] gets some tins of beans out from the cupboard and packs of sausages out of the fridge."
                if s3_mc.diet != "Meat":
                    if s3_mc.current_partner == "Bill":
                        bill "We can do veggie sausages for you, [s3_name]."
                    elif s3_mc.current_partner == "Camilo":
                        camilo "We can do veggie sausages for you, [s3_name]."
                    elif s3_mc.current_partner == "Harry":
                        harry "We can do veggie sausages for you, [s3_name]."
                    elif s3_mc.current_partner == "AJ":
                        aj "We can do veggie sausages for you, [s3_name]."
                    s3_mc "Aw, you star. Thanks, babe!"
            "Marshmallows":
                $ s3e4p3_supper = "Marshmallows"
                if s3_mc.current_partner == "Bill":
                    bill "Reminds me of being a kid."
                    "[s3_mc.current_partner] rummages in a cupboard in search for some marshmallows."
                    if s3_mc.diet != "Meat":
                        bill "We've got veggie marshmallows for you, [s3_name]."
                        s3_mc "That's awesome. Thanks, babe!"
                    bill "Got some."
                elif s3_mc.current_partner == "Camilo":
                    camilo "Reminds me of being a kid."
                    "[s3_mc.current_partner] rummages in a cupboard in search for some marshmallows."
                    if s3_mc.diet != "Meat":
                        camilo "We've got veggie marshmallows for you, [s3_name]."
                        s3_mc "That's awesome. Thanks, babe!"
                    camilo "Got some."
                elif s3_mc.current_partner == "Harry":
                    harry "Reminds me of being a kid."
                    "[s3_mc.current_partner] rummages in a cupboard in search for some marshmallows."
                    if s3_mc.diet != "Meat":
                        harry "We've got veggie marshmallows for you, [s3_name]."
                        s3_mc "That's awesome. Thanks, babe!"
                    harry "Got some."
                elif s3_mc.current_partner == "AJ":
                    aj "Reminds me of being a kid."
                    "[s3_mc.current_partner] rummages in a cupboard in search for some marshmallows."
                    if s3_mc.diet != "Meat":
                        aj "We've got veggie marshmallows for you, [s3_name]."
                        s3_mc "That's awesome. Thanks, babe!"
                    aj "Got some."
                    "[s3_mc.current_partner] puts them on a counter, along with some wooden sticks to roast them."
            "Noodle soup":
                $ s3e4p3_supper = "Soup"
                if s3_mc.current_partner == "Bill":
                    bill "Soup?"
                    s3_mc "Yeah. Specifically noodle soup."
                    s3_mc "Nothing better than sitting around the fire pit sipping a mug of hot soup."
                    bill "Well, when you put it like that it sounds so wholesome."
                    "[s3_mc.current_partner] starts getting out some tins of soup and some mugs."
                elif s3_mc.current_partner == "Camilo":
                    camilo "Soup?"
                    s3_mc "Yeah. Specifically noodle soup."
                    s3_mc "Nothing better than sitting around the fire pit sipping a mug of hot soup."
                    camilo "Well, when you put it like that it sounds so wholesome."
                    "[s3_mc.current_partner] starts getting out some tins of soup and some mugs."
                elif s3_mc.current_partner == "Harry":
                    harry "Soup?"
                    s3_mc "Yeah. Specifically noodle soup."
                    s3_mc "Nothing better than sitting around the fire pit sipping a mug of hot soup."
                    harry "Well, when you put it like that it sounds so wholesome."
                    "[s3_mc.current_partner] starts getting out some tins of soup and some mugs."
                elif s3_mc.current_partner == "AJ":
                    aj "Soup?"
                    s3_mc "Yeah. Specifically noodle soup."
                    s3_mc "Nothing better than sitting around the fire pit sipping a mug of hot soup."
                    aj "Well, when you put it like that it sounds so wholesome."
                    "[s3_mc.current_partner] starts getting out some tins of soup and some mugs."
    else:
        elladine "Right. Time to plan out the food."
        nicky "I think we should go for marshmallows!"
        elladine "Nice choice."
        "Nicky rummages in the cupboards and the fridge."

    nicky "Do we need to get the campfire started?"
    elladine "Surely we'd just use the fire pit since, like, it's already there."
    nicky "But it's not camping without a proper fire!"
    s3_mc "Maybe this is safer. No one will lose an eyebrow."

    if s3_mc.current_partner == "Bill":
        bill "Nah, someone has to light it, surely."
    elif s3_mc.current_partner == "Camilo":
        camilo "Nah, someone has to light it, surely."
    elif s3_mc.current_partner == "Harry":
        harry "Nah, someone has to light it, surely."
    elif s3_mc.current_partner == "AJ":
        aj "Nah, someone has to light it, surely."

    nicky "Well, how hard can it be?"
    elladine "I'll show you."
    elladine "I'm a proper fire starter."

    scene s3-firepit-night with dissolve
    $ on_screen = []

    "You, [s3_mc.current_partner] and Elladine head over to the firepit."

    "The warm red hues of the flames illuminate everyone's faces as they gather around the firepit."
    "A grill has been suspended over the flames."
    "You pile up everything you brought from the kitchen by the fire."
    elladine "Aw, it's already on."
    seb "You can't turn a fire on, Elladine."
    elladine "Well, I don't know?"
    elladine "This place could be hooked up to all sorts of magic."

    if s3_mc.current_partner == "Bill":
        miki "It was already on when we got here. I set the grill up, though."
    elif s3_mc.current_partner == "Camilo":
        iona "It was already on when we got here. I set the grill up, though."
    elif s3_mc.current_partner == "Harry":
        genevieve "It was already on when we got here. I set the grill up, though."
    elif s3_mc.current_partner == "AJ":
        seb "It was already on when we got here. I set the grill up, though."

    elladine "[s3_3rd_girl_options[s3_mc.current_partner]] is a sorcerer."
    "[s3_3rd_girl_options[s3_mc.current_partner]] gives [s3_mc.current_partner] a melancholy look."
    "Elladine smiles at her sympathetically."
    elladine "Thanks, hun."
    "[s3_mc.current_partner] edges closer to you and squeezes your hand reassuringly."

    if s3e4p2_decorate_tent:
        if s3_mc.current_partner == "Bill":
            miki "Your tent looks great, by the way."
            s3_mc "I wanted it to look nice for tonight."
            miki "Course you did."
        elif s3_mc.current_partner == "Camilo":
            iona "Your tent looks great, by the way."
            s3_mc "I wanted it to look nice for tonight."
            iona "Course you did."
        elif s3_mc.current_partner == "Harry":
            genevieve "Your tent looks great, by the way."
            s3_mc "I wanted it to look nice for tonight."
            genevieve "Course you did."
        elif s3_mc.current_partner == "AJ" and s3_mc.bff != "Seb":
            seb "Your tent looks great, by the way."
            s3_mc "I wanted it to look nice for tonight."
            seb "Course you did."

    genevieve "OK, for real. I'm starving!"
    genevieve "What food did you guys bring over?"

    if s3e4p2_good_tent or s3e4p2_decorate_tent:
        if s3e4p3_supper == "Beans":
            s3_mc "We brought sausages and beans!"
            genevieve "Aw, brilliant."
        elif s3e4p3_supper == "Marshmallows":
            s3_mc "We brought marshmallows!"
            genevieve "Aw, brilliant."
        elif s3e4p3_supper == "Soup":
            s3_mc "We brought noodle soup!"
            genevieve "Aw, brilliant."
            if s3_mc.current_partner != "Harry":
                harry "I always forget this stuff can come in tins. "
                harry "Much quicker to just cut open the little packets."
                harry "I'm all about low effort cooking."
    else:
        elladine "Marshmallows!"


    if s3e4p2_good_tent or s3e4p2_decorate_tent:
        if s3e4p3_supper == "Beans":
            "You put a frying pan on the grill and slap the sausages into the sizzling oil."
            "[s3_mc.current_partner] plops the baked beans into a saucepan."
            bill "Sausages and beans is, like, camping perfection."
            "The sausages and beans have been sizzling in a pan on the fire for a few minutes."
            "Genevieve pokes the sausage."
            genevieve "It doesn't look all that cooked to me..."
            "Camilo sticks a fork in it and holds the sausage up."
            camilo "It's all pink and floppy."
            miki "That's the name of your sex tape, Camilo."
            "Camilo playfully nudges her."
            iona "Give it a minute, babe."
            "[s3_mc.current_partner] is warming [his_her] hands by the fire."
            s3_mc "You cold, [s3_mc.current_partner]?"

            if s3_mc.current_partner == "Bill":
                bill "Nah, not majorly."
                bill "But if you want to warm me up I'm not going to object."
            elif s3_mc.current_partner == "Camilo":
                camilo "Nah, not majorly."
                camilo "But if you want to warm me up I'm not going to object."
            elif s3_mc.current_partner == "Harry":
                harry "Nah, not majorly."
                harry "But if you want to warm me up I'm not going to object."
            elif s3_mc.current_partner == "AJ":
                aj "Nah, not majorly."
                aj "But if you want to warm me up I'm not going to object."

            # CHOICE
            menu:
                thought "I should..."
                "Cuddle up to [him_her] by the fire":
                    s3_mc "Come here, you."
                    "You both snuggle up closer together."
                    "[s3_mc.current_partner] leans [his_her] head onto your shoulder and you wrap your arms around [him_her], enveloping [him_her] in your embrace."
                    if s3_mc.current_partner == "Bill":
                        bill "You're so comfy, babe."
                        bill "Like, I could literally fall asleep right here, right now."
                    elif s3_mc.current_partner == "Camilo":
                        camilo "You're so comfy, babe."
                        camilo "Like, I could literally fall asleep right here, right now."
                    elif s3_mc.current_partner == "Harry":
                        bill "You're so comfy, babe."
                        bill "Like, I could literally fall asleep right here, right now."
                    elif s3_mc.current_partner == "AJ":
                        aj "You're so comfy, babe."
                        aj "Like, I could literally fall asleep right here, right now."
                    "[s3_mc.current_partner] pretends to snore."
                    iona "Have you put [s3_mc.current_partner] under a sleeping spell?"
                    s3_mc "I'm afraid so."
                    "You start moving your fork towards [s3_mc.current_partner]'s plate."
                    s3_mc "I wanted a second helping of sausages and beans."
                    "Elladine laughs. [s3_mc.current_partner] sits up straight again."
                    if s3_mc.current_partner == "Bill":
                        bill "I'm awake! I'm awake!"
                    elif s3_mc.current_partner == "Camilo":
                        camilo "I'm awake! I'm awake!"
                    elif s3_mc.current_partner == "Harry":
                        harry "I'm awake! I'm awake!"
                    elif s3_mc.current_partner == "AJ":
                        aj "I'm awake! I'm awake!"
                "Whisper what I want to do to [him_her] tonight in [his_her] ear":
                    thought "That ought to warm [him_her] up."
                    "You lean in to [s3_mc.current_partner]'s ear and whisper."
                    s3_mc "Tonight..."
                    s3_mc "I have something I want to do to you..."
                    if s3_mc.current_partner == "Bill":
                        bill "Firepit.sausages.a.Oh.yeah."
                    elif s3_mc.current_partner == "Camilo":
                        camilo "Firepit.sausages.a.Oh.yeah."
                    elif s3_mc.current_partner == "Harry":
                        harry "Firepit.sausages.a.Oh.yeah."
                    elif s3_mc.current_partner == "AJ":
                        aj "Firepit.sausages.a.Oh.yeah."
                    s3_mc "It involves..."
                    "You slowly stroke [his_her] leg with your finger."
                    s3_mc "One hundred percent less clothes and for us to be very..."
                    s3_mc "Very..."
                    s3_mc "Close."
                    if s3_mc.current_partner == "Bill":
                        bill "You're so naughty."
                    elif s3_mc.current_partner == "Camilo":
                        camilo "You're so naughty."
                    elif s3_mc.current_partner == "Harry":
                        harry "You're so naughty."
                    elif s3_mc.current_partner == "AJ":
                        aj "You're so naughty."
                    "You smile seductively."
                    s3_mc "You have no idea."
                "Put some more logs on the fire":
                    "You get some logs from the side and pop them on the fire to keep it roaring, taking care to not knock the sausages."
                    if s3_mc.current_partner == "Bill":
                        bill "Good idea, babe!"
                    elif s3_mc.current_partner == "Camilo":
                        camilo "Good idea, babe!"
                    elif s3_mc.current_partner == "Harry":
                        harry "Good idea, babe!"
                    elif s3_mc.current_partner == "AJ":
                        aj "Good idea, babe!"
                    "[s3_mc.current_partner] busies himself warming [his_her] hands on the fire."
                    "You start moving your fork towards [s3_mc.current_partner]'s plate."
                    elladine "[s3_mc.current_partner]!"
                    "[s3_mc.current_partner]'s head whips round."
                    if s3_mc.current_partner == "Bill":
                        bill "Hey!"
                    elif s3_mc.current_partner == "Camilo":
                        camilo "Hey!"
                    elif s3_mc.current_partner == "Harry":
                        harry "Hey!"
                    elif s3_mc.current_partner == "AJ":
                        aj "Hey!"
                    s3_mc "Damn, I thought I distracted you! I wanted a second helping."

            seb "Don't think I've ever been, like, camping before."
            genevieve "Aw, really?"
            genevieve "I spend a bit of every summer working in a tent."
            seb "Oh yeah. You're, like, a doctor for campers sometimes aren't you?"
            "Genevieve shrugs."
            genevieve "Close enough. Festival goers."
            seb "You must see some right states."
            seb "Mosh pits, fights, and all sorts."
            "Iona stands up and starts dishing out the sausages and beans. Everyone quickly tucks in."
            iona "Yeah, do you ever get a chance to, like, unwind?"
            iona "It must be so hectic."
            genevieve "I love sneaking a cheeky second to go and watch some grime artists."
            genevieve "A good bop always puts me in a good mood."
            genevieve "And during my lunch breaks I go and see some stand up comedians in the comedy tents."
            genevieve "So, yeah. I think I'm pretty lucky in my job."
            genevieve "It's hard work but it's the highlight of the year"

        elif s3e4p3_supper == "Soup":
            "You put a pan on the griddle and pour in half a dozen tins of noodle soup."
            s3_mc "Pass the mugs out, [s3_mc.current_partner]."

            if s3_mc.current_partner == "Bill":
                bill "Sure, babe."
            elif s3_mc.current_partner == "Camilo":
                camilo "Sure, babe."
            elif s3_mc.current_partner == "Harry":
                harry "Sure, babe."
            elif s3_mc.current_partner == "AJ":
                aj "Sure, babe."

            "The soup begins to boil. You smell the air as it rises."
            "Nicky helps stir the pot."
            nicky "It looks about ready."

            if s3_mc.current_partner == "Bill":
                bill "I'll help serve it up."
            elif s3_mc.current_partner == "Camilo":
                camilo "I'll help serve it up."
            elif s3_mc.current_partner == "Harry":
                harry "I'll help serve it up."
            elif s3_mc.current_partner == "AJ":
                aj "I'll help serve it up."

            "[s3_mc.current_partner] ladles soup into everyone's mug."
            nicky "Cheers, [s3_mc.current_partner]."
            elladine "Yeah, thanks for that!"
            nicky "Noodle soup was such a good shout."
            "[s3_mc.current_partner] sits back down beside you, cradling the warm mug in [his_her] hands."

            if s3_mc.current_partner == "Bill":
                bill "Looks like it's going down well with the others."
            elif s3_mc.current_partner == "Camilo":
                camilo "Looks like it's going down well with the others."
            elif s3_mc.current_partner == "Harry":
                harry "Looks like it's going down well with the others."
            elif s3_mc.current_partner == "AJ":
                aj "Looks like it's going down well with the others."

            "[s3_mc.current_partner] slurps up a noodle in the soup."
            "It twists and turns before disappearing into [his_her] mouth."

            # CHOICE
            menu:
                thought "Hmm, noodle soup..."
                "Do a lady and the tramp thing with the noodle":
                    s3_mc "Shall we do a lil slurpin with the noodle thing..."
                    s3_mc "Like they do on Lady and The Tramp?"
                    "You slurp up a noodle and look at [him_her] with twinkly puppy-dog eyes."
                    if s3_mc.current_partner == "Bill":
                        bill "OK. You are the boss!"
                    elif s3_mc.current_partner == "Camilo":
                        camilo "OK. You are the boss!"
                    elif s3_mc.current_partner == "Harry":
                        harry "OK. You are the boss!"
                    elif s3_mc.current_partner == "AJ":
                        aj "OK. You are the boss!"
                    "[s3_mc.current_partner] takes out a long noodle and puts one end in [his_her] mouth."
                    "You take the other end in yours and slurp."
                    "The noodle piece disappears into your mouth and your lips meet."
                    "You only kiss for a moment, but it is a soft and tender one at that."
                    iona "Oh my word, you two. Get a room."
                    iona "Or a tent."
                    s3_mc "Sorry, you lot."
                    s3_mc "We're getting carried away."
                "Tie a knot in a noodle with your tongue":
                    "You slip a noodle into your mouth and your tongue does acrobats inside."
                    s3_mc "Tada!"
                    "You open your mouth and show [s3_mc.current_partner] your tongue knotting abilities."
                    if s3_mc.current_partner == "Bill":
                        bill "Um, ok wow."
                        bill "That's a real tongue twister."
                        "[he_she!c] leans over and whispers into your ear."
                        bill "I hope we get to put that tongue to good use later."
                    elif s3_mc.current_partner == "Camilo":
                        camilo "Um, ok wow."
                        camilo "That's a real tongue twister."
                        "[he_she!c] leans over and whispers into your ear."
                        camilo "I hope we get to put that tongue to good use later."
                    elif s3_mc.current_partner == "Harry":
                        harry "Um, ok wow."
                        harry "That's a real tongue twister."
                        "[he_she!c] leans over and whispers into your ear."
                        harry "I hope we get to put that tongue to good use later."
                    elif s3_mc.current_partner == "AJ":
                        aj "Um, ok wow."
                        aj "That's a real tongue twister."
                        "[he_she!c] leans over and whispers into your ear."
                        aj "I hope we get to put that tongue to good use later."
                    "You wink at [s3_mc.current_partner]."
                    s3_mc "You bet."
                "Just have a good slurp of the soup":
                    "You take an indulgent gulp of the soup. You can feel your whole body warming up."
                    s3_mc "Hmm, this is so tasty!"
                    if s3_mc.current_partner == "Bill":
                        bill "Yeah, it's delicious."
                    elif s3_mc.current_partner == "Camilo":
                        camilo "Yeah, it's delicious."
                    elif s3_mc.current_partner == "Harry":
                        harry "Yeah, it's delicious."
                    elif s3_mc.current_partner == "AJ":
                        aj "Yeah, it's delicious."

            "Nicky helps himself to another mug from the hot bubbling pot."
    else:
        if s3e4p2_decorate_tent or s3e4p2_good_tent:
            "You pass out the sticks and the marshmallows to everyone."
            iona "I feel like I'm a kid again, camping up on the mountains with my aunt and uncle."
            "She pretends to cheers your stick."
            iona "Cheers!"
        else:
            "Elladine passes out the sticks and the marshmallows to everyone."
            iona "I haven't had these since I went camping as a kid! My aunt and uncle would always bring them up the mountains with us. They're lush."
            seb "Yeah, banging choice, Elladine."

        "You reach over to the fire and turn the marshmallow around the stick until it goes crispy golden colour."
        "Out of the corner of your eye you see a small bright flame on the end of [s3_mc.current_partner]'s stick."

        if s3_mc.current_partner == "Bill":
            bill "Ah!"
            "[he_she!c] lets it drop into the pit. The sticky mess gets quickly engulfed by the flames."
            s3_mc "Perfect marshmallow roasting, hun. It's completely obliterated."
            bill "I don't have any technique whatsoever."
            bill "Yours looks amazing."
        elif s3_mc.current_partner == "Camilo":
            camilo "Ah!"
            "[he_she!c] lets it drop into the pit. The sticky mess gets quickly engulfed by the flames."
            s3_mc "Perfect marshmallow roasting, hun. It's completely obliterated."
            camilo "I don't have any technique whatsoever."
            camilo "Yours looks amazing."
        elif s3_mc.current_partner == "Harry":
            harry "Ah!"
            "[he_she!c] lets it drop into the pit. The sticky mess gets quickly engulfed by the flames."
            s3_mc "Perfect marshmallow roasting, hun. It's completely obliterated."
            harry "I don't have any technique whatsoever."
            harry "Yours looks amazing."
        elif s3_mc.current_partner == "AJ":
            aj "Ah!"
            "[he_she!c] lets it drop into the pit. The sticky mess gets quickly engulfed by the flames."
            s3_mc "Perfect marshmallow roasting, hun. It's completely obliterated."
            aj "I don't have any technique whatsoever."
            aj "Yours looks amazing."

        # CHOICE
        menu:
            thought "My marshmallow does look pretty good..."
            "Eat it all in one go":
                "You chomp down on the marshmallow."
                s3_mc "Nomnomnom."
                "The sugary sweet gooey goddess bursts through your mouth as you bite through the crispier parts."
                "It's a little hot, but you bite through the pain."
                if s3_mc.current_partner == "Bill":
                    bill "Nice?"
                    s3_mc "Delicious."
                    bill "That is one lucky marshmallow."
                elif s3_mc.current_partner == "Camilo":
                    camilo "Nice?"
                    s3_mc "Delicious."
                    camilo "That is one lucky marshmallow."
                elif s3_mc.current_partner == "Harry":
                    harry "Nice?"
                    s3_mc "Delicious."
                    harry "That is one lucky marshmallow."
                elif s3_mc.current_partner == "AJ":
                    aj "Nice?"
                    s3_mc "Delicious."
                    aj "That is one lucky marshmallow."
            "Feed [s3_mc.current_partner] the marshmallow":
                "You take the stick out of the fire and poke it towards [s3_mc.current_partner]'s face."
                s3_mc "Want a bite of my marshmallow?"
                if s3_mc.current_partner == "Bill":
                    "[s3_mc.current_partner] looks at it a little suspiciously."
                    bill "I've never actually had them before but, like, yeah sure."
                    bill "Let's try them."
                    "[s3_mc.current_partner] bites the marshmallow off your stick."
                    bill "Oh, okay. That's actually, like kinda weird but good."
                    bill "It's so sticky!"
                elif s3_mc.current_partner == "Camilo":
                    "[s3_mc.current_partner] looks at it a little suspiciously."
                    camilo "I've never actually had them before but, like, yeah sure."
                    camilo "Let's try them."
                    "[s3_mc.current_partner] bites the marshmallow off your stick."
                    camilo "Oh, okay. That's actually, like kinda weird but good."
                    camilo "It's so sticky!"
                elif s3_mc.current_partner == "Harry":
                    "[s3_mc.current_partner] gives you some sexy eyes and licks [his_her] lips."
                    harry "You don't have to ask me twice."
                    "[he_she!c] bites the marshmallow off your stick and licks [his_her] lips."
                    harry "Mmm! Delicious."
                    harry "I love marshmallows."
                elif s3_mc.current_partner == "AJ":
                    "[s3_mc.current_partner] gives you some sexy eyes and licks [his_her] lips."
                    aj "You don't have to ask me twice."
                    "[he_she!c] bites the marshmallow off your stick and licks [his_her] lips."
                    aj "Mmm! Delicious."
                    aj "I love marshmallows."
            "Set it on fire":
                "You leave the marshmallow on the flames."
                s3_mc "And it burns, burns, burns..."
                if s3_mc.current_partner == "Bill":
                    bill "Um..."
                elif s3_mc.current_partner == "Camilo":
                    camilo "Um..."
                elif s3_mc.current_partner == "Harry":
                    harry "Um..."
                elif s3_mc.current_partner == "AJ":
                    aj "Um..."
                s3_mc "The marshmallow of fire!"
                s3_mc "The marshmallow of fire..."
                "It catches fire."
                if s3e1p2_set_fire:
                    "Elladine laughs at you from across the circle."
                    elladine "[s3_name] is at it again."
                    elladine "We know what you're like around fire!"
                "Your marshmallow melts off your stick and is obliterated by the flames."
                if s3_mc.current_partner == "Bill":
                    bill "Proper roasted that one is."
                elif s3_mc.current_partner == "Camilo":
                    camilo "Proper roasted that one is."
                elif s3_mc.current_partner == "Harry":
                    harry "Proper roasted that one is."
                elif s3_mc.current_partner == "AJ":
                    aj "Proper roasted that one is."
                "You both laugh and grab another marshmallow to eat."

        miki "Camping always makes me think of this time I made this, like, marshmallow tower."
        camilo "You what?"
        iona "Come again?"
        miki "Oh, yeah, I did a whole YouTube series."
        miki "It was called Camping With Friends!"
        miki "In one of the videos we had this competition to see who could model the funniest thing out of marshmallows."
        "Camilo starts stacking the marshmallow on top of each other on the stick, trying to fashion his own marshmallow tower."
        "Elladine bursts out laughing."
        elladine "That's a very phallic looking tower indeed."
        camilo "It's proper pink and floppy."
        miki "That's the name of your sex tape, Camilo."
        "Camilo playfully pokes her with the stick of marshmallows."
        seb "Yum."

    "Genevieve looks around the Villa. She seems a little on edge."
    genevieve "I could have sworn I saw something moving over there."
    seb "Could have been the Villa's Ghost."
    genevieve "Er, what?"
    elladine "Ghost story time!"
    "Elladine gets out her phone, turns on the torch, and shines it under her chin."
    "Genevieve looks a little concerned while the others start to make spooky noises."
    elladine "It was a cold and lonely night."
    seb "Pretty sure it's dark and stormy."
    genevieve "I love that cocktail..."
    camilo "That's the name of your sex tape, Viv."
    elladine "Fine! It was a hot and steamy night..."

    if s3_mc.current_partner == "Bill":
        bill "That's more like it..."
    elif s3_mc.current_partner == "Camilo":
        camilo "That's more like it..."
    elif s3_mc.current_partner == "Harry":
        harry "That's more like it..."
    elif s3_mc.current_partner == "AJ":
        aj "That's more like it..."
        
    elladine "The Islanders were just settling down to a nice cup of..."

    # CHOICE
    menu:
        s3_mc "A nice cup of..."
        "Hot chocolate":
            $ s3e4p3_drink = "hot chocolate"
            miki "Oh, damn you [s3_name]."
            miki "Now I'm craving a hot chocolate."
            iona "Yeah, me too."
            elladine "Miki. Focus."
        "Fear of my enemies":
            $ s3e4p3_drink = "fear"
            elladine "A cup of fear?"
            s3_mc "Specifically, the fear of my enemies."
            "Seb and Iona snort loudly with laughter."
            s3_mc "What? I thought this was meant to be a scary story."
            iona "You can't cup fear."
            seb "I don't know."
            seb "If I leave my cups out for too long they start wearing fuzzy green jackets."
            seb "And that can be a little haunting."
            elladine "Ugh. Grim, but fine."
        "Kombucha":
            $ s3e4p3_drink = "kombucha"
            iona "Kombucha?"
            s3_mc "Yeah, that can be quite a scary drink to be honest because you don't know if you're going to like it."
            seb "I second that."
            elladine "OK..."

    elladine "The Islanders were just settling down to a nice cup of fear/hot chocolate/Kombucha."
    elladine "When all of a sudden..."
    "Seb jumps up."
    seb "There was a shiny demon!"
    "He points to the grass."
    seb "In the middle of the lawn."
    "Genevieve squeals."
    genevieve "Ah!"
    iona "That's not very ghostly though."
    genevieve "Demons are scary."
    seb "Yeah, and it's a hot and steamy night."
    seb "Perfect climate for a wild demon to appear."
    iona "I guess that explains the shininess."
    elladine "OK, all of a sudden a shiny demon popped up."
    harry "And it said..."

    # CHOICE
    menu:
        thought "What did the demon say to us?"
        "Welcome to Clown Island":
            camilo "Aw, I love clowns."
            s3_mc "Yeah, and on Clown Island do you know what we eat for breakfast, lunch, and dinner?"
            genevieve "Wha.. what?"
            s3_mc "Souls."
            s3_mc "I think it might be soul eating time."
            s3_mc "Said the shiny demon."
        "I'm seeking fresh souls":
            s3_mc "I'm seeking fresh souls, said the shiny demon."
            "Everyone is silent except the crackle of the fire."
            "Miki stands up and shouts."
            miki "Back off, you evil shiny demon."
            miki "You're not taking my friend's souls."
            genevieve "Yeah! You tell em'."
            if s3_mc.current_partner == "Bill":
                miki "The demon just grinned and said 'I may have sinned but there's no need to push me around.'"
                miki "And then, the demon latched onto [s3_mc.current_partner] and said..."
                miki "I've got [him_her] first so you can do your worst."
                miki "[he_she!c]'s going underground!"
            elif s3_mc.current_partner == "Camilo":
                iona "The demon just grinned and said 'I may have sinned but there's no need to push me around.'"
                iona "And then, the demon latched onto [s3_mc.current_partner] and said..."
                iona "I've got [him_her] first so you can do your worst."
                iona "[he_she!c]'s going underground!"
            elif s3_mc.current_partner == "Harry":
                genevieve "The demon just grinned and said 'I may have sinned but there's no need to push me around.'"
                genevieve "And then, the demon latched onto [s3_mc.current_partner] and said..."
                genevieve "I've got [him_her] first so you can do your worst."
                genevieve "[he_she!c]'s going underground!"
            elif s3_mc.current_partner == "AJ":
                seb "The demon just grinned and said 'I may have sinned but there's no need to push me around.'"
                seb "And then, the demon latched onto [s3_mc.current_partner] and said..."
                seb "I've got [him_her] first so you can do your worst."
                seb "[he_she!c]'s going underground!"
            "You and [s3_mc.current_partner] look at [s3_3rd_girl_options[s3_mc.current_partner]], a little afraid."
            elladine "Go along with it, [s3_mc.current_partner]."
        "Hey, I'm the new Islander!":
            s3_mc "Hi, I'm the new Islanders, said the demon."
            if s3_mc.current_partner == "Bill":
                miki "Now that is terrifying."
                "[s3_3rd_girl_options[s3_mc.current_partner]] stands up."
                miki "Yeah, and it's come to steal [s3_mc.current_partner]'s soul from [s3_name]!"
            elif s3_mc.current_partner == "Camilo":
                iona "Now that is terrifying."
                "[s3_3rd_girl_options[s3_mc.current_partner]] stands up."
                iona "Yeah, and it's come to steal [s3_mc.current_partner]'s soul from [s3_name]!"
            elif s3_mc.current_partner == "Harry":
                genevieve "Now that is terrifying."
                "[s3_3rd_girl_options[s3_mc.current_partner]] stands up."
                genevieve "Yeah, and it's come to steal [s3_mc.current_partner]'s soul from [s3_name]!"
            elif s3_mc.current_partner == "AJ":
                seb "Now that is terrifying."
                "[s3_3rd_girl_options[s3_mc.current_partner]] stands up."
                seb "Yeah, and it's come to steal [s3_mc.current_partner]'s soul from [s3_name]!"
            "[s3_3rd_girl_options[s3_mc.current_partner]] winks at you cheekily."
            s3_mc "No, not [s3_mc.current_partner]!"

    if s3_mc.current_partner == "Bill":
        bill "Save me, [s3_name]."
    elif s3_mc.current_partner == "Camilo":
        camilo "Save me, [s3_name]."
    elif s3_mc.current_partner == "Harry":
        harry "Save me, [s3_name]."
    elif s3_mc.current_partner == "AJ":
        aj "Save me, [s3_name]."

    # CHOICE
    menu:
        thought "[s3_mc.current_partner] soul is about to be stolen by the demon!"
        "Cling on to him tightly":
            $ s3_mc.like(s3_mc.current_partner)
            "You quickly grab onto [s3_mc.current_partner]."
            s3_mc "I'll protect your soul!"
            miki "Aw, you're like, soul mates."
            if s3_mc.current_partner == "Bill":
                bill "Thanks, [s3_name]."
                "[he_she!c] hugs you back, tightly."
                bill "And by the power of a cuddle the demon was shattered into a million pieces!"
            elif s3_mc.current_partner == "Camilo":
                camilo "Thanks, [s3_name]."
                "[he_she!c] hugs you back, tightly."
                camilo "And by the power of a cuddle the demon was shattered into a million pieces!"
            elif s3_mc.current_partner == "Harry":
                harry "Thanks, [s3_name]."
                "[he_she!c] hugs you back, tightly."
                harry "And by the power of a cuddle the demon was shattered into a million pieces!"
            elif s3_mc.current_partner == "AJ":
                aj "Thanks, [s3_name]."
                "[he_she!c] hugs you back, tightly."
                aj "And by the power of a cuddle the demon was shattered into a million pieces!"
            iona "A demon shattering cuddle?"
            iona "Really?"
        "Offer [s3_mc.current_partner] for a price":
            $ s3_mc.dislike(s3_mc.current_partner)
            s3_mc "Sorry, shiny demon. You can't just have [s3_mc.current_partner]."
            "[s3_mc.current_partner] smiles at you."
            s3_mc "Nothing is free these days."
            s3_mc "You've got to pay."
            s3_mc "I want to make a profit."
            "[s3_mc.current_partner]'s face drops into a frown."
            if s3_mc.current_partner == "Bill":
                bill "Oh."
            elif s3_mc.current_partner == "Camilo":
                camilo "Oh."
            elif s3_mc.current_partner == "Harry":
                harry "Oh."
            elif s3_mc.current_partner == "AJ":
                aj "Oh."
            seb "Looks like your soul's about to be sold, [s3_mc.current_partner]."
            seb "But the demon has forgotten his pin and [s3_mc.current_partner] costs more than the limit on contactless."
            seb "So the demon sulks away back to the underworld, sparing [s3_mc.current_partner]'s soul for another day."
            if s3_mc.current_partner == "Bill":
                bill "Phew."
            elif s3_mc.current_partner == "Camilo":
                camilo "Phew."
            elif s3_mc.current_partner == "Harry":
                harry "Phew."
            elif s3_mc.current_partner == "AJ":
                aj "Phew."
        "Throw the cup of [s3e4p3_drink] on it":
            s3_mc "I'll throw my cup of [s3e4p3_drink] over the demon."
            if s3e4p3_drink == "fear":
                $ s3e4p3_drink = "fear from [s3_name]'s enemies"
            miki "The metaphorical cup of [s3e4p3_drink] makes the demon flea into the hot and steamy night."

    "Genevieve cheers and claps excitedly."
    genevieve "Yay!"
    genevieve "Be gone, shiny demon!"
    seb "Unfortunately, the shiny demon left behind a ghostly presence..."
    seb "Which will haunt the Villa for years and years to come."
    "The wind picks up a little causing the shadows of the dancing flames to flicker."

    # CHOICE
    menu:
        thought "The tale is over..."
        "Well, that wasn't a very scary story":
            iona "Yeah, I agree."
            iona "There is nothing scary about a villain that just pops up without any kind of build up."
            iona "It is the anticipation of it that makes it frightening."
            if s3e4p3_drink == "fear from [s3_name]'s enemies":
                $ s3e4p3_drink = "fear"
            elladine "We were drinking a cup of [s3e4p3_drink]! That was the setup."
            iona "Terrifying."
            seb "Watch out..."
            seb "Iona Hitchcock is about."
            "Iona rolls her eyes."
        "What happens next? I want a sequel!":
            elladine "Yeah! We could do a whole novel about it."
            miki "Write the book and then make it into three separate movies ultimate gains."
            elladine "I'm too sleepy for that."
        "Can we get into the tents already?":
        "[s3_mc.current_partner] raises [his_her] eyebrows in surprise. Miki bursts out laughing."
            miki "Did a story about a shiny devil make you feel..."
            miki "Erotically charged?"
            "You wink?"
            s3_mc "Nah, I'm just feeling hot and steamy tonight."

    "You hear a light snoozing. Nicky has dozed off on Elladine's lap."
    camilo "Aw, he's so cute when he's sleeping."
    iona "I'm knackered too."
    genevieve "But it's getting pretty dark..."
    elladine "Yeah, bed time, I think."
    genevieve "Hm, yeah."
    "She looks around at the empty loungers."
    harry "Genevieve, the demon isn't actually real."

    if s3_mc.current_partner != "Harry":
        harry "It'll be fine, hun, I'm right with you! "
        "Genevieve begrudgingly follows Harry into their tent."
    
    if s3_mc.current_partner == "Bill":
        miki "I'm actually going to go and sleep inside, I think."
        bill "Are you sure you're OK?"
        miki "Yeah, no way I'm sleeping in a tent by myself."
        s3_mc "OK hun, whatever works for you."
        "[s3_3rd_girl_options[s3_mc.current_partner]] heads inside the Villa."
    elif s3_mc.current_partner == "Camilo":
        iona "I'm actually going to go and sleep inside, I think."
        camilo "Are you sure you're OK?"
        iona "Yeah, no way I'm sleeping in a tent by myself."
        s3_mc "OK hun, whatever works for you."
        "[s3_3rd_girl_options[s3_mc.current_partner]] heads inside the Villa."
    elif s3_mc.current_partner == "Harry":
        genevieve "I think I'm going to skip the camp out and sleep inside."
        genevieve "Don't fancy sleeping in a tent on my own in the dark outside."
        aj "You can share with me and Seb."
        aj "We're not going to be making anything go bump in the night."
        "AJ laughs. Seb rolls his eyes."
        seb "Truth to be told, yeah, if you want to share with us you totally can."
        seb "It might be squashed but it beats sleeping the Villa on your own."
        "Genevieve puts on a brace face."
        genevieve "Alright, alright."
        genevieve "That's real sweet of you guys."
        "They all squeeze into one tent together."
    elif s3_mc.current_partner == "AJ":
        seb "I'm actually going to go and sleep inside, I think."
        aj "Are you sure you're OK?"
        seb "Yeah, no way I'm sleeping in a tent by myself."
        s3_mc "OK hun, whatever works for you."
        "[s3_3rd_girl_options[s3_mc.current_partner]] heads inside the Villa."


    if s3_mc.current_partner == "Bill":
        bill "Right, shall we get in our tent?"
    elif s3_mc.current_partner == "Camilo":
        camilo "Right, shall we get in our tent?"
    elif s3_mc.current_partner == "Harry":
        harry "Right, shall we get in our tent?"
    elif s3_mc.current_partner == "AJ":
        aj "Right, shall we get in our tent?"

    if s3e4p2_give_rock:
        if s3_mc.current_partner == "Bill":
            bill "Sorry, our new home."
            "[s3_mc.current_partner] opens [his_her] clenched fist and reveals the little pebble."
            s3_mc "Aw, you kept our keys!"
            bill "Yeah, of course."
            bill "Can't have any shiny demons trying to break in, can we?"
        elif s3_mc.current_partner == "Camilo":
            camilo "Sorry, our new home."
            "[s3_mc.current_partner] opens [his_her] clenched fist and reveals the little pebble."
            s3_mc "Aw, you kept our keys!"
            camilo "Yeah, of course."
            camilo "Can't have any shiny demons trying to break in, can we?"
        elif s3_mc.current_partner == "Harry":
            harry "Sorry, our new home."
            "[s3_mc.current_partner] opens [his_her] clenched fist and reveals the little pebble."
            s3_mc "Aw, you kept our keys!"
            harry "Yeah, of course."
            harry "Can't have any shiny demons trying to break in, can we?"
        elif s3_mc.current_partner == "AJ":
            aj "Sorry, our new home."
            "[s3_mc.current_partner] opens [his_her] clenched fist and reveals the little pebble."
            s3_mc "Aw, you kept our keys!"
            aj "Yeah, of course."
            aj "Can't have any shiny demons trying to break in, can we?"

        s3_mc "No way, not in our home."
        "[s3_mc.current_partner] unzips the tent and you clamber into your new home for the night."

    if s3e4p2_say_dirty:
        s3_mc "Sure, let's get in there and get filthy."
        "[he_she!c] unzips the tent. You take [s3_mc.current_partner]'s hand and lead [him_her] in."

    if s3e4p2_decorate_tent or s3e4p2_good_tent:
        "You and [s3_mc.current_partner] huddle in the tent. It's super cosy."
    else:
        "You and [s3_mc.current_partner] huddle in the tent. It's a bit chilly."

    scene s3-inside-tent-standard-night with dissolve
    $ on_screen = []

    if s3e4p2_decorate_tent:
        if s3_mc.current_partner == "Bill":
            bill "It looks like someone is serving up some camping eleganza."
            bill "You did such a good job of doing it up."
        elif s3_mc.current_partner == "Camilo":
            camilo "It looks like someone is serving up some camping eleganza."
            camilo "You did such a good job of doing it up."
        elif s3_mc.current_partner == "Harry":
            harry "It looks like someone is serving up some camping eleganza."
            harry "You did such a good job of doing it up."
        elif s3_mc.current_partner == "AJ":
            aj "It looks like someone is serving up some camping eleganza."
            aj "You did such a good job of doing it up."
        s3_mc "Thanks babe."
    else:
        if s3_mc.current_partner == "Bill":
            bill "We're serving camping realness in here."
        elif s3_mc.current_partner == "Camilo":
            camilo "We're serving camping realness in here."
        elif s3_mc.current_partner == "Harry":
            harry "We're serving camping realness in here."
        elif s3_mc.current_partner == "AJ":
            aj "We're serving camping realness in here."

    thought "Hmm, we've got sleeping bags and a duvet..."

    # CHOICE
    menu:
        thought "Do I want to cuddle up to [s3_mc.current_partner] or put some distance between us?"
        "Spread out the duvet and cuddle":
            "You throw the duvet across you both."
            "[s3_mc.current_partner] quickly snuggles up to you, enveloping you in [his_her] arms."
            if s3_mc.current_partner == "Bill":
                bill "Huddle close before we get too cold."
            elif s3_mc.current_partner == "Camilo":
                camilo "Huddle close before we get too cold."
            elif s3_mc.current_partner == "Harry":
                harry "Huddle close before we get too cold."
            elif s3_mc.current_partner == "AJ":
                aj "Huddle close before we get too cold."
        "Get in the sleeping bag on your own":
            "You get in your sleeping bag. [s3_mc.current_partner] does the same."
        "Zip two sleeping bags together and share":
            s3_mc "Let's zip two sleeping bags together."
            "You fiddle with the zips of the two bags until they're joined as one big bag."
            if s3_mc.current_partner == "Bill":
                bill "You think we'll fit?"
                s3_mc "Of course!"
                "You slide into the sleeping bag beside [him_her]. It's not very roomy, but it's super cosy."
                bill "OK, this is comfier than I thought."
            elif s3_mc.current_partner == "Camilo":
                camilo "You think we'll fit?"
                s3_mc "Of course!"
                "You slide into the sleeping bag beside [him_her]. It's not very roomy, but it's super cosy."
                camilo "OK, this is comfier than I thought."
            elif s3_mc.current_partner == "Harry":
                harry "You think we'll fit?"
                s3_mc "Of course!"
                "You slide into the sleeping bag beside [him_her]. It's not very roomy, but it's super cosy."
                harry "OK, this is comfier than I thought."
            elif s3_mc.current_partner == "AJ":
                aj "You think we'll fit?"
                s3_mc "Of course!"
                "You slide into the sleeping bag beside [him_her]. It's not very roomy, but it's super cosy."
                aj "OK, this is comfier than I thought."

    "You lay beside each other, listening to the chirping of crickets."
    if s3_mc.current_partner == "Bill":
        bill "Honestly, I can't get over how, like, close we've gotten in such a short time."
    elif s3_mc.current_partner == "Camilo":
        camilo "Honestly, I can't get over how, like, close we've gotten in such a short time."
    elif s3_mc.current_partner == "Harry":
        harry "Honestly, I can't get over how, like, close we've gotten in such a short time."
    elif s3_mc.current_partner == "AJ":
        aj "Honestly, I can't get over how, like, close we've gotten in such a short time."

    # CHOICE
    menu: 
        thought "[s3_mc.current_partner] thinks we're getting closer!"
        "Yeah, I agree, it's lovely":
            if s3_mc.current_partner == "Bill":
                bill "It's like we've known each other for ages, isn't it?"
            elif s3_mc.current_partner == "Camilo":
                camilo "It's like we've known each other for ages, isn't it?"
            elif s3_mc.current_partner == "Harry":
                harry "It's like we've known each other for ages, isn't it?"
            elif s3_mc.current_partner == "AJ":
                aj "It's like we've known each other for ages, isn't it?"
            s3_mc "Totally."
        "We could get even closer...":
            if s3_mc.current_partner == "Bill":
                bill "Oh, yeah?"
                "[s3_mc.current_partner] winks at you."
                bill "I'm sure that could be arranged."
            elif s3_mc.current_partner == "Camilo":
                camilo "Oh, yeah?"
                "[s3_mc.current_partner] winks at you."
                camilo "I'm sure that could be arranged."
            elif s3_mc.current_partner == "Harry":
                harry "Oh, yeah?"
                "[s3_mc.current_partner] winks at you."
                harry "I'm sure that could be arranged."
            elif s3_mc.current_partner == "AJ":
                aj "Oh, yeah?"
                "[s3_mc.current_partner] winks at you."
                aj "I'm sure that could be arranged."
        "This tent is pretty cramped":
            if s3_mc.current_partner == "Bill":
                bill "Yeah, I guess it is!"
            elif s3_mc.current_partner == "Camilo":
                camilo "Yeah, I guess it is!"
            elif s3_mc.current_partner == "Harry":
                harry "Yeah, I guess it is!"
            elif s3_mc.current_partner == "AJ":
                aj "Yeah, I guess it is!"

    if s3_mc.current_partner == "Bill":
        bill "It's only been a few days and we're already on a sort of holiday away from home."
        s3_mc "How?"
        bill "That's what camping feels like to me, even if it's in your back garden."
        bill "We're literally already on holiday...so, it's like we're on a holiday away from a holiday!"
        "[s3_mc.current_partner] smiles at you, blushing a little."
        bill "It's so funny that this is the first time we've, like, actually slept alone."
    elif s3_mc.current_partner == "Camilo":
        camilo "It's only been a few days and we're already on a sort of holiday away from home."
        s3_mc "How?"
        camilo "That's what camping feels like to me, even if it's in your back garden."
        camilo "We're literally already on holiday...so, it's like we're on a holiday away from a holiday!"
        "[s3_mc.current_partner] smiles at you, blushing a little."
        camilo "It's so funny that this is the first time we've, like, actually slept alone."
    elif s3_mc.current_partner == "Harry":
        harry "It's only been a few days and we're already on a sort of holiday away from home."
        s3_mc "How?"
        harry "That's what camping feels like to me, even if it's in your back garden."
        harry "We're literally already on holiday...so, it's like we're on a holiday away from a holiday!"
        "[s3_mc.current_partner] smiles at you, blushing a little."
        harry "It's so funny that this is the first time we've, like, actually slept alone."
    elif s3_mc.current_partner == "AJ":
        aj "It's only been a few days and we're already on a sort of holiday away from home."
        s3_mc "How?"
        aj "That's what camping feels like to me, even if it's in your back garden."
        aj "We're literally already on holiday...so, it's like we're on a holiday away from a holiday!"
        "[s3_mc.current_partner] smiles at you, blushing a little."
        aj "It's so funny that this is the first time we've, like, actually slept alone."

    # CHOICE
    menu:
        thought "This is the first time me and [s3_mc.current_partner] have slept alone together!"
        "It's about time, right?":
            if s3_mc.current_partner == "Bill":
                bill "Totally."
            elif s3_mc.current_partner == "Camilo":
                camilo "Totally."
            elif s3_mc.current_partner == "Harry":
                harry "Totally."
            elif s3_mc.current_partner == "AJ":
                aj "Totally."
        "We should take advantage of it":
            if s3_mc.current_partner == "Bill":
                bill "You think?"
            elif s3_mc.current_partner == "Camilo":
                camilo "You think?"
            elif s3_mc.current_partner == "Harry":
                harry "You think?"
            elif s3_mc.current_partner == "AJ":
                aj "You think?"
            s3_mc "For sure."
        "It feels weird without the others!":
            if s3_mc.current_partner == "Bill":
                bill "Yeah..."
                bill "Isn't it weird how we now find it weird not having a bunch of other people sleeping next to you?"
            elif s3_mc.current_partner == "Camilo":
                camilo "Yeah..."
                camilo "Isn't it weird how we now find it weird not having a bunch of other people sleeping next to you?"
            elif s3_mc.current_partner == "Harry":
                harry "Yeah..."
                harry "Isn't it weird how we now find it weird not having a bunch of other people sleeping next to you?"
            elif s3_mc.current_partner == "AJ":
                aj "Yeah..."
                aj "Isn't it weird how we now find it weird not having a bunch of other people sleeping next to you?"
            s3_mc "Yeah, totally."

    if s3e4p3_wear_shirt:
        "[s3_mc.current_partner] gently strokes the sleeve of [his_her] top."
        if s3_mc.current_partner == "Bill":
            bill "By the way, you look so cute in my top."
            s3_mc "Thanks for lending it to me."
            bill "Any day."
            bill "You wear it better than me."
            bill "Are you sleepy?"
            bill "Or would you like to stay up talking and maybe..."
            "He shakes the tent a little."
            bill "Test to see if this tent is as strong as it looks?"
        elif s3_mc.current_partner == "Camilo":
            camilo "By the way, you look so cute in my top."
            s3_mc "Thanks for lending it to me."
            camilo "Any day."
            camilo "You wear it better than me."
            camilo "Are you sleepy?"
            camilo "Or shall we chill out in this tent.."
            camilo "And maybe take advantage of this alone time?"
        elif s3_mc.current_partner == "Harry":
            harry "By the way, you look so cute in my top."
            s3_mc "Thanks for lending it to me."
            harry "Any day."
            harry "You wear it better than me."
            harry "Are you sleepy?"
            harry "Or do you maybe want to..."
            "Harry raises his eyebrow."
            harry "Get up close and personal?"
        elif s3_mc.current_partner == "AJ":
            aj "By the way, you look so cute in my top."
            s3_mc "Thanks for lending it to me."
            aj "Any day."
            aj "You wear it better than me."
            aj "Are you sleepy?"
            aj "Or do you want to stay up all night talking and..."
            aj "Doing other stuff?"

    # CHOICE
    menu:
        thought "Do I want to go to sleep or spend some time with [s3_mc.current_partner]?"
        "Stay up with [s3_mc.current_partner]":
            $ s3e4p3_stay_up = True
            $ s3_mc.like(s3_mc.current_partner)
            jump s3e4p3_stay_up
        "Go to sleep":
            s3_mc "I'm so tired."
            s3_mc "I think I'll just go to sleep."
            if s3_mc.current_partner == "Bill":
                bill "That's fair enough!"
                bill "It's pretty late."
                bill "Night, gorgeous."
            elif s3_mc.current_partner == "Camilo":
                camilo "That's fair enough!"
                camilo "It's pretty late."
                camilo "Night, gorgeous."
            elif s3_mc.current_partner == "Harry":
                harry "That's fair enough!"
                harry "It's pretty late."
                harry "Night, gorgeous."
            elif s3_mc.current_partner == "AJ":
                aj "That's fair enough!"
                aj "It's pretty late."
                aj "Night, gorgeous."
            "You both settle down and drift off to sleep."

            jump s3e4p3_ending

label s3e4p3_stay_up:
    s3_mc "We can stay up!"

    if s3_mc.current_partner == "Bill":
        bill "Cool."
        bill "We can have a proper good chat."
        bill "It's hard chatting at night with loads of people in the same room, isn't it?"
    elif s3_mc.current_partner == "Camilo":
        camilo "Cool."
        camilo "We can have a proper good chat."
        camilo "It's hard chatting at night with loads of people in the same room, isn't it?"
    elif s3_mc.current_partner == "Harry":
        harry "Cool."
        harry "We can have a proper good chat."
        harry "It's hard chatting at night with loads of people in the same room, isn't it?"
    elif s3_mc.current_partner == "AJ":
        aj "Cool."
        aj "We can have a proper good chat."
        aj "It's hard chatting at night with loads of people in the same room, isn't it?"
    s3_mc "Yeah, for sure."
    "You huddle closer to [s3_mc.current_partner]."

    if s3_mc.current_partner == "Bill":
        call s3e4p3_stay_up_bill
    elif s3_mc.current_partner == "Camilo":
        call s3e4p3_stay_up_camilo
    elif s3_mc.current_partner == "Harry":
        call s3e4p3_stay_up_harry
    elif s3_mc.current_partner == "AJ":
        call s3e4p3_stay_up_aj

    "You can hear giggling from the other tents. Someone moans a little too loud."

    if s3_mc.current_partner == "Bill":
        bill "Sounds like the others are getting it on in their tents!"
    elif s3_mc.current_partner == "Camilo":
        camilo "This really reminds me of the times I used to pitch a tent with my girl in my back garden to get away from all my family."
        "He laughs, raising his voice a little so the other Islanders can hear him."
        camilo "Except my family weren't all around me getting it on as well."
        "Someone laughs. Someone else moans."
    elif s3_mc.current_partner == "Harry":
        harry "Sounds like the others are getting it on in their tents!"
    elif s3_mc.current_partner == "AJ":
        aj "Sounds like the others are getting it on in their tents!"

    "[s3_mc.current_partner] grins."
    
    # CHOICE
    menu:
        thought "Should me and [s3_mc.current_partner] do bits?"
        "Nah, we should just cuddle":
            if s3_mc.current_partner == "Bill":
                bill "Come here."
                "[he_she!c] wraps [his_her] arms around you, spooning you close."
                bill "I love a good cuddle."
                bill "You're by far the best person I've got to spoon."
                s3_mc "Oh, really?"
                bill "Yeah."
                bill " [s3_name]:The Best Spooner is what should be on your CV."
            elif s3_mc.current_partner == "Camilo":
                camilo "Come here."
                "[he_she!c] wraps [his_her] arms around you, spooning you close."
                camilo "I love a good cuddle."
                camilo "You're by far the best person I've got to spoon."
                s3_mc "Oh, really?"
                camilo "Yeah."
                camilo " [s3_name]:The Best Spooner is what should be on your CV."
            elif s3_mc.current_partner == "Harry":
                harry "Come here."
                "[he_she!c] wraps [his_her] arms around you, spooning you close."
                harry "I love a good cuddle."
                harry "You're by far the best person I've got to spoon."
                s3_mc "Oh, really?"
                harry "Yeah."
                harry " [s3_name]:The Best Spooner is what should be on your CV."
            elif s3_mc.current_partner == "AJ":
                aj "Come here."
                "[he_she!c] wraps [his_her] arms around you, spooning you close."
                aj "I love a good cuddle."
                aj "You're by far the best person I've got to spoon."
                s3_mc "Oh, really?"
                aj "Yeah."
                aj " [s3_name]:The Best Spooner is what should be on your CV."
            "You smile and snuggle further into [s3_mc.current_partner]."

"Yes! Get on top of [him_her] and do bits":
"You straddle [s3_mc.current_partner] and interlock your fingers with [his_her], gently holding [him_her] down on the tent ground."
harry "Easy tiger!"
"Harry balances up on his elbows and leans up to kiss you."
"You lean down to his level and kiss his neck."
harry "You're so sexy."
"Bill gestures for you to come down to him and kiss him."
"His hands squeeze your thighs as you kiss his neck."
bill "I love having you on top of me like this."
"Camilo pulls you close to him and kisses you."
"His hands stroke your lower waist."
camilo "Damn. Girl, you are so hot."
"AJ tugs lightly on your wrists, pulling you closer to her."
"She kisses you urgently."
aj "I can't get enough of you."
"The cool air doesn't stop you from stripping off."
B/H/Cam/aj "Woah."
"As you move your hips [s3_mc.current_partner]'s breath quickens."
B/H/Cam/aj "Oh, woah."
Choiceseb "I should..."
-Go lower
-Go higher
-Go deeper
You move slowly on top of [s3_mc.current_partner], trying not to dismantle the tent in the process.

Outside, you hear the rustling of the other tents.
Bill pulls you closer and moans into your ear.
bill "Let's give the others a proper show."
He rolls you onto your back and kisses your neck.
harry "Oops."
harry "I'll try and be a little bit quieter..."
He kisses you, hard. 
camilo "I wish it was just us right now."
camilo "I would be so much louder if it was."
aj "This is so hot."
aj "Don't let anything distract you."
You start to explore [his_her] body with your lips and tongue.
[s3_mc.current_partner] moans slightly louder than you expected.
seb "Can someone turn it down?"
elladine "Yeah, some of us are trying to sleep!"
(MC coupled with one of the boys):
elladine "Can someone turn it down?"
elladine "Some of us are trying to sleep!"
iona "Not all of us."
You roll off [s3_mc.current_partner] and lie back in a fit of laughter.
B/H/Cam/aj "Oops."
You cuddle up next to each other.
[s3_mc.current_partner]'s heat radiates around you.
B/H/Cam/aj "That was pretty intense."
s3_mc "Because we're in tents?"
B/H/Cam/aj "Yeah. I know. Weak."
You roll your eyes and hit [him_her] with a pillow.
B/H/Cam/aj "Nah, I'm kidding."
[s3_mc.current_partner] sounds a little out of breath.
B/H/Cam/aj "No jokes about that."
B/H/Cam/aj "That was amazing."
s3_mc "I know, I try."
[s3_mc.current_partner] rolls onto his side and kisses your cheek.
B/H/Cam/aj "You don't even have to try, babe."
B/H/Cam/aj "You're always amazing."

    jump s3e4p3_ending

label s3e4p3_stay_up_bill:
"Bill takes your hands in his and pulls you towards him, so close you can count his eyelashes."

    # CHOICE
    menu:
        thought "I'm so close to Bill..."
        "Kiss him fast":
            "You lean in and press your lips against his, clutching at his stubbled jaw."
            "He returns the kiss with the same passion as his hands run down your body."
        "Kiss him slow":
            "You brush your lips against his. He leans into it, but you pull back until you're only just maintaining contact."
            "You control the pace and he follows your lead until you're kissing fully and deeply. His hands run down your body."
        "Cuddle up to him":
            "You turn and press your head into his chest. It's warm and firm and you can hear his heart beating."
            "Bill lightly strokes your arm with his hand."

    s3_mc "I like your hands."
    bill "Grew them myself."
    s3_mc "Good job. They feel very...reliable."
    bill "They've gotta be. I'm a roofer, after all."
    bill "And I like to make stuff."
    bill "My granddad's a cabinet maker, and we sometimes make furniture together."
    s3_mc "Like, from scratch?"
    bill "Yup. We'd just finished a piano stool before I came here."
    bill "He knows a guy, who knows a guy, who gets decent timber for cheap. It's great to be around him."

    # CHOICE
    menu:
        thought "Bill makes furniture with his grandad..."
        "That's really sweet":
            "You stroke his fingers with yours."
            s3_mc "I think it's adorable."
            bill "I don't know about that, but I do really enjoy spending time with the old fella."
            bill "And it's not just that he's got good stories or bants, or whatever."
            bill "He's a solid person."
            bill "His head's bursting with common sense."
            s3_mc "That's exactly what I was picturing."
            s3_mc "I can imagine you being like that when you're old."
            s3_mc "Dispensing wisdom to the young'uns."
            "He smiles broadly."
            s3_mc "That's the dream, innit?"
        "What else can you do with your hands?":
            "You stroke his fingers with yours."
            s3_mc "What else can you do with your hands?"
            bill "Is there something in particular you want me to do?"
            "You wink."
            s3_mc "There might be."
            bill "Just to be clear, we're talking about sex, right?"
            s3_mc "You're so upfront, I love it."
            s3_mc "Yes, we're talking about sex."
            "He grins."
            bill "Good to know we're on the same page."
        "Does your dad ever help?":
            bill "My dad's not much of a woodworker. He'd sometimes take me round to his plumbing jobs, though."
            bill "He and my grandad have these big long arguments about whether plumbing or carpentry was harder."
            bill "It's all in good fun. Just their way of saying 'I love you'."
            s3_mc "So, that's where you get it from."

    s3_mc "What's your favourite thing you've ever made?"
    "He thinks about it for a moment."
    bill "Let me see..."
    bill "It'd have to be the spice rack we made."
    s3_mc "Erm...it took two of you to make a spice rack?"
    bill "It was the first thing my granddad showed me how to make. We didn't used to speak much before that."
    bill "He really warmed up showing me all the proper tools and stuff."
    bill "The spice rack is useless, obviously, but it was all about spending time together. We're proper mates now."
    s3_mc "That's lovely. But what did you mean by 'it's useless'?"
    bill "Well, most spices are unnecessary, you know?"
    bill "All you need is salt, pepper, curry powder, oregano and cinnamon. Everything else is just showing off."

    # CHOICE
    menu:
        thought "Bill thinks most spices are unnecessary..."
        "Agree with him":
            s3_mc "Tell me about it. Everything these days is cumin this, fennel that. It's just not necessary."
            bill "I knew you'd get it!"
            bill "Wait, are you taking the piss?"
            s3_mc "Not at all!"
            bill "Oh, good."
        "Argue the point":
            s3_mc "Doesn't that exclude like 90% of the world's cuisine?"
            bill "Might do, but it works for me."
            s3_mc "But you could be really missing out!"
            bill "It's never really bothered me..."
            s3_mc "One day I'm going to try and change your mind."
            s3_mc "There are some cracking spices out there."
            "He thinks for a moment. You can almost see the wrestling match going on inside his head."
            bill "Yeah, sure. Why not?"
            s3_mc "Great."
            bill "I wouldn't do this for anyone else, you know?"
        "Laugh it off":
            s3_mc "You and your opinions!"
            s3_mc "I feel like a fish that doesn't see the bait until it's been hooked."
            s3_mc "Or maybe it's something else that's got me hooked."
            "You put your arms around him."

    "He puts his arms around you and gives you a squeeze."

label s3e4p3_stay_up_harry:
    "Harry smoothes out his hair with one hand. His biceps bulge pleasingly."
    harry "Alone again..."

    # CHOICE
    menu:
        thought "Alone with Harry..."
        "Kiss him":
            "You close the distance between you and brush your fingers down the side of his face."
            harry "H-"
            "Before he can start talking, you put a finger to his lips, then lean in and kiss him."
            "His arms envelop you. You melt into each other's lips and for a few moments, that's all there is."
        "Tell him to kiss you":
            "You gaze at him seductively."
            s3_mc "Kiss me."
            "He wastes no time in moving towards you, kissing you hard on the mouth. He softly bites your lower lip."
            "His arms envelop you. You melt into each other's lips and for a few moments, that's all there is."
        "Admire his body a bit more":
            "He chuckles softly."
            harry "What?"
            s3_mc "Just admiring the view."
            "Harry smiles confidently and flexes a little more."
            "You fan yourself."
            s3_mc "Could you be any hotter?"

    harry "When I'm with you, I feel like the coolest guy in the world."
    harry "Like a super-spy. 'The name's Zhōng. Harry Zhōng.'"

    # CHOICE
    menu:
        thought "Harry feels like a secret agent when he's with me..."
        "You don't have the snappiest name for it":
            # NEED TO FILL
            "EMPTY"
        "Do I get to be a spy too?":
            harry "Of course! Harry and [s3_name] a crime-fighting, super-spying duo."
            harry "We can both get proper sweet tuxedos."
            s3_mc "Or we could both wear sleek, sexy silk dresses."
            harry "Do you think I could pull it off?"
            s3_mc "I think you'd rock it."
        "Does that make me the femme fatale?":
            harry "I'm not sure I'd last very long if you were the enemy."
            harry "I'd be like 'see ya MI6, I'm off to join [s3_name] and take over the world'."
            "You pretend to pout."
            s3_mc "So you wouldn't even put up a fight?"
            "You run a finger slowly down his chest."
            s3_mc "Shame."
            "Harry grins."
            harry "Maybe just for show."

    s3_mc "Oh, you know what else spies have?"
    s3_mc "Cool gadgets."
    harry "Like a pen that's also a smoke bomb!"

    # CHOICE
    menu:
        s3_mc "Or a..."
        "Lighter":
            pass
        "Water bottle":
            pass
        "Torch":
            pass

    # CHOICE
    menu:
        s3_mc "That's also a..."
        "Tranquiliser dart":
            pass
        "Poison dispenser":
            pass
        "Laser":
            pass

    harry "I dunno, sounds... dangerous."
    s3_mc "That's the point!"
    harry "I meant dangerous for you."
    harry "I can see a hundred ways it could go wrong..."
    harry "Besides, you're forgetting the best gadget of all."
    s3_mc "What's that?"
    harry "The one in my pants."

    # CHOICE
    menu:
        s3_mc "That was... "
        "Confusing":
            # NEED TO FILL
            "EMPTY"
        "Sexy":
            harry "What would a spy be without his dry wit?"
            s3_mc "'Dry wit' might be pushing it, babe."
        "Hilarious":
            harry "Hmm, I was going for 'suave'."
            harry "But hilarious is a decent runner-up prize."
            s3_mc "It's actually the first prize."

    "You both laugh."

label s3e4p3_stay_up_camilo:
    "Camilo runs his fingers down your arm and looks into your eyes. He winks."

    # CHOICE
    menu:
        thought "He looks good..."
        "Tease him":
            # NEED TO FILL
            "EMPTY"
        "Kiss him":
            "You lean in and kiss him, feeling his strong arms wrap around you and pull you in tighter."
            "The subtle, spicy scent of his aftershave washes over you."
            camilo "You're bloody fantastic."
            s3_mc "You're pretty great yourself."
        "Tease him and then kiss him":
            "You stroke his hair, and when he leans in for a kiss, you kiss his forehead."
            camilo "Keeping me on my toes?"
            "You respond by grabbing his chin and pulling him in for a fierce, passionate kiss."
            camilo "Whew, mamacita. That was amazing."

    "Camilo twirls a bit of your hair in his finger."
    camilo "[s3_name], can I ask a question?"
    s3_mc "Sure."
    camilo "Did you worry about coming in here? The Villa, I mean."
    s3_mc "In what way?"
    camilo "Well, like leaving your family behind."

    # CHOICE
    menu:
        thought "Was I worried about leaving my family?"
        "Not at all":
            s3_mc "I hadn't really thought about it, if I'm honest."
            s3_mc "I guess I don't have that kind of relationship with them."
            camilo "But won't they miss you?"
            s3_mc "Maybe?"
            s3_mc "But I'm sure they'll last a summer without me!"
        "Maybe my grandparents":
            s3_mc "Yeah, my grandparents especially."
            camilo "I get that. Mine are in Colombia and I miss them a lot."
            s3_mc "But the rest of my family will be fine without me for a summer!"
        "Yeah, definitely":
            s3_mc "Totally. I was a bit of a mess at the airport, haha!"
            camilo "I knew you'd feel me."
            camilo "I think about mine every day. Wondering how they're getting on and that."

    s3_mc "You're really close with yours, right?"
    camilo "Yeah, but more than that, they really depend on me."
    camilo "What with my dad being ill, and me being the oldest kid..."
    camilo "I dunno, I just feel really responsible for everyone."

    # CHOICE
    menu:
        thought "Camilo feels responsible for his family..."
        "I'm sure they appreciate it":
            s3_mc "They're really lucky to have you."
            s3_mc "I'm sure they appreciate everything you do."
            camilo "Yeah... It doesn't feel that way all the time."
            camilo "Don't get me wrong, I love my family to bits, but sometimes it feels like it's just one thing after another, you know?"
        "That's really noble":
            s3_mc "I admire that. I like a man who takes care of his family."
            camilo "It's not like I'm some kind of hero, though."
            camilo "I just did what had to be done. There wasn't anyone else to step up after my dad got sick."
            s3_mc "That takes courage."
            camilo "Maybe. I hadn't really thought about it, if I'm honest."
        "That must be tough":
            s3_mc "That's gotta be tough on you."
            "He shrugs."
            camilo "I dunno, I never thought about it really."
            camilo "After my dad got sick, I was the one who had to step up."
            camilo "Just the way it goes, innit."

    camilo "Just the way it goes, innit"
    "You put your arms around his neck. You feel the hard muscles in his shoulders relax a little."
    s3_mc "Well, I'm definitely glad you came here, mister."
    camilo "Yeah, lucky you, eh?"
    s3_mc "Seriously, though. You deserve to have a bit of fun and be happy."
    camilo "You're a big part of that, [s3_name]."
    s3_mc "Which one? Having a bit of fun or being happy?"
    camilo "Huh? Which one? What do you-"
    camilo "Oh, you're taking the mickey."
    camilo "You're bad!"
    s3_mc "I try."

label s3e4p3_stay_up_aj:
    aj "I can't tell if you're sending me kiss-you-right-now signals or not..."

    # CHOICE
    menu:
        thought "Am I sending signals telling AJ to kiss me?"
        "Nah, I don't want to right now":
            # NEED TO FILL
            "EMPTY"
        "Yes! Kiss me, AJ":
            s3_mc "Yeah, I am!"
            s3_mc "Kiss me, AJ!"
            "She closes her eyes and leans in to kiss you."
            "You kiss passionately, your hands bring her closer towards you."
            "It is urgent and frantic. You can't get enough of each other. You can't get close enough."
            "She pulls away, you're both breathless."
            s3_mc "That was..."
            aj "Yeah..."
            aj "That was some kiss."
            aj "Wow."
            "She smiles, catching up with her breath."
            aj "You take my breath away, [s3_name]."
            aj "I'm normally awful at reading signals so I'm glad I got this one right."
        "Pucker your lips and kiss her":
            aj "I'll take that as a yes."
            "You lean in to kiss her."
            "You kiss passionately, your hands bring her closer towards you."
            "It is urgent and frantic. You can't get enough of each other. You can't get close enough."
            "She pulls away, you're both breathless."
            s3_mc "That was..."
            aj "Yeah..."
            aj "That was some kiss."
            aj "Wow."
            "She smiles, catching up with her breath."
            aj "You take my breath away, [s3_name]."
            aj "I'm normally awful at reading signals so I'm glad I got this one right."

    aj "I think flirty signals just fly right past me sometimes."
    aj "Do you notice it when people flirt with you?"

    # CHOICE
    menu:
        thought "Do I pick up on flirty vibes?"
        "Are you flirting with me right now?":
            # NEED TO FILL
            "EMPTY"
        "Yeah, I can always tell":
            aj "I wish I had that."
        "No one flirts with me":
            aj "Don't be silly. I know people flirt with you, [s3_name]!"
            aj "I'm one of them."

    aj "My friends always tease me and say they don't want to take me out of goal because I'm, like, so oblivious to obvious passes."
    aj "Even though I'm apparently a really big flirt."
    aj "How can you tell if someone likes you or not?"

    # CHOICE
    menu:
        thought "How can I tell if someone is into me?"
        "Cast a spell":
            # NEED TO FILL
            "EMPTY"
        "Body language":
            s3_mc "It's all about the body language."
            aj "Really?"
            aj "What should I look out for?"
            s3_mc "If it's open and they're leaning towards you that's a good sign."
            aj "Open like when someone's on the field and you pass the ball to them?"
            s3_mc "Yeah, that works."
        "Just ask them":
            aj "Yeah, to be honest, that's the way I usually go about it."
            aj "If I like them, I don't want to hang around waiting for them to maybe make a move."

    aj "At least with us it's pretty clear how we feel about each other."
    aj "I much prefer uncomplicated and straightforward things, do you get me?"

    # CHOICE
    menu:
        thought "AJ likes things to be simple..."
        "I love the thrill of the chase":
            # NEED TO FILL
            "EMPTY"
        "I'm just a simple love machine":
            $ s3_mc.like("AJ")
            aj "Me too!"
        "I've been told I can be a bit chaotic":
            aj "Oh, well, life can make us a bit like that sometimes."

    aj "And you know what?"
    aj "I'm totally dating my fantasy."



Something rattles the sides of your tent, waking you up from your slumber.
genevieve "Psst."
genevieve "MC?"
Genevieve pokes her head through the door.
genevieve "Um, hun..."
Choiceseb "Genevieve?"
-Give us some privacy
-Are you alright?
s3_mc "What's up, hun?"

-I thought you were the demon!
You back away a little.
genevieve "I'm not the demon!"
genevieve "But..."

-Sorry, were we too loud? (Only available if you did bits in the tent)
genevieve "I mean, earlier, yeah. You were pretty loud."
s3_mc "Oops, my bad."
genevieve "It's chill, hun, I don't blame you for wanting to take advantage of this alone time."
genevieve "But that's not what I was coming over here for."

genevieve "Sorry, I just could have sworn I heard something, like, moving around out here."
s3_mc "It could have been a bird or the wind."
genevieve "Yeah. A bird."
s3_mc "Or maybe one of the others had to go to the loo?"
genevieve "You're probably right. I just hate how quiet and dark it is."
genevieve "Anyway."
genevieve "I'll leave you to your sleep..."
Genevieve reluctantly pops her head out of the tent.
thought "Hmm..."
thought "I wonder what she heard?"

"While these lot are all going bump in the night, I've made my own campsite on my floor for me, myself and I."
"I don't have any sausages and beans though."
"But I've got my floor."
"And you know what? The floor is so supportive."
"It's not like walls. It's there for you right where you need it."
"Walls are always getting in my way."
"Anyway, let's leave our Islanders 'sleeping' outside."
"Coming up..."
"The Islanders are in for a few surprises."
genevieve "Wait, those weren't there when we went to bed."
genevieve "Who is in those tents?"
"Maybe a shiny demon?"
"They're quite rare, actually."



#########################################################################
## Episode 5, Part 1
#########################################################################

#########################################################################
## Episode 5, Part 2
#########################################################################

#########################################################################
## Episode 5, Part 3
#########################################################################

#########################################################################
## Episode 6, Part 1
#########################################################################

#########################################################################
## Episode 6, Part 2
#########################################################################

#########################################################################
## Episode 6, Part 3
#########################################################################