#########################################################################
## Episode 7, Part 1
#########################################################################
label s3e7p1:
    scene sand with dissolve
    $ on_screen = []

    show screen day_title(7, 1) with Pause(4)
    hide screen day_title with dissolve

    $ outfit = "pjs"
    "Welcome back, to Love Island!"
    "Where there's one thing on everyone's lips..."
    miki "...aliens?"
    show miki at npc_exit
    pause .3
    $ renpy.hide("miki")
    $ on_screen = []
    "What? No! Last night's recoupling."

    $ outfit = "evening"
    if s3_mc.current_partner == "Yasmin":
        yasmin "The girl I want to couple up with is..."
        yasmin "[s3_name]."
        show yasmin at npc_exit
        pause .3
        $ renpy.hide("yasmin")
        $ on_screen = []
    elif s3_mc.current_partner == "Tai":
        tai "The girl I want to couple up with is..."
        tai "[s3_name]."
        show tai at npc_exit
        pause .3
        $ renpy.hide("tai")
        $ on_screen = []
    elif s3_mc.current_partner == "Ciaran":
        ciaran "The girl I want to couple up with is..."
        ciaran "[s3_name]."
        show ciaran at npc_exit
        pause .3
        $ renpy.hide("ciaran")
        $ on_screen = []

    if s3e6p3_listen:
        "It wasn't all sunshine and roses."
        "[s3_name] overheard an argument between [s3_mc.past_partners[1]] and [s3_mc.current_partner]."
        "I love a good love triangle, don't you?"
    else:
        "But who knows what [s3_mc.past_partners[1]] thinks about that?"
        "Well, I do. I'm the one keeping an eye on things."
        "All day every day."
        "It gets a bit tiring, really."
    
    $ outfit = "swim"
    "It's all change on the Villa train!"
    "And we're going full steam ahead."
    "Coming up!"
    camilo "It's all in the wrist..."
    show camilo at npc_exit
    pause .3
    $ renpy.hide("camilo")
    $ on_screen = []
    "Er, thanks for that Camilo."
    "And mystery is a foot."
    elladine "It's the shiny demon!"
    show elladine at npc_exit
    pause .3
    $ renpy.hide("elladine")
    "That was just a story, Elladine."
    "Wasn't it?"

    scene s3-bedroom-day with dissolve
    $ on_screen = []
    $ outfit = "pjs"
    $ pronouns(s3_mc.current_partner)

    "It's the morning after yesterday's recoupling."
    "[s3_name] is all snuggled up in bed."
    "You wake slowly. A light breeze is playing on your skin."
    thought "Hey! Who stole the duvet?"
    "When you peek over the edge of your bed, your duvet is folded neatly on the floor."
    thought "How did it get there? Someone's folded it up..."

    if s3e6p3_loyal == False:
        thought "Good thing [s3_mc.current_partner]'s so warm."

    if s3e6p3_bits:
        "As you stretch, you remember last night, and [s3_mc.current_partner]'s soft hands running over your skin."
        thought "I can't believe we did that in the same room as everyone!"
        thought "I wonder if he'd/she'd be up for doing it again sometime."
    elif s3e6p3_loyal:
        thought "Good thing it's so warm in here."

    "[s3_mc.current_partner] stirs and murmurs."
    "[he_she!c] blinks [him_her]self awake, and gives you a sleepy smile."

    if s3e6p3_loyal:
        if s3_mc.current_partner == "Yasmin":
            "Her dark gaze is cool and collected."
            yasmin "Good morning."
            yasmin "It sounded like you slept well."
        elif s3_mc.current_partner == "Tai":
            # NEED TO FILL
            "EMPTY - Route: Coupled with Tai but said that previous partner is the only one for you last night."
        elif s3_mc.current_partner == "Ciaran":
            "As he looks away, his cheeks flush."
            ciaran "Hope you slept well, [s3_name]."
    else:
        if s3_mc.current_partner == "Yasmin":
            "Her dark gaze is cool and collected."
            yasmin "Well, hello there."
            yasmin "It feels just right to see your face first thing in the morning."
        elif s3_mc.current_partner == "Tai":
            tai "Hey, you."
            tai "Your face was the first thing I saw, I call that a good sign for the day."
        elif s3_mc.current_partner == "Ciaran":
            "As his gaze travels down to your lips, his cheeks flush."
            ciaran "Last night was proper grand."
            "His dark gaze is warm and friendly."
    
    thought "The others will  be getting up soon."

    # CHOICE
    menu:
        thought "But maybe I could take a little more time in bed with [s3_mc.current_partner]..."
        "Hint that you're cold...":
            # NEED TO FILL
            "EMPTY"
        "Snuggle with [s3_mc.current_partner]":
            $ s3_mc.like(s3_mc.current_partner)
            s3_mc "With the duvet on the floor, it's so cold."
            "You mime shivering."
            if s3_mc.current_partner == "Yasmin":
                yasmin "It is?"
            elif s3_mc.current_partner == "Tai":
                "He raises his eyebrows."
                tai "Yeah, it's like the Arctic Circle in here."
            elif s3_mc.current_partner == "Ciaran":
                "He raises his eyebrows."
                ciaran "Yeah, it's like the Arctic Circle in here."
            s3_mc "I think I need warming up."
            if s3e6p3_loyal:
                "[s3_mc.current_partner] warps [his_her] arms around you and gives you a quick hug."
                "After a moment, [he_she] draws away."
            else:
                "[s3_mc.current_partner] warps [his_her] arms around you, [his_her] skin warm against yours."
                "After a few minutes, [he_she] shifts restlessly."
        "Get straight up":
            s3_mc "I'm starting to get cold without the duvet."
            if s3_mc.current_partner == "Yasmin":
                yasmin "Mm, OK."
            elif s3_mc.current_partner == "Tai":
                tai "Mm, OK."
            elif s3_mc.current_partner == "Ciaran":
                ciaran "Mm, OK."

    if s3_mc.current_partner == "Yasmin":
        yasmin "Let me get you a cup of tea."
    elif s3_mc.current_partner == "Tai":
        tai "Let me get you a cup of tea."
    elif s3_mc.current_partner == "Ciaran":
        ciaran "Let me get you a cup of tea."

    "[s3_mc.current_partner] bounces up and wanders towards the kitchen."
    "You stretch luxuriously."
    s3_mc "Now this is good."
    s3_mc "I could get used to being waited on."
    "From the bathroom you hear a yelp."
    seb "Where are my pyjamas?"
    "The shower is still running when you investigate. Seb opens the bathroom door a crack. His hair is dripping wet."
    s3_mc "Seb, are you...?"
    "Seb looks down and winces."
    seb "I could've sworn I brought my pyjamas in."
    seb "And the towels are over by the beds."
    seb "I had a song in my head. Must've got distracted."
    seb "Typical."
    "Seb sighs and shakes his head."
    seb "[s3_name], you've got to help me."
    seb "Can you grab a towel?"
    "You spot a stack of fresh towels."

    # CHOICE
    menu:
        thought "Seb wants me to get him a towel..."
        "Steal all the towels":
            # NEED TO FILL
            "EMPTY"
        "Get him a towel":
            $ s3e7p1_give_towel = True
            $ s3_mc.like("Seb")
            "You nip across the bedroom, pick up a towel, and bring it over to Seb."
            seb "You're a legend."
            # SUB-CHOICE
            menu:
                thought "Seb appreciated that..."
                "Anything for my bestie!" if s3_mc.bff == 'Seb':
                    pass
                "I couldn't leave you in the lurch":
                    pass
                "I'm your knight in shining armour":
                    pass
                "How could I say no to that sad pout?":
                    pass
        "Tell me a secret, and I'll get the towel":
            $ s3_mc.like("Seb")
            "You nip across the bedroom and pick up a towel."
            seb "That's the one, can you...?"
            s3_mc "Or maybe I should make you work for it."
            s3_mc "Tell me a secret, and I'll bring it over."
            "Seb sighs."
            s3_mc "You're a sneaky soul, [s3_name]."
            seb "I respect that."
            seb "Alright, I saw Nicky giving Elladine a foot massage yesterday."
            seb "And you know what that means."
            # SUB-CHOICE
            menu:
                thought "Oh, I know what that means... (no further reactions)"
                "Toe-sucking?":
                    pass
                "He was being nice?":
                    pass
                "She had sore feet?":
                    pass
            seb "They're basically married."
            seb "You don't give a foot rub unless you really like them."
            seb "Trust me, I know."
            thought "He has a lot of opinions about foot massages!"
            "Seb holds out his hand."
            seb "I kept my end of the deal. Now you."
            "You bring the towel over to Seb, who takes it with a suspicious expression."

    "He turns towards the bathroom."

    if s3_mc.current_partner == "Yasmin":
        yasmin "Hey, Seb! Don't forget these."
    elif s3_mc.current_partner == "Tai":
        tai "Hey, Seb! Don't forget these."
    elif s3_mc.current_partner == "Ciaran":
        ciaran "Hey, Seb! Don't forget these."
        
    "[he_she!c] chucks Seb's trunks to him."
    seb "You had these the whole time?"
    tai "Maybe..."
    ciaran "I just found them, honest!"
    yasmin "Maybe..."
    "Seb grunts, grabs the trunks, then ducks into the bathroom."
    "Soon you can hear the drone of the hairdryer."
    thought "He'll be in there a while. You don't just wake up with hair like this."
    thought "Maybe I can get some tips from him later."
    "You spot AJ jogging over from the gym. Her cheeks are a bit pink and her hair's ruffled."
    "She's carrying a bundle of clothes."
    aj "I was doing some stretches outside..."
    aj "And I found these out on the lawn!"
    thought "Those are Seb's PJs!"
    thought "How did they get all the way out there?"
    "The rest of the Islanders are starting to move. [s3_mc.current_partner] brings you a hot cup of tea, just the way you like it."

    if s3_mc.current_partner == "Yasmin":
        yasmin "Enjoy."
    elif s3_mc.current_partner == "Tai":
        tai "Enjoy."
    elif s3_mc.current_partner == "Ciaran":
        ciaran "Enjoy."
    
    "You sip the tea, enjoying warmth spreading through your body."
    iona "What's going on?"
    aj "I found these folded up by the daybeds!"
    "She waves the PJs as evidence. Everyone looks at the shower door."
    bill "That's well weird."
    miki "Maybe it's aliens?"
    genevieve "There's no evidence of life existing outside Earth."
    genevieve "Even on those moons with ice on."

    # CHOICE
    menu:
        thought "Genevieve doesn't think aliens are real..."
        "Aliens are real for sure":
            s3_mc "Some things are just unexplained."
            miki "Exactly!"
        "Genevieve's right":
            s3_mc "I don't think there's life outside Earth."
            s3_mc "And if there was, they wouldn't even know what PJs were."
        "Why would aliens want Seb's PJs?":
            s3_mc "An alien wouldn't travel all that way..."
            genevieve "...if they even existed..."
            s3_mc "...just to steal Seb's PJs."
            s3_mc "Can you imagine how bad the jet lag would be?"
            miki "But..."

    "Miki's points at Seb's PJs."
    miki "These are Seb's, right?"
    miki "What if he was abducted, and they only left his clothes?"
    miki "What if he was..."
    miki "Replaced by someone else?"
    miki "Something else?"

    # CHOICE
    menu:
        thought "Did Seb seem like he'd been replaced?"
        "He was his usual self":
            s3_mc "He seemed pretty Seb-like."
            s3_mc "Do aliens blow dry their hair?"
        "I'm suspicious of Seb":
            s3_mc "He did spend a long time in the shower."
            s3_mc "Maybe he was perfecting his Seb disguise!"
        "Maybe Miki's been replaced":
            s3_mc "You seem to know an awful lot about this, Miki."
            s3_mc "What if you're the one in disguise?"

    miki "How would we know?!"
    "Everyone looks at the bathroom door. There's a shuffling sound from behind it."
    "The door creaks open."
    "Steam billows out. A shape emerges..."
    seb "Why is everyone staring at me?"
    elladine "No, wait. We've got it all wrong!"
    elladine "It's the shiny demon! I dreamt about it last night!"
    seb "You what?"

    # CHOICE
    menu:
        thought "Elladine thinks the shiny demon has come to the Villa!"
        "Say something brave":
            "You put on a serious expression, and strike your most heroic pose."
            s3_mc "Never fear, Elladine."
            s3_mc "I will protect you!"
            "Elladine's eyes widen with confusion, but AJ catches on."
            aj "Aw, [s3_name], you're a knight in shining armour!"
            s3_mc "We're true of heart and spirit."
            s3_mc "Together we can conquer anything!"
            elladine "Hmm, or maybe I ate too much cheese yesterday."
        "Tell her she's being silly":
            s3_mc "You've been listening to too many ghost stories."
            seb "I was just having a shower..."
            elladine "No, no. The demon is messing with us."
            elladine "Or maybe I ate too much cheese yesterday."
        "Say there's no such thing":
            s3_mc "You've been listening to too many ghost stories."
            seb "I was just having a shower..."
            elladine "No, no. The demon is messing with us."
            elladine "Or maybe I ate too much cheese yesterday."

    elladine "Dairy does give me weird dreams, after all..."
    nicky "What's this about cheese?"
    "Nicky emerges from the bed, yawning."
    nicky "I'm starved. Camilo, mate, you know how you're a cooking legend..."
    "He puts on puppy eyes."
    camilo "I see where this is going."
    nicky "You couldn't make us a bit of breakfast, could you?"
    tai "Your food looked great on the telly. I'd love to try it for myself."
    camilo "Go on..."
    yasmin "Yeah, those empanadas looked incredible."

    if "Camilo" not in s3_mc.past_partners and s3_mc.like_mc["Camilo"] > 8 and s3_like_camilo:
        iona "Go on, show them what you're made of."
        iona "I bet you'll knock it out of the park."
    else:
        iona "Go on, babe, you're well tasty."
        iona "You're food! Your food's well tasty."

    camilo "Since you asked so nicely..."
    camilo "I am a legend at whisking."
    camilo "It's all in the wrist..."
    s3_mc "Had a lot of practice?"
    camilo "Wouldn't you like to know?"
    camilo "[s3_name], want to help?"
    thought "I could do with a snack."
    thought "And some breakfast, too."
    if s3_mc.past_partners[1] == "Camilo":
        thought "Now I'm not with Camilo, this is my chance to have some real quality time with him."
        thought "Without anyone interrupting..."
    elif "Camilo" not in s3_mc.past_partners and s3_mc.like_mc["Camilo"] > 8 and s3_like_camilo:
        thought "This is my chance to have some quality time with Camilo, without anyone else around."
    else:
        thought "This is my chance to graft on Camilo without Iona around..."
        thought "Or catch some real quality time."

    # CHOICE
    menu:
        thought "Should I help Camilo make breakfast?"
        "Help Camilo in the kitchen (gem choice)":
            $ s3_mc.like("Camilo")
            $ s3e7p1_help_camilo = True
            call s3e7p1_help_camilo from _call_s3e7p1_help_camilo
        "Leave him to cook alone":
            s3_mc "I'd rather be waited on hand and foot!"
            camilo "Aww, you don't want to give me a hand?"
            s3_mc "Nah, you're on your own"
            camilo "OK, but I get the pick of the pancakes! Chef's choice."

    "I would happily eat any of Camilo's pancakes. Even the tester one."
    "Seriously, no one brought me any breakfast today!"
    "Should I be worried?"

    scene s3-daybeds-day with dissolve
    $ on_screen = []

    if s3e7p1_help_camilo:
        "Everyone cheers as you bring out the glorious pancakes."
    else:
        "Everyone cheers as Camilo brings out the glorious pancakes."

    camilo "Thank you, thank you."

    if s3e7p1_help_camilo:
        camilo "I could not have done it without my beautiful assistant."
        "[s3_mc.current_partner] raises [his_her] eyebrows, but [he_she] claps along with the other Islanders."
        # CHOICE
        menu:
            thought "Camilo thinks I was a great assistant... (no further reactions)"
            "That's Head Chef to you":
                pass
            "I hope they're good":
                pass
            "I wanna know what everyone thinks":
                pass 
        if s3_mc.bff == "Elladine":
            elladine "These look stunning."
        elif s3_mc.bff == "Genevieve":
            genevieve "These look stunning."
        elif s3_mc.bff == "Nicky":
            nicky "These look stunning."
        elif s3_mc.bff == "Seb":
            seb "These look stunning."
    else:
        iona "Stunning!"
        iona "And the pancakes are good, too."
    
    "There's a shuffle while the Islanders grab plates and pancakes."


    if s3_mc.current_partner == "Tai":
        tai "You want to sit here, [s3_name]?"
    elif s3_mc.current_partner == "Ciaran":
        ciaran "You want to sit here, [s3_name]?"
    elif s3_mc.current_partner == "Yasmin":
        yasmin "You want to sit here, [s3_name]?"

    if s3e6p3_hug_old_li:
        "As you consider, [s3_mc.past_partners[1]] meets your eye and smiles."

    # CHOICE
    menu:
        thought "Who should I eat breakfast with?"
        "I'll chill by myself":
            "You lounge on your daybed with your plate, listening to the others chat."
            "Nicky brings Elladine a cup of coffee, and perches on the edge of her daybed to talk."
            "Tai and Ciaran are playfully arm-wrestling. Ciaran's in the lead."
            "So far."
            "All is peaceful."
        "[s3_mc.past_partners[1]]":
            $ pronouns(s3_mc.past_partners[1])
            
            if s3e6p3_hug_old_li:
                $ s3_mc.like(s3_mc.past_partners[1])
                "You stroll over to [s3_mc.past_partners[1]], who gives you a grin."
                if s3_mc.past_partners[1] == "Bill":
                    bill "Knew you couldn't stay away from me for long."
                elif s3_mc.past_partners[1] == "Camilo":
                    camilo "Knew you couldn't stay away from me for long."
                elif s3_mc.past_partners[1] == "Harry":
                    harry "Knew you couldn't stay away from me for long."
                elif s3_mc.past_partners[1] == "AJ":
                    aj "Knew you couldn't stay away from me for long."

                "[he_she!c] glances at [s3_mc.current_partner]."
                if s3_mc.past_partners[1] == "Bill":
                    bill "Can't break us up that easily."
                elif s3_mc.past_partners[1] == "Camilo":
                    camilo "Can't break us up that easily."
                elif s3_mc.past_partners[1] == "Harry":
                    harry "Can't break us up that easily."
                elif s3_mc.past_partners[1] == "AJ":
                    aj "Can't break us up that easily."
                "[he_she!c] then looks at the pancakes you've brought over."
            else:
                "You stroll over to [s3_mc.past_partners[1]], who looks at you in surprise."
                if s3_mc.past_partners[1] == "Bill":
                    bill "I thought you'd be eating breakfast with [s3_mc.current_partner]?"
                    s3_mc "I fancied having breakfast with you."
                    "[he_she!c] frowns."
                    bill "OK...I'm not going to lie, that's a little weird."
                    bill "But seeing as you're here..."
                    bill "Let's see what you've got."
                elif s3_mc.past_partners[1] == "Camilo":
                    camilo "I thought you'd be eating breakfast with [s3_mc.current_partner]?"
                    s3_mc "I fancied having breakfast with you."
                    "[he_she!c] frowns."
                    camilo "OK...I'm not going to lie, that's a little weird."
                    camilo "But seeing as you're here..."
                    camilo "Let's see what you've got."
                elif s3_mc.past_partners[1] == "Harry":
                    harry "I thought you'd be eating breakfast with [s3_mc.current_partner]?"
                    s3_mc "I fancied having breakfast with you."
                    "[he_she!c] frowns."
                    harry "OK...I'm not going to lie, that's a little weird."
                    harry "But seeing as you're here..."
                    harry "Let's see what you've got."
                elif s3_mc.past_partners[1] == "AJ":
                    aj "I thought you'd be eating breakfast with [s3_mc.current_partner]?"
                    s3_mc "I fancied having breakfast with you."
                    "[he_she!c] frowns."
                    aj "OK...I'm not going to lie, that's a little weird."
                    aj "But seeing as you're here..."
                    aj "Let's see what you've got."
                "[he_she] looks at the pancakes."

            if s3_mc.past_partners[1] == "Bill":
                bill "I'd have done these a tiny bit thicker. Just so's they've got more bite."
                bill "But the flavour's just right. You have to get that balance of sweet and sharp."
            elif s3_mc.past_partners[1] == "Camilo":
                if s3e7p1_help_camilo:
                    camilo "You did good on the breakfast. These are stunners."
                else:
                    camilo "These are stunners, if I do say so myself."
            elif s3_mc.past_partners[1] == "Harry":
                harry "These are brilliant!"
                if s3e3p1_teach_harry:
                    harry "Better than my [s3e3p1_harry_bfast]."
                    harry "But you were a really good teacher."
            elif s3_mc.past_partners[1] == "AJ":
                aj "Good breakfast after a good workout. I'm in paradise!"

            if s3_mc.past_partners[1] == "Bill":
                bill "I'm loving these [s3e7p1_fruit]."
            elif s3_mc.past_partners[1] == "Camilo":
                camilo "I'm loving these [s3e7p1_fruit]."
            elif s3_mc.past_partners[1] == "Harry":
                harry "I'm loving these [s3e7p1_fruit]."
            elif s3_mc.past_partners[1] == "AJ":
                aj "I'm loving these [s3e7p1_fruit]."
        "[s3_mc.current_partner]":
            $ s3_mc.like(s3_mc.current_partner)
            $ pronouns(s3_mc.current_partner)
            if s3_mc.current_partner == "Tai":
                tai "Breakfast is the most important meal of the day."
                tai "And it feels great spending it with you."
                tai "I love these [s3e7p1_fruit], they're amazing."
            elif s3_mc.current_partner == "Ciaran":
                "Ciaran wolfs down his pancakes, then eyes you plate hopefully."
                ciaran "These remind me of my ma's cooking. So good."
                ciaran "And the [s3e7p1_fruit] are amazing."
            elif s3_mc.current_partner == "Yasmin":        
                yasmin "Very nice to see you, [s3_name]."
                yasmin "These are [s3e7p1_fruit] are stunning."
            "[he_she!c] picks up one of the bananas and offers it to you."

            # CHOICE
            menu:
                thought "Mmh, [s3_mc.current_partner] is offering me a [s3e7p1_fruit], I should..."
                "Eat it neatly":
                    "You take the fruit from [his_her] fingers and savour the taste."
                "Eat it flirty":
                    "As you nibble the fruit, your tongue brushes against [his_her] fingers."
                    "[his_her!c] breath hitches, and [he_she] bites [his_her] lips."
                "Feed it to [him_her] instead":
                    "You pluck the fruit from [his_her] fingers and hold it to [his_her] mouth."
                    "[he_she!c] nibbles lightly, [his_her] eyes never leaving yours. For a second, [his_her] lips brush your skin."

            s3_mc "Delicious."

    "Around the daybeds, everything falls silent as the Islanders tuck in. It's rare that everyone's this quiet."
    ciaran "Let me get the dishes!"
    camilo "I can do it, mate, don't worry about it."
    ciaran "That's not fair! You did a load of work making breakfast."
    camilo "Alright, I'll supervise."

    scene s3-daybeds-day with dissolve
    $ on_screen = []

    "While you relax and enjoy the sun, [s3_mc.bff] comes to recline on the daybed next to you."

    if s3_mc.bff == "Elladine":
        elladine "Alright, [s3_name]?"
        elladine "Nicky got me another cup of coffee, isn't that sweet?"
    elif s3_mc.bff == "Genevieve":
        genevieve "Alright, [s3_name]?"
        if s3e6p1_break_up and s3_mc.past_partners[1] == "Harry":
            genevieve "Harry's funny once you get to know him."
        elif s3_mc.current_partner == "Yasmin":
            genevieve "Ciaran is sweet. He's like a cute little puppy."
    elif s3_mc.bff == "Nicky":
        nicky "Alright, [s3_name]?"
        nicky "Elladine made me get her another cup of coffee. She'll be bouncing off the walls by lunchtime!"
    elif s3_mc.bff == "Seb":
        seb "Alright, [s3_name]?"
        seb "Another day, another breakfast."
        if s3e7p1_give_towel == False:
            seb "Don't think I've forgotten about earlier."
            seb "At least here there's nothing for you to steal."

    if s3_mc.bff == "Elladine":
        elladine "Things changed a lot last night. What's going on with [s3_mc.past_partners[1]]?"
    elif s3_mc.bff == "Genevieve":
        genevieve "Things changed a lot last night. What's going on with [s3_mc.past_partners[1]]?"
    elif s3_mc.bff == "Nicky":
        nicky "Things changed a lot last night. What's going on with [s3_mc.past_partners[1]]?"
    elif s3_mc.bff == "Seb":      
        seb "Things changed a lot last night. What's going on with [s3_mc.past_partners[1]]?"

    # CHOICE
    menu:
        thought "Genevieve's asking how I feel about the recoupling..."
        "I'm really into [s3_mc.current_partner]":
            $ s3_mc.like(s3_mc.current_partner)
            s3_mc "Being coupled up with [s3_mc.current_partner] is amazing."
            if s3_mc.bff == "Elladine":
                elladine "It's good you're getting along."
                elladine "Wonder what [s3_mc.past_partners[1]] thinks about it."
            elif s3_mc.bff == "Genevieve":
                genevieve "It's good you're getting along."
                genevieve "Wonder what [s3_mc.past_partners[1]] thinks about it."
            elif s3_mc.bff == "Nicky":
                nicky "It's good you're getting along."
                nicky "Wonder what [s3_mc.past_partners[1]] thinks about it."
            elif s3_mc.bff == "Seb":
                seb "It's good you're getting along."
                seb "Wonder what [s3_mc.past_partners[1]] thinks about it."
        "I can't decide between [s3_mc.past_partners[1]] and [s3_mc.current_partner]":
            $ s3_mc.like(s3_mc.current_partner)
            $ s3_mc.like(s3_mc.past_partners[1])
            s3_mc "They're both great."
        "I miss [s3_mc.past_partners[1]]":
            $ s3_mc.like(s3_mc.past_partners[1])
            s3_mc "I'd just gotten used to being with [s3_mc.past_partners[1]] and the next thing I know, everything's changed."
        "I'm thinking ahead":
            s3_mc "I don't know if I want to be tied down at this point."
            s3_mc "There's still a lot of time to go till the final."
            if s3_mc.bff == "Elladine":
                elladine "Yeah, and you can't be bogged down worrying about what [s3_mc.past_partners[1]] and [s3_mc.current_partner] are thinking."
            elif s3_mc.bff == "Genevieve":
                genevieve "Yeah, and you can't be bogged down worrying about what [s3_mc.past_partners[1]] and [s3_mc.current_partner] are thinking."
            elif s3_mc.bff == "Nicky":
                nicky "Yeah, and you can't be bogged down worrying about what [s3_mc.past_partners[1]] and [s3_mc.current_partner] are thinking."
            elif s3_mc.bff == "Seb":
                seb "Yeah, and you can't be bogged down worrying about what [s3_mc.past_partners[1]] and [s3_mc.current_partner] are thinking."

    if s3_mc.bff == "Elladine":
        elladine "It's like you're in a love triangle."
        elladine "It's like a situation from one of Miki's telenovelas."
        elladine "Or one of those books, you know, the series where she has to decide between the werewolf and the vampire."
    elif s3_mc.bff == "Genevieve":
        genevieve "It's like you're in a love triangle."
        genevieve "It's like a situation from one of Miki's telenovelas."
        genevieve "Or one of those books, you know, the series where she has to decide between the werewolf and the vampire."
    elif s3_mc.bff == "Nicky":
        nicky "It's like you're in a love triangle."
        nicky "It's like a situation from one of Miki's telenovelas."
        nicky "Or one of those books, you know, the series where she has to decide between the werewolf and the vampire."
    elif s3_mc.bff == "Seb":
        seb "It's like you're in a love triangle."
        seb "It's like a situation from one of Miki's telenovelas."
        seb "Or one of those books, you know, the series where she has to decide between the werewolf and the vampire."

    # CHOICE
    menu:
        thought "[s3_mc.bff] thinks I'm in a vampire-werewolf love triangle..."
        "I'd go for the werewolf":
            s3_mc "Rugged, outdoorsy... what's not to love about a werewolf?"
            if s3_mc.bff == "Elladine":
                elladine "The smell of wet dog?"
            elif s3_mc.bff == "Genevieve":
                genevieve "The smell of wet dog?"
            elif s3_mc.bff == "Nicky":
                nicky "The smell of wet dog?"
            elif s3_mc.bff == "Seb":
                seb "The smell of wet dog?"
        "Vampires all the way, hun":
            s3_mc "Graceful, intense...what's not to love about a vampire?"
            if s3_mc.bff == "Elladine":
                elladine "Being room temperature?"
            elif s3_mc.bff == "Genevieve":
                genevieve "Being room temperature?"
            elif s3_mc.bff == "Nicky":
                nicky "Being room temperature?"
            elif s3_mc.bff == "Seb":
                seb "Being room temperature?"
        "I prefer merfolk":
            s3_mc "Stunning, great at singing... what's not to love about merfolk?"
            if s3_mc.bff == "Elladine":
                elladine "The tail?"
            elif s3_mc.bff == "Genevieve":
                genevieve "The tail?"
            elif s3_mc.bff == "Nicky":
                nicky "The tail?"
            elif s3_mc.bff == "Seb":
                seb "The tail?"

    if s3_mc.bff == "Elladine":
        elladine "I know it's all a bit of fun, but I could never get into all the paranormal romance stuff."
        elladine "Call me weird but the girls in them are way too trusting of all these monsters who want to have sex with them."
        # CHOICE
        menu:
            thought "Paranormal romance is..."
            "The worst":
                # NEED TO FILL
                "EMPTY"
            "My favourite genre":
                elladine "Oh, sorry hun! I didn't mean to be mean or anything."
                s3_mc "Don't be silly. Everyone has different tastes."
                elladine "It's just... well, maybe I prefer my men to be flesh and blood?"
                elladine "I don't really read much anyways."
            "Not bad, but not my favourite":
                elladine "Yeah, I suppose it's not the worst stuff I've ever read."
                elladine "Not that I've read a lot."

        elladine "I never have enough time, and I'm just more about the here and now."
        elladine "Do you read much?"
        # CHOICE
        menu:
            thought "Am I a reader?"
            "Every now and again":
                # NEED TO FILL
                "EMPTY"
            "Reading? What, like actual books?":
                # NEED TO FILL
                "EMPTY"
            "It's my life":
                elladine "That's really cool! I wish I read more often."

        elladine "Sometimes I worry that Nicky won't like me because I'm not as clever as he is."
        elladine "He always goes on about art and music and I end up sitting there just listening to him."
        elladine "Don't get me wrong, I love it! I find intelligence attractive."
        elladine "But I wonder if he thinks I'm good enough for him."
        # CHOICE
        menu:
            thought "Elladine is worried that Nicky doesn't think she's good enough..."
            "If you're worried, why not do something about it?":
                # NEED TO FILL
                "EMPTY"
            "Maybe he does, but why worry about what you can't change?":
                # NEED TO FILL
                "EMPTY"
            "Don't be silly, you're one of the smartest people here":
                $ s3_mc.like("Elladine")
                s3_mc "Seriously. There's no need to put yourself down."
                s3_mc "Just because you don't read much, it doesn't mean anything about how clever you are."
                s3_mc "And even then, I don't think Nicky would mind. He's into you regardless. It's so obvious."
                elladine "Damn, [s3_name]."
                elladine "You're right. I'm tying myself in knots again."
                elladine "Totally pointless."
                elladine "Thanks for the advice, babe. It's always nice to have you around."
                s3_mc "Likewise."

    elif s3_mc.bff == "Genevieve":
        "Genevieve looks like she is about to sneeze."
        "She flaps her hands about."
        # CHOICE
        menu:
            thought "Genevieve is going to sneeze on me!"
            "Duck and cover!":
                "You quickly move out of her line of sneeze."
                "She sneezes loudly. Luckily she misses you."
                genevieve "Sorry, babe."
            "Run and grab her a tissue":
                s3_mc "I'll run and grab you a-"
                "She sneezes loudly. Luckily she misses you."
                genevieve "Ah, damn. Sorry, [s3_name]."
            "Tell her to say 'pineapple'":
                s3_mc "Say, pineapple!"
                genevieve "Pineapple!"
                "She doesn't sneeze."
                genevieve "Woah. That's, like, magic."

        genevieve "I always sneeze when I look up at the light."
        genevieve "I've got a ACHOO syndrome."
        s3_mc "Ha, ha. Very funny."
        genevieve "No, I'm serious. It's autosomal dominant compulsive helio-ophthalmic outbursts of sneezing."
        genevieve "Seb told me he has it too. Then he sneezed. It was cute."
        # CHOICE
        menu:
            thought "Viv says she sneezes at light..."
            "I've heard of it":
                genevieve "Cool! Not many people have."
                genevieve "Which is weird, because supposedly over a fifth of the population has it."
            "Sounds made up":
                genevieve "Yeah, it does! But it's science, and who are we to question science?"
                s3_mc "I'm [s3_name], and I question science."
            "I have it too!":
                genevieve "No way! That makes three of us. Over a fifth of the population does, so the stats work out."
            "I studied that before at work" if s3_mc.job == 'Scientist':
                genevieve "That's so cool! I hope you find a cure. It's really annoying, especially at festivals."
                genevieve "Every time I step outside the medical tent, it's sneeze o'clock."

        genevieve "There are theories about why it happens, but nothing concrete."
        genevieve "Wanna hear my theory?"
        # CHOICE
        menu:
            thought "Do I want to hear Viv's theory about ACHOO?"
            "I'll do the theorising, thanks" if s3_mc.job == 'Scientist':
                # NEED TO FILL
                "EMPTY"
            "Snore, pass":
                genevieve "That's fair, actually. Sorry, this kind of stuff is so interesting to me, I forget it's boring for other people."
                s3_mc "That's OK. Thanks for not getting annoyed."
                genevieve "It takes more than that to annoy me, [s3_name]."
            "Yeah!":
                genevieve "I think we're all allergic to the sun."
                s3_mc "Um... OK?"
                genevieve "It's just pure radiation, isn't it? It's the cause of so many diseases, and being exposed to it for too long physically burns you."
                genevieve "And for some people, even looking at it is bad?"
                genevieve "Which leads me to conclude that the sun is evil."
                genevieve "You have to admit it's a good theory."
                # SUB-CHOICE
                menu:
                    thought "Your theory is..."
                    "Silly":
                        # NEED TO FILL
                        "EMPTY"
                    "Bang on the money":
                        s3_mc "The sun is evil, and it's our destiny to destroy it."
                        genevieve "What, really? Wow, I've never taken it that far."
                        s3_mc "It makes sense. Think about it like this. The sun is really big and a really long way away, right?"
                        genevieve "Right."
                        s3_mc "So to destroy it, we'd need to really pull together as a species."
                        s3_mc "We'd need spaceships, supplies, some way of actually destroying it. Right?"
                        s3_mc "The effort would be enormous. We'd need to all pull together. It would unite humanity."
                        genevieve "Wouldn't we die without it, though? We need it for growing food and stuff."
                        s3_mc "I think if we had science good enough to destroy the entire sun, we'd have solved basic problems like 'needing food'."
                        genevieve "Wow. I think you might be right."
                    "Not impossible":
                        genevieve "Right! Thanks, [s3_mc]. It's nice to talk to you about this stuff."
                        genevieve "I miss looking into things like that sometimes, being in here."
                        genevieve "Although, it's a great holiday so far."
                    "Scientifically unlikely":
                        genevieve "It's not like I'm just making this up."
                        genevieve "Think what you like, it's OK."
                        genevieve "Thanks for listening to me either way."

    elif s3_mc.bff == "Nicky":
        nicky "My sister was really into those books."
        nicky "But she stopped reading them when the vampire and the werewolf had a baby together."
        nicky "She said her immersion was broken..."
        nicky "Tell you what, this is her dream situation right here. The amount of times she's tried to get herself into a love triangle."
        # CHOICE
        menu:
            thought "Nicky's sister tried to make a love triangle around her..."
            "That's what I did here":
                # NEED TO FILL
                "EMPTY"
            "She can have mine":
                s3_mc "If you can get her in here, she can take my place. I can't handle all the drama."
                nicky "You hear that Rachel?"
                nicky "I don't know if this'll make the cut of the show, but I hope she heard you."
            "Why?!":
                nicky "Beats me."
                nicky "Sometimes it feels like we're not even related."
                nicky "But then she starts talking, and I remember we have basically the same exact voice."

        s3_mc "You must miss her."
        nicky "Yeah, a bit. But I knew I would, coming in here."
        nicky "So I can't complain about it now."
        nicky "I mean, it's started to feel kind of nice to be away from her drama. Not having to worry."
        nicky "Agh, that was horrible. Am I a bad person?"
        # CHOICE
        menu:
            thought "Nicky says he's glad to be away from his sister's drama..."
            "That's awful, Nicky":
                # NEED TO FILL
                "EMPTY"
            "You just traded it for mine":
                nicky "Ha. You're not wrong."
                nicky "But I don't have to look out for you as much as I do her."
                nicky "You're independent."
            "I understand":
                s3_mc "She sounds like a lot to deal with. It must be nice to have a break."
                nicky "Exactly. Thanks for understanding, [s3_name]."

        s3_mc "Did you come all the way to Love Island just to avoid your sister?"
        s3_mc "Because this isn't the best place for no drama..."
        nicky "No! Well, it was an unintended benefit."
        nicky "But I came here to find love, like everyone else."
        s3_mc "And have you?"
        nicky "Well, it's a bit early for the L word."
        nicky "But Elladine is great. I like her, she likes me, and she agrees that all pop music is derivative."
        nicky "Or she tells me she does, which is enough."
        # CHOICE
        menu:
            thought "You said you found it hard to get close to people..."
            "Do you take it back?":
                # NEED TO FILL
                "EMPTY"
            "Were you lying?":
                # NEED TO FILL
                "EMPTY"
            "Is she the exception?":
                nicky "That's a nice way of putting it. Yeah, she's the exception."

    elif s3_mc.bff == "Seb":
        seb "Hey, [s3_name]."
        seb "Random question, but you were single when you first came to Love Island, right?"
        s3_mc "Well, yeah, obviously! They wouldn't have let me on otherwise."
        seb "D'you mind if I ask why?"
        # CHOICE
        menu:
            thought "I was single because..."
            "I'd rather not talk about it":
                # NEED TO FILL
                "EMPTY"
            "I was in a serious relationship, but it ended":
                seb "Oh man, I'm sorry."
                seb "Was it you who did the dumping, or...?"
                # SUB-CHOICE
                menu:
                    thought "When that relationship ended..."
                    "I got dumped":
                        seb "That sucks."
                        s3_mc " Well, if that hadn't happened, I wouldn't be on Love Island right now. So, swings and roundabouts."
                    "I was the dumper":
                        # NEED TO FILL
                        "EMPTY"
                    "It was a mutual decision":
                        # NEED TO FILL
                        "EMPTY"
            "I haven't been in a serious relationship before":
                seb "Wow, so you've never been in a relationship before?"
                s3_mc "Not properly, no."
                # SUB-CHOICE
                menu:
                    thought "I wasn't dating before because..."
                    "I had a lot of TV to watch.":
                        # NEED TO FILL
                        "EMPTY"
                    "I was focused on my career":
                        # NEED TO FILL
                        "EMPTY"
                    "I had some work to on myself":
                        seb "Respect."
                        seb "It's probably easier to know who's right for you if you've already got your stuff together, just generally."

        s3_mc "Why are you asking about this all of a sudden?"
        seb "I dunno, I'm just..."
        seb "I guess I'm still kind of wondering if I even belong here."
        s3_mc "Really? Still?"
        seb "Yeah, sorry to say."
        seb "'Cause my whole dating life has been such a disaster up to this point."
        seb "It's left me with this mindset of... why even try, you know?"
        seb "It's proving kind of hard to break out of."
        seb "It feels like the rest of you are all so glamorous and confident and everything, and I'm just... not."
        # CHOICE
        menu:
            thought "Seb's feeling like he doesn't belong..."
            "You probably don't, but so what?":
                # NEED TO FILL
                "EMPTY"
            "I think you fit in here just fine":
                # NEED TO FILL
                "EMPTY"
            "Sometimes I feel the same way":
                seb "Really?"
                s3_mc "Yeah. Sometimes I stop and think, like, how did I even get here?"
                seb "Wow. I didn't realise."

        seb "I can't even imagine the Villa without you."
        seb "Sometimes I forgot you weren't literally born here."
        s3_mc "Well, I wasn't. Nobody was."
        s3_mc "I mean, presumably. I guess it's possible babies have been born here before."
        s3_mc "That's not the point. The point is, all of us feel out of place sometimes."
        s3_mc "It doesn't mean there's anything wrong with you."
        seb "Well. Thanks."
        "He stares into the distance for a while, then nods slowly."
        seb "Thanks, [s3_name]."
        s3_mc "You already said that."
        seb "I know, but I just want you to know I appreciate it."
        seb "It's nice to have someone to talk about stuff."
        # CHOICE
        menu:
            thought "Seb's glad to have someone to talk to..."
            "Okay, but I'm not your therapist":
                # NEED TO FILL
                "EMPTY"
            "Of course, you can always vent to me":
                s3_mc "That's what friends are for."
            "So how's that total independence thing working out for you?":
                seb "Alright, alright. Maybe other people are good to have around sometimes."
                s3_mc "It's called having friends, mate. Sorry to blow your mind."

        seb "Friends, huh?"
        s3_mc "Of course."
        "He smiles to himself."

    "You watch the sunlight filtering down to the daybeds, and stretch in the gentle warmth."

    if s3_mc.bff == "Elladine":
        elladine "I was wondering... how did last night go? With [s3_mc.current_partner]?"
    elif s3_mc.bff == "Genevieve":
        genevieve "I was wondering... how did last night go? With [s3_mc.current_partner]?"
    elif s3_mc.bff == "Nicky":
        nicky "I was wondering... how did last night go? With [s3_mc.current_partner]?"
    elif s3_mc.bff == "Seb":
        seb "I was wondering... how did last night go? With [s3_mc.current_partner]?"

    # CHOICE
    menu:
        thought "How did last night go with [s3_mc.current_partner]?"
        "It was weird":
            s3_mc "I'm not used to it yet."
            s3_mc "It's such a big change."
        "It was nice":
            s3_mc "I really liked it."
            s3_mc "[s3_mc.current_partner] is great."
        "We didn't do anything" if s3e6p3_kiss == False:
            s3_mc "We didn't do bits, if that's what you're asking."
            if s3_mc.bff == "Elladine":
                elladine "That's not what I meant!"
            elif s3_mc.bff == "Genevieve":
                genevieve "That's not what I meant!"
            elif s3_mc.bff == "Nicky":
                nicky "That's not what I meant!"
            elif s3_mc.bff == "Seb":
                seb "That's not what I meant!"
        "We had some fun" if s3e6p3_bits:
            s3_mc "If you're asking if anything happened..."
            s3_mc "I can say that it definitely did."
            if s3_mc.bff == "Elladine":
                elladine "It did?!"
                elladine "In the same room as everyone?"
                elladine "Come to think of it, I did hear creaking."
                elladine "But I thought it was the window!"
            elif s3_mc.bff == "Genevieve":
                genevieve "It did?!"
                genevieve "In the same room as everyone?"
                genevieve "Come to think of it, I did hear creaking."
                genevieve "But I thought it was the window!"
            elif s3_mc.bff == "Nicky":
                nicky "It did?!"
                nicky "In the same room as everyone?"
                nicky "Come to think of it, I did hear creaking."
                nicky "But I thought it was the window!"
            elif s3_mc.bff == "Seb":
                seb "It did?!"
                seb "In the same room as everyone?"
                seb "Come to think of it, I did hear creaking."
                seb "But I thought it was the window!"

    "You stretch out on the daybed, watching the sky."
    "[s3_mc.bff] sighs."
    if s3_mc.bff == "Elladine":
        elladine "We should probably get changed. Can't be in PJs all day."
    elif s3_mc.bff == "Genevieve":
        genevieve "We should probably get changed. Can't be in PJs all day."
    elif s3_mc.bff == "Nicky":
        nicky "We should probably get changed. Can't be in PJs all day."
    elif s3_mc.bff == "Seb":
        seb "We should probably get changed. Can't be in PJs all day."

    if s3_mc.past_partners[1] == "Harry" or s3_mc.past_partners[1] == "AJ":
        "A burst of laughter erupts as you arrive in the dressing room."
        iona "...so I told him he'd need way more maple syrup!"
        miki "I can't believe you said that!"
        iona "Hi babe. We were just talking about Bill and Camilo."
    elif s3_mc.past_partners[1] == "Bill" or s3_mc.past_partners[1] == "Camilo":
        "The dressing room falls quiet as you come in. Miki picks up her contouring sponge while Iona puts on eyeliner."
        s3_mc "Everything alright, girls?"
        miki "We were just talking about Bill and Camilo."

    miki "Bill didn't even complain about me taking photos of dinner last night."
    s3_mc "At dinner?"
    miki "Of dinner. To post once I'm out."

    if "Bill" in s3_mc.past_partners or s3_mc.like_mc["Bill"] > 8 and s3_like_bill:
        miki "[s3_name]..."
        miki "I know things aren't necessarily how you'd like them to be."
        miki "But I wanted to say, I know Bill will wait for you, if you want him to."
        miki "He really likes you."
    else:
        miki "It can be quite hard to get the lighting right."
        miki "He was so helpful."
        iona "I bet he was!"
        miki "Iona!"
        
    # CHOICE
    menu:
        thought "I wonder if Miki and Bill will last"
        "They're a cute pair":
            $ s3_mc.like("Miki")
            $ s3_mc.dislike("Bill")
            thought "Maybe they'll make it work."
            thought "They both like sandwiches a lot."
        "I don't think they're suited":
            thought "I feel like Miki's a bit refined for Bill."
            thought "I couldn't see him throwing out his ketchup if she wanted him to."
        "All I want is to be back with him" if 'Bill' in s3_mc.past_partners:
            $ s3_mc.like("Bill")
            thought "It feels weird not being with him."
            thought "Hopefully we'll couple up again soon."
        "I hope not":
            thought "I feel like Miki's a bit refined for Bill."
            thought "I couldn't see him throwing out his ketchup if she wanted him to."

    miki "Did you hear people arguing here last night?"
    iona "Nope. I was chatting with Genevieve."
    iona "Apparently Harry's quite funny when you get to know him."
    iona "Wonder what the people in here were arguing about, though?"

    if s3e6p3_listen == False:
        s3_mc "I didn't hear anything."
    else:
        thought "They're talking about the argument I heard between [s3_mc.past_partners[1]] and [s3_mc.current_partner]."
        # CHOICE
        menu:
            thought "Should I tell them what I overheard?"
            "Tell them":
                s3_mc "It was [s3_mc.past_partners[1]] and [s3_mc.current_partner]."
                s3_mc "They were arguing about me."
                iona "Ohhh."
            "Say nothing":
                s3_mc "I didn't hear anything."
                iona "Shame."

    "There's a brief pause before Iona dramatically sighs."
    iona "Not gonna lie, I am well into Camilo."

    if "Camilo" in s3_mc.past_partners or s3_mc.like_mc["Camilo"] > 8 and s3_like_camilo:
        iona "But, [s3_name], I know he's into you, too."
        iona "I don't want to get between you."
        iona "Anyway, Camilo was really sweet last night."
        iona "He said he respects you too much to cheat on you, and he'll wait for you if that's what you want."
        iona "You've got a keeper there!"
        # CHOICE
        menu:
            thought "Iona thinks Camilo will wait for me..."
            "Just remember he's mine":
                $ s3_mc.like("Camilo")
                # NEED TO FILL
                "EMPTY"
            "That's a relief":
                $ s3_mc.like("Iona")
                iona "You've got nothing to worry over, babe."
            "You're sweet too":
                $ s3_mc.like("Iona")
                iona "You've got nothing to worry over, babe."
    else:
        iona "Did you know he can tie a cherry stem with his tongue?"
        iona "He doesn't even like cherries. That's dedication."

    "Iona wanders into the bathroom to spray her hair."
    thought "I should get ready for the day."
    thought "This is my chance to look my best!"
    thought "Watch out, everyone. Here I come!"

    scene s3-dressing-room with dissolve
    $ on_screen = []
    $ outfit = "swim"

    miki "[s3_name], you're wowing me today!"
    ## Add back once  MC images are in game.
    # thought "I like this one. It's never done me wrong."
    # miki "Whew, [s3_name]. Looking good."
    # thought "I'll go with this today."
    # miki "Hmm, I think there's something out there that can suit your aesthetic, babe."
    "While Iona's still in the bathroom, Miki whispers to you."
    miki "Did you hear creaking in the bedroom last night?"
    miki "I wonder if anyone was getting naughty."
    miki "Or maybe it was the alien paying us a visit."

    # CHOICE
    menu:
        thought "Miki heard creaking in the bedroom..."
        "You were dreaming":
            # NEED TO FILL
            "EMPTY"
        "It was probably one of the other couples":
            miki "No way!"
            miki "In the same room as everyone?"
        "It was the shiny demon":
            miki "No way!"
            miki "How would it even get in?"
        "It was me and [s3_mc.current_partner]!" if s3e6p3_bits:
            miki "No way!"
            miki "In the same room as everyone?"

    "Iona struts back in, her hair styling complete."
    iona "Miki, your make-up game is so good."
    iona "I thought vloggers would look different without their filters on."
    iona "But you're just as gorgeous in real life."
    miki "I don't use filters!"
    miki "Well, I mean, there's colour balancing. And lighting correction. And pore reduction..."
    miki "But that's just to give a fresh-faced look."
    iona "Oh, like 'no make-up' make-up."
    iona "I never see the point in that."
    iona "Why'd you want to look like you didn't make an effort if it took hours to do anyway."
    "She turns to you."
    iona "What do you think?"

    # CHOICE
    menu:
        thought "What do I think about 'no make-up' make-up?"
        "I don't get this":
            s3_mc "It's a lot of effort to look like you just got out of bed."
            miki "I like it. It means you look like a light desert breeze."
        "I like the look":
            s3_mc "It's fun to have a low-key look. Even if it takes a little while to do."
            miki "Yes, it means you look like a light desert breeze."
        "You both look great":
            s3_mc "You've got different styles, but I love both your looks."
            iona "Aww, you're adorable!"
            miki "Thank you. I do like feeling like a light dessert breeze."

    miki "That aesthetic gets a lot of engagement right now."
    miki "If you say so, babe."
    "As Iona winds up her lipstick, a chunk of it falls out."
    iona "My poor Manuka Vibes!"
    iona "I got that in Tenerife!"
    s3_mc "It's OK. I'll do emergency surgery."

    if s3_mc.job == "Model":
        s3_mc "I've had emergencies like this on photoshoots."
    elif s3_mc.job == "Scientist":
        s3_mc "In the lab, you need a steady hand."
        
    s3_mc "Tweezers."
    "Miki hands you the tweezers."
    miki "Tweezers."
    "You lift the broken piece of lipstick, carefully so as not to squash it."
    s3_mc "Iona, hairdryer."
    iona "I don't think it's long for this world."
    "She brings the hairdryer closer. You feel the warmth along your hand, and the lipstick begins to soften."
    "You gently push the two halves together, letting the hairdryer melt them into one."
    s3_mc "Cocktail stick."
    miki "Cocktail stick."
    "With the cocktail stick, you lightly smooth the broken edge of the lipstick."
    "The broken half tilts."
    iona "I can't watch! Put it out of its misery, hun!"

    # CHOICE
    menu:
        thought "Iona thinks the lipstick should be put out of its misery..."
        "It's only a lipstick!":
            miki "Here lies Manuka Vibes, a loyal friend to the end."
        "Alright, I'm calling it":
            s3_mc "I think we need to say goodbye."
            miki "But..."
            "Iona buries her face in your shoulder."
            s3_mc "There, there. Sometimes these things happen."
            s3_mc "Let go, Miki. You need to let go."
            "Miki gently lays the lipstick on the dressing table."
            miki "Here lies Manuka Vibes, a loyal friend to the end."
        "I'm not giving up":
            $ s3e7p1_saved_lipstick = True
            $ s3_mc.like("Iona")
            s3_mc "I've got this. Hairdryer off."
            "You wait for the lipstick to go solid again. After a couple of breathless minutes, it's as good as new."
            iona "You're total stars, both of you!"
            iona "If I ever do a makeup brand, I'm naming my first lipstick after you."
            iona "Sticky Miki?"
            miki "That... doesn't really fit my brand."
            "Together, you contemplate the fixed lipstick."

    # CHOICE
    menu:
        thought "As witness to these dramatic events, I can only say.."
        "It's gorgeous":
            if s3e7p1_saved_lipstick:
                s3_mc "It looks amazing on you."
                s3_mc "I'm glad we could save it. "
            else:
                s3_mc "It looked amazing on you."
                s3_mc "You should definitely get another one."
        "It wasn't made very well":
            s3_mc "It shouldn't have just broken like that."
            s3_mc "Maybe you can get in touch with the manufacturer?"
            iona "Ooh, maybe I could get a gift voucher."
        "You've got better lipsticks":
            s3_mc "That lipstick you wore the other night looked amazing."
            iona "Aww, thanks."
            iona "I think that was Sultry Sunrise."
        "I'm sorry for your loss" if s3e7p1_saved_lipstick == False:
            s3_mc "It looked amazing on you."
            s3_mc "You should definitely get another one."
            iona "Thanks, hun."

    iona "I will say a few words."
    iona "Manuka Vipes, you served me well through good times and bad..."
    iona "...through a whole lot of kissing..."
    iona "...and that 18-inch pizza challenge."

    if s3e7p1_saved_lipstick:
        iona "Thanks to [s3_name], you will live on in style."
    else:
        iona "May you live on in style."
        miki "I can't watch."
        "Iona solemnly scoops out the broken lipstick, then scrapes it into a little lip balm case."
        
    iona "You will now be known as Manuka Vibes 2: Revenge of the Vibe."
    miki "So beautiful."
    "You stand in silence. Outside, the birds are singing."
    miki "It's me! Guys, I got a text!"
    elladine "Who got a text? Miki got a text!"
    "Everyone piles into the dressing room while Miki reads the text."
    text "Girls, as a reward for successfully completing yesterday's secret challenge the whole Villa is being given a luxury treat..."
    "AJ and Genevieve high-five."
    text "Put on your aprons and grab those spatulas. It's BBQ time! #timetoketchup #mushroommayhem #pullthatpork"
    s3_mc "A BBQ lunch?"
    s3_mc "That'll be..."
    s3_mc "Barbecute."

    "I was really hoping for some pancakes."
    "Maybe Camilo can bring me leftovers."

    scene sand with dissolve
    $ on_screen = []

    "Next time on Love Island..."
    "Ciaran needs help handling the meat..."
    ciaran "I can't fit it all in!"
    show ciaran at npc_exit
    pause .3
    $ renpy.hide("ciaran")
    $ on_screen = []
    "The shiny demon strikes again..."
    seb "I should have expected this."
    show seb at npc_exit
    pause .3
    $ renpy.hide("seb")
    "And maybe I'll get my breakfast?"

    jump s3e7p2
    return

label s3e7p1_help_camilo:
    scene s3-kitchen-day with dissolve
    $ on_screen = []

    "You follow Camilo into the kitchen, where he confidently pours flour and sugar into a bowl. He passes you the bowl, then starts heating up a pan."
    camilo "We've got pancakes on the menu today."
    "You slowly add milk to the bowl, then get whisking."
    camilo "Keep up the speed!"

    # CHOICE
    menu:
        thought "Camilo thinks he's an expert in the kitchen..."
        "I like a guy who knows his way around a whisk":
            s3_mc "It's nice to know that you enjoy cooking."
            s3_mc "Some guys don't even want to step into the kitchen, you know?"
            camilo "Oh yeah, I've had mates who thought it was too girly, or whatever."
            camilo "But my way of thinking is, like, why'd you skip the chance to eat something well nice?"
        "I know what I'm doing!":
            s3_mc "I've got this."
            "For a second, Camilo looks like he's itching to take over from you."
            "Then he smiles."
            camilo "You're right. I need to learn to, like, let go in the kitchen."
        "Who invented the work 'whisk'?":
            "Camilo looks thoughtful as you whisk the batter."
            camilo "The geezer who invented the pancake?"
            s3_mc "Of course, Lord Whisk. That makes sense."
            camilo "Was the guy who invented pancakes really called Lord Whisk?"
            s3_mc "Why not?"
            s3_mc "All done."

    "Once the batter's ready, he pours a little bit into the sizzling pan."
    camilo "So how'd it go with [s3_mc.current_partner]?"

    # CHOICE
    menu:
        thought "Camilo's wondering how last night went with Ciaran..."
        "My lips are sealed":
            camilo "Oooh, mysterious."
        "We didn't do anything" if s3e6p3_kiss == False:
            camilo "Oh, I wasn't asking that!"
        "If you're asking if we did bits, you're in luck" if s3e6p3_bits == True:
            camilo "You don't waste time cracking on, do you?"
        "I dunno, I was asleep":
            camilo "Oooh, mysterious."

    if "Camilo" not in s3_mc.past_partners and s3_mc.like_mc["Camilo"] <= 8:
        camilo "Not gonna lie, I am well into Iona."
        camilo "Did you know she's technically in the mile high club?"
        s3_mc "Technically?"
        camilo "They were taxiing down the runway. So more like the ten metre high club."
        camilo "Anyway, it'd be nice you got a good thing going with Tai/Ciaran/Yasmin too."

    if "Camilo" in s3_mc.past_partners:
        camilo "Not gonna lie, being coupled up with you was amazing."
        camilo "What I'm trying to say is... are you still into me?"
        # CHOICE
        menu:
            thought "Camilo's asking if I'm still into him..."
            "I wish I was back with you" if 'Camilo' in s3_mc.past_partners:
                # NEED TO FILL
                "EMPTY"
            "Of course I'm into you":
                $ s3_mc.like("Camilo")
                camilo "That's made my day."
                camilo "Even more than these legendary pancakes."
            "I'm not, sorry...":
                $ s3_mc.dislike("Camilo")
                "Camilo looks a little surprised, but quickly recovers."
                camilo "No worries, babe."
                camilo "Iona's a great girl. I'll be fine."
            "You should be with Iona":
                $ s3_mc.dislike("Camilo")
                "Camilo looks a little surprised, but quickly recovers."
                camilo "No worries, babe."
                camilo "Iona's a great girl. I'll be fine."
    elif s3_mc.like_mc["Camilo"] > 8:
        camilo "Not gonna lie, you're amazing."
        camilo "What I'm trying to say is... are you still into me?"
        # CHOICE
        menu:
            thought "Camilo's asking if I'm still into him..."
            "I wish I was back with you" if 'Camilo' in s3_mc.past_partners:
                $ s3e7p1_want_cam = True
                # NEED TO FILL
                "EMPTY"
            "Of course I'm into you":
                $ s3e7p1_want_cam = True
                $ s3_mc.like("Camilo")
                camilo "That's made my day."
                camilo "Even more than these legendary pancakes."
            "I'm not, sorry...":
                $ s3_mc.dislike("Camilo")
                "Camilo looks a little surprised, but quickly recovers."
                camilo "No worries, babe."
                camilo "Iona's a great girl. I'll be fine."
            "You should be with Iona":
                $ s3_mc.dislike("Camilo")
                "Camilo looks a little surprised, but quickly recovers."
                camilo "No worries, babe."
                camilo "Iona's a great girl. I'll be fine."

    camilo "Right now, let's enjoy these legendary pancakes."
    "The tester pancake starts to sizzle, but Camilo flops it expertly. You survey the fruits on the counter."

    # CHOICE
    menu:
        thought "What filling will be the tastiest?"
        "Strawberries":
            $ s3e7p1_fruit = "strawberries"
        "Cherries":
            $ s3e7p1_fruit = "cherries"
        "Bananas":
            $ s3e7p1_fruit = "bananas"

    "You chop the [s3e7p1_fruit] into bite-sized chunks."
    "Camilo hums a cheery tune as he tosses another pancake and slides it onto the plate."
    camilo "These are great, but they're not my tia's pancakes."
    s3_mc "Your 'tia'?"
    camilo "My auntie. She makes them plain with honey. They're the best."
    "As he finishes building a tall stack of pancakes, you spot icing sugar on his cheek."

    # CHOICE
    menu:
        thought "That sugar on his face is distracting..."
        "Lick it off" if s3e7p1_want_cam:
            $ s3_mc.like("Camilo")
            "You run your tongue up Camilo's cheek and he wiggles away, laughing."
            camilo "Ah! Ahaha! That tickles!"
        "Wipe it off":
            "Camilo gives you a grateful grin."
            camilo "Ooh, personal grooming. I like it."
        "Leave it on":
            "Camilo doesn't seem to notice."
        "Laugh at it":
            "Camilo doesn't seem to notice."

    "Together, you bring out the pancakes."

    return

#########################################################################
## Episode 7, Part 2
#########################################################################
label s3e7p2:
    scene sand with dissolve
    $ on_screen = []

    show screen day_title(7, 2) with Pause(4)
    hide screen day_title with dissolve

    "Previously on Love Island..."

    if s3e7p1_help_camilo:
        $ outfit = "pjs"
        "[s3_name] and Camilo got frisky..."
        camilo "We've got pancakes on the menu today."
        "With the whisking."
        camilo "Keep up the speed!"
        show camilo at npc_exit
        pause .3
        $ renpy.hide("camilo")
        $ on_screen = []
    else:
        $ outfit = "swim"
        "Miki and the girls chatted aesthetics..."
        miki "That aesthetic gets a lot of engagement right now."
        show miki at npc_exit
        pause .3
        $ renpy.hide("miki")
        $ on_screen = []

    $ outfit = "pjs"
    "And Genevieve got scientific."
    genevieve "Aliens aren't real!"
    show genevieve at npc_exit
    pause .3
    $ renpy.hide("genevieve")
    $ on_screen = []

    $ outfit = "swim"
    "Coming up..."
    bill "We're not all from barbecue central."
    show bill at npc_exit
    pause .3
    $ renpy.hide("bill")

    "Yeah, well, you're in luck, Bill."
    "The next stop is Barbecue Central!"
    "Save me a sausage, [s3_name]!"

    scene s3-lawn-bbq with dissolve
    $ on_screen = []

    "Bill and Tai rush straight over to the barbecue. Ciaran hangs back."
    tai "I'll sort it."
    bill "No, I've got this."
    nicky "Well that's good because..."
    nicky "It's barbecuing time!"
    nicky "And there is literally nothing more fun than a barbecue."
    miki "Nicky's right."
    miki "It's just like camping but with a touch more sophistication."
    iona "Hopefully the shiny demon won't turn up again."
    "Genevieve, Yasmin, and Harry wander over to the group."

    if s3_like_harry and "Harry" in s3_mc.past_partners:
        "His smile seems to light up when he sees you."

    if s3_mc.current_partner == "Yasmin":
        yasmin "Hey."
        "She waves at you, smiling sweetly."
        # CHOICE
        menu:
            thought "I should..."
            "Blow her a kiss":
                # NEED TO FILL
                "EMPTY"
            "Just wave back":
                "You casually wave back."
                s3_mc "Hi."
            "Call her beautiful ":
                $ s3_mc.like("Yasmin")
                s3_mc "Hey beautiful."
                "She grins from cheek to cheek."

    genevieve "Did someone say... shiny demon?"
    tai "Shiny demon?"
    tai "Oh! That's that weird ghost story you guys came up with, right?"
    iona "Yeah..."
    bill "OK, OK, OK."
    bill "Let's not start that again."
    iona "It was this weird ghost story. We told it before you came in."
    "Genevieve seems to shudder a little and starts to head back inside."
    genevieve "I'm going to start on the jollof rice."

    # CHOICE
    menu:
        thought "Genevieve is going to make jollof rice."
        "I love jollof rice":
            $ s3_mc.like("Genevieve")
            genevieve "Sweet!"
        "That sounds like fun!":
            genevieve "Come over to the kitchen and help me out if you'd like, MC!"
        "What's that?":
            genevieve "The recipe varies but we Nigerians do it the best."
            genevieve "Rice with tomatoes, onions, nutmeg, ginger, chilli peppers..."
            genevieve "All sorts of good stuff."

    harry "Show us how to make it. It sounds lush."
    genevieve "Sure. I can do that."

    if s3_like_harry and "Harry" in s3_mc.past_partners:
        harry "You should join us as well, [s3_name]!"

    if s3_mc.bff == "Genevieve":
        genevieve "Yes! More the merrier."
    else:
        "Genevieve raises her eyebrows."

    "They both head over to the kitchen."
    ## Add back once MC images are in game
    # elladine "Hey, [s3_name]! Keeping it low-key with that swimsuit, I see."
    elladine "That's one of my favourites on you, [s3_name]. You're gorgeous."
    # elladine "I love that swimsuit, [s3_name]! I'd ask to borrow it if you weren't already wearing it!"
    "She winks at you."

    if s3_like_aj and s3_mc.like_mc["AJ"] > 8:
        "AJ catches sight of you and instantly starts playing with her hair."
        # CHOICE
        menu:
            thought "I should..."
            "Tell her I miss her":
                $ s3_mc.like("AJ")
                # NEED TO FILL
                "EMPTY"
            "Tell her she's cute":
                $ s3_mc.like("AJ")
                s3_mc "You're so cute when you're all, like, embarrassed and flustered."
                aj "Yeah, that's just how you make me feel. Not going to lie."
                aj "All full of butterflies."
                if s3_mc.current_partner == "Yasmin":
                    "You notice Yasmin looking out of the corner of their eye at you."
                if s3_mc.past_partners[1] == "AJ":
                    aj "I miss you, like, so much."
            "Wave at her":
                "AJ waves back goofily."

    "Seb clears his throat."
    seb "What's the food saying, Bill?"
    tai "It's saying 'why aren't you letting a pro like Tai cook me?'"
    "Bill taps Tai's butt with the spatula. Ciaran laughs."
    tai "Oi, oi, steady on now mate."
    ciaran "Is it me or is it getting hotter out here?"
    seb "Seriously, Bill. How long?"
    seb "I'm hungry."
    bill "It'll be a while till it's ready. So feel free to, like, mill about until it's done."
    tai "He doesn't want you to see the take out being delivered."
    "Bill waves the spatula again. Tai laughs and pretends to doge him."
    thought "Looks like I've got some time to kill before the food is ready..."

    # CALL VILLA CHOICE SCREEN
    call screen s3e7p2_select_who_to_talk_to()
    call screen s3e7p2_select_who_to_talk_to()
    call screen s3e7p2_select_who_to_talk_to()

label s3e7p2_lawn:
    scene s3-lawn-bbq with dissolve
    $ on_screen = []
    $ s3e7p2_visited.append("lawn")

    "Over by the lawn, Bill, Iona and Tai are standing by the barbecue."
    bill "Watch out folks."
    "Bill is trying to flip burgers but they keep sticking."
    bill "The Grill King is at work."
    "Tai laughs."
    tai "But your highness, your patties keep sticking. Did you dab some oil on the grill before putting them on?"
    bill "Oil? You joking? The burgers have fat in them, yeah?"
    tai "Including the veggie ones?"
    bill "I..."
    bill "...hmph."
    "Bill takes care not to use the same spatula for the veggie burgers, but nothing looks like it's cooking."

    if s3_mc.current_partner == "Tai":
        "Tai leans over and nudges your shoulder gently."
        tai "You're looking good, [s3_name]."
        s3_mc "Thanks, Tai."
        tai "These burgers on the other hand..."
        bill "Oi!"
        tai "You need a touch of the Tai magic, am I right, [s3_name]?"

        # CHOICE
        menu:
            thought "Tai wants to work his magic on the BBQ"
            "Good idea, you seem like a good cook":
                "Bill frowns."
                bill "Well, so am I."
            "I thought your thing was pottery":
                tai "I'm a man of many talents, [s3_name]."
                tai "Rugby, Tai Chi, pottery making, cooking..."
                tai "I've got it all."
                "Bill rolls his eyes."
            "You can use that magic touch on me anyday":
                tai "Oh, yeah?"
                tai "I'd do a spell for you any day, [s3_name]."

    "Iona points at the burgers on the barbecue."
    "They're still not cooked."
    iona "I don't think you've got thick enough flames."
    tai "She's right, you've got to have a good girthy flame otherwise it won't cook."
    bill "Girthy flames are not a thing."
    tai "You wouldn't know."
    "Tai picks up some more charcoal from the pile to the side of the barbecue."
    tai "You need more charcoal."
    bill "Nah, that's where you're wrong."
    bill "I don't want it smokey, like, you've got to have it on a low heat so it doesn't get smokey."
    iona "But that twang of smokiness is half the flavour of a good barbecue."
    tai "Yeah, when it'd get sweltering hot back in New Zealand, me and my mates would..."
    "Bill puts down the spatula."
    bill "Alright, mate."
    bill "We're not all from barbecue central."
    tai "That's fair. Alright, I'll let up on you."
    bill "Thank you."
    tai "You need sunshine for a decent barbecue, which you don't get much of."
    bill "But I've had barbecues in the rain before!"
    "Iona rolls her eyes."
    iona "Excuse me, babes."
    bill "Huh? Oh, sorry."
    "He and Tai step aside."
    "Iona tops up the charcoal while the two of them continue to bicker."
    iona "Why is barbecuing such a thing for some men?"
    iona "You wouldn't see them fighting over how to cook something on the hob."
    iona "But stick some flames outside and suddenly they're king of the grills."

    # CHOICE
    menu:
        thought "I should..."
        "Agree with Tai":
            $ s3_mc.like("Tai")
            $ s3_mc.dislike("Bill")
            s3_mc "Tai is right, Bill. They're clearly not cooked."
        "Agree with Bill":
            $ s3_mc.dislike("Tai")
            $ s3_mc.like("Bill")
            s3_mc "Give Bill a chance, Tai."
            s3_mc "Maybe he likes them medium rare."
            tai "Alright, alright."
        "Agree with Iona":
            $ s3_mc.like("Iona")
            s3_mc "Yeah, sorry boys, but Iona is right."
            s3_mc "You're not proving yourself to be any more of a guy just because you can cook on an open flame."
            tai "What? This is just banter."
            bill "Yeah, this is what guys do at a barbecue."
        "Stay out of it":
            pass

    iona "You guys are ridiculous."
    "Iona snatches the spatula off Bill and nudges him out the way with her hip."
    iona "Leave it to the Grill Queen."
    tai "Grill Queen? I'll let my taste buds be the judge of that."
    "She sticks her tongue out at Tai. The burgers finally start to sizzle."
    "While Iona takes over the barbecue Bill whispers in your ear."
    bill "Seeing as they've taken over..."
    bill "I'd kind of like to go for a chat with you."

    # CHOICE
    menu:
        thought "Bill wants to take me for a chat..."
        "What are we doing right now?":
            bill "Um, well, yeah, but I meant like, in private..."
        "A chat about what?":
            if "Bill" in s3_mc.past_partners:
                bill "Like, about us and stuff."
            else:
                bill "Just wanted to see if you were OK."
        "We can chat right here":
            bill "Nah, I kinda wanted to chat in private."

    bill "I'll make up some decoy so they don't get suspicious."
    "Tai sprinkles some salt on the burgers. He licks the remaining salt off his fingers."
    tai "That's weird."
    tai "That salt legit tastes sweet. But it's not sugar..."
    iona "What's weirder is you just licked your fingers."
    tai "No, that's good luck."
    iona "Um, no, you have to throw it over your shoulder for good luck."
    "Bill puts his hands on his hips and takes an indulgent sniff of the air."
    bill "What's that smell?"
    tai "That's what a cooking burger actually smells like, mate."
    bill "No, I think I can smell something weird coming from the Villa..."
    "Iona sniffs."
    iona "I can't smell anything."
    "Bill turns to you and winks."
    bill "Come and check with me, [s3_name]?"
    thought "Looks like Bill is trying to get me to go with him for a chat!"

    # CHOICE
    menu:
        thought "Should I pretend to check out the weird smell with Bill?"
        "Yeah, sure":
            $ s3e7p2_bill_talk = True
            call s3e7p2_bill_talk from _call_s3e7p2_bill_talk
        "Um... no you're alright":
            s3_mc "What are you going on about?"
            "He winks at you and whispers."
            bill "Go along with it..."
            bill "It smells weird."
            bill "Really weird."
            iona "Right, well go and check it out then."
            bill "I will..."
            "He gestures to you."
            bill "[s3_name]?"
            s3_mc "Nah, you can deal with whatever that is"
            bill "OK. Fine."
            show bill at npc_exit
            pause .3
            $ renpy.hide("bill")
            $ on_screen.remove("bill")
            
            "He sighs and walks off."
            iona "Still can't believe you don't know about throwing salt over your shoulder."
            tai "Why would I waste salt like that?"
            tai "You can leave us to it, [s3_name]."
            tai "We'll have these burgers sorted for you, babe."
            s3_mc "Fine..."

            if len(s3e7p2_visited) == 3:
                iona "They're ready now, to be honest."
                iona "Tai, gather the herd for me."
                tai "Come and get it, Islanders!"
                jump s3e7p2_ending
            else:
                "You wander away, leaving Tai and Iona to their burgers."
    
    return

label s3e7p2_bill_talk:
    bill "Let's go and see what it is!"
    "You follow Bill out to the Villa's front door."

    scene s3-outside-villa-entrance with dissolve
    $ on_screen = []

    s3_mc "How come we're out here?"
    bill "With everyone out back I thought we could hide out front."
    "You both sit down on the steps that lead up to Villa."
    bill "Sorry if it seems like I'm getting all weird and macho around that Tai guy."
    bill "Most of it was just bants."

    if s3_mc.current_partner == "Tai":
        bill "Especially now you're in a couple with him."
        bill "That has put my back up even more."
        bill "But, he does put me on edge a little, you know."
    else:
        bill "But, I guess all these new people are making me anxious."

    s3_mc "That's fair enough, it must be kind of hard having two new guys come in."
    bill "Yeah..."
    bill "You know, me and my brother and sister used to always have barbecues together when we were kids."
    bill "Rain or shine."
    bill "I once made my brother hold an umbrella over me while I tended the grill."
    s3_mc "That's dedication!"
    bill "Yeah, Paul got pretty soaked and the brolly may have, like, caught fire around the edges but..."
    s3_mc "What?"
    bill "I was adamant it wouldn't because it was raining but, yeah, it did."
    bill "The barbecue was banging though, which is really all that matters."
    "Bill kicks a piece of gravel under his feet."
    bill "I think I was just, like, not an easy kid to get on with. If I'm honest."
    bill "Being the middle kid was tough, you know?"

    # CHOICE
    menu:
        thought "Bill thinks being the middle kid is tough..."
        "Yeah, I know it is, I'm a middle kid":
            bill "Aw, then you totally get it."
        "I'd hate it if I was ":
            bill "Aw, then you totally get it."
        "Is this another one of your opinions?":
            bill "Nah, it's been proven, like, scientifically or something."

    bill "You're never sure where you stand in the family because you're not the youngest anymore but you're not the older one either."
    bill "I think I struggle, you know, with people like Tai because of that."
    s3_mc "I mean, Tai was baiting you quite a bit. You should talk to him about it."
    bill "...Yeah, you're right. I'll have a word with him later. Clear the air."
    bill "I'm sure he's just a big joker."
    bill "But that's just it, I like to know where I stand with people and I just don't know with him cos he's such a big personality."
    bill "Speaking of where I stand..."
    "Bill sighs."
    bill "I've got to ask..."
    bill "How do you feel about me, like, right now, [s3_name]?"
    bill "Romantically speaking."

    # CHOICE
    menu:
        thought "How do I feel about Bill right now..."
        "I'm not interested, I really like [s3_mc.current_partner] now":
            $ s3_like_bill = False
            bill "I understand."
        "I really fancy you":
            $ s3e7p2_like_bill = True
            $ s3_like_bill = True
            bill "Yeah."
            bill "I really fancy you too, to be honest."
        "I miss you so much" if 'Bill' in s3_mc.past_partners:
            $ s3e7p2_like_bill = True
            $ s3_like_bill = True
            if s3e6p1_break_up:
                bill "For real?"
                bill "I thought what we had was, like, over."
                s3_mc "Can't a girl change her mind?"
                "Bill grins."
                bill "She sure can."
            else:
                bill "Yeah, I miss you so much too. It's so weird not being together."
        "We're like two ships passing in the night" if 'Bill' not in s3_mc.past_partners:
            bill "You can say that again!"
            bill "Even though that saying makes no sense."
            bill "Ships are lit up like Christmas trees. You can see them for miles! And..."
            s3_mc "Bill."
            bill "Yeah?"
            bill "Oh, right."
            "He rubs the back of his neck."

    "Bill sighs but smiles at you."

    if s3e7p2_like_bill:
        bill "I think I'd also say watch out for anyone called [s3_name]."
        bill "Because she's going to properly get your feelings in a twist."
        bill "It's weird, like, not being together any more.."
        thought "Bill said I get his feelings in a twist!"

        # CHOICE
        menu:
            thought "I should..."
            "Tell him you're with [s3_li]":
                # NEED TO FILL
                "EMPTY"
            "Kiss him passionately":
                $ s3_mc.like("Bill")
                "You bite your lip teasingly."
                s3_mc "I'm sure we can untwist those feelings."
                bill "How do you plan to do that?"
                s3_mc "With a kiss."
                bill "That solves everything."
                "You lean towards him. Your lips meet."
                "His hands clasps yours tightly as you kiss passionately."
                "For a moment everything around you ceases to exist."
                bill "Wow."
                s3_mc "That was amazing."
                bill "Yeah, it was the perfect way to unwind."
                "He leans his head on your shoulder. You both hold hands for a while, playing with each other's fingers."
                "You're not speaking, just enjoying the moment."
            "Hug him tightly":
                $ s3_mc.like("Bill")
                "You wrap your arms around him and hug him tightly."
                bill "Thanks [s3_name]."

    "A low growl comes from Bill's stomach."
    bill "Oops. Sorry."

    if s3e7p2_like_bill:
        bill "All these feelings chat is making me hungry."
    else:
        bill "I'm getting hungry."
    bill "We should probably head back to the others."
    bill "We don't want to miss out on the food."

    if len(s3e7p2_visited) == 3:
        bill "I bet they've finished cooking by now."
        "You both walk back over to the lawn."
        jump s3e7p2_ending
    else:
        bill "I bet they haven't finished cooking quite yet."
        bill "I'm going to go and see if I can give any last minute pointers."
        "You both wander off back into the Villa."

    return

label s3e7p2_kitchen:
    scene s3-kitchen-day with dissolve
    $ on_screen = []
    $ s3e7p2_visited.append("kitchen")

    "Genevieve and Harry are cooking in the kitchen."
    "You breathe in the spiced air that hangs around the kitchen."
    s3_mc "Oh, something smells nice!"
    genevieve "That'll be my jollof rice, babe."
    harry "Actually I think you'll find it's my sandwiches that smell amazing."
    genevieve "What's in those sandwiches?"
    harry "Jam."
    genevieve "And?"
    harry "More jam..."
    genevieve "Uh huh."
    harry "OK, fine."
    "He looks at you."
    harry "Four sandwiches for you [s3_name]!"
    "She sticks out her tongue at him while getting some spices out of the cupboard."
    genevieve "And one for Genevieve."
    genevieve "How will I survive?"
    "She stirs one of the pans filled with rice."
    genevieve "Mind giving that other pan a stir, [s3_name]?"
    genevieve "The one with the orange stuff in it."
    "She starts rummaging around in a cupboard."

    # CHOICE
    menu:
        thought "I should..."
        "Ask her how to spell orange":
            genevieve "Are you being serious?"
            s3_mc "Yeah. Go!"
            genevieve "O- r- a- n- g- e. Orange."
            s3_mc "As your prize I will stir your rice."
            genevieve "Gee, thanks."
        "Stir the pan for Genevieve":
            $ s3e7p2_helped_kitchen = True
            $ s3_mc.like("Genevieve")
            "You stir the strong-smelling rice for Genevieve."
            genevieve "Cheers, doll."
        "Be flirty and sprinkle spices on Harry":
            $ s3_mc.like("Harry")
            "You grab one of the glass bottles of spices and shake it over Harry's hair."
            harry "Um..."
            s3_mc "You're just so spicy."
            harry "You're so hot too."
            "Genevieve chuckles."

    harry "Tomatoes next, right?"
    genevieve "Yeah, and onions, curry powder, and a bit of salt."
    "There is a pile of salt on the kitchen counter. She pinches a tiny amount from the small snowy pile."
    "Harry scrapes in the tomatoes."
    genevieve "Mind chopping those eyes for me, [s3_name]?"
    s3_mc "Eyes?!"
    "Harry covers his eyes with his hands."
    if "Harry" in s3_mc.past_partners or s3_mc.like_mc > 8:
        harry "Stay away from [s3_name]'s pretty eyes, Genevieve!"
    else:
        harry "Stay away from my eyes, Genevieve!"
    genevieve "Sorry, sorry, I meant onions."
    genevieve "We used to call them eyes at home because they make your eyes water."
    harry "Oh... phew. Of course. Silly me."
    "He wipes his face on his arm."
    "You start to chop up the onions. Your eyes instantly start watering."

    # CHOICE
    menu:
        thought "My eyes!"
        "Step away from the onions":
            "In a frenzy of panic, you put the chopping utensils down and step away from the tear-inducing-vegetables."
            genevieve "You alright, [s3_name]?"
            s3_mc "My eyes are, like, falling out."
            genevieve "Don't worry I've got it."
            "She takes over from you."
            genevieve "Next time, try the trick with the spoon in your mouth."
            genevieve "That sometimes works."
            "She quickly pops a spoon in her mouth and expertly chops up the remaining onions."
        "Ask Harry to wipe your tears":
            $ s3_mc.like("Harry")
            s3_mc "Harry..."
            s3_mc "Could you wipe my eyes for me?"
            if "Harry" in s3_mc.past_partners or s3_mc.like_mc > 8:
                harry "Sure, of course, hun!"
                "He grabs some kitchen tissues and gently wipes away your tears."
                "You manage to slice the rest of the onions."
                harry "You alright now, [s3_name]?"
                s3_mc "Yes, I am."
                s3_mc "Thanks to you."
                if s3_mc.current_partner != "Yasmin":
                    "Genevieve scoffs. You both turn round to her. She hides it under a cough. "
                    genevieve "Don't mind me."
            else:
                harry "Um, sure."
                "He hands you a tissue. You stare at it through the bleary eyes."
                harry "Oh, you want me to wipe your face?"
                harry "Yeah, I don't really want to do that..."
                genevieve "I'll do it."
                "Genevieve pats down your face. She has a gentle hand."
                s3_mc "Way to kill a moment, Viv."
                genevieve "Huh?"
                s3_mc "Nevermind."
        "Ask Genevieve for help":
            $ s3_mc.like("Genevieve")
            $ s3e7p2_helped_kitchen = True
            "You manage to work through the tears. The onions are sliced up in no time."
            genevieve "Perfect!"
            genevieve "Thanks [s3_name]."

    harry "How did you learn to cook like this, Genevieve?"
    genevieve "My family are big into cooking."
    genevieve "Not knowing how to cook would be, like, not knowing how to breathe."
    "She pours out the blended sauce into a pan. The room fills with the aroma of fragrant tomato."

    if s3e3p1_teach_harry:
        harry "This is like when [s3_name] taught me to make my breakfast the other day."
        genevieve "Oh? When was that?"
        harry "Um, just the other day."
        s3_mc "Aw, yeah. That was really tasty."
        harry "Yeah, I really appreciate you all, like, giving me this knowledge."
        harry "I never bothered to cook at home."
        genevieve "Cooking's a joy! I'm glad we've both been able to help you."

    genevieve "Right, in about a quarter of an hour, we'll check in the rice and see how it's doing."
    genevieve "Then we'll mix it with the sauce!"
    "She washes her hands under the tap and dries them on a kitchen cloth."

    if "Harry" in s3_mc.past_partners or s3_mc.like_mc > 8:
        if s3e7p2_helped_kitchen:
            genevieve "I knew I could count on you, [s3_name]."
        else:
            genevieve "Thanks for the help you two."
        "Harry is smiling at you, he is grinning from cheek to cheek."
        if s3_mc.current_partner != "Yasmin":
            "Genevieve frowns a little."
    else:
        genevieve "Thanks for the help you two."
        "Harry smiles at Genevieve, blushing a little."

    if len(s3e7p2_visiting) == 3:
        "You hear Tai call from the lawn."
        tai "Food is ready, Islanders."
        tai "Come and get it!"
        "You, Harry and Genevieve walk back over to the lawn."
        jump s3e7p2_ending
    else:
        s3_mc "I'm going to go and see what the others are up to while we wait for the food to be ready."
        harry "Cool."
        genevieve "See you around, babes."
        "You wander off back into the Villa."

    return

label s3e7p2_pool:
    scene s3-poolside-day with dissolve
    $ on_screen = []
    $ s3e7p2_visited.append("pool")

    "AJ's doing some laps in the pool."
    "She sees you and waves."
    aj "Hey, you."
    "She grins at you."

    if s3e6p1_break_up == False and "AJ" in s3_mc.past_partners:
        "She pulls herself out of the pool and sits on the edge beside you."
        s3_mc "How are you holding up?"
        aj "I'm OK."
        aj "Which is, like, code for I miss you so much and I wish I could kiss you right now."
        aj "But yeah, no, really, I'm OK... I'm OK."
        "She leans her head against your shoulder."
        aj "I'm trying not to be, like, really upset about it. But yeah, I miss this."

        # CHOICE
        menu:
            thought "AJ misses me and wishes she could kiss me!"
            "I'm sorry, I like [s3_li] now":
                # NEED TO FILL
                "EMPTY"
            "Why don't you just kiss me?":
                aj "Because..."
                aj "I don't want to be that girl."
                aj "That's something I promised myself when I came here."
                s3_mc "What?"
                aj "I wouldn't let what I want get in the way of what's right."
                aj "And that wouldn't be right. It wouldn't be, like, fair on [s3_li]."
                aj "They're new and, like, I'd be upset if someone did that to me if I was new to the team."
                s3_mc "I think I get what you're saying..."
                aj "I guess while we wait for, like, the right time..."
                aj "We'll have to save these kisses, won't we?"
                s3_mc "Yeah, I guess we will."
                "She kisses her palm, puts it down her bra, and pats her chest."
                aj "I'll keep them close to the heart, you know?"
                "You both laugh at her silliness."
            "I want to kiss you too, but I don't want to upset anyone":
                aj "No, me neither."
                aj "At all."
                aj "I guess while we wait for, like, the right time..."
                aj "We'll have to save these kisses, won't we?"
                s3_mc "Yeah, I guess we will."
                "She kisses her palm, puts it down her bra, and pats her chest."
                aj "I'll keep them close to the heart, you know?"
                "You both laugh at her silliness."
        "She gets up, suddenly, and starts to shake out her arms."
    else:
        aj "Hi!"
        s3_mc "Hey, AJ."
        "You go and sit on the edge of the pool, dangling your legs in the water."
        "She pulls herself out of the pool in one fluid motion, and starts to shake out her arms."

    aj "Argh."
    aj "I've got so much, like, excess energy today."
    aj "I can feel it in my elbows."
    s3_mc "Elbows?"
    aj "Yeah."
    aj "Whenever I'm anxious or anything I get this weird tingly feeling in my elbow joints."
    s3_mc "How come you're anxious?"
    aj "With everything changing with..."
    "She gestures to you."
    aj "You know..."
    s3_mc "Us?"

    if "AJ" in s3_mc.past_partners:
        if s3e6p1_break_up:
            aj "It's hard not to be a little bit anxious when something that I thought was so strong just gets, like, broken."
            s3_mc "You mean us?"
            aj "Yeah..."
            aj "I don't want you to feel, like, bad or anything."
            aj "It's just how I feel."
        else:
            aj "Yeah."
            s3_mc "Well, I still like you, AJ."
            s3_mc "That hasn't changed."
            "She blushes a little."
            aj "Good."
            aj "That's really good."    
    else:
        aj "Not sure... things just feel, like..."
        s3_mc "Different?"
        aj "Yeah. Different. That's the world."
        aj "It's probably the new people and stuff."
        aj "They seem lovely and everything, but, yeah, it's just a bit different."

    "She stretches out her arms behind her."
    aj "Diving competition to burn off some steam before the food is ready?"
    aj "I need to cool off."
    aj "Whoever gets the biggest splash is the winner."
    "Without warning, AJ takes a huge leap and plummets into the pool."
    "She quickly resurfaces, smiling again."
    aj "Come on, [s3_name]. Let's see what you got."

    # CHOICE
    menu:
        thought "Can I do a better dive than that?"
        "Yes...cannonball!":
            "You take a running leap into the pool."
            s3_mc "Ah!"
            aj "Ah!"
            "You make a great splash as you hit the water."
            "AJ laughs loudly."
            s3_mc "It's good to see you smiling again."
            aj "Yeah."
            "AJ starts to swim around you in the pool."
            "You climb out of the pool."
        "Belly flop!":
            "You take a running leap into the pool."
            s3_mc "Ah!"
            aj "Ah!"
            "You make a great splash as you hit the water."
            "AJ laughs loudly."
            s3_mc "It's good to see you smiling again."
            aj "Yeah."
            "AJ starts to swim around you in the pool."
            "You climb out of the pool."
        "No, I don't want to dive":
            aj "Oh, OK."
            "AJ starts to do some laps around the pool again."

    aj "It's amazing how, like, exercise can totally boost my mood sometimes."
    "Sitting back on the edge of the poolside, you watch AJ swim up and down the pool for a while."
    "She pauses and turns to face you."
    aj "Sorry if I don't talk much."
    aj "I'm getting in my chill zone."
    "AJ changes her stroke and starts swimming on her back."
    s3_mc "That's fair enough, hun."

    if len(s3e7p2_visiting) == 3:
        "Suddenly, you hear Tai call from the lawn."
        tai "Food is ready, Islanders."
        tai "Come and get it!"
        "AJ stops swimming. She shakes some water out of her ear."
        aj "Was that what I think it was?"
        s3_mc "Yep. Food is ready."
        aj "Nice one."
        "She clambers out of the water and you both head over to the barbecue."
        jump s3e7p2_ending
    else:
        thought "Guess I ought to leave her to it."

    return

label s3e7p2_beanbags:
    scene s3-bean-bags-day with dissolve
    $ on_screen = []
    $ s3e7p2_visited.append("beanbags")

    "Ciaran, Seb and Nicky are chilling on the beanbags."
    ciaran "Alright, [s3_name]?"

    # CHOICE
    menu:
        thought "Ciaran asked if I'm alright..."
        "I am now I'm with you":
            $ s3_mc.like("Ciaran")
            "Ciaran grins while pushing his hair back."
            ciaran "Me too."
            "He brushes off a beanbag beside him."
            ciaran "Come sit next to me, if you want to."
            "You sit down beside him in a comfy beanbag."
        "Yeah, I'm OK, thanks":
            "You nod."
            s3_mc "I'm alright."
            ciaran "Good."
            "You slump down beside the boys in a beanbag."
        "I'm hungry":
            "You flop down on a beanbag and sigh."
            s3_mc "I'm hungry."
            seb "You and me both, [s3_name]."

    seb "I'm starving."
    nicky "I don't think the food will be ready for a while."
    "Seb groans."
    nicky "Hey, quit moaning."
    nicky "It's not like we're over there helping."
    ciaran "Yeah, I've got to admit."
    ciaran "I'm just not one of those people who, like, likes to deal with a barbecue."
    ciaran "It's just too hot for me."

    # CHOICE
    menu:
        thought "Ciaran says the barbecue is too hot for him..."
        "That's because he's barbecute":
            nicky "Barbe what?"
            s3_mc "Cute."
            s3_mc "Barbecute."
            "Ciaran laughs, blushing a little."
            ciaran "[s3_name], if you were a keyboard, it would just have two letters."
            ciaran "'Q' and 'T'."
            nicky "Wow."
            seb "I don't get it."
            seb "Those letters aren't in that word, like, at all."
            s3_mc "The letters 'Q' 'T' sound like cutie when read together."
            nicky "Don't worry Seb, this is a young man's game."
        "Ciaran is too hot for me":
            $ s3e7p2_ciaran_hot = True
            s3_mc "The only thing too around here is you, Ciaran."
            "You fan yourself. Nicky and Seb laugh as Ciaran goes bright red."
            ciaran "Wow, gee, thanks, [s3_name]."
            ciaran "I don't know what to say to that..."
            "He strokes his chin in contemplation."
            ciaran "Have you got any sunglasses?"
            s3_mc "No."
            ciaran "Shame, because I need them to look at you."
            ciaran "You're hotter than the sun in my eyes."
            "Seb and Nicky high five Ciaran."
            seb "Very smooth."
        "Barbecuing is not that bad":
            ciaran "I know, I know..."

    nicky "Seriously though, barbecuing isn't all that."
    nicky "I don't see why people want to have a fire when it's this hot already."
    ciaran "Yeah, it's so weird to stick yourself in front of a burning fire when the sun is roasting you enough."
    ciaran "And besides, I'm seriously not used to any of this heat."
    if s3e7p2_ciaran_hot:
        "He smiles at you."
    ciaran "It never stops raining in Ireland."

    # CHOICE
    menu:
        thought "Ciaran is talking about Ireland..."
        "I'd love to visit you one day":
            $ s3_mc.like("Ciaran")
            ciaran "That, would be, like, totally grand."
            if s3e6p1_walk:
                ciaran "I can take you on an actual tour of Waterford!"
            else:
                ciaran "I live in the oldest city in Ireland so we've got plenty of history to show you."
                ciaran "Or maybe we could, like, do a road trip around the whole of Ireland!"
                s3_mc "Yes! I'd actually, like, proper love that."
        "You're right, Ireland is lovely and wet":
            ciaran "Wet and lovely!"
            ciaran "Just the way I like it!"
            s3_mc "You like it wet and lovely, eh?"
            ciaran "Huh?"
            s3_mc "Nevermind..."
        "Do you ever talk about anything else?":
            $ s3_mc.dislike("Ciaran")
            nicky "Woah, harsh, [s3_name]!"
            ciaran "Sorry..."
            ciaran "Um..."
            ciaran "My dog?"
            s3_mc "Next!"

    "Seb shades his eyes from the sun with his hands."
    seb "I actually miss the rain a little bit."
    nicky "Nah, mate."
    nicky "That's just what the rain wants you to think."
    nicky "It's like when it rains a lot..."
    nicky "Then you'll miss the sun."
    ciaran "Yeah, I think it's easy to always end up wishing for the thing you don't have."
    ciaran "But I'm with [s3_name], so I won't be wishing for anything else any time soon."
    "He gives you the biggest smile."

    if s3e5p2_confess_attraction_ciaran and s3_mc.current_partner != "Ciaran":
        ciaran "I know that feeling all too well..."
        "He sighs and smiles sadly at you."
        
    nicky "Nah, we just get, like, way too bored with things way too quickly."
    nicky "We think we want something else, and then as soon as we get it, we're ready for whatever comes after that."

    # CHOICE
    menu:
        thought "I think..."
        "We wish for what we don't have too much":
            s3_mc "You're right Ciaran."
            s3_mc "It's easy to fall into that trap."
            "Ciaran nods."
            ciaran "I know all about that..."
        "We all get bored too easily":
            s3_mc "Yeah, Nicky, you've hit the nail on the head."
            s3_mc "We're always wanting to move onto the next thing before we've even finished or properly learnt to enjoy what's happening, like... now."
            ciaran "I guess you're right."
        "You're both overthinking things":
            s3_mc "Can't we just enjoy the fun day of barbecuing for what it is meant to be?"
            s3_mc "Fun!"
            seb "Surprisingly, I second that."

    if len(s3e7p2_visiting) == 3:
        "Suddenly, you hear Tai call from the lawn."
        tai "Food is ready, Islanders."
        tai "Come and get it!"
        seb "Saved by the bell."
        seb "Right, help me up, Nicky."
        nicky "Yeah, suppose we better eat this grub  then."
        "You all get up and walk back over to the lawn."
        jump s3e7p2_ending
    else:
        seb "And on that deep note..."
        seb "I'm going to get some water."
        nicky "Yeah, all these deep talks are making me hella thirsty."
        ciaran "Aw, fill me up too, Seb?"
        "He waves his water bottle over in Seb's direction."
        seb "Nah, get your own hot stuff."
        ciaran "Fine..."
        seb "See you later, [s3_name]."
        s3_mc "See you lot soon."
        "They all get up and wander back to the Villa."
        "You head off to find the others."

    return

label s3e7p2_ending:
    scene s3-lawn-bbq with dissolve
    $ on_screen = []

    "Everyone makes their way over to the barbecue."
    bill "Food, food, food."
    "Bill is still chanting loudly."
    bill "Food, food, food."
    iona "The next person to say food gets none."

    # CHOICE
    menu:
        thought "The food is ready..."
        "Say it smells nice":
            $ s3_mc.like("Tai")
            $ s3_mc.like("Iona")
            "You sniff."
            s3_mc "This smells delicious."
            tai "Thanks [s3_name]."
            "Tai hands you a plate. Bill grabs one and helps himself."
            iona "Yeah, it'll be good."
        "Chant 'Food'!":
            $ s3_mc.like("Tai")
            $ s3_mc.dislike("Iona")
            s3_mc "Food, food, food."
            "Iona rolls her eyes and reluctantly hands you and Bill a plate."
        "Demand seconds":
            bill "Me too! Food!"
            "Iona hands you and Bill a plate."
            iona "You haven't even had your first lot, yet!"

    "Seb looks suspiciously at the sausages."
    seb "Did you make the food, mate?"
    bill "Um, no. Not really."
    seb "Good."
    iona "Did you find out what that weird smell was, Bill?"
    bill "What?"
    bill "Oh, that. Nah, must have been something in the air."
    if s3e7p2_bill_talk:
        "He looks at you."
    genevieve "Food, food, food."
    "Genevieve and Harry come over. Genevieve is carrying her Jollof rice. Harry carries a plate of plain looking sandwiches."

    if s3_li != "Yasmin":
        miki "I think that combination perfectly embodies your relationship."
        genevieve "What do you mean?"
        miki "You guys are such a funny combo!"
        miki "Your personalities seem like complete opposites."
        "Genevieve and Harry laugh, placing their food down on the rug."

        if "Harry" not in s3_mc.past_partners:
            harry "Maybe we're like one of those weird food combos that actually taste amazing."
            genevieve "Like jam and cheese."
            "Harry's face screws up in disgust."
            harry "That sounds criminal."
        else:
            "Harry glances in your direction and gives you an awkward smile."
            harry "Yeah... I know what you mean."

    "Everybody starts tucking into the food."
    elladine "This is delish, thanks you lot."
    miki "Yeah, proper well done."
    bill "I could have done a better job."
    iona "Put a sausage in it, Bill."
    bill "Nah, I'm joking. It is pretty good."
    "[s3_li] comes over, carrying [his_her] plate."
    s3_li "Hey."
    "[s3_ex] glances over at you."
    s3_li "Mind if I sit next to you?"

    # CHOICE
    menu:
        thought "Can [s3_li] sit next to me?"
        "Go for it":
            $ s3_mc.like(s3_li)
            s3_li "Thanks!"
        "Yeah, I saved it for you":
            $ s3_mc.like(s3_li)
            s3_li "Thanks!"
        "Nah, that seat is saved for [s3_ex]":
            $ pronouns(s3_li)
            $ s3_mc.like(s3_ex)
            $ s3_mc.dislike(s3_li)
            s3_li "Oh, OK."
            "[s3_li] plonks [him_her]self beside Seb. [s3_ex] scooches over so he's/she's sitting beside you."
            s3_ex "Room for a little one?"
            s3_mc "There's always room for you."

    bill "Someone pass us the ketchup?"
    "Genevieve hands the ketchup bottle to Bill. He squirts a big dollop on his sausage and takes a big bite."
    bill "Um..."
    "His face goes bright red. He starts to fan his mouth."
    bill "Ouch!"
    "Camilo dips his sausage in the remainder of the red sauce on Bill's plate."
    bill "Why is this ketchup spicy?"
    camilo "It's not ketchup."
    camilo "It's hot sauce."
    iona "The Shiny Demon strikes again."
    bill "What!?"
    bill "Ah, I've got a text. I can't read it. Too Spicy."
    "Camilo laughs at Bill and takes his phone off him. Bill grabs his water bottle in an attempt to cool his burning mouth."
    camilo "Um..."
    "Camilo's face drops."
    miki "What does it say?"
    text "Islanders, the public have been voting to save the couples they deem most compatible."
    text "The couples with the least votes will be in danger of leaving the island tonight."
    iona "O.M.G."
    "Tai looks shocked, and for a moment, a little smaller in size."
    tai "You what?"
    bill "It's a dumping..."
    ciaran "One of the couples could be going home..."

    scene sand with dissolve
    $ on_screen = []
    "Coming up..."
    "I hope the Islander's don't get the hump..."
    camilo "I hope you have some good news for us..."
    "Because..."
    miki "At least one of us is getting dumped!"

    jump s3e7p3
    return

#########################################################################
## Episode 7, Part 3
#########################################################################
label s3e7p3:
    scene sand with dissolve
    $ on_screen = []

    show screen day_title(7, 3) with Pause(4)
    hide screen day_title with dissolve

    "Welcome back to Love Island, or whatever..."
    "Earlier, our Islanders sampled Bill and Tai's meat"
    "Which was handled with care by Iona..."
    tai "You've got to have a good girthy flame or else it won't cook!"
    bill "Girthy flames are not a thing. What are you on about?"
    tai "Yeah, you wouldn't know..."
    show tai at npc_exit
    show bill at npc_exit
    pause .3
    $ renpy.hide("tai")
    $ renpy.hide("bill")
    $ on_screen = []

    "Note to self, look up 'girthy flame' later. Safe search on."
    "But not even our Islanders' cooking could fix what was about to happen..."
    elladine "I don't want to make this decision."
    iona "You don't have a choice, babe."
    bill "Mate..."
    show iona at npc_exit
    show bill at npc_exit
    pause .3
    $ renpy.hide("iona")
    $ renpy.hide("bill")
    $ on_screen = []

    "Sigh, sorry if my energy is a little off."
    "This dumping really has me down in the..."
    "...dumps."
    "Coming up, I guess..."
    "The Islanders worry about who's getting dumped..."
    miki "What if it's me?"
    show miki at npc_exit
    pause .3
    $ renpy.hide("miki")
    $ on_screen = []

    $ outfit = "evening"
    "And we say goodbye to one of the couples."
    bill "Mate..."
    show bill at npc_exit
    pause .3
    $ renpy.hide("bill")

    $ outfit = "evening"
    scene s3-dressing-room with dissolve
    $ on_screen = []

    "All around you, the girls are putting makeup on, zipping up dresses, and sorting out their hair."
    "It's quiet."
    "Too quiet..."

    # CHOICE
    menu:
        thought "You could hear a pin drop in this room right now."
        "Get a conversation going":
            "You clear your throat and start to speak."
            s3_mc "So... books are great, yeah?"
            miki "Huh?"
            s3_mc "You know. They have, like, so much information in them."
            s3_mc "And they're made of trees which is so weird to think about."
            s3_mc "Like, humans looked at a tree one day and were like, 'I'm going to turn that into my nan's chicken stew recipe.'"
            elladine "That is pretty bizarre when you think about it."
            "The conversation dies down again."
            thought "That was short-lived..."
        "Tell the group a riddle":
            s3_mc "Hey! I have a riddle for everyone."
            "Some of the girls groan."
            iona "Can't go wrong with a good riddle."
            iona "It better be a hard one."
            s3_mc "What goes in hard, comes out soft, and can be blown?"
            "Iona smirks."
            elladine "It's glass!"
            s3_mc "Ooh, that's a good answer, but not the one I'm looking for."
            aj "Bubble gum?"
            s3_mc "Correct!"
            aj "Really? I never get riddles."
            "The conversation dies down again."
            thought "That was short-lived..."
        "Let the silence linger...":
            "The silence carries on. Somewhere in the room, you hear a tiny ping."
            elladine "Damn, dropped my hairpin."

    s3_mc "It's so quiet in here tonight."
    miki "Huh?"
    miki "Oh, sorry, babes."
    miki "I guess everyone's just worried about the dumping."
    miki "What if it's me? I haven't found love yet..."
    genevieve "That's not going to happen, hun."
    miki "But it could!"
    iona "Don't feel like that, babes."
    iona "You're so strong, and smart, you'll smash it on the outside if you get booted."
    iona "Trust me, I'm going to be like, 'Look out, Aberdeen! Here I come.'"
    aj "Just Aberdeen?"
    iona "You've got to start with realistic goals, babes. The world will follow."
    "Elladine sighs."
    elladine "Starting with realistic goals in life... a woman after my own heart."

    # CHOICE
    menu:
        thought "If I get voted off I'll..."
        "Focus on my career":
            $ s3_mc.like("Elladine")
            s3_mc "I'm proud to be a [s3_mc.job!l] and this experience has made me realise how much I want to get back to it."
            elladine "Good for you, girl!"
        "Cry for days and eat a huge cake":
            $ s3_mc.dislike("Miki")
            s3_mc "Get all my gals round and just open the floodgates..."
            miki "Aw, no, [s3_name]! I'm sure you'll be fine."
        "Own the world like Iona":
            $ s3_mc.like("Iona")
            s3_mc "You'll see me on every TV ad, glossy mag cover, and Christmas number one."
            if s3_mc.job == "Musician":
                s3_mc "I'll be the next Adele or Mariah!"
            else:
                s3_mc "My lack of musical talent won't hold me back!"

    iona "Yas, queen! That's the energy we need in here."

    if s3_li == "Yasmin":
        "Yasmin looks over at you."
        yasmin "Don't worry, babe, whatever happens, I'll be there for you."
    else:
        miki "Don't worry, babe. Whatever happens, we'll be there for you."

    iona "Alright, let's get ready and get out there to face whatever comes our way."
    thought "This could be my last evening in the Villa."
    thought "I should put in the extra effort to go out stunning..."
    # Add back once MC images in game
    # Outfit change to evening wear
    thought "This outfit's one of my favourites. Let's put it to good use tonight."
    iona "Girl, you look great tonight. Wish I had that natural beauty."
    "You wink at her."
    # thought "Doesn't matter what happens tonight. Not when I look this fierce."
    # iona "Damn, girl! I wish I could look half as good as you. (you get 🤩 with Iona)"
    # "You wink at her."
    # thought "This old thing will have to do."
    # yasmin "You must have a lot of confidence, MC, that you don't need to dress up too much."
    # yasmin "Though I suppose you have the natural beauty to back it up."
    s3_mc "I guess we should get a move on."
    iona "Come at me, destiny! I'm ready."

    scene s3-firepit-night with dissolve
    $ on_screen = []

    "The Islanders have made their way to their doom."
    "Dumping."
    "Doomping?"
    "Ugh, sorry, I'm still distracted."
    "I just don't want to say goodbye to any of my friends! Like Nicky or Bill, or even... [s3_name]!"
    "And yes, they are my friends, even if they don't know I exist."
    "With the amount of time I spend watching them, I'd say we're besties at this point..."
    
    $ pronouns(s3_li)
    "You gather round the firepit in your couples."
    if s3e6p3_loyal:
        "[s3_li] stands next to you, clasping [his_her] hands together."
    else:
        "[s3_li] takes a hold of your hand and gives it a small squeeze."
        s3_li "For luck."
    "You look around. The others seem nervous."
    "Even Iona seems to be losing her cool as she gently cracks her knuckles."
    "The fire flickers harshly in a gust of wind. Then you hear a loud ding as your phone goes off."
    s3_mc "I got a text...."
    miki "Read it out, babes."
    miki "It's me, isn't it?"
    bill "Hey, don't say that. We'll get through this..."
    text "Islanders, the public have been voting for their favourite couples. The couples with the least votes are in danger of being dumped from the Island."
    text "The two couples who received the fewest votes are..."
    text "Camilo and Iona."
    text "Miki and Bill."
    "There's a brief moment of silence before another phone pings."
    nicky "That's mine..."
    text "For one of these two couples, their time in the Villa has come to an end."
    text "The rest of you must now vote for which couple should be going home tonight. #whatthepublicwants #theshowmustgoon"
    miki "I knew it."
    bill "Mate..."

    # CHOICE
    menu:
        thought "Miki, Bill, Iona and Camilo are up for dumping..."
        "I'm so relieved it isn't me and [s3_li]...":
            s3_li "Shh, babe. Don't let them hear you say that."
            s3_li "This is tough enough on everyone."
        "I don't want to vote for any of them!":
            s3_mc "We've all become such good mates. This hurts..."
            miki "Thanks, babes. You're too sweet sometimes."
            camilo "Yeah..."
        "Mate...":
            camilo "Mate..."
            iona "Mate..."
            miki "Mate..."
            genevieve "Mate!"
            nicky "We're all mates now. That's what makes this so hard..."

    elladine "I don't want to make this decision."
    iona "You don't have a choice, babe."
    "She stifles a half laugh, half sob."
    iona "Look, I know I had all this big V energy in the dressing room, but now I'm actually facing this dumping... it hurts, guys."
    "Camilo gives her a reassuring hug."
    bill "You know, this is the problem I have with public votes."
    bill "They always choose the wrong option."
    "Silence follows for a moment."
    camilo "Alright you lot, there's no point standing around."
    camilo "You need to go and decide who you're voting for."
    bill "Do better than the public!"
    "Miki pulls a dramatic sad face."
    miki "Remember me like this when you're voting."
    miki "Would you kick anyone off who's this adorable?"
    "[s3_li] pulls you away from the others."
    s3_li "Come on then, babe. We have a decision to make..."

    scene s3-poolside-night with dissolve
    $ on_screen = []

    "You and [s3_li] make your way to the pool."
    "The sound of the calm water lapping the poolside is a stark contrast to the crackle of the firepit."
    s3_li "This is a much better place to try and decide who to send home."

    # CHOICE
    menu:
        s3_mc "I can't believe that we..."
        "Have to dump our friends":
            s3_li "Yeah..."
            s3_li "I know I've only been here for a couple of days, but this is tough."
            s3_li "How do you end someone's summer of love?"
        "Weren't up to be dumped":
            $ s3_mc.dislike(s3_li)
            s3_li "Hey, I know we're a recent couple, but the public clearly see that there's something good going on here."
            s3_li "Don't do us down like that."
        "Haven't done it in the pool yet":
            if s3e5p2_waterfall_bits and s3_li == "Tai":
                s3_li "Behind a waterfall wasn't enough?"
            s3_li "Hey, there's still time..."

    "You both look down at your phone."
    s3_li "Look, you've known those four longer than me."
    s3_li "Bounce your thoughts off me, but I think it should be your call."

    if s3_mc.past_partners[1] == "Bill" or s3_mc.past_partners[1] == "Camilo":
        s3_li "For what it's worth, you and [s3_mc.past_partners[1]] were coupled before I, um, stole you away..."
        if s3e6p3_loyal or (s3_li == "Yasmin" and s3_like_yasmin == False) or (s3_li == "Tai" and s3_like_tai == False) or (s3_li == "Ciaran" and s3_like_ciaran == False):
            s3_li "And I know you two still hold a torch for each other."
            s3_li "Unlike me and you, so I will understand if you want to save him for that reason."
        else:
            s3_li "But the two of you seem to have moved on."
            s3_li "Although, I'd understand if you want to save him as a mate."
    else:
        s3_li "I don't know what your personal feelings are for either of the couples."
        s3_li "I guess it comes down to who you get on with the most?"
        s3_li "So, I guess the first thing to ask, really, is who do you think has a more solid relationship?"

    # CHOICE
    menu:
        s3_mc "The couple with the best relationship is..."
        "Camilo and Iona":
            if ("Camilo" in s3_mc.past_partners and s3_like_camilo) or s3_mc.like_mc["Camilo"] > 8: 
                s3_li "Really?"
                s3_li "I get the feeling that Iona is way more into Camilo than he is her."
                s3_li "I feel like he's got his eye on someone else..."
            else:
                s3_li "They definitely seem to have a hard time to keep their hands off of each other."
                s3_li "I mean, I've been woken up by their bed springs squeaking enough times..."
                s3_li "But do you think it's deeper than just sex?"
        "Bill and Miki":
            if ("Bill" in s3_mc.past_partners and s3_like_bill) or s3_mc.like_mc["Bill"] > 8:
                s3_li "Really?"
                s3_li "Neither seem to get one another, or be very interested in doing so."
                s3_li "I feel like he's got his eye on someone else..."
            else:
                s3_li "I think they had a rocky start, but it looks like they're starting to understand one another."
                s3_li "Miki's even been laughing at Bill's jokes!"
                s3_li "It's kinda sweet..."
        "Um, I have no idea...":
            s3_li "Yeah, it's a tough one."

    s3_li "Alright, let's look at it a different way."
    s3_li "Is there one person in particular you want to save? You know, who you get on with the most."

    # CHOICE
    menu:
        s3_mc "The person I want to save the most is..."
        "Camilo":
            s3_li "He's a sweetheart, I can see why."
            s3_li "That means you'd also be saving Iona."
        "Bill":
            s3_li "The man with many opinions, eh? Interesting choice."
            s3_li "That means you'd also be saving Miki."
        "Miki":
            s3_li "The drama! Being saved like this would be another chapter in her own Telenovela."
            s3_li "That means you'd also be saving Bill."
        "Iona":
            s3_li "I don't think I've ever met such a salty person in my life. I'd miss her quips if she left."
            s3_li "That means you'd also be saving Camilo."

    # CHOICE
    menu:
        s3_mc "That's..."
        "Good, I want to keep them both":
            s3_li "Alright, then."
        "A shame, but the way it has to be":
            s3_li "I won't tell them you said that."
        "Not exactly what I want":
            s3_li "I won't tell them you said that."

    s3_li "Sounds like you made up your mind..."
    s3_mc "I have."

    # CHOICE
    menu:
        thought "I want to dump..."
        "Bill and Miki":
            $ s3e7p3_dump_m = "Bill"
            $ s3e7p3_dump_f = "Miki"

            $ s3e7p3_stay_m = "Camilo"
            $ s3e7p3_stay_f = "Iona"
            $ s3_other_m = "Camilo"
            $ s3_other_f = "Iona"
        "Camilo and Iona":
            $ s3e7p3_dump_m = "Camilo"
            $ s3e7p3_dump_f = "Iona"

            $ s3e7p3_stay_m = "Bill"
            $ s3e7p3_stay_f = "Miki"
            $ s3_other_m = "Bill"
            $ s3_other_f = "Miki"


    s3_li "That's it then. I'll support you all the way."
    s3_li "Do you want me to send the text or do you want to send it?"

    # CHOICE
    menu:
        thought "Who should send the text?"
        "I'll do it":
            s3_li "Alright."
            "You type [s3e7p3_dump_m] and [s3e7p3_dump_f]'s name into the phone and hit send."
        "You do it":
            s3_li "Of course, babe."
            "[s3_li] takes the phone from your hand and types [s3e7p3_dump_m] and [s3e7p3_dump_f]'s name into it. [he_she!c] hits send."
        "Let's both do it":
            s3_li "Um, it could be tricky, but OK..."
            "The two of you try to type on the same keypad."
            "You misspell a bunch of words, including [s3e7p3_dump_m]'s name, but eventually you finish the text and hit send."

    "Two blue ticks flash up next to the message."
    s3_li "I guess that's that then."

    # CHOICE
    menu:
        s3_mc "Yep. It's done..."
        "Ask for a cuddle":
            s3_mc "Can I have a hug?"
            s3_li "You don't have to ask, babe."
            "[s3_li] puts [his_her] arms around and pulls you into a warm embrace."
            s3_li "It was a tough call..."
        "Say good riddance":
            s3_mc "Goodbye ti bad rubbish."
            s3_li "Woah! That was too harsh, babe..."
            "You shrug."
        "Burst into tears":
            $ s3e7p3_cry = True
            "You let out several large, wet, sobs."
            "[s3_li] puts an arm round your shoulders and gives you a reassuring squeeze."
            s3_li "It was a tough call..."

    "You see Elladine and Nicky heading back to the firepit."
    s3_li "Guess the others have made up their minds, too. Let's head back..."

    scene s3-firepit-night with dissolve
    $ on_screen = []

    "You and the rest of the Islanders gather back round the firepit."
    "Bill, Miki, Camilo and Iona are in the same spot as before."
    camilo "Oh, hey, guys. Fancy seeing you here."
    camilo "Hope you have some good news for us..."
    $ leaving("camilo")

    $ pronouns(s3_bff)
    "[s3_bff] stands next to you. [he_she!c] smiles weakly at you before leaning over to whisper in your ear."
    s3_bff "Who did you vote for?"

    # CHOICE
    menu:
        thought "[s3_bff] wants to know who I voted for..."
        "Tell the truth":
            s3_mc "I voted for [s3e7p3_dump]."
            if s3e7p3_dump_m == "Bill":
                if s3_mc.like_mc["Bill"] > 8 or s3_mc.like_mc["Camilo"] > 8:
                    if s3_mc.like_mc["Bill"] > s3_mc.like_mc["Camilo"]:
                        s3_bff "Really? That surprises me. I thought you two were sweet for each other."
                        s3_bff "I voted for Camilo for that reason."
                    else:
                        s3_bff "Same. But that's because I know you and Camilo are still sweet on each other."
                else:
                    s3_bff "Yeah, same. I think Bill and Miki have more going for them."
            else:
                if s3_mc.like_mc["Bill"] > 8 or s3_mc.like_mc["Camilo"] > 8:
                    if s3_mc.like_mc["Bill"] < s3_mc.like_mc["Camilo"]:
                        s3_bff "Really? That surprises me. I thought you two were sweet for each other."
                        s3_bff "I voted for Bill for that reason."
                    else:
                        s3_bff "Same. But that's because I know you and Bill are still sweet on each other."
                else:
                    s3_bff "Yeah, same. I think Camilo and Iona have more going for them."
        "Refuse to answer the question":
            s3_mc "I don't want to tell anyone, sorry."
            s3_bff "That's smart, to be honest. Keeps the drama at bay."
        "Burst into tears":
            "You dab your eyes as the tears stream down."
            s3_bff "Oh no, don't cry, girl..."
            if s3e7p3_cry:
                s3_li "Aw, babe. I hate to see you crying again."
            else:
                s3_li "Aww, babe. Come here."
            "[s3_li] gives you a reassuring hug."
            s3_mc "This whole situation is the worst!"

    "The Islanders stand round the firepit, nervous and sad glances are thrown around."
    if s3e7p3_dump_m == "Camilo":
        "Suddenly Camilo's phone goes off."
        camilo "Oh, here we go..."
    else:
        "Suddenly Bill's phone goes off."
        bill "Oh, here we go..."

    text "[s3e7p3_dump_m] and [s3e7p3_dump_f], your fellow Islanders have voted you the least compatible couple. As a result you will now be dumped from the Island."
    text "Please go and pack your bags and make your way to the Villa entrance. #sorrytoseeyougo #dontforgettowrite"
    "Stunned silence follows."

    if s3e7p3_dump_m == "Camilo":
        camilo "There it is, then..."
        "Iona starts to cry."
        iona "I wasn't ready to leave..."
        "Camilo pulls her into a comforting embrace. The other Islanders gather round the couple and all hug them too."
    else:
        bill "There it is, then..."
        "Miki starts to cry."
        miki "I wasn't ready to leave..."
        "Bill pulls her into a comforting embrace. The other Islanders gather round the couple and all hug them too."

    $ pronouns(s3_li)
    # CHOICE
    menu:
        thought "I'm going to..."
        "Stay where I am":
            "You stand still. [s3_li] goes to move, but when [he_she] sees you, [he_she] stays in place too."
        "Go and hug them":
            "You make your way to the group with [s3_li] and wrap your arms around everyone."
        "Burst into tears":
            "The sobs fall hard and fast. [s3_li] is about to go over to the group when [he_she] sees you."
            "[s3_li] rubs your back."
            s3_li "It's OK, babe. Let it all out."

    if s3e7p3_dump_m == "Camilo":
        "Eventually the hugging stops. Bill and Miki both let out a sigh of relief."
        iona "Well, I guess we should go and pack our things."
        "Camilo wipes his face with his arms and sniffs."
        camilo "Yeah, those suitcases aren't going to do it themselves."
    else:
        "Eventually the hugging stops. Camilo and Iona both let out a sigh of relief."
        miki "Well, I guess we should go and pack our things."
        "Bill wipes his face with his arms and sniffs."
        bill "Yeah, those suitcases aren't going to do it themselves."

    thought "I know I voted for them to go, but..."
    thought "It's sad thinking that this could be my last chance to hang out with them in the Villa."
    thought "I'd better make this next half hour count."

    # CHOICE
    menu:
        thought "Should I offer to help pack their bags, so we can spend a little more time together?"
        "Yes, I want to hang out with them one last time":
            $ s3e7p3_help_pack = True
            call s3e7p3_help_pack from _call_s3e7p3_help_pack
        "Nah, I hate packing suitcases...":
            thought "I really, really hate packing bags"
            thought "There's no way I'm doing it."
            "As [s3e7p3_dump] head upstairs to pack, you and the others head outside to wait for them at the entrance."

    "Like the awkward couple who leave a party before anyone else, [s3e7p3_dump_m] and [s3e7p3_dump_f] make their way out of the Villa..."
    "With every other Islander lined up to say goodbye and applaud them."
    "Just like how everyone cheers when I leave a room."
    "That's normal, right?"
    "Right?"

    scene s3-outside-villa-entrance-night with dissolve
    $ on_screen = []

    if s3e7p3_help_pack:
        "You walk out of the Villa's main doors before [s3e7p3_dump_m] and [s3e7p3_dump_f] and go stand next to [s3_li]."
    else:
        "You stand outside the Villa's main doors next to [s3_li], waiting for [s3e7p3_dump_m] and [s3e7p3_dump_f] to come out."
        "They emerge with their suitcases in tow and everyone cheers."

    # CHOICE
    menu:
        thought "I'm going to..."
        "Cheer for them, too":
            "You join in with the applause and outcry of support for the couple."
            "[s3e7p3_dump_m] turns to you and smiles."
        "Remain silent":
            "You remain standing impassively while the others around you continue to shout cries of support to the couple."
            "[s3e7p3_dump_m] turns to you and frowns."
        "Hug [s3_li] for comfort":
            $ s3_mc.like(s3_li)
            "You wrap your arms around [s3_li]'s waist and squeeze it gently."
            "[he_she!c] does the same back to you and rests [his_her] head against yours."

    "[s3e7p3_dump_m] and [s3e7p3_dump_f] walk past everyone, waving."
    "You can see the glisten of tears in their eyes."

    if s3e7p3_dump_f == "Miki":
        "[s3e7p3_dump_f] pauses, glances over at Iona and speaks to you quietly."
        miki "Please can you do one last thing for me?"
        s3_mc "Yeah?"
        miki "Make sure Iona's alright. Like, I don't want her to slip into the background."
        miki "Not that I think she will! I mean, she's not the kind of girl you miss."
        miki "But we were close and I don't want her to go all quiet because I'm no longer here..."
    else:
        "[s3e7p3_dump_f] pauses, glances over at Miki and speaks to you quietly."
        iona "Please can you do one last thing for me?"
        s3_mc "Yeah?"
        iona "Make sure Miki's alright. Like, I don't want her to slip into the background."
        iona "Not that I think she will! I mean, she's not the kind of girl you miss."
        iona "But we were close and I don't want her to go all quiet because I'm no longer here..."

    # CHOICE
    menu:
        thought "I..."
        "Will make sure she doesn't":
            $ s3_mc.like(s3e7p3_dump_f)
            if s3e7p3_dump_f == "Miki":
                miki "Thanks, babes, I knew you would. That makes me feel better."
            else:
                iona "Thanks, babes, I knew you would. That makes me feel better."
        "Need to focus on myself":
            $ s3_mc.dislike(s3e7p3_dump_f)
            if s3e7p3_dump_f == "Miki":
                miki "Oh.. fair enough."
                miki "Thanks for being honest at least..."
            else:
                iona "Oh.. fair enough."
                iona "Thanks for being honest at least..."
        "Can't make any promises...":
            $ s3_mc.dislike(s3e7p3_dump_f)
            if s3e7p3_dump_f == "Miki":
                miki "Oh.. fair enough."
                miki "Thanks for being honest at least..."
            else:
                iona "Oh.. fair enough."
                iona "Thanks for being honest at least..."

    "She smiles over at [s3e7p3_dump_m] and goes back to join him."
    "As they pass, you see a paper sign stuck to the back of [s3e7p3_dump_m] which reads 'Just Married'."
    "The other Islanders start to laugh."

    if s3e7p3_dump_m == "Bill":
        bill "What's so funny?"
    else:
        camilo "What's so funny?"

    elladine "I think the Shiny Demon has struck again..."

    if s3e7p3_dump_f == "Miki":
        miki "Oh no... babe, they got you."
    else:
        iona "Oh no... babe, they got you."

    "[s3e7p3_dump_m] reaches behind himself and pulls the note off. He laughs at it."

    if s3e7p3_dump_m == "Bill":
        bill "Alright, as a favour to us dumpees, please tell us, who was the Shiny Demon?"
    else:
        camilo "Alright, as a favour to us dumpees, please tell us, who was the Shiny Demon?"

    # CHOICE
    menu:
        s3_mc "It's obviously..."
        "Iona" if s3e7p3_dump_f != 'Iona':
            # NEED TO FILL
            "EMPTY"
        "Miki" if s3e7p3_dump_f != 'Miki':
            # NEED TO FILL
            "EMPTY"
        "Bill" if s3e7p3_dump_m != 'Bill':
            bill "It really isn't."
            bill "I'd have admitted to it by now and taken all the credit..."
        "Camilo" if s3e7p3_dump_m != 'Camilo':
            camilo "It really isn't."
            camilo "I'd have admitted to it by now and taken all the credit..."
        "Tai":
            "He shakes his head."
            s3_mc "How is it not you?"
        "Ciaran":
            "He shakes his head."
            s3_mc "How is it not you?"
        "Nicky":
            "He shakes his head."
            s3_mc "How is it not you?"
        "Seb":
            "He shakes his head."
            s3_mc "How is it not you?"
        "Yasmin":
            "She shrugs her shoulders."
            s3_mc "How is it not you?"
        "Elladine":
            "She shrugs her shoulders."
            s3_mc "How is it not you?"
        "Genevieve":
            pass
        "Harry":
            harry "It really isn't."
            harry "I'd have admitted to it by now and taken all the credit..."
        "AJ":
            aj "It really isn't."
            aj "I'd have admitted to it by now and taken all the credit..."

    "A mischievous grin spreads across Genevieve's face. She tents her fingers together and laughs villainously."
    genevieve "Mwa-hah-hah..."
    elladine "Genevieve, it was you?"
    genevieve "It was! I was the Shiny Demon..."

    if s3e7p3_dump_m == "Bill":
        bill "What? I'd never have guessed!"
        miki "I honestly thought it was Tai this entire time!"
    else:
        camilo "What? I'd never have guessed!"
        iona "I honestly thought it was Tai this entire time!"

    "Tai scoffs."
    tai "OK, I get why you'd think that."
    tai "And now I'm sad that it wasn't me."
    genevieve "I got the idea during the camp out and today seemed like the kind of day that needed the mood boost."
    "After the laughter and shock dies down, [s3e7p3_dump_m] and [s3e7p3_dump_f] look at each other and then turn back to the rest of you."
    "[s3e7p3_dump_f] sighs."

    if s3e7p3_dump_f == "Miki":
        miki "I'll be honest, when I walked through those doors at the start..."
        miki "I didn't think I'd be walking out of them as the first dumped couple."
    else:
        iona "I'll be honest, when I walked through those doors at the start..."
        iona "I didn't think I'd be walking out of them as the first dumped couple."

    if s3e7p3_dump_m == "Bill":
        if ("Bill" in s3_mc.past_partners and s3_like_bill) or s3_mc.like_mc["Bill"] > 8:
            miki "I may not have found love, but I did find some amazing friends and had some incredible experiences."
            miki "Though, I am glad I won't have to suck another toe for a while..."
            bill "And yeah, I can't say I was exactly expecting to leave like this either."
            bill "But I'm just glad that I got to meet such great people. And get close to someone really special."
            "He looks at you with a wide smile."
            bill "And maybe I'll see that person again once she's out here..."
        else:
            miki "But I'm okay with this."
            "She turns to [s3e7p3_dump_m]."
            miki "And now I get to know this silly lug better."
            miki "And all his interesting opinions."
            bill "Hey... why does that sound sarcastic?"
            miki "Oh, does it? Oh woah, how unintentional."
            "She winks at him and nudges him in the ribs."
            bill "Cheeky."
            bill "And yeah, I can't say I was exactly expecting to leave like this either."
            bill "But I'm just glad that I got to meet such great people. And get close to someone really special."
            "He looks down at [s3e7p3_dump_f] with a wide smile."
            bill "And I can't wait to see where we go from this point on..."
            miki "I guess you'll have to get used to sleeping on a boat..."
            bill "Mate, we weren't meant to sleep on a boat. That's why we left the sea!"
            miki "Save it for the taxi ride."
        bill "Well, this is it, then. Goodbye all!"
    else:
        if ("Camilo" in s3_mc.past_partners and s3_like_camilo) or s3_mc.like_mc["Camilo"] > 8:
            iona "I may not have found love, but I did find some amazing friends and had some incredible experiences."
            iona "Though, I am glad I won't have to suck another toe for a while..."
            camilo "And yeah, I can't say I was exactly expecting to leave like this either."
            camilo "But I'm just glad that I got to meet such great people. And get close to someone really special."
            "He looks at you with a wide smile."
            camilo "And maybe I'll see that person again once she's out here..."
        else:
            iona "But I'm okay with this."
            "She turns to [s3e7p3_dump_m]."
            iona "I now get to know this Adonis better. We've already got plans to do a road trip around Scotland."
            camilo "I've never been before. It's gonna be well good!"
            camilo "I'll get to see Nessie!"
            iona "No you won't, babe, I told you, no one sees Nessie. That's the point."
            camilo "And yeah, I can't say I was exactly expecting to leave like this either."
            camilo "But I'm just glad that I got to meet such great people. And get close to someone really special."
            "He looks down at [s3e7p3_dump_f] with a wide smile."
            camilo "And I can't wait to see where we go from this point on..."
            iona "I told you! Scotland. Land of the brave. And haggis. Haggis is great."
        camilo "Well, this is it, then. Goodbye all!"

    "Some more of the Islanders begin to tear up as the couple make their way to the end of the driveway and out of sight."

    # CHOICE
    menu:
        thought "That's it then..."
        "Wave sadly":
            "You give the couple one last, slow wave."
            s3_mc "Damn..."
        "Do a secret fist pump":
            "While the others are distracted, you do a little triumphantly fist pump."
            thought "Still here! Go me!"
        "Take a moment":
            "Everything that's happened today seems to hit you at once."
            "You feel both sadness and relief all at once."

    "There's silence for a while, then [s3_li]'s phone pings."
    elladine "Oh, what now?"

    if s3e7p3_dump_f == "Miki":
        iona "Please don't be another surprise dumping..."
    else:
        miki "Please don't be another surprise dumping..."

    "[s3_li] glances at you, then looks down at [his_her] phone."
    text "Islanders, tomorrow night there will be a recoupling and the GIRLS will choose who they want to couple up with. #Ididnotseethatcoming #getyourgrafton #girlpower"
    harry "Oh..."
    "The girls look around at one another."
    "There's a moment of silence..."
    s3_mc "This has been a tough dumping..."

    if s3e7p3_dump_f == "Miki":
        $ s3e7p3_stayed = "Camilo and Iona"
    else:
        $ s3e7p3_stayed = "Bill and Miki"

    # CHOICE
    menu:
        thought "How shall I bring up the mood?"
        "Cheer for [s3e7p3_stayed]":
            s3_mc "Three cheers for [s3e7p3_stayed]!"
            if s3e7p3_stayed == "Bill and Miki":
                bill "That's well sweet."
            else:
                camilo "That's well sweet."
            "Though they're quiet at first, the other Islanders soon cheer enthusiastically."
        "A group hug":
            s3_mc "Group hug, everyone!"
            "Everyone comes in for a huge hug."
        "Start a dance":
            s3_mc "Come on, everyone!"
            s3_mc "Let's celebrate what we have tonight."
            "You start a conga, and though they're quiet at first, the other Islanders soon join in enthusiastically."

    "You feel your heart lift, knowing that your friends are around you."
    thought "I'm so glad I escaped that dumping!"
    "And so we say goodbye to [s3e7p3_dump_m] and [s3e7p3_dump_f]."

    if s3e7p3_dump_m == "Bill":
        "What will we possibly do without Bill's thoughts on everything?"
        "Other than have some peace and quiet..."
    else:
        "I don't know how I'll cope without seeing Camilo's cheeks every morning..."
        "Get your head out of the gutter. I meant face cheeks."
        "Such perfect bone structure..."

    "But enough about old news!"

    scene sand with dissolve
    $ on_screen = []

    "...Coming up!"
    "The recoupling's all anyone can talk about..."
    s3_li "You know, the recoupling? Everyone's been talking about it all morning."
    "And AJ reveals a magic gift."
    aj "They call me 'Magic Hands'."
    harry "Oh AJ, don't stop!"
    "Don't miss it..."

    jump s3e8p1
    return

label s3e7p3_help_pack:
    s3_mc "Let me help you guys pack."

    if s3e7p3_dump_m == "Bill":
        bill "That's really kind of you, [s3_name]."
    else:
        camilo "That's really kind of you, [s3_name]."
    
    scene s3-dressing-room with dissolve
    $ on_screen = []

    "The three of you head to the dressing room."
    "You and [s3e7p3_dump_m] are helping [s3e7p3_dump_f] pack up her makeup and hair brushes."

    # CHOICE
    menu:
        s3_mc "So..."
        "Why do you have so many hair brushes?" if s3e7p3_dump_f == 'Iona':
            iona "Hey, I may have shorter hair, but I take care of it, babe."
            iona "Especially with how much dye goes in it. It gets super brittle. Gotta treat it nice."
        "I can't believe that just happened":
            if s3e7p3_dump_m == "Bill":
                bill "Yeah, but, like, it did..."
                miki "I guess you lot saw us as too much competition."
            else:
                camilo "Yeah, but, like, it did..."
                iona "I guess you lot saw us as too much competition."
        "This really is the end, eh?":
            if s3e7p3_dump_m == "Bill":
                bill "Don't say that!"
                miki "Yeah, it might be the end of us in here, but we should still meet up on the outside."
            else:
                camilo "Don't say that!"
                iona "Yeah, it might be the end of us in here, but we should still meet up on the outside."

    "She picks up one of her shirts."

    if s3e2p3_food_fight:
        if s3e7p3_dump_m == "Bill":
            miki "Oh, this still has a little bit of the 'sauce surprise' on it from that food fight..."
            bill "Snap! One of mine had stains all over it, too."
            bill "Which I blame [s3_name] for entirely..."
            s3_mc "But it was so much fun!"
        else:
            iona "Oh, this still has a little bit of the 'sauce surprise' on it from that food fight..."
            camilo "Snap! One of mine had stains all over it, too."
            if s3e2p3_clean_off_with_cam == False:
                camilo "Which I blame [s3_name] for entirely..."
                s3_mc "But it was so much fun!"
    else:
        if s3e7p3_dump_m == "Bill":
            miki "Oh, this is still damp from jumping in the pool!"
            bill "Snap! One of mine got all bunched up, too."
        else:
            iona "Oh, this is still damp from jumping in the pool!"
            camilo "Snap! One of mine got all bunched up, too."

    if s3e2p3_clean_off_with_cam:
        camilo "That was a great night..."

    "One of [s3e7p3_dump_f]'s lipsticks slips from her fingers and rolls to [s3e7p3_dump_m]'s foot."

    if s3e7p3_dump_f == "Miki":
        miki "Agh!"
    else:
        iona "Agh!"

    "[s3e7p3_dump_m] chuckles and picks it up."

    if s3e7p3_dump_m == "Bill":
        if ("Bill" in s3_mc.past_partners and s3_like_bill) or s3_mc.like_mc["Bill"] > 8:
            bill "Careful, butter fingers."
            miki "Thanks! This is my favourite lippy."
        else:
            bill "Careful, babe. Don't want to lose your favourite lipstick."
            miki "Aw, you remembered."
    else:
        if ("Camilo" in s3_mc.past_partners and s3_like_camilo) or s3_mc.like_mc["Camilo"] > 8:
            camilo "Careful, butter fingers."
            iona "Thanks! This is my favourite lippy."
        else:
            camilo "Careful, babe. Don't want to lose your favourite lipstick."
            iona "Aw, you remembered."

    "She looks down at her lipstick and then at you."
    if s3e7p3_dump_f == "Miki":
        $ leaving("bill")
        miki "Actually, babes, I want you to have this."
    else:
        $ leaving("camilo")
        iona "Actually, babes, I want you to have this."
    "She goes to hand you the lipstick."

    # CHOICE
    menu:
        s3_mc "Oh..."
        "But I already have this lipstick":
            # NEED TO FILL
            "EMPTY"
        "You shouldn't share make-up, though":
            # NEED TO FILL
            "EMPTY"
        "This is so sweet, babe":
            if s3e7p3_dump_f == "Miki":
                $ s3_mc.like("Miki")
                miki "I'm glad you like it."
                miki "It's a good colour for you."
            else:
                $ s3_mc.like("Iona")
                iona "I'm glad you like it."
                iona "It's a good colour for you."

    if s3e7p3_dump_f == "Miki":
        miki "I want you to have it as a little keepsake from me."
        miki "I know we weren't as close in here as you and [s3_mc.bff], but out of everyone, you seem the most solid."
        miki "I think you deserve to get everything you want out of this experience."
    else:
        iona "I want you to have it as a little keepsake from me."
        iona "I know we weren't as close in here as you and [s3_mc.bff], but out of everyone, you seem the most solid."
        iona "I think you deserve to get everything you want out of this experience."

    if s3e7p3_dump_f == "Miki":
        if s3_mc.past_partners[1] == "Bill" and s3e6p1_break_up == False:
            "[s3e7p3_dump_f] glances over at [s3e7p3_dump_m], who's currently dabbing some of her eyeshadow onto his cheeks."
            "She leans in closer to you."
            miki "I know you and [s3e7p3_dump_m] still have feelings for each other."
            miki "I'm sorry he won't be here for you to finish the show with..."
        elif s3_mc.past_partners[1] == "Bill" and s3e6p1_break_up:
            miki "I know it wasn't your choice to split up with [s3e7p3_dump_m], but I'm glad you've taken it well."
            miki "Means I get him to myself."
        elif ("Bill" in s3_mc.past_partners and s3_like_bill) or s3_mc.like_mc["Bill"] > 8:
            "She leans in closer to you."
            miki "I know you and [s3e7p3_dump_m] are kinda into each other."
            miki "I want you to know that I'm going to be off the scene once we're out of here, if you wanna message him once the summer's over or something."
            miki "Of course, that doesn't really help while you're still in here."
        else:
            miki "I can't wait to get out there with him and take on the world together."
            miki "But what about? You're with [s3_li] at the moment."
    else:
        if s3_mc.past_partners[1] == "Camilo" and s3e6p1_break_up == False:
            "[s3e7p3_dump_f] glances over at [s3e7p3_dump_m], who's currently dabbing some of her eyeshadow onto his cheeks."
            "She leans in closer to you."
            iona "I know you and [s3e7p3_dump_m] still have feelings for each other."
            iona "I'm sorry he won't be here for you to finish the show with..."
        elif s3_mc.past_partners[1] == "Camilo" and s3e6p1_break_up:
            iona "I know it wasn't your choice to split up with [s3e7p3_dump_m], but I'm glad you've taken it well."
            iona "Means I get him to myself."
        elif ("Camilo" in s3_mc.past_partners and s3_like_camilo) or s3_mc.like_mc["Camilo"] > 8:
            "She leans in closer to you."
            iona "I know you and [s3e7p3_dump_m] are kinda into each other."
            iona "I want you to know that I'm going to be off the scene once we're out of here, if you wanna message him once the summer's over or something."
            iona "Of course, that doesn't really help while you're still in here."
        else:
            iona "I can't wait to get out there with him and take on the world together."
            iona "But what about? You're with [s3_li] at the moment."

    if s3e7p3_dump_f == "Miki":
        if s3e6p3_loyal == False or (s3_like_ciaran and s3_li == "Ciaran") or (s3_like_tai and s3_li == "Tai") or (s3_like_yasmin and s3_li == "Yasmin"):
            miki "You and [s3_li] seem really cute together."
        else:
            miki "It's kinda obvious that you and [s3_li] are just friends."
            miki "At least that's how it seems."
            miki "So, like..."
        miki "Do you want to go all the way to the finale with [him_her]?"
    else:
        if s3e6p3_loyal == False or (s3_like_ciaran and s3_li == "Ciaran") or (s3_like_tai and s3_li == "Tai") or (s3_like_yasmin and s3_li == "Yasmin"):
            iona "You and [s3_li] seem really cute together."
        else:
            iona "It's kinda obvious that you and [s3_li] are just friends."
            iona "At least that's how it seems."
            iona "So, like..."
        iona "Do you want to go all the way to the finale with [him_her]?"

    # CHOICE
    menu:
        thought "Do I want to end the show with [s3_li]?"
        "I actually do. [he_she!c]'s so sweet":
            if s3e7p3_dump_f == "Miki":
                miki "That's great to hear."
                if s3e6p3_loyal == False or (s3_like_ciaran and s3_li == "Ciaran") or (s3_like_tai and s3_li == "Tai") or (s3_like_yasmin and s3_li == "Yasmin"):
                    miki "It looks like you're on the right path to doing it. Just make sure you keep being so cute together."
                else:
                    miki "But it's not obvious right now. You need to make yourself available for [him_her]!"
            else:
                iona "That's great to hear."
                if s3e6p3_loyal == False or (s3_like_ciaran and s3_li == "Ciaran") or (s3_like_tai and s3_li == "Tai") or (s3_like_yasmin and s3_li == "Yasmin"):
                    iona "It looks like you're on the right path to doing it. Just make sure you keep being so cute together."
                else:
                    iona "But it's not obvious right now. You need to make yourself available for [him_her]!"
            if s3_li == "Ciaran":
                $ s3_like_ciaran = True
            elif s3_li == "Tai":
                $ s3_like_tai = True
            elif s3_li == "Yasmin":
                $ s3_like_yasmin = True
        "I don't think so...":
            if s3e6p3_loyal or (s3_like_ciaran == False and s3_li == "Ciaran") or (s3_like_tai == False and s3_li == "Tai") or (s3_like_yasmin == False and s3_li == "Yasmin"):
                if s3e7p3_dump_f == "Miki":
                    miki "Yeah, no shock there."
                else:
                    iona "Yeah, no shock there."
            if s3e7p3_dump_f == "Miki":
                miki "Well, you better find yourself someone else soon. You won't be in here forever!"
            else:
                iona "Well, you better find yourself someone else soon. You won't be in here forever!"
        "I just want someone else to walk in":
            if s3e7p3_dump_f == "Miki":
                miki "Hmm, I don't think that's very likely."
                miki "If I were you, I'd just find someone you like in here, or could see yourself with, and just go for it!"
                miki "You haven't got much time left..."
            else:
                iona "Hmm, I don't think that's very likely."
                iona "If I were you, I'd just find someone you like in here, or could see yourself with, and just go for it!"
                iona "You haven't got much time left..."

    if s3e7p3_dump_f == "Miki":
        miki "Look, I want you to take the lipstick."
        miki "Use it to leave your mark on the right person..."
        "[s3e7p3_dump_m] walks over to the two of you."
        bill "All your make-up's packed."
        miki "Oh! Sorry, babe, I got caught up talking to [s3_name]."
    else:
        iona "Look, I want you to take the lipstick."
        iona "Use it to leave your mark on the right person..."
        iona "Oh, and make sure to keep the Shiny Demon away from this one."
        "[s3e7p3_dump_m] walks over to the two of you."
        camilo "All your make-up's packed."
        iona "Oh! Sorry, babe, I got caught up talking to [s3_name]."

    if s3e7p3_dump_m == "Bill":
        if ("Bill" in s3_mc.past_partners and s3_like_bill) or s3_mc.like_mc["Bill"] > 8:
            "She looks at the two of you."
            miki "I'll leave you two alone for a minute."
            miki "I'll go pack you stuff, seeing as you did mine."
        else:
            "She smiles at him."
            miki "Let me return the favour. I'll go and pack up your stuff!"
            bill "Aww, thanks, babe."
            "She makes her way to the bedroom."
    else:
        if ("Camilo" in s3_mc.past_partners and s3_like_camilo) or s3_mc.like_mc["Camilo"] > 8:
            "She looks at the two of you."
            iona "I'll leave you two alone for a minute."
            iona "I'll go pack you stuff, seeing as you did mine."
        else:
            "She smiles at him."
            iona "Let me return the favour. I'll go and pack up your stuff!"
            camilo "Aww, thanks, babe."
            "She makes her way to the bedroom."

    if s3e7p3_dump_f == "Miki":
        $ leaving("miki")
    else:
        $ leaving("iona")

    "[s3e7p3_dump_m] turns to you."

    if s3e7p3_dump_m == "Bill":
        bill "Can't say I expected to be leaving so soon..."
        if (s3_mc.past_partners[1] == "Bill" and s3e6p1_break_up == False) or s3_mc.like_mc["Bill"] > 8:
            if "Bill" in s3_mc.past_partners:
                bill "Or that we wouldn't get another chance to be coupled up..."
            else:
                bill "Or that we wouldn't get a chance to couple up."
    else:
        camilo "Can't say I expected to be leaving so soon..."
        if (s3_mc.past_partners[1] == "Camilo" and s3e6p1_break_up == False) or s3_mc.like_mc["Camilo"] > 8:
            if "Camilo" in s3_mc.past_partners:
                camilo "Or that we wouldn't get another chance to be coupled up..."
            else:
                camilo "Or that we wouldn't get a chance to couple up."


    if (s3_mc.past_partners[1] == s3e7p3_dump_m and s3e6p1_break_up == False) or s3_mc.like_mc[s3e7p3_dump_m] > 8:
        # CHOICE
        menu:
            thought "[s3e7p3_dump_m] said that he's going before we could couple up..."
            "It's a shame we never coupled up" if s3e7p3_dump_m not in s3_mc.past_partners:
                # NEED TO FILL
                "EMPTY"
            "What are you going to do now?":
                # NEED TO FILL
                "EMPTY"
            "At least we had our chance at being a couple" if s3e7p3_dump_m in s3_mc.past_partners:
                if s3e7p3_dump_m == "Bill":
                    bill "That's true..."
                    bill "Those few days were some of the happiest memories I have from being here..."
                else:
                    camilo "That's true..."
                    camilo "Those few days were some of the happiest memories I have from being here..."
            "There's definitely time for one final kiss":
                "He looks at you and bites his lips in anticipation."
                s3_mc "Let me give you something to remember me by."
                "You pull him into an embrace and your lips lock for the last time in the Villa."
                "A bittersweet feeling washes over you as your tongues make contact and move across each other."
                "You wrap your hands around his shoulders and hold him tight, your eyes shut, drawing the moment out."
                "[s3e7p3_dump_m] sighs as he pulls away from you."
                if s3e7p3_dump_m == "Bill":
                    bill "I thought this would make it easier."
                    bill "But it's obviously done the exact opposite..."
                else:
                    camilo "I thought this would make it easier."
                    camilo "But it's obviously done the exact opposite..."
            "We can always meet up on the outside":
                "He smiles."
                if s3e7p3_dump_m == "Bill":
                    bill "I hope we do."
                    bill "Even if nothing romantic happens, like, I still want to be friends with you."
                else:
                    camilo "I hope we do."
                    camilo "Even if nothing romantic happens, like, I still want to be friends with you."
    else:
        if s3e7p3_dump_m == "Bill":
            bill "But at least it's with [s3e7p3_dump_f]."
        else:
            camilo "But at least it's with [s3e7p3_dump_f]."

        # CHOICE
        menu:
            thought "[s3e7p3_dump_m]'s happy that he's leaving with [s3e7p3_dump_f]..."
            "Do you think you'll last?":
                if s3e7p3_dump_m == "Bill":
                    bill "Well that's a loaded question and a half..."
                    bill "I'd like to think so!"
                    bill "I guess we're definitely attracted to each other physically, that much is clear."
                    bill "Let's see if we can go beyond that."
                else:
                    camilo "Well that's a loaded question and a half..."
                    camilo "I'd like to think so!"
                    camilo "I guess we're definitely attracted to each other physically, that much is clear."
                    camilo "Let's see if we can go beyond that."
            "You two make a cute couple":
                if s3e7p3_dump_m == "Bill":
                    bill "I was going for edgy, but I'll take cute."
                else:
                    camilo "I was going for raunchy, but I'll take cute."
            "What are you going to do now?":
                if s3e7p3_dump_m == "Bill":
                    bill "I guess we're going to see how we do outside of this place, one day at a time."
                    bill "So I guess part of that will be seeing her boat..."
                    "He shakes his head."
                    bill "What have I got myself into?"
                else:
                    camilo "I guess we're going to see how we do outside of this place, one day at a time."
                    camilo "I know she wants me to see Scotland with her."
                    camilo "It's going to take a lot of effort not to wind her up by doing a really bad Scottish accent constantly while we're there."
    
    "Just then [s3e7p3_dump_f] walks back in."
    if s3e7p3_dump_m == "Bill":
        miki "That's it, We're all packed."
        bill "Guess that means it's time to go and say goodbye..."
        "They both turn to you."
        bill "See you around, [s3_name]. It's been a lot of fun."
        miki "Win this thing for us, yeah?"
        miki "Oh, and find love, I suppose..."
    else:
        iona "That's it, We're all packed."
        camilo "Guess that means it's time to go and say goodbye..."
        "They both turn to you."
        camilo "See you around, [s3_name]. It's been a lot of fun."
        iona "Win this thing for us, yeah?"
        iona "Oh, and find love, I suppose..."
    "The three of you make your way outside."

    return

#########################################################################
## Episode 8, Part 1
#########################################################################
label s3e8p1:
    scene sand with dissolve
    $ on_screen = []

    show screen day_title(8, 1) with Pause(4)
    hide screen day_title with dissolve

    "Previously on Love Island..."
    "One couple got dumped from the Island!"

    if s3e7p3_dump_f == "Miki":
        miki "I wasn't ready to leave..."
    else:
        iona "I wasn't ready to leave..."

    "And the Islanders learned of tonight's recoupling in a surprise text!"
    "Talk about shaking things up."
    "It's like James Bond's martini in here!"
    "It's the eighth day in the villa, so let's recap who our couples are!"
    "There's [s3e7p3_dump_f] and [s3e7p3_dump_m], who narrowly escaped being dumped last night thanks to [s3_name]."
    "Elladine and Nicky are still going strong."

    if s3_li == "Yasmin":
        "[s3_name] got picked by Yasmin, which certainly caused a storm."
        "Ciaran chose Genevieve, while Tai chose AJ."
        "And the most unexpected coupling of the night was Harry and Seb!"
        "Like many healthy relationships, they were each other's last hope."
        "I really hope they make it..."
    else:
        "Genevieve and Harry are coupled up..."
        "As are Yasmin and Seb."
        if s3_li == "Tai":
            "Finally, AJ and Ciaran together..."
        else:
            "Finally, AJ and Tai together..."
        "And [s3_li] snagged [s3_name]!"
        "[s3_name] is a hot commodity right now..."
        "If this was Essex in the winter, she'd be the spray tan!"

    "This morning, [s3_li] gets serious..."
    s3_li "I wanted to have a chat with you in private..."
    $ leaving("s3_li")
    "And Harry gets loud..."
    harry "Oh AJ, don't stop!"
    $ leaving("harry")
    "It's gonna be a bumpy ride."

    scene s3-bedroom-day with dissolve
    $ on_screen = []

    "The bedroom is empty and peaceful."
    "And here we have the wild spotted [s3_name], who routinely sleeps while everyone else is still awake..."
    "Sorry. Too many nature documentaries."
    "Wake up, [s3_name]! This is no time to be asleep. Get up and get grafting!"
    "You feel someone nudge your leg."
    s3_mc "Five more minutes, mum!"
    s3_li "Huh? [s3_name], wake up!"
    "You open your eyes to see [s3_li] standing at the foot of your bed, holding a mug."
    "The others are getting ready in the next room."
    s3_li "Rise and shine, sleepyhead. I got you a tea."
    "You sit up. When you grab the mug and take a sip, it's absolutely perfect."

    # CHOICE
    menu:
        thought "This tea's really good..."
        "You're a star":
            $ s3_mc.like(s3_li)
            s3_li "Aw, glad you like it!"
            s3_li "Tea in the morning always helps me start the day right."
        "I miss [s3_mc.past_partners[1]]'s tea...":
            $ s3_mc.dislike(s3_li)
            $ s3_mc.like(s3_mc.past_partners[1])
            "[s3_li]'s face falls."
            s3_li "Oh..."
            s3_li "Well, I can always perfect my next brew."
        "I'll get you one next time":
            $ s3_mc.like(s3_li)
            s3_li "Aw, that would be amazing."
            s3_li "I love a good cuppa in the morning."

    s3_li "You looked so peaceful there, snoozing away."
    s3_li "What were you dreaming about?"

    # CHOICE
    menu:
        thought "I was dreaming about..."
        "You":
            $ s3_mc.like(s3_li)
            s3_li "Yeah? What were we doing?"
            s3_li "Anything fun?"
            s3_mc "We were in the Villa eating breakfast. Then Godzilla ate you, and I made it my mission to avenge you. Then I woke up."
            s3_li "Woah. That's intense!"
            s3_li "They say dreams have meanings..."
            s3_li "I wonder what Godzilla means in a dream?"
        "[s3_mc.past_partners[1]]":
            $ s3_mc.dislike(s3_li)
            $ s3_mc.like(s3_mc.past_partners[1])
            s3_li "Oh..."
            "[he_she!c] hesitates for a second."
            s3_li "What were you up to?"
            s3_mc "We were in the pool, and [s3_mc.past_partners[1]] got eaten by a dolphin."
            s3_mc "Then I rode the dolphin around the pool!"
            s3_li "Woah. That's intense!"
            s3_li "They say dreams have meanings..."
            s3_li "I wonder what dolphins mean in a dream?"
        "Superman":
            s3_mc "He was riding a cloud next to me, playing the violin."
            s3_mc "He was well good at it. At least Grade 5."
            s3_li "Woah. That's intense!"
            s3_li "They say dreams have meanings..."
            s3_li "I wonder what Superman means in a dream?"

    # CHOICE
    menu:
        thought "What do I think my dream meant?"
        "I need to eat less cheese before bed":
            # NEED TO FILL
            "EMPTY"
        "My mind's busy":
            s3_mc "It's not really about the dream. Maybe my brain's just going over the day."
            s3_li "That makes sense."
        "I need to eat more cheese before bed":
            s3_mc "I obviously need more cheese."
            s3_li "More?!"
            s3_mc "So I can interpret the dreams better."
            "[s3_li] laughs."

    "[he_she!c] sits down on the bed, squishing your toes under [his_her] butt."
    s3_li "So, I wanted to have this chat with you in private before everything kicks off today."
    s3_mc "Kicks off?"
    s3_li "The recoupling! Everyone's been talking about it all morning."

    if s3_li != "Ciaran":
        s3_li "I'm almost looking forward to it."
        s3_li "In a pulling off a plaster kind of way."
    else:
        s3_li "I'm bricking it."
        
    s3_li "How about you?"

    # CHOICE
    menu:
        thought "Everyone's worried about the recoupling..."
        "It's scary":
            s3_mc "We're so close to the end now."
            s3_mc "It's a lot of responsibility!"
            if s3_li == "Yasmin":
                s3_li "I suppose whatever will happen, will happen."
                s3_li "But there's still something I want to say to you, [s3_name]."
            else:
                s3_li "Yeah, that's actually what I wanted to talk to you about..."
        "I know I'll be fine":
            if s3_li == "Yasmin":
                s3_mc "It's girls' choice, so we've got nothing to be scared of."
                s3_mc "We're not going home whatever happens."
                s3_li "I suppose whatever will happen, will happen."
                s3_li "But there's still something I want to say to you, [s3_name]."
            else:
                s3_mc "It's girls' choice, so I've got nothing to be worried about."
                s3_mc "At least I know I'm not going home."
                s3_li "I wish I had that luxury."
                s3_li "That's what I wanted to talk to you about."
        "I'm excited!":
            s3_mc "That means the drama's hotting up."
            s3_mc "I can't wait."
            if s3_li == "Yasmin":
                s3_li "I suppose whatever will happen, will happen."
                s3_li "But there's still something I want to say to you, [s3_name]."
            else:
                s3_li "I'm glad you're feeling chill about it."
                s3_li "That makes me feel a lot better."
                s3_li "But I did want to talk to you about it..."

    s3_li "We've only got a few days left now. I picked you because I like you."

    if s3e6p3_loyal:
        s3_li "And I think we make a great couple."
    else:
        s3_li "And I know you fancy me too."

    s3_li "But don't feel pressured to re-couple with me because of that."
    s3_li "I nicked you from [s3_mc.past_partners[1]]. You didn't choose to be with me."

    if s3_li == "Yasmin":
        s3_li "You have to follow your heart. What's the point of love if you don't?"
    elif s3_li == "Tai":
        s3_li "I think you're a great girl, but I don't want to force something you're not comfortable with."
        s3_li "That's not the Tai way."
    elif s3_li == "Ciaran":
        s3_li "And there's plenty more hares in the field!"
        s3_mc "You mean fish in the sea?"
        s3_li "Maybe it's just a Waterford expression..."

    if s3e6p3_loyal:
        s3_mc "Thanks for considering my feelings."
        s3_mc "It's nice to know you think about this stuff."
        s3_li "No worries."
    else:
        s3_mc "What if I want to pick you?"
        "[s3_li] looks you full in the face, his eyes meeting yours."
        s3_li "I'd be over the moon."

    s3_li "Having said that... it would be nice to know what you're thinking."
    s3_li "Just so I'm not surprised tonight."

    # CHOICE
    menu:
        thought "[s3_li] is wondering who I'm going to pick in the recoupling tonight..."
        "Of course I'll pick you!":
            $ s3_mc.like(s3_li)
            if s3_li == "Yasmin":
                $ s3e8p1_hope_recoupling_yasmin = True
            s3_mc "I like having you around."
            s3_li "Really?"
            s3_li "I hoped you'd say that!"
        "I'll go with you":
            $ s3_mc.like(s3_li)
            if s3_li == "Yasmin":
                $ s3e8p1_hope_recoupling_yasmin = True
            s3_mc "I like having you around."
            s3_li "Really?"
            s3_li "I hoped you'd say that!"
        "I'm not picking you":
            $ s3_mc.dislike(s3_li)
            s3_li "Oh... OK."
            s3_li "Thanks for letting me know."

    s3_li "Sorry to ambush you with all this. You're not even dressed!"
    s3_li "I'll give you time to enjoy your cuppa and get ready."
    s3_mc "Thanks."
    thought "I should get ready for the day."
    thought "To the dressing room!"

    scene s3-dressing-room with dissolve
    $ on_screen = []

    "You walk into the dressing room and find [s3e7p3_stay_f] plucking her eyebrows."
    s3_mc "That looks intense."
    "[s3e7p3_stay_f] jumps."

    if s3e7p3_stay_f == "Miki":
        miki "[s3_name]! You made me pull out, like, five!"
        miki "It's gonna take ages to pencil over that..."
    else:
        iona "[s3_name]! You made me pull out, like, five!"
        iona "It's gonna take ages to pencil over that..."

    s3_mc "Sorry! Thought you saw me."
    "[s3e7p3_stay_f] puts down the tweezers, and walks towards you, arms open."

    # CHOICE
    menu:
        thought "[s3e7p3_stay_f] is going to hug me..."
        "Let her":
            "You wrap your arms around each other in a warm embrace."
            "She pats you on the back, a little awkwardly."
            "After a few moments, she pulls away."
        "High-five her":
            "You intercept her hug, high five-ing her right hand."
            if s3e7p3_stay_f == "Miki":
                miki "That works too."
            else:
                iona "That works too."
        "Shake her hand":
            "You intercept her hug, catching her right hand and shaking it."
            "She looks at you confused."
            if s3e7p3_stay_f == "Miki":
                miki "OK..."
            else:
                iona "OK..."

    if s3e7p3_stay_f == "Miki":
        miki "I just wanted to say thank you. For saving me and [s3e7p3_stay_m] last night."
    else:
        iona "I just wanted to say thank you. For saving me and [s3e7p3_stay_m] last night."
    
    s3_mc "Oh..."

    # CHOICE
    menu:
        thought "[s3e7p3_stay_f] is talking about the dumping last night..."
        "You're welcome, hun.":
            $ s3_mc.like(s3e7p3_stay_f)
            s3_mc "Of course I saved you, babes!"
            s3_mc "This place wouldn't be the same without you."
            if s3e7p3_stay_f == "Miki":
                iona "[s3_name], that's so nice of you."
        "I flipped a coin.":
            $ s3_mc.dislike(s3e7p3_stay_f)
            s3_mc "I couldn't make that choice."
            if s3e7p3_stay_f == "Miki":
                miki "I get it. We're all friends."
                miki "It must have been so hard to make that decision."
                miki "I don't know what I would have done if I had to choose between you and [s3e7p3_dump_f]."
                miki "Girl Code doesn't cover this kind of situation!"
            else:
                iona "I get it. We're all friends."
                iona "It must have been so hard to make that decision."
                iona "I don't know what I would have done if I had to choose between you and [s3e7p3_dump_f]."
                iona "Girl Code doesn't cover this kind of situation!"
        "I did it for [s3e7p3_stay_m].":
            $ s3_mc.dislike(s3e7p3_stay_f)
            s3_mc "I think I still have a chance with him."
            if s3e7p3_stay_f == "Miki":
                miki "Well... thanks anyway."
            else:
                iona "Well... thanks anyway."

    "[s3e7p3_stay_f] turns back to the mirror and begins straightening her hair."
    "You grab your make-up bag and sit down beside her."

    if s3e7p3_stay_f == "Iona":
        iona "You know, I never saw myself fancying someone like Camilo."
        iona "But at first, I wasn't sure if our personalities were a good match."
        iona "But I'm totally loving being coupled up with him."
        iona "At the rate we're going, I'd definitely want to give it a go on the outside."
        iona "My family always wanted me to get with a lad who could cook. All I usually eat is spaghetti on toast."
        iona "With Camilo, I might even end up getting my five-a-day..."
        "She shivers."
        iona "Feels weird to even think about that."
        iona "I'm definitely picking him in the recoupling."
    else:
        miki "You know I always had the hots for Bill..."
        miki "But at first, I wasn't sure if our personalities were a good match."
        miki "The other night he tried to argue with me about cereal bars..."
        miki "But I'm starting to like that."
        s3_mc "Arguing about cereal bars?"
        miki "“It's not a meal. Have cereal or have nothing.”"
        "Miki sighs dreamily."
        miki "So passionate..."
        miki "I'm definitely picking him in the recoupling."


    if s3e7p3_stay_f == "Miki":
        if ("Bill" in s3_mc.past_partners and s3_like_bill) or s3_mc.like_mc["Bill"] > 8:
            iona "Unless you get there first, I suppose..."
            iona "I guess it's up to the powers that be."
        miki "It's strange thinking about tonight."
        miki "Do you know who you're picking? If you don't mind me asking."

    else:
        if ("Camilo" in s3_mc.past_partners and s3_like_camilo) or s3_mc.like_mc["Camilo"] > 8:
            iona "Unless you get there first, I suppose..."
            iona "I guess it's up to the powers that be."
        iona "I'm well nervous about tonight."
        s3_mc "That's not like you."
        iona "suppose it's just the vibe in here."
        iona "It's quiet, you know?"
        iona "Like a fusebox right before it takes your eyebrows off."
        iona "Do you know who you're picking? If you don't mind me asking."

    # CHOICE
    menu:
        thought "Have I made up my mind about the recoupling?"
        "None of your business":
            s3_mc "Why does everyone keep asking me about this?"
            if s3e7p3_stay_f == "Miki":
                miki "Sorry, I was just curious."
            else:
                iona "Sorry, I was just curious."
            s3_mc "I like to keep that air of mystery."
        "I don't know yet":
            if s3e7p3_stay_f == "Miki":
                miki "Ooh! Waiting till the last second, are we?"
                s3_mc "I guess I'm hoping I'll know in the moment."
                miki "Let your gut decide! I like it."
            else:
                iona "Ooh! Waiting till the last second, are we?"
                s3_mc "I guess I'm hoping I'll know in the moment."
                iona "Let your gut decide! I like it."
        "I've made up my mind":
            if s3e7p3_stay_f == "Miki":
                miki "Good for you!"
                miki "Don't worry, I won't ask. Gotta keep that element of surprise."
            else:
                iona "Good for you!"
                iona "Don't worry, I won't ask. Gotta keep that element of surprise."

    if s3e7p3_stay_f == "Miki":
        miki "I swear, [s3_name], you would be such a good protagonist."

    if s3e7p3_help_pack:
        if s3e7p3_stay_f == "Miki":
            miki "So, [s3_name]..."
            "[s3e7p3_stay_f] looks at you, feigning disinterest."
            miki "Couldn't help but notice you helped [s3e7p3_dump_m] and [s3e7p3_dump_f] pack last night."
            s3_mc "Yeah, I thought it would be nice to see them one last time."
            miki "How was [s3e7p3_dump_f]? Was she upset?"
        else:
            iona "So, [s3_name]..."
            "[s3e7p3_stay_f] looks at you, feigning disinterest."
            iona "Couldn't help but notice you helped [s3e7p3_dump_m] and [s3e7p3_dump_f] pack last night."
            s3_mc "Yeah, I thought it would be nice to see them one last time."
            iona "How was [s3e7p3_dump_f]? Was she upset?"

        # CHOICE
        menu:
            thought "How was [s3e7p3_dump_f] when I helped her pack?"
            "She was fine":
                if s3e7p3_stay_f == "Miki":
                    miki "That's good. She's so strong. I know she'll be OK."
                    miki "At least she won't have to fuss about with wires anymore if she doesn't want to."
                else:
                    iona "That's good. She's so strong. I know she'll be OK."
                    iona "I imagine she's got millions more YouTube subscribers waiting for her."
            "She was crying":
                if s3e7p3_stay_f == "Miki":
                    miki "Oh no! Poor girl."
                    miki "I wish I could hug her right now..."
                else:
                    iona "Oh no! Poor girl."
                    iona "I wish I could hug her right now..."
            "She was angry":
                if s3e7p3_stay_f == "Miki":
                    miki "No way!"
                else:
                    iona "No way!"

        if s3e7p3_stay_f == "Miki":
            iona "Did she say anything about me?"

        # CHOICE
        menu:
            thought "What did [s3e7p3_dump_f] say about [s3e7p3_stay_f]?"
            "Something mean":
                s3_mc "She said, and I'm quoting..."
                s3_mc "'She's not the kind of girl you miss.'"
                if s3e7p3_stay_f == "Miki":
                    miki "I can't believe she said that about me!"
                    miki "I thought we were friends..."
                    miki "Thanks for telling me, [s3_name]."
                    miki "I guess she was just in it for the cash..."
                    miki "I'm gonna head downstairs."
                    miki "Gosh, that's really ruined my mood."
                    miki "People miss me! People miss me all the time!"
                    miki "Do you miss me, [s3_name]?"
                    s3_mc "You're right in front of me."
                    miki "But like, when I'm in the other room?"
                else:
                    iona "I can't believe she said that about me!"
                    iona "I thought we were friends..."
                    iona "Thanks for telling me, [s3_name]."
                    iona "I guess she was just in it for the cash..."
                    iona "I'm gonna head downstairs."
                    iona "Gosh, that's really ruined my mood."
                    iona "People miss me! People miss me all the time!"
                    iona "Do you miss me, [s3_name]?"
                    s3_mc "You're right in front of me."
                    iona "But like, when I'm in the other room?"
                # SUB-CHOICE
                menu:
                    thought "Do I miss [s3e7p3_stay_f] when she's gone?"
                    "I miss you dearly":
                        # NEED TO FILL
                        "EMPTY"
                    "I like it when you're gone":
                        # NEED TO FILL
                        "EMPTY"
                    "No, cos you're coming back":
                        if s3e7p3_stay_f == "Miki":
                            iona "Aw, that's sweet."
                            iona "I think."
                if s3e7p3_stay_f == "Miki":
                    miki "Anyway, I'm gonna go. This whole thing has put me in a bad mood."
                else:
                    iona "Anyway, I'm gonna go. This whole thing has put me in a bad mood."
                "She slurps out of the room."
            "Something nice":
                $ s3e8p1_nice = True
                s3_mc "She asked me to look out for you. You're important to her."
                if s3e7p3_stay_f == "Miki":
                    miki "That's so sweet of her!"
                    miki "We totally have to grab a coffee after the summer, all three of us."
                    miki "I'm gonna head downstairs."
                    "She gives you a big smile."
                    miki "I'm so happy she thinks I'm a good friend."
                    miki "See you later, [s3_name]!"
                else:
                    iona "That's so sweet of her!"
                    iona "We totally have to grab a coffee after the summer, all three of us."
                    iona "I'm gonna head downstairs."
                    "She gives you a big smile."
                    iona "I'm so happy she thinks I'm a good friend."
                    iona "See you later, [s3_name]!"
                "She hugs you before running downstairs."
                
        if s3e7p3_stay_f == "Miki":
            $ leaving("miki")
        else:
            $ leaving("iona")
    else:
        if s3e7p3_stay_f == "Miki":
            miki "Anyway, enough serious talk!"
            miki "I think I'll go for a swim. You never know, I could be going home tonight!"
        else:
            iona "Anyway, enough serious talk!"
            iona "I think I'll go for a swim. You never know, I could be going home tonight!"

        s3_mc "But you just did your hair!"

        if s3e7p3_stay_f == "Miki":
            miki "OK, when I said swim, I more meant 'dip my big toe in'."
            miki "The sun is the thing I'll miss the most about this place."
            miki "It's absolutely absent in Cambridge."
            miki "See you in a bit!"
            "She switches off her straighteners and leaves."
        else:
            iona "So? I can do it again later. Live in the moment, [s3_name]!"
            "She runs out of the room. Moments later you hear a loud splash, and a groan from a presumably sopping Genevieve."

        if s3e7p3_stay_f == "Miki":
            $ leaving("miki")
        else:
            $ leaving("iona")

    thought "That was an intense conversation."
    thought "Better get dressed."

    # ADD once MC images are in game
    # Outfit change to swimwear
    "You throw on your favourite bathing suit."
    # thought "Lock up your sons and daughters, here I come!"

    thought "Still looking fresh."

    scene s3-kitchen-day with dissolve
    $ on_screen = []

    "You walk into the kitchen. [s3e7p3_stay_m] is making breakfast. AJ is massaging Harry's shoulders."
    "AJ spots you first."
    aj "I love that look. You always look hot in it."

    # ADD BACK once MC images in game
    # aj "You know you're hot in whatever, [s3_name], but you'd be even hotter in something. I dunno..."
    # aj "Hotter, if you know what I mean."

    "[s3e7p3_stay_m] grins when he sees you."
    s3_other_m "There she is! My hero!"
    "He wraps you in a big hug. He smells good."

    if s3e7p3_stay_m == "Bill":
        "Like fresh linen and good decisions."
    else:
        "Like Georgio Armani."

    s3_other_m "Sit down! I made breakfast as a thank you for saving me and [s3e7p3_stay_f] last night."
    s3_other_m "We both thought you would save [s3e7p3_stay_m] and [s3e7p3_stay_f]."
    "He exhales with relief."

    if s3e7p3_stay_m == "Bill":
        s3_other_m "I wanted a serious pint after all that!"
    else:
        s3_other_m "You know what, bruv, I thought I was headed back to Romford."

    # CHOICE
    menu:
        thought "[s3e7p3_stay_m] is talking about last night's dumping..."
        "I couldn't lose [s3e7p3_stay_f]":
            "[s3e7p3_stay_m] nods and smiles at you."
            s3_other_m "You're a good friend, [s3_name]. I know [s3e7p3_stay_f] thinks so, too."
        "You're both my friends":
            "[s3e7p3_stay_m] smiles at you."
            s3_other_m "Thanks for saying that, [s3_name]. [s3e7p3_stay_f] and I feel the same way about you."
        "I did it for you, [s3e7p3_stay_m]":
            $ s3_mc.like(s3e7p3_stay_m)
            "He grins at you."
            s3_other_m "I'd do the same for you."
            s3_other_m "Hopefully we can spend more time together now that I'll be staying..."

    s3_other_m "Anyway... your breakfast is ready!"
    s3_other_m "By the way, love the outfit!"

    # ADD BACK ONCE MC images in game
    # s3_other_m "By the way, love the new outfit!"

    if s3e7p3_stay_m == "Bill":
        s3_other_m "Though it's the person inside that really makes it."
    else:
        s3_other_m "You have such a good sense of style, [s3_name]."

    "You sit down at the breakfast bar, eyeing up what [s3e7p3_stay_m] has in his frying pan."

    if s3e7p3_stay_m == "Bill":
        if s3_mc.diet == "Vegan":
            "It's a perfectly cooked vegan omelette, smothered in mushrooms, dairy-free cheese, and..."
        elif s3_mc.diet == "Vegetarian":
            "It's a perfectly cooked vegetarian omelette, smothered in mushrooms, cheese, and..."
        else:
            "It's a perfectly cooked omelette, smothered in mushrooms, cheese, and..."

        "Peanut butter?"
        s3_mc "Bill, why is there peanut butter in my otherwise delicious breakfast?"
        "Bill puts down the spatula and looks at you, dead serious."
        s3_other_m "This is how you make an omelette!"
        s3_other_m "No complaints till you've tried it."

        # CHOICE
        menu:
            thought "Bill's made me an... interesting looking omelette."
            "Tell him you're not hungry":
                # NEED TO FILL
                "EMPTY"
            "Eat it with a smile":
                $ s3_mc.like("Bill")
                "You take a big bite, forcing a smile as you chew."
                "It's...not bad."
                "Actually, it's great."
                "Bill watches, beaming."
                s3_mc "Bill, this is incredible!"
                s3_other_m "Am I a good cook or what?!"
            "Tell him it looks gross":
                $ s3_mc.dislike("Bill")
                "Bill takes the plate from you, rolling his eyes."
                s3_other_m "Your opinion is incorrect."
                s3_other_m "Forget it. I was just trying to be nice."
    else:
        "He's made your favourite - his famous pancakes!"
        s3_mc "Thanks, Camilo! These look great!"
        s3_other_m "No problemo! It's the least I can do for you."
        "You down your pancakes eagerly. Camilo watches with satisfaction."
        s3_mc "Shtop shtarung at muh."
        s3_other_m "What?"
        "You swallow your mouthful."
        s3_mc "Stop staring at me!"
        s3_other_m "Sorry. Nothing more satisfying than a satisfied customer!"

    "You're distracted from breakfast as Harry lets out a loud moan."
    harry "Oh AJ, don't stop!"
    "You clear your throat loudly, stifling giggles."
    harry "I know you're there, [s3_name]. I don't care."
    harry "Some things are worth moaning for."
    "AJ winks at you from behind Harry."
    aj "Not the first time I've been told that, babes."
    aj "I give these to the girls on the team all the time."
    aj "They call me 'Magic Hands'."
    aj "Well, one girl does, but that's for different reasons."
    harry "You're a miracle worker."
    aj "You're lucky I'm here! You've got terrible form."
    aj "You're going to end up with rounded shoulders unless you stand straight."
    "She finishes up her massage and pats Harry on the back."
    aj "You're all done, mate."
    harry "Aw. Just a minute longer?"
    aj "Nope. My magic hands are too powerful. The human body can only take so much."
    aj "Who's next? [s3_name]?"

    # CHOICE
    menu:
        thought "Do I want a Magic Hands massage?"
        "No":
            aj "Aw, OK."
            "She leans in close, out of earshot of the boys."
            aj "Babe, while I've got you here, I'd love to go for a chat?"
            aj "I don't think there's anyone in the living room."
            thought "A little bit of privacy is just what we need..."
        "Yes":
            s3_mc "Why not?"
            "AJ beams and beckons you over to sit in front of her."
            "Her hands come to your shoulders, fingers firm on your muscles."
            "Warmth spreads through your back as she works out your tension."
            aj "Is the pressure OK?"
            s3_mc "It's heavenly."
            "Harry clears his throat."
            harry "See? It's not just me."
            s3_mc "I never should have judged you."
            "AJ finishes up and pats you on the back."
            aj "All done!"
            s3_mc "But..."
            aj "Sorry, babe."
            aj "Unless you wanna go into the living room?"
            thought "Sounds like she wants to talk about something in private."

    # CHOICE
    menu:
        thought "Do I want to join AJ in the living room?"
        "Yes":
            s3_mc "Sure, AJ."
            aj "Great! Let's go."
            $ s3e8p1_aj_chat = True
            call s3e8p1_aj_chat from _call_s3e8p1_aj_chat
        "No thanks ":
            aj "Aw, OK."

    "[s3e7p3_stay_m] starts to wash up the pans from breakfast."
    s3_other_m "Feels weird cooking without [s3e7p3_dump_m]..."
    s3_other_m "He was always such a laugh in the kitchen."

    if s3e7p3_dump_m == "Bill":
        s3_mc "I'm gonna miss his fry ups."
    else:
        s3_mc "I'm gonna miss his pancakes."

    "AJ smiles at him."
    aj "I think the right choice was made."
    aj "I'm glad you're here, [s3e7p3_stay_m]."
    "[s3e7p3_stay_m] pretends to wipe a tear."

    if s3e7p3_stay_m == "Bill":
        s3_other_m "Stop, you're making me weepy..."
    else:
        s3_other_m "Ah, chica..."

    harry "I don't think that's fair to say, AJ. It was a hard decision."
    aj "[s3_name] agrees with me! Right?"

    # CHOICE
    menu:
        thought "Do I think it's best that [s3e7p3_stay_m] stayed?"
        "I wanted to help [s3e7p3_stay_f]":
            # NEED TO FILL
            "EMPTY"
        "[s3e7p3_stay_m] deserves to be here":
            "Harry frowns while [s3e7p3_stay_m] pats you on the shoulder."
            s3_other_m "Thanks, [s3_name]."
        "They're both special":
            "Harry nods in agreement."
            s3_mc "Just because we saved [s3e7p3_stay_m] doesn't mean [s3e7p3_dump_m] will just be forgotten."
            aj "That's true."

    s3_mc "But Harry's right, it was a hard decision either way."
    harry "At least we all got to make it together."
    "AJ nods."
    aj "We have to stick together now."
    harry "It's so quiet here now without him."
    harry "I hate being able to hear my own thoughts."
    "He sips a cappuccino, leaving foam on his nose."
    "He puts the mug down, oblivious."

    # CHOICE
    menu:
        thought "Harry has foam on his nose..."
        "Laugh":
            "You nudge AJ and point to Harry."
            "She lets out a small laugh."
            aj "Harry, babes, you've got something on your..."
            "Harry wipes his cheeks."
            harry "Did I get it?"
            aj "Uh, yeah, hun. You got it."
        "Lick it off":
            "You hop off your seat and approach Harry. You stop in front of him and stare at his nose. He looks at you, baffled."
            harry "What are you looking at me like that?"
            "You quickly nip forwards and lick the foam off his nose."
            if s3_mc.past_partners[1] == "Harry":
                "Harry looks shocked, but then smiles, wiping his nose."
                harry "Any excuse to lick me, eh, [s3_name]?"
                harry "Maybe I should put foam in some other places..."
            else:
                "Harry yelps and jumps back."
                harry "What is it with you and licking my face?"
                harry "You're a strange one, [s3_name]."
                harry "Though, I can't say I didn't enjoy it..."
            "You sit back down."

    "The conversation freezes as [s3e7p3_stay_f] comes charging down the stairs, phone in hand."
    thought "Oh, here we go..."
    s3_other_f "I've got a text!"
    s3_other_m "We can hear you! You don't need to shout!"
    s3_other_f "It's a challenge!"
    "She comes to a halt at the breakfast bar."
    text "Howdy, Islanders! It's time to pull on your boots and separate the wheat from the chaff in today's Cowboy Challenge! #rideemcowboy #giddyup"
    s3_mc "Oh no. We're not going to have to ride a bull, are we?"
    
    scene sand with dissolve
    $ on_screen = []

    "Oh my stars! Who told her?!"
    "Looks like these little doggies have found themselves in a doozy!"
    "Will they play to the gallery and pony up the win?"
    "Or will they suck an egg and have their plans come a-cropper?"
    "Find out next time in the rootinest tootinest reality show in all the West!"
    "...Who writes this stuff?"

    jump s3e8p2
    return

label s3e8p1_aj_chat:
    scene s3-lounge with dissolve
    $ on_screen = []

    "You enter the living room with AJ."
    aj "Oh good, there's no-one here. All alone."
    s3_mc "OK, that sounds like the start of a horror movie..."
    aj "And now I'm going to peel off my mask and chase you screaming through the Villa..."

    # CHOICE
    menu:
        thought "AJ's trying to spook me..."
        "But we're friends":
            # NEED TO FILL
            "EMPTY"
        "There are cameras everywhere":
            aj "Drat. Foiled again."
        "You're the one who'll be running":
            aj "Uh, good luck catching me."
            aj "I'm lightning fast, baby!"
        "That's kinda hot" if s3_mc.bisexual:
            aj "You like  being scared?"
            s3_mc "Yep. It gets my heartbeat racing."
            aj "Well, there are loads of ways I could do that..."
            "[s3_name]. You're gonna have to show me."

    "She pats the sofa."
    aj "C'mon."
    s3_mc "You're still trying to massage me?"
    aj "Nah, I just had to get you away from everyone else."

    if s3_like_aj or "AJ" in s3_mc.past_partners:
        aj "We never get to be alone out there."
        aj "Touching you in front of everyone just felt wrong."
        aj "And too PG..."

    if "AJ" not in s3_mc.past_partners:
        aj "The stress is just kind of getting to me."
        if s3_li != "Tai":
            aj "And I'm having doubts about Tai."
        else:
            aj "And I'm having doubts about Ciaran."

    s3_mc "OK, I'll lie down in that case."
    s3_mc "But face up!"
    aj "Fine."
    "You lie down on the sofa. AJ perches on the back, looking down at you."

    if s3_like_aj or "AJ" in s3_mc.past_partners:
        aj "Mind if I lie with you?"

        # CHOICE
        menu:
            thought "Do I mind if she lies with me?"
            "Keep your distance":
                # NEED TO FILL
                "EMPTY"
                $ s3e8p1_keep_distance_aj = True
            "Only if you spoon me":
                aj "That can be arranged."
                "She slides down the sofa and snuggles into you."
                s3_mc "That's more like it."
            "Go for it":
                s3_mc "Be my guest."
                aj "Oui, oui!"
                "She slides down the sofa and snuggles into you."

                if "AJ" not in s3_mc.past_partners:
                    aj "You know, I like boys. I like their big arms and their jawlines and their stubbly faces."
                    aj "But it's hard being with them."
                    aj "Girls are so easy. I am one, so I know what to say, what to do."
                    aj "I know my way around their bodies better, too."
                    aj "But sometimes with boys, I feel like I have to prove myself to them."
                    aj "Like, cos Tai's a rugby coach, I feel like I can only talk about sport with him."
                    aj "Like, Ciaran's a bouncer. So I feel like I have to act tough around him."

                "AJ sighs, then gives you a flirty grin."
                aj "Maybe I just have someone else on my mind."
                aj "Of course, if you pick me tonight, there's nothing to worry about here..."
                "You turn to look at her. AJ is staring at your lips. She leans in slightly."
                # SUB-CHOICE
                menu:
                    thought "Do I want to kiss AJ?"
                    "No, cuddle instead":
                        # NEED TO FILL
                        "EMPTY"
                    "Yes":
                        "You close the gap between you both and kiss her."
                        "AJ giggles into the kiss before climbing on top of you, continuing to kiss you passionately as she straddles your hips."
                        "You run your hands up her back, pulling her close, and start to massage her shoulders."
                        aj "What are you doing?"
                        s3_mc "Didn't you bring me in here for a massage?"
                        aj "A ruse so clever, even you believed it..."
                        aj "I'm wasted in sports. Maybe I should mastermind a crime..."
                        "She kisses you again, and whispers in your ear."

        if s3e8p1_keep_distance_aj == False:
            aj "You know, it's my birthday tomorrow..."
            s3_mc "It is?"
            aj "What are you gonna get me for a present?"
            # CHOICE
            menu:
                thought "I'm getting you..."
                "Cuddles":
                    # NEED TO FILL
                    "EMPTY"
                "Bits":
                    aj "Can I have my present now then?"
                    s3_mc "What a coincidence, I've got it right here..."
                    "You pretend to dig into an invisible pocket, fishing something out, then use that hand to push back her hair before kissing her deeply."
                    "You feel her smiling into the kiss as she runs her hands over your body, firm and confident."
                    "You let her take control, let her move your body with hers in incredible ways."
                    "Your eyes meet, and you give each other a content smile."
                    "Afterwards, you lay your head on AJ's chest, listening to her heart beat."

        aj "I could just live here forever."
        aj "In this beautiful Villa with this beautiful girl."
        s3_mc "Your hockey team might have something to say about it."
        aj "Just during off-season, then. The Villa must be empty most of the year, when the show's not on."
        s3_mc "That would be perfect."
        s3_mc "Then we can always be alone and have moments like this."
        aj "Sounds like a plan."
        "After a while, AJ gets up. She holds her out for you to take."
    else:
        "AJ sighs and she stretches."
        aj "I just wish I was in a couple that felt right."

        # CHOICE
        menu:
            thought "AJ's worried about not being in the right couple..."
            "Try to chill out":
                # NEED TO FILL
                "EMPTY"
            "Stick at it":
                # NEED TO FILL
                "EMPTY"
            "Graft on someone else":
                s3_mc "You're in a Villa filled with beautiful people!"
                s3_mc "I bet there's someone here who's right for you."
                s3_mc "That's the whole idea of this summer, right?"
                "AJ beams at you, looking a lot happier."
                aj "Thanks, hun."
                aj "I knew I'd feel better for talking to you."
                s3_mc "Any time!"

    aj "We should head back to the others."

    if s3_like_aj or "AJ" in s3_mc.past_partners:
        aj "Don't want [s3_li] to get suspicious."
        $ pronouns(s3_li)
        # CHOICE
        menu:
            thought "[s3_li] might get suspicious about me and AJ sneaking off..."
            "You're right":
                s3_mc "Yeah, we should head back."
                aj "OK. Let's go."
            "Let [him_her]":
                s3_mc "I don't care if [he_she] sees."
                aj "You're so naughty."
                aj "C'mon, though. I want some food."

    "AJ gives your hand a squeeze before you both head back to the kitchen."

    scene s3-kitchen-day with dissolve
    $ on_screen = []

    "When you return, [s3e7p3_stay_m] and Harry are still in the kitchen, chatting about the previous night's events."

    return

#########################################################################
## Episode 8, Part 2
#########################################################################
label s3e8p2:
    scene sand with dissolve
    $ on_screen = []

    show screen day_title(8, 2) with Pause(4)
    hide screen day_title with dissolve

    "Well, howdy partners, and welcome to this here newest episode of Love Island."
    "The Islanders have had a chance to let off some steam after last night's dumpin'."

    if s3e7p3_help_pack:
        "[s3e7p3_stay_f] was chomping at the bit to find out what was said between [s3_name] and [s3e7p3_dump_f]."
        s3_other_f "Did she say anything about me?"

        if s3e8p1_nice:
            "And [s3_name] told her just what she wanted to hear."
            s3_mc "She asked me to look out for you. You're important to her."
            s3_other_f "That's so sweet of her!"
        else:
            "And [s3_name] sure gave her something to think about."
            s3_mc "She said, and I'm quoting..."
            s3_mc "'She's not the kind of girl you miss.'"
            s3_other_f "I can't believe she said that about me!"
        $ leaving('s3_other_f')
        
    "Ol' Magic Hands' AJ treated Harry to a mighty fine massage."
    harry "Oh, AJ, don't stop!"
    $ leaving('harry')

    if s3e8p1_aj_chat:
        "And [s3_name] and AJ got personal."
        if 'AJ' in s3_mc.past_partners:
            aj "We never get to be alone out there."
        else:
            if s3_li == "Tai":
                aj "I'm having doubts about Ciaran."
            else:
                aj "I'm having doubts about Tai."
        $ leaving('aj')

    "There was talk of the recouplin'..."
    "...and a breakfast that any cowboy'd be happy to cash their chips in for..."
    "... That one means 'to die for', by the way..."

    if s3e7p3_stay_m == "Camilo":
        "Though [s3_name] certainly didn't take her time to enjoy it."
        s3_mc "Shtop shtaring at muh."
    else:
        "Though we may have to take Bill's word on that one."
        bill "OK, [s3_name], look. This is how you make an omelette."
        $ leaving('bill')
        "Peanut butter, Bill? Really?"

    "Up next, it's the show you've all been waiting for. The main event."
    "Time for the Islanders to pull on their trotter boxes and don their head cases, it's shootin' time!"
    "Wait, what the heck's a 'trotter box'?"
    "They're boots, apparently. Huh. The more you know."

    "As you approach the challenge area, you see an inflatable pen set up in the centre of the platform."
    "Inside it is a mechanical bull."
    "On the other side of the ring is the makeshift façade of an Old West saloon."
    "Shooting targets of various sizes are hung upon it."
    genevieve "Woah, nelly. We've got ourselves a challenge, cow-folk."

    if s3_li == "Ciaran" or s3_li == "Tai":
        harry "Um. Was that a cowgirl voice?"
    else:
        ciaran "Um. Was that a cowgirl voice?"

    genevieve "You betcha, partner."
    genevieve "Get it?"
    "[s3e7p3_stay_f] bursts out laughing."

    if s3_li == "Ciaran" or s3_li == "Tai":
        harry "Please tell me that's not part of the challenge."
    else:
        ciaran "Ha! Love it."
    
    s3_other_m "Looks like we're in for some Bucking Bronco."
    aj "Oh, bring it on."
    aj "Our team hired one of these for an end-of-season party once."
    aj "Obviously I won. My thighs have never been more sore."

    if s3_li == "Tai":
        ciaran "Is that a challenge?"
    else:
        tai "Is that a challenge?"

    if "AJ" in s3_mc.past_partners:
        aj "That wasn't supposed to be dirty..."
    else:
        aj "Easy tiger."
        
    nicky "Guys it's mine!"
    nicky "I've just got a message."
    text "Islanders, it's time to mosey on over and pick an outfit from the boxes. You'll need to look the part today, as we find out who among you is the best at holding on to a rough ride... #thistownaintbigenough #messwiththebull"
    seb "Oh no..."

    # CHOICE
    menu:
        thought "This sounds like..."
        "A chance to show off my skills":
            s3_mc "This is gonna be epic."
            s3_mc "Not to one-up AJ, but I've got some serious skills on these things."
            s3_li "And I bet you look while you're doing it, too."
        "An opportunity for flirting":
            s3_mc "This is gonna be hilarious."
            s3_mc "I can't wait to lasso my beau."
            s3_li "I'm looking forward to it myself."
        "A disaster waiting to happen":
            s3_mc "I'm with Seb on this one. There's no way this doesn't end in disaster."
            s3_li "Don't stress it, babe. We're gonna do great."

    if s3_li == "Yasmin":
        seb "Well, at least you've got a partner."
        "He gestures to Harry."
        seb "No offence, mate. I'm just not really into the idea of getting lassoed by you."
        harry "Hey, don't worry. I'm not too worried about winning this one either."
        harry "Maybe we can play bad guys? Give the riders a little extra soaking."
        seb "That sounds more like it. We can be outlaws trying to chase down the sheriff."
        genevieve "Dag-nabbit, you curmudgeons! You know that ain't part o' this here challenge."
        harry "Pretty sure cowboy-talk isn't part of the challenge either, Viv."
        genevieve "What the deuce are you talking 'bout, Harry-boy? Got a pining for a hiding, small fry?"
        "There is a brief pause."
        s3_other_f "What does that even mean?"
        genevieve "Look, I love westerns, OK? Have I really never mentioned that?"
        ciaran "Not even once, babe. But it's hilarious."
        text "Harry and Seb - you will be competing together in this challenge as a couple. #roomformore #twocowboysonehorse"
        "Seb groans audibly."

    nicky "Let's get on with it, shall we?"
    "You realise that Nicky has already chosen an outfit from the trunk."
    elladine "Looking good!"
    genevieve "Smoking, you might say."
    nicky "Thanks, guys."
    nicky "Well, don't just stand there. Come pick an outfit!"
    "The Islanders rush towards the chests of clothes."

    #CHOICE
    menu:
        thought "Everyone's trying to get to pick their outfit first!"
        "Barge through them!":
            thought "I'm not about to let them choose before me!"
            "You charge through the stampede, stepping on more than a few toes as you go."
            s3_mc "Out of the way, slow-pokes!"
            genevieve "Ow!"
            s3_mc "Sorry, babes!"
        "Wait your turn ":
            "You follow the others over to the chests, poking your head between the other Islanders to get a good view."
            s3_mc "Leave something for me!"

    "You are pushed back to the back as the islanders grab their outfits in a frenzy."
    harry "Cor, I don't look half bad, do I?"
    aj "Hey cow-folks. Get a load of this."
    s3_other_m "Ha! This is what I'm talking about."
    s3_li "How do I look, [s3_name]?"

    $ pronouns(s3_li)
    if s3_li == "Yasmin":
        $ cow_type = 'cowgirl'
    else:
        $ cow_type = 'cowboy'

    # CHOICE
    menu:
        thought "How does [s3_li] look in [his_her] outfit?"
        "Like a million bucks":
            $ s3_mc.like(s3_li)
            s3_li "Knew I could count on you to have my back."
        "Maybe if you chose a different hat...":
            s3_li "Hmm. You think?"
            "[s3_li]'s brow furrows."
        "More cow than [cow_type]":
            $ s3_mc.dislike(s3_li)
            s3_li "You don't have to put it like that..."

    s3_li "Don't wait around! Get yourself something nice!"
    "You find a number of different cowboy accessories and toys to wear over your swimsuit."
    "[s3_li] watches as you put them on, a grin on [his_her] face."
    # "Outfit change to cowboy clothes wearing over swimwear"
    s3_li "I love it. Like a smoking gun."
    "As soon as you don your outfit, you feel a splash of cold water on your back."

    if s3_mc.past_partners[1] == s3e7p3_dump_m:
        bff "Gotcha."
    else:
        if s3_mc.past_partners[1] == "Bill":
            bill "Oops. I was practising hitting the targets."
        elif s3_mc.past_partners[1] == "Camilo":
            camilo "Oops. I was practising hitting the targets."
        elif s3_mc.past_partners[1] == "Harry":
            harry "Oops. I was practising hitting the targets."
        elif s3_mc.past_partners[1] == "AJ":
            aj "Oops. I was practising hitting the targets."
        "You don't believe [s3_mc.past_partners[1]] for a second. [he_she] doesn't look very apologetic."

    s3_mc "Hey! That was cold!"
    "You pick up a water pistol and start firing back."
    s3_other_f "Don't waste all the water or you'll not have any left for the challenge!"
    s3_other_f "Oh, what do I care! We have a whole pool."
    s3_other_f "Oh, that's me."
    text "Cowgirl, it's time to ride. First you'll need to mount the mechanical bull. Then use the rope to lasso your beau onto the saddle with you. #lassoyourbeau #lotsofknots"
    s3_other_f "It looks like Bill/Camilo and I will be up first."
    s3_other_f "We've got to try and hold and hit as many targets as possible."
    s3_other_m "Go ahead, I'll be waiting."
    s3_other_f "I really did not want to go first, but here we are."
    elladine "You'll be fine! Once you get up there, instinct will take over."
    "[s3e7p3_stay_f] climbs onto the bull with trepidation. It doesn't look like she's done this before."
    s3_other_f "What now?"
    "Suddenly, the bull jerks to life."
    "[s3e7p3_stay_f] grabs the handle in a panic."
    s3_other_f "Woah, nelly!"
    s3_other_f "Now what?"

    # CHOICE
    menu:
        thought "Should I give her some advice?"
        "Give her some words of encouragement":
            s3_mc "You got this, girl!"
            s3_mc "Holster your pistol so you can use the lasso!"
            aj "And use your strongest arm to hold on!"
            s3_other_f "I'm trying! Woah! This is so hard!"
        "Shout and whoop loudly":
            "You whoop and holler loudly like a cowgirl. The other Islanders join in."
            elladine "Go on, [s3e7p3_stay_f]!"
            nicky "I believe!"
        "Say something snarky":
            s3_mc "Don't hurt yourself too much when you fall off, [s3e7p3_stay_f]."
            s3_other_f "Hey! (you get 🙁 with [s3e7p3_stay_f])"
            "The other Islanders seem to ignore your comment."
            elladine "Go on, [s3e7p3_stay_f]!"
            nicky "I believe!"
        "Stay quiet":
            pass

    "[s3e7p3_stay_f] struggles for a while, but it's not long before she finds her balance."
    "Shakily, she starts to spin the lasso above her head, staring at [s3e7p3_stay_m] as she does."
    s3_other_f "You ready, babe?"
    s3_other_m "You bet your boots, honey."
    "[s3e7p3_stay_f] does her best to throw the lasso at [s3e7p3_stay_m], but it falls to the ground several metres short."
    s3_other_m "Almost!"
    "The bull seems to pick up speed, throwing [s3e7p3_stay_f] around like a ragdoll."
    s3_other_f "Aaah!"
    "She steadies herself for long enough to reel the lasso back in, and then goes for another shot."
    "It misses again."
    s3_other_m "Woah, cowgirl, looks like you got me!"
    "He throws himself into the pen and puts the rope around himself as if he had been lassoed."
    seb "Hey... that's cheating!"
    seb "Isn't it?"
    genevieve "Nah! Just let 'em have it. Else we'll be here all day."
    aj "Now you gotta reel him in!"
    "[s3e7p3_stay_f] weakly tugs at the lasso as [s3e7p3_stay_m] comically pretends to struggle."
    "Once he's close enough, he pulls himself onto the moving bull, with a little effort."
    "He straddles the bull behind her, as she falls back into his arms for support."
    s3_other_f "My hero."
    s3_other_m "Heads up, we've still gotta hit the targets!"
    "[s3e7p3_stay_f] and [s3e7p3_stay_m] whip out their water pistols and begin spraying wildly at the targets."
    "The water goes everywhere. Very little of it hits the targets, but [s3e7p3_stay_f] and [s3e7p3_stay_m] don't seem to mind much."
    s3_other_m "I don't think I've hit a single one."
    "Suddenly, [s3e7p3_stay_m] turns his pistol on [s3e7p3_stay_f], squirting her neck. She squeals."
    s3_other_f "[s3e7p3_stay_m]! Stop!"
    "He points the pistol towards the other Islanders instead."
    s3_other_m "This here's a hold-up. Now give me all your valuables, you darn city-slickers."
    genevieve "Not on your life, you scoundrel!"
    "[s3e7p3_stay_m] starts to spray the other Islanders with the last of his water. [s3e7p3_stay_f] joins in."

    # CHOICE
    menu:
        thought "Hey! They're just shooting at us now!"
        "Shoot back!":
            "You lift up your water pistol and return fire."
            s3_mc "Take that, you pair of no-good outlaws!"
        "Dive for cover!":
            "You dive to the ground and cover your head in your hands."
            s3_mc "Take cover!"
            "Despite trying to get out of the way, you feel a spray of cold water on the side of your face."
            s3_other_m "Can't hide from me!"
        "Play dead":
            "You clutch your heart and fall to the ground, as if dead."
            s3_mc "Tell my ma and pa... tell them... I love them..."
            if s3_mc.bff == "Elladine":
                elladine "[s3_name]! But she was so young!"
            elif s3_mc.bff == "Genevieve":
                genevieve "[s3_name]! But she was so young!"
            elif s3_mc.bff == "Nicky":
                nicky "[s3_name]! But she was so young!"
            elif s3_mc.bff == "Seb":
                seb "[s3_name]! But she was so young!"

    "Suddenly, the bull rears up especially high, and [s3e7p3_stay_m] and [s3e7p3_stay_f] come tumbling off the back."
    "They lie together for a few moments in a tangle of arms and legs, still giggling."
    bill "Honestly? Love a good Western. Absolutely classic genre."
    camilo "Mate. Who knew that could be so much fun?"
    "You feel your phone vibrate."
    text "[s3_name] and [s3_li], you're up next. Let's see your moves."
    s3_mc "My turn!"

    if s3_mc.bff == "Elladine":
        elladine "You got this, [s3_name]!"
    elif s3_mc.bff == "Genevieve":
        genevieve "You got this, [s3_name]!"
    elif s3_mc.bff == "Nicky":
        nicky "You got this, [s3_name]!"
    elif s3_mc.bff == "Seb":
        seb "You got this, [s3_name]!"

    "You make your way to the inflatable bullpen, where [s3e7p3_stay_f] and [s3e7p3_stay_m] are still recovering from their fall."
    
    if ("Bill" in s3_mc.past_partners and s3_like_bill) or s3_mc.like_mc["Bill"] > 8:
        thought "They seem to really enjoy themselves. Is Bill having second thoughts about me?"
    elif ("Camilo" in s3_mc.past_partners and s3_like_camilo) or s3_mc.like_mc["Camilo"] > 8:
        thought "They seem to really enjoy themselves. Is Camilo having second thoughts about me?"
    else:
        thought "I had my doubts about them at first, but [s3e7p3_stay_m] and [s3e7p3_stay_f] do make a cute couple."
    
    s3_other_m "That was fun. I almost want to do it again just for a laugh."
    s3_other_f "We did awfully, hun."
    s3_other_f "Not that it matters."

    # CHOICE
    menu:
        thought "[s3e7p3_stay_f] and [s3e7p3_stay_m] didn't do all that well. How am I feeling about my chances?"
        "There is no way I don't bottle this...":
            # NEED TO FILL
            "EMPTY"
        "Everyone knows who the real cowgirl in this town is":
            s3_mc "It's [s3_name]."
            "You strike a dramatic pose."
            s3_mc "I came to this town to ride bulls and tame boys/hotties (appears instead of boys)."
            s3_mc "Or was it the other way round?"
            s3_mc "Either way, you need to get out of my pen!"
            s3_other_f "We're going, we're going."
            s3_other_m "Yeah. Hold your horses."
            s3_mc "Oh, ha ha."
        "You guys shot your load too early":
            s3_mc "Riding the bull, it's all about stamina, you see."
            s3_other_m "Listen, I could teach you all a thing or two about stamina."
            s3_other_f "Is that a promise?"
            if s3s7p3_stay_m == "Bill":
                s3_other_m "Ha! Babe, if there's one thing you know about me, it's that I never say something ig I don't mean it."
            else:
                s3_other_m "For you, chica, it can be."
            s3_mc "Excuse me, lovebirds, but I do need to get on the bull, you know."

    thought "Right, time to get on with it then."
    "Once [s3e7p3_stay_m] and [s3e7p3_stay_f] have moved out of the way, you holster your water pistol, grab the lasso and clamber onto the bull."
    "No sooner have you placed your butt in the saddle do you feel the mechanical bull begin to rock."
    s3_mc "Woah!"
    s3_bff "Go on, [s3_name]!"
    s3_li "Hold on, babe!"
    "You hold on for dear life as the machine bucks and throws you around. With the lasso in one hand, you get ready to throw..."
    thought "The challenge is to lasso my partner to get them on the bull with me..."
    thought "Not that I have to follow the rules..."

    # CHOICE
    menu:
        thought "What should I do?"
        "Aim for [s3_li]":
            "You spin the lasso and throw it with all your strength in the direction of [s3_li]."
            "[he_she!c]'s ready for you, and in a flash, jumps towards it, catching [him_her]self in your knot."
            "A cheer goes up in the crowd of Islanders."
            nicky "Nice shot!"
            harry "Proper well done."
            s3_li "Got me on your first try, eh? I reckon that's a sign."
            s3_mc "Come 'ere, suga'."
            "You tug lightly on the rope - holding onto the bull takes a lot of your strength - and [s3_li] offers no resistance."
            "[he_she!c] climbs into the pen, and then onto the back of the bull. You feel [his_her] breath on your neck."
        "Am for [s3_ex] instead":
            thought "I know who my beau really ought to be..."
            "You spin up the lasso and throw it with all your strength in the direction of [s3_ex]."
            s3_ex "The challenge was to lasso your partner, [s3_name]."
            s3_ex "Not that I'm complaining."
            s3_mc "I know what the challenge was."
            s3_ex "As much as I'd love to be up there with you, babe..."
            s3_ex "Maybe another time?"
            elladine "Sorry, [s3_name], but the challenge is the challenge."
            elladine "You can't choose for this one."
            "You catch a glimpse of [s3_li] frowning uncomfortably."
            s3_ex "Go ahead, [s3_li]. I won't get in the way this time."
            "[s3_ex] gives you a reassuring wink as [s3_li] comes over and climbs on the bull behind you."
            "You feel his breath on your neck."
        "Do some tricks with the lasso":
            thought "Honestly, I doubt I'll be able to lasso anyone from here..."
            thought "Maybe I could put on a different kind of show?"
            "You start to swing the lasso above your head like you've seen in the movies."
            "Getting a rhythm for the motion, you start to spin it side-to-side as well, and then pass it from your right to your left."
            aj "OK, that's pretty impressive."
            nicky "You can say that again."
            seb "You are supposed to actually throw it, though. Just saying."
            elladine "Looks like she's having her own fun."
            "Just then, the bull jerks unpredictably, and you feel yourself thrown sideways. You're losing your balance..."
            s3_mc "Uh-oh!"
            "[s3_li] comes rushing to your aid, clambering into the bullpen and pushing you back into the saddle."
            s3_mc "Phew. Thanks, babe."
            s3_li "Any time."
            "[he_she!c] gives you a smirk, before climbing onto the back of the with you. You feel [his_her] breath on your neck."

    s3_li "Hey, hot stuff."
    "[his_her] hands run up your waist. The bull bucks and spins, and you find yourself thrown into [his_her] chest more than once."

    # CHOICE
    menu:
        thought "[s3_li] almost cradling me in [his_her] arms..."
        "Ask [him_her] not to touch you":
            "You awkwardly disentangle yourself from [s3_li]'s embrace."
            s3_mc "Sorry, honey. I'm just not there yet."
            s3_li "Alright. My bad."
        "Allow [him_her] to hold you by the waist":
            "You melt into [s3_li]'s arms. They're strong, toned, and glistening from the sweat that's starting to form."
            s3_li "Comfy?"
            s3_mc "Very."
            if s3_li == "Tai":
                tai "Choice."
                s3_mc "Huh?"
                tai "Ha, sorry. Kiwi slang. Means 'awesome'."
                s3_mc "Choice."
                "Tai smiles."
            elif s3_li == "Ciaran":
                ciaran "Grand."
            elif s3_li == "Yasmin":
                yasmin "Sweet."
        "Direct [him_her] to hold onto your shoulders":
            "You bring back one of your hands to take hold of [s3_li]'s."
            "You place [his_her] hands on your shoulder. [he_she!c] understands, and does the same with [his_her] other hand."
            s3_li "That better?"
            s3_mc "Mhmm."
            if s3_li == "Tai":
                tai "Choice."
                s3_mc "Huh?"
                tai "Ha, sorry. Kiwi slang. Means 'awesome'."
                s3_mc "Choice."
                "Tai smiles."
            elif s3_li == "Ciaran":
                ciaran "Grand."
            elif s3_li == "Yasmin":
                yasmin "Sweet."

    s3_li "Don't forget about the targets, though, eh?"
    s3_mc "Oh, shoot!"
    s3_li "That's the idea."
    "The bull is still throwing you around. It takes a lot of effort to hold on."
    s3_mc "This is harder than it looks!"
    "You raise the water pistol to the targets and take a few shots."
    "You manage to hit a few targets, but the constant movement of the machine beneath you makes it hard to get much done."

    # CHOICE
    menu:
        thought "This isn't working very well..."
        "Start firing at the other Islanders":
            # NEED TO FILL
            "EMPTY"
        "Give up and shoot at [s3_li] instead":
            s3_mc "This is going nowhere..."
            "Without warning, you twist around and aim your water pistol at [s3_li]."
            s3_li "Huh?"
            "You shoot water in [his_her] face."
            s3_li "Hey!"
            s3_mc "Too slow on the draw, babe!"
            "The bull throws you both to one side before [s3_li] can retaliate. You're both barely holding on."
            s3_other_f "Ooh, looks like there's division in the ranks!"
        "Concentrate on the shooting while [s3_li] keeps you steady":
            s3_mc "Hold me still! I need to aim properly!"
            s3_li "I've got you!"
            "You feel [s3_li] against your back. The rocking of the bull pushes you into [him_her] again and again."
            if s3_li == "Tai" or s3_li == "Ciaran":
                "His chest is smooth and chiselled. You can feel the shape of his abs and pecs against you as you melt into his arms."
            elif s3_li == "Yasmin":
                "Her chest is soft and warm. You think you can almost feel her frantic heartbeat as you melt into her arms."
            "In this position, you're able to aim with both hands, and you hit a lot more of the targets."
            nicky "Nice one, you two!"
            elladine "Great technique!"

    "The bull is getting faster, and it's getting harder and harder to stay put."
    "You notice that [s3_li] is also having trouble."
    "[he_she!c]'s holding on with both hands, barely able to keep a grasp on the pistol."

    # CHOICE
    menu:
        thought "[s3_li]'s having a bit of trouble..."
        "Moan at [him_her]":
            # NEED TO FILL
            "EMPTY"
        "Help [him_her]":
            s3_mc "I've got you."
            "You cling to [s3_li]  as best as you can, trying to prevent [him_her] from falling off the back of the bull."
            "You manage to hold [him_her] for a little while longer, but soon [his_her] weight is pulling you off with [him_her]."
            seb "I can't watch."
            elladine "How is she still holding on?"
            "With one last fierce movement, you're thrown to the ground, not far from [s3_li]."
        "Grab [his_her] pistol and go for glory.":
            $ s3e8p2_glory = True
            s3_mc "Sorry babe, but right now, you're as useful as a ten gallon hat with holes in.."
            "You grab the pistol from [s3_li]'s hand."
            s3_li "Huh?"
            "While [s3_li] is distracted, a particularly violent swing sends [him_her] flying from the saddle."
            s3_mc "Long live the queen, baby."
            "The bull goes wild beneath you. You know you don't have long left."
            "Using only your thighs to hold you in place, you start firing at the targets, a pistol in each hand."
            s3_other_f "Woah!"
            s3_bff "Atta girl!"
            "You hit a number of targets. You also miss a lot, but you know it's all for show anyway."
            s3_li "Have you done this before?!"
            "You realise that your pistols have both run out of water, and let out one more whooping shout..."
            "...before the bull finally sends you flying."
            "You crash into the soft air-cushioned plastic to raucous applause."

    nicky "That's gonna be a tough act to follow."
    harry "No kidding!"

    if s3e7p3_stay_m == "Bill":
        bill "Nice going guys. You really put on a show."
    else:
        camilo "Nice going guys. You really put on a show."

    if s3_mc.past_partners[1] == "Bill":
        bill "Especially [s3_name]."
    elif s3_mc.past_partners[1] == "Camilo":
        camilo "Especially [s3_name]."
    elif s3_mc.past_partners[1] == "Harry":
        harry "Now that's what I call fresh mozzarella."
    elif s3_mc.past_partners[1] == "AJ":
        aj "I think that was one of the hottest things I've ever seen."
    
    s3_li "Can't say I disagree with that."

    if s3e8p2_glory:
        s3_other_f "And when you took [his_her] pistol and just started riding with no hands..."
        s3_other_f "Wow!"
        s3_li "You can say that again. (you get 😍 with [s3_li])"

    "[s3_li] is still sitting in the pen with you, a wide grin on [his_her] face."

    # CHOICE
    menu:
        "Crawl over for a kiss":
            s3_mc "Come here, [cow_type]."
            "[s3_li]'s grin widens."
            "You cup your hand around [his_her] face."
            if s3_li == "Tai":
                "You catch a whiff of sandalwood, tinged with musk."
            elif s3_li == "Ciaran":
                "You catch a whiff of something minty on his breath."
            elif s3_li == "Yasmin":
                "You catch a whiff of lavender and coconut oil."
            s3_li "What's that thing that cowboys say? I'm really starting to 'cotton' to you."
            s3_mc "People say that?"
            s3_li "Yeah. Apparently it's a really old phrase that started hundreds of years ago... in England. I think... I dunno but it got to America so..."
            s3_mc "Just kiss me, [s3_li]."
            "You draw [his_her] lips to yours. They're soft and gentle."
            "You straddle [him_her] as [he_she] sits back against the edge of the inflatable pen. You feel [his_her] lips curl into a smile."
            "For a few short moments you forget the challenge and the other islanders, and explore [s3_li]."
            "A cold squirt of water jerks you back to reality."
            genevieve "Sorry babe, it's my turn!"
        "Help [him_her] stand":
            "You stand up and outstretch your hand for [s3_li]. [he_she!c] takes it with a smile."
            s3_li "You were pretty good on that bull."
            s3_mc "I aim to please."
        "Leave the pen":
            "You stand and wipe yourself down, before climbing out of the pen, leaving [s3_li] to follow you."

    if s3_li == "Yasmin":
        "Genevieve and Ciaran are up next, followed by Harry and Seb."
        "They argue about who should be lassoing who, and don't do very well."
        seb "You shoot worse than my cat."
        harry "I think I'd rather have your cat as my partner. At least she wouldn't moan as much as you."
    else:
        "Genevieve and Harry are up next, followed by Yasmin and Seb."
        "Genevieve puts on her cowgirl voice again, much to Harry's dismay."
        genevieve "Get a wiggle on, Harry-boy and shoot them targets! Ain't got no time for small fries."
        harry "Viv, please."
        genevieve "You got a pining for a hiding or summin'?"
        s3_other_f "What does that even mean?"
        genevieve "Look, I love westerns, OK? Have I really never mentioned that?"
        harry "No. You didn't."

    if s3_li == "Tai":
        "Then it's AJ's and Ciaran, with Nicky and Elladine going last."
        "AJ outlasts Ciaran by a long while. She seems to be having the time of her life without him."
    else:
        "Then it's AJ's and Tai, with Nicky and Elladine going last."
        "AJ outlasts Tai, though he seems to try his hardest. She seems to be having a great time even without him."


    nicky "Nice work AJ. At least now I know what my competition's like."

    if s3e8p2_glory:
        aj "I reckon [s3_mc]'s go was more impressive, but thanks! (if you chose “Grab [his_her] pistol and go for glory”)"

    nicky "Time to see what Ella and I can do. But I'm confident."
    s3_mc "Good luck!"
    "Elladine gets up on the bull a little unsure of herself, but manages to stay on long enough to wrangle Nicky."
    "Once Nicky is on the machine, he seems to be in his element."
    "The difference between him and Elladine is like night and day."
    elladine "Woah!"
    "She doesn't last long."
    "But Nicky stays on for longer..."
    "...and longer..."
    "...and longer."
    "No matter how much the bull tries to throw him off, he holds on."
    nicky "Woohoo!"
    "Eventually, he's tossed from the saddle, but only because he's holding on with one hand while he swings the lasso above his head."
    s3_other_m "Good job, mate."
    harry "Yeah, I think you've seriously got all of us beat. Definitely the best of the lads."
    nicky "Thanks guys. But it was really nothing."
    aj "You've done it before, haven't you?"
    nicky "Would you believe me if I said I haven't?"

    # CHOICE
    menu:
        thought "Nicky says he's never ridden one of these bulls before..."
        "I don't believe you":
            pass
        "That was really good for a first time":
            pass

    nicky "Well, it's the truth."
    nicky "I guess I just have a knack for it!"
    elladine "I'd say more than just a knack, babe. That was breathtaking."
    nicky "Oh, hello. Another text."
    text "Nice ridin', Islanders. Now it's time to vote! \nWhoever you decide was the rootinest tootinest rider will be crowned Sheriff and receive their own official badge! #hailtothesheriff"
    aj "Ooh, a badge! Does that mean Nicky should get it? He was on there for the longest, right?"
    
    s3_other_m "I'd say it's between Nicky and [s3_mc], for sure."

    # UNSURE IF THIS IS ACCURATE
    if s3_li == "Bill" or s3_li == "Camilo":
        s3_other_m "Though I might be a bit biased, there."

    if s3_li == "Yasmin":
        yasmin "It's gotta be [s3_mc]."
        if s3e8p2_glory:
            yasmin "I mean, did you see that display with the pistols? "
            yasmin "She stayed on for almost as long as he did, I reckon."
        else:
            s3_mc "Me? I wasn't on there for that long, was I?"
            yasmin "Clearly longer than you think."
        yasmin "Not to mention the outfit is incredible."
        # Add back if favourite outfits are implimented
        # yasmin "But she's also looking incredible in that outfit."
    else:
        s3_bff "It's gotta be [s3_mc]."
        if s3e8p2_glory:
            s3_bff "I mean, did you see that display with the pistols? "
            s3_bff "She stayed on for almost as long as he did, I reckon."
        else:
            s3_mc "Me? I wasn't on there for that long, was I?"
            s3_bff "Clearly longer than you think."
        s3_bff "Not to mention the outfit is incredible."
        # Add back if favourite outfits are implimented
        # s3_bff "But she's also looking incredible in that outfit."

    aj "Well, I can't decide. I think you were both amazing."
    s3_other_f "Let's not overthink it. Nicky stayed on the longest. Let's give it to him."
    harry "I think he did do pretty well. And he is sorta like our own Villa sheriff already, right?"
    nicky "What do you mean?"
    harry "You're like everyone's best mate in here, Nicky. Always sorting out trouble and being there for people."
    harry "That's what a sheriff's about, right?"

    if s3_li == "Yasmin":
        yasmin "I still think it should be [s3_mc]. What did the text say again?"
    else:
        s3_bff "I still think it should be [s3_mc]. What did the text say again?"

    nicky "'The rootinest-tootinest rider', whatever that means."
    s3_other_m "That settles it, then. Nicky is the sheriff."
    s3_other_m "Unless [s3_mc] wants to have another go?"
    s3_other_f "That's not really fair, is it?"
    s3_li "I don't see why not. It's clear I was just holding her back anyway."
    s3_li "I bet she could beat Nicky's time."
    nicky "Wanna give it a go, [s3_mc]?"
    thought "They're right. I could definitely beat Nicky's time if I went again - I was so close before."
    thought "And what's a better way to impress [s3_li]? I could really have some fun with that..."

    # CHOICE
    menu:
        thought "Shall I have another go?"
        "You're on, Nicky!":
            $ s3e8p2_ride_again = True
        "I doubt I could beat him":
            if s3_li == "Yasmin":
                yasmin "Don't be silly! You were a natural on that thing."
            else:
                s3_bff "Don't be silly! You were a natural on that thing."
                # SUB-CHOICE
                menu:
                    thought "Am I sure I don't want to have another go? I won't get another chance to be 'Sheriff of the Villa'."
                    "I'll show him what I'm made of.":
                        $ s3e8p2_ride_again = True
                    "Nicky will make the better sheriff.":
                        nicky "You really think so?"
                        s3_other_m "Defo."
                        nicky "Alright, then I guess I can't argue about that."
                        aj "Found the badge!"
                        "AJ presents a large, five-pointed star with the word 'SHERIFF' printed across it in big capital letters."
                        aj "Shame it's made of plastic."
                        nicky "Ha. I'll take it anyway. You've all humbled me."
                        "He takes the badge and pins it to his outfit. It looks ridiculous on his sexy cowboy outfit."
                        camilo "You deserve it mate."
                        elladine "What if you make [s3_mc] your deputy too? As a compromise?"
                        nicky "Not a bad idea. I'd be chuffed to have her as my deputy."
                        s3_mc "Aw. Thanks, you guys."
                        nicky "I do declare that as the sheriff of this here Villa, I will take [s3_mc] to be my lawful deputy."

    "The Islanders cheer."
    aj "Woo!"
    tai "Congrats, guys."
    ciaran "Yeah, nicely done."
    genevieve "Tell you what, partners. Now all we need is a proper showdown. Every good Western ends in a showdown."
    s3_other_f "Ooh! You're right."
    genevieve "As everyone knows the showdown always happens at high noon. What's the time?"
    seb "Uhh, quarter past one."
    genevieve "Close enough."
    elladine "It sounds like fun! But who's in the showdown? Maybe the sheriff against an outlaw?"
    seb "That's too obvious. We need something with a bit more drama. Something with some real stakes."
    
    # If MC's partner from day 3 is not dumped
    if s3_ex == "Harry" or s3_ex != s3_other_m or s3_ex == "AJ":
        seb "I reckon it should be [s3_ex] against [s3_li]."
        seb "You know, for [s3_mc]'s love."
        "There's an uneasy pause after Seb's suggestion."
        elladine "Well... it's not like we haven't seen the tension there."
        s3_li "I'm up for it if [he_she] is."
        s3_ex "Oh, really?"

        # CHOICE
        menu:
            "They're going to fight for me?"
            "Please don't":
                s3_mc "I don't want to be that girl that everyone fights over. It's not fun at all."
                s3_mc "And there's gonna be a recoupling later anyway. We can save the drama for then."
                s3_ex "That's fair."
                nicky "Something else, then."
                
                if s3e8p2_ride_again:
                    nicky "Maybe if the sheriff's a little bit tired after that rodeo, her deputy could step in for her?"
                else:
                    nicky "As the sheriff round here, I think it's my responsibility to defend you all."
                
                nicky "And I've heard word of a no-gooder lurking around these parts."
                nicky "Anyone happen to know anything about that?"
                aj "Ooh! Can I be the baddy?"
                aj "I always wanted to be one of the sexy girl villains, like the ones in the Bond movies."
                aj "Or maybe I just fancied them to be honest. A bit of both, probably."
                nicky "Sounds good to me."
                s3_mc "Face away from each other, then! Take three paces and then turn and draw."
                genevieve "That's not how they did it."
                s3_other_f "Don't worry about it, hun. It's all for the drama anyway."
                "Nicky and AJ stand back to back."
                s3_mc "Now take three steps."
                s3_mc "One..."
                s3_mc "Two..."
                aj "Draw!"
                "AJ swings around suddenly and squirts Nicky in the back of the head."
                nicky "Hey, no fair! You're supposed to draw after three!"
                aj "What can I say? I told you I wanted to be a bad guy."
                nicky "You're so dead!"
                "Nicky aims for AJ and returns fire. He misses, and hits Seb instead."
                seb "Hey! Don't drag me into this!"
                "Seb shoots back. Nicky dives for cover. It's not long before another water fight has broken out."

            "I love being fought over":
                s3_li "In that case, how can we refuse?"
                s3_ex "Anything for the chance to win my girl's affections."
                s3_mc "Face away from each other, then! Take three paces and then turn and draw."
                genevieve "That's not how they did it."
                s3_other_f "Don't worry about it, hun. It's all for the drama anyway."
                "[s3_li] and [s3_ex] stand back to back."
                s3_mc "Now take three steps."
                s3_mc "One..."
                s3_mc "Two..."
                s3_ex "Draw!"
                "[s3_ex] swings around suddenly and squirts [s3_li] in the back of the head."
                s3_li "Hey, no fair! You're supposed to draw after three!"
                s3_ex "All's fair in love and war."
                s3_li "You're so dead!"
                $ pronouns(s3_ex)
                "[s3_li] aims for [s3_ex] and returns fire. [he_she!c] misses, and hits Seb instead."
                seb "Hey! Don't drag me into this!"
                "Seb shoots back. [s3_li] dives for cover. It's not long before another water fight has broken out."
    
    # If MC's partner from day 3 is dumped
    else:
        seb "Shame that [s3_ex] isn't around. Reckon it would have been fun to see him fight [s3_li]."
        seb "You know, for [s3_mc]'s love."
        s3_li "Lucky for me he's not."
        menu:
            "Seb suggested a showdown for my affection..."
            "I wouldn't want anyone to fight over me":
                s3_mc "I don't want to be that girl that everyone fights over. It's not fun at all."
                seb "Yeah, I get that. Sorry, [s3_mc]."

            "I love being fought over":
                seb "See? It could have been a high-tension battle. Lots of emotional weight behind it."
                seb "Ah, well. He's not here, anyways."

        nicky "Something else, then."

        if s3e8p2_ride_again:
            nicky "Maybe if the sheriff's a little bit tired after that rodeo, her deputy could step in for her?"
        else:
            nicky "As the sheriff round here, I think it's my responsibility to defend you all."

        nicky "And I've heard word of a no-gooder lurking around these parts."
        nicky "Anyone happen to know anything about that?"
        aj "Ooh! Can I be the baddy?"
        aj "I always wanted to be one of the sexy girl villains, like the ones in the Bond movies."
        aj "Or maybe I just fancied them to be honest. A bit of both, probably."
        nicky "Sounds good to me."
        s3_mc "Face away from each other, then! Take three paces and then turn and draw."
        genevieve "That's not how they did it."
        s3_other_f "Don't worry about it, hun. It's all for the drama anyway."
        "Nicky and AJ stand back to back."
        s3_mc "Now take three steps."
        s3_mc "One..."
        s3_mc "Two..."
        aj "Draw!"
        "AJ swings around suddenly and squirts Nicky in the back of the head."
        nicky "Hey, no fair! You're supposed to draw after three!"
        aj "What can I say? I told you I wanted to be a bad guy."
        nicky "You're so dead!"
        "Nicky aims for AJ and returns fire. He misses, and hits Seb instead."
        seb "Hey! Don't drag me into this!"
        "Seb shoots back. Nicky dives for cover. It's not long before another water fight has broken out."

    "You're caught in the crossfire."
    tai "Oh, sorry [s3_mc]! Didn't mean to hit you, there."
    bff "I did!"
    "The water pistols soon run dry, but spirits are definitely lifted."
    aj "Oh, soot. Looks like the fun's on pause critters. I got a text."

    if s3e8p2_ride_again:
        text "Sheriff [s3_mc]! Time to round up your posse and head back to the Villa for a real showdown. It's the recoupling! #stickmeup #pickyourpartner"
    else:
        text "Sheriff Nicky! Time to round up your posse and head back to the Villa for a real showdown. It's the recoupling! #stickmeup #pickyourpartner"
    
    aj "I was wrong."
    aj "The fun's not just on pause, it's all over."
    seb "Yeah. I'd almost forgotten we had this coming up tonight."
    nicky "Don't worry guys. I have a feeling it'll all work out."

    if s3e8p2_ride_again:
        nicky "So sayeth the Sheriff's deputy."
    else:
        nicky "So sayeth the Sheriff of the Villa."

    "As you head back to the Villa, Genevieve starts to sing."
    genevieve "I shot the sheriff..."
    seb "...With a water pistol."
    genevieve "...but I did not shoot the deputy..."
    "Lovely rendition there, Viv, but you can't fool me."

    if s3e8p2_ride_again:
        "I saw those cheeky shots you took at [s3_mc] when you thought no one was watching."
    else:
        "I saw those cheeky shots you took at Nicky when you thought no one was watching."

    "Meanwhile, I'm in here, dry as a bone. Missing out on all the fun."
    "Frankly, it's criminal."
    "Sheriff, I'd like to report a crime!"

    "Coming up!"
    "It's the recoupling we've all been waiting for!"
    elladine "Whoever we end up with tonight is who we really want."
    "Have the new additions turned any heads?"
    "Will everyone get to be with who they want and live happily ever after?"
    "Who knows? Anything could happen! Otherwise it wouldn't be Love Island."
    "Until next time, partners!"

    jump s3e8p3
    return

label s3e8p2_ride_again:
    "You dash back towards the bullpen and mount the machine again."
    "For a moment you're not sure if it will start, but then it lurches into action."
    "You feel a surge of adrenaline as you feel everyone watching you."

    # CHOICE
    menu:
        "Here it goes..."
        "Yeehaw!":
            "You whoop and holler and make sure to put on a good show for the Islanders."
            tai "Choices."
            aj "She's a natural. I can tell."
            $ s3_mc.like("Tai")
            $ s3_mc.like("AJ")

        "Focus on beating Nicky's time":
            "You stick your head down and put all of your effort into staying on the bull."
            yasmin "That's some laser focus right there."

        "Scream and hold on for dear life":
            "The bull seems faster this time, or is it your imagination?"
            "You grip it by the neck and hold on for dear life."
            s3_mc "This was a mistake!"
            s3_other_m "Oh my day, [s3_mc]."
            tai "Is she alright?"

    "With no targets to shoot and no one on the bull with you, you're able to concentrate better on what you're doing."
    "The bull bucks and twists, but you manage to keep your grip. Your thighs burn from the effort of keeping them glued to the machine."
    bff "Told you she could do it."
    harry "Oh my word."
    s3_li "I should have let her go on her own from the start."
    "You hold on for dear life as you're tossed around."
    "You can't keep track of how long you've been on the bull, but it feels like a long time."
    thought "This must have been longer than Nicky by now."
    "The Islanders are cheering and whooping for you outside the pen."

    # CHOICE
    menu:
        "They're really enjoying the show I'm putting on. I should..."
        "Rub it in Nicky's face":
            s3_mc "Hey Nicky!"
            s3_mc "Are you regretting this idea yet?"
            nicky "Not at all. You're doing great."
            s3_mc "You bet I am."
            s3_mc "There's a new sheriff in town, Islanders."
            s3_li "And she's smoking hot."
            $ s3_mc.like(s3_li)
            "You can't keep it up forever. Your legs start to ache and burn, and you're eventually chucked from the bull."

        "Make some saucy jokes":
            s3_li "Phew. get a load of this cowgirl's stamina."
            $ s3_mc.like(s3_li)
            s3_mc "You know it, Ciaran/Tai/Yasmin."
            s3_mc "Now I just need something other than a bull to ride..."
            harry "Oh dear, [s3_mc], what a terrible line."
            "You can't keep it up forever. Your legs start to ache and burn, and you're eventually chucked from the bull."

        "Try and do some tricks before I'm knocked off":
            thought "My last chance to impress, I suppose."
            "Having beaten Nicky's time, you let go with one hand and start to gyrate in the saddle, making sure to put on a show for the other Islanders."
            s3_mc "Bet you can't do this!"
            "During a lull in the bull's movement, you stand up in the stirrups and let out a final whooping cry..."
            "...before being thrown from the saddle in one quick twist of the machine."

    nicky "Well, that settles it."
    "You give yourself a moment to relax before standing and rejoining the other Islanders."
    s3_mc "My legs feel like jelly!"
    harry "I'm not surprised."
    "You turn to face Nicky."
    s3_mc "There's a new sheriff in town. It's MC."
    "Nicky raises his hands, palms facing outwards towards you."
    nicky "Well, I know when I've been beat."
    s3_mc "Now hand over your badge and your gun."
    "Nicky grins sheepishly as he hands over his water pistol to you."
    aj "I've got the badge! Found it in the trunk just now."
    "AJ presents a large, five-pointed star with the word 'SHERIFF' printed across it in big capital letters."
    aj "Shame it's made of plastic."
    s3_mc "That's OK. I'm honoured, guys. Really."

    # NEED TO ADD
    # Add sheriff badge to MC's outfit
    "You pin the badge to your swimsuit. It looks a little silly, but you feel a burst of pride nonetheless."
    s3_li "Now that's a sheriff I'd lay down my life for."
    elladine "Hmm. May I make a suggestion?"
    "You cough loudly and point at your badge."
    elladine "Sorry... May I make a suggestion please, Sheriff?"
    s3_mc "Go right ahead."
    elladine "Seeing as Nicky had the best time the first time round, and he was so humble about giving it up..."
    elladine "I propose a consolation prize."
    nicky "What did you have in mind?"
    elladine "You should be MC's deputy!"
    nicky "I could live with that."
    seb "Hear hear!"
    nicky "If the Sheriff will have me?"
    s3_mc "Of course, babes! We'll make a great team."
    s3_mc "As the Sheriff of this here Villa, I do declare Nicky Horne to be my lawful deputy."

    return

# #########################################################################
# ## Episode 8, Part 3
# #########################################################################
label s3e8p3:
    scene sand with dissolve
    $ on_screen = []

    show screen day_title(8, 3) with Pause(4)
    hide screen day_title with dissolve
    "Well howdy there, partners!"
    "Hold onto your saddles, 'cos we've got a doozy of an episode for ya!"
    "I'm all a'tizzy at what's afoot on this here Love Island!"
    "My god, I can't stop..."
    "Tonight, it's a girl's choice recoupling!"
    genevieve surprised "I'm going to shake things up a bit..."
    $ leaving("genevieve")
    "And plans come a-cropper..."
    $ entering("s3_mc_image")
    s3_mc surprised "This is it. Who am I going to choose?"
    $ leaving("s3_mc_image")
    "This one's gonna be a doozy cow-pokes!"

    scene s3-bean-bags-night with dissolve
    $ new_scene()
    $ outfit = "evening"

    "You're sitting on the beanbags with the girls. There is a nervous tension in the air."
    "You can see the boys huddled together on the daybeds. They keep glancing over in your direction."
    "You're drinking cocktails, because the situation calls for it."
    "Elladine necks hers in one gulp and addresses the group."
    elladine surprised "Right, girls. We need to coordinate."
    aj surprised "Huh?"
    elladine cheeky "Everyone says who they're picking, then we'll know what to expect."
    elladine neutral "That way there are no surprises."
    genevieve happy "Surprises are the whole reason I'm here!"
    genevieve surprised "If we know who everyone's picking, there's no drama."
    if s3_other_f == "Iona":
        iona surprised "Chill out Elladine. It'll be fun!"
        show genevieve neutral
        iona cheeky "What's life in the Villa without a few surprises?"
    else:
        miki surprised "And drama makes everything more exciting!"
        miki smile "Like, that's the key to going viral."
        show genevieve neutral
        miki blush "Sometimes I film myself falling off the barge, just because people love seeing that."
        miki smile "You gotta do it for the views, girls! Keep the tension levels up."
        elladine angry "But I don't want the tension to be up!"
    elladine blush "Sorry. Just worried I guess."
    genevieve smile "I think we all are, hun. Some of us are just better at hiding it."
    
    # CHOICE
    menu:
        thought "I should chime in..."
        "Agree with Elladine":
            show s3_mc_image surprised
            $ s3_mc.like("Elladine")
            show elladine smile
            s3_mc "I agree with Elladine."
            s3_mc happy "We should sort it all out now, so we don't step on each other's toes."
        "Comfort Elladine":
            s3_mc happy "By the time you close your eyes to sleep tonight, it'll all be over and you'll be cuddled up with Nicky. Think about that."
            $ s3_mc.like("Elladine")
            elladine happy "You're right. Thanks, [s3_name]."
        "Agree with Genevieve":
            if s3e8p2_ride_again == True:
                s3_mc happy "As the Sheriff of this here Villa..."
                s3_mc "Miss Genevieve is correct."
            else:
                s3_mc happy "Genevieve is right."
            s3_mc neutral "Elladine, babe, you got to live in the moment."
            s3_mc happy "Everything's gonna work out fine."
            elladine smile "I don't agree but... maybe you're right."

    elladine sad "Unless someone chooses Nicky..."
    genevieve surprised "I might do that. Just to shake things up."
    show s3_mc_image surprised
    elladine surprised "Genevieve! This might be the last recoupling!"
    show s3_mc_image neutral
    elladine angry "Whoever we end up with tonight is who we really want."
    show genevieve sad
    elladine neutral "And I know you don't want Nicky."
    if s3e8p1_hope_recoupling_yasmin:
        $ entering("yasmin")
        "Yasmin catches your eye and winks at you."
    if s3_like_aj:
        $ entering("aj")
        "AJ nudges you and smiles."
    if s3_like_aj and s3e8p1_hope_recoupling_yasmin:
        menu:
            thought "Both AJ and Yasmin are looking at me..."
            "Fart":
                # NEED TO FILL
                "EMPTY"
            "Smile at AJ":
                $ s3_mc.like("AJ")
                show aj smile
                "You smile at AJ. She smiles back at you. Yasmin doesn't seem to notice."
            "Wink at Yasmin":
                $ s3_mc.like("Yasmin")
                show yasmin smile
                "You wink at Yasmin. She smiles at you. AJ doesn't seem to notice."
    
    show s3_mc_image surprised
    show elladine surprised
    "You all jump at the text tone. Yasmin looks at her phone."
    text "Islanders, please gather by the fire pit for the recoupling. #putthemup #yellowbellied"
    "Yasmin calls over to the boys."
    yasmin surprised "Boys! Firepit!"
    show s3_mc_image neutral
    "They don't seem to hear her, still deep in discussion."
    yasmin sad "[s3_name], get their attention, will you?"
    show yasmin neutral

    # CHOICE
    menu:
        thought "How do I get their attention?"
        "Command the boys to assemble!":
            show s3_mc_image surprised
            "You stand, facing the boys, and bellow at the top of your lungs."
            s3_mc happy "Boys! Assemble!"
            "The boys' head turns towards you."
            "Tai is the first to run over."
            tai smile "Tai smash!"
            "He bounds over to the firepit."
            "Harry sprints behind him."
            harry happy "Hey! Brute strength is nothing when you're a genius billionaire... like I will be once I pay off my student loan!"
            "The rest of the boys soon follow."
            if s3_other_m == "Bill":
                show s3_mc_image neutral
                s3_other_m happy "Ready for action."
            else:
                show s3_mc_image neutral
                s3_other_m happy "Are we gonna fight?!"
            ciaran happy "Where's everyone running to?"
            "He runs after the rest of the boys blindly, grinning widely."
        "Say something filthy about a yurt?":
            "All the boys' heads immediately whip round."
            s3_mc cheeky "Bits! In a yurt?!"
            harry surprised "Who did bits on a yacht?"
            tai cheeky "I think it's about putting bits in their yoghurt."
            ciaran happy "She said yurt'!"
            s3_other_m smile "That's not even a word."
            tai surprised "Yoghurt is a word!"
            s3_mc happy "Just get over here! It's recoupling time."
            "The boys walk towards the firepit. Ciaran approaches you."
            ciaran cheeky "You did say yurt, right? Who was it?"
            s3_mc "Er... Viv. At a festival."
            genevieve surprised "How did you know?!"
        "Burp really loudly":
            show s3_mc_image cheeky
            "You stand, flexing your stomach muscles, summoning gas from the deepest pits inside you."
            elladine surprised "[s3_name], what are you..."
            "You unleash a monstrous burp."
            "The girls squeal, but it succeeds in getting the boys' attention."
            s3_other_m surprised "That was impressive."
            ciaran cheeky "Why am I turned on?"
            s3_mc happy "Firepit time!"
            "They head over, every boy giving you a high-five as they pass."

    "When the boys are all in place, you and the other girls look at each other."
    s3_other_f surprised "Good luck everyone!"
    genevieve smile "Yeah girls, good luck."
    elladine serious "We can do this."
    aj happy "Let's go!"
    
    scene s3-firepit-night with dissolve
    $ new_scene()

    "You sit down around the firepit with the rest of the girls. The boys line up in front of you."

    # TO DO: This needs to be fixed to not have non-LI NPCs in there
    $ sorted_li_like = {key: value for key, value in sorted(s3_mc.like_mc.items(), key=lambda item: item[1])}
    $ s3_fav_li = list(sorted_li_like.keys())[-1]

    if s3_fav_li == "Bill":
        "Bill catches your eye, and gives you a wink and a smile."
    elif s3_fav_li == "Harry":
        "Harry makes a point of giving you a big smile."
    elif s3_fav_li == "Camilo":
        "Camilo catches your eye, and gives you a wink and a smile."
    elif s3_fav_li == "Ciaran":
        "Ciaran gives you a small wave and a shy smile."
    elif s3_fav_li == "Tai":
        "Tai catches your eye, flashes a smile, and blows you a kiss."
    elif s3_fav_li == "Yasmin":
        "Yasmin, sitting next to you, gives your hand a reassuring squeeze."

    "You wait for a text."
    s3_mc surprised "That's my phone!"
    text "[s3_name], you will be choosing first."
    if s3e8p1_hope_recoupling_yasmin:
        yasmin "Perfect!"
        $ leaving("yasmin")
    if s3_like_aj:
        aj surprised "Lucky!"
        $ leaving("aj")
    show s3_mc_image neutral
    "You stand facing the boys."
    thought "This is it..."

    # CHOICE
    menu:
        s3_mc "I want to couple up with this person because..."
        "I see us having a future together":
            s3_mc @ sad "And I want to see if I'm right."
        "They're hot":
            s3_mc @ cheeky "And so am I, so it makes sense."
        "They make me laugh":
            s3_mc @ cheeky "And there's nothing more important than that."
    
    # CHOICE
    menu:
        s3_mc "They make me feel..."
        "Fuzzy":
            s3_mc "My insides get all wibbly whenever I look at them."
            s3_mc happy "In a good way. Not like when I eat Mexican food."
        "Horny":
            s3_mc cheeky "If I had a horn, I would be honking all day."
        "Safe":
            s3_mc happy "When I'm in their arms, I don't feel like I'm miles and miles away from the UK. I feel like I'm home."
            s3_mc sad "Should have brought some crackers for cheese."

    # CHOICE
    menu:
        s3_mc cheeky "So the person I want to couple up with is..."
        "Bill" if s3_other_m == "Bill":
            show s3_mc_image happy
            bill happy "Get in!"
            bill cheeky "[s3_name], you're amazing and I can't wait to get to know you better."
            if "Bill" in s3_mc.past_partners:
                bill happy "Thank you for coming back to me."
            if s3e8p1_hope_recoupling_yasmin:
                "Yasmin gives you a hurt look."
                $ s3_mc.dislike("Yasmin")
            show s3_mc_image neutral
            $ s3_li = "Bill"
            $ s3_li_lower = s3_li.lower()
            $ s3_mc.current_partner = "Bill"
            $ s3_mc.past_partners.append("Bill")
            $ s3_mc.like_mc["Bill"] += 5
        "Camilo" if s3_other_m == "Camilo":
            show s3_mc_image happy
            camilo happy "Oh, get in!"
            camilo "I swear down, you won't regret it, I'm going to treat you so good, chica."
            if "Camillo" in s3_mc.past_partners:
                camilo cheeky "Thank you for coming back to me."
            if s3e8p1_hope_recoupling_yasmin:
                "Yasmin gives you a hurt look."
                $ s3_mc.dislike("Yasmin")
            $ s3_li = "Camilo"
            $ s3_li_lower = s3_li.lower()
            $ s3_mc.current_partner = "Camilo"
            $ s3_mc.past_partners.append("Camilo")
            $ s3_mc.like_mc["Camilo"] += 5
        "Tai":
            if  "Tai" not in s3_mc.past_partners:
                tai smile "Yes!"
            else:
                tai smile "I knew I made the right choice picking you."
            tai cheeky "You won't regret this, I promise."
            if s3e8p1_hope_recoupling_yasmin:
                "Yasmin gives you a hurt look."
                $ s3_mc.dislike("Yasmin")
            $ s3_li = "Tai"
            $ s3_li_lower = s3_li.lower()
            $ s3_mc.current_partner = "Tai"
            $ s3_mc.past_partners.append("Tai")
            $ s3_mc.like_mc["Tai"] += 5
            show tai smile
        "Ciaran":
            if  "Ciaran" not in s3_mc.past_partners:
                ciaran surprised "Really?"
            else:
                ciaran happy "Thanks for sticking with me. I knew I made the right decision choosing you."
            show s3_mc_image happy
            ciaran grimace "So all those nice things you just said were about me?"
            show s3_mc_image sad
            ciaran happy "Brilliant!"
            show s3_mc_image happy
            ciaran cheeky "I can't wait to get to know you better, [s3_name]."
            if s3e8p1_hope_recoupling_yasmin:
                "Yasmin gives you a hurt look."
                $ s3_mc.dislike("Yasmin")
            show ciaran happy
            $ s3_li = "Ciaran"
            $ s3_li_lower = s3_li.lower()
            $ s3_mc.current_partner = "Ciaran"
            $ s3_mc.past_partners.append("Ciaran")
            $ s3_mc.like_mc["Ciaran"] += 5
        "Harry":
            harry happy "Oh, thank god."
            show s3_mc_image surprised
            harry surprised "I was getting so nervous there, my arse was sweating."
            if "Harry" in s3_mc.past_partners:
                harry serious "I've wanted you back ever since you got nicked from me."
                show s3_mc_image happy
                harry cheeky "Thanks for coming back to me."
            else:
                harry blush "I didn't even think you liked me..."
            $ s3_mc.like("Harry")
            harry happy "I think we're gonna be really happy together."
            show s3_mc_image neutral
            if s3e8p1_hope_recoupling_yasmin:
                "Yasmin gives you a hurt look."
                $ s3_mc.dislike("Yasmin")
            $ s3_li = "Harry"
            $ s3_li_lower = s3_li.lower()
            $ s3_mc.current_partner = "Harry"
            $ s3_mc.past_partners.append("Harry")
            $ s3_mc.like_mc["Harry"] += 5
        "AJ" if s3_mc.bisexual:
            $ entering("aj","smile")
            "AJ punches the air."
            aj surprised "Yes!"
            show s3_mc_image surprised
            aj smile "I was going to pick you!"
            if "AJ" in s3_mc.past_partners:
                aj cheeky "Thanks for coming back to me, babe."
                show s3_mc_image happy
                aj smile "I knew we were meant to be."
                aj blush "I only wish I'd got to make the romantic speech..."
            show s3_mc_image happy
            show aj smile
            if s3e8p1_hope_recoupling_yasmin:
                "Yasmin gives you a hurt look."
                $ s3_mc.dislike("Yasmin")
            $ s3_li = "AJ"
            $ s3_li_lower = s3_li.lower()
            $ s3_mc.current_partner = "AJ"
            $ s3_mc.past_partners.append("AJ")
            $ s3_mc.like_mc["AJ"] += 5
        "Yasmin" if s3_mc.bisexual:
            yasmin cheeky "Fabulous. I can't wait to see where this goes."
            if "Yasmin" in s3_mc.past_partners:
                yasmin surprised "I was pretty confident, but you can never be 100 percent."
            yasmin cheeky "You make me nervous in ways I don't usually get."
            yasmin smile "This is just what I hoped for."
            $ s3_li = "Yasmin"
            $ s3_li_lower = s3_li.lower()
            $ s3_mc.current_partner = "Yasmin"
            $ s3_mc.past_partners.append("Yasmin")
            $ s3_mc.like_mc["Yasmin"] += 5

    $ pronouns(s3_li)
    "You and [s3_li] embrace amid applause. [s3_bff] whoops and claps harder than anyone else."
    "You take [his_her] hand as [s3_li] sits down next to you, squeezing it reassuringly."
    show s3_mc_image neutral
    "A silence, and then..."
    "Elladine springs up, clutching her phone."
    if s3_li == "Bill":
        $ leaving("bill")
    elif s3_li == "Camilo":
        $ leaving("camilo")
    elif s3_li == "Tai":
        $ leaving("tai")
    elif s3_li == "Ciaran":
        $ leaving("ciaran")
    elif s3_li == "Harry":
        $ leaving("harry")
    elif s3_li == "AJ":
        $ leaving("aj")
    elif s3_li == "Yasmin":
        $ leaving("yasmin")
    elladine surprised "My turn!"
    elladine happy "I want to couple up with this guy because, well, I couldn't imagine coupling up with anyone else!"
    elladine blush "He always makes me laugh, and I've learned a lot from him."
    show s3_mc_image happy
    elladine cheeky "Like, did you guys know that Finland has the most metal bands per capita?"
    show s3_mc_image neutral
    elladine happy "Anyway...the guy I want to couple up with is..."
    show s3_mc_image happy
    elladine smile "Nicky!"
    $ entering("nicky","happy")
    "You and the other Islanders applaud as Nicky steps out of the line-up."
    if s3e8p2_ride_again:
        nicky "Elladine, nothing could have made me happier."
        nicky smile "All the stuff you just said... ditto."
        elladine smile "Oh, thanks."
        elladine blush "I guess."
    else:
        "He grins, and starts shooting finger guns up in the air."
        nicky smile "Nothing could make the Sheriff of the Villa happier!"
        elladine "Hey, I can always change my mind..."
    "They kiss before sitting next to each other."
    $ leaving("nicky")
    $ leaving("elladine")
    "[s3_other_f]'s phone beeps next. She stands to address the boys."
    if s3_li != s3_other_m:
        s3_other_f cheeky "I want to couple up with this boy because I proper like him. "
        show s3_mc_image neutral
        s3_other_f surprised "And I wouldn't want to be with anyone else."
        s3_other_f neutral "So I'd like to couple up with..."
        show s3_mc_image happy
        s3_other_f cheeky "[s3_other_m]."
        $ entering("s3_other_m_image","happy")
        "[s3_other_m] punches the air a little before sitting down next to [s3_other_f], taking her hand and kissing it."
        s3_other_m neutral "You make me so happy, [s3_other_f]. Thanks for picking me."
        $ leaving("s3_other_m_image")
        $ leaving("s3_other_f_image")
    else:
        s3_other_f sad "Well, I'm disappointed."
        s3_other_f serious "But I'm not one to stand in the way of love..."
        s3_other_f smile "So, I'd like to couple up with this guy because we're great friends and... I don't want to go home."
        s3_other_f "The boy I want to couple up with is..."
        show s3_mc_image happy
        s3_other_f happy "Harry."
        $ entering("harry","happy")
        "Harry smiles and kisses [s3_other_f] on the cheek before sitting next to her."
        $ leaving("s3_other_f_image")
        $ leaving("harry")
    show s3_mc_image neutral
    if s3_li != "Yasmin":
        "Yasmin is the next one to receive a text."
        if s3e8p1_hope_recoupling_yasmin:
            yasmin sad "Well, I'd hoped to already picked by someone..."
            yasmin "But since it's my choice now..."
        if s3_li == "Ciaran" or s3_li == "AJ":
            yasmin blush "This might surprise some of you, but..."
            yasmin happy "I actually think me and this guy might be a good fit, and I'm excited to get to know him better."
            show s3_mc_image happy
            yasmin cheeky "So I'm picking Harry."
            "Harry raises his eyebrows in surprise, but then smiles before sitting next to Yasmin."
            harry cheeky "I'm surprised, but flattered."
            harry happy "Let's give this a go!"
            $ leaving("harry")
            $ leaving("yasmin")
        else:
            yasmin "I want to couple up with this boy because we came in together, so we may as well stick that way."
            yasmin smile "The boy I'd like to couple up with is..."
            show s3_mc_image happy
            yasmin cheeky "Ciaran."
            "Ciaran smiles and gives her an awkward hug before sitting beside her."
            ciaran happy "Thanks, Yasmin. You're a good friend."
            $ leaving("ciaran")
            $ leaving("yasmin")
    show s3_mc_image neutral
    "Genevieve's phone goes off next."
    "She looks at the boys left in front of her and takes a deep breath."
    genevieve surprised "I'm going to shake things up a bit..."
    show s3_mc_image surprised
    genevieve smile "I'm picking this guy because I wanna get to know him better."
    genevieve neutral "We haven't been coupled up before, but I think we could make a great pair."
    show s3_mc_image neutral
    genevieve blush "I haven't run this by him, so I hope it's OK with him. But we've grown close as friends, and I'd like to pursue something more."
    genevieve smile "And if he treats me anywhere near close to how he treats his cats, I'm golden."
    genevieve neutral "So I'd like to couple up with..."
    genevieve smile "Seb."
    $ entering("seb","smile")
    "Seb breaks into a huge grin."
    seb surprised "Woah, Viv. Really?"
    show s3_mc_image happy
    "The Islanders whoop and holler as Seb blushes and kisses Genevieve on the cheek."
    show seb smile
    "Seb and Genevieve are both smiling nervously as they sit down."
    if s3_mc.bff == 'Genevieve':
        $ s3_mc.like('Genevieve')
        "You give Genevieve a thumbs up. She gives you one back."
    $ leaving("seb")
    $ leaving("genevieve")
    show s3_mc_image neutral
    if s3_li != "AJ":
        "AJ is the last to receive a text. "
        aj surprised "I want to couple up with this person because..."
        if "AJ" in s3_mc.past_partners:
            aj sad "Well, to be honest, my first choice is gone."
            aj serious "But you live and learn, eh?"
        else:
            aj sad "I haven't really found someone I connect with romantically in here."
            aj smile "But I think this lad and I get on pretty well."
        aj neutral "So the person I'd like to couple up with is..."
        show s3_mc_image happy
        if s3_li == "Tai" or s3_li == "Yasmin":
            aj smile "Harry."
            harry happy "Yeehaw!"
            "He gives AJ a high-five."
        else:
            aj smile "Tai."
            tai happy "Looks like this town is big enough for the both of us!"
            "He embraces AJ in a big hug."
        show s3_mc_image neutral
    if s3_li == "Yasmin" or s3_li == "AJ":
        "Ciaran and Tai look at each other. They are the last boys left in the line-up."
        $ entering("ciaran")
        $ entering("tai")
        "Ciaran looks at his feet."
        ciaran sad "Well, bud, looks like this is the end of the line for us."
        show s3_mc_image sad
        tai surprised "Not so fast..."
        show s3_mc_image surprised
        show ciaran grimace
        tai neutral "Ciaran, we're both single now."
        tai cheeky "But we don't have to be."
        show s3_mc_image neutral
        tai smile "Why don't we give it a go?"
        if s3_mc.past_partners[2] == "Yasmin":
            ciaran surprised "Like Harry and Seb?"
            tai serious "That was a friendship couple..."
        ciaran grimace "Tai?"
        tai cheeky "Ciaran, I want this. I want this to happen."
        tai smile "When I'm around you, all I do is smile."
        tai blush "Basically, I have a huge crush on you."
        ciaran neutral "What are you saying, Tai?"
        show s3_mc_image surprised
        tai smile "I guess I'm asking, Ciaran, if you want to couple up with me?"
        "Ciaran flushes red, a smile forming on his lips."
        ciaran blush "Tai! I..."
        ciaran cheeky "I'd... I'd..."
        show s3_mc_image happy
        tai "Is that a yes?"
        ciaran happy "It's a yes!"
        "Tai grins and wraps Ciaran in his arms. Their embrace lasts for a long time. Ciaran's fingers curl into Tai's hair."
        "The rest of the Islanders explode into applause, Nicky is wolf-whistling and Yasmin is whooping loudly."
        "Ciaran and Tai sit down next to you and [s3_li]. You reach across and squeeze Ciaran's leg. He gives you a huge smile."

        # CHOICE
        menu:
            thought "Ciaran and Tai are coupled up!"
            "What a nice surprise!":
                pass
            "I knew there was something there":
                pass
            "I didn't see that coming":
                pass

        thought "I hope it works out for them!"
    s3_mc "Is that everyone all coupled up?"
    nicky happy "Looks like it."
    genevieve surprised "How are we feeling?"
    seb cheeky "I'm feeling great."
    "Viv beams at him. He whispers something in her ear and she nods."
    show s3_mc_image cheeky
    genevieve cheeky "I think we're going to go somewhere more private."
    "Seb pulls her away towards the daybeds, and she giggles."
    $ leaving("genevieve")
    $ leaving("seb")
    show s3_mc_image neutral
    "Slowly, the rest of the couples disperse."
    if s3_li == "Yasmin" or s3_li == "AJ":
        "Tai offers his hand to Ciaran, who takes it. They head towards the Villa, holding hands, already laughing about something."
    "When you're the last couple at the firepit, [s3_li] turns to you, smiling."
    s3_li cheeky "Hey."
    s3_mc happy "Hey."
    if s3_li == s3_mc.past_partners[0] or s3_li == s3_mc.past_partners[1]:
        s3_li happy "I'm so happy, I can't stop smiling."
        show s3_mc_image sad
        s3_li surprised "When [s3_mc.past_partners[2]] chose you, I felt my heart fall out of my chest."
        show s3_mc_image cheeky
        s3_li cheeky "And now you're back where you belong... with me."
    elif s3_li == s3_mc.past_partners[2]:
        s3_li surprised "I'm so thrilled that you picked me."
        show s3_mc_image sad
        s3_li sad "It was such a risk, splitting you up from [s3_mc.past_partners[1]]..."
        show s3_mc_image happy
        if s3_li != "Ciaran":
            s3_li smile "But it turns out it was the right thing to do, and that makes me so happy."
        else:
            s3_li happy "But it turns out it was the right thing to do, and that makes me so happy."
    else:
        show s3_mc_image happy
        s3_li happy "I'm so excited to finally be coupled up with you, I've been wanting this for so long."
        s3_li cheeky "To get to share a bed with you... feels like a dream come true."
    s3_li surprised "Look, I've got some stuff I want to say to you, away from everyone else."
    show s3_mc_image surprised
    s3_li cheeky "Stuff I've been wanting to say for a while."
    s3_li serious "Can we go somewhere more private?"
    # CHOICE
    menu:
        thought "Do I want to have a private chat with [s3_li]?"
        "I'd love to":
            s3_mc happy "That sounds wonderful."
            s3_li cheeky "Great! Let's go."
            $ s3_mc.like(s3_li)
            call s3e8p3_private_chat from _call_s3e8p3_private_chat
        "Sorry, I'm too sleepy":
            s3_mc sad "I'd love to, but I'm knackered."
            if s3_li != "Tai":
                s3_li @ sad "Aw, OK. We can just head to bed then."
            else:
                s3_li neutral "Aw, OK. We can just head to bed then."
            "You hold hands and walk back towards the Villa."


    scene s3-bedroom-night with dissolve
    $ new_scene()

    $ entering("s3_li_image")
    "You enter the bedroom with [s3_li]."
    "A few other couples are already there."
    if s3_li == "AJ" or s3_li == "Yasmin":
        "Tai and Ciaran are spooning, wrapped in a duvet, whispering quietly to each other."
        "Tai is the little spoon. He's beaming."
    else:
        "Genevieve and Seb are sitting up in bed, chatting. A spark is clearly visible between them."
        "Elladine and Nicky are already asleep in each other's arms."
    thought "I'd better put my pyjamas on."
    show s3_mc_image cheeky
    thought "Maybe I should wear something special to show [s3_li] that I'm into [him_her]..."
    
    # Outfit change to sleepwear
    $ outfit = "pjs"
    call customize_outfit from _call_customize_outfit_13
    
    s3_li happy "Hey, babe. Nice jammies."
    genevieve happy "So how are you two feeling?"
    seb cheeky "That's not fair, Viv. [s3_name] isn't coupled up with me, so clearly she's distraught."
    s3_mc cheeky "You're making him big-headed, Viv."
    s3_li surprised "Soon, he'll be too powerful."
    show s3_mc_image neutral
    seb "Oh, please. This isn't even my final form."
    "You get into bed with [s3_li]."
    if s3_li != s3_mc.past_partners[0] and s3_li != s3_mc.past_partners[1] and s3_li != s3_mc.past_partners[2]:
        s3_li happy "I'm excited to finally share a bed with you!"
    else:
        s3_li happy "Feels so good to be getting into bed with you again, babe."
    genevieve surprised "[s3_name]! I asked how you're feeling."
    genevieve cheeky "Before I was interrupted..."

    # CHOICE
    menu:
        thought "I'm feeling..."
        "Sad":
            # NEED TO FILL
            "EMPTY"
        "Relieved":
            s3_mc sad "I'm just happy all that drama's over."
            s3_li happy "Gosh, me too."
        "Happy":
            $ s3_mc.like(s3_li)
            s3_mc happy "I got who I wanted. I couldn't be happier."
            s3_li happy "I feel the same."
    genevieve surprised "Well, I'm ready to pass out. Night, you two."
    "Viv and Seb curl up together under the blanket."
    $ leaving("genevieve")
    show s3_mc_image neutral
    "You follow suit and get into bed with [s3_li]. [he_she!c] is warm under the duvet. You stick your foot out and stroke [his_her] leg."
    if s3_li != "Ciaran":
        s3_li smile "What do you say to a kiss goodnight?"
    else:
        s3_li happy "What do you say to a kiss goodnight?"
    if s3e8p3_bits == True:
        s3_mc cheeky "A kiss, after what we just did?"
        s3_li cheeky "Hey, I just can't get enough of you."
    show s3_mc_image happy

    # CHOICE
    menu:
        thought "A kiss goodnight..."
        "I'm tired":
            # NEED TO FILL
            "EMPTY"
        "Would be great":
            "[s3_li] smiles and lifts the duvet over the two of you."
            "[he_she!c] presses [his_her] lips to yours, kissing you slowly, full of emotion and tenderness."
            if s3_li != "Ciaran":
                s3_li smile "I'm so happy to be here with you, [s3_name]."
            else:
                s3_li smile "I'm so happy to be here with you, [s3_name]."
            show s3_mc_image happy
            s3_mc "Me too."
        "How about a snog?":
            "[s3_li]'s eyes light up."
            s3_li "Oh, hell yeah!"
            "[he_she!c] lifts the duvet over the two of you, before leaning in and kissing you with force."
            "[his_her!c] tongue glides against your bottom lip as [his_her] hands caress your body, and you let out a small moan."
            seb surprised "Hey! We can hear you!"
            "You giggle."
            $ leaving("seb")

    s3_li "We should go to sleep. It's been a long day."
    s3_mc sad "No doubt something else big will happen tomorrow."
    s3_li neutral "I don't want to think about that. I just want to think about how happy I am being here with you."
    s3_li happy "Let's just stay under this fluffy duvet forever."
    s3_mc happy "Sounds good to me."
    thought "This is my opportunity to get some cuddling in..."
    show s3_mc_image surprised

    # CHOICE
    menu:
        thought "What do I want to do?"
        "No cuddles":
            # NEED TO FILL
            "EMPTY"
        "Be the big spoon":
            "You wait until [s3_li] looks comfy, and then wrap your arms around [his_her] back."
            show s3_mc_image happy
            s3_li surprised "Hey! You're big-spooning me!"
            if s3_li == "Tai":
                s3_li smile "I've always wanted to be the little spoon! I feel so safe!"
            if s3_li == "Yasmin" or s3_li == "AJ":
                $ s3_mc.like(s3_li)
                s3_li smile "This is great. I feel so safe."
            else:
                $ s3_mc.like(s3_li)
                s3_li cheeky "I've never had a girl spoon me before. I like it!"
            show s3_mc_image neutral
            "You drift off to sleep, holding [s3_li] close."
        "Be the little spoon":
            $ s3_mc.like(s3_li)
            "You pull [s3_li]'s arm around you so [he_she]'s spooning you."
            show s3_mc_image happy
            s3_li cheeky "Ah, I love being the big spoon."
            if s3_li != "Ciaran":
                s3_li smile "Makes me feel like I can protect you from anything."
            else:
                s3_li happy "Makes me feel like I can protect you from anything."
            "You drift slowly off to sleep, [s3_li]'s arms around you, feeling like you're finally safe."
    
    scene sand with dissolve
    $ on_screen = []
    $ outfit = "swim"

    "Everyone's coupled up and no-one cried..."
    "I'd say that's a success, wouldn't you?"
    "Tomorrow on Love Island..."
    "It seems there's finally peace in the Villa..."
    s3_bff surprised "New Islanders?!"
    $ leaving("s3_bff_image")
    $ entering("s3_mc_image")
    s3_mc sad "This is gonna be bad..."
    $ leaving("s3_mc_image")

    "Kidding!"
    "'Peace in the Villa...' can't believe you fell for that."
    "Catch you next time."

    # jump s3e9p1
    return

label s3e8p3_private_chat:

    scene s3-gym-night with dissolve
    $ new_scene()

    "[s3_li] leads you to the gym."
    show s3_mc_image happy
    s3_li surprised "Everywhere else is occupied."
    s3_li blush "Are you OK hanging out here?"

    # CHOICE
    menu:
        thought "Having a romantic moment in the gym..."
        "It's a bit smelly":
            show s3_mc_image sad
            s3_li blush "Yeah, but it'll have to do."
            s3_li cheeky "Besides, I like the smell."
            show s3_mc_image cheeky
            s3_li "Who doesn't love a bit of sweat sometimes?"
        "It's romantic":
            show s3_mc_image cheeky
            s3_li surprised "You think the gym is romantic?"
            if s3_li == "Tai":
                s3_mc surprised "No! It's romantic that you want to spend time with me so much, you're willing to do it next to AJ's sweaty towel."
            else:
                s3_mc surprised "No! It's romantic that you want to spend time with me so much, you're willing to do it next to Tai's sweaty towel."
            if s3_li =="Ciaran":
                s3_li happy "Hey, all good relationships are about compromise."
            else:
                s3_li smile "Hey, all good relationships are about compromise."
        "Wanna lift some weights?":
            show s3_mc_image cheeky
            if s3_li == "Tai" or s3_li == "AJ":
                s3_li happy "Yeah!"
                "[he_she!c] lifts up a dumb-bell the size of your head and starts doing curls."
                show s3_mc_image angry
                "You frown at [him_her]."
                s3_li surprised "What?"
                s3_mc "I was kidding..."
                s3_li cheeky "Oh... I knew that."
                "[he_she!c] puts down the weights. You can tell [he_she]'s slightly disappointed."
            else:
                if s3_li != "Ciaran":
                    s3_li smile "I'd rather spend time with you."
                else:
                    s3_li happy "I'd rather spend time with you."
        
    show s3_li_image neutral
    show s3_mc_image neutral
    "You lie down with [him_her] on the yoga mats, facing each other under the stars. The breeze is cool, but you don't feel it."
    s3_li cheeky "You are so beautiful, [s3_name]."
    if s3_li != s3_mc.past_partners[0] and s3_li != s3_mc.past_partners[1] and s3_li != s3_mc.past_partners[2]:
        if s3_li != "Tai":
            s3_li sad "I've missed out on being coupled up with you before."
        else:
            s3_li neutral "I've missed out on being coupled up with you before."
        s3_li serious "Feelings are so hard to get a hold of in here. There is much uncertainty."
    else:
        show s3_mc_image sad
        s3_li sad "When we were coupled up last time, I didn't know how long it would last."
        s3_li serious "Things are always uncertain here, you know?"
    show s3_mc_image happy
    s3_li blush "But it seems like the only thing I can be certain of here... is you."

    if s3_li == "Bill":
        show s3_li_image happy
        "Bill smiles at you. He leans in and brushes your hair with his fingertips."
        "The heavy scent of his now familiar aftershave surrounds you."
        s3_li smile "Can I kiss you?"
        show s3_mc_image neutral
        
        # CHOICE
        menu:
            "Kiss him first":
                # NEED TO FILL
                "EMPTY"
            "Ask him a personal question instead":
                # NEED TO FILL
                "EMPTY"
            "Tell him to go ahead":
                "You reach up and put your arms around his neck."
                s3_mc cheeky "Be my guest."
                show s3_li_image cheeky
                "He kisses you hard and fast, and for a moment the world melts away, leaving just the two of you."
                "He kisses your neck, trailing down to your shoulder and across your collarbone, leaving goosebumps on your skin."
                "He pulls away and grins at you."
        
        show s3_li_image neutral
        show s3_mc_image neutral
        "Bill scratches his head, winces, and pulls a face."
        s3_li blush "Shoulder's a bit tight. Old injury. But a great story."
        s3_mc sad "Ooh, what happened?"
        s3_li surprised "OK, so I was on a job, right. We were patching up this old barn."
        s3_li neutral "It was in a right state. All rickety and broken. And it had rained, so the roof was dead slippery."
        show s3_mc_image surprised

        # CHOICE
        menu:
            thought "This sounds like a scene in a horror film..."
            "I don't want to hear the details":
                # NEED TO FILL
                "EMPTY"
            "I hope this is mega gruesome":
                # NEED TO FILL
                "EMPTY"
            "I had no idea roofing was so dangerous":
                show s3_mc_image sad
                s3_li surprised "It can be pretty dangerous business."
                s3_li neutral "Everyone in the business knows someone who knows someone with a nasty story."
        
        s3_li "But this one's not too nasty."
        s3_li "So anyway. There was also all this rusty farm machinery about."
        s3_mc surprised "You just said..."
        s3_li surprised "Just wait."
        s3_li neutral "So I'm working on the roof of this barn, and suddenly my foot slips and I fall off."
        s3_mc sad "Oh no!"
        s3_li happy "Luckily, I landed on a soft patch of grass. Bit bruised, but I was OK."
        s3_mc neutral "Phew."
        s3_li surprised "And then I got attacked by an ostrich."
        s3_mc surprised "Wait, what?"
        s3_li sad "It was an ostrich farm, and one of them got loose."
        show s3_mc_image neutral

        # CHOICE
        menu:
            thought "Bill got attacked by an ostrich..."
            "That's the funniest thing I've ever heard":
                show s3_mc_image happy
                s3_li surprised "Well, it wasn't at the time."
                s3_li happy "But after five years of my mates bringing it up down the pub, I started to see the funny side."
            "I bet it wasn't as funny as it sounds":
                show s3_mc_image surprised
                s3_li surprised "Yeah, it was bloody scary at that time."
                s3_li smile "I can see the funny side now, though."
            "Ostriches are terrifying":
                show s3_mc_image surprised
                s3_li surprised "Yeah, it was bloody scary at that time."
                s3_li smile "I can see the funny side now, though."
        
        show s3_mc_image happy
        show s3_li_image cheeky
        "He grins and winks at you. You're quiet for a moment."
        s3_li neutral "What are you so deep in thought about?"
        s3_mc cheeky "Wouldn't you like to know?"
    
    elif s3_li == "Harry":
        show s3_mc_image neutral
        s3_li surprised "Ow!"
        "He winces and rubs his eye."
        s3_mc surprised "What's up, babes?"
        s3_li sad "Something just went in my eye..."
        s3_li neutral "Could you take a look?"
        s3_mc neutral "Sure."
        "You move closer to him. He tilts his head towards you, his big, dark eyes wide."
        s3_li sad "Can you see anything?"
        show s3_mc_image sad

        # CHOICE
        menu:
            thought "I don't see anything... What should I do?"
            "Tell him it's extremely serious":
                # NEED TO FILL
                "EMPTY"
            "Flirt":
                "You put on a serious face."
                s3_mc neutral "There's something here."
                s3_li "What is it?"
                s3_mc cheeky "It's... the cutest guy I've ever seen."
                s3_li smile "Stop it, [s3_name]! You'll make me go all red."
                s3_mc happy "I think you're adorable when you blush. I can't see anything in your eye, by the way."
                s3_li neutral "I think I know what it was, anyway."
                s3_mc neutral "What was it?"
                s3_li happy "I was just blinded by how fit you are."
                s3_mc happy "You're such a melt."
                "You both laugh."
            "Kiss him":
                show s3_mc_image cheeky
                show s3_li_image smile
                "You close your eyes and move forward. He comes to meet you and your lips brush softly together."
                "For a moment, you both lose yourselves in a single perfect moment."
            
        "Harry smiles at you."
        s3_li smile "We're adorable, aren't we?"
        s3_mc happy "We are the adorablest."
        s3_li happy "There is no way we won't win this whole thing."
        show s3_mc_image neutral

        # CHOICE
        menu:
            thought "Harry seems pretty convinced we're going to win..."
            "We've got some stiff competition":
                # NEED TO FILL
                "EMPTY"
            "Of course we will":
                show s3_mc_image happy
                "You grin at Harry, and hold your hand up for a high five."
                "He doesn't leave you hanging."
            "It'll be OK if we don't, though":
                s3_mc "Sure, that'd be nice."
                s3_mc "I won't mind if we don't, though."
        
        s3_li angry "I'm actually going to be really annoyed if we don't win."
        s3_mc surprised "Sure, but, there's more to it than just winning."
        s3_li serious "I told myself I was gonna focus on finding love, but I can't help it. I just can't shut off my competitive streak."
        show s3_mc_image neutral

        # CHOICE
        menu:
            thought "What is there apart from winning?"
            "Making friends":
                # NEED TO FILL
                "EMPTY"
            "Nothing. Winning is everything":
                # NEED TO FILL
                "EMPTY"
            "Finding love":
                "You reach out and touch the back of Harry's hand. He brushes your hand with his fingers and smiles."
                s3_li surprised "Yeah, I'm not saying that's not a big part of it."
                s3_li angry "But this is a competition. If I don't win I'll feel like it was a bit of a waste."
                "He shrugs."
                s3_li neutral "That's just who I am."
                s3_mc sad "Thanks..."
                s3_li surprised "No, that's not what I'm saying! I love being here with you, and I'm so glad I met you."
                s3_li angry "But a part of me needs to win."
        
        s3_li sad "I.. I sort of wish I wasn't like that, though."
        s3_mc happy "Why don't we just try and enjoy the time that's left and not even think about the final?"
        s3_li happy "OK, I can try that."
        "He wraps his arms around you and squeezes."
    
    elif s3_li == "Camilo":
        s3_li smile "I was looking forward to getting you to myself again."
        s3_li cheeky "You look absolutely stunning, [s3_name]. I really want to kiss you right now."

        # CHOICE
        menu:
            thought "Camilo wants to kiss me..."
            "Make him work for it":
                # NEED TO FILL
                "EMPTY"
            "Get him to tell you a story instead":
                # NEED TO FILL
                "EMPTY"
            "Let him kiss you":
                s3_mc cheeky "Come and get it."
                "Camilo envelops you in his arms and kisses you deeply on the mouth."
                "He runs his hands down your body as his lips trail down your neck and over your collarbones."
        
        s3_li happy "You're amazing, you know that?"
        s3_li smile "I fancy the pants off you, but it's like... you're also a mate."
        s3_mc happy "I like that."
        s3_li neutral "And that's kinda new to me. Like, relationships come and go, but friends are there forever."
        s3_mc sad "Well, not always. People drift apart, or you ghost them or whatever."
        s3_li surprised "You've ghosted friends before?"
        show s3_mc_image neutral

        # CHOICE
        menu:
            thougth "Have I ever ghosted a friend?"
            "No, I've never done that myself":
                # NEED TO FILL
                "EMPTY"
            "Yes, loads. No mercy":
                s3_mc sad "Yeah, hasn't everyone? Some people are just toxic."
                s3_mc neutral "It's not my responsibility to keep those in my life, you know?"
                s3_li sad "Yeah."
            "Sometimes you have to":
                s3_mc sad "I didn't like it, but sometimes people just turn out to be toxic."
                s3_mc neutral "I need to protect my peace, you know?"
                s3_li sad "Yeah."
        
        s3_mc "So have you cut people out of your friendship group back home?"
        s3_li blush "Yes. No. Kinda."
        s3_li "There was this guy. Er, he might be watching so I'm gonna call him... Bonathan."
        s3_mc surprised "Is... is his name just Jonathan?"
        s3_li surprised "Oh bloody-"
        s3_li blush "Yeah."
        show s3_mc_image neutral
        s3_li neutral "He started seeing Kayla, Tall Dave's ex. Serious violation of the bro code, innit."
        s3_li "Then Monster Munch had a party and invited Jonathan, and Jonathan brought Kayla to the party."
        s3_mc surprised "Hang on, you have a mate called Monster Munch?"
        s3_li happy "His real name's Adnan, but nobody uses their real name, do they?"
        s3_mc cheeky "Jonathan does, apparently."
        s3_li smile "Nah, his nickname is Greasy Jonno."
        s3_mc surprised "That's not a very nice nickname!"
        s3_li surprised "Oh, no. It's 'cause one time he went to Greece."
        show s3_mc_image neutral

        # CHOICE
        menu:
            s3_mc "That nickname is..."
            "Very silly":
                # NEED TO FILL
                "EMPTY"
            "Like my friend Mushroom Kate":
                s3_mc happy "Her brother was Mushroom Paul, because he had a haircut like a mushroom. She inherited the title, I guess."
                s3_mc neutral "She had a normal haircut, though."
            "Like my friend Lipstick":
                s3_mc happy "We started calling him that in primary school because he stuck his lips together with glue."
            
        s3_li neutral "Anyway, so everyone wanted to cut Greasy Jonno out."
        s3_li serious "But I knew that him and Kayla, it wasn't like some fling, you get me? They were in love and that."
        s3_li smile "So I tried to get them to see that. And now Greasy Jonno is mates with everyone again."
        s3_li happy "I think sometimes you just need to give peeps a time out, innit."
        s3_mc sad "No chance of that in here..."
        s3_li neutral "Is there someone you'd wanna cut out in the Villa?"

        # CHOICE
        menu:
            "I wouldn't rule it out in future":
                # NEED TO FILL
                "EMPTY"
            "One or two names spring to my mind...":
                # NEED TO FILL
                "EMPTY"
            "No, I think everyone's great":
                s3_mc happy "Oh, no way. I'm actually surprised at how well I'm getting on with the people in here."
                s3_li happy "Right? They've been ups and downs but no really bad drama."
        
        s3_li smile "I actually think there are a couple of people I'm gonna stay mates with after the show's over. That's like the opposite."
        s3_mc cheeky "Am I included in that?"
        "He scoops an arm around your waist and pulls you in."
        s3_li cheeky "Absolutely."

    elif s3_li == "AJ":
        "AJ leans her head on your shoulder."
        s3_li smile "You're so comfy."
        s3_mc happy "Oh, yeah?"
        s3_li cheeky "Yeah."
        s3_li neutral "I love it when a person is, like, proper comfy."
        s3_li smile "And it looks like I've found that in you."
        show s3_mc_image neutral

        # CHOICE
        menu:
            thought "I should..."
            "Say I'm not a human pillow":
                # NEED TO FILL
                "EMPTY"
            "Call AJ comfy too":
                show s3_mc_image happy
                "AJ smiles and leans in closer towards you."
            "Kiss her!":
                show s3_mc_image happy
                "You tilt her face up towards you. She leans in closer."
                "Your lips touch."
                "The world disappears."
                "You move away."
                "She starts playing with her hair shyly."
                $ s3_mc.like(s3_li)
                s3_li cheeky "OK, so not only have I found my comfy human pillows and my potential soulmate..."
                s3_li "But I've also found someone that kisses me like..."
                s3_li smile "That."
                s3_li blush "Woah."
                s3_li cheeky "Amazing."
                "She rests her head on your shoulder."
                s3_li smile "Today is a good day."
        
        s3_li neutral "Do you ever have those feels where you think you're reliving a moment that you're already like, lived?"
        s3_mc surprised "Like déjà vu?"
        s3_li surprised "I guess, if that's what it's called!"
        s3_li serious "Is that French or..."
        s3_mc happy "Yeah, it means 'already seen'."
        s3_li happy "That's so cool!"
        s3_li serious "And, like, profound."
        s3_li neutral "But, yeah, have you ever had that before?"
        s3_li smile "When you feel like you've already seen something?"
        show s3_mc_image neutral

        # CHOICE
        menu:
            thought "Do I get déjà vu?"
            "No, never":
                # NEED TO FILL
                "EMPTY"
            "I'm having it right now":
                s3_li surprised "Me too! I'm having it right now!"
            "Yeah, all the time":
                s3_li surprised "Me too! I'm having it right now!"
        
        show s3_mc_image surprised
        s3_li smile "For real."
        s3_li neutral "It feels like I've met you before, like, maybe in another life."
        s3_li smile "You're familiar."
        show s3_mc_image happy
        s3_li blush "But it's a good familiar, not like a boring one."
        show s3_mc_image neutral

        # CHOICE
        menu:
            thought "AJ says we've met before..."
            "So you're a time traveller?":
                # NEED TO FILL
                "EMPTY"
            "I better not be boring you":
                # NEED TO FILL
                "EMPTY"
            "Maybe we're soulmates":
                show s3_mc_image happy
                $ s3_mc.like(s3_li)
                s3_li smile "I think you're right."
        
        s3_li neutral "I reckon that's why I feel so comfortable around you."
        show s3_mc_image neutral
        s3_li smile "Because we've already done all this before, or we're doing it again."
        s3_li happy "That doesn't mean I don't think it's new or exciting, but it's a different kind of excitement."
        s3_li smile "Like we're meant to be together, you get me?"

        # CHOICE
        menu:
            thought "AJ thinks we're meant to be together!"
            "You're so cute when you get complicated":
                # NEED TO FILL
                "EMPTY"
            "Are you saying alternative realities exist?":
                # NEED TO FILL
                "EMPTY"
            "I totally think the same!":
                s3_mc happy "We're obviously meant to be together."
                s3_li serious "But, you know what, I don't want fate to choose for me."
                s3_li sad "Because that feels like it isn't as special or something."
                s3_li neutral "I want to do the choosing."
                s3_mc surprised "What do you mean?"
                s3_li blush "I'm not sure anymore."
                "She grins and laughs at herself, leaning onto your shoulder again."
                show s3_mc_image happy
                s3_li smile "I just know that right here is where I want to be."

    elif s3_li == "Tai":
        "Tai stretches his arms, rolling his neck slowly and easing out his muscles."
        "As you shift nearer, he sighs happily. His body is so close to yours."

        # CHOICE
        menu:
            thought "Tai looks so hot right now..."
            "Tickle him":
                # NEED TO FILL
                "EMPTY"
            "Stroke his hair":
                show s3_mc_image cheeky
                show s3_li_image cheeky
                "You reach out and run your fingers through his hair. That familiar sandalwood smell wafts over you."
                "Tai's eyes half-close and he grins sleepily, looking like an incredibly satisfied cat."
                $ s3_mc.like(s3_li)
                s3_li happy "That feels so amazing."
            "Kiss him":
                show s3_mc_image cheeky
                show s3_li_image cheeky
                "While Tai's still stretching, you lean in and kiss him. He grins against your mouth and wraps his arms around you."
                "He kisses you back eagerly, then brushes his lips lightly along your jawline."
                $ s3_mc.like(s3_li)
                s3_li happy "You feel so amazing."
        
        show s3_mc_image neutral
        "He stretches out his arms again, and his shoulder clicks."
        s3_li neutral "You see? You can always do with a stretch."
        s3_li surprised "Speaking of, does any bit of you need TLC?"
        s3_mc surprised "What did you have in mind?"
        "Tai draws so close that you can see each of his long eyelashes. He cocks his head cheekily."
        s3_li smile "A little massage."
        s3_li "A Tai massage, if you will."
        s3_mc cheeky "You're so cheesy."
        s3_li happy "Well, we don't want your muscles getting sore."
        show s3_mc_image neutral

        # CHOICE
        menu:
            thought "Tai's offering me a massage..."
            "I'm good for now":
                # NEED TO FILL
                "EMPTY"
            "My feet could do with a rub":
                # NEED TO FILL
                "EMPTY"
            "My shoulders are a bit tight":
                s3_mc sad "I hunched over my phone a bit too long last time the texts came in."
                s3_mc "My shoulders could do with some attention."
                show s3_mc_image happy
                s3_li happy "Happy to help. Always."
                "Tai starts rubbing your shoulders, lightly at first, his fingers seeking out any spots of tension."
                show s3_mc_image neutral
                "Tai's voice is low and soft."
                s3_li smile "Feeling good?"

                # CHOICE
                menu:
                    thought "Tai's wondering if the massage is feeling good..."
                    "Lighter!":
                        # NEED TO FILL
                        "EMPTY"
                    "That's perfect":
                        "Tai carries on massaging, his movements focused."
                    "More pressure!":
                        s3_mc "I like more force."
                        s3_li cheeky "You're saying you like it hard?"
                        s3_li smile "My pleasure."
                
                s3_mc cheeky "I could do this for hours."
                
            "I'm getting a twinge in my glutes":
                show s3_mc_image cheeky
                s3_li cheeky "Ooh, now that sounds like fun."
                "He winks, then puts on a very serious frown."
                s3_li happy "The gluteus maximus is very important for supporting your lower back."
                s3_li cheeky "And in your case, it's also pure flames."
                "Tai starts rubbing your lower back, lightly at first, his fingers seeking out any spots of tension."
                "Slowly, his hands drift downwards."
                "Tai's voice is low and soft."
                s3_li neutral "Feeling good?"
                show s3_mc_image neutral

                # CHOICE
                menu:
                    thought "Tai's wondering if the massage is feeling good..."
                    "Lighter!":
                        # NEED TO FILL
                        "EMPTY"
                    "That's perfect":
                        show s3_mc_image cheeky
                        "Tai carries on massaging, his movements focused."
                    "More pressure!":
                        s3_mc cheeky "I like more force."
                        s3_li cheeky "You're saying you like it hard?"
                        s3_li happy "My pleasure."
                
                s3_mc cheeky "I could do this for hours."
                
        s3_li happy "Well, if you ever want a massage another time, all you need to do is ask."
        s3_li smile "Or tell me, I don't mind."
        s3_li "Sometimes being told what to do can be fun."
        show s3_mc_image surprised

        # CHOICE
        menu:
            thought "Tai likes being told what to do!"
            "I prefer being chill":
                # NEED TO FILL
                "EMPTY"
            "I like taking the lead":
                show s3_mc_image cheeky
                s3_li happy "Get the handcuffs out, eh?"
                s3_li smile "Honestly, I'm good with whatever. "
            "I'm happy either way":
                show s3_mc_image happy
                $ s3_mc.like(s3_li)
                s3_li smile "Honestly, I'm good with whatever."

        show s3_mc_image neutral    
        s3_li cheeky "It's the person who matters."
        "He stretches again, then winces."
        s3_li surprised "Or I do, but it's with a physio. So it's different."
        s3_li neutral "But I've got a bit of a crick in my shoulder. If you could give it a rub, that's be amazing."

        # CHOICE
        menu:
            thought "Should I give Tai a shoulder massage?"
            "I don't feel in the mood":
                # NEED TO FILL
                "EMPTY"
            "Maybe I could massage somewhere else":
                s3_mc cheeky "You know, your calves, or thighs."
                s3_mc "Or somewhere a little further up."
                s3_li cheeky "Now that's a plan."
                s3_li smile "But could you start with my shoulders for now?"
                s3_mc happy "My hands are at the ready!"
                "You lay a hand on Tai's shoulder, feeling the strength of his muscles beneath his skin."
                show s3_li_image neutral
                show s3_mc_image neutral
                "As you rub with your thumbs in small circles, you seek out any spots of tension."
                "Tai makes a deep, satisfied noise in the back of his throat. It almost sounds like a purr."
                s3_mc happy "Hope you're not falling asleep."
                s3_li cheeky "No way. I couldn't miss this."
                s3_li smile "That is amazing."
                show s3_mc_image neutral
                thought "Tai's loving his massage."
                show s3_mc_image cheeky

                # CHOICE
                menu:
                    thought "Shall I make it a bit naughty?"
                    "I'll stay on the shoulders": 
                        # NEED TO FILL
                        "EMPTY"
                    "I'll go for it":
                        "You whisper in Tai's ear, your breath against his skin."
                        s3_mc "Would you like my hands anywhere else?"
                        s3_li cheeky "You know I do."
                        "Your hands drift down Tai's back, down his shoulder blades, down to his hips."
                        "His breath shudders as you stroke his skin, and he leans back against you, eager for your touch."
                        s3_li happy "You... [s3_name]... that's..."
                        s3_mc "Never thought I'd see you lost for words."
                        s3_li cheeky "Mmm..."
            "Let me at those muscles":
                s3_mc happy "My hands are at the ready!"
                s3_li smile "Aww, that's so nice."
                s3_li "Normally, I'm the one doing it."
                show s3_mc_image neutral
                "You lay a hand on Tai's shoulder, feeling the strength of his muscles beneath his skin."
                "As you rub with your thumbs in small circles, you seek out any spots of tension."
                "Tai makes a deep, satisfied noise in the back of his throat. It almost sounds like a purr."
                s3_mc cheeky "Hope you're not falling asleep."
                s3_li cheeky "No way. I couldn't miss this."
                s3_li smile "That is amazing."
                thought "Tai's loving his massage."

                # CHOICE
                menu:
                    thought "Shall I make it a bit naughty?"
                    "I'll stay on the shoulders": 
                        # NEED TO FILL
                        "EMPTY"
                    "I'll go for it":
                        "You whisper in Tai's ear, your breath against his skin."
                        s3_mc cheeky "Would you like my hands anywhere else?"
                        s3_li cheeky "You know I do."
                        "Your hands drift down Tai's back, down his shoulder blades, down to his hips."
                        "His breath shudders as you stroke his skin, and he leans back against you, eager for your touch."
                        s3_li blush "You... [s3_name]... that's..."
                        s3_mc "Never thought I'd see you lost for words."
                        s3_li "Mmm..."
    
    elif s3_li == "Ciaran":
        s3_li grimace "Woah."
        s3_mc surprised "You OK?"
        s3_li sad "Sorry. Just a pang of homesickness."
        s3_li "Started thinking about my dog."
        s3_li neutral "I wish I could give her a pet right now."
        show s3_mc_image neutral

        # CHOICE
        menu:
            thought "Ciaran wants to pet his dog."
            "You can pet me":
                # NEED TO FILL
                "EMPTY"
            "I don't like dogs":
                # NEED TO FILL
                "EMPTY"
            "That's sweet":
                s3_mc happy "All these people in swimwear, you're thinking about your dog. It's cute."
                s3_li grimace "It is?"
                s3_li "I thought it was a bit sappy, but cute works too!"
        
        s3_li happy "Captain Kerry and I are best pals, y'know."
        s3_li neutral "Whoever says dogs don't have personalities are clearly cat people."
        s3_mc surprised "Captain Kerry?"
        s3_li grimace "Oh... did I call her that?"
        s3_li "Forget I said anything. Just a mistake."
        show s3_mc_image neutral

        # CHOICE
        menu:
            thought "Ciaran called his dog Captain..."
            "Is she your superior?":
                # NEED TO FILL
                "EMPTY"
            "Like Captain America, but for Ireland?":
                s3_li blush "Uh, sure! That's totally what I meant."
            "Does she have a ship?":
                s3_li blush "Um, not, it's not like..."
                "He trails off."
        
        s3_mc angry "Ciaran, what are you hiding?"
        "Ciaran puffs his cheeks up and blows them out."
        s3_li sad "OK. You're going to think this is silly."
        s3_li grimace "Or maybe not... it's a chance I have to take."
        show s3_mc_image neutral
        s3_li sad "Being a bouncer is a lot of standing around. And there's only so much social media you can scroll through."
        s3_li blush "So... I kind of started writing short stories on my Notes app."
        s3_li "About me. And my dog. Going on adventures."
        show s3_mc_image surprised
        
        # CHOICE
        menu:
            s3_mc "Oh, wow. That's..."
            "So funny":
                # NEED TO FILL
                "EMPTY"
            "So cute!":
                s3_mc happy "That's adorable."
                s3_mc "I didn't know you were a writer."
                s3_li "Oh, I'm not! Definitely not. They've probably got loads of mistakes. I've got rubbish grammar."
                s3_li cheeky "That's all I've written, really."
            "Absolutely incredible":
                s3_mc happy "That's the greatest thing I've ever heard."
                s3_mc "Hands down."
                s3_li happy "I'm glad you think so!"

        s3_mc neutral "If she's Captain Kerry, what are you?"
        s3_li neutral "..."
        s3_li grimace "Ciaran-man."
        s3_mc happy "You're the cutest."
        s3_mc "Can I read one?"
        s3_li happy "Well, I don't have my phone right now. But you can when we're out of the Villa."
        s3_li sad "They're not good, though."
        show s3_mc_image neutral

        # CHOICE
        menu:
            thought "Ciaran doesn't think his stories are good."
            "I'm sure they're good":
                s3_mc happy "You're a smart guy, and so creative. I'm sure they're great."
                s3_mc neutral "Even if it's not, it doesn't matter to me."
            "I don't care":
                s3_mc happy "Ciaran, I don't care if they're not Shakespeare."
                s3_mc angry "That guy's overrated anyway. Hasn't put anything out in years."
        
        s3_mc happy "I care about you, so I want to read them."
        s3_li surprised "That means so much to me."
        s3_li "I've never shared them with anyone, but I'm really excited about sharing them with you."
        s3_li happy "That's a good sign, right?"
        s3_mc neutral "Definitely."
        "He gives you a small smile, and you feel butterflies in your stomach."
        "The wind catches his hair, blowing it into his face. He pushes it back."
        "You feel something stir inside you."

        # CHOICE
        menu:
            thought "I want to..."
            "Straddle him":
                # NEED TO FILL
                "EMPTY"
            "Tell him how I feel":
                # NEED TO FILL
                "EMPTY"
            "Kiss him":
                "His hair falls in his face again, despite his best efforts."
                s3_li sad "Damn pomade, never holds."
                s3_mc "Let me get that for you..."
                "You move forward, running your hand through his hair and keeping it there."
                s3_li happy "Thanks."
                s3_mc cheeky "No problem."
                "You lean forwards and press your lips to his. His teeth clash with yours and neither of you can keep from smiling."
                "He cups your face with his strong hands, while you run your fingertips across his back."
                s3_li surprised "That tickles!"
                s3_mc neutral "In a good way?"
                s3_li cheeky "Yeah, in a good way."
        
        "You smile at each other, and the butterflies continue."
        
    elif s3_li == "Yasmin":
        show s3_mc_image neutral
        show s3_li_image neutral
        "It takes a moment to notice that Yasmin's stroking the back of your hand with her thumb again."
        s3_mc "There you go again."
        s3_li blush "What do you mean?"
        "You demonstrate by doing it back to her."
        "Her skin is soft and smooth, and her hand is small and pretty. Her purple nails catch the light."
        s3_mc cheeky "This. You keep doing it when we're alone together."
        s3_li "Oh, that..."
        s3_li neutral "It's just a way of, like ...letting you know I'm here, if that makes any kind of sense."
        s3_li cheeky "And I really like to feel how soft your skin is. Is that weird?"
        show s3_mc_image neutral

        # CHOICE
        menu:
            thought "The thing Yasmin does with her thumb..."
            "It's a bit annoying":
                # NEED TO FILL
                "EMPTY"
            "I'd rather see what you can do with your fingers..":
                show s3_mc_image cheeky
                s3_li cheeky "Naughty, [s3_name]."
                "You pretend to look innocent."
                s3_mc happy "What? I meant I can't wait to see you play bass!"
                s3_li smile "Sure, girl, sure."
            "I like it":
                s3_mc happy "It's comforting."
                s3_li smile "I'm glad."
        
        show s3_mc_image neutral
        s3_li cheeky "I guess playing different instruments has got me used to using my hands a lot."
        s3_li sad "But here there's no strings, no keys, nothing to keep my hands busy..."
        "She runs her hands lightly down your arms and bites her lip."
        s3_li smile "Except you, of course."
        show s3_mc_image surprised
        
        # CHOICE
        menu:
            thought "Yasmin's got restless hands..."
            "Move them away":
                # NEED TO FILL
                "EMPTY"
            "Move them to your hair":
                # NEED TO FILL
                "EMPTY"
            "Move them to your waist":
                show s3_mc_image neutral
                "You guide her hands down. They settle on your waist before gliding around to your lower back."
        
        s3_li smile "Even this close, it feels like I can't get close enough."
        s3_li cheeky "You're a hell of a girl, [s3_name]."
        show s3_mc_image cheeky

        # CHOICE
        menu:
            thought "Yasmin called me a hell of a girl..."
            "You hardly even know me yet":
                # NEED TO FILL
                "EMPTY"
            "You're the one who's amazing":
                show s3_mc_image happy
                s3_li smile "We make a pretty good pair, then, huh?"
                s3_mc "I guess we do."
            "I prefer to think of myself as a little piece of heaven":
                show s3_mc_image happy
                s3_li cheeky "Oh, I bet you are."
    show s3_mc_image happy
    if s3_li == "Bill" or s3_li == "Harry" or s3_li == "Camilo" or s3_li == "AJ":
        s3_li cheeky "How would you feel about some reunion bits?"
    else:
        s3_li cheeky "How about some celebratory bits?"
    show s3_mc_image surprised

    # CHOICE
    menu:
        thought "Do I want to do bits with [s3_li]?"
        "I'd rather talk":
            s3_mc neutral "I'd rather talk. I love hearing what you have to say."
            if s3_li != "Ciaran":
                s3_li smile "That sounds great."
            else:
                s3_li neutral "That sounds great."
        "Let's get it on!":
            $ s3e8p3_bits = True
            show s3_mc_image cheeky
            "You look [him_her] in the eyes, smiling. [he_she!c] leans forward and kisses you."
            "[his_her!c] lips are soft and gentle, but quickly grow urgent as [he_she] pulls you on top of [him_her]."

            # CHOICE
            menu:
                thought "Do I want to take this all the way?"
                "Nah":
                    # NEED TO FILL
                    "EMPTY"
                "Hell yes!":
                    $ s3_mc.like(s3_li)
                    "You continue kissing [s3_li], harder and faster, your breathing growing heavier."
                    if s3_li != "AJ" and s3_li != "Yasmin":
                        "A line of slick sweat forms between your bodies. [s3_li] reaches into his pocket and pulls out a condom."
                        s3_mc happy "You're so sexy when you're well prepared."
                    else:
                        "A line of slick sweat forms on your skin, as [s3_li]'s hands start to roam your body."
                    "When you start moving against each other, [s3_li]'s eyes flutter closed as [he_she] twirls [his_her] fingers into your hair."
                    s3_li "[s3_name]..."
                    "[he_she!c] pulls your hair slightly, a delicious feeling that forces a soft moan out of you."
                    "When it's over, you lay next to each other, breathless, staring up at the stars, your fingers interlaced."
                    s3_li surprised "Well, that was a workout."
                    s3_mc cheeky "A high intensity one."
                    s3_li happy "A cardio blast."
                    s3_mc "Glute-concentrated."
                    s3_li blush "My inner thighs are burning."
                    s3_mc happy "Maybe I can give you a sports massage."
                    s3_li cheeky "I may take you up on that later."
    show s3_mc_image happy
    if s3_li != "Ciaran":
        s3_li smile "This all turned out exactly like I hoped."
    else:
        s3_li happy "This all turned out exactly like I hoped."

    if s3_li == "Bill":
        s3_li surprised "You're like, my dream girl, you know that?"
        s3_li cheeky "You're strong, beautiful, and you eat with your mouth closed."
        s3_mc cheeky "Wow, what high standards."
        s3_li surprised "You'd be surprised. Seriously."
        show s3_mc_image happy
        s3_li neutral "But yeah, you're special, alright."
    elif s3_li == "Harry":
        s3_li surprised "Have you seen that old movie, 'Hitch'? It's a classic."
        s3_li "It's that one where Will Smith runs a business as a dating coach, getting geeky dudes together with hot girls."
        s3_li happy "When I saw that movie, I thought, that looks easy, I could do that."
        s3_li serious "I legit thought about setting up a similar business."
        s3_li happy "'Zhong' is a much cooler name for a movie than 'Hitch', don't you think?"
        s3_li blush "But wow, I do not have the capacity for that."
        s3_li sad "I find you, a girl I actually like, and my bum starts sweating every time you even look at me."
        s3_mc happy "That's cute."
        s3_li surprised "I'm glad you think so. I'm learning a lot about myself with you, [s3_name]."
    elif s3_li == "Camilo":
        s3_li smile "Chica, you are so surprising."
        s3_li sad "I thought for sure you'd stay with [s3_mc.past_partners[2]]."
        show s3_mc_image happy
        s3_li cheeky "I guess you couldn't resist this Colombian charm..."
        s3_li smile "But, yeah. I'm seriously so happy."
    elif s3_li == "AJ":
        s3_li surprised "I just wish I'd picked you before you picked me!"
        show s3_mc_image cheeky
        s3_li serious "I want you to know how into you I am."
        s3_mc surprised "Let's do it again then. AJ, you've got a text!"
        "You mimic the text tone. AJ giggles."
        s3_li surprised "Ooh, a text? I get to pick first!"
        show s3_mc_image sad
        s3_li cheeky "I want to couple up with this girl because she's super cool, hot, and makes me feel all melty inside."
        show s3_mc_image happy
        s3_li smile "It's [s3_name]!"
        s3_mc cheeky "Oh em gee! I can't believe you picked me!"
    elif s3_li == "Tai":
        s3_li surprised "It's such a boost to the ego, a beautiful girl choosing you over five other lads."
        s3_mc neutral "Don't let your head get too big."
        s3_li neutral "I won't. I'll get a helmet."
        show s3_mc_image cheeky 
        s3_li "Although, if we end up in the final, it'll crack."
        show s3_mc_image sad
        s3_li "I can't wait to get out of this place with you. Take you on some real dates."
        s3_mc happy "I can't wait, either."
    elif s3_li == "Ciaran":
        show s3_mc_image cheeky
        s3_li cheeky "I feel so fuzzy, knowing you chose me over the others."
        s3_li sad "When we were coupled up before, I was the one that picked you, so I could never be sure that you were into me."
        s3_li grimace "I've been thinking about this for ages, and how much I hoped you'd pick me."
        show s3_mc_image sad
        s3_li blush "Sometimes I dream about it..."
        show s3_mc_image surprised
        s3_li grimace "Sorry, is that weird?"
        s3_mc happy "It's cute!"
        s3_li happy "Oh, good."
    elif s3_li == "Yasmin":
        s3_mc cheeky "I can't believe you were nervous."
        s3_li surprised "Well, you make me feel that way."
        s3_li blush "I've never thought about someone so much before. I had a dream about you last night."
        s3_mc surprised "What happened?"
        s3_li sad "I was watching you use the toilet..."
        s3_mc angry "Oh. OK?"
        s3_li smile "But I read in a book once it means I feel intimate with you."
        s3_mc surprised "How long did the dream last?"
        s3_li blush "I don't wanna talk about it."
        s3_mc happy "Play your cards right, your dream could become a reality!"
    show s3_mc_image happy
    s3_li neutral "It's getting late. We should head to bed."
    "[he_she!c] offers you [his_her] hand."
    show s3_mc_image cheeky

    # CHOICE
    menu:
        thought "Do I..."
        "High five it":
            # NEED TO FILL
            "EMPTY"
        "Take it":
            show s3_mc_image happy
            if s3_li != "Ciaran":
                show s3_li_image smile
            else:
                show s3_li_image happy
            "You lace your fingers between [s3_li]'s. [his_her!c] hand is warm, and you smile at each other before heading towards the Villa."
    return