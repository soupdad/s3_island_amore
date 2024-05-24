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
            call s3e7p1_help_camilo
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